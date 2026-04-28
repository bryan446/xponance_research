# MSCI Quality Indexes Methodology

Source: `MSCI_Quality_Indexes_Methodology_20250520.pdf`

This document is a **methodology / rulebook hybrid**. It is more prescriptive than the FTSE quality research paper because it gives a live index-construction recipe, but it is also more factor-specific than the Morningstar global factor rulebook because it is focused only on `quality`. The note below is organized as a step-by-step construction document so you can see how MSCI goes from a quality idea to a repeatable, investable index.

This document is **not** mainly trying to prove that MSCI has found the academically best quality definition. Its main purpose is to specify the construction rules for MSCI's quality indexes once MSCI has decided what `quality` means. In that sense, it is best read as an implementation methodology for a provider-style quality index.

All `Theoretical Example` blocks below are illustrative and invented. They are included only to make the mechanics easier to visualize and should not be read as MSCI examples or MSCI results.

## Step 1. Start from an MSCI Parent Index

**What MSCI Does**  
MSCI begins with an existing `MSCI Parent Index`. The applicable universe is all existing constituents of that parent index, which can be a country or regional MSCI index.

**Why This Step Exists**  
MSCI wants the quality index to be anchored to an investable benchmark universe that already has sufficient liquidity and capacity. This avoids treating the global market as one unconstrained stock pool.

**What This Means for Us**  
This is directly relevant to Aapryl because your project also starts from defined benchmark universes such as `Russell 1000`, `Russell 2000`, `MSCI EAFE`, and `MSCI EM`. MSCI is showing a benchmark-relative construction mindset rather than a free-form stock selection exercise.

**Theoretical Example**  
If MSCI is building a quality index for a developed-market regional benchmark, it does not begin with every listed company in the region. It starts with the names already in the relevant MSCI parent index and only scores those names.

**Reference**  
- Section 2.1, `Applicable Universe`, p. 4

## Step 2. Define Quality as a Quality Growth Strategy

**What MSCI Does**  
MSCI frames quality as a `quality growth strategy`. It targets companies with durable business models and sustainable competitive advantages, especially companies with:

- high `ROE`
- stable earnings that are less tied to the broad business cycle
- strong balance sheets with low financial leverage

**Why This Step Exists**  
MSCI needs a conceptual definition before it can choose descriptors. The document makes clear that MSCI is not defining quality as cheapness, deep fundamental distress, or pure defensiveness. It is defining quality as the combination of strong profitability, financial strength, and earnings durability.

**What This Means for Us**  
This matters for Aapryl because MSCI's version of quality is closer to `quality growth` than to a broader accounting-quality framework. That makes it especially relevant to the `quality` sleeve of `Quality Growth`, and somewhat different from the FTSE definition that leans more heavily on accruals and operating-efficiency improvement.

**Theoretical Example**  
Suppose Company A has consistently high profitability, modest debt, and steady earnings through different market environments. Company B has volatile earnings and carries much more leverage. MSCI's conceptual definition is trying to ensure Company A receives the higher quality score.

**Reference**  
- Section 1, `Introduction`, p. 3

## Step 3. Compute the Three Core Descriptors

**What MSCI Does**  
MSCI builds the quality signal from three fundamental descriptors:

- `Return on Equity (ROE)`
- `Debt to Equity (D/E)`
- `Earnings Variability`

Appendix I defines them as:

- `ROE = trailing 12-month earnings per share / latest book value per share`
- `D/E = total debt / book value`
- `Earnings Variability = standard deviation of year-over-year EPS growth over the last five fiscal years`

**Why This Step Exists**  
These three descriptors are MSCI's chosen operational definition of quality. Together they try to capture profitability, leverage discipline, and earnings stability in a way that can be standardized across all stocks in the parent index.

**What This Means for Us**  
This is one of the most important takeaways from the MSCI file. Compared with FTSE, MSCI's quality model is narrower and simpler. Compared with Morningstar, it is a little richer because it adds an earnings-stability dimension. This gives you another plausible provider-style definition for the `quality` sleeve.

**Theoretical Example**  
Imagine three companies:

- Company A: high ROE, low D/E, stable earnings
- Company B: high ROE, very high D/E, unstable earnings
- Company C: average ROE, low D/E, stable earnings

MSCI's descriptor set gives A the strongest all-around starting profile, penalizes B for leverage and instability, and gives C some credit for quality even without standout profitability.

**Reference**  
- Section 2.2, p. 4
- Appendix I, p. 9

## Step 4. Apply Data Availability Rules

**What MSCI Does**  
MSCI does not compute a composite quality score for every stock automatically. It applies explicit data-availability rules:

- if `ROE` is missing, the stock is not eligible
- if `D/E` is missing, the stock is not eligible
- if `Earnings Variability` is missing but `ROE` and `D/E` are available, MSCI computes the composite quality z-score from those two descriptors
- if all three are missing, the stock is not eligible

As of the May 2025 update, `ROE` and `D/E` are explicitly mandatory.

**Why This Step Exists**  
MSCI wants the quality signal to remain internally consistent. It is willing to tolerate missing earnings-variability data in some cases, but it does not allow a stock into the index without the profitability and leverage descriptors that define the core of the methodology.

**What This Means for Us**  
For Aapryl, this is a useful reminder that methodology design always becomes a data-availability policy question. A factor definition is not complete until you know which missing-data cases are acceptable and which ones force exclusion.

**Theoretical Example**  
If a company has valid ROE and debt data but too little earnings history to compute a five-year variability measure, MSCI may still keep it in the quality universe. But if the company is missing ROE entirely, MSCI will not compute the composite score at all.

**Reference**  
- Section 2.2.3, p. 5
- Appendix II, p. 10
- Appendix VIII, p. 18

## Step 5. Winsorize Each Descriptor Within the Parent Index

**What MSCI Does**  
Before standardization, MSCI winsorizes each descriptor at the `5th` and `95th` percentiles within the parent index. Values below the 5th-percentile observation are set to the 5th-percentile value, and values above the 95th-percentile observation are set to the 95th-percentile value.

**Why This Step Exists**  
MSCI does not want a few extreme accounting values to distort the mean and standard deviation used in the z-score step. Winsorization limits the effect of outliers while preserving the overall rank structure of the universe.

**What This Means for Us**  
This is useful for Aapryl because it shows one concrete provider-style way to make quality signals more robust. If your future model uses accounting variables across global universes, outlier handling will matter.

**Theoretical Example**  
Suppose one stock has an absurdly high ROE because its book value collapsed after restructuring. MSCI does not want that one accounting oddity to dominate the quality model, so it caps the observation at the 95th-percentile ROE value before standardizing.

**Reference**  
- Section 2.2.1, p. 4

## Step 6. Standardize Each Descriptor Into a Z-Score

**What MSCI Does**  
After winsorization, MSCI converts each descriptor into a z-score using the mean and standard deviation of that descriptor within the relevant parent index.

**Why This Step Exists**  
The three descriptors use different raw units and scales. Z-scoring makes them comparable so MSCI can average them into a single composite quality measure.

**What This Means for Us**  
This is directly tied to your manager's question about multi-factor ranking. MSCI is using the same general logic as many provider methodologies: standardize raw inputs first, then combine comparable scores rather than raw ratios.

**Theoretical Example**  
ROE might be measured in percentage terms, while D/E can take very different numeric ranges. Z-scoring lets MSCI compare a stock that is one standard deviation above average on ROE with a stock that is one standard deviation below average on D/E.

**Reference**  
- Section 2.2.2, pp. 4-5

## Step 7. Reverse the Sign for Debt to Equity and Earnings Variability

**What MSCI Does**  
MSCI assigns a negative z-score direction to `Debt to Equity` and `Earnings Variability` so that:

- higher leverage receives a lower score
- more volatile earnings receive a lower score

**Why This Step Exists**  
All three descriptors need to point in the same economic direction before they can be averaged. MSCI wants higher composite values to mean better quality across every component.

**What This Means for Us**  
This is a simple but important implementation detail. It shows that a factor model is not just about choosing the right variables; it is also about making sure every variable contributes with the intended sign before the combination step.

