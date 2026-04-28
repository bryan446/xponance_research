# Important Formulas from the Morningstar Global Factor Indexes Rulebook

Source: `20250507_Global_Factor_Indexes_Rulebook.pdf`

This note extracts the main mathematical expressions from the Morningstar rulebook and explains what they do in plain English. Unlike the FTSE formulas note, these formulas are mostly about `factor definitions` and `portfolio-construction mechanics`, not broad academic factor research.

## How to Read These Formulas

- `Factor definition formulas` explain how Morningstar defines exposures like quality, value, momentum, low volatility, size, and yield.
- `Construction formulas` explain how Morningstar turns factor scores into portfolio weights.
- Some portfolio rules are expressed as constraints rather than equations, but they are still important because they control how the final index behaves.

---

## 1. Factor Tilt Score

**Purpose**  
Converts a normalized factor exposure into a tilt multiplier for portfolio weighting.

**Formula**

If `z > 0`:

\[
Factor\_score = 1 + a z
\]

Otherwise:

\[
Factor\_score = \frac{1}{1 - a z}
\]

with:

\[
a = 1
\]

**Terms**

- `z`: normalized and clipped factor exposure
- `a`: tilt-strength parameter, set to `1`
- `Factor_score`: multiplier used to tilt the benchmark weight

**Plain-English Explanation**  
Morningstar gives stronger factor names a multiplier above 1 and weaker factor names a multiplier below 1.

**Why Morningstar Uses It**  
Morningstar wants a smooth weighting rule that increases benchmark weights for stronger factor names and reduces them for weaker names without switching to equal-weighting or an all-or-nothing stock-picking process.

**Interpretation**

- Higher `z` means a larger tilt upward
- Lower `z` means a smaller tilt weight
- `z = 0` implies no tilt and therefore a factor score of `1`

**Reference**

- p. 5, `Index Weighting`

---

## 2. Unconstrained Factor Weight

**Purpose**  
Applies the tilt score to the stock's benchmark weight.

**Formula**

\[
Unconstrained\ Factor\ Weight = Factor\_score \times Benchmark\ Weight
\]

After that, weights are normalized to sum to 1.

**Terms**

- `Factor_score`: tilt multiplier from the previous formula
- `Benchmark Weight`: the company-level benchmark market-cap weight

**Plain-English Explanation**  
Morningstar starts from the benchmark weight and scales it up or down based on factor strength.

**Why Morningstar Uses It**  
This keeps the index benchmark-aware and investable. Morningstar is not building an equal-weight factor basket; it is building a constrained benchmark-relative factor tilt.

**Interpretation**

- strong factor exposure -> weight above benchmark
- weak factor exposure -> weight below benchmark

**Reference**

- p. 5, `Index Weighting`

---

## 3. Quality Factor

**Purpose**  
Defines Morningstar's quality exposure.

**Formula**

\[
Quality = \frac{1}{2}\left[ROA_z + \left(1 - \frac{Total\ Debt}{Total\ Invested\ Capital}\right)_z\right]
\]

**Terms**

- `ROA_z`: z-score of trailing 12-month return on assets
- `Total Debt / Total Invested Capital`: leverage ratio
- `(1 - Total Debt / Total Invested Capital)_z`: z-score of inverse leverage

**Plain-English Explanation**  
Morningstar quality is just two things:

- profitability
- lower leverage

and they are equally weighted.

**Why Morningstar Uses It**  
Morningstar uses a simple quality definition that rewards profitable companies with more conservative balance sheets. Compared with FTSE's quality paper, this is a much simpler implementation-oriented definition.

**Interpretation**

- higher ROA improves quality
- lower debt relative to invested capital improves quality
- the rulebook says the quality factor is `sector neutralized`

**Reference**

- p. 13, `Quality Factor`

---

## 4. Size Factor

**Purpose**  
Measures company size so that smaller firms have larger factor values.

**Formula**

\[
size_{i,t} = -\ln(MV_{i,t})
\]

**Terms**

- `MV_{i,t}`: market value of firm `i` at time `t`
- `-\ln(MV)`: negative log market cap

**Plain-English Explanation**  
Smaller companies receive larger size-factor values because the negative log flips the sign.

**Why Morningstar Uses It**  
The log transforms market value so that very large companies do not dominate the scale, and the negative sign ensures the factor increases as firms get smaller.

**Interpretation**

- larger factor value -> smaller company
- smaller factor value -> larger company
- the rulebook says the size factor is `sector neutralized`

**Reference**

- p. 13, `Size Factor`

---

## 5. Value Factor

**Purpose**  
Defines Morningstar's value exposure.

**Formula**

\[
Value\ Factor = Value\ Score - Growth\ Score
\]

**Terms**

- `Value Score`: weighted average of price-scaled value metrics
- `Growth Score`: weighted average of growth metrics

**Plain-English Explanation**  
Morningstar calls a stock more value-oriented when its value characteristics are stronger than its growth characteristics.

