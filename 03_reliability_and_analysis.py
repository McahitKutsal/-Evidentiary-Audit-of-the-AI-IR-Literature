"""
Reliability and analysis for the evidentiary audit.

Usage:
    python 03_reliability_and_analysis.py 02_coding_workbook.xlsx

Requires: pandas, numpy, openpyxl, scipy.
Krippendorff's alpha is implemented here directly (nominal metric), so no extra package is needed
for that part; scipy is used only for the Spearman correlation in section 5.

What it does:
  1. Nominal Krippendorff's alpha per variable on double-coded claims
     (rows in Claims sheet sharing claim_id but with different coder values).
  2. Unitising agreement: for double-coded articles, compares the number of
     claims each coder extracted per article and reports the share of articles
     with identical counts plus mean absolute difference. (Full unitising alpha
     requires character-offset segmentation; see note at the bottom.)
  3. Descriptive tables for Findings 6.2-6.5.
  4. Transmission table for Finding 6.5 / Table 4: declared-forecast indicators
     in the originating text versus the citing text, for W3 claims.
  5. Spearman rho with bootstrapped CI between within-year citation standing and
     article-level share of adequate fit (Finding 6.6).

A note on reading this output: a reported alpha of "not computed" is not a pass.
It means no double-coded units were found for that variable, and the protocol's
alpha >= 0.70 gate has therefore not been applied to it at all.
"""
import sys
import numpy as np
import pandas as pd

ALPHA_THRESHOLD = 0.70
VARIABLES = ["claim_type", "primary_warrant", "w3_subcode", "positioning",
             "fit_final", "scope_conditions", "conjectural_status", "falsifier",
             "canonical_claim_id", "citation_valence", "w4_developed",
             "orig_scope_conditions", "orig_conjectural_status", "orig_falsifier",
             "w3_source_peer_reviewed", "secondary_claim_type"]
INDICATORS = ["scope_conditions", "conjectural_status", "falsifier"]
ORIG_INDICATORS = ["orig_scope_conditions", "orig_conjectural_status", "orig_falsifier"]


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
        # Every coder gave every unit the same value. Alpha is undefined here rather
        # than perfect: with no variance there is nothing for chance to explain.
        return float("nan")
    return 1 - do / de


def as_binary(series):
    """Indicator columns hold 1, 0 or the string 'NA'. Return a float series with
    NA -> NaN, tolerating either numeric or text storage."""
    return pd.to_numeric(series, errors="coerce")