**Theoretical Example**  
If Company A and Company B have identical ROE, but Company B carries much more debt, MSCI wants Company B's leverage term to reduce its quality score rather than accidentally raise it due to a raw-scale mismatch.

**Reference**  
- Section 2.2.2, p. 5

## Step 8. Average Descriptor Z-Scores into a Composite Quality Z-Score

**What MSCI Does**  
MSCI computes a `Composite Quality Z-Score` by averaging the z-scores of the available descriptors, subject to the missing-data rules in Appendix II.

**Why This Step Exists**  
This is the main combination step. It converts three separate quality signals into one integrated quality measure that can be used for ranking and weighting.

**What This Means for Us**  
For Aapryl, this is a clean provider example of a `composite ranking` model. Instead of doing a hard screen and then a second-stage ranking, MSCI first combines the descriptors into a single quality score and only then ranks stocks.

**Theoretical Example**  
Suppose one stock has a z-score of `+1.2` on ROE, `+0.5` on low leverage after sign reversal, and `+0.3` on earnings stability. Its composite quality z-score would be the average of those three numbers, producing a balanced view of its overall quality.

**Reference**  
- Section 2.2.3, p. 5
- Appendix II, p. 10

## Step 9. Transform the Composite Z-Score into a Nonlinear Quality Score

**What MSCI Does**  
MSCI transforms the composite quality z-score into a nonlinear `Quality Score`:

- if `Z > 0`, `Quality Score = 1 + Z`
- if `Z < 0`, `Quality Score = (1 - Z)^-1`

**Why This Step Exists**  
This transformation preserves the ranking order of the z-scores but converts them into a positive weighting factor that can be multiplied by benchmark weights. It also compresses negative-quality names rather than assigning them negative portfolio weights.

**What This Means for Us**  
This is one of the key operational insights from the MSCI methodology. The score is not just a research statistic. It is built specifically to become a portfolio-tilting input.

**Theoretical Example**  
If a stock has a composite z-score of `+0.8`, its quality score becomes `1.8`. If another stock has a composite z-score of `-0.5`, its quality score becomes `1 / 1.5`, which is below 1. That means the stronger stock gets an overweight relative to parent weight, while the weaker stock would receive a reduced relative weight if it were included.

**Reference**  
- Section 2.2.3, p. 5

## Step 10. Rank Securities by Quality Score

**What MSCI Does**  
MSCI ranks all eligible parent-index constituents by `Quality Score`. If multiple securities have the same quality score, the security with the higher parent-index weight receives the higher rank.

**Why This Step Exists**  
Ranking converts the composite score into an ordered list that MSCI can use for constituent selection. The tie-breaker makes the procedure deterministic and keeps the construction process repeatable.

**What This Means for Us**  
This shows the bridge between composite scoring and security selection. Even though MSCI uses a composite ranking approach inside the quality model, the final index still has an explicit selection stage.

**Theoretical Example**  
If two stocks both receive a quality score of `1.35`, MSCI breaks the tie by ranking the larger parent-index constituent ahead of the smaller one.

**Reference**  
- Section 2.3, p. 5

## Step 11. Select the Highest-Ranked Positive-Score Names Up to a Fixed Constituent Count

**What MSCI Does**  
MSCI uses a `fixed number of securities` approach. It selects the highest-ranked stocks with `positive Quality Scores` until it reaches the predetermined target constituent count for that quality index. That fixed number is set at initial construction and then evaluated at each index review to maintain sufficient market-cap coverage.

**Why This Step Exists**  
MSCI wants a quality index with strong factor emphasis but still enough breadth, liquidity, and capacity. A fixed-count design gives MSCI tighter control over index breadth than a market-cap coverage rule.

**What This Means for Us**  
This is a major difference versus Morningstar. Morningstar selects until it reaches a market-cap coverage threshold. MSCI instead fixes the number of names. That gives you two different provider templates for thinking about selection design in Aapryl.

**Theoretical Example**  
If the target count is `300`, MSCI keeps taking the highest-ranked stocks with positive quality scores until the final list contains 300 names, subject to the later buffer rules.

**Reference**  
- Section 2.3, p. 5
- Appendix III, pp. 11-13

