# Fidelity Global Quality Value Index Methodology

Source: `methodology-fidelity-global-quality-value-index.pdf`

This document is a **live index methodology / rulebook** for a blended `Quality Value` strategy. It is one of the most relevant documents for the Aapryl project because it is not just about `quality` in isolation or `factor implementation` in the abstract. It shows how a real provider constructs a portfolio that explicitly combines `quality` and `value` while controlling country and sector exposures and maintaining an investable index.

This note is written as a step-by-step working document, not a loose summary. The goal is to capture what Fidelity is actually doing, why each step exists, and what parts of the methodology are most important for the project you were asked to plan. One important operational detail from the methodology is that `FactSet` and `MSCI` are the main data sources for the eligibility and construction metrics, and Fidelity/S&P maintain an explicit field-mapping appendix for implementation.

All `Theoretical Example` blocks below are illustrative and invented. They are included only to make the methodology easier to visualize and should not be read as Fidelity examples or Fidelity results.

## What This Document Answers

This methodology answers several questions that are central to the Aapryl project:

- how a provider can define `Quality Value` as a real index rather than as a research concept
- how `quality` and `value` can be combined in a sequential construction process
- how country and sector neutrality can be preserved structurally
- how banks can be handled differently from non-banks
- how size bias can be controlled inside a value process
- how annual full reconstitution can coexist with lighter monthly maintenance
- how an index can be both factor-driven and benchmark-aware

## What This Document Does Not Answer

This methodology is very useful, but it does **not** answer the whole project by itself. It does not tell you:

- how to build `Deep Value`
- how to build `Quality Growth`
- how to build `Aggressive Growth`
- how to use actual `active-manager exposures` to set region and sector limits
- whether Fidelity's exact ESG overlay belongs in Aapryl
- whether this exact design would be best for `Russell 1000`, `Russell 2000`, `MSCI EAFE`, or `MSCI EM`

It is most useful as a template for thinking about the `Quality Value` index specifically, and especially for your manager's question about `multi-factor ranking` versus `2-step` construction.

## Methodology in Order

## 1. Start from a Broad Reference Index

**What Fidelity Does**  
Fidelity begins with the `S&P Developed Ex-Korea BMI Index` as the reference index. At each annual reconstitution observation date, stocks from that reference index are screened for security type eligibility, liquidity, and investability.

**Why This Step Exists**  
Fidelity wants the Quality Value index to begin from a broad, investable benchmark rather than an unconstrained global universe.

**What This Means for Us**  
This aligns with your assignment because your future indices will also be built from pre-defined parent benchmarks like `Russell 1000`, `Russell 2000`, `MSCI EAFE`, and `MSCI EM`.

**Theoretical Example**  
Instead of asking, "What are the best quality-value stocks in the world?", Fidelity asks, "Which quality-value stocks inside this benchmark universe should we own?"

**Reference**  
- `Index Objective`, p. 4
- `Eligibility Criteria`, p. 6

## 2. Apply Basic Eligibility and Investability Screens

**What Fidelity Does**  
The methodology keeps only eligible common-stock primary listings and removes:

- non-primary share classes except where the primary is unavailable
- limited partnerships
- ADRs
- securities without required price, market-cap, or volume data
- the least liquid names
- stocks with less than `15%` free-float market capitalization

Liquidity exclusion includes removing the bottom quintile ranked by days to trade `US$10 million`.

The methodology also treats `dual-listed companies` as separate eligible entities when they are legally distinct companies listed in different countries.

**Why This Step Exists**  
This is a practical investability filter. Fidelity is not trying to build a theoretical paper portfolio; it is trying to build a live, tradable index.

**What This Means for Us**  
For Aapryl, this is a reminder that factor design is only one layer. Every methodology also needs explicit rules for listings, liquidity, and free float before scoring begins.

**Theoretical Example**  
A company might look extremely cheap and high quality on paper, but if it trades very little and has tiny free float, Fidelity excludes it before any factor ranking takes place.

