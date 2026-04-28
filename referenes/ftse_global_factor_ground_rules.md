# FTSE Global Factor Index Series Ground Rules

Source: `ftse-global-factor-index-series-ground-rules.pdf`

This document is a **rulebook for FTSE's full global factor family**, not a research paper. Its job is to specify how FTSE defines factors, converts them into z-scores, turns factor scores into investable portfolio weights, constrains those weights, and maintains the indexes over time.

For the Aapryl project, this is one of the most useful documents for `model rules` and `implementation steps`. It is much less about discovering the best factor academically and much more about how a serious provider actually builds and runs factor portfolios.

This note is written as a step-by-step working document, not a loose summary. The goal is to capture what FTSE is doing, why the steps exist, and what parts of the rulebook matter most for your project.

All `Theoretical Example` blocks below are illustrative and invented. They are included only to make the rulebook easier to visualize and should not be read as FTSE examples or FTSE results.

## What This Document Answers

This rulebook answers several project-relevant questions:

- how FTSE defines each major factor mathematically
- how FTSE treats missing data and outliers
- how FTSE combines multiple factors into one index
- how FTSE turns factor scores into benchmark-relative weights
- how FTSE constrains country and industry drift
- how FTSE controls concentration, capacity, and turnover
- how FTSE handles `fixed tilt` versus `target exposure` index designs
- how FTSE maintains narrow versus broad factor indexes
- how FTSE reviews and maintains factor indexes tied to `Russell 1000`, `Russell 2000`, and other universes

## What This Document Does Not Answer

This rulebook is very useful, but it does **not** answer the whole Aapryl assignment by itself. It does not tell you:

- which custom factor definitions are best for `Deep Value`
- how to define `Aggressive Growth`
- how to use `active-manager exposures` to set region and sector limits
- whether a staged `2-step` design is better than a simultaneous tilt system for your use case
- how to implement the methodology specifically in FactSet
- how Aapryl should operationalize monthly portfolio updates in production

This document is best understood as FTSE's answer to:

**"How do you run a family of factor indexes as benchmark-relative, constrained tilt portfolios?"**

## Methodology in Order

## 1. Start from an Eligible Underlying Universe

**What FTSE Does**  
FTSE defines each factor index off an existing eligible universe coming from its own benchmark families, including:

- FTSE Global Equity Index Series
- FTSE China A All Cap Index Series
- FTSE UK Index Series
- FTSE/JSE Africa Index Series
- Russell US Equity Indices
- FTSE EPRA Nareit Global Real Estate Index Series

All eligible lines of the same company can be included. For the `FTSE All-World ex CW Balanced Factor Index`, FTSE also applies controversial-weapons exclusions.

**Why This Step Exists**  
FTSE wants the factor index to be benchmark-anchored, not unconstrained. The parent universe defines the investable opportunity set before factor tilting begins.

**What This Means for Us**  
This is directly relevant because your project also starts from specific benchmark families, especially `Russell 1000`, `Russell 2000`, `MSCI EAFE`, and `MSCI EM`. FTSE is reinforcing the idea that factor portfolios should begin from a benchmark universe, not from a free-form stock search.

**Theoretical Example**  
If FTSE is building a Russell 1000 quality factor index, it begins with the Russell 1000 eligible universe and tilts that universe rather than selecting from all US-listed stocks.

**Reference**  
- Section 4, `Eligible securities`, p. 8
- Section 1, `Introduction`, p. 3

## 2. Set a Data Cut-Off Date Before the Review

**What FTSE Does**  
The data cut-off date for factor data is the close of business on the last business day of the month prior to the review month.

**Why This Step Exists**  
FTSE needs a consistent observation point for factor calculations before the review is implemented.

**What This Means for Us**  
This is an implementation detail, but it matters a lot in practice. Any future Aapryl process will also need exact observation dates, not just a statement that portfolios update monthly.

**Theoretical Example**  
If a factor review happens in September, FTSE uses the factor data as of the last business day of August rather than letting metrics float during the review month.

**Reference**  
- Section 5, `Factor construction`, p. 9

## 3. Convert Raw Factor Data into Cross-Sectional Z-Scores

**What FTSE Does**  
FTSE normalizes factor values cross-sectionally into z-scores within each eligible universe:

\[
Z_{F,i} = \frac{F_i - \mu_F}{\sigma_F}
\]

FTSE then:

- truncates z-scores above `+3` or below `-3`
- re-normalizes after truncation
- repeats the process until all z-scores lie in `[-3, 3]`

For multi-component factors, FTSE averages the non-missing sub-factor z-scores and then re-normalizes the average.

**Why This Step Exists**  
FTSE needs all factors to be on a common scale before combining or tilting them.

**What This Means for Us**  
This is directly relevant to your manager's email because it is a concrete provider implementation of the `z-score` framework. It is also evidence for the `composite / simultaneous tilt` side of the construction debate.

**Theoretical Example**  
A stock might be 1.4 standard deviations above the universe mean on value and 0.8 above on quality. FTSE wants those standardized signals before it builds a multi-factor tilt.

**Reference**  
- Rule 5.2.1, p. 9
- Rule 5.2.2, p. 9

## 4. Apply Explicit Missing-Data Rules

**What FTSE Does**  
FTSE assigns:

- a neutral z-score of `0` for missing factor data on all factors except `yield`
- a z-score of `-3` for missing or zero `yield`

**Why This Step Exists**  
FTSE wants a deterministic and scalable missing-data policy across the factor family.

**What This Means for Us**  
This is an important implementation detail. It shows that provider methodologies often choose a mechanical missing-data treatment rather than excluding every name with partial data.

**Theoretical Example**  
If a stock is missing a quality input, FTSE does not automatically remove it from most factor models. It typically gets a neutral treatment instead.

**Reference**  
- Rule 5.2.3, p. 9

## 5. Define the Factors Themselves

**What FTSE Does**  
FTSE defines the core factors as follows:

- `Momentum`: cumulative total local return over a 12-month lookback, skipping the most recent month
- `Quality`: composite of profitability and leverage
- `Size`: negative log of full market capitalization
- `Value`: composite of cash-flow yield, earnings yield, and sales-to-price
- `Low Volatility`: negative volatility of weekly local returns
- `Yield`: log of trailing 12-month dividend yield
- `Beta`: stock beta relative to the underlying market index

For `Quality`, FTSE specifically uses:

- `ROA`
- `change in asset turnover`
- `accruals`
- `operating cash flow / total debt`

For `financials and real estate`, FTSE uses `ROA` only as the quality measure.

**Why This Step Exists**  
The rulebook needs stable production definitions for each factor.

**What This Means for Us**  
This section confirms the production version of the quality logic you saw in the FTSE quality white paper. It is especially relevant because it shows how FTSE operationalizes quality once the research phase is over.

**Theoretical Example**  
A non-financial stock can score on all four quality components, while a bank would use only ROA in FTSE's quality framework.

**Reference**  
- Rules 5.3 to 5.9, pp. 9-11
- Rule 5.4, pp. 10-11

## 6. Choose an Index Architecture: Fixed Tilt or Target Exposure

**What FTSE Does**  
FTSE organizes the factor family into two major architecture types:

- `Fixed Tilt Indices`
- `Target Exposure Indices`

In a `Fixed Tilt Index`, the tilt strengths are fixed numeric constants, such as `1`, `2`, or `0.5`.

In a `Target Exposure Index`, the tilt strengths are solved so the final index hits specified active factor-exposure targets.

For target-exposure indexes, FTSE uses `Exp(Z)` as the mapping from z-scores to tilt multipliers and solves for the tilt strengths that meet the desired active exposure targets and any beta target or beta band.

**Why This Step Exists**  
FTSE wants flexibility in how strongly the factor is expressed. Some indexes are defined by fixed recipes, while others are defined by exposure objectives.

**What This Means for Us**  
This is very important for Aapryl. It shows that there are at least two serious ways to build factor portfolios:

- use a fixed recipe
- target a desired factor exposure directly

That is a more sophisticated framing than just `rank vs 2-step`.

It also shows that target-exposure design is not just a high-level idea. FTSE explicitly treats it as a constrained iterative solve. If the requested exposures cannot be met exactly, the methodology has a fallback ladder: after `100` iterations FTSE cuts targeted active exposures by `2.5%`; after `10` such cuts it increases the turnover target by `50%`; then, if needed, it removes the turnover target entirely and continues reducing exposures in `2.5%` steps up to `40` times.

**Theoretical Example**  
A fixed-tilt quality index might always use quality tilt strength `1`. A target-exposure quality index might instead try to hit a `0.4 sigma` active quality target, then gradually relax that target if country, industry, capacity, and turnover constraints make the original request infeasible.