def main(path):
    claims = pd.read_excel(path, sheet_name="Claims")
    articles = pd.read_excel(path, sheet_name="Articles")
    claims = claims[claims["claim_id"].notna()]

    # ---- 1. Variable reliability ----
    print("\n== Krippendorff's alpha (nominal), double-coded claims ==")
    any_computed = False
    for var in VARIABLES:
        if var not in claims.columns:
            print(f"{var:26s} column absent from workbook")
            continue
        units = [g[var].tolist() for _, g in claims.groupby("claim_id") if g["coder"].nunique() >= 2]
        a = krippendorff_alpha_nominal(units)
        if np.isnan(a):
            print(f"{var:26s} alpha = not computed  (n units = {len(units)})"
                  f"  <-- NOT a pass; the threshold has not been applied")
        else:
            any_computed = True
            flag = "" if a >= ALPHA_THRESHOLD else "  <-- below threshold, revise and re-code"
            print(f"{var:26s} alpha = {a:.3f}  (n units = {len(units)}){flag}")
    if not any_computed:
        print("\n  WARNING: no variable had two or more coders on any claim_id.")
        print("  Either double coding has not been done, or the two coders did not")
        print("  reconcile claim boundaries onto shared claim_ids. Reliability is")
        print("  UNKNOWN, not acceptable. See the note on unitising at the bottom.")

    # ---- 2. Unitising agreement ----
    print("\n== Unitising agreement (claims extracted per article, by coder) ==")
    dc = articles[articles["double_coded"].astype(str).str.lower() == "yes"]["article_id"]
    counts = claims[claims["article_id"].isin(dc)].groupby(["article_id", "coder"]).size().unstack(fill_value=0)
    if counts.shape[1] >= 2:
        if counts.shape[1] > 2:
            print(f"note: {counts.shape[1]} coders present; comparing the first two "
                  f"({counts.columns[0]} vs {counts.columns[1]}) and ignoring the rest")
        c1, c2 = counts.iloc[:, 0], counts.iloc[:, 1]
        print(f"articles double-coded: {len(counts)}")
        print(f"identical claim count: {(c1 == c2).mean():.2%}")
        print(f"mean |difference|:     {(c1 - c2).abs().mean():.2f}")
    else:
        print("fewer than two coders found on double-coded articles")

    # ---- 3. Descriptives ----
    # One intact row per claim. drop_duplicates keeps a whole row from a single
    # coder; groupby().first() would take the first non-null value per column
    # independently and could splice two coders' judgments into one record that
    # neither coder made.
    dupes = claims["claim_id"].duplicated().sum()
    final = claims.drop_duplicates(subset="claim_id", keep="first").copy()
    if dupes:
        print(f"\nnote: {dupes} duplicate claim_id rows; descriptives use the first "
              f"coder's intact row per claim. Reconcile before reporting.")

    print("\n== Claim types ==")
    print(final["claim_type"].value_counts(normalize=True).round(3))
    print("\n== Primary warrant ==")
    print(final["primary_warrant"].value_counts(normalize=True).round(3))
    print("\n== Fit (final) ==")
    print(final["fit_final"].value_counts(normalize=True).round(3))
    print("\n== Fit for causal claims in P1 articles ==")
    print(final[(final["claim_type"] == "causal") & (final["positioning"] == "P1")]["fit_final"]
          .value_counts(normalize=True).round(3))

    if "p4_causal_flag" in final.columns:
        n_flag = (final["p4_causal_flag"].astype(str) == "P4-CAUSAL").sum()
        print(f"\nP4 causal claims (reported separately, not excluded): {n_flag}")

    ind = final.copy()
    for c in INDICATORS:
        ind[c] = as_binary(ind[c])
    ind = ind.dropna(subset=INDICATORS)
    if len(ind):
        print("\n== Declared-forecast indicators (eligible claims) ==")
        print(ind[INDICATORS].mean().round(3))
        tot = ind[INDICATORS].sum(axis=1)
        print(f"declared forecasts (3/3): {(tot == 3).mean():.3f}   "
              f"circulated findings (0/3): {(tot == 0).mean():.3f}   n = {len(ind)}")

    # ---- 4. Transmission: originating vs citing text (Table 4) ----
    print("\n== Table 4. Declared-forecast indicators, originating vs citing text (W3 claims) ==")
    if not all(c in final.columns for c in ORIG_INDICATORS):
        print("originating-text columns absent from workbook; cannot compute")
    else:
        w3 = final[final["primary_warrant"] == "W3"].copy()
        for c in INDICATORS + ORIG_INDICATORS:
            w3[c] = as_binary(w3[c])
        print(f"{'Indicator':24s} {'orig %':>8s} {'citing %':>9s} {'loss pp':>8s} {'n pairs':>8s}")
        for orig, cite in zip(ORIG_INDICATORS, INDICATORS):
            pair = w3.dropna(subset=[orig, cite])
            if not len(pair):
                print(f"{cite:24s} {'-':>8s} {'-':>9s} {'-':>8s} {0:>8d}")
                continue
            o, c = pair[orig].mean(), pair[cite].mean()
            print(f"{cite:24s} {o*100:8.1f} {c*100:9.1f} {(o-c)*100:8.1f} {len(pair):8d}")
        unresolved = (w3[ORIG_INDICATORS[0]].isna()).sum()
        print(f"\nW3 claims whose originating text was not retrieved: {unresolved} of {len(w3)}")
        if unresolved == len(w3) and len(w3):
            print("H2 and RQ3 cannot be evaluated until originating texts are coded.")

    # ---- 5. Citation standing vs adequate-fit share ----
    fit_known = final[final["fit_final"].notna()]
    share = (fit_known.groupby("article_id")["fit_final"]
             .apply(lambda s: (s == "adequate").mean()).rename("adequate_share"))
    art = articles.merge(share, on="article_id", how="inner")
    art = art[art["citations_per_year"].notna()]
    if len(art) >= 10:
        # Percentile rank within year, so that articles from years with different
        # numbers of publications are on one scale. Pooling raw ranks would let a
        # rank of 5 mean "top decile" in a thin year and "median" in a thick one.
        art["pct_rank_within_year"] = art.groupby("year")["citations_per_year"].rank(
            ascending=False, pct=True)
        from scipy.stats import spearmanr
        rho = spearmanr(art["pct_rank_within_year"], art["adequate_share"]).correlation
        rng = np.random.default_rng(20260907)
        boots = []
        for _ in range(2000):
            b = art.sample(len(art), replace=True, random_state=int(rng.integers(1e9)))
            boots.append(spearmanr(b["pct_rank_within_year"], b["adequate_share"]).correlation)
        lo, hi = np.nanpercentile(boots, [2.5, 97.5])
        print("\n== Spearman rho, within-year citation standing vs adequate-fit share ==")
        print(f"rho = {rho:.3f}   95% bootstrap CI [{lo:.3f}, {hi:.3f}]   n = {len(art)}")
        print("Percentile rank runs 0 = most cited to 1 = least cited, so:")
        print("  NEGATIVE rho = more cited articles have a HIGHER adequate-fit share")
        print("                 (reception favours better-warranted claims)")
        print("  POSITIVE rho = more cited articles have a LOWER adequate-fit share")
        print("                 (reception favours worse-warranted claims)")
        print("Protocol H3 conjectures that rho is not positive. Report whichever way it falls.")
    else:
        print(f"\n({len(art)} articles with citation data; need 10, skipping rank analysis)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "02_coding_workbook.xlsx")

# NOTE on unitising alpha: Krippendorff's unitising alpha (alpha_u) needs each coder's
# claim segments recorded as character offsets in the source text. If you want the full
# statistic, add two columns to Claims (char_start, char_end) and use the
# `krippendorff` package's `alpha(..., level_of_measurement='unitizing')` or
# implement Krippendorff (2018, ch. 12). The per-article count comparison above is the
# minimum the protocol requires and is reported as such.
#
# NOTE on claim_id: the alpha in section 1 pairs coders on a shared claim_id. Two coders
# extracting independently will not produce matching ids on their own, so a reconciliation
# pass must assign a shared claim_id to the segments both coders identified before this
# script is run. Without it every alpha reports "not computed", which is why that state is
# printed as a warning and not as a pass.
