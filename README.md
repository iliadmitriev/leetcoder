# leetcoder

Download your accepted LeetCode submissions as local files, organized by programming language.

## What it does

By default, downloads your accepted solution for **today's daily challenge**. With `--all`, downloads all your accepted submissions within a configurable date range. Files are saved into per-language folders with names like `1.two-sum.py`.

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

## Usage

### Daily challenge (default)

```bash
uv run leetcoder.py
```

Fetches today's daily challenge and downloads your accepted submission for it.

### Download all submissions

```bash
uv run leetcoder.py --all
```

Downloads all your accepted submissions within the configured date range. To change the range, edit `START_DATE` and `END_DATE` in the `main()` function:

```python
START_DATE = datetime(2021, 1, 1, tzinfo=timezone.utc)
END_DATE = datetime(2026, 12, 2, tzinfo=timezone.utc)
```

## Resuming

Safe to re-run. Already-existing files are skipped, so interrupted runs pick up where they left off.

## Rate limiting

The script includes built-in delays between requests and automatic retries (up to 5 attempts with increasing backoff) on timeouts and connection errors.
