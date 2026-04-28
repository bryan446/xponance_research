# Morningstar Global Factor Indexes Rulebook

Source: `20250507_Global_Factor_Indexes_Rulebook.pdf`

This document is a **rulebook**, not a research paper. That means its job is to specify the repeatable construction rules for Morningstar's live factor indexes: universe definition, eligibility, ranking, selection, weighting, optimization, constraints, maintenance, and governance. It is therefore most useful for understanding how an index provider turns a factor signal into an investable portfolio.

This document is **not** mainly trying to prove that Morningstar's factor definitions are the best academic definitions. Instead, it explains the operating rules used to build and maintain the indexes once the factor framework has already been chosen.

All `Theoretical Example` blocks below are illustrative and invented. They are included to make the mechanics easier to visualize and should not be read as Morningstar examples.

## Step 1. Define the Parent Benchmark Universe

**What Morningstar Does**  
Morningstar starts each factor index from a parent benchmark in the `Morningstar Target Market Exposure` family. Large-mid parent indexes cover the top 85% of the investable market, while small-cap parents cover the 85%-99% range. Only the `primary share class` of each company is used, and market capitalization is measured at the company level.

**Why This Step Exists**  
This anchors the factor index to an investable benchmark universe instead of treating the whole equity market as one unconstrained pool. It also keeps the methodology company-based rather than share-class-based.

**What This Means for Us**  
This is directly relevant to Aapryl because your project also starts from benchmark universes such as `Russell 1000`, `Russell 2000`, `MSCI EAFE`, and `MSCI EM`. Morningstar gives a strong template for thinking of the benchmark as the parent universe that the factor portfolio tilts away from, rather than as something to ignore.

**Theoretical Example**  
If Morningstar is building a Developed Markets Value Factor Index, it does not scan every listed stock globally. It begins with the Developed Markets Target Market Exposure benchmark and only works inside that benchmark's constituent set.

**Reference**  
- p. 4, `Starting Universe`
- Appendix 2, pp. 10-11

## Step 2. Apply Eligibility Rules

**What Morningstar Does**  
A stock must have a valid factor exposure score from the Morningstar risk model to be eligible. For momentum indexes, a stock must also have at least `6 months (126 days)` of continuous return data.

**Why This Step Exists**  
Morningstar does not want to include securities that cannot actually be scored on the target factor. This protects the consistency of the ranking and selection process.

**What This Means for Us**  
For Aapryl, this suggests that factor design is not only about theoretical signals. You also need practical data-availability rules. If a signal cannot be computed consistently across the benchmark, you need an eligibility rule before you ever rank names.

**Theoretical Example**  
If a newly listed company has only two months of price history, it may still be in a parent benchmark, but Morningstar would exclude it from the momentum factor index because the signal cannot be constructed reliably.

**Reference**  
- p. 4, `Eligibility`

## Step 3. Assign Factor Exposure Scores

**What Morningstar Does**  
Each stock is assigned a factor exposure score. These scores come primarily from the `Morningstar Global Industry Standard Risk Model`, with momentum using a slightly modified local-price formulation described in Appendix 3.

**Why This Step Exists**  
The factor score is the raw material for every later step. Without a defined exposure measure, Morningstar cannot rank, select, or weight securities consistently.

**What This Means for Us**  
For your project, this shows the distinction between `factor research` and `factor implementation`. Once the factor is defined, the system needs one standardized score per company so that portfolio construction becomes mechanical.

**Theoretical Example**  
Morningstar may assign one stock a high value score and another a low value score before doing anything else. Those scores become the basis for ranking and all portfolio decisions that follow.

**Reference**  
- p. 4, `Portfolio Construction`
- Appendix 3, pp. 12-14

## Step 4. Normalize Factor Exposures

**What Morningstar Does**  
Morningstar normalizes factor exposures using `z-scores`. For `quality`, `size`, `value`, and `yield`, the normalizations are `sector neutral`. Exposures are also clipped at `+/- 3` to limit the impact of extreme outliers.