## Step 12. Apply a 20% Buffer Rule Around the Fixed Count

**What MSCI Does**  
At each review, MSCI applies a `20%` buffer around the target constituent count to reduce turnover. The methodology example says that for a target of `300` securities, the buffer range runs from ranks `241` through `360`.

The process works broadly as follows:

- names ranked above the guaranteed-add threshold are added first
- existing constituents in the buffer range are then retained on a priority basis
- if the target count is still not reached, MSCI adds the next-highest-ranked names until the target is met

**Why This Step Exists**  
MSCI wants the index to be stable across reviews. Without buffers, a stock moving only slightly around the cutoff could be repeatedly added and removed, creating unnecessary turnover.

**What This Means for Us**  
This is highly relevant to your project because your future Aapryl portfolios will likely need some turnover-control rule. MSCI provides a very clear example of how a selection-based factor index can reduce churn without abandoning the factor ranking altogether.

**Theoretical Example**  
Suppose the index targets 100 names. A current constituent slips from rank 78 to rank 113, while a non-constituent rises to rank 101. A buffer rule may keep the existing constituent and delay adding the new one if the rank changes are only marginal.

**Reference**  
- Section 3.1.1, p. 7
- Appendix III, pp. 11-13

## Step 13. Weight Selected Names by Quality Score Times Parent Weight

**What MSCI Does**  
MSCI weights selected securities by:

`Quality Weight = Quality Score × Market Capitalization Weight in the Parent Index`

**Why This Step Exists**  
This creates a benchmark-relative tilt rather than equal-weighting the selected stocks. Higher-quality names receive larger weights, but parent-index size still matters.

**What This Means for Us**  
This is one of the most useful construction rules in the document. It shows how MSCI combines factor conviction with investability. The methodology is not trying to forget market cap; it is trying to quality-tilt market-cap weights.

**Theoretical Example**  
If Stock A has a parent weight of `2.0%` and quality score of `1.5`, while Stock B has a parent weight of `1.0%` and quality score of `2.0`, their raw quality-weight products are `3.0` and `2.0` respectively before normalization. Both receive an uplift, but the larger parent constituent can still retain more absolute weight.

**Reference**  
- Section 2.4, p. 6

## Step 14. Normalize the Weights

**What MSCI Does**  
After computing the quality-weight products, MSCI normalizes them so the final index weights sum to `100%`.

**Why This Step Exists**  
The raw quality-weight products are only relative sizing signals. Normalization converts them into a valid portfolio.

**What This Means for Us**  
This may seem mechanical, but it matters because it confirms that MSCI's weighting scheme is a tilting scheme, not a standalone score report. The end product is a live index with proper portfolio weights.

**Theoretical Example**  
If all raw quality-weight products across selected stocks add to `250`, each stock's final portfolio weight becomes its raw product divided by `250`.

**Reference**  
- Section 2.4, p. 6

## Step 15. Apply Issuer Caps

**What MSCI Does**  
MSCI caps issuer weights to limit concentration risk:

- for broad parent indexes, issuer weight is capped at `5%`
- for narrow parent indexes, issuer weight is capped at `max(10%, maximum issuer weight in the Parent Index)`

MSCI defines narrow parent indexes as those whose maximum parent-index weight exceeds `10%`.

**Why This Step Exists**  
Quality weighting can concentrate the portfolio in a few dominant names. MSCI uses issuer caps to prevent the factor index from becoming excessively concentrated.

**What This Means for Us**  
For Aapryl, this is a direct example of how a provider keeps a factor portfolio investable without discarding the underlying factor signal. It is also a reminder that concentration control can be implemented with caps even when a full optimizer is not used.

**Theoretical Example**  
If one high-quality mega-cap stock would naturally rise to `7.5%` of a broad quality index, the issuer cap would cut it back to `5%`, and the excess weight would be redistributed across the rest of the portfolio.

**Reference**  
- Section 2.4, p. 6
- Appendix IV, p. 14

## Step 16. Rebalance Semiannually

**What MSCI Does**  
MSCI reviews and rebalances the quality indexes on a `semi-annual` basis, usually as of the close of the last business day of `May` and `November`. It uses fundamental variables as of the end of `April` and `October` respectively.