**Why Morningstar Uses It**  
Morningstar is not relying on a single cheapness metric like book-to-price. It uses a broader style-box framework that compares value and growth characteristics together.

**Interpretation**

- higher value factor -> more value-oriented
- lower value factor -> more growth-oriented
- the rulebook says the value factor is `sector neutralized`

**Reference**

- p. 13, `Value Factor`
- p. 14

---

## 6. Value Score

**Purpose**  
Measures the stock's cheapness using price-scaled fundamentals.

**Formula**

\[
Value\ Score =
\left[
w_E \times \frac{E}{P_t}
+ w_{BV} \times \frac{BV}{P_t}
+ w_R \times \frac{R}{P_t}
+ w_{CF} \times \frac{CF}{P_t}
+ w_D \times \frac{D}{P_t}
\right]
\]

**Terms**

- `E / P_t`: earnings to price
- `BV / P_t`: book value to price
- `R / P_t`: revenue to price
- `CF / P_t`: cash flow to price
- `D / P_t`: dividend to price
- `w_*`: weights assigned to each component

**Plain-English Explanation**  
This score combines several cheapness ratios instead of using only one.

**Why Morningstar Uses It**  
Different valuation ratios capture different parts of what “cheap” means. Combining them gives a broader value signal.

**Interpretation**

- higher value score usually means cheaper on fundamentals relative to price

**Note**  
The rulebook shows the weighted-average structure but does not specify the exact numeric weights in this document.

**Reference**

- p. 13, `Value Factor`

---

## 7. Growth Score

**Purpose**  
Measures the stock's growth characteristics.

**Formula**

\[
Growth\ Score =
\left[
w_E \times E_{growth}
+ w_{BV} \times BV_{growth}
+ w_R \times R_{growth}
+ w_{CF} \times CF_{growth}
+ w_D \times D_{growth}
\right]
\]

**Terms**

- `E_growth`: earnings growth
- `BV_growth`: book value growth
- `R_growth`: revenue growth
- `CF_growth`: cash flow growth
- `D_growth`: dividend growth
- `w_*`: weights assigned to each component

**Plain-English Explanation**  
This score combines multiple growth measures rather than treating growth as one number.

**Why Morningstar Uses It**  
Morningstar's style framework compares value against growth, so it needs a separate structured growth score alongside the value score.

**Interpretation**

- higher growth score means stronger growth characteristics

**Note**  
The rulebook shows the weighted-average structure but does not specify the exact numeric weights in this document.

**Reference**

- p. 13, `Value Factor`

---

## 8. Momentum Total Return

**Purpose**  
Defines the raw return leg of Morningstar's momentum signal.

**Formula**

\[
TR = \frac{P_1 - P_{12}}{P_{12}} + \frac{D}{P_{12}}
\]

**Terms**

- `P_{12}`: local price 12 months prior to previous month-end
- `P_1`: local price 1 month prior to previous month-end
- `D`: dividends paid over the interval, reinvested on the ex-date

**Plain-English Explanation**  
This is the stock's local-currency total return over the standard `12-1` momentum window.

**Why Morningstar Uses It**  
Morningstar follows the classic momentum construction that skips the most recent month and measures performance over the prior 11 months.

**Interpretation**

- higher total return usually means stronger raw momentum

**Reference**

- p. 12, `Momentum Factor`

---

## 9. Momentum Raw Score

**Purpose**  
Adjusts total return for the local risk-free rate.

**Formula**

\[
MOM = TR - RF
\]

**Terms**

- `TR`: total return from the previous formula
- `RF`: mean annualized local risk-free rate over the lookback window

**Plain-English Explanation**  
Momentum is measured as excess return, not just raw return.

**Why Morningstar Uses It**  
Subtracting the local risk-free rate makes the momentum signal more comparable across markets and more consistent with an excess-return framework.

**Interpretation**

- higher `MOM` means stronger momentum exposure

**Reference**

- p. 13, `Momentum Factor`

---

## 10. Low Volatility Composite

**Purpose**  
Defines Morningstar's low-volatility factor exposure.

**Formula**

\[
Volatility\ Composite = 50\% \times IVOL_z + 25\% \times TVOL_z + 25\% \times MAX5
\]

Morningstar then flips the sign so that larger values indicate lower volatility.

**Terms**

- `IVOL_z`: standardized idiosyncratic volatility
- `TVOL_z`: standardized total volatility
- `MAX5`: average of the highest five daily returns over the past month

**Plain-English Explanation**  
Morningstar combines several different volatility-related measures into one composite and then flips the sign so the factor behaves like a low-volatility score.

**Why Morningstar Uses It**  
No single volatility proxy captures the whole low-volatility effect. Morningstar blends firm-specific risk, total volatility, and lottery-like extreme return behavior.

**Interpretation**

- larger final factor values -> lower-volatility exposure

