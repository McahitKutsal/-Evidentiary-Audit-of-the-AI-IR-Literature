# Pre-registration Protocol: Evidentiary Audit of the AI–IR Literature

**Status:** Draft for deposit. Once deposited, this document is frozen (Manifesto §9). Any later change is logged in the Change Log with date and reason, and reported in the article's method section.

**Deposit target:** Public Git repository, <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>
**Freeze commit:** [ ] (full 40-character SHA of the commit carrying the `protocol-frozen` tag)
**Freeze date:** [ ] (tagger date of `protocol-frozen`, UTC)
**Archive DOI:** [ ] (Zenodo DOI minted from the tagged release; see §15)

The deposit mechanism and its evidentiary limits are stated in §15. That section is part of the protocol and is reported in the article's method section.

---

## 1. Research questions

RQ1. What share of claims in the peer-reviewed AI–IR literature (2015–2025) rest on each warrant type?
RQ2. Does the fit between claim type and warrant type, assessed relative to the author's own epistemological positioning, vary with citation rank?
RQ3. What share of predictive claims carry the three declared-forecast indicators, and how many indicators survive transmission into citing texts?
RQ4. Which three claims are most central by supporting citation weight, and what research designs would test them?

## 2. Hypotheses (declared as conjecture; results are reported whichever way they fall)

H1. Predictive and causal claims outnumber descriptive and conceptual claims in the corpus.
H2. Among W3 claims, at least one declared-forecast indicator present in the originating text is absent in the citing text in more than half of cases.
H3. Within publication year, the association between citation rank and share of adequately fitted claims is not positive.

Null or opposite results for H2 and H3 are reported as findings, not as failures (Manifesto §13).

## 3. Search

Databases: Web of Science Core Collection; Scopus.
Date range: 1 January 2015 – 31 December 2025.
Search string: see Appendix C of the article.
Language: English.
Document type: research article.
Start-date justification: annual hit counts 2010–2025 recorded before screening.

## 4. Eligibility

Include: peer-reviewed research articles in journals indexed under IR, political science, or security studies in either database; substantive engagement with AI as variable, concept, or object; English language.

Exclude: book reviews, editorials, forum pieces without original argument; AI used only as illustration; computer science or law venues without IR/security framing; grey literature; books and chapters.

## 5. Screening

Two screeners, independent, at title/abstract and at full text. Disagreements resolved by discussion; unresolved cases included at full-text stage and decided there. PRISMA 2020 flow recorded at every step.

## 6. Sampling rule

If N included ≤ 400: full coding.
If N > 400: stratified random sample by publication year and journal, minimum 400 articles, drawn with a fixed seed recorded here: seed = [ ].

## 7. Unit of analysis and extraction

Unit: the claim (single proposition asserted by the author as their own).
Extraction scope: all claims in abstract, introduction, conclusion; body claims marked as hypothesis, argument, contribution, or finding. Claims attributed to others without endorsement are not extracted; ambiguous endorsement is extracted and flagged.

## 8. Variables

| Variable | Level | Values |
|---|---|---|
| Claim type | claim | descriptive, conceptual, causal, predictive, normative, other |
| Warrants present | claim | W1–W8 (multi) |
| Primary warrant | claim | W1–W8 |
| W3 sub-code | claim | traces to W1/W2; traces to W3; traces to W4–W8; unknown |
| Positioning | article | P1, P2, P3, P4 |
| Positioning inferred | article | yes/no |
| Fit | claim | adequate, partial, inadequate |
| Scope conditions stated | claim (predictive/causal-future) | 0/1 |
| Conjectural status signalled | claim | 0/1 |
| Falsifier identified | claim | 0/1 |
| Canonical claim ID | claim | ID or none |
| Citation valence (for W3) | claim | supporting, neutral, critical |

Fit is assigned by the matrix in Appendix A of the article. Coders record inputs; fit is computed, then reviewed. Coder override of computed fit is permitted only with a logged reason.

## 9. Reliability

