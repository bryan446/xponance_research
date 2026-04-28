# Important Formulas from the MSCI Quality Indexes Methodology

Source: `MSCI_Quality_Indexes_Methodology_20250520.pdf`

This note extracts the main mathematical expressions from the MSCI quality methodology and explains what they do in plain English. Compared with the FTSE formulas note, these formulas are more `index-construction` and `descriptor-definition` oriented. Compared with the Morningstar formulas note, they are more narrowly focused on `quality`.

Some formulas below are printed explicitly in the MSCI methodology. Others are described in words and are rewritten here in clean mathematical form so the process is easier to follow. Where that happens, it is stated clearly.

## What Findings This Document Actually Has

This MSCI document is primarily a `methodology` document, not a research white paper like the FTSE quality paper. That means it does **not** present a long empirical argument with many backtested findings. Still, it does contain clear implied methodological conclusions:

- MSCI believes `quality` is best captured by a combination of:
  - high `ROE`
  - low `Debt to Equity`
  - low `Earnings Variability`
- MSCI treats these three descriptors as sufficient for a live provider-style quality index, which is a much narrower and simpler definition than FTSE's broader accounting-quality framework.
- MSCI believes quality should be implemented as a `benchmark-relative selection-and-weighting` process, not as an equal-weight portfolio of the highest-scoring names.
- MSCI believes a `fixed-count constituent design` is an acceptable way to balance factor exposure, market-cap coverage, and capacity.
- MSCI believes turnover should be managed explicitly with `20% buffer rules`.
- MSCI believes concentration risk can be managed with `issuer caps` rather than a broader optimizer-led sector/region framework.
- MSCI treats `ROE` and `D/E` as core mandatory inputs as of the May 2025 update, which is a strong statement about what MSCI considers non-negotiable in its quality definition.
- Through the `Quality Tilt` and `Sector Neutral Quality` variants, MSCI is also implicitly saying that the same quality signal can be expressed through different portfolio constructions:
  - `selected subset + quality weighting`
  - `full-universe tilt`
  - `sector-neutral selection and weighting`

So the main "findings" here are really `design conclusions`, not academic findings.

## How MSCI Thinks About Quality

MSCI is trying to build a provider-style `quality growth` index. Its process is:

1. Start from a parent benchmark.
2. Compute a few core quality descriptors.
3. Standardize and combine them into a composite quality score.
4. Select the highest-quality names.
5. Weight them relative to parent-index market-cap weights.
6. Cap concentrations and rebalance on a fixed schedule.

That means the formulas in this methodology fall into four buckets:

- `descriptor formulas`
- `standardization formulas`
- `quality score formulas`
- `portfolio weighting and cap formulas`

---

## 1. Return on Equity (ROE)

**Purpose**  
Measures profitability relative to shareholder equity and serves as MSCI's main profitability descriptor.

**Formula**

$$
ROE = \frac{Trailing\ 12\ Month\ Earnings\ Per\ Share}{Latest\ Book\ Value\ Per\ Share}
$$

**Terms**

- `ROE`: return on equity
- `Trailing 12 Month Earnings Per Share`: earnings per share over the last 12 months
- `Latest Book Value Per Share`: most recent book value per share

**Plain-English Explanation**  
This tells you how much earnings the company is generating for each unit of book equity.

**Why MSCI Uses It**  
MSCI wants quality to begin with a profitability measure, and ROE is the profitability measure it chose. This reflects MSCI's view that a high-quality company should generate strong profits relative to the capital shareholders have committed to the business. It also reinforces the document's `quality growth` framing, because high-ROE companies are often associated with stronger business franchises and better compounding ability.

**Interpretation**

- Higher `ROE` is better for quality
- Lower `ROE` is worse for quality
- If `ROE` is missing, the stock is not eligible for the MSCI Quality Index

**Reference**

- Appendix I, p. 9
- Appendix II, p. 10

---

## 2. Debt to Equity (D/E)

