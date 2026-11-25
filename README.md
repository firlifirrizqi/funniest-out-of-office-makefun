[![Make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/firlifirrizqi/funniest-out-of-office-makefun/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/firlifirrizqi/funniest-out-of-office-makefun/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) of the same name: the funniest single line of an out-of-office auto-reply, in 140 characters or fewer.

## The line

> Out of office. I've set this auto-reply to auto-reply to itself, so by Monday we'll have had a very productive meeting without you.

## How it works

`main.py` writes that single line (131 characters, within the 140-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. A `verify()` helper re-reads the file and asserts it is byte-identical to the entry, 1–140 characters, and not only whitespace.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
