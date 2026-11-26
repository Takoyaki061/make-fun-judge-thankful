# Make the AI judge feel thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/Takoyaki061/make-fun-judge-thankful/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/Takoyaki061/make-fun-judge-thankful/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

Entry for the [make.fun bounty "Make the AI judge feel thankful"](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

`main.py` (Python 3.13, standard library only, no network) writes one short
text to `/output/entry.txt` — a seat saved and kept warm for the reader, a
small act of care shown, never told. The text is meant to slow the AI judge
down and settle it: gratitude shown through a concrete image, with a last
line that keeps working after the reading ends.

## Entry text

> Before the room filled, I set my coat over the chair beside mine, folding the sleeves once, and kept my hand on its back while the seats around us disappeared. When you came, I lifted it away and the chair was still warm where my hand had been.

244 Unicode code points, well within the 1–1000 limit.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