**Reference**  
- `Eligibility Criteria`, p. 6
- `Highlights`, p. 4

## 3. Define a Selection Universe of the Largest 2000 Stocks

**What Fidelity Does**  
After eligibility screens, Fidelity sorts the remaining securities by free-float-adjusted market capitalization and keeps the largest `2000` stocks. This becomes the `Selection Universe`.

For multiple listings, market capitalization is combined across listings into the primary listing.

**Why This Step Exists**  
Fidelity wants the strategy to represent a broad developed-market equity opportunity set while remaining large-cap and mid-cap enough to support investability and neutrality targets.

**What This Means for Us**  
This is an important design choice. Fidelity is not scoring the entire parent benchmark equally. It is first shrinking the universe to a large and liquid subset. The methodology also uses the constituent and sector weights of this selection universe to define the broad global equity market it is trying to stay neutral against. That kind of universe-definition step may matter a lot in your own design work, especially for small-cap universes.

**Theoretical Example**  
If 4,500 developed-market stocks pass basic screens, Fidelity does not continue with all 4,500. It keeps the largest 2,000 and treats that group as the broad market for the rest of the methodology.

**Reference**  
- `The Selection Universe`, p. 7

## 4. Apply ESG and Controversy Exclusions Before Factor Construction

**What Fidelity Does**  
Before scoring and selection, Fidelity excludes companies based on:

- business involvement screens
- MSCI controversy rating of `0`
- MSCI Global Norms non-compliance
- missing MSCI ESG coverage

The business involvement screens cover multiple controversial industries and activities such as tobacco, weapons, thermal coal, gambling, alcohol, cannabis, adult entertainment, and others.

**Why This Step Exists**  
In this methodology, ESG is not a side note. It is built into the investable universe definition. Fidelity wants the index to satisfy a specific sustainability profile before any factor ranking occurs.

**What This Means for Us**  
This part may or may not belong in Aapryl, but methodologically it matters because it shows how non-factor exclusions can be layered ahead of the main factor process. It also means that Fidelity's Quality Value design is not a pure factor design; it is a `quality + value + ESG-constrained` design.

**Theoretical Example**  
If a stock has excellent quality and value scores but fails a business involvement screen, it never reaches the selection stage at all.

**Reference**  
- `Exclusions Based on Business Involvement`, pp. 9-11
- `Exclusions Based on MSCI's Controversy Rating`, p. 11
- `MSCI ESG Global Norms Screens Overview`, pp. 11-12
- `Treatment of Missing MSCI Data`, p. 12

## 5. Build Country+Sector Groups

**What Fidelity Does**  
Fidelity forms `country+sector groups` by intersecting country and GICS sector after the ESG and data-availability screens. Special handling includes:

- for China only, `Communication Services` and `Information Technology` are combined
- if a country+sector group has fewer than `10` eligible stocks, those stocks are reassigned to an `Other` country bucket
- banks are later treated separately for quality scoring

**Why This Step Exists**  
This is Fidelity's main structural neutrality mechanism. It prevents the methodology from becoming a pure global rank that could accidentally turn into large country and sector bets.

**What This Means for Us**  
This is extremely relevant to your manager's interest in region and sector limits. Fidelity does not just cap sector and country exposures at the end. It embeds neutrality into the scoring and selection architecture itself.

**Theoretical Example**  
Instead of comparing a Japanese industrial company directly against a Swiss pharmaceutical company at every step, Fidelity first groups companies into country+sector buckets and makes many of the decisions within those buckets.

**Reference**  
- `Country+sector groups`, pp. 12-13

## 6. Remove the Bottom 5% of Momentum Names Within Each Group

**What Fidelity Does**  
Within each country+sector group, Fidelity excludes the lowest `5%` of stocks ranked by price momentum. Momentum is measured using the security's total return from `12 months before` the observation date to `1 month before` the observation date.

