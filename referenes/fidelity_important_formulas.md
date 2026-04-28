# Important Formulas from the Fidelity Global Quality Value Index Methodology

Source: `methodology-fidelity-global-quality-value-index.pdf`

This note extracts the main mathematical formulas and formula-like construction rules from the Fidelity Global Quality Value methodology. Some of these are printed explicitly in the methodology. Others are described in words and are rewritten here in clean mathematical form so the full process is easier to follow.

This document is especially important because Fidelity is not just defining a `quality` factor. It is building a live `Quality Value` index. That means the formulas below cover:

- factor definitions
- standardization rules
- gating rules
- selection rules
- weighting rules
- monthly maintenance rules

## How Fidelity Thinks About Quality Value

Fidelity's methodology is not a single blended score across the full universe. It is a staged process:

1. Start from a benchmark-based selection universe.
2. Build peer-relative `quality`, `ESG`, and `value` signals.
3. Eliminate names with weak combined `quality + ESG`.
4. Rank the survivors on `value`, adjusted for `size`.
5. Preserve country and sector neutrality through group-based selection and weighting.

That is why the formulas below are best understood as pieces of a sequential portfolio-construction system rather than standalone research ratios.

---

## 1. Cash Flow Margin

**Purpose**  
Measures the non-bank company's ability to convert revenue into operating cash flow.

**Formula**

\[
Cash\ Flow\ Margin = \frac{Operating\ Cash\ Flow}{Revenue}
\]

**Terms**

- `Operating Cash Flow`: trailing-12-month operating cash flow
- `Revenue`: trailing-12-month revenue

**Plain-English Explanation**  
This shows how much cash a company generates from each dollar of sales.

**Why Fidelity Uses It**  
Fidelity wants quality to include a cash-generation measure, not just an accounting-profit measure. This helps distinguish companies with stronger earnings quality and stronger cash conversion from companies whose reported profits may be less robust.

**Interpretation**

- Higher values are better for quality
- Lower values are worse for quality

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8

---

## 2. Return on Invested Capital (ROIC)

**Purpose**  
Measures profitability relative to invested capital for non-bank companies.

**Formula**

\[
ROIC = \frac{EBIT}{Total\ Capital}
\]

**Terms**

- `EBIT`: earnings before interest and taxes over the last 12 months
- `Total Capital`: total invested capital committed by equity and debt holders

**Plain-English Explanation**  
This shows how effectively the company generates operating profit from the capital invested in the business.

**Why Fidelity Uses It**  
Fidelity wants quality to capture profitability in a way that accounts for capital structure and capital efficiency, not just raw earnings.

**Interpretation**

- Higher `ROIC` is better for quality
- Lower `ROIC` is worse for quality

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8

---

## 3. Free Cash Flow Stability

**Purpose**  
Measures the consistency of a non-bank company's free-cash-flow generation.

**Formula**

