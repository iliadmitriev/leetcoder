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
            tqdm.write(
                f"  ⚠️ Retry {attempt}/{retries} after {e.__class__.__name__} ({wait}s)"
            )
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


def save_file(headers, sub, force=False):
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

    already_exists = os.path.exists(filepath)
    if already_exists and not force:
        return "skipped", filename, date_str

    code = download_code(headers, sub["id"])
    if code:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        if force and already_exists:
            return "overwritten", filename, date_str
        return "saved", filename, date_str
    else:
        return "failed", filename, date_str


def scan_problem(headers, problem, start_dt=None, end_dt=None, force=False):
    slug = problem["titleSlug"]
    question_id = problem["frontendId"]
    title = problem["title"]

    offset = 0
    limit = 20

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
            return "failed", slug

        sub_data = data.get("data", {}).get("submissionList", {})
        submissions = sub_data.get("submissions", [])
        has_next = sub_data.get("hasNext", False)

        for sub in submissions:
            ts = int(sub["timestamp"])
            sub_time = datetime.fromtimestamp(ts, tz=timezone.utc)

            if start_dt and sub_time < start_dt:
                return "not_found", slug

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
                force=force,
            )

            if status == "saved":
                tqdm.write(f"  ✅ [{date_str}] Saved {filename}")
                return "saved", filename
            elif status == "overwritten":
                tqdm.write(f"  🔄 [{date_str}] Overwritten {filename}")
                return "overwritten", filename
            elif status == "skipped":
                return "skipped", filename
            else:
                tqdm.write(f"  ❌ [{date_str}] Failed {filename}")
                return "failed", filename

        if not has_next:
            return "not_found", slug

        offset += limit
        time.sleep(0.1)


def parse_range(range_str):
    parts = range_str.split("-")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError(
            f"Invalid range '{range_str}', expected format: START-END (e.g. 1-50)"
        )
    try:
        start, end = int(parts[0]), int(parts[1])
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid range '{range_str}', expected integers (e.g. 1-50)"
        )
    if start > end:
        start, end = end, start
    return start, end


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid date '{date_str}', expected format: YYYY-MM-DD"
        )


def resolve_problems(headers, args):
    start_dt = None
    end_dt = None

    if args.all:
        problems = fetch_solved_problems(headers)
        logger.info(f"Processing {len(problems)} solved problems...")
        return problems, start_dt, end_dt

    if args.range:
        range_start, range_end = parse_range(args.range)
        all_solved = fetch_solved_problems(headers)
        problems = [
            p
            for p in all_solved
            if p["frontendId"].isdigit()
            and range_start <= int(p["frontendId"]) <= range_end
        ]
        logger.info(
            f"Found {len(problems)} solved problems in range {range_start}-{range_end}"
        )
        return problems, start_dt, end_dt

    if args.problems:
        target_ids = {str(pid) for pid in args.problems}
        all_solved = fetch_solved_problems(headers)
        problems = [
            p for p in all_solved if p["frontendId"] in target_ids
        ]
        missing = target_ids - {p["frontendId"] for p in problems}
        if missing:
            logger.warning(f"No solved problems found for IDs: {', '.join(sorted(missing))}")
        logger.info(f"Found {len(problems)} matching solved problems")
        return problems, start_dt, end_dt

    if args.from_date or args.to_date:
        start_dt = parse_date(args.from_date) if args.from_date else datetime(2021, 1, 1, tzinfo=timezone.utc)
        end_dt = parse_date(args.to_date) if args.to_date else datetime.now(tz=timezone.utc)
        problems = fetch_solved_problems(headers)
        logger.info(
            f"Processing {len(problems)} solved problems ({start_dt:%Y-%m-%d} to {end_dt:%Y-%m-%d})..."
        )
        return problems, start_dt, end_dt

    return None, start_dt, end_dt


def main():
    parser = argparse.ArgumentParser(description="Download your LeetCode submissions")
    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument(
        "--all",
        action="store_true",
        help="download all solved problems",
    )
    source_group.add_argument(
        "--range",
        metavar="START-END",
        type=str,
        help="download solved problems by ID range (e.g. 1-50)",
    )
    source_group.add_argument(
        "--problems",
        nargs="+",
        type=int,
        metavar="ID",
        help="download specific solved problems by ID (e.g. 1 42 100)",
    )
    parser.add_argument(
        "--from-date",
        metavar="YYYY-MM-DD",
        type=str,
        help="download submissions from this date (implies all solved problems)",
    )
    parser.add_argument(
        "--to-date",
        metavar="YYYY-MM-DD",
        type=str,
        help="download submissions up to this date (implies all solved problems)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing files",
    )
    args = parser.parse_args()

    SESSION_COOKIE = os.getenv("LEETCODE_SESSION_COOKIE")
    CSRF_TOKEN = os.getenv("LEETCODE_CSRF_TOKEN")

    assert SESSION_COOKIE, (
        "Please set the LEETCODE_SESSION_COOKIE environment variable."
    )
    assert CSRF_TOKEN, "Please set the LEETCODE_CSRF_TOKEN environment variable."

    headers = get_headers(SESSION_COOKIE, CSRF_TOKEN)

    total_saved = 0
    total_skipped = 0
    total_overwritten = 0
    total_failed = 0
    total_not_found = 0

    problems, start_dt, end_dt = resolve_problems(headers, args)

    if problems is None:
        daily = fetch_daily_challenge()
        logger.info(f"Today's daily challenge: {daily['title']} ({daily['titleSlug']})")
        problems = [daily]

    for problem in tqdm(problems, desc="Downloading", unit=" problem"):
        status, detail = scan_problem(
            headers, problem, start_dt, end_dt, force=args.force
        )
        if status == "saved":
            total_saved += 1
        elif status == "overwritten":
            total_overwritten += 1
        elif status == "skipped":
            total_skipped += 1
        elif status == "not_found":
            total_not_found += 1
        else:
            total_failed += 1
        time.sleep(0.1)

    parts = []
    if total_saved:
        parts.append(f"{total_saved} saved")
    if total_overwritten:
        parts.append(f"{total_overwritten} overwritten")
    if total_skipped:
        parts.append(f"{total_skipped} skipped")
    if total_not_found:
        parts.append(f"{total_not_found} not found")
    if total_failed:
        parts.append(f"{total_failed} failed")
    logger.info(f"Done: {', '.join(parts) or 'nothing to do'}.")


if __name__ == "__main__":
    load_dotenv()
    main()