**Why This Step Exists**  
Fidelity labels this as a `data quality screen`, but functionally it also removes the worst recent price losers from the candidate set. This may help avoid obvious deteriorating names before the value-selection stage.

**What This Means for Us**  
This is a subtle but important detail. Fidelity is not building a pure Quality Value methodology with no price-based input. It is quietly using momentum as a guardrail. That may be closer to how active managers behave in practice than a purely accounting-based process.

**Theoretical Example**  
If a stock looks cheap and profitable but has collapsed in price relative to peers over the last year, Fidelity may remove it before it can be selected as a value name.

**Reference**  
- `Data`, p. 12
- `Data Quality Screens`, p. 13

## 7. Define Quality, ESG, and Value Differently for Non-Banks and Banks

**What Fidelity Does**  
For `non-banks`, Fidelity defines:

- `Quality` as:
  - cash flow margin
  - return on invested capital
  - free cash flow stability
- `ESG` as:
  - MSCI Industry Adjusted Company Score
- `Value` as:
  - free cash flow yield
  - EBITDA / enterprise value
  - tangible book value / price
  - next-twelve-month earnings / price

For `banks`, Fidelity uses a different model:

- `Quality`:
  - return on equity
  - debt to assets penalty
- `Value`:
  - tangible book value / price
  - next-twelve-month earnings / price

The debt-to-assets term for banks uses a special rule: the highest quintile of debt-to-assets gets a z-score of `-2`, while all others get `0`.

**Why This Step Exists**  
Banks have different accounting structures, leverage norms, and business models. Fidelity is explicitly recognizing that the same quality framework should not be imposed mechanically on all sectors.

**What This Means for Us**  
This is very relevant to Aapryl. It is another clear example, along with FTSE, that factor models often need sector- or industry-specific treatment. It also shows that Fidelity's version of `quality` is not the same as FTSE's or MSCI's:

- FTSE emphasized accruals, ROA, efficiency, and leverage
- MSCI emphasized ROE, leverage, and earnings stability
- Fidelity emphasizes cash generation, ROIC, and free-cash-flow consistency

**Theoretical Example**  
A bank with strong ROE and manageable debt/assets may score well under Fidelity's bank model even though cash flow margin and ROIC would not be the right variables to use for that sector.

**Reference**  
- `Composite Quality, ESG, and Value Scores`, pp. 8-9

## 8. Winsorize Metrics and Standardize Them Within Country+Sector Groups

**What Fidelity Does**  
Fidelity winsorizes the raw quality, ESG, and value inputs and then converts them into z-scores within each country+sector group. The methodology states that:

- outliers below the `2nd` percentile are reset to the lower threshold
- outliers above the `98th` percentile are reset to the upper threshold
- z-scores are then capped at `3` standard deviations

For quality, banks are removed from Financials and treated as their own sector for z-score purposes.

**Why This Step Exists**  
Winsorization reduces the influence of outliers, while within-group z-scoring makes the signal relative to local sector and country context rather than globally absolute.

**What This Means for Us**  
This is a major project takeaway. Fidelity is effectively saying:

- do not compare raw factor ratios globally
- normalize relative to peer groups
- control unintended country/sector bias early in the process

That is directly relevant to your manager's question about how to build these indices in a way that feels realistic.

**Theoretical Example**  
A Japanese utility and a UK software company may both have strong quality characteristics, but Fidelity measures them relative to the distributions in their own country+sector groups rather than forcing one raw ranking across the whole world.

**Reference**  
- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

## 9. Build Composite Quality and Combined Quality+ESG Scores

**What Fidelity Does**  
Inside each country+sector group:

- the quality metric z-scores are equally weighted and re-standardized to create a `Composite Quality Score`
- the `Combined Quality and ESG Score` is then the equal-weighted sum of:
  - `Composite Quality Score`
  - `ESG Score`

If a quality or value metric is missing for a security, Fidelity assigns that metric a z-score of `0` instead of automatically excluding the stock.