**Why This Step Exists**  
Normalization makes factor scores comparable across names. Sector-neutralization reduces the chance that a factor index simply becomes a disguised sector bet. Clipping keeps a few extreme observations from dominating the portfolio.

**What This Means for Us**  
This is highly relevant to your manager's question about sector constraints. Morningstar handles bias at two levels: first in the normalized factor itself through sector-neutralization, then again later through active sector constraints. That layered approach is important.

**Theoretical Example**  
If one utility stock has an extreme leverage statistic and one tech stock has a very different capital structure, Morningstar does not want the raw numbers alone to dominate the ranking. Z-scoring and sector-neutralization make the comparison more controlled.

**Reference**  
- p. 4, `Portfolio Construction`
- Appendix 3, pp. 12-14

## Step 5. Rank Securities by Factor Exposure

**What Morningstar Does**  
After normalization, Morningstar ranks stocks by their target factor exposure.

**Why This Step Exists**  
Ranking is the bridge between factor measurement and portfolio selection. It converts a continuous factor score into an ordered opportunity set.

**What This Means for Us**  
This is one reason the Morningstar document is useful for the `ranking / tilt` side of your future methodology comparison. Its process is explicitly score-based and rank-driven.

**Theoretical Example**  
If 1,000 securities are eligible and sorted by value exposure, Morningstar can identify which names are most value-oriented before deciding how many to include.

**Reference**  
- p. 4, `Portfolio Construction`

## Step 6. Select Securities Until They Reach 30% of Parent Float Market Cap

**What Morningstar Does**  
Morningstar does not simply pick a fixed number of top-ranked names. Instead, it selects securities until they collectively represent `30%` of the parent index's `float-adjusted market capitalization`.

**Why This Step Exists**  
This makes selection benchmark-relative and capacity-aware. The index size adjusts to the market-cap structure of the parent universe instead of being arbitrarily fixed.

**What This Means for Us**  
This is a strong example of provider-style implementation logic. For Aapryl, the exact `30%` figure may or may not be right, but the larger idea is important: selection can be tied to benchmark market representation rather than an arbitrary top-100 or top-quintile count.

**Theoretical Example**  
If the top-ranked 85 stocks together make up 30% of the benchmark's float-adjusted market cap, the portfolio stops there. In another region, it might take 140 names to hit the same target.

**Reference**  
- pp. 4-5, `Portfolio Construction` and `Number of Stocks`

## Step 7. Apply Turnover Buffers

**What Morningstar Does**  
Morningstar applies buffering rules to reduce turnover:

- stocks in the `top 20%` are guaranteed inclusion
- current constituents between `20% and 40%` of parent market cap ranking get preference
- then Morningstar fills from the remaining universe until the `30%` market-cap target is reached

**Why This Step Exists**  
A pure re-ranking process can create unnecessary turnover whenever names move just above or below a cut line. Buffering stabilizes the portfolio and reduces trading noise.

**What This Means for Us**  
This is one of the most practical parts of the rulebook for Aapryl. If you build monthly-updating portfolios later, some version of buffering or banding will likely be necessary to keep turnover from exploding.

**Theoretical Example**  
A stock that drops from the 19th percentile to the 27th percentile would still likely stay in the portfolio if it is already a constituent, rather than being forced out immediately and possibly bought back next rebalance.

**Reference**  
- pp. 4-5, `Portfolio Construction`
- p. 5 footnote 2

## Step 8. Create Unconstrained Factor-Tilted Benchmark Weights

**What Morningstar Does**  
Morningstar computes a `factor score` from the normalized exposure `z`:

`Factor_score = 1 + a*z if z > 0, else 1/(1-a*z)`

with `a = 1`.

The unconstrained factor weight is then:

`factor_score * benchmark_weight`

These weights are normalized to sum to 1.

