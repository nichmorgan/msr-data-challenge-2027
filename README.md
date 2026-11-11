# MSR Data Challenge 2027 — GitSkills

Brief description: analysis of the GitSkills dataset for the MSR Data Challenge
2027 — investigating skill-text portability (vendor-neutral vs. tool-specific
locations) and tool licensing.

## Useful Links

- [GitSkills sample dataset](https://github.com/giuseppedestefanis/gitskills-sample)
- [Full GitSkills dataset (Hugging Face)](https://huggingface.co/datasets/mvaccargiu/gitskills)
- [MSR 2027 Mining Challenge](https://conf.researchr.org/track/msr-2027/msr-2027-mining-challenge)
- [GitSkills paper (arXiv)](https://arxiv.org/abs/2608.10906)

## Index

1. [Research Questions](docs/rq.md)
2. [Docs](docs/) — artifacts relevant for our research
3. [Brainstorm](brainstorm/) — any findings for our research
4. [Data exploration](.data-exploration) - suggested folder for scripts
5. [Scripts](scripts/README.md) — GitSkills parquet download and Argilla labeling setup

## Research Questions

1. What are the most common tools mentioned in skills files?
2. What is the license distribution of the tools and dependencies mentioned by skills files?
3. What is the license distribution of the projects that host tools mentioned in skills files, grouped by the freedom each license provides?

## Methodology

Initial methodology, to be expanded upon...

1. Parse the skills files and create a list of most common tools mentioned within skills files.
2. Run a script to locate the repository or site of the mentioned tools and find their license/whether they are open source or proprietary.
3. Resolve the projects that host the mentioned tools, group their licenses by the freedom each license provides, and describe that distribution.

## Research Team

- nichmorgan
- sullivanap
- swBodenhemier