Any stock with a `negative Combined Quality and ESG Score` is eliminated.

Fidelity is also unusually tolerant of missing factor data at this stage:

- if one quality metric is missing, that metric gets a z-score of `0`
- if all quality metrics are missing, they all get `0`
- if one value metric is missing, that metric gets a z-score of `0`
- if all value metrics are missing, they all get `0`

So the methodology is much less strict about missing factor data than the MSCI quality methodology, which uses hard exclusion rules for missing core descriptors.

**Why This Step Exists**  
This is the key gate in the methodology. Fidelity does not let value drive selection unless the company first clears a minimum quality-plus-ESG hurdle.

**What This Means for Us**  
This is probably the single most important methodological insight in the whole document for your project:

Fidelity is **not** doing a one-pass blended rank of quality and value across the full universe. It is doing a staged process:

1. build quality
2. combine quality with ESG
3. eliminate weak names
4. then rank the survivors on value

This is much closer to a `2-step` or `multi-stage` construction than to a simple weighted average of value and quality z-scores.

**Theoretical Example**  
Suppose Stock A is extremely cheap but has weak cash generation and poor ESG. Stock B is moderately cheap but clearly higher quality. Fidelity's process can eliminate Stock A before the value ranking ever happens.

**Reference**  
- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

## 10. Compute Value Scores Only After the Quality+ESG Gate

**What Fidelity Does**  
After removing stocks with negative combined quality and ESG scores, Fidelity creates value z-scores within each country+sector group and combines them equally to form a `Value Score`.

Missing value metrics are assigned a z-score of `0`.

**Why This Step Exists**  
Fidelity wants value selection to occur only among names that have already passed a minimum quality and ESG standard.

**What This Means for Us**  
This sequencing matters a lot. It shows that in Fidelity's design, `quality` is a gate and `value` is the final selection driver. That is highly relevant to your manager's ranking-vs-2-step question.

**Theoretical Example**  
If 100 names start in a country+sector group, Fidelity may first eliminate 35 with weak quality+ESG. It then compares value only among the remaining 65 rather than across the original 100.

**Reference**  
- `Calculating Composite Quality, ESG Scores, and Value Scores`, pp. 13-14

## 11. Blend Value with Size to Remove Small-Cap Bias

**What Fidelity Does**  
Fidelity calculates a `Size Factor Score` as the z-score of the logarithm of each security's free-float market capitalization within each country+sector group. It then builds:

- `Size Adjusted Value Score = 60% Value Score + 40% Size Factor Score`

This score is used for final ranking and selection.

**Why This Step Exists**  
Fidelity explicitly says it is trying to remove size bias from the value process. Cheap stocks often lean small, and Fidelity does not want the final portfolio to become an unintended small-cap value strategy.

**What This Means for Us**  
This is one of the best ideas in the paper. It shows that a provider may want a `value` signal, but not the full baggage that often comes with it. This kind of adjustment could be very important when you compare methodologies across `Russell 1000` and `Russell 2000`.

**Theoretical Example**  
If two stocks have the same value score but one is much larger and more liquid, the size adjustment can push that larger stock higher in the final ranking.

**Reference**  
- `Calculating the Size Adjusted Value Scores`, p. 14

## 12. Select Constituents Within Each Country+Sector Group

**What Fidelity Does**  
Fidelity ranks securities within each country+sector group by `Size Adjusted Value Score`.

The number of stocks selected from each group is:

- the market-cap weight of that country+sector group in the selection universe
- multiplied by `250`
- subject to a minimum of `3`

If a group ends up with fewer than three stocks, it is not selected and its group weight becomes zero in the final selection.

The process targets roughly `250` stocks overall, though the final number may differ slightly because of rounding.

**Why This Step Exists**  
This is how Fidelity preserves country and sector neutrality while still allowing stock selection within each bucket. Instead of taking the top 250 names globally, it allocates selection slots proportionally by group.