**Why This Step Exists**  
Morningstar does not equal-weight the selected names. It starts from benchmark weights and tilts them up or down based on factor strength. This preserves investability while still increasing exposure.

**What This Means for Us**  
This is probably the single most useful operational lesson in the document. The factor portfolio is not constructed as a naive top-bucket basket. It is built as a `benchmark-relative tilt`, which is very relevant if your eventual indices need to remain benchmark-aware.

**Theoretical Example**  
If a stock has a 2.0% benchmark weight and a strong factor score, its unconstrained factor weight might rise above 2.0%. A weaker-scoring stock may remain included, but at a reduced weight.

**Reference**  
- p. 5, `Index Weighting`

## Step 9. Normalize the Unconstrained Weights and Use Them as Optimization Targets

**What Morningstar Does**  
Morningstar treats the normalized tilted weights as `target weights` for the optimizer.

**Why This Step Exists**  
The raw tilt may violate implementation constraints. Turning those weights into targets allows Morningstar to preserve the factor intent while still solving for a feasible portfolio.

**What This Means for Us**  
This is important for FactSet-based implementation thinking. A factor design can have a clean theoretical target portfolio, but the live portfolio may need to be a constrained approximation of that target.

**Theoretical Example**  
If the raw tilt produces too much concentration in one stock or sector, Morningstar does not discard the signal. It uses the raw tilt as the target and then solves for the closest feasible portfolio.

**Reference**  
- p. 5, `Index Weighting`
- p. 5, `Index Constraints via Optimization`

## Step 10. Optimize Final Weights

**What Morningstar Does**  
Morningstar uses an optimizer to adjust the unconstrained target weights `as little as possible` while meeting the rulebook constraints. The objective is to minimize the `L2 norm` between target and final weights.

**Why This Step Exists**  
This step reconciles two goals that often conflict: maximize factor expression and maintain investability. Optimization is the mechanism that balances those goals.

**What This Means for Us**  
This is directly relevant to your future project because your manager explicitly mentioned FactSet optimization capabilities. This rulebook is giving you a real example of how an optimizer is used in index construction rather than in traditional active management.

**Theoretical Example**  
If the raw target portfolio would push too much weight into one stock and one sector, the optimizer can spread some of that weight out while keeping the final portfolio as close as possible to the factor-tilted target.

**Reference**  
- p. 5, `Index Constraints via Optimization`

## Step 11. Apply Stock-Level Constraints

**What Morningstar Does**  
Morningstar applies the following stock-level rules:

- no short positions
- max security weight <= `20x` its benchmark weight
- max security weight <= `benchmark weight + 4%`
- minimum nonzero weight = `1 basis point`

**Why This Step Exists**  
These constraints prevent extreme stock-specific concentration and ensure the portfolio remains implementable.

**What This Means for Us**  
This is a useful reminder that a factor index is still a portfolio with practical risk limits. For Aapryl, the exact numbers may differ, but some explicit stock-level caps are almost certainly necessary.

**Theoretical Example**  
If a benchmark constituent has a 0.10% weight and the factor tilt wants to push it to 4.50%, Morningstar's stock-level caps would force that down to a lower feasible weight.

**Reference**  
- p. 5, `Index Constraints via Optimization`

## Step 12. Apply Region Active-Weight Constraints

**What Morningstar Does**  
Morningstar constrains region weights relative to the parent benchmark.

For `quality`, `size`, `value`, and `yield`:
- benchmark region weight `+/- 2%`
- if infeasible, loosen in `1%` increments up to `15%`

For `momentum` and `low volatility`:
- benchmark region weight `+/- 10%`
- if infeasible, loosen in `1%` increments up to `25%`

Regional constraints do not apply for `US` and `Developed Markets Europe`, since each sits within one region.

**Why This Step Exists**  
This keeps the factor index from becoming an unintended region bet while still allowing some flexibility to express the factor.

