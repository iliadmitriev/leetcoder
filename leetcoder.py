import logging
import os
import re
import time
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

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


def fetch_accepted_problem_slugs(session_cookie, csrf_token):
    headers = get_headers(session_cookie, csrf_token)
    slugs = []
    limit, skip = 100, 0

    logger.info("Fetching list of accepted problems...")
    while True:
        payload = {
            "query": SOLVED_PROBLEMS_QUERY,
            "variables": {
                "filters": {
                    "skip": skip,
                    "limit": limit,
                    "questionStatus": "SOLVED",
                }
            },
        }
        resp = requests.post(LEETCODE_GRAPHQL_URL, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()

        if "errors" in data:
            logger.error(f"GraphQL error: {data['errors']}")
            break

        result = data.get("data", {}).get("userProgressQuestionList", {})
        questions = result.get("questions", [])
        total = result.get("totalNum", 0)

        for q in questions:
            slugs.append(
                {
                    "titleSlug": q["titleSlug"],
                    "frontendId": q.get("frontendId", ""),
                    "title": q.get("title", q["titleSlug"]),
                }
            )

        skip += limit
        if skip >= total:
            break
        time.sleep(0.5)

    logger.info(f"Found {len(slugs)} accepted problems.")
    return slugs


def fetch_accepted_submissions(
    username, session_cookie, csrf_token, start_dt, end_dt, daily_slugs=None
):
    headers = get_headers(session_cookie, csrf_token)
    results = []

    problems = fetch_accepted_problem_slugs(session_cookie, csrf_token)

    if daily_slugs is not None:
        problems = [p for p in problems if p["titleSlug"] in daily_slugs]

    logger.info(f"Fetching submissions for {len(problems)} problems...")

    for problem in problems:
        slug = problem["titleSlug"]
        question_id = problem["frontendId"]
        title = problem["title"]

        offset = 0
        limit = 20

        while True:
            payload = {
                "query": SUBMISSIONS_QUERY,
                "variables": {
                    "offset": offset,
                    "limit": limit,
                    "slug": slug,
                },
            }
            resp = requests.post(LEETCODE_GRAPHQL_URL, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()

            if "errors" in data:
                logger.error(f"GraphQL error for {slug}: {data['errors']}")
                break

            sub_data = data.get("data", {}).get("submissionList", {})
            submissions = sub_data.get("submissions", [])
            has_next = sub_data.get("hasNext", False)

            for sub in submissions:
                ts = int(sub["timestamp"])
                sub_time = datetime.fromtimestamp(ts, tz=timezone.utc)
                if sub_time < start_dt:
                    break

                if start_dt <= sub_time <= end_dt and sub.get("statusDisplay", "").lower() == "accepted":
                    results.append(
                        {
                            "id": sub["id"],
                            "title": title,
                            "lang": sub.get("lang", "unknown"),
                            "submitTime": ts,
                            "question": {
                                "questionId": question_id,
                                "titleSlug": slug,
                            },
                        }
                    )

            if not has_next:
                break
            offset += limit
            time.sleep(0.5)

        time.sleep(0.8)

    return results


def download_code(submission_id, session_cookie, csrf_token):
    headers = get_headers(session_cookie, csrf_token)
    payload = {
        "query": SUBMISSION_DETAILS_QUERY,
        "variables": {"id": int(submission_id)},
    }
    resp = requests.post(LEETCODE_GRAPHQL_URL, headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        return None
    return data["data"]["submissionDetails"].get("code")


def main():
    # ================= CONFIGURATION =================

    USERNAME = os.getenv("LEETCODE_USERNAME")
    SESSION_COOKIE = os.getenv("LEETCODE_SESSION_COOKIE")
    CSRF_TOKEN = os.getenv("LEETCODE_CSRF_TOKEN")

    assert USERNAME, "Please set the LEETCODE_USERNAME environment variable."
    assert SESSION_COOKIE, (
        "Please set the LEETCODE_SESSION_COOKIE environment variable."
    )
    assert CSRF_TOKEN, "Please set the LEETCODE_CSRF_TOKEN environment variable."

    # Date range (UTC)
    START_DATE = datetime(2024, 1, 1, tzinfo=timezone.utc)
    END_DATE = datetime(2024, 1, 31, tzinfo=timezone.utc)

    # Optional: Filter only specific daily challenge slugs
    # If None, downloads ALL accepted submissions in the period
    DAILY_CHALLENGE_SLUGS = None  # e.g., ["two-sum", "valid-palindrome"]
    # =================================================

    submissions = fetch_accepted_submissions(
        USERNAME,
        SESSION_COOKIE,
        CSRF_TOKEN,
        START_DATE,
        END_DATE,
        DAILY_CHALLENGE_SLUGS,
    )
    logger.info(
        f"Found {len(submissions)} accepted submissions in the specified period."
    )

    # Group by language
    lang_groups = {}
    for sub in submissions:
        lang = sub.get("lang", "unknown")
        lang_groups.setdefault(lang, []).append(sub)

    for lang_slug, subs in lang_groups.items():
        lang_info = map_language(lang_slug)
        folder = lang_info["folder"]
        ext = lang_info["ext"]
        os.makedirs(folder, exist_ok=True)

        logger.info(f"Processing {len(subs)} submissions for {lang_slug}...")
        for sub in subs:
            q_id = sub.get("question", {}).get("questionId", "unknown")
            title = sub.get("title", "untitled")
            kebab_title = to_kebab_case(title)
            filename = f"{q_id}.{kebab_title}.{ext}"
            filepath = os.path.join(folder, filename)

            if os.path.exists(filepath):
                logger.info(f"  ⏭️ Skipping {filename} (already exists)")
                continue

            time.sleep(0.8)  # Prevent rate limiting on code fetches
            code = download_code(sub["id"], SESSION_COOKIE, CSRF_TOKEN)
            if code:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(code)
                logger.info(f"  ✅ Saved {filename}")
            else:
                logger.warning(f"  ❌ Failed to fetch code for {filename}")


if __name__ == "__main__":
    load_dotenv()
    main()