**What This Means for Us**  
This is one of the strongest construction ideas in the methodology. Fidelity is not saying, "keep sectors roughly neutral if possible." It is structurally tying constituent counts to the market-cap weights of country+sector groups.

**Theoretical Example**  
If a country+sector group represents `4%` of the selection universe, Fidelity aims to allocate about `10` names to it in a 250-stock index before rounding.

**Reference**  
- `Selecting Constituents`, p. 14

## 13. Weight Stocks with an Equal-Excess Approach

**What Fidelity Does**  
At annual reconstitution, each stock's weight within its country+sector group is:

- its market-cap weight in the selection universe
- plus an equal overweight adjustment applied uniformly to all selected constituents in that group

The uniform overweight is set so that:

- the selected names in the group collectively add back up to the group's weight in the selection universe

Fidelity explicitly says the purpose of this `Equal Excess` weighting approach is to reduce stock-specific risk and concentration.

**Why This Step Exists**  
Fidelity wants to preserve country+sector neutrality without simply reproducing market-cap weights among selected names. Equal excess shifts some weight from the very largest selected names toward the rest of the chosen group.

**What This Means for Us**  
This is a very useful weighting idea for Aapryl because it sits between pure market-cap weighting and equal weighting. It is a practical way to:

- keep group weights neutral
- reduce individual-stock concentration
- still respect the original benchmark structure

**Theoretical Example**  
If a country+sector group has five selected names and a 6% total group weight, the group weight is preserved at 6%, but the biggest stock does not get all of that weight just because it was biggest in the universe. Some of the group's weight is redistributed evenly across the selected names.

**Reference**  
- `Weighting Constituents in an Annual Reconstitution Observation Date`, p. 15

## 14. Enforce an ESG Exposure Improvement at the Index Level

**What Fidelity Does**  
After stock weights are assigned, Fidelity compares:

- the index-level exposure to the z-scores of MSCI Industry-Adjusted Company Scores
- versus the universe-level market-cap-weighted ESG exposure

If the index-level exposure is below the universe exposure, Fidelity:

- scales up constituents with ESG z-scores above the universe exposure
- scales down constituents with ESG z-scores below the universe exposure
- continues until the index-level ESG exposure is `0.1` standard deviations above the universe level exposure

This ESG-exposure approach was updated in November 2024. The methodology-change appendix indicates that Fidelity moved away from an older, coarser rule based on the share of the index rated `BBB or better` and replaced it with this more continuous z-score-based exposure target.

**Why This Step Exists**  
Fidelity wants the final portfolio not only to avoid the worst ESG names, but also to show a measurable improvement in ESG exposure relative to the universe.

**What This Means for Us**  
This is important mainly as a structural idea: overlays can be added after the main selection process. Even if Aapryl does not use ESG, the design pattern matters because it shows how a secondary portfolio objective can be layered on top of factor selection without redesigning the whole methodology.

**Theoretical Example**  
If the selected portfolio has strong quality-value characteristics but only average ESG exposure, Fidelity nudges weights toward higher-ESG selected names until the portfolio clears the required ESG-improvement threshold.

**Reference**  
- `ESG Exposure`, p. 15
- `Appendix II - Methodology Changes`, pp. 25-26

## 15. Run a Full Annual Reconstitution but Only Conditional Monthly Rebalances

**What Fidelity Does**  
The index is:

- fully reconstituted annually on the `3rd Friday of February`
- rebalanced in other months only if a constituent:
  - gets an ESG controversy score of `0`
  - falls into a business involvement exclusion
  - becomes non-compliant under MSCI Global Norms screens

Observation and reference dates are generally `18 index business days` prior to the rebalance or reconstitution date.

If no constituent triggers one of the monthly exclusion conditions in a non-February month, there is `no rebalance` and `no pro forma` file for that month.