**Purpose**  
Measures financial leverage and serves as MSCI's balance-sheet-strength descriptor.

**Formula**

$$
D/E = \frac{Total\ Debt}{Book\ Value}
$$

**Terms**

- `D/E`: debt-to-equity ratio
- `Total Debt`: latest fiscal-year total debt
- `Book Value`: latest fiscal-year book value

**Plain-English Explanation**  
This tells you how much debt the company carries relative to its equity base.

**Why MSCI Uses It**  
MSCI wants the quality model to reward companies with stronger balance sheets and lower financial leverage. A company with very high profitability but an overlevered capital structure is not treated as fully high quality in this methodology. This is one of the main ways MSCI separates `quality growth` from simply `high profitability`.

**Interpretation**

- Lower `D/E` is better for quality
- Higher `D/E` is worse for quality
- If `D/E` is missing, the stock is not eligible for the MSCI Quality Index

**Reference**

- Appendix I, p. 9
- Appendix II, p. 10

---

## 3. Earnings Variability

**Purpose**  
Measures earnings stability and serves as MSCI's durability descriptor.

**Formula**

$$
Earnings\ Variability = std\left(YoY\ EPS\ Growth\ over\ the\ last\ 5\ fiscal\ years\right)
$$

**Terms**

- `std(...)`: standard deviation
- `YoY EPS Growth`: year-over-year earnings-per-share growth
- `last 5 fiscal years`: the five-fiscal-year history used by MSCI

**Plain-English Explanation**  
This measures how unstable the company's earnings growth has been over time.

**Why MSCI Uses It**  
MSCI's quality concept is not just profitability plus leverage. It also wants companies whose earnings are more stable and durable. This variable is MSCI's way of capturing the idea that high-quality businesses should not have wildly erratic earnings patterns. It is especially important because it separates MSCI's methodology from Morningstar's simpler `ROA + inverse leverage` framework.

**Interpretation**

- Lower `Earnings Variability` is better for quality
- Higher `Earnings Variability` is worse for quality
- If it is missing but `ROE` and `D/E` are present, MSCI can still compute the composite quality z-score using the two available descriptors

**Reference**

- Appendix I, p. 9
- Appendix II, p. 10

---

## 4. Z-Score Standardization

**Purpose**  
Converts each raw descriptor into a standardized score so different variables can be combined.

**Formula**

$$
z = \frac{x - \mu}{\sigma}
$$

**Terms**

- `z`: standardized score
- `x`: the stock's winsorized descriptor value
- `\mu`: mean of that descriptor within the parent index
- `\sigma`: standard deviation of that descriptor within the parent index

**Plain-English Explanation**  
This shows how far a stock's descriptor is above or below the parent-index average in standard-deviation units.

**Why MSCI Uses It**  
ROE, leverage, and earnings variability are measured on different scales. MSCI needs a common unit before it can average them. Z-scoring also makes the signal benchmark-relative, which fits the provider-style design of the methodology.

**Interpretation**

- Positive `z` means above-average on that descriptor
- Negative `z` means below-average on that descriptor
- A larger absolute value means the stock is farther from the parent-index mean

**Reference**

- Section 2.2.2, pp. 4-5

---

## 5. Negative Z-Score Convention for D/E and Earnings Variability

**Purpose**  
Ensures that worse leverage and less stable earnings reduce the quality score.

**Formula**

The methodology states this in words rather than printing separate equations. Rewritten cleanly, the directional convention is:

$$
z_{D/E}^{quality} = - \frac{x_{D/E} - \mu_{D/E}}{\sigma_{D/E}}
$$

$$
z_{EV}^{quality} = - \frac{x_{EV} - \mu_{EV}}{\sigma_{EV}}
$$

**Terms**

- `z_{D/E}^{quality}`: quality-oriented z-score for debt to equity
- `z_{EV}^{quality}`: quality-oriented z-score for earnings variability
- `x`: winsorized descriptor value
- `\mu`: parent-index mean
- `\sigma`: parent-index standard deviation