**Why This Step Exists**  
MSCI wants the quality data to be refreshed often enough to reflect updated company fundamentals while keeping turnover moderate and aligning with the parent-index review cycle.

**What This Means for Us**  
This is useful for Aapryl as a benchmark cadence, but it is not necessarily the cadence you should copy. Your team wants monthly updates operationally, so MSCI's rebalance timing is better understood as one provider's tradeoff between responsiveness and stability.

**Theoretical Example**  
If a company's leverage falls materially after its latest reporting cycle, MSCI's next scheduled semiannual review is when that updated balance-sheet strength would normally feed into the index methodology.

**Reference**  
- Section 3.1, p. 7

## Step 17. Maintain the Index Through Corporate-Action Rules Between Reviews

**What MSCI Does**  
Between formal reviews, MSCI applies corporate-action rules designed to minimize unnecessary turnover while still reflecting investor participation in events. The methodology states that:

- corporate-event treatment aims to minimize turnover outside reviews
- changes in index market capitalization caused by corporate events are offset through the variable weighting factor
- if the parent index is reviewed more frequently than the quality index, intermediate parent changes are neutralized in the quality index

The detailed event handling covers common cases such as mergers, deletions, and spin-offs.

**Why This Step Exists**  
An index methodology is not complete if it only describes rebalancing. Corporate events can change constituents and weights between reviews, so MSCI needs rules that preserve consistency and reduce ad hoc decisions.

**What This Means for Us**  
This is important context for Aapryl because your eventual monthly process will need an operating policy for corporate events. Even if you do not copy MSCI's exact rules, the methodology shows that maintenance governance is part of the design, not an afterthought.

**Theoretical Example**  
If a current constituent is acquired, the index cannot wait until the next scheduled review to decide what happens. MSCI's event rules determine how that position is treated so the index remains investable and consistent.

**Reference**  
- Section 3.2, p. 7

## Step 18. Interpret the Methodology as a Benchmark-Relative Quality Selection Framework

**What MSCI Does**  
Taken as a whole, MSCI's process uses benchmark constituents, benchmark-relative weights, a fixed number of selected names, and caps to create a quality index that emphasizes the factor while preserving scale and capacity.

**Why This Step Exists**  
This is the real design philosophy behind the methodology. MSCI is not building a pure equal-weight stock-picker portfolio. It is building an investable index product.

**What This Means for Us**  
This is one of the most useful ways to read the document for Aapryl. MSCI gives you a provider-style template for:

- a clear descriptor set
- composite ranking
- fixed-count selection
- benchmark-relative weighting
- turnover control
- concentration control

**Theoretical Example**  
If you tried to replicate MSCI with an equal-weight portfolio of the top 50 quality names, you would no longer be following the methodology's core intent. MSCI is explicitly keeping one foot in the parent benchmark at every major stage.

**Reference**  
- Section 1, p. 3
- Sections 2.3-2.4, pp. 5-6
- Section 3, p. 7

## Key MSCI Design Choices

- MSCI defines quality more narrowly than FTSE. It focuses on `ROE`, leverage, and earnings stability rather than using accruals or asset-turnover improvement.
- MSCI's quality model is closer to a `quality growth` interpretation than to a broad accounting-quality or defensive-quality interpretation.
- MSCI uses a `fixed-count selection` method, not the `market-cap coverage` selection rule used by Morningstar.
- MSCI uses `benchmark-relative weighting`, not equal weighting. The quality score scales parent-index weights rather than replacing them.
- MSCI controls concentration mainly with `issuer caps`, not with the broader optimizer-and-constraint framework used in the Morningstar rulebook.
- MSCI's methodology is simple and transparent by provider standards. That appears to be a deliberate design choice, not an omission.

**Reference**  
- Section 1, p. 3
- Sections 2.2-2.4, pp. 4-6
- Appendix IV, p. 14

## Variants and Extensions in the Methodology

### MSCI Quality Tilt Index

MSCI also defines a `Quality Tilt Index`. Unlike the main MSCI Quality Index, the tilt version:

