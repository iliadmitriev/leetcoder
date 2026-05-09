import argparse
import logging
import os
import re
import time
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

DAILY_CHALLENGE_QUERY = """
query questionOfToday {
    activeDailyCodingChallengeQuestion {
        date
        link
        question {
            titleSlug
            title
            questionFrontendId
        }
    }
}
"""

SOLVED_PROBLEMS_QUERY = """
query userProgressQuestionList($filters: UserProgressQuestionListInput) {
  userProgressQuestionList(filters: $filters) {
    totalNum
    questions {
      frontendId
      title
      titleSlug
    }
  }
}
"""

SUBMISSIONS_QUERY = """
query($offset: Int!, $limit: Int!, $slug: String) {
  submissionList(offset: $offset, limit: $limit, questionSlug: $slug) {
    hasNext
    submissions {
      id
      lang
      timestamp
      statusDisplay
      title
      titleSlug
    }
  }
}
"""

SUBMISSION_DETAILS_QUERY = """
query submissionDetails($id: Int!) {
  submissionDetails(submissionId: $id) {
    code
  }
}
"""


def get_headers(session_cookie: str, csrf_token: str) -> dict:
    return {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={session_cookie}; csrftoken={csrf_token}",
        "x-csrftoken": csrf_token,
        "Referer": "https://leetcode.com/profile/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }


def graphql_post(headers, payload, retries=5, backoff=2):
    for attempt in range(1, retries + 1):
        try:
            resp = requests.post(LEETCODE_GRAPHQL_URL, headers=headers, json=payload)
            resp.raise_for_status()
            return resp
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt == retries:
                raise
            wait = backoff * attempt
            tqdm.write(f"  ⚠️ Retry {attempt}/{retries} after {e.__class__.__name__} ({wait}s)")
            time.sleep(wait)


def to_kebab_case(title: str) -> str:
    kebab = re.sub(r"[\s_\-]+", "-", title.lower())
    kebab = re.sub(r"[^a-z0-9-]", "", kebab)
    return kebab.strip("-")


def map_language(lang_slug: str) -> dict:
    mapping = {
        "cpp": {"folder": "cpp", "ext": "cpp"},
        "python3": {"folder": "python", "ext": "py"},
        "python": {"folder": "python", "ext": "py"},
        "golang": {"folder": "golang", "ext": "go"},
        "java": {"folder": "java", "ext": "java"},
        "javascript": {"folder": "js", "ext": "js"},
        "typescript": {"folder": "ts", "ext": "ts"},
        "rust": {"folder": "rust", "ext": "rs"},
    }
    return mapping.get(lang_slug, {"folder": lang_slug, "ext": "txt"})


def fetch_daily_challenge():
    resp = requests.post(
        LEETCODE_GRAPHQL_URL,
        json={"query": DAILY_CHALLENGE_QUERY},
    )
    resp.raise_for_status()
    data = resp.json()
    q = data["data"]["activeDailyCodingChallengeQuestion"]["question"]
    return {
        "titleSlug": q["titleSlug"],
        "frontendId": q.get("questionFrontendId", ""),
        "title": q.get("title", q["titleSlug"]),
    }


def fetch_solved_problems(headers):
    problems = []
    limit, skip = 100, 0

    resp = graphql_post(
        headers,
        {
            "query": SOLVED_PROBLEMS_QUERY,
            "variables": {
                "filters": {"skip": 0, "limit": 1, "questionStatus": "SOLVED"}
            },
        },
    )
    resp.raise_for_status()
    total = (
        resp.json()
        .get("data", {})
        .get("userProgressQuestionList", {})
        .get("totalNum", 0)
    )

    pbar = tqdm(total=total, desc="Fetching solved problems", unit=" problems")

    while True:
        resp = graphql_post(
            headers,
            {
                "query": SOLVED_PROBLEMS_QUERY,
                "variables": {
                    "filters": {
                        "skip": skip,
                        "limit": limit,
                        "questionStatus": "SOLVED",
                    }
                },
            },
        )
        resp.raise_for_status()
        data = resp.json()

        if "errors" in data:
            logger.error(f"GraphQL error: {data['errors']}")
            break

        page = data.get("data", {}).get("userProgressQuestionList", {})
        questions = page.get("questions", [])

        for q in questions:
            problems.append(
                {
                    "titleSlug": q["titleSlug"],
                    "frontendId": q.get("frontendId", ""),
                    "title": q.get("title", q["titleSlug"]),
                }
            )

        pbar.update(len(questions))
        skip += limit
        if skip >= total:
            break
        time.sleep(0.1)

    pbar.close()
    return problems


def download_code(headers, submission_id):
    resp = graphql_post(
        headers,
        {
            "query": SUBMISSION_DETAILS_QUERY,
            "variables": {"id": int(submission_id)},
        },
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        return None
    detail = data["data"].get("submissionDetails")
    if detail is None:
        return None
    return detail.get("code")


def fmt_ts(ts):
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d")


def save_file(headers, sub):
    lang_info = map_language(sub.get("lang", "unknown"))
    folder = lang_info["folder"]
    ext = lang_info["ext"]
    os.makedirs(folder, exist_ok=True)

    q_id = sub.get("question", {}).get("questionId", "unknown")
    title = sub.get("title", "untitled")
    kebab_title = to_kebab_case(title)
    filename = f"{q_id}.{kebab_title}.{ext}"
    filepath = os.path.join(folder, filename)
    date_str = fmt_ts(sub.get("submitTime", 0))

    if os.path.exists(filepath):
        return "skipped", filename, date_str

    code = download_code(headers, sub["id"])
    if code:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        return "saved", filename, date_str
    else:
        return "failed", filename, date_str


def scan_problem(headers, problem, start_dt=None, end_dt=None):
    saved = 0
    skipped = 0
    failed = 0

    slug = problem["titleSlug"]
    question_id = problem["frontendId"]
    title = problem["title"]

    offset = 0
    limit = 20
    past_range = False

    while True:
        resp = graphql_post(
            headers,
            {
                "query": SUBMISSIONS_QUERY,
                "variables": {"offset": offset, "limit": limit, "slug": slug},
            },
        )
        resp.raise_for_status()
        data = resp.json()

        if "errors" in data:
            tqdm.write(f"  ❌ GraphQL error for {slug}")
            break

        sub_data = data.get("data", {}).get("submissionList", {})
        submissions = sub_data.get("submissions", [])
        has_next = sub_data.get("hasNext", False)

        for sub in submissions:
            ts = int(sub["timestamp"])
            sub_time = datetime.fromtimestamp(ts, tz=timezone.utc)

            if start_dt and sub_time < start_dt:
                past_range = True
                break

            if sub.get("statusDisplay", "").lower() != "accepted":
                continue

            if start_dt and end_dt and not (start_dt <= sub_time <= end_dt):
                continue

            status, filename, date_str = save_file(
                headers,
                {
                    "id": sub["id"],
                    "title": title,
                    "lang": sub.get("lang", "unknown"),
                    "submitTime": ts,
                    "question": {
                        "questionId": question_id,
                        "titleSlug": slug,
                    },
                },
            )

            if status == "saved":
                saved += 1
                tqdm.write(f"  ✅ [{date_str}] Saved {filename}")
            elif status == "skipped":
                skipped += 1
            else:
                failed += 1
                tqdm.write(f"  ❌ [{date_str}] Failed {filename}")

            time.sleep(0.1)

        if past_range or not has_next:
            break
        offset += limit
        time.sleep(0.1)

    return saved, skipped, failed


def main():
    parser = argparse.ArgumentParser(
        description="Download your LeetCode submissions"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="download all accepted submissions in the date range (default: today's daily challenge only)",
    )
    args = parser.parse_args()

    SESSION_COOKIE = os.getenv("LEETCODE_SESSION_COOKIE")
    CSRF_TOKEN = os.getenv("LEETCODE_CSRF_TOKEN")

    assert SESSION_COOKIE, "Please set the LEETCODE_SESSION_COOKIE environment variable."
    assert CSRF_TOKEN, "Please set the LEETCODE_CSRF_TOKEN environment variable."

    headers = get_headers(SESSION_COOKIE, CSRF_TOKEN)

    total_saved = 0
    total_skipped = 0
    total_failed = 0

    if args.all:
        USERNAME = os.getenv("LEETCODE_USERNAME")
        assert USERNAME, "Please set the LEETCODE_USERNAME environment variable."

        START_DATE = datetime(2021, 1, 1, tzinfo=timezone.utc)
        END_DATE = datetime(2026, 12, 2, tzinfo=timezone.utc)

        problems = fetch_solved_problems(headers)
        logger.info(f"Processing submissions for {len(problems)} solved problems...")

        for problem in tqdm(problems, desc="Downloading submissions", unit=" problems"):
            s, k, f = scan_problem(headers, problem, START_DATE, END_DATE)
            total_saved += s
            total_skipped += k
            total_failed += f
    else:
        daily = fetch_daily_challenge()
        logger.info(f"Today's daily challenge: {daily['title']} ({daily['titleSlug']})")

        s, k, f = scan_problem(headers, daily)
        total_saved += s
        total_skipped += k
        total_failed += f

    logger.info(f"Done: {total_saved} saved, {total_skipped} skipped, {total_failed} failed.")


if __name__ == "__main__":
    load_dotenv()
    main()
