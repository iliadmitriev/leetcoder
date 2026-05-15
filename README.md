# leetcoder

Download your accepted LeetCode submissions as local files, organized by programming language.

## What it does

Downloads your latest accepted LeetCode submission as a local file, organized by programming language. Multiple source modes are available — by default, it fetches today's daily challenge. Files are saved into per-language folders with names like `1.two-sum.py`.

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

| Language       | Folder   | Extension |
| -------------- | -------- | --------- |
| Python/Python3 | `python` | `.py`     |
| C++            | `cpp`    | `.cpp`    |
| Go             | `golang` | `.go`     |
| Java           | `java`   | `.java`   |
| JavaScript     | `js`     | `.js`     |
| TypeScript     | `ts`     | `.ts`     |
| Rust           | `rust`   | `.rs`     |

## Setup

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Configuration

Create a `.env` file in the project root:

```env
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

Downloads your latest accepted submission for today's daily challenge.

### Download by problem ID range

```bash
uv run leetcoder.py --range 1-50
```

Downloads your latest accepted submission for solved problems #1 through #50.

### Download specific problems

```bash
uv run leetcoder.py --problems 1 42 100
```

Downloads your latest accepted submission for the specified problem IDs.

### Download by date

```bash
uv run leetcoder.py --from-date 2024-01-01 --to-date 2024-06-30
```

Downloads accepted submissions made between the given dates (implies all solved problems). You can omit either end:

```bash
uv run leetcoder.py --from-date 2024-01-01
uv run leetcoder.py --to-date 2024-06-30
```

### Download all submissions

```bash
uv run leetcoder.py --all
```

Downloads your latest accepted submission for every solved problem.

### Force overwrite

Add `--force` to any mode to overwrite existing files:

```bash
uv run leetcoder.py --all --force
uv run leetcoder.py --range 1-50 --force
```

## Resuming

Safe to re-run. Already-existing files are skipped, so interrupted runs pick up where they left off. Use `--force` to overwrite with the latest submission.

## Rate limiting

The script includes built-in delays between requests and automatic retries (up to 5 attempts with increasing backoff) on timeouts and connection errors.
