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

1. What proportion of skills use vendor-neutral rather than tool-specific
   locations, and how does this proportion change over time?  
2. Do skill texts address one named tool, or any agent that implements the
   specification?  
3. What kind of license have these tools?  

## Methodology

Initial methodology, to be expanded upon...

1. Sample by skills file first commit date in order to see change in time, sort each skills file path into "vender-neutral" and "tool-specific" categories (use or compile a list of vender and tool names to filter with, include a third "unsorted" group that we can analyze and add new entries to the compiled lists with), graph proportions over time.  
2. Create a list of most common tools and agents mentioned within skills files, and how these tools and agents relate to the vender-neutral and tool-specific categories.   
3. Find license totals for each group of vender-neutral and tool-specific over time to see how the project license relates to how the skill file is stored and named. Also find the relation between license and tools/agents mentioned within the skills files.  

## Research Team

- nichmorgan
- sullivanap
- swBodenhemier