**Reference**

- p. 12, `Low Volatility Factor`

---

## 11. CAPM Regression Used for Idiosyncratic Volatility

**Purpose**  
Defines the regression used to estimate CAPM residuals for the low-volatility factor.

**Formula**

\[
r_{i,t} - r_{f,t} = \alpha_{i,t} + \beta_t (r_{m,t} - r_{f,t}) + \epsilon_{i,t}
\]

**Terms**

- `r_{i,t}`: stock return
- `r_{f,t}`: risk-free rate
- `r_{m,t}`: market return
- `\alpha`: regression intercept
- `\beta`: market sensitivity
- `\epsilon_{i,t}`: residual return component

**Plain-English Explanation**  
Morningstar separates each stock's return into market-driven and residual pieces.

**Why Morningstar Uses It**  
The residuals are then used to estimate idiosyncratic volatility rather than total market-linked volatility.

**Reference**

- p. 12, `Low Volatility Factor`

---

## 12. Idiosyncratic Volatility

**Purpose**  
Measures the volatility of the CAPM residual.

**Formula**

\[
IVOL = std(\epsilon_{i,t})
\]

**Terms**

- `\epsilon_{i,t}`: CAPM residual
- `std(...)`: standard deviation

**Plain-English Explanation**  
This captures the part of volatility that is specific to the stock rather than explained by the market.

**Why Morningstar Uses It**  
Idiosyncratic volatility is one of the building blocks of Morningstar's low-volatility composite.

**Reference**

- p. 12, `Low Volatility Factor`

---

## 13. Total Volatility

**Purpose**  
Measures the volatility of the stock's raw daily returns.

**Formula**

\[
TVOL = std(r_{i,t})
\]

**Terms**

- `r_{i,t}`: stock return
- `std(...)`: standard deviation

**Plain-English Explanation**  
This is the stock's total return volatility over the lookback window.

**Why Morningstar Uses It**  
Morningstar combines this with idiosyncratic volatility and MAX5 to create a broader low-volatility signal.

**Reference**

- p. 12, `Low Volatility Factor`

---

## 14. Total Yield

**Purpose**  
Defines the yield factor.

**Formula**

\[
Total\ Yield = Buyback\ Yield_{ttm} + Dividend\ Yield_{ttm}
\]

**Terms**

- `Buyback Yield_ttm`: trailing 12-month buyback yield
- `Dividend Yield_ttm`: trailing 12-month dividend yield

**Plain-English Explanation**  
Morningstar treats shareholder yield as the combination of dividends and buybacks.

**Why Morningstar Uses It**  
This broadens the yield concept beyond just dividends and captures another way companies return capital to shareholders.

**Interpretation**

- higher total yield means larger positive yield exposure
- the rulebook says the yield factor is `sector neutralized`

**Reference**

- p. 14, `Yield Factor`

---

## 15. Region and Sector Constraint Bands

**Purpose**  
Defines the main active-weight constraint framework used in the optimizer.

**Constraint Rules**

For `quality`, `size`, `value`, and `yield`:

\[
Region\ or\ Sector\ Weight = Benchmark\ Weight \pm 2\%
\]

If no feasible solution is found, Morningstar loosens the bound in `1%` increments up to `15%`.

For `momentum` and `low volatility`:

\[
Region\ or\ Sector\ Weight = Benchmark\ Weight \pm 10\%
\]

If no feasible solution is found, Morningstar loosens the bound in `1%` increments up to `25%`.

**Plain-English Explanation**  
These are not factor formulas, but they are mathematical portfolio rules that strongly shape the final index.

**Why Morningstar Uses It**  
The active bands are meant to stop the index from turning into an unintended region or sector bet.

**Reference**

- pp. 5-6, `Index Constraints via Optimization`
- Appendix 5, p. 16

---

## 16. Stock-Level Constraint Rules

**Purpose**  
Defines the stock-level limits inside the optimizer.

**Constraint Rules**

\[
Weight_i \le 20 \times BenchmarkWeight_i
\]

\[
Weight_i \le BenchmarkWeight_i + 4\%
\]

\[
Minimum\ Nonzero\ Weight = 1\ basis\ point
\]

No short positions are allowed.

**Plain-English Explanation**  
These rules stop any one stock from becoming too dominant relative to the benchmark.

**Why Morningstar Uses It**  
The factor tilt may point toward concentrated positions, but the final index must still be investable and benchmark-aware.

**Reference**

- p. 5, `Index Constraints via Optimization`

---

## Key Takeaways

- Morningstar uses formulas mainly to define `factor exposures` and `benchmark-relative tilts`.
- The most important formulas for your immediate project are:
  - `quality`
  - `value`
  - `factor_score`
  - `factor weight`
  - the active-weight and stock-weight constraints
- Morningstar quality is materially simpler than FTSE quality.
- The rulebook is stronger on `implementation mechanics` than on academic factor justification.

