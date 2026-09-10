# Forecast or Finding? An Evidentiary Audit of the AI-IR Literature

Materials for a protocol-registered, claim-level evidentiary audit of peer-reviewed scholarship on artificial intelligence in international relations, 2015-2025.

The study codes individual **claims** (not articles) by claim type, warrant type, the author's own epistemological positioning, and the fit between claim and warrant assessed relative to that positioning. Its conceptual contribution is the distinction between a **declared forecast**, which states its scope conditions, signals its conjectural status, and identifies a falsifier, and a **circulated finding**, which is the same proposition travelling without those markers.

**Status: pre-data.** No corpus has been screened or coded. The article draft carries unfilled `[VERİ: ...]` placeholders throughout its findings sections. Only a two-article, 21-claim pilot exists, and that pilot is explicitly not protocol data.

## Contents

| File | What it is |
|---|---|
| `forecast_or_finding_ai_ir_evidentiary_audit.md` | Article draft. Findings sections are placeholders. |
| `01_protocol_preregistration.md` | The pre-registration protocol. §15 defines the deposit and freeze mechanism. |
| `02_coding_workbook.xlsx` | The coding instrument. Sheets: Legend, Fit_Matrix, Canonical_Claims, Articles, Claims, Change_Log, Summary. |
| `03_reliability_and_analysis.py` | Krippendorff's alpha, descriptive tables, and the citation-rank analysis. |

The repository holds the research materials. Project management documents, working notes and task lists are kept outside it and are not part of the deposit. Nothing they contain is load-bearing for the study: the protocol is self-contained, every design decision is recorded in the protocol change log and in Appendix D of the article, the pilot's twenty-one coded claims are in the `Claims` sheet of the workbook, and the identity of the pilot coder is recorded in the workbook's `Change_Log`.

## Protocol freeze

This project uses a public Git repository plus a Zenodo-archived release in place of a registry deposit. The protocol is frozen by an annotated tag named `preregistration-v1`, and the freeze is not treated as complete until a Zenodo DOI has been minted from the corresponding release.

The reasoning, and the limits of this mechanism, are stated in full in §15 of the protocol. In short: a Git commit SHA is a cryptographic hash over the repository tree and its history, so the frozen text cannot be altered without breaking every descendant commit; but a Git history is not tamper-evident against its own owner, who can rewrite it. The Zenodo archive, which the depositor cannot revise once published, is what supplies the property a registry deposit would have supplied.

### Deposits

| Deposit | Tag | Commit | Date | DOI | Status |
|---|---|---|---|---|---|
| Snapshot 1 | `protocol-freeze` | `f507074` | 2026-09-10 | [10.5281/zenodo.22696658](https://doi.org/10.5281/zenodo.22696658) | superseded |
| Snapshot 2 | `protocol-freeze-v1` | `2e70926` | 2026-09-10 | [10.5281/zenodo.22697017](https://doi.org/10.5281/zenodo.22697017) | superseded |
| **The freeze** | `preregistration-v1` | pending | pending | pending | pending |

**Neither snapshot is the pre-registration.** Both were deposited before the sampling seed was chosen and before the codebook decisions listed in §16 of the protocol were settled. They are dated public snapshots, recorded here because they exist and are citable; presenting either as a pre-registration would assert that the design was fixed when it was not, which is the failure this article was written to measure. They are left in place rather than deleted. The freeze is a third deposit, tagged `preregistration-v1`, and that tag alone is what the article cites.

**Freeze status: not yet frozen.** The instrument defects that would have made a freeze meaningless have been repaired and are recorded in the workbook's `Change_Log` and in Appendix D of the article. The conditions for the freeze are listed in §16 of the protocol. Anyone reading this repository before v2 should treat the protocol as a working draft.

### Verifying the freeze

Once the tag exists, any reader can verify it:

```bash
git clone https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature
cd -Evidentiary-Audit-of-the-AI-IR-Literature
git rev-parse preregistration-v1^{commit}       # must equal the SHA published in the article
git show preregistration-v1                                   # the frozen protocol text
```

Then confirm that the Zenodo record for that release contains the same tree.

## Running the analysis

```bash
pip install pandas numpy openpyxl scipy
python 03_reliability_and_analysis.py 02_coding_workbook.xlsx
```

`scipy` is used only for the Spearman correlation in the citation analysis; everything else, including Krippendorff's alpha, is implemented in the script itself.

## Reporting rules

Findings are reported at aggregate level only. Individual articles are named only as positive examples. No named negative generalisations are made about authors or schools.

## Licence

Text, protocol, codebook and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Analysis script: MIT.

See `LICENSE`. This matches the licence recorded on the Zenodo deposit.