**Reference**  
- Rules 6.1.2 to 6.1.3, p. 12
- Rule 6.2.3, p. 13
- Rule 6.6.2, p. 16
- Tables three and four, pp. 30-32

## 7. Build the Initial Factor Tilt from Market-Cap Weights

**What FTSE Does**  
FTSE starts with market-cap weights and applies factor tilts multiplicatively. The general factor-tilt weight is:

\[
W_{1i} = \frac{1}{\Pi}
\times S_{V,i}^n
\times S_{Q,i}^p
\times S_{M,i}^q
\times S_{LV,i}^r
\times S_{S,i}^s
\times S_{Y,i}^t
\times S_{C,i}^u
\times S_{\beta,i}^v
\times W_{Mi}
\]

For fixed tilt indices:

- FTSE uses a cumulative-normal mapping from z-score to positive weight multiplier

For target exposure indices:

- FTSE uses `Exp(Z)` and solves tilt strengths to hit exposure targets

**Why This Step Exists**  
This is the central portfolio-construction engine of the rulebook. FTSE is not selecting top names and equal-weighting them. It is tilting benchmark weights simultaneously across factors.

**What This Means for Us**  
This is the most important architectural lesson in the file. It is a strong real-world example of `simultaneous multi-factor tilt`, which sits on the opposite side of the construction debate from Fidelity's staged `quality gate then value rank` approach.

**Theoretical Example**  
If a stock has above-average value and quality z-scores, FTSE increases its weight through the product of the value and quality tilts rather than by giving it a simple additive score.

**Reference**  
- Rule 6.1.1, p. 12
- Rules 6.2.1 to 6.2.3, pp. 13-14

## 8. Apply Country and Industry Tilts to Stay Near the Benchmark

**What FTSE Does**  
After factor tilts, FTSE applies `country` and `industry` tilts so that final country and industry weights remain inside benchmark-relative bounds.

The bounds are defined using lower and upper formulas that depend on benchmark weight and two parameters:

- `P`
- `Q`

These create either:

- `neutral` country/industry targets
- `banded` country/industry targets

If a reallocation creates new breaches, FTSE iteratively relaxes or reassigns weights until a feasible solution is found.

**Why This Step Exists**  
FTSE wants factor portfolios to reflect factor exposure without turning into uncontrolled country or industry bets.

**What This Means for Us**  
This is highly relevant to your manager's interest in sector and region limits. FTSE gives you a concrete provider framework for benchmark-relative country and industry constraints. It does not use active-manager-informed limits, but it gives a mechanical baseline.

**Theoretical Example**  
If a quality tilt overweights healthcare and underweights energy too aggressively, FTSE's industry constraints pull those sector weights back into acceptable ranges.

**Reference**  
- Rules 6.3.1 to 6.3.4, pp. 13-14
- Rules 6.8 and 6.9 tables, pp. 17-32

## 9. Apply Capacity and Maximum-Weight Constraints

**What FTSE Does**  
FTSE then applies:

- a `maximum stock capacity ratio`
- a `maximum company weight`
- later a `minimum stock weight`

The default maximum stock capacity ratio is `20`, unless explicitly changed for a specific index.

Weights are iteratively capped and renormalized until they converge.

**Why This Step Exists**  
FTSE wants the factor portfolio to remain investable and not become overly concentrated in a few names.

**What This Means for Us**  
This is important for Aapryl because any real production portfolio will need concentration and capacity controls, especially in smaller or more factor-concentrated universes.

**Theoretical Example**  
If a mega-cap stock would become too dominant after factor tilts, FTSE cuts it back and redistributes the excess weight across the rest of the portfolio.

**Reference**  
- Rule 6.4.1, pp. 14-15

## 10. Apply a Turnover Tilt Instead of Always Doing a Full Rebalance

**What FTSE Does**  
FTSE calculates the two-way turnover between current weights and target weights:

\[
T = \sum |W_{3i} - W_{0i}|
\]

It then defines:

\[
\alpha = \min \left(1, \frac{TTO}{T}\right)
\]

and uses a partial-rebalance formula:

\[
W_{4i} = \alpha W_{3i} + (1-\alpha)W_{0i}
\]

If turnover is within the allowed maximum, then `alpha = 1` and FTSE performs a full rebalance.

**Why This Step Exists**  
FTSE wants to control turnover directly rather than allowing the model to fully reset the portfolio whenever factor signals change.