**Why This Step Exists**  
Fidelity separates structural factor rebuilding from exception-driven maintenance. It avoids unnecessary full monthly turnover while still reacting to important ESG events.

**What This Means for Us**  
This is highly relevant to your project because your team wants eventual `monthly` updates. Fidelity shows one model where "monthly" does not mean "rebuild everything monthly." Instead, it can mean a lighter operational process layered on top of a less frequent core reconstitution.

**Theoretical Example**  
The full stock-selection logic might only be rerun once a year, while monthly checks only remove names that newly violate a hard exclusion rule.

**Reference**  
- `Rebalancing`, pp. 17-18

## 16. Replace Removed Names Within the Same Country+Sector Group

**What Fidelity Does**  
At non-annual monthly rebalances, deleted names are replaced with the next-highest `Size Adjusted Value Score` names from the same country+sector group. Fidelity adds replacements one by one until:

- the removed weight has been fully replaced, or
- there are no more eligible replacements in the group

New names enter at:

- their selection-universe weight
- plus the average excess weight of constituents already held in that group

If the last addition causes the replacement weight to overshoot, its weight is trimmed. If there are not enough replacements, the remaining constituents are rescaled.

**Why This Step Exists**  
Fidelity wants monthly maintenance to preserve the architecture of the annual portfolio. Replacement is local to the country+sector group so neutrality is maintained.

**What This Means for Us**  
This is another very useful implementation pattern for Aapryl. It shows how to perform maintenance without reopening every design decision at each small update.

**Theoretical Example**  
If a French health care stock is removed due to an ESG controversy, Fidelity does not replace it with the best stock in the whole world. It looks for the next-best candidate in the same French health care group.

**Reference**  
- `Weighting Constituents in a Non-Annual Reconstitution Observation Date`, pp. 15-16

## 17. Maintain the Index with Standard S&P Corporate-Action Rules

**What Fidelity Does**  
Outside rebalancing dates, additions are generally not made except for spin-offs. Deletions can occur due to mergers, suspensions, bankruptcies, and similar events. Standard corporate-action handling then follows S&P DJI practice.

The methodology also explicitly notes that the index does `not` have a fixed number of constituents over time, so additions and deletions do not have to match one-for-one.

**Why This Step Exists**  
Even a factor index needs operational maintenance rules. A methodology is not complete if it only describes selection and weighting.

**What This Means for Us**  
For Aapryl, this reinforces that portfolio automation will need a maintenance policy for corporate actions, not just a scheduled rebalance engine.

**Theoretical Example**  
If a current constituent is acquired for cash between annual reconstitutions, the index cannot wait until next February to respond. A corporate-action rule removes it and adjusts the index accordingly.

**Reference**  
- `Additions and Deletions`, p. 18
- `Corporate Actions`, pp. 18-19

## Key Design Conclusions

- This is the closest external template so far for building a real `Quality Value` index.
- Fidelity uses a **hybrid process**:
  - multi-factor combination within `quality`
  - multi-factor combination within `value`
  - but a **sequential gate** between `quality+ESG` and `value`
- The methodology is much closer to a `2-step` or `multi-stage` construction than to a one-shot weighted average of quality and value across the full universe.
- Country and sector neutrality are handled structurally through `country+sector groups`, not only through end-stage caps.
- Fidelity deliberately controls size bias by adding `40%` size to the final value-ranking score.
- The weighting approach is not simple market cap and not equal weight. It is a benchmark-aware, within-group concentration-reduction method.
- Banks are treated separately, which reinforces the broader lesson that factor models often need sector-specific logic.
- Fidelity is more permissive on missing factor data than MSCI. Missing quality or value inputs are often set to `0` rather than triggering exclusion.
- The methodology depends heavily on explicit `FactSet + MSCI` field definitions. The hidden field-mapping appendix is an implementation detail that matters a lot in practice.
- ESG is not cosmetic in this methodology. It affects:
  - universe eligibility
  - score combination
  - monthly maintenance
  - final exposure adjustment
