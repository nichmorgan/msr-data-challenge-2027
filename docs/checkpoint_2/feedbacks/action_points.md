# Checkpoint 2 feedback — action points

These entries restate the raw notes in [raw/f1.md](raw/f1.md) and [raw/f2.md](raw/f2.md). A recommendation stays a recommendation, an observation stays an observation, and a reviewer’s uncertainty stays uncertainty. `Decision` and `Reasoning` are left blank while a point is still being discussed.

---

## Research questions

Checkpoint section: [initial_research.tex](../sections/initial_research.tex). Paper Section II.

### Counting unit

- **Point:** The counting unit needs a sentence in the paper. Once per distinct skill text is a defensible choice, but a skill copied into 5,000 repositories teaches its tool to 5,000 agents, and a template that stamps the same catalog everywhere will either dominate the ranking or disappear from it, depending on the unit. Report per distinct text and per repository next to each other. If the rankings differ, that is worth a paragraph on its own.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

---

## Related work

Paper section: Research Questions and Related Work.

### Closer related work

- **Point:** Closer related work: Hong et al. (arXiv:2607.01456) and Zhang et al. (arXiv:2608.08453) on what `SKILL.md` files contain; Jia et al. (arXiv:2607.01136), who trace what skills depend on and call, which is next door to the extraction step; and the license-mining literature (Vendome et al. on license evolution, for one) for RQ2.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

---

## Method

Checkpoint section: [technical_details.tex](../sections/technical_details.tex). Paper section: Method.

### Chunk skill bodies before labeling

- **Point:** The 384-character clip may hit the 384-token limit on the full run. A skill body averages several thousand characters and names tools throughout, so without chunking the extractor reads only the first paragraph and misses most of what it is meant to count. Maybe chunk the body, run each chunk, and merge hits per skill. That is a few lines of code, but it needs to be in place before the validation sample is labeled, or the recall measured will not be the recall obtained.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Cutoff, sample size, and agreement subset

- **Point:** A score cutoff of 0.8 and a precision of 80% are different metrics, and nothing ties them together. After the validation sample is labeled, sweep the cutoff, plot precision and recall against it, and pick the cutoff from the plot. State the sample size now, before labeling. Do the same for the agreement subset.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Sample rows in the notebook

- **Point:** In `explore_entities.ipynb`, the 500-row draw samples each column separately with the same seed. It happens to line up, but sample rows instead.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

---

## Pilot findings

Checkpoint section: [pilot_findings.tex](../sections/pilot_findings.tex).

### Seeded skill-body sample and 50 hand labels

- **Point:** Draw a seeded sample of skill bodies using the population rules, run the label-only model, and have the two of you hand-label 50 of the hits.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

## RQ2 resolution

Paper sections: Method and Future Work.

### Resolving every name may stall the plan

- **Point:** RQ2, as written, is where the plan could stall. Resolving every tool name to a publishing repository using a reasoning model plus web search is slow, hard to rerun (the rerun problem is already noted in the work), and the long tail of names is probably in the thousands.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Resolve the top N tools

- **Point:** Resolve the top N tools by skill count and report what share of all mentions they cover.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Deterministic license sources first

- **Point:** Use deterministic sources before any model. PyPI and npm return a license field through their APIs, and GitHub’s license endpoint returns an SPDX ID.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Write the freedom mapping before seeing the data

- **Point:** Write the license-to-freedom mapping down before seeing the data, using the OSI or FSF definitions it follows.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

## Remaining work, report, and prose

Checkpoint section: [remaining_work.tex](../sections/remaining_work.tex).

### Dates on the remaining-work list

- **Point:** The remaining-work list has an order but no dates, which may make the plan hard to judge.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Report length

- **Point:** The report is four pages, exceeding a two- to three-page limit. The reviewer is not sure the instructor will care.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### README still lists three questions

- **Point:** The README still lists three research questions, while the report has two.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:

### Shorter method sentences

- **Point:** Some sentences in the method run long enough that they had to be re-read multiple times. Shorter ones would help MSR reviewers.
- **Source:** f1

**Deliberation**

- Decision:
- Reasoning:
