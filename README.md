# leetcoder

Download your accepted LeetCode submissions as local files, organized by programming language.

## What it does

Connects to LeetCode via its GraphQL API and downloads the source code of your accepted submissions within a configurable date range. Files are saved into per-language folders with names like `1.two-sum.py`.

Example output structure:

```
python/
  1.two-sum.py
  2.add-two-numbers.py
golang/
  1.two-sum.go
  3.longest-substring-without-repeating-characters.go
```

## Supported languages

| Language    | Folder   | Extension |
|-------------|----------|-----------|
| Python/Python3 | `python` | `.py` |
| C++        | `cpp`    | `.cpp` |
| Go         | `golang` | `.go` |
| Java       | `java`   | `.java` |
| JavaScript | `js`     | `.js` |
| TypeScript | `ts`     | `.ts` |
| Rust       | `rust`   | `.rs` |

## Setup

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Configuration

Create a `.env` file in the project root:

```env
LEETCODE_USERNAME=your_username
LEETCODE_SESSION_COOKIE=your_session_cookie
LEETCODE_CSRF_TOKEN=your_csrf_token
```

### Getting your session cookie and CSRF token

1. Log in to [leetcode.com](https://leetcode.com) in your browser
2. Open DevTools (F12) -> Application -> Cookies -> `https://leetcode.com`
3. Copy the values of `LEETCODE_SESSION` and `csrftoken`

### Date range

Edit `START_DATE` and `END_DATE` in the `main()` function of `leetcoder.py`:

```python
START_DATE = datetime(2021, 1, 1, tzinfo=timezone.utc)
END_DATE = datetime(2026, 12, 2, tzinfo=timezone.utc)
```

## Usage

```bash
uv run leetcoder.py
```

The script will:

1. Fetch your list of solved problems (with progress bar)
2. For each problem, scan its submissions and immediately download+save any accepted submission within the date range (with progress bar)
3. Print each saved file with its date: `✅ [2025-04-12] Saved 1.two-sum.py`
4. Skip files that already exist on disk
5. Print a summary at the end

## Resuming

Safe to re-run. Already-existing files are skipped, so interrupted runs pick up where they left off.

## Rate limiting

The script includes built-in delays between requests and automatic retries (up to 5 attempts with increasing backoff) on timeouts and connection errors.