**What This Means for Us**  
This is a major operational idea for Aapryl. It shows that turnover control can be embedded mathematically in the rebalancing process rather than handled only through selection buffers.

**Theoretical Example**  
If the unconstrained new portfolio would require too much trading, FTSE only moves partway from the current weights toward the target weights.

**Reference**  
- Rule 6.5.1, p. 15

## 11. Apply Minimum Stock Weight Rules

**What FTSE Does**  
FTSE removes securities whose final weight would fall below a minimum-security threshold. Excess weight is redistributed across the remaining constituents.

For target-exposure indices, FTSE may rerun the optimization-like tilt process after applying the minimum weight threshold so that factor targets remain as close as possible to the design.

**Why This Step Exists**  
Very tiny weights may not be practical or meaningful in a live index.

**What This Means for Us**  
This is another important production detail. A theoretically optimal portfolio can still be operationally poor if it contains too many tiny weights.

**Theoretical Example**  
If the model wants to hold a stock at only 0.01 basis points, FTSE may zero it out and reallocate that tiny weight elsewhere.

**Reference**  
- Rules 6.7.1 to 6.7.2, p. 16

## 12. Use Different Parameter Tables for Different Index Families

**What FTSE Does**  
FTSE provides explicit parameter tables that specify for each index:

- factor tilt strengths
- narrow vs non-narrow construction
- country and industry constraint parameters
- minimum stock weight
- maximum company weight
- maximum two-way turnover
- review month(s)

The tables include direct examples on:

- `Russell 1000`
- `Russell 2000`
- developed markets
- emerging markets
- pure factor indexes
- mixed factor indexes
- capped factor indexes

Examples include:

- `Russell 1000 2Qual/Val 5% Capped Factor Index`
- `Russell 1000 Quality Factor Index`
- `Russell 2000 Quality Factor Index`
- `Russell 1000 Value Factor Index`
- `Russell 2000 Value Factor Index`
- `Russell 2000 0.4 Target Exposure Quality Factor Index`
- `Russell 1000 Comprehensive Equal Factor Risk Contribution Target Exposure Index`

The tables also provide directly useful parameter evidence. For example:

- `Russell 1000 2Qual/Val 5% Capped Factor Index` uses `V = 1`, `Q = 2`, `Narrow = Y`, `Max company weight = 5%`, `Max two-way turnover = 50%`, `Review = J`
- `Russell 1000 Quality Factor Index` uses a narrow construction with `Max two-way turnover = 2%`
- `Russell 2000 Quality Factor Index` also uses a narrow construction, but with `Max two-way turnover = 0.5%`

**Why This Step Exists**  
FTSE wants each live index to have an explicit, parameterized recipe.

**What This Means for Us**  
This is especially relevant because your manager specifically mentioned `Russell 1000` and `Russell 2000`. FTSE is showing concrete examples of how those universes can support pure and mixed factor products.

**Theoretical Example**  
A Russell 1000 quality-only index can have different turnover limits and review timing than a Russell 2000 multi-factor index.

**Reference**  
- Table one, pp. 17-23
- Table two, p. 25
- Table three, pp. 30-31
- Table four, pp. 28-32

## 13. Use Phased and Special Structures Where Needed

**What FTSE Does**  
Some indexes use special construction logic. For example, the `FTSE All-World ex CW Balanced Factor Index` is the equal combination of:

- a March-reviewed version
- a September-reviewed version

so the effective constituent weight is:

\[
W^*_{i,t} = 0.5 W^{Mar}_{i,t} + 0.5 W^{Sep}_{i,t}
\]

**Why This Step Exists**  
FTSE uses phased structures when it wants smoother turnover or more stable index behavior.

**What This Means for Us**  
This is relevant because it shows another operational design option: you do not always need one monolithic rebalance. A phased or staggered structure can smooth implementation.

**Theoretical Example**  
Instead of fully refreshing the same portfolio in one month, FTSE can blend two staggered review streams so the overall portfolio changes more gradually.

**Reference**  
- Rule 6.8.2, p. 26

## 14. Define Narrow Indexes Through Exposure-Contribution Ranking

**What FTSE Does**  
For `narrow` indexes, FTSE does not just pick an arbitrary top number of names. It ranks stocks by contribution to factor exposure and then shrinks the universe until one of several conditions would be violated:

- active exposure condition
- weighted capacity ratio condition
- effective N condition

