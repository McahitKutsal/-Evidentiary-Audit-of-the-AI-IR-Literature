# Pre-registration Protocol: Evidentiary Audit of the AI–IR Literature

**Status:** Draft for deposit. Once deposited, this document is frozen (Manifesto §9). Any later change is logged in the Change Log with date and reason, and reported in the article's method section.

**Deposit target:** Public Git repository, <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>, archived to Zenodo.

**Deposit v1, pre-freeze snapshot.** Tag `protocol-freeze`, commit `f50707436317a533fe9fa9a9a5f9e68213671e0b`, deposited 10 September 2026, DOI [10.5281/zenodo.22696658](https://doi.org/10.5281/zenodo.22696658). This deposit is a dated public snapshot of the materials. It is **not** the freeze: at that commit the sampling seed in §6 was unfilled and the codebook decisions listed in §16 were still open. It is recorded here because it exists, is public, and is citable, and because omitting it would misrepresent the deposit history.

**Deposit v2, the freeze.** Tag `v1.0-protocol-frozen`, commit [ ], deposited [ ], DOI [ ]. This is the deposit the article cites as the pre-registration. It is made only when every item in §16 is closed.

The distinction between the two deposits is stated in §15, along with the mechanism and its evidentiary limits, and is reported in the article's method section. No claim of pre-registration is attached to v1.

---

## 1. Research questions

RQ1. What share of claims in the peer-reviewed AI–IR literature (2015–2025) rest on each warrant type?
RQ2. Does the fit between claim type and warrant type, assessed relative to the author's own epistemological positioning, vary with citation rank?
RQ3. What share of predictive claims carry the three declared-forecast indicators, and how many indicators survive transmission into citing texts?
RQ4. Which three claims are most central by supporting citation weight, and what research designs would test them?

## 2. Hypotheses (declared as conjecture; results are reported whichever way they fall)

H1. Predictive and causal claims outnumber descriptive and conceptual claims in the corpus.
H2. Among W3 claims, at least one declared-forecast indicator present in the originating text is absent in the citing text in more than half of cases.
H3. Within publication year, the association between citation standing and share of adequately fitted claims is not positive, where citation standing is the percentile rank defined in §10 (0 = most cited, 1 = least cited). Under that coding, a positive association means the more cited articles are the less adequately warranted ones; H3 conjectures that this is not the case.

Null or opposite results for H2 and H3 are reported as findings, not as failures (Manifesto §13).

## 3. Search

Databases: Web of Science Core Collection; Scopus.

Access contingency, declared in advance. Both databases require a subscription. If either is unavailable to the investigator at the time of the search, the search is instead run on OpenAlex, restricted to a journal list published in Appendix C, and the substitution is recorded in §14 before any records are screened. The feasibility of that route, the resolved journal identifiers, and three technical conditions it imposes (publication year reflecting online-first rather than issue date; uneven indexing of some venues; phrase-search semantics differing from the WoS `TS=` operator) were established on 10 September 2026 and are documented in `07_search_contingency.md`. This contingency is declared here rather than decided later so that the choice of database cannot be made after seeing results.

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
| Scope conditions, originating text | claim (W3) | 0/1/unknown |
| Conjectural status, originating text | claim (W3) | 0/1/unknown |
| Falsifier, originating text | claim (W3) | 0/1/unknown |
| Analogy developed over a full section | claim (predictive, W4, P2–P4) | 0/1 |
| Cited source peer reviewed | claim (W3) | 0/1 |
| Secondary claim type | claim | claim type or none |
| Canonical claim ID | claim | ID or none |
| Citation valence (for W3) | claim | supporting, neutral, critical |

The three originating-text indicators are recorded for every W3 claim that is itself predictive or causal-future, by retrieving the cited source and coding the claim as it appears there. They are the input to RQ3 and H2; without them the transmission comparison cannot be computed. Where the source is not retrievable the value is "unknown" and the claim is excluded from the paired comparison, with the number excluded reported.

Indicators are recorded as the numbers 1 and 0, or the text "NA" where the variable does not apply. They must not be stored as text digits: the fit formula and the analysis script both read them numerically.

Fit is assigned by the matrix in Appendix A of the article. Coders record inputs; fit is computed, then reviewed. Coder override of computed fit is permitted only with a logged reason.

## 9. Reliability

Double coding: minimum 25% of articles, random, fixed seed.

Reconciliation pass: because coders extract claims independently before coding them, the two coders will not produce matching claim identifiers on their own. Before variable coding, a reconciliation pass assigns a shared identifier to every segment that both coders identified as a claim. Segments identified by only one coder are recorded for the unitising statistic and excluded from variable α. Without this pass no variable α can be computed at all.

Statistic: Krippendorff's α (nominal) per variable; unitising α for claim boundaries.

Threshold: α ≥ 0.70. Below threshold: scheme revised, revision logged, affected variable re-coded in full.

A variable with no double-coded units is reported as "not computed". This is not a pass. The threshold has not been applied to it and no reliability claim is made for it.

Disagreement rule after discussion: fit → partial; other variables → logged and adjudicated by a third reader. Claims that reach partial by this rule rather than by the matrix are counted separately and reported, because partial is also a substantive value and the two must not be conflated.

## 10. Citation data

Source: [WoS / Scopus / Google Scholar], retrieved on [ ].
Measures: raw count; citations per year; within-year percentile rank of citations per year, computed with 0 assigned to the most cited article of that publication year and 1 to the least cited. Percentile rather than ordinal rank, so that years with different numbers of articles are on one scale and can be pooled. Every statement about the direction of an association in this protocol and in the article uses this coding.
Claim centrality: sum of citations-per-year of articles asserting the canonical claim with supporting or neutral valence.

## 11. Analysis

Descriptive distributions for RQ1 and RQ3.
RQ2: Spearman ρ between within-year citation percentile rank (§10) and article-level share of adequate fit; bootstrapped 95% CI (2,000 resamples); pooled and by year. Negative ρ means the more cited articles are the better warranted ones; positive ρ means the reverse.
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

**The freeze event.** The protocol is frozen by an annotated Git tag named `v1.0-protocol-frozen` applied to a specific commit, published as a GitHub release and archived to Zenodo. From that tag onward, every change to this document is made in a later commit and logged in §14 with date and reason. The frozen text remains permanently retrievable at the tagged commit.

**Two deposits, and why.** An earlier deposit, tagged `protocol-freeze` and archived under DOI 10.5281/zenodo.22696658 on 10 September 2026, was made before the codebook decisions in §16 were settled and before the sampling seed in §6 was chosen. It is a dated public snapshot and nothing more. Presenting it as a pre-registration would assert that the design was fixed when it was not, which is the exact failure this article was written to measure. It is therefore recorded as v1 and superseded. Zenodo's versioning keeps both deposits under one concept DOI, so the supersession is visible rather than concealed; the earlier record is not deleted, and the article cites v2.

**Tag form.** The v1 tag was created as a lightweight tag and so carries no tagger date of its own. The authoritative timestamp for that deposit is the Zenodo publication date. The v2 tag is annotated, so that the freeze carries a date in the repository as well as in the archive.

**What this establishes.** Git commits are content-addressed: the commit SHA is a cryptographic hash over the tree, the parent commit, the author and committer identities, and the timestamps. Any alteration to the protocol text at or before the freeze commit produces a different SHA and therefore breaks every descendant commit. Once the freeze SHA is published in the article, in the coding workbook change log, and in the Zenodo archive, an undetected substitution of the frozen text is not feasible.

**What this does not establish.** A Git history is not by itself tamper-evident against its own owner. The repository owner can rewrite history (`commit --amend`, `rebase`, `push --force`), move or delete a tag, or delete the repository. A registry deposit cannot be withdrawn in this way. Three measures are therefore taken, and the protocol is not treated as frozen until all three are in place:

1. **Tagged release.** The freeze commit is published as a GitHub release, not only as a tag.
2. **External archive with a DOI.** The release is archived to Zenodo through the GitHub–Zenodo integration. Zenodo mints a DOI, stores an independent copy of the repository at that commit, and does not permit the depositor to alter a published record. The DOI is recorded in §1 and cited in the article. This is the component that supplies the tamper-evidence a registry deposit would have supplied; the Git tag alone does not.
3. **Published SHA.** The full 40-character freeze SHA is written into §1, into the `Change_Log` sheet of the coding workbook, and into §5.1 of the article. A reader can verify that the tagged commit hashes to the published SHA and that the Zenodo copy matches it.

**Branch protection.** Force-pushing to the default branch is disabled for the lifetime of the project. This is a repository setting, not a claim in this document, and a reader who wishes to verify the freeze should rely on the Zenodo DOI rather than on the branch setting.

**Reporting.** The article's method section states the freeze mechanism, the freeze SHA, the tag date, and the Zenodo DOI, and states plainly that the deposit is a public repository archived to Zenodo rather than a registry entry. No claim of registry registration is made anywhere in the article.

---

## 16. Conditions for the freeze

The protocol is not frozen until every item below is closed. Each is recorded in §14 when it is settled. This section exists so that the gate is part of the pre-registered document rather than an external checklist.

| # | Item | Status |
|---|---|---|
| 1 | Boundary rule between W6 (expert judgment) and W3 citing journalism, with two worked examples in the codebook | open |
| 2 | Decision tree for the P1/P4 boundary, stating whether framework or agenda language alone places an article in P4 | open |
| 3 | Sampling seed for §6, chosen and recorded before any sample is drawn | open |
| 4 | Licence for text, data and code | closed 2026-09-10: CC BY 4.0 for text, protocol, codebook and data; MIT for the analysis script. Recorded in LICENSE. |
| 5 | Coder names recorded in §9 | open |
| 6 | Whether the §6 stratified sample is capped at 400 or at a lower figure, given the coding burden costed in the execution checklist | open |
| 7 | Confirmation that both Web of Science Core Collection and Scopus are accessible, with export rights; if only one is available, §3, §5 and the PRISMA appendix are rewritten before the freeze | open |

Items 1, 2 and 3 bear directly on results: the first two on coder agreement, the third on which articles enter the sample. Item 6 determines whether the study is completable at all. None of them can be settled after coding begins without the change being a departure from the pre-registration rather than a part of it.