**Plain-English Explanation**  
MSCI flips the sign for these two descriptors so lower leverage and more stable earnings receive higher quality scores.

**Why MSCI Uses It**  
Before combining descriptors, MSCI needs every variable to point in the same economic direction. Otherwise, a stock with very high leverage could accidentally look better instead of worse when scores are averaged.

**Interpretation**

- Lower `D/E` increases quality
- Lower `Earnings Variability` increases quality
- Higher values on either variable reduce quality

**Reference**

- Section 2.2.2, p. 5

---

## 6. Composite Quality Z-Score

**Purpose**  
Combines the three standardized descriptors into one overall quality measure.

**Formula**

The methodology describes this in words. Rewritten in formula form:

$$
Z_{Quality} = \frac{z_{ROE} + z_{D/E}^{quality} + z_{EV}^{quality}}{3}
$$

If `Earnings Variability` is missing but `ROE` and `D/E` are available:

$$
Z_{Quality} = \frac{z_{ROE} + z_{D/E}^{quality}}{2}
$$

**Terms**

- `Z_{Quality}`: composite quality z-score
- `z_{ROE}`: ROE z-score
- `z_{D/E}^{quality}`: sign-adjusted leverage z-score
- `z_{EV}^{quality}`: sign-adjusted earnings-variability z-score

**Plain-English Explanation**  
This is MSCI's main combined quality statistic before portfolio weighting.

**Why MSCI Uses It**  
MSCI does not want to rank stocks on three separate variables independently. It wants one integrated measure of quality that reflects profitability, leverage discipline, and earnings stability at the same time. Averaging the z-scores is the methodology's core combination step.

**Interpretation**

- Higher `Z_{Quality}` means stronger overall quality
- Lower `Z_{Quality}` means weaker overall quality
- Missing `ROE` or `D/E` stops the stock from being eligible at all

**Reference**

- Section 2.2.3, p. 5
- Appendix II, p. 10

---

## 7. Quality Score Transformation

**Purpose**  
Converts the composite quality z-score into a positive weighting multiplier.

**Formula**

$$
Quality\ Score =
\begin{cases}
1 + Z, & Z > 0 \\
(1 - Z)^{-1}, & Z < 0
\end{cases}
$$

where `Z` is the composite quality z-score.

**Terms**

- `Quality Score`: nonlinear score used for ranking and weighting
- `Z`: composite quality z-score

**Plain-English Explanation**  
MSCI turns the z-score into a score that is always positive and can directly scale portfolio weights.

**Why MSCI Uses It**  
MSCI needs a value that can multiply a benchmark weight without creating negative portfolio weights. This transformation preserves ordering, rewards strong-quality stocks with a multiplier above 1, and compresses weaker stocks below 1.

**Interpretation**

- If `Z > 0`, the quality score is above `1`
- If `Z = 0`, the quality score is effectively `1`
- If `Z < 0`, the quality score is below `1`
- Stronger quality gets an overweight relative to parent weight

**Reference**

- Section 2.2.3, p. 5

---

## 8. Quality Weight Before Normalization

**Purpose**  
Turns the quality score into a raw portfolio weight signal.

**Formula**

$$
Quality\ Weight = Quality\ Score \times Market\ Capitalization\ Weight\ in\ the\ Parent\ Index
$$

**Terms**

- `Quality Weight`: raw pre-normalization portfolio weight
- `Quality Score`: nonlinear score from the previous step
- `Market Capitalization Weight in the Parent Index`: the stock's benchmark weight

**Plain-English Explanation**  
MSCI starts with the stock's parent-index weight and then tilts it up or down based on quality.

**Why MSCI Uses It**  
This is the heart of the benchmark-relative design. MSCI is not trying to forget market cap; it is trying to quality-tilt market-cap weights. That makes the index more investable than an equal-weight portfolio of top-quality stocks.

**Interpretation**

- Larger benchmark names can still remain large in the quality index
- Stronger quality names get bigger weights than they had in the parent index
- Weaker quality names get smaller relative weights if included