Appendix A makes the thresholds explicit for single-factor narrowing:

- active exposure of the candidate narrow portfolio must stay below `2x` the broad portfolio's active exposure benchmark
- weighted capacity ratio must stay below `2.5x` the broad portfolio's weighted capacity ratio
- `Effective N` must remain above `67%` of the broad portfolio's `Effective N`

For multi-factor narrowing, FTSE ranks on a multi-factor score and repeats a similar process without the active-exposure condition.

**Why This Step Exists**  
FTSE wants a more concentrated index without destroying investability, capacity, or diversification.

**What This Means for Us**  
This is very useful if Aapryl ever wants a more concentrated version of a factor sleeve. FTSE is giving a disciplined way to concentrate without just saying "take the top 100."

**Theoretical Example**  
FTSE keeps removing the weakest contributors to factor exposure until doing so would make the portfolio too concentrated or too capacity-stressed.

**Reference**  
- Appendix A, p. 38

## 15. Review Indexes on a Defined Schedule Tied to the Underlying Family

**What FTSE Does**  
FTSE reviews indexes on defined schedules tied to the relevant benchmark family.

For factor indexes derived from FTSE underlyings:

- price cut-off is typically the Wednesday before the first Friday of the review month
- implementation is after the close on the third Friday of the review month

For factor indexes derived from Russell 1000 or Russell 2000:

- June reviews align with the Russell reconstitution schedule
- December reviews use a different price cut-off convention

Separately, FTSE states that simulated back-histories apply a `six-month lag` to realised fundamental data before launch, so the rulebook's historical results are not using fundamentals as if they were immediately known.

Company-level capping is applied at reviews where relevant.

**Why This Step Exists**  
FTSE needs review timing to be synchronized with the underlying benchmark process.

**What This Means for Us**  
This is directly relevant because your project uses Russell 1000 and Russell 2000 as primary reference benchmarks. Review timing should not be designed in isolation from the underlying benchmark calendar.

**Theoretical Example**  
If the Russell 1000 reconstitution changes the parent universe materially in June, the factor index review needs to align with that event rather than pretending the parent universe is static.

**Reference**  
- Section 7, `Periodic review of constituents`, p. 33
- Rule 6.10.1, p. 32

## 16. Handle Intra-Review Changes by Following the Underlying Index

**What FTSE Does**  
FTSE generally:

- considers additions at the next review
- removes constituents concurrently if they are removed from the underlying index
- redistributes deleted weight pro rata to the remaining constituents

**Why This Step Exists**  
The factor index remains tied to the benchmark family even between reviews.

**What This Means for Us**  
This is important for future Aapryl automation. Parent-index changes must flow through to the factor portfolio under a clear policy.

**Theoretical Example**  
If a stock is removed from the Russell 2000 between scheduled factor reviews, FTSE removes it from the related factor index at the same time.

**Reference**  
- Section 8, `Changes to constituent companies`, p. 34

## 17. Use Limited ESG Inputs Except in the Balanced ex CW Index

**What FTSE Does**  
The rulebook explicitly states that most indexes in the series do **not** use ESG objectives. The notable exception is the `FTSE All-World ex CW Balanced Factor Index`, which uses controversial-weapons exclusions driven by Sustainalytics product involvement data.

**Why This Step Exists**  
FTSE wants the rest of the factor family to remain non-ESG factor benchmarks, while allowing one special ESG-sensitive variant.

**What This Means for Us**  
This is useful because it separates `factor construction logic` from `ESG overlay logic`. If Aapryl does not want ESG embedded everywhere, FTSE shows a way to keep the core factor methodology clean and layer ESG only where needed.

**Theoretical Example**  
You could use the same core factor engine for most custom indices while applying special exclusions only to specific products.

**Reference**  
- Section 1.4, p. 3
- Section 9, `ESG data inputs`, p. 35

## 18. Maintain Weights Through Standard Index Calculation and Corporate-Action Rules

**What FTSE Does**  
FTSE calculates the index using a standard divisor-based formula:

\[
\sum_{i=1}^{N} \frac{p_i \times e_i \times s_i \times f_i \times c_i}{d}
\]

Corporate actions generally preserve constituent weights across stock splits, rights issues, share changes, and free-float changes, unless special treatment is required under the non-market-cap-weighted corporate actions guide.

**Why This Step Exists**  
The factor index still needs a standard operational index-calculation framework once weights have been set.