**What This Means for Us**  
This is directly useful given your manager's interest in region limits. Even if Aapryl later replaces these exact bands with `active-manager-informed` bands, Morningstar gives you a concrete constraint framework to start from.

**Theoretical Example**  
If Emerging Asia-Pacific is 18% of the parent benchmark, the quality index would initially try to keep it between 16% and 20%. Only if the optimizer cannot find a feasible portfolio would the band widen.

**Reference**  
- p. 5, `Index Constraints via Optimization`
- Appendix 5, p. 16

## Step 13. Apply Sector Active-Weight Constraints

**What Morningstar Does**  
Morningstar applies sector active-weight constraints in the same style as the regional ones.

For `quality`, `size`, `value`, and `yield`:
- benchmark sector weight `+/- 2%`
- loosen in `1%` increments up to `15%` if needed

For `momentum` and `low volatility`:
- benchmark sector weight `+/- 10%`
- loosen in `1%` increments up to `25%` if needed

**Why This Step Exists**  
This prevents the factor index from drifting into a disguised sector portfolio rather than a factor portfolio.

**What This Means for Us**  
This is especially useful for your project because your manager explicitly wants to think about sector limits. Morningstar shows one clean way to express sector neutrality operationally: use benchmark-relative active bands enforced through optimization.

**Theoretical Example**  
If Technology is 22% of the parent benchmark, the quality index would initially keep it between 20% and 24%. If the factor signal strongly favors tech and the optimizer cannot satisfy all rules, the constraint can widen gradually.

**Reference**  
- p. 6
- Appendix 5, p. 16

## Step 14. Reconstitute and Rebalance Semiannually

**What Morningstar Does**  
Morningstar reconstitutes and rebalances the index `semi-annually`, using market data as of the last trading day of `May` and `November`. Changes are implemented after Friday's close and reflected the following Monday.

**Why This Step Exists**  
A fixed rebalance cycle creates a predictable and governable maintenance schedule. It also balances responsiveness against turnover.

**What This Means for Us**  
Aapryl may not use the same cadence, especially if you end up running monthly updates. But the Morningstar rulebook shows how an index provider turns methodology into a recurring production cycle.

**Theoretical Example**  
If a stock becomes much more attractive on value by late May, it does not enter the index immediately. It is evaluated at the scheduled rebalance using the rulebook process.

**Reference**  
- p. 7, `Scheduled Maintenance`

## Step 15. Maintain the Index Through Corporate-Action, Calculation, and Correction Rules

**What Morningstar Does**  
Morningstar handles maintenance through separate governance documents covering:

- corporate actions
- index calculation
- price data
- data corrections
- methodology review
- possible index cessation

**Why This Step Exists**  
A live index needs more than a selection model. It also needs ongoing governance and operational rules so subscribers can trust how the index behaves through real-world events.

**What This Means for Us**  
This matters because your project is not only about factor research. If Aapryl eventually consumes these portfolios operationally, the production process will need maintenance rules in addition to construction rules.

**Theoretical Example**  
If one stock goes through a merger, spin-off, or split, the portfolio needs a pre-defined treatment rule rather than an ad hoc decision every time.

**Reference**  
- pp. 7-9

## Step 16. Interpret the Framework as a Benchmark-Relative Factor-Tilt Process

**What Morningstar Does**  
Taken together, Morningstar's process builds a factor index as a `benchmark-relative, optimized, constrained tilt`, not as a pure unconstrained factor basket.

**Why This Step Exists**  
This is the philosophical center of the rulebook: strong factor exposure matters, but investability, diversification, and benchmark control also matter.

**What This Means for Us**  
This is why the document is so useful for your project. It is not telling you which factor should win academically. It is showing you how a provider converts a factor idea into a live, investable index product.

**Theoretical Example**  
A pure stock-picker might buy only the strongest factor names and ignore benchmark structure. Morningstar instead keeps the parent benchmark as the anchor and tilts around it under explicit constraints.