**Reference**

- Section 2.4, p. 6

---

## 9. Weight Normalization

**Purpose**  
Converts raw quality weights into valid portfolio weights that sum to 100%.

**Formula**

The methodology states that raw weights are normalized to 100%. Rewritten mathematically:

$$
Final\ Weight_i = \frac{Raw\ Quality\ Weight_i}{\sum_j Raw\ Quality\ Weight_j}
$$

**Terms**

- `Final Weight_i`: normalized final portfolio weight for stock `i`
- `Raw Quality Weight_i`: pre-normalization quality weight for stock `i`
- `\sum_j Raw Quality Weight_j`: sum of raw quality weights across all selected constituents

**Plain-English Explanation**  
This rescales the raw tilted weights so the final portfolio adds up correctly.

**Why MSCI Uses It**  
The `Quality Score x benchmark weight` product only tells MSCI the relative tilt. It still needs a normalization step to produce actual portfolio weights.

**Interpretation**

- Higher raw quality weights translate into higher final weights
- The normalization step does not change rank order; it only rescales the portfolio

**Reference**

- Section 2.4, p. 6

---

## 10. Security-Level Inclusion Factor

**Purpose**  
Links the final security weight to the stock's pro forma market-cap weight in the parent index.

**Formula**

$$
Inclusion\ Factor = \frac{Final\ Security\ Weight}{Security\ Pro\ Forma\ Market\ Capitalization\ Weight\ in\ the\ Parent\ Index}
$$

**Terms**

- `Inclusion Factor`: final security-level inclusion factor
- `Final Security Weight`: the stock's weight in the quality index
- `Security Pro Forma Market Capitalization Weight in the Parent Index`: the stock's pro forma benchmark weight

**Plain-English Explanation**  
This tells MSCI how much of the stock's parent-index market-cap weight should be carried into the final quality index.

**Why MSCI Uses It**  
This is a technical bridge between the target quality weight and the actual index implementation mechanics. It expresses the final portfolio decision as a factor relative to the parent index.

**Interpretation**

- An inclusion factor above `1` means an overweight versus the parent index
- An inclusion factor below `1` means an underweight versus the parent index

**Reference**

- Section 2.4, p. 6

---

## 11. Issuer Cap for Broad Parent Indexes

**Purpose**  
Limits concentration in broad quality indexes.

**Formula**

$$
Issuer\ Cap_{broad} = 5\%
$$

**Terms**

- `Issuer Cap_{broad}`: maximum issuer weight for broad parent-index quality indexes

**Plain-English Explanation**  
No issuer can exceed a 5% weight in the designated broad MSCI quality indexes.

**Why MSCI Uses It**  
Benchmark-relative weighting can still become concentrated when a few large names also have strong quality scores. The cap keeps the index from becoming too top-heavy.

**Interpretation**

- If a stock's unconstrained weight would exceed 5%, it is capped
- The capped excess weight must be redistributed elsewhere in the portfolio

**Reference**

- Section 2.4, p. 6
- Appendix IV, p. 14

---

## 12. Issuer Cap for Narrow Parent Indexes

**Purpose**  
Applies a more flexible concentration cap for narrower country or regional universes.

**Formula**

$$
Cap_{narrow} = \max(10\%,\ Maximum\ Issuer\ Weight\ in\ the\ Parent\ Index)
$$

**Terms**

- `Cap_{narrow}`: maximum issuer weight in a narrow-parent quality index
- `Maximum Issuer Weight in the Parent Index`: the largest issuer weight in the parent benchmark

**Plain-English Explanation**  
For narrower universes, MSCI allows a higher cap because concentration is often structurally unavoidable.

**Why MSCI Uses It**  
MSCI recognizes that a cap suitable for a broad global benchmark may be too restrictive in a more concentrated country or regional market. This formula adjusts the concentration limit to the shape of the underlying universe.

**Interpretation**

