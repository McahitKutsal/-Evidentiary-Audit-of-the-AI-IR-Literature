"""
Reliability and analysis for the evidentiary audit.

Usage:
    python 03_reliability_and_analysis.py 02_coding_workbook.xlsx

Requires: pandas, numpy, openpyxl (preinstalled in most environments).
Krippendorff's alpha is implemented here directly (nominal metric), so no extra package is needed.

What it does:
  1. Nominal Krippendorff's alpha per variable on double-coded claims
     (rows in Claims sheet sharing claim_id but with different coder values).
  2. Unitising agreement: for double-coded articles, compares the number of
     claims each coder extracted per article and reports the share of articles
     with identical counts plus mean absolute difference. (Full unitising alpha
     requires character-offset segmentation; see note at the bottom.)
  3. Descriptive tables for Findings 6.2–6.5.
  4. Spearman rho with bootstrapped CI between within-year citation rank and
     article-level share of adequate fit (Finding 6.6).
"""
import sys
import numpy as np
import pandas as pd

ALPHA_THRESHOLD = 0.70
VARIABLES = ["claim_type", "primary_warrant", "w3_subcode", "positioning",
             "fit_final", "scope_conditions", "conjectural_status", "falsifier",
             "canonical_claim_id", "citation_valence"]


def krippendorff_alpha_nominal(units):
    """units: list of lists; each inner list holds the values given to one unit by different coders.
    Units with fewer than two values are ignored."""
    units = [[v for v in u if pd.notna(v) and v != ""] for u in units]
    units = [u for u in units if len(u) >= 2]
    if not units:
        return float("nan")
    values = sorted({v for u in units for v in u})
    idx = {v: i for i, v in enumerate(values)}
    k = len(values)
    o = np.zeros((k, k))
    for u in units:
        m = len(u)
        for i, a in enumerate(u):
            for j, b in enumerate(u):
                if i != j:
                    o[idx[a], idx[b]] += 1.0 / (m - 1)
    n = o.sum()
    nc = o.sum(axis=1)
    do = sum(o[i, j] for i in range(k) for j in range(k) if i != j)
    de = sum(nc[i] * nc[j] for i in range(k) for j in range(k) if i != j) / (n - 1)
    if de == 0:
        return 1.0
    return 1 - do / de


def main(path):
    claims = pd.read_excel(path, sheet_name="Claims")
    articles = pd.read_excel(path, sheet_name="Articles")
    claims = claims[claims["claim_id"].notna()]

    # ---- 1. Variable reliability ----
    print("\n== Krippendorff's alpha (nominal), double-coded claims ==")
    for var in VARIABLES:
        if var not in claims.columns:
            continue
        units = [g[var].tolist() for _, g in claims.groupby("claim_id") if g["coder"].nunique() >= 2]
        a = krippendorff_alpha_nominal(units)
        flag = "" if (np.isnan(a) or a >= ALPHA_THRESHOLD) else "  <-- below threshold, revise and re-code"
        print(f"{var:22s} alpha = {a:.3f}  (n units = {len(units)}){flag}")

    # ---- 2. Unitising agreement ----
    print("\n== Unitising agreement (claims extracted per article, by coder) ==")
    dc = articles[articles["double_coded"].astype(str).str.lower() == "yes"]["article_id"]
    counts = claims[claims["article_id"].isin(dc)].groupby(["article_id", "coder"]).size().unstack(fill_value=0)
    if counts.shape[1] >= 2:
        c1, c2 = counts.iloc[:, 0], counts.iloc[:, 1]
        print(f"articles double-coded: {len(counts)}")
        print(f"identical claim count: {(c1 == c2).mean():.2%}")
        print(f"mean |difference|:     {(c1 - c2).abs().mean():.2f}")
    else:
        print("fewer than two coders found on double-coded articles")

    # ---- 3. Descriptives (use one coder's final row per claim: first row) ----
    final = claims.groupby("claim_id").first().reset_index()
    print("\n== Claim types ==");   print(final["claim_type"].value_counts(normalize=True).round(3))
    print("\n== Primary warrant =="); print(final["primary_warrant"].value_counts(normalize=True).round(3))
    print("\n== Fit (final) ==");   print(final["fit_final"].value_counts(normalize=True).round(3))
    print("\n== Fit for causal claims in P1 articles ==")
    print(final[(final["claim_type"] == "causal") & (final["positioning"] == "P1")]["fit_final"].value_counts(normalize=True).round(3))

    ind = final[final["scope_conditions"].isin([0, 1, "0", "1"])].copy()
    for c in ["scope_conditions", "conjectural_status", "falsifier"]:
        ind[c] = ind[c].astype(int)
    if len(ind):
        print("\n== Declared-forecast indicators (eligible claims) ==")
        print(ind[["scope_conditions", "conjectural_status", "falsifier"]].mean().round(3))
        allthree = (ind[["scope_conditions", "conjectural_status", "falsifier"]].sum(axis=1) == 3).mean()
        none = (ind[["scope_conditions", "conjectural_status", "falsifier"]].sum(axis=1) == 0).mean()
        print(f"declared forecasts (3/3): {allthree:.3f}   circulated findings (0/3): {none:.3f}")

    # ---- 4. Citation rank vs adequate-fit share ----
    share = final.groupby("article_id")["fit_final"].apply(lambda s: (s == "adequate").mean()).rename("adequate_share")
    art = articles.merge(share, on="article_id", how="inner")
    art = art[art["citations_per_year"].notna()]
    if len(art) >= 10:
        art["rank_within_year"] = art.groupby("year")["citations_per_year"].rank(ascending=False)
        from scipy.stats import spearmanr
        rho = spearmanr(art["rank_within_year"], art["adequate_share"]).correlation
        rng = np.random.default_rng(20260907)
        boots = []
        for _ in range(2000):
            b = art.sample(len(art), replace=True, random_state=int(rng.integers(1e9)))
            boots.append(spearmanr(b["rank_within_year"], b["adequate_share"]).correlation)
        lo, hi = np.nanpercentile(boots, [2.5, 97.5])
        print(f"\n== Spearman rho, within-year citation rank vs adequate-fit share ==")
        print(f"rho = {rho:.3f}   95% bootstrap CI [{lo:.3f}, {hi:.3f}]   n = {len(art)}")
        print("(rank 1 = most cited; negative rho means more cited articles have higher adequate share)")
    else:
        print("\n(fewer than 10 articles with citation data; skipping rank analysis)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "02_coding_workbook.xlsx")

# NOTE on unitising alpha: Krippendorff's unitising alpha (alpha_u) needs each coder's
# claim segments recorded as character offsets in the source text. If you want the full
# statistic, add two columns to Claims (char_start, char_end) and use the
# `krippendorff` package's `alpha(..., level_of_measurement='unitizing')` or
# implement Krippendorff (2018, ch. 12). The per-article count comparison above is the
# minimum the protocol requires and is reported as such.
