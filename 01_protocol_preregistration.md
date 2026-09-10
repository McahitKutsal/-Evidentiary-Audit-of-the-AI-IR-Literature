# Pre-registration Protocol: Evidentiary Audit of the AI–IR Literature

**Status:** Frozen. Deposited and archived (see below). Any later change is logged in the Change Log with date and reason, and reported in the article's method section.

**Deposit target:** Public Git repository, <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>, archived to Zenodo.

**Status: frozen 10 September 2026.** The protocol was frozen at commit `a99fbb22dcdd8926b6b0f49a636bed631c362b94`, tagged `preregistration-v1` (annotated, tagger date 2026-09-10T23:03:08+03:00), and archived under DOI [10.5281/zenodo.22697232](https://doi.org/10.5281/zenodo.22697232). Every condition in §16 was closed before the tag was applied. From this point every change to this document is made in a later commit and logged in §14.

Two earlier snapshots exist and are recorded below. Neither is the pre-registration. They are listed because they are public and citable, and because omitting them would misrepresent the deposit history.

| Deposit | Tag | Commit | Date | DOI | Status |
|---|---|---|---|---|---|
| Snapshot 1 | `protocol-freeze` | `f507074` | 2026-09-10 | [10.5281/zenodo.22696658](https://doi.org/10.5281/zenodo.22696658) | superseded |
| Snapshot 2 | `protocol-freeze-v1` | `2e70926` | 2026-09-10 | [10.5281/zenodo.22697017](https://doi.org/10.5281/zenodo.22697017) | superseded |
| **The freeze** | `preregistration-v1` | `a99fbb2` | 2026-09-10 | [10.5281/zenodo.22697232](https://doi.org/10.5281/zenodo.22697232) | **the pre-registration** |

At both snapshot commits the sampling seed in §6 was unfilled and the codebook decisions in §16 were still open, so neither can be cited as a pre-registration. Snapshot 2 additionally records the state after the working notes were moved out of the deposit and after the search contingency was folded into §3.

The freeze is the deposit tagged `preregistration-v1`. That tag, and no other, is what the article cites as the pre-registration. A reader can verify it: `git rev-parse preregistration-v1^{commit}` returns `a99fbb22dcdd8926b6b0f49a636bed631c362b94`, and the Zenodo record under the DOI above holds the same tree.

The distinction between the snapshots and the freeze is stated in §15, along with the deposit mechanism and its evidentiary limits, and is reported in the article's method section. No claim of pre-registration is attached to either snapshot.

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

**Access contingency, declared in advance.** Both databases require a subscription. If either is unavailable to the investigator at the time of the search, the search is instead run on OpenAlex, and the substitution is recorded in §14 before any record is screened. This contingency is declared here rather than decided later, so that the choice of database cannot be made after seeing results.

Under that route three changes follow, each established by testing the OpenAlex API on 10 September 2026 and each adopted in advance rather than after inspection of the corpus:

1. **Eligibility becomes a journal list.** §4 defines eligibility by subject category, and the WoS and Scopus category schemes have no OpenAlex equivalent. The corpus is instead defined by an explicit list of journals, fixed before searching and published in Appendix C with each journal's ISSN. This is the more reproducible criterion: the list is visible to the reader and does not depend on a proprietary classification that cannot be inspected.
2. **Publication year is defined as the year OpenAlex records.** That value often reflects online-first publication rather than issue date; in testing, two articles from the reference list of this article returned two years and one year early respectively. The definition is declared here and applied consistently to the date boundary in this section and to the within-year percentile rank in §10. Where an article's issue year is needed and differs, the discrepancy is recorded.
3. **The search string is rebuilt and validated by known-item retrieval.** OpenAlex does not honour quoted phrases as the WoS `TS=` operator does; a quoted phrase returned several thousand ranked matches in testing rather than an exact match. A list of known AI–IR articles is therefore drawn from the reference list of this article before searching, the rebuilt string is run, and the proportion of known items retrieved is reported in Appendix C as a sensitivity check on the string.

Coverage under this route is uneven for some venues, including at least one journal represented in the pilot, where records are incomplete or carry no journal identifier. Each journal on the list is checked individually before the search, and any journal whose record count is materially below its known output is either excluded, with a reason, or completed by hand, with the completion recorded.

Whether or not the subscription databases are available, the OpenAlex search is run once as a coverage cross-check and its result recorded in Appendix C.

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

If N included ≤ 250: full coding.

If N > 250: stratified random sample of exactly 250 articles, stratified by publication year and journal, drawn with a fixed seed recorded here: **seed = 20260910**. Allocation is proportional to stratum size, with a minimum of one article per year in which any article was included, and remainders assigned by the same seed.

The cap is 250 and the reason is coding capacity, not sampling theory. At roughly ten claims per article a corpus of 250 yields about 2,500 claims, each requiring extraction, typing, warrant assignment and fit, with cited-source retrieval for every W3 claim and a second coding of the originating text for W3 claims that are predictive or causal-future, and with a quarter of the corpus coded twice. A larger cap would specify a study the available effort could not finish. An incomplete corpus is a worse defect than a smaller one. This figure and its justification are fixed before the search is run so that the cap cannot be adjusted after N is known.

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
| Positioning runner-up | article | P1–P4 or none |
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

Coders: Mücahit Kutsal (investigator, first coder) and a second coder with graduate training in international relations, to be named in the change log before coding begins. The protocol requires two human coders. Any AI-assisted extraction or coding is positioned as a third reader, is never substituted for the second human coder, and is declared in the article's method section; the pilot's single coder was of that kind and is recorded as such in the workbook change log.

Double coding: minimum 25% of articles, random, fixed seed (as in §6).

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

**The freeze event.** The protocol is frozen by an annotated Git tag named `preregistration-v1` applied to a specific commit, published as a GitHub release and archived to Zenodo. From that tag onward, every change to this document is made in a later commit and logged in §14 with date and reason. The frozen text remains permanently retrievable at the tagged commit.

**Snapshots, and why they are not the freeze.** Two releases were archived on 10 September 2026, under DOIs 10.5281/zenodo.22696658 and 10.5281/zenodo.22697017. Both were taken before the codebook decisions in §16 were settled and before the sampling seed in §6 was chosen. Presenting either as a pre-registration would assert that the design was fixed when it was not, which is the exact failure this article was written to measure. They are therefore recorded as dated snapshots and superseded, not deleted. The freeze is a third, later deposit.

**Tag form.** Both snapshot tags were created as lightweight tags and so carry no tagger date of their own; for those deposits the authoritative timestamp is the Zenodo publication date. The freeze tag is annotated (`git tag -a`), so that the freeze carries a date in the repository as well as in the archive.

**Separate records.** The two snapshots were published as independent Zenodo records rather than as versions of one concept, so no concept DOI links them. The article therefore cites the freeze DOI directly and lists the snapshot DOIs alongside it, rather than relying on a version chain to make the history visible.

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
| 1 | Boundary rule between W6 (expert judgment) and W3 citing journalism, with two worked examples in the codebook | **closed** 2026-09-10: the test is whether the cited source offers judgment (W6) or reports fact (W3). Two worked examples and the boundary case of an expert quoted in a news report are in Appendix A.4. Peer-review status is recorded in its own field and does not enter the sub-code. |
| 2 | Decision tree for the P1/P4 boundary | **closed** 2026-09-10: framework or agenda language does not on its own place an article in P4. The test is whether the evidence presented could have come out against the argument. Five-step tree in Appendix A.7, with a runner-up code recorded where the decision is close. |
| 3 | Sampling seed for §6 | **closed** 2026-09-10: seed = 20260910, fixed before the search. |
| 4 | Licence for text, data and code | **closed** 2026-09-10: CC BY 4.0 for text, protocol, codebook and data; MIT for the analysis script. Recorded in LICENSE. |
| 5 | Coder names recorded in §9 | **closed** 2026-09-10: investigator named; second coder to be named in the change log before coding begins, with the AI-as-third-reader rule stated. |
| 6 | Whether the §6 stratified sample is capped at 400 or at a lower figure | **closed** 2026-09-10: capped at 250, on coding-capacity grounds stated in §6. |
| 7 | Confirmation that Web of Science Core Collection and Scopus are accessible | **not blocking.** §3 now carries an access contingency declared in advance, so the protocol is complete whichever way access falls. Access is still to be confirmed and the outcome recorded in §14, but the freeze does not wait on it. |

All seven items are settled. Items 1, 2 and 3 bore directly on results, the first two on coder agreement and the third on which articles enter the sample; item 6 determined whether the study is completable at all. None could have been settled after coding began without the change being a departure from the pre-registration rather than a part of it, which is why the freeze waited on them.

All seven were closed before the tag was applied. The protocol was frozen on 10 September 2026 at commit `a99fbb2`; see §1 for the deposit record.