- The cap is never below `10%`
- The cap can be higher if the parent benchmark itself is more concentrated

**Reference**

- Appendix IV, p. 14

---

## 13. Sector-Relative Quality Score for the Sector Neutral Variant

**Purpose**  
Recomputes the quality signal within each sector for the `MSCI Sector Neutral Quality Index`.

**Formula**

The methodology describes this in words. Rewritten mathematically:

$$
Z_{rel,i} = \frac{Z_{Quality,i} - \mu_{sector}}{\sigma_{sector}}
$$

with sector-relative scores winsorized at:

$$
Z_{rel,i} \in [-3, 3]
$$

**Terms**

- `Z_{rel,i}`: sector-relative quality score for stock `i`
- `Z_{Quality,i}`: composite quality z-score for stock `i`
- `\mu_{sector}`: mean composite quality z-score in the stock's sector
- `\sigma_{sector}`: standard deviation of composite quality z-scores in the stock's sector

**Plain-English Explanation**  
This measures how strong a stock's quality is relative to its own sector peers rather than relative to the whole parent index.

**Why MSCI Uses It**  
Quality can be mixed up with sector structure if some sectors naturally have different profitability or leverage patterns. The sector-relative version reduces that problem by redefining quality in peer-relative terms.

**Interpretation**

- Positive `Z_{rel}` means above-sector-average quality
- Negative `Z_{rel}` means below-sector-average quality
- Winsorization at `+/- 3` limits sector-level outliers

**Reference**

- Appendix VI, p. 16

---

## 14. Sector-Neutral Quality Score Transformation

**Purpose**  
Converts the sector-relative quality score into a positive weighting multiplier for the sector-neutral index.

**Formula**

$$
Quality\ Score_{sector\ neutral} =
\begin{cases}
1 + Z_{rel}, & Z_{rel} > 0 \\
(1 - Z_{rel})^{-1}, & Z_{rel} < 0
\end{cases}
$$

**Terms**

- `Quality Score_{sector neutral}`: weighting score for the sector-neutral quality index
- `Z_{rel}`: sector-relative quality score

**Plain-English Explanation**  
This is the same nonlinear transform as the main quality index, except it is applied to sector-relative quality rather than parent-index-relative quality.

**Why MSCI Uses It**  
MSCI wants the sector-neutral index to preserve the same general weighting logic while changing only the reference frame of the quality measurement.

**Interpretation**

- Higher sector-relative quality gives a larger sector-neutral weighting score
- Lower sector-relative quality gives a smaller score

**Reference**

- Appendix VI, p. 16

---

## 15. Sector-Neutral Weight Rescaling

**Purpose**  
Rescales stock weights so each sector matches the sector weight of the parent index in the `MSCI Sector Neutral Quality Index`.

**Formula**

The methodology describes this in words. Rewritten mathematically for clarity:

$$
Final\ Weight_{i,s} =
Parent\ Sector\ Weight_s \times
\frac{Raw\ Weight_{i,s}}{\sum_{j \in s} Raw\ Weight_{j,s}}
$$

**Terms**

- `Final Weight_{i,s}`: final weight of stock `i` in sector `s`
- `Parent Sector Weight_s`: the parent-index weight of sector `s`
- `Raw Weight_{i,s}`: the stock's pre-sector-normalized weight
- `\sum_{j \in s} Raw Weight_{j,s}`: total raw weight of selected stocks in sector `s`

**Plain-English Explanation**  
Within each sector, MSCI rescales the selected stocks so the entire sector ends up matching the parent index's sector weight.

**Why MSCI Uses It**  
This is how MSCI enforces sector neutrality at the portfolio level after computing sector-relative quality scores. It ensures the index expresses stock selection within sectors without drifting into large active sector bets.

**Interpretation**

- The stocks still compete with each other within sector
- The final portfolio keeps sector weights aligned with the parent benchmark
- If a sector has no selected names, MSCI redistributes that sector's weight across the remaining sectors

**Reference**

- Appendix VI, p. 16
