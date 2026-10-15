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

## Research Questions

1. What are the most common tools and agents mentioned in skills files?
2. What is the license distribution of the tools and dependencies mentioned by skills files?
3. What are the skills files allowing the most common agents and tools to access in the project, and how does this relate to the license of the tool?

## Methodology

Initial methodology, to be expanded upon...

1. Parse the skills files and create a list of most common tools and agents mentioned within skills files.
2. Run a script to locate the repository or site of the mentioned tools and agents and find their license/whether they are open source or proprietary.
3. Collect a sample of the result from RQ2 and analyze the skills files themselves. What are the tools and agents allowed to change within the repo, what access rights are they given. Categorize the results into different levels of access, and then map those categories to the licenses found from RQ2.

## Research Team

- nichmorgan
- sullivanap
- swBodenhemier