- Fidelity recently tightened the ESG overlay design by moving from a bucketed ratings rule to a continuous exposure-improvement rule, which suggests that implementation details in the overlay matter materially.
- The index is only `approximately` a 250-stock portfolio. It is not managed to a hard fixed constituent count after maintenance.

## Why This Matters for Aapryl

- This document gives you a strong model for how `Quality Value` can be built in a way that looks `manager-like`, not just academically factor-pure.
- It is strong evidence that a provider may prefer a `gated sequential approach` rather than a simple blended z-score across the whole universe.
- It offers a concrete way to preserve sector and regional neutrality by construction, which is highly relevant to your manager's interest in exposure controls.
- It suggests that final index design may need to be `hybrid`:
  - composite models within factor sleeves
  - sequential gating between factor sleeves
- It provides a useful template for `annual full rebuild + lighter monthly maintenance`, which may be closer to what Aapryl eventually needs operationally than a full monthly reconstitution.
- Because Fidelity uses `FactSet` for many of the metrics, it also suggests that this kind of methodology is implementable in the tool stack your team already has.
- The note also implies that for real implementation you will need a `field-mapping document`, not just a conceptual factor definition. Fidelity explicitly has one.

## What to Borrow for Aapryl

- the idea of treating `Quality Value` as a staged process rather than a single blended score
- peer-relative normalization inside sector and geography buckets
- special handling for banks and other structurally different industries
- a size adjustment to prevent value from drifting into unwanted small-cap exposure
- group-based selection and weighting to preserve neutrality
- a distinction between `core reconstitution` and `maintenance rebalance`

## What Not to Copy Blindly

- the ESG overlay and exclusion framework
- the exact `largest 2000` stock rule
- the exact `250 stock` target
- the specific country+sector grouping conventions
- the exact `60% value / 40% size` blend
- the exact S&P Developed Ex-Korea benchmark assumptions
- the permissive `missing metrics = zero` treatment without testing whether it causes unintended behavior in your universes

Those are Fidelity-specific answers to Fidelity's own index objective. The more important lesson is the design pattern, not the literal parameter values.

## Deepest Project Takeaway

If you reduce the whole Fidelity methodology to one sentence, it is this:

**Fidelity builds Quality Value as a staged process that first enforces quality and ESG acceptability, then ranks the survivors on value adjusted for size, and finally preserves country and sector neutrality through structured selection and weighting.**

That is why this document is so important for your assignment. It is one of the clearest real-world examples showing that `Quality Value` can be built as a `hybrid multi-factor + two-step process`, which is exactly the kind of question your manager wants you to think through.

## References

Primary source sections used in this note:

- `Index Objective`, p. 4
- `Highlights`, p. 4
- `Eligibility Criteria`, p. 6
- `The Selection Universe`, p. 7
- `Composite Quality, ESG, and Value Scores`, pp. 8-9
- `Exclusions Based on Business Involvement`, pp. 9-11
- `Exclusions Based on MSCI's Controversy Rating`, p. 11
- `MSCI ESG Global Norms Screens Overview`, pp. 11-12
- `Treatment of Missing MSCI Data`, p. 12
- `Country+sector groups`, pp. 12-13
- `Data Quality Screens`, p. 13
- `Calculating Composite Quality, ESG Scores, and Value Scores`, pp. 13-14
- `Calculating the Size Adjusted Value Scores`, p. 14
- `Selecting Constituents`, p. 14
- `Weighting Constituents in an Annual Reconstitution Observation Date`, p. 15
- `ESG Exposure`, p. 15
- `Weighting Constituents in a Non-Annual Reconstitution Observation Date`, pp. 15-16
- `Index Calculations`, p. 17
- `Rebalancing`, pp. 17-18
- `Additions and Deletions`, p. 18
- `Corporate Actions`, pp. 18-19
- `Appendix II - Methodology Changes`, pp. 25-26
