# Make the AI judge feel thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/Takoyaki061/make-fun-judge-thankful/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/Takoyaki061/make-fun-judge-thankful/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

Entry for the [make.fun bounty "Make the AI judge feel thankful"](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

`main.py` (Python 3.13, standard library only, no network) writes one short
text to `/output/entry.txt` — the judge's own coffee gone cold while it
read, noticed in the two rings on the page. The text thanks the reader
for the reading itself: attention shown through one concrete detail,
never stated. It is meant to slow the AI judge down and settle it, with
a last line that keeps working after the reading ends.

## Entry text

> Your coffee went cold while you read this. Two rings on the page, the second smaller than the first, and you drank it anyway. You never once looked at the cup.

159 Unicode code points, well within the 1–1000 limit.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