- includes all parent-index constituents with available quality scores
- applies the same quality-score weighting logic
- follows the same rebalancing schedule and corporate-event treatment

This matters because it gives you a clean provider example of `full-universe tilt` versus `selected high-score subset`.

**Why It Matters for Aapryl**  
This is useful for your manager's construction question because it shows that even within one provider's framework, there can be more than one way to express the same factor:

- `selection + weighting`
- `full-universe tilt`

That is not the same as the `multi-factor ranking vs 2-step` question in your email, but it is a closely related construction choice.

**Reference**  
- Appendix V, p. 15

### MSCI Sector Neutral Quality Index

MSCI also defines a `Sector Neutral Quality Index`. In this variant:

- the composite quality z-score is standardized within each sector
- the sector-relative quality score is winsorized at `+/- 3`
- the final quality score uses the same nonlinear transformation as the main index
- after selection and weighting, each sector's weight is reset to match the parent index sector weight
- if no names are selected from a sector, that sector weight is redistributed across the remaining sectors

This matters because it shows one concrete provider approach to reducing unintended sector bets in a quality strategy.

**Why It Matters for Aapryl**  
Your manager explicitly mentioned interest in sector and region controls. MSCI does not solve the `active-manager-based` constraint problem, but this variant shows one important idea: sector neutrality can be built either at the score-computation stage, the final weighting stage, or both.

**Reference**  
- Appendix VI, p. 16
- Appendix VIII, p. 18

### Broad Versus Narrow Parent Index Treatment

MSCI distinguishes between broad and narrow parent indexes when applying issuer caps. Broad indexes get a simple `5%` cap, while narrow indexes use a higher cap linked to the parent index's maximum issuer weight.

**Why It Matters for Aapryl**  
This is a useful reminder that concentration controls may need to vary across universes. A rule that is reasonable for a broad developed-market benchmark may be too restrictive for a concentrated country universe.

**Reference**  
- Section 2.4, p. 6
- Appendix IV, p. 14

## What This Means for Aapryl

- This is a strong methodology template for the `quality` sleeve of `Quality Value` and `Quality Growth`.
- It gives you a concrete example of a `fixed-count selection` framework, which is different from Morningstar's `select to market-cap coverage` approach.
- It is a useful benchmark for comparing `selection + weighting` versus `full-universe tilt`.
- It provides a simpler, more provider-style quality definition than FTSE, which may make it easier to operationalize in FactSet.
- It is less useful for the `active-manager-based sector/region limit` idea because MSCI does not solve that problem directly.
- By inference, this methodology is closer to the `composite ranking` side of the ranking-vs-2-step discussion, because MSCI first builds a composite score and then ranks on that score. That inference is about the construction logic; it is not a direct MSCI comparison study.

## What This Document Does Not Answer

This methodology does **not** answer the full Aapryl assignment. It does not tell you:

- how to build `Deep Value`
- how to build `Aggressive Growth`
- how to use active-manager-based sector and region limits
- the final answer on `multi-factor ranking` versus `2-step`
- how to run monthly Aapryl production automation
- whether MSCI's quality definition is better than FTSE's for your specific benchmark universes

## References

Primary source sections used in this note:

- Section 1, `Introduction`, p. 3
- Section 2.1, `Applicable Universe`, p. 4
- Section 2.2, `Determination Of Quality Score`, pp. 4-5
- Section 2.3, `Security Selection`, p. 5
- Section 2.4, `Weighting Scheme`, p. 6
- Section 3.1, `Index Reviews`, p. 7
- Section 3.1.1, `Buffer Rules`, p. 7
- Section 3.2, `Ongoing Event Related Changes`, p. 7
- Appendix I, `Calculation Of Fundamental Variables`, p. 9
- Appendix II, `Quality Z-Score Computation`, p. 10
- Appendix III, `Rules to Determine Fixed Number of Securities`, pp. 11-13
- Appendix IV, `Issuer Weight Capping`, p. 14
- Appendix V, `Constructing MSCI Quality Tilt Index`, p. 15
- Appendix VI, `Constructing MSCI Sector Neutral Quality Index`, p. 16
- Appendix VIII, `Changes to this Document`, p. 18