**Reference**  
- Overview, p. 3
- pp. 4-7

## Factor Definitions Most Relevant to Us

### Quality

Morningstar defines quality as:

`Quality = 1/2 [ROA_z + (1 - Debt / Invested Capital)_z]`

Where:
- `ROA_z` is the z-score of trailing 12-month return on assets
- `(1 - Debt / Invested Capital)_z` is the z-score of inverse leverage
- the factor is `sector neutralized`

**Why This Matters**  
This is a much simpler quality definition than the FTSE quality paper. Morningstar quality is basically `profitability + balance-sheet conservatism`, whereas FTSE's quality framework also incorporates accruals and change in asset turnover.

**Theoretical Example**  
If one company has high ROA and low debt relative to invested capital, while another has similar ROA but much higher debt, Morningstar quality will favor the first company even if both are profitable.

**Reference**  
- p. 13, `Quality Factor`

### Value

Morningstar defines value as:

`Value Factor = Value Score - Growth Score`

The value score is built from price-scaled fundamentals such as:
- earnings / price
- book value / price
- revenue / price
- cash flow / price
- dividend / price

The growth score is built from growth rates of those same variables.

The factor is `sector neutralized`.

**Why This Matters**  
This gives you a concrete example of a provider-style `value` definition that is not just one ratio like book-to-price. It is a composite of valuation and growth-style components.

**Theoretical Example**  
A stock with cheap valuation multiples but weak growth may still score as value if its value score is sufficiently stronger than its growth score.

**Reference**  
- pp. 13-14, `Value Factor`

### Other Factors in the Rulebook

The rulebook also defines:
- `momentum`
- `size`
- `low volatility`
- `yield`

These are useful for context, but they are secondary to your immediate project compared with `quality` and `value`.

**Reference**  
- pp. 12-14, Appendix 3

## What to Borrow for Aapryl

The most useful things to borrow from this document are:

- `benchmark-relative parent universe design`
- `buffer-driven turnover control`
- `factor-tilted benchmark weights`
- `optimization-based constraint enforcement`
- `explicit sector and region active-weight bands`
- `rule-based reconstitution and maintenance framework`

Morningstar is especially helpful as a model for `how to build and constrain a live portfolio once the factor signal has already been chosen`.

## What Not to Copy Blindly

The parts that should not be copied without testing are:

- Morningstar's exact factor definitions
- the exact `30%` parent-market-cap selection rule
- the exact `+/- 2%` and loosening bands
- the `semiannual` rebalance timing
- the assumption that a single-factor construction template can be reused unchanged for your custom multi-factor sleeves

Those design choices may or may not be right for `Deep Value`, `Quality Value`, `Quality Growth`, and `Aggressive Growth`.

## Why This Document Is Useful

This rulebook is strongest for `implementation mechanics`, not factor discovery.

It is useful because it shows:
- how to go from factor score to live portfolio rules
- how to define an investable selection process
- how to control turnover with buffers
- how to use optimization to keep sector and region drifts under control
- how an index provider thinks about governance and maintenance

It is also a good benchmark for the `composite ranking / tilt` side of your ranking-vs-2-step comparison. That is an inference from the construction design, not an explicit Morningstar test.

It does **not** answer:
- how to build `Deep Value`
- how to build `Aggressive Growth`
- how to use active-manager-based exposure design
- whether ranking or 2-step is better for your project
- how to run monthly production automation

## References

Primary source sections used in this note:

- Overview, p. 3
- Index Construction, pp. 4-6
- Index Maintenance and Calculation, p. 7
- Methodology Review and Index Cessation Policy, p. 8
- Data Correction and Precision, p. 9
- Appendix 2: Parent Benchmarks, pp. 10-11
- Appendix 3: Factor Definitions, pp. 12-14
- Appendix 4: Index Inception and Performance Start Dates, pp. 14-15
- Appendix 5: Morningstar Regions and Sectors, p. 16