**What This Means for Us**  
This is less important for factor design itself, but very important for eventual production maintenance and automation.

**Theoretical Example**  
A stock split should not change the economic weight of a holding in the factor index even though the share count and price change.

**Reference**  
- Section 10, `Corporate actions and events`, p. 36
- Section 11, `Indices algorithm and calculation method`, p. 37

## Key Design Conclusions

- This document is FTSE's strongest statement of how to build factor portfolios as `constrained benchmark-relative tilts`.
- FTSE's architecture is much closer to `simultaneous multi-factor tilting` than to a staged `2-step` selection process.
- Country and industry control are embedded directly in the construction engine, not just added afterward.
- Turnover control is mathematically integrated into the rebalance process through a partial-rebalance formula.
- Concentration control is handled through capacity ratios, company caps, minimum stock weights, and narrow-index conditions.
- The rulebook confirms the production implementation of FTSE's quality model:
  - profitability + leverage for most sectors
  - ROA only for financials and real estate
- FTSE supports both `fixed recipe` and `target exposure` paradigms, which is highly relevant to how you think about Aapryl's custom designs.
- FTSE's target-exposure architecture is explicitly iterative and constraint-aware: if exact exposure targets are infeasible, the rulebook relaxes exposures and turnover in a defined order rather than abandoning the methodology.
- The rulebook includes direct Russell 1000 and Russell 2000 examples, making it especially relevant to your benchmark set.
- The Russell parameter tables are not generic examples; they include specific live designs such as `Russell 1000 2Qual/Val 5% Capped` and `Russell 2000 0.4 Target Exposure Quality`, which makes this rulebook unusually relevant to your assignment.

## Why This Matters for Aapryl

- This document gives you a serious provider template for the `simultaneous tilt` side of the construction debate.
- It shows that a custom factor index does not have to be a hard screen followed by a rank. It can instead be a benchmark-relative tilt system with layered constraints.
- It provides a strong baseline for region and sector control, even though it does not solve your manager's `active-manager-based exposure` idea.
- It shows multiple ways to express factor views:
  - pure factor
  - mixed factor
  - narrow factor
  - fixed tilt
  - target exposure
- It also shows that `target exposure` design needs a feasibility policy, not just a target number. FTSE's relaxation ladder is a good reminder that some desired exposures will conflict with turnover, concentration, and neutrality constraints.
- It is especially useful for thinking about how to build factor portfolios on top of `Russell 1000` and `Russell 2000`.
- It suggests that for Aapryl, some of the most important decisions may be:
  - whether to use `fixed tilt` or `target exposure`
  - how tight country and industry bands should be
  - how much turnover to allow
  - whether to build broad or narrow sleeves

## What to Borrow for Aapryl

- z-score normalization with explicit truncation rules
- mechanical missing-data treatment
- benchmark-relative multiplicative factor tilts
- country and industry constraint bands
- capacity, max-weight, and minimum-weight controls
- turnover-control via partial rebalance
- narrow-index logic based on exposure contribution rather than arbitrary top-N selection

## What Not to Copy Blindly

- FTSE's exact factor definitions without testing them in your target universes
- FTSE's exact country and industry constraint parameters
- the exact tilt-strength values in the tables
- the exact review schedules
- the assumption that a simultaneous tilt system is always better than a staged selection process

Those are FTSE-specific answers to FTSE's own index family. The more important lesson is the framework.

## Deepest Project Takeaway

If you reduce the whole rulebook to one sentence, it is this:

**FTSE builds factor portfolios by starting from benchmark market-cap weights and then applying simultaneous factor, country, industry, capacity, and turnover tilts to create a controlled active exposure profile.**

That is why this document matters so much for your assignment. It is one of the clearest real-world examples showing how a provider can build factor indexes as a `simultaneous constrained tilt system`, which is exactly the main contrast to the staged Fidelity-style approach.

## References

Primary source sections used in this note:

- Section 1, `Introduction`, pp. 3-4
- Section 4, `Eligible securities`, p. 8
- Section 5, `Factor construction`, pp. 9-11
- Section 6, `Index construction`, pp. 12-32
- Section 7, `Periodic review of constituents`, p. 33
- Section 8, `Changes to constituent companies`, p. 34
- Section 9, `ESG data inputs`, p. 35
- Section 10, `Corporate actions and events`, p. 36
- Section 11, `Indices algorithm and calculation method`, p. 37
- Appendix A, `Narrow index`, p. 38