Double coding: minimum 25% of articles, random, fixed seed.
Statistic: Krippendorff's α (nominal) per variable; unitising α for claim boundaries.
Threshold: α ≥ 0.70. Below threshold: scheme revised, revision logged, affected variable re-coded in full.
Disagreement rule after discussion: fit → partial; other variables → logged and adjudicated by a third reader.

## 10. Citation data

Source: [WoS / Scopus / Google Scholar], retrieved on [ ].
Measures: raw count; citations per year; within-year rank.
Claim centrality: sum of citations-per-year of articles asserting the canonical claim with supporting or neutral valence.

## 11. Analysis

Descriptive distributions for RQ1 and RQ3.
RQ2: Spearman ρ between within-year citation rank and article-level share of adequate fit; bootstrapped 95% CI (2,000 resamples); pooled and by year.
RQ3 transmission: paired comparison of indicator presence, originating vs citing text, for W3 claims.
No inferential test is treated as confirmatory beyond H1–H3.

## 12. Reporting rules

Findings reported at aggregate level only. Individual articles named only as positive examples. No named negative generalisations about authors or schools (Manifesto §VI).

## 13. Self-application

Before submission, the article's own claims are coded with this scheme. Any claim coding as W8 is removed or re-warranted. Result reported in Limitations.

## 14. Change log

| Date | Change | Reason | Stage |
|---|---|---|---|
| 2026-09-10 | Deposit target changed from OSF Registries to a public Git repository with a Zenodo-archived tagged release (§1, §15) | Investigator preference; equivalent public time-stamping and DOI, with the tamper-evidence limits stated in §15 | Pre-freeze |
| | | | |

---

## 15. Deposit and freeze mechanism

The protocol is deposited as a file in a public Git repository rather than in a registry. This section states exactly what that does and does not establish, so that a reader can weigh it.

**What is deposited.** This protocol, the coding workbook, the analysis script, and the article draft are committed to <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>. The repository is public from the first commit.

**The freeze event.** The protocol is frozen by an annotated Git tag named `protocol-frozen` applied to a specific commit. The tag carries a tagger date. From that tag onward, every change to this document is made in a later commit and logged in §14 with date and reason. The frozen text remains permanently retrievable at the tagged commit.

**What this establishes.** Git commits are content-addressed: the commit SHA is a cryptographic hash over the tree, the parent commit, the author and committer identities, and the timestamps. Any alteration to the protocol text at or before the freeze commit produces a different SHA and therefore breaks every descendant commit. Once the freeze SHA is published in the article, in the coding workbook change log, and in the Zenodo archive, an undetected substitution of the frozen text is not feasible.

**What this does not establish.** A Git history is not by itself tamper-evident against its own owner. The repository owner can rewrite history (`commit --amend`, `rebase`, `push --force`), move or delete a tag, or delete the repository. A registry deposit cannot be withdrawn in this way. Three measures are therefore taken, and the protocol is not treated as frozen until all three are in place:

1. **Tagged release.** The freeze commit is published as a GitHub release, not only as a tag.
2. **External archive with a DOI.** The release is archived to Zenodo through the GitHub–Zenodo integration. Zenodo mints a DOI, stores an independent copy of the repository at that commit, and does not permit the depositor to alter a published record. The DOI is recorded in §1 and cited in the article. This is the component that supplies the tamper-evidence a registry deposit would have supplied; the Git tag alone does not.
3. **Published SHA.** The full 40-character freeze SHA is written into §1, into the `Change_Log` sheet of the coding workbook, and into §5.1 of the article. A reader can verify that the tagged commit hashes to the published SHA and that the Zenodo copy matches it.

**Branch protection.** Force-pushing to the default branch is disabled for the lifetime of the project. This is a repository setting, not a claim in this document, and a reader who wishes to verify the freeze should rely on the Zenodo DOI rather than on the branch setting.

**Reporting.** The article's method section states the freeze mechanism, the freeze SHA, the tag date, and the Zenodo DOI, and states plainly that the deposit is a public repository archived to Zenodo rather than a registry entry. No claim of registry registration is made anywhere in the article.