\[
Free\ Cash\ Flow\ Stability =
\frac{\#\ of\ trailing\ 20\ quarters\ where\ (Operating\ Cash\ Flow - Capex) > 0}{20}
\]

**Terms**

- `Operating Cash Flow`: operating cash flow for a quarter
- `Capex`: capital expenditures for a quarter
- `20`: trailing 20 quarters used by the methodology

**Plain-English Explanation**  
This measures how often the company has generated positive free cash flow over the last 20 quarters.

**Why Fidelity Uses It**  
Fidelity wants quality to reward not only strong profitability, but consistency and financial resilience. A company that regularly generates positive free cash flow is treated as more durable.

**Interpretation**

- Higher values are better for quality
- A value near `1` means free cash flow has been positive in almost every quarter

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8

---

## 4. MSCI Industry-Adjusted Company Score

**Purpose**  
Serves as Fidelity's sole ESG metric.

**Formula**

This is a vendor-provided score rather than a Fidelity-created equation:

\[
ESG\ Raw\ Score = MSCI\ Industry\ Adjusted\ Company\ Score
\]

with score range:

\[
0 \le ESG\ Raw\ Score \le 10
\]

**Terms**

- `MSCI Industry Adjusted Company Score`: company-level MSCI ESG score, industry-relative

**Plain-English Explanation**  
This is MSCI's view of how well the company manages financially relevant ESG risks and opportunities.

**Why Fidelity Uses It**  
Fidelity wants ESG built directly into the factor process, not just used as a separate exclusion overlay.

**Interpretation**

- Higher values are better
- Lower values are worse

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8

---

## 5. Free Cash Flow Yield

**Purpose**  
Measures how much free cash flow a non-bank company generates relative to its share price.

**Formula**

\[
Free\ Cash\ Flow\ Yield = \frac{Free\ Cash\ Flow\ Per\ Share}{Share\ Price}
\]

**Terms**

- `Free Cash Flow Per Share`: free cash flow on a per-share basis
- `Share Price`: current share price

**Plain-English Explanation**  
This measures cash-generation value relative to market price.

**Why Fidelity Uses It**  
Fidelity wants value to include a cash-based valuation measure, not just earnings- or book-based measures.

**Interpretation**

- Higher values are cheaper / more attractive
- Lower values are more expensive / less attractive

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8

---

## 6. EBITDA to Enterprise Value

**Purpose**  
Measures operating profitability relative to total enterprise value for non-bank companies.

**Formula**

\[
EBITDA/EV = \frac{Adjusted\ EBITDA}{Enterprise\ Value}
\]

**Terms**

- `Adjusted EBITDA`: EBITDA adjusted for research and development expenses
- `Enterprise Value`: market value of equity plus net debt and other claims as defined by the methodology inputs

**Plain-English Explanation**  
This measures how much operating earnings the company generates relative to the total value of the business.

**Why Fidelity Uses It**  
Fidelity wants value to include a capital-structure-aware valuation measure rather than relying only on price-based equity multiples.

**Interpretation**

- Higher values are cheaper
- Lower values are more expensive

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8

---

## 7. Tangible Book Value to Price

**Purpose**  
Measures asset-based value relative to share price.

**Formula**

\[
Tangible\ Book\ Value\ to\ Price =
\frac{Tangible\ Book\ Value\ Per\ Share}{Share\ Price}
\]

where:

\[
Tangible\ Book\ Value = Total\ Book\ Value - Intangible\ Assets
\]

excluding R&D adjustments as described in the methodology.

**Terms**

- `Tangible Book Value Per Share`: book value net of intangibles on a per-share basis
- `Share Price`: current share price

**Plain-English Explanation**  
This compares the company's tangible asset base to its market value.

**Why Fidelity Uses It**  
Fidelity wants value to include an asset-based measure, especially one that is less distorted by intangible accounting.

**Interpretation**

- Higher values are cheaper
- Lower values are more expensive

**Reference**

- `Composite Quality, ESG, and Value Scores`, pp. 8-9

---

## 8. Next-Twelve-Month Earnings to Price

**Purpose**  
Measures forward earnings power relative to share price.

**Formula**

\[
NTM\ Earnings\ to\ Price =
\frac{Consensus\ Next\ 12\ Month\ EPS}{Share\ Price}
\]

with EPS adjusted for research and development expenses as stated in the methodology.

**Terms**

- `Consensus Next 12 Month EPS`: analyst-consensus expected earnings per share for the next 12 months
- `Share Price`: current share price

**Plain-English Explanation**  
This is a forward earnings yield.

**Why Fidelity Uses It**  
Fidelity wants value to include forward-looking earnings power rather than only trailing fundamentals.

**Interpretation**

- Higher values are cheaper
- Lower values are more expensive

**Reference**

- `Composite Quality, ESG, and Value Scores`, pp. 8-9

---

## 9. Bank Return on Equity

**Purpose**  
Serves as the bank-specific profitability metric.

**Formula**

\[
ROE_{bank} = \frac{Net\ Income}{Shareholders'\ Equity}
\]

**Terms**

- `Net Income`: last-12-month net income
- `Shareholders' Equity`: equity from the last available report

**Plain-English Explanation**  
This measures how profitably the bank is using shareholder capital.

**Why Fidelity Uses It**  
Banks are treated differently because standard non-bank quality metrics like cash flow margin and ROIC are less appropriate for them.

**Interpretation**

- Higher values are better for bank quality
- Lower values are worse for bank quality

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 9

---

## 10. Bank Debt to Assets

**Purpose**  
Serves as the bank-specific leverage metric.

**Formula**

\[
Debt/Assets = \frac{Total\ Debt}{Total\ Assets}
\]

**Terms**

- `Total Debt`: total debt from the last annual report
- `Total Assets`: total assets from the last annual report

**Plain-English Explanation**  
This measures bank leverage relative to the size of the balance sheet.

**Why Fidelity Uses It**  
Fidelity wants to penalize the most highly levered banks inside the bank-quality framework.

**Interpretation**

- Lower values are better
- Higher values are worse

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 9

---

## 11. Bank Debt-to-Assets Penalty Rule

**Purpose**  
Converts bank leverage into a very simple quality penalty.

**Formula**

The methodology states this as a rule rather than a continuous equation:

\[
z_{Debt/Assets} =
\begin{cases}
-2, & \text{if the stock is in the highest quintile of Debt/Assets} \\
0, & \text{otherwise}
\end{cases}
\]

**Terms**

- `highest quintile`: top 20% of banks by debt-to-assets ratio
- `z_{Debt/Assets}`: leverage penalty used in bank quality scoring

**Plain-English Explanation**  
The most highly levered banks receive a negative penalty; everyone else receives no leverage penalty.

**Why Fidelity Uses It**  
This is a deliberately blunt rule. Fidelity is not trying to fine-tune bank leverage continuously; it is trying to penalize the worst leverage bucket.

**Interpretation**

- Being in the highest leverage quintile hurts quality sharply
- All other banks avoid that penalty

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 9

---

## 12. Price Momentum Screen

**Purpose**  
Removes the weakest recent price performers inside each country+sector group.

**Formula**

The methodology describes this in words. Rewritten cleanly:

\[
Price\ Momentum = Simple\ Total\ Return\ from\ t-12m\ to\ t-1m
\]

and then:

\[
Momentum\ Percentile\ Rank =
\frac{Rank\ within\ country+sector\ group}{Count\ of\ securities\ in\ group}
\]

Stocks are excluded if:

\[
Momentum\ Percentile\ Rank \le 5\%
\]

**Terms**

- `t-12m`: same date of the month 12 months before the observation date
- `t-1m`: same date of the month one month before the observation date

**Plain-English Explanation**  
This removes the bottom 5% of momentum names within each peer group.

**Why Fidelity Uses It**  
Fidelity labels this a data-quality screen, but functionally it also helps avoid the very weakest price-trend names before factor selection.

**Interpretation**

- Lower momentum is worse
- The worst 5% by group are removed

**Reference**

- `Data`, p. 12
- `Data Quality Screens`, p. 13

---

## 13. Winsorization Rule

**Purpose**  
Limits the impact of outliers before z-score standardization.

**Formula**

The methodology states the thresholds in words. Rewritten as:

\[
x_{wins} =
\begin{cases}
P2(x), & x < P2(x) \\
x, & P2(x) \le x \le P98(x) \\
P98(x), & x > P98(x)
\end{cases}
\]

This corresponds to keeping the middle `96%` of the distribution and resetting extreme tails to the threshold values.

**Terms**

- `x`: raw metric value
- `x_{wins}`: winsorized metric value
- `P2(x)`: 2nd-percentile threshold
- `P98(x)`: 98th-percentile threshold

**Plain-English Explanation**  
Values below the 2nd percentile are raised to the 2nd-percentile level, and values above the 98th percentile are lowered to the 98th-percentile level.

**Why Fidelity Uses It**  
Fidelity wants the z-score process to be less distorted by extreme outliers.

**Interpretation**

- Extreme values are clipped
- Mid-range values are left unchanged

**Reference**

- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

---

## 14. Group-Level Z-Score

**Purpose**  
Standardizes each metric within a country+sector group.

**Formula**

\[
z_i = \frac{x_{wins,i} - \mu_{group}}{\sigma_{group}}
\]

with:

\[
z_i \in [-3, 3]
\]

after capping.

**Terms**

- `x_{wins,i}`: winsorized value for stock `i`
- `\mu_{group}`: mean of eligible securities in the same country+sector group
- `\sigma_{group}`: standard deviation of eligible securities in the same country+sector group
- `z_i`: capped z-score for stock `i`

**Plain-English Explanation**  
This measures how far each stock is above or below its peer-group average.

**Why Fidelity Uses It**  
Fidelity wants comparisons to be local to country and sector context, not global across structurally different types of companies.

**Interpretation**

- Positive values mean above-peer-group average on that metric
- Negative values mean below-peer-group average

**Reference**

- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

---

## 15. Composite Quality Score

**Purpose**  
Combines the quality metrics into one peer-relative quality measure.

**Formula**

For non-banks, rewritten from the methodology:

\[
Q_{raw} = \frac{z_{CFM} + z_{ROIC} + z_{FCFS}}{3}
\]

For banks, rewritten from the methodology:

\[
Q_{raw,bank} = \frac{z_{ROE} + z_{Debt/Assets}}{2}
\]

Fidelity then standardizes this raw quality signal again within the relevant group:

\[
Composite\ Quality\ Score = cap_3\left(zscore(Q_{raw})\right)
\]

**Terms**

- `z_{CFM}`: z-score of cash flow margin
- `z_{ROIC}`: z-score of return on invested capital
- `z_{FCFS}`: z-score of free cash flow stability
- `z_{ROE}`: z-score of bank ROE
- `z_{Debt/Assets}`: bank leverage penalty term

**Plain-English Explanation**  
Fidelity averages the quality inputs, then standardizes the combined quality signal again.

**Why Fidelity Uses It**  
This creates one integrated quality measure rather than leaving quality as a basket of separate metrics.

**Interpretation**

- Higher values mean stronger quality
- Lower values mean weaker quality

**Reference**

- `Composite Quality, ESG, and Value Scores`, pp. 8-9
- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

---

## 16. ESG Score

**Purpose**  
Converts the raw MSCI ESG metric into the same group-relative scoring language used elsewhere.

**Formula**

With one ESG metric, Fidelity's ESG score is effectively:

\[
ESG\ Score = cap_3\left(zscore(MSCI\ Industry\ Adjusted\ Company\ Score)\right)
\]

**Terms**

- `MSCI Industry Adjusted Company Score`: raw MSCI ESG score
- `ESG Score`: group-relative standardized ESG score

**Plain-English Explanation**  
This is the peer-relative ESG score used in the combined quality-plus-ESG gate.

**Why Fidelity Uses It**  
Fidelity wants ESG in the same standardized score language as the quality metrics.

**Interpretation**

- Higher values are better
- Lower values are worse

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8
- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

---

## 17. Combined Quality and ESG Score

**Purpose**  
Acts as the main pre-value gate.

**Formula**

\[
Combined\ Quality\ and\ ESG\ Score =
\frac{Composite\ Quality\ Score + ESG\ Score}{2}
\]

Stocks are eliminated if:

\[
Combined\ Quality\ and\ ESG\ Score < 0
\]

**Terms**

- `Composite Quality Score`: standardized quality score
- `ESG Score`: standardized ESG score

**Plain-English Explanation**  
Fidelity first asks whether the stock is at least acceptable on the combined quality-and-ESG dimension before it lets value drive selection.

**Why Fidelity Uses It**  
This is the methodology's gating step. It prevents very low-quality or low-ESG names from being selected just because they look cheap.

**Interpretation**

- Positive scores survive
- Negative scores are removed

**Reference**

- `Composite Quality, ESG, and Value Scores`, p. 8
- `Calculating Composite Quality, ESG Scores, and Value Scores`, p. 13

---

## 18. Value Score

**Purpose**  
Combines the value metrics into one peer-relative value measure.

**Formula**

For non-banks:

\[
V_{raw} =
\frac{z_{FCFY} + z_{EBITDA/EV} + z_{TBV/P} + z_{NTM\ E/P}}{4}
\]

For banks:

\[
V_{raw,bank} =
\frac{z_{TBV/P} + z_{NTM\ E/P}}{2}
\]

Fidelity then standardizes this raw value signal again:

\[
Value\ Score = cap_3\left(zscore(V_{raw})\right)
\]

**Terms**

- `z_{FCFY}`: z-score of free cash flow yield
- `z_{EBITDA/EV}`: z-score of EBITDA to enterprise value
- `z_{TBV/P}`: z-score of tangible book value to price
- `z_{NTM E/P}`: z-score of next-twelve-month earnings to price

**Plain-English Explanation**  
Fidelity averages the value metrics and re-standardizes the combined value signal.

**Why Fidelity Uses It**  
This gives Fidelity one integrated value ranking variable after the quality-and-ESG gate has been applied.

**Interpretation**

- Higher values are cheaper / more attractive
- Lower values are more expensive / less attractive

**Reference**

- `Composite Quality, ESG, and Value Scores`, pp. 8-9
- `Calculating Composite Quality, ESG Scores, and Value Scores`, pp. 13-14

---

## 19. Size Factor Score

**Purpose**  
Measures the stock's size within its country+sector group.

**Formula**

\[
Size\ Factor\ Score = cap_3\left(zscore(\ln(Free\ Float\ Market\ Capitalization))\right)
\]

**Terms**

- `Free Float Market Capitalization`: combined free-float market cap for all share classes
- `ln(...)`: natural logarithm

**Plain-English Explanation**  
This is a standardized size score based on log market capitalization.

**Why Fidelity Uses It**  
Fidelity wants to remove unwanted size bias from the value process.

**Interpretation**

- Higher values correspond to larger stocks within the group
- Lower values correspond to smaller stocks within the group

**Reference**

- `Calculating the Size Adjusted Value Scores`, p. 14

---

## 20. Size-Adjusted Value Score

**Purpose**  
Creates the final selection-ranking score by blending value with size.

**Formula**

\[
Size\ Adjusted\ Value\ Score =
0.6 \times Value\ Score + 0.4 \times Size\ Factor\ Score
\]

**Terms**

- `Value Score`: standardized combined value score
- `Size Factor Score`: standardized size score

**Plain-English Explanation**  
This is Fidelity's final ranking score for constituent selection.

**Why Fidelity Uses It**  
Fidelity explicitly wants to keep the value portfolio from drifting too far into small-cap bias.

**Interpretation**

- Higher values rank better for selection
- The stock must first survive the combined quality-and-ESG gate before this score matters

**Reference**

- `Calculating the Size Adjusted Value Scores`, p. 14

---

## 21. Group-Level Stock Count Target

**Purpose**  
Allocates the approximate number of selected stocks to each country+sector group.

**Formula**

\[
Target\ Stocks_{group} =
Market\ Cap\ Weight_{group\ in\ Selection\ Universe} \times 250
\]

subject to a minimum of:

\[
Target\ Stocks_{group} \ge 3
\]

If the group still results in fewer than 3 stocks, the group is dropped from the final selection.

**Terms**

- `Market Cap Weight_{group in Selection Universe}`: group weight inside the selection universe
- `250`: Fidelity's approximate total-stock target

**Plain-English Explanation**  
Larger country+sector groups get more selected stocks.

**Why Fidelity Uses It**  
Fidelity wants group-level neutrality and broad representation rather than global top-N selection.

**Interpretation**

- Bigger groups get more slots
- Very small groups can be excluded entirely

**Reference**

- `Selecting Constituents`, p. 14

---

## 22. Annual Stock Weight

**Purpose**  
Determines the stock's annual reconstitution weight inside the final index.

**Formula**

\[
Stock\ Weight_i =
Market\ Cap\ Weight\ in\ Selection\ Universe_i +
Overweight\ Adjustment_i
\]

**Terms**

- `Market Cap Weight in Selection Universe_i`: the stock's weight in the selection universe
- `Overweight Adjustment_i`: equal-excess uplift applied within the country+sector group

**Plain-English Explanation**  
Fidelity starts with the stock's benchmark-like group weight and then adds a uniform excess-weight increment across selected stocks in the group.

**Why Fidelity Uses It**  
This lets Fidelity preserve group neutrality while reducing concentration in the largest names.

**Interpretation**

- Every selected stock in the same group gets the same excess increment
- Larger stocks still matter, but concentration is reduced

**Reference**

- `Weighting Constituents in an Annual Reconstitution Observation Date`, p. 15

---

## 23. Equal-Excess Overweight Adjustment

**Purpose**  
Redistributes the weight of excluded names evenly across the selected names inside a country+sector group.

**Formula**

Rewritten from Fidelity's printed equation:

\[
Overweight\ Adjustment_i =
\frac{
\sum_{k=1}^{M} Market\ Cap\ Weight\ in\ Selection\ Universe_k -
\sum_{k=1}^{N} Market\ Cap\ Weight\ in\ Final\ Selection_k
}{N}
\]

**Terms**

- `M`: number of stocks in the country+sector group inside the selection universe
- `N`: number of selected stocks in that group inside the final selection
- `Market Cap Weight in Selection Universe_k`: stock `k` weight in the selection universe
- `Market Cap Weight in Final Selection_k`: selected stock `k` weight before the equal-excess increment

**Plain-English Explanation**  
This is the leftover group weight from names that were not selected, divided equally among the selected names.

**Why Fidelity Uses It**  
Fidelity wants group weights to stay benchmark-aware while reducing single-stock concentration.

**Interpretation**

- Smaller selected names benefit proportionally more from the equal excess
- The group's total weight stays aligned with the selection universe

**Reference**

- `Weighting Constituents in an Annual Reconstitution Observation Date`, p. 15

---

## 24. Index-Level ESG Exposure

**Purpose**  
Measures the portfolio's ESG exposure after constituent selection and initial weighting.

**Formula**

Rewritten from the methodology:

\[
Index\ ESG\ Exposure = \sum_i w_i \times z_{ESG,i}
\]

\[
Universe\ ESG\ Exposure = \sum_i w^{univ}_i \times z_{ESG,i}
\]

If:

\[
Index\ ESG\ Exposure < Universe\ ESG\ Exposure
\]

then weights are scaled until:

\[
Index\ ESG\ Exposure =
Universe\ ESG\ Exposure + 0.1
\]

where `0.1` means one-tenth of a standard deviation.

**Terms**

- `w_i`: index weight of stock `i`
- `w^{univ}_i`: selection-universe market-cap weight of stock `i`
- `z_{ESG,i}`: ESG z-score of stock `i`

**Plain-English Explanation**  
If the portfolio's ESG exposure is too low, Fidelity adjusts weights until the portfolio's ESG exposure is slightly better than the universe's.

**Why Fidelity Uses It**  
Fidelity wants the final index to show measurable ESG improvement, not just exclusions.

**Interpretation**

- Higher-ESG names are scaled up
- Lower-ESG names are scaled down
- The target is universe exposure plus `0.1` standard deviations

**Reference**

- `ESG Exposure`, p. 15
- `Appendix II - Methodology Changes`, pp. 25-26

---

## 25. Monthly Replacement Weight Formula

**Purpose**  
Determines how replacement stocks are added during non-annual rebalances.

**Formula**

The methodology describes this in words. Rewritten cleanly:

\[
Replacement\ Weight =
Selection\ Universe\ Weight +
Average\ Excess\ Weight\ of\ Existing\ Constituents\ in\ the\ Group
\]

**Terms**

- `Selection Universe Weight`: replacement stock's market-cap weight in the selection universe
- `Average Excess Weight`: average equal-excess uplift already embedded in the group's current holdings

**Plain-English Explanation**  
Replacement names are inserted using the same general weight logic as the annual portfolio.

**Why Fidelity Uses It**  
Fidelity wants monthly maintenance to preserve the same structural weighting design rather than create an ad hoc replacement process.

**Interpretation**

- Replacements inherit the same group architecture
- Country+sector neutrality is preserved

**Reference**

- `Weighting Constituents in a Non-Annual Reconstitution Observation Date`, pp. 15-16

---

## 26. Monthly Rescaling Formula

**Purpose**  
Rescales the portfolio if there are not enough replacement stocks available in a country+sector group.

**Formula**

\[
Final\ Stock\ Weight_j =
\frac{Stock\ Weight_j}{\sum_{j=1}^{P} Stock\ Weight_j}
\]

**Terms**

- `Stock Weight_j`: current pre-rescaling stock weight
- `P`: number of remaining stocks in the index

**Plain-English Explanation**  
If replacement weight cannot be fully restored, Fidelity rescales the remaining holdings to sum to 100%.

**Why Fidelity Uses It**  
This ensures the index remains fully invested even when there are insufficient replacement candidates.

**Interpretation**

- Remaining constituents are scaled proportionally
- The index stays normalized to 100%

**Reference**

- `Weighting Constituents in a Non-Annual Reconstitution Observation Date`, p. 16

