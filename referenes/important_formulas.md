# Important Formulas from the FTSE Russell Quality Factor Paper

Source paper: `FTSE_Quality_Factor_Paper.pdf`

This document rewrites the main mathematical expressions from the paper in a cleaner format and explains:

- what the formula measures
- what each term means
- why FTSE includes it in the research or methodology
- how FTSE interprets high or low values

## How FTSE Thinks About Quality

The paper is not just a list of accounting ratios. FTSE is trying to solve a portfolio-design problem:

1. Define `quality` in a way that is economically sensible.
2. Test whether the chosen signals are associated with stronger future fundamentals and better stock outcomes.
3. Build an investable index that captures the factor without becoming too concentrated, illiquid, or high-turnover.

That is why some formulas in the paper are:

- `conceptual` formulas used to motivate the idea of quality
- `signal` formulas used to score companies
- `portfolio construction` formulas used to turn scores into an index

The paper also compares multiple candidate measures and does **not** keep them all. One of its main conclusions is that `profitability + leverage` is a stronger final definition of quality than `profitability + growth`.

---

## 1. Gordon Growth Framing of Quality

**Purpose**  
This is the high-level valuation identity FTSE uses to motivate the idea of quality. It is not the final portfolio construction formula, but it explains why profitability, safety, growth, and payout might affect stock prices.

**Formula**

\[
P = \frac{D}{r - g} = \frac{Earnings \times Payout\ Ratio}{r - g}
\]

**Terms**

- \( P \): current stock price
- \( D \): dividend
- \( r \): discount rate or required return
- \( g \): expected dividend growth rate
- \( Earnings \): company earnings
- \( Payout\ Ratio \): proportion of earnings paid out to shareholders

**Plain-English Explanation**  
A stock can deserve a higher price if it has higher earnings, a higher payout ratio, lower risk, or stronger expected growth.

**Why FTSE Uses It**  
FTSE starts here because it needs a theoretical reason for why a “quality” factor should exist at all. This identity shows that stock prices are linked to a few core economic drivers: the amount a company earns, how much of those earnings reach shareholders, how risky the company is, and how fast those cash flows can grow. FTSE is basically saying: if we want to build a quality index, we should look for accounting measures that proxy for those underlying traits. That is why the rest of the paper focuses on profitability, earnings quality, operating efficiency, leverage, and growth. The formula is therefore a conceptual map, not a stock-ranking rule.

**Interpretation**

- Higher earnings can support a higher valuation
- Higher payout can support a higher valuation
- Lower required return \(r\) implies safer companies and a higher valuation
- Higher sustainable growth \(g\) implies a higher valuation

---

## 2. Return on Assets (ROA)

**Purpose**  
Measures how profitable a company is relative to its asset base.

**Formula**

\[
ROA_t = \frac{Net\ Income_t}{\frac{Total\ Assets_t + Total\ Assets_{t-1}}{2}}
\]

**Terms**

- \( ROA_t \): return on assets in period \(t\)
- \( Net\ Income_t \): net income in period \(t\)
- \( Total\ Assets_t \): total assets in period \(t\)
- \( Total\ Assets_{t-1} \): total assets in the prior period
- Denominator: average total assets across the current and previous period

**Plain-English Explanation**  
ROA asks: how much profit did the company produce for each dollar of assets it employed?

**Why FTSE Uses It**  
FTSE wants a profitability measure that reflects the economics of the whole firm, not just the equity slice. ROE can be flattered by leverage, capital structure changes, or buybacks. ROA is harder to manipulate in that way because it measures earnings against the full asset base. In the paper, FTSE finds that firms with high current ROA tend to have better future profitability, which is exactly what the paper wants from a quality signal: not just “good accounting today,” but some persistence into the future. FTSE therefore treats ROA as the anchor variable for quality, especially for identifying firms with strong underlying profitability.

**Interpretation**

- Higher ROA usually indicates stronger profitability
- Lower ROA usually indicates weaker profitability
- In FTSE's framework, higher ROA contributes positively to quality

---

## 3. Asset Turnover (ATO)

**Purpose**  
Measures how efficiently a company uses assets to generate sales.

**Formula**

\[
ATO_t = \frac{Sales_t}{Total\ Assets_t}
\]

**Terms**

- \( ATO_t \): asset turnover in period \(t\)
- \( Sales_t \): sales or revenue in period \(t\)
- \( Total\ Assets_t \): total assets in period \(t\)

**Plain-English Explanation**  
This shows how much revenue the company generates per dollar of assets.

**Why FTSE Uses It**  
FTSE includes ATO because profitability alone does not tell you *how* the firm is producing that profitability. A company can show decent profits for reasons that may not be durable. Asset turnover helps FTSE look inside the profitability number and ask whether the firm is actually becoming more operationally efficient. FTSE leans on prior research showing that changes in ATO can signal future profitability improvements. In the paper, ATO is not really used as a standalone quality signal; its main value comes from showing whether profitability is being supported by better asset utilization.

**Interpretation**

- Higher ATO suggests stronger asset efficiency
- Lower ATO suggests weaker asset efficiency
- ATO by itself matters less in the paper than the change in ATO

---

## 4. Change in Asset Turnover

**Purpose**  
Measures whether operating efficiency is improving or deteriorating.

**Formula**

\[
\Delta ATO_t = ATO_t - ATO_{t-1}
\]

**Terms**

- \( \Delta ATO_t \): change in asset turnover in period \(t\)
- \( ATO_t \): current-period asset turnover
- \( ATO_{t-1} \): prior-period asset turnover

**Plain-English Explanation**  
This asks whether the company is getting better or worse at turning assets into sales.

**Why FTSE Uses It**  
This is one of the paper’s more important design choices. FTSE does not want to treat all high-profit firms as equally high-quality. It wants to separate firms whose profitability is being reinforced by improving operations from firms whose profits may be less durable. Change in ATO does that job. In the empirical section, FTSE shows that firms with both high ROA and improving ATO tend to have stronger future ROA than firms with only high ROA. So \(\Delta ATO\) is valuable because it adds information about the *quality of profitability*, not just its level.

**Interpretation**

- Positive values indicate improving efficiency
- Negative values indicate deteriorating efficiency
- In FTSE's model, higher \(\Delta ATO\) supports a higher quality score

---

## 5. Profit Margin

**Purpose**  
Measures profitability per dollar of sales.

**Formula**

\[
Profit\ Margin = \frac{Net\ Income}{Sales}
\]

**Terms**

- \( Net\ Income \): accounting profit
- \( Sales \): revenue

**Plain-English Explanation**  
This shows how much profit remains from each dollar of revenue.

**Why FTSE Uses It**  
FTSE discusses profit margin mainly to show that profitability can come from several economic channels, such as pricing power, business-model strength, or competitive position. But the paper does not elevate profit margin into the final quality composite because raw margins can vary widely across sectors. That makes it less reliable as a broad, cross-industry quality measure. In other words, FTSE uses it as part of the conceptual discussion of profitability, but not as a central ingredient in the final model.

**Interpretation**

- Higher margins may suggest pricing power or operational strength
- Sector differences make raw margin comparisons harder across industries

---

## 6. Current Accruals

**Purpose**  
Measures the non-cash component of near-term earnings.

**Formula**

\[
Current\ Accruals = \Delta WC - Depreciation
\]

**Terms**

- \( Current\ Accruals \): current accrual measure
- \( \Delta WC \): change in working capital
- \( Depreciation \): depreciation expense

**Plain-English Explanation**  
This helps distinguish cash-backed earnings from earnings driven more by accounting adjustments.

**Why FTSE Uses It**  
FTSE uses accrual measures because the paper views “quality” as partly about earnings persistence. A company whose profits are strongly backed by cash flow is generally more credible than one whose profits depend heavily on accounting accruals. Current accruals are one candidate way to measure that. FTSE is effectively asking: are these reported profits likely to stick, or are they built on transitory accounting components that may reverse? Current accruals are not FTSE’s final preferred accrual definition, but they are part of the comparison set that leads FTSE toward a broader total-accruals measure.

**Interpretation**

- Lower accruals are generally better in this framework
- Higher accruals may indicate less durable earnings quality

---

## 7. Change in Working Capital

**Purpose**  
Provides one building block for accrual measures.

**Formula**

\[
\Delta WC = (\Delta Current\ Assets - \Delta Cash\ \&\ Short\text{-}Term\ Investments) - (\Delta Current\ Liabilities - \Delta Short\text{-}Term\ Debt)
\]

**Terms**

- \( \Delta WC \): change in working capital
- \( \Delta Current\ Assets \): change in current assets
- \( \Delta Cash\ \&\ Short\text{-}Term\ Investments \): change in cash and short-term investments
- \( \Delta Current\ Liabilities \): change in current liabilities
- \( \Delta Short\text{-}Term\ Debt \): change in short-term debt

**Plain-English Explanation**  
This isolates the non-cash change in operating working capital.

**Why FTSE Uses It**  
FTSE uses this because working-capital changes often reveal when reported earnings are drifting away from cash realization. Rising receivables or inventories, for example, can make earnings look healthy even though the underlying cash picture is weaker. FTSE does not use \(\Delta WC\) as a standalone quality factor; instead, it treats it as one of the raw accounting ingredients needed to build accrual-based earnings-quality measures.

**Interpretation**

- Larger positive working-capital build can be a warning sign if it reflects receivables or inventory growth not supported by cash

---

## 8. Current Plus Non-Current Accruals

**Purpose**  
Extends the accrual concept beyond short-term balance-sheet items.

**Formula**

\[
Current\ +\ Non\text{-}Current\ Accruals = (\Delta Total\ Assets - \Delta Cash) - (\Delta Total\ Assets - \Delta Short\text{-}Term\ Debt - \Delta Long\text{-}Term\ Debt - \Delta Minority\ Interests - \Delta Common\ Equity - \Delta Preferred\ Stock)
\]

**Terms**

- \( \Delta Total\ Assets \): change in total assets
- \( \Delta Cash \): change in cash
- \( \Delta Short\text{-}Term\ Debt \): change in short-term debt
- \( \Delta Long\text{-}Term\ Debt \): change in long-term debt
- \( \Delta Minority\ Interests \): change in minority interests
- \( \Delta Common\ Equity \): change in common equity
- \( \Delta Preferred\ Stock \): change in preferred stock

**Plain-English Explanation**  
This tries to capture a broader view of how much of earnings comes from accrual-based balance-sheet changes rather than cash.

**Why FTSE Uses It**  
FTSE includes this because a narrow working-capital accrual measure may miss important non-current balance-sheet movements. If the paper is trying to identify durable earnings, it needs to test whether a broader accrual lens works better than a short-term one. This measure is therefore part of FTSE’s comparison exercise: it helps FTSE judge whether earnings-quality information is concentrated in current accounts or spread across the broader balance sheet.

**Interpretation**

- Higher values generally imply more accrual-based earnings
- FTSE ultimately finds total accruals to be the stronger preferred measure

---

## 9. Total Accruals (TACC)

**Purpose**  
Measures the full non-cash component of earnings using current, non-current, and financial balance-sheet changes.

**Formula**

\[
TACC = \frac{\Delta WC + \Delta NCO + \Delta FIN}{Average\ Total\ Assets}
\]

**Terms**

- \( TACC \): total accruals
- \( \Delta WC \): change in working capital
- \( \Delta NCO \): change in net non-current operating assets
- \( \Delta FIN \): change in net financial assets
- \( Average\ Total\ Assets \): average total assets used to scale the accrual measure

**Plain-English Explanation**  
This gives a scaled measure of how much reported earnings rely on non-cash accounting components.

**Why FTSE Uses It**  
This is FTSE’s preferred accrual formulation because it is broader and, in the paper’s tests, more informative than narrower accrual definitions. FTSE finds that high-accrual firms often show a recognizable pattern: their profitability looked good going into portfolio formation but tends to fade afterward. Low-accrual firms show the opposite pattern more often. That makes total accruals useful for distinguishing firms with repeatable, cash-backed profitability from firms whose profitability may be overstated or less persistent. In the logic of the paper, TACC is therefore not just a measure of “accounting oddities”; it is one of FTSE’s main ways of separating true quality from superficial earnings strength.

**Interpretation**

- Lower TACC is usually better
- Higher TACC may indicate lower earnings persistence
- In FTSE's framework, lower accruals contribute positively to quality

---

## 10. Change in Net Non-Current Operating Assets (Delta NCO)

**Purpose**  
Captures changes in longer-term operating assets and liabilities.

**Formula**

\[
\Delta NCO = (\Delta Total\ Assets - \Delta Current\ Assets - \Delta Investments\ and\ Advances) - (\Delta Total\ Liabilities - \Delta Current\ Liabilities - \Delta Long\text{-}Term\ Debt)
\]

**Terms**

- \( \Delta NCO \): change in net non-current operating assets
- \( \Delta Total\ Assets \): change in total assets
- \( \Delta Current\ Assets \): change in current assets
- \( \Delta Investments\ and\ Advances \): change in investments and advances
- \( \Delta Total\ Liabilities \): change in total liabilities
- \( \Delta Current\ Liabilities \): change in current liabilities
- \( \Delta Long\text{-}Term\ Debt \): change in long-term debt

**Plain-English Explanation**  
This isolates non-current operating balance-sheet changes that feed into the broader accrual measure.

**Why FTSE Uses It**  
FTSE uses this because it wants its accrual measure to capture more than just short-term operating noise. Large changes in plant, equipment, intangibles, or other non-current operating accounts can also matter for whether reported earnings are supported by real economic performance. \(\Delta NCO\) is therefore part of FTSE’s attempt to build a more complete measure of earnings quality.

---

## 11. Change in Net Financial Assets (Delta FIN)

**Purpose**  
Captures financial-balance-sheet changes that also influence accrual-based earnings quality.

**Formula**

\[
\Delta FIN = (\Delta Short\text{-}Term\ Investments + \Delta Long\text{-}Term\ Investments) - (\Delta Long\text{-}Term\ Debt + \Delta Short\text{-}Term\ Debt + \Delta Preferred\ Stock)
\]

**Terms**

- \( \Delta FIN \): change in net financial assets
- \( \Delta Short\text{-}Term\ Investments \): change in short-term investments
- \( \Delta Long\text{-}Term\ Investments \): change in long-term investments
- \( \Delta Long\text{-}Term\ Debt \): change in long-term debt
- \( \Delta Short\text{-}Term\ Debt \): change in short-term debt
- \( \Delta Preferred\ Stock \): change in preferred stock

**Plain-English Explanation**  
This measures how financial asset and financing changes contribute to the broader accrual picture.

**Why FTSE Uses It**  
FTSE includes \(\Delta FIN\) because a company’s accounting quality is not driven only by operating accounts. Financial asset and financing movements can also shape how sustainable reported earnings really are. By including this term inside total accruals, FTSE is trying to avoid a narrow definition of earnings quality.

---

## 12. ROA Growth

**Purpose**  
Measures longer-horizon growth in profitability.

**Formula**

\[
ROA\ Growth = \frac{Net\ Income_t - Net\ Income_{t-5}}{Average\ Total\ Assets\ over\ the\ prior\ 5\ years}
\]

**Terms**

- \( ROA\ Growth \): growth in profitability over five years
- \( Net\ Income_t \): current net income
- \( Net\ Income_{t-5} \): net income five years earlier
- Denominator: average total assets over the prior five years

**Plain-English Explanation**  
This asks whether the company's profitability has improved over a multi-year horizon.

**Why FTSE Uses It**  
FTSE tests growth because some versions of the quality factor treat firms with sustained improving profitability as higher quality. That is a reasonable hypothesis, so FTSE includes growth in the comparison set. But the paper also recognizes the weakness of growth as a quality signal: high growth can attract competition, can be cyclical, and often comes bundled with expensive valuations. In the empirical results, growth does not add as much to the final quality definition as leverage does. So FTSE uses this formula mainly as something to test and compare, not as a core building block of the final non-financial quality composite.

**Interpretation**

- Higher values suggest stronger historical profitability growth
- FTSE treats this as secondary, not core, in the final quality definition

---

## 13. ROA-GARP

**Purpose**  
Measures growth in profitability adjusted for valuation.

**Formula**

\[
ROA\text{-}GARP = \frac{ROA\ Growth}{P/B}
\]

**Terms**

- \( ROA\text{-}GARP \): return-on-assets growth at a reasonable price
- \( ROA\ Growth \): the profitability growth measure above
- \( P/B \): price-to-book ratio

**Plain-English Explanation**  
This tries to identify profitability growth without paying too much for it.

**Why FTSE Uses It**  
FTSE uses this because it does not want to reward growth blindly. A company with strong historical growth may already trade at a very rich valuation, which weakens the investment case if the goal is to find quality that is not already overpriced. Dividing by price-to-book is FTSE’s way of converting a raw growth signal into a “growth at a reasonable price” signal. Even so, the paper finds that profitability plus growth does not improve the quality composite as much as profitability plus leverage. That result is important because it shows FTSE considered the growth route and rejected it as the primary final combination.

**Interpretation**

- Higher values suggest stronger growth relative to valuation
- Useful conceptually, but weaker than the final profitability-plus-leverage definition

---

## 14. Operating Cash Flow to Total Debt (OPCFD)

**Purpose**  
Measures balance-sheet strength and the company's ability to support debt with operating cash flow.

**Formula**

\[
OPCFD = \frac{Operating\ Cash\ Flow}{Total\ Debt}
\]

**Terms**

- \( OPCFD \): operating cash flow to total debt
- \( Operating\ Cash\ Flow \): cash generated by operations
- \( Total\ Debt \): total debt outstanding

**Plain-English Explanation**  
This asks how much operating cash flow the company generates relative to its debt burden.

**Why FTSE Uses It**  
This is FTSE’s preferred leverage-quality measure. The paper argues that leverage is an important dimension of quality because heavily indebted firms are more vulnerable and often have weaker future profitability. But FTSE does not want to use a crude debt ratio alone, because different industries naturally operate with different balance-sheet structures. OPCFD is better aligned with economic reality because it asks whether the company’s cash generation can actually support its debt load. FTSE then makes the measure even more useful by evaluating it on an industry-relative basis for non-financials. That lets the paper treat leverage as a signal of financial resilience rather than a blunt anti-debt screen.

**Interpretation**

- Higher OPCFD means lower effective leverage and stronger balance-sheet quality
- Lower OPCFD means heavier debt burden relative to cash flow
- In FTSE's model, higher OPCFD supports higher quality

---

## 15. Operating Cash Flow to Total Assets (OPCFA)

**Purpose**  
Measures operating cash generation relative to the asset base.

**Formula**

\[
OPCFA = \frac{Operating\ Cash\ Flow}{Total\ Assets}
\]

**Terms**

- \( OPCFA \): operating cash flow to total assets
- \( Operating\ Cash\ Flow \): cash generated by operations
- \( Total\ Assets \): total assets

**Plain-English Explanation**  
This tells you how much operating cash flow the firm generates per dollar of assets.

**Why FTSE Uses It**  
This appears in the definitions appendix as a related measure rather than one of the paper’s central final signals. It helps frame the broader family of cash-flow-based quality measures FTSE considered, but it is not the main leverage signal used in the final composite. In that sense, it is useful background context more than a headline result.

---

## 16. Debt to Assets

**Purpose**  
A basic leverage ratio.

**Formula**

\[
Debt/Assets = \frac{Total\ Debt}{Total\ Assets}
\]

**Terms**

- \( Total\ Debt \): total debt outstanding
- \( Total\ Assets \): total assets

**Plain-English Explanation**  
This shows how much of the asset base is financed with debt.

**Why FTSE Uses It**  
FTSE discusses simple leverage ratios because they are intuitive and common in practice. But the paper is also careful to explain why they are not ideal as the final quality measure. A plain debt ratio can reflect industry structure as much as genuine financial weakness, and it does not directly capture whether the firm can service that debt comfortably. FTSE uses this ratio as a conceptual benchmark, then moves toward OPCFD as the more economically useful implementation measure.

**Interpretation**

- Higher values usually indicate more leverage
- Lower values usually indicate less leverage

---

## 17. Composite Profitability Score

**Purpose**  
Aggregates the main profitability and earnings-quality signals into a single profitability component.

**Formula**

\[
Composite\ Profitability\ Score = \frac{Rank(ROA) + Rank(Accruals) + Rank(\Delta ATO)}{3}
\]

**Terms**

- \( Rank(ROA) \): rank of profitability
- \( Rank(Accruals) \): rank of accrual quality
- \( Rank(\Delta ATO) \): rank of efficiency improvement

**Plain-English Explanation**  
This blends current profitability, earnings quality, and operating improvement into one score.

**Why FTSE Uses It**  
This is a major step in the methodology. FTSE does not trust any single accounting ratio to define quality on its own. ROA captures the level of profitability, accruals capture whether earnings are cash-backed and persistent, and change in ATO captures whether the firm is becoming more operationally efficient. By combining them, FTSE gets a more robust profitability-quality signal and reduces reliance on one potentially noisy measure. The score is rank-based because FTSE is trying to compare companies relative to each other, not estimate some absolute law of what counts as “good enough.”

**Interpretation**

- Higher score means better profitability quality
- Rankings are relative, not absolute

---

## 18. Composite Quality Score

**Purpose**  
Combines profitability quality with leverage quality.

**Formula**

\[
Composite\ Quality\ Score = \frac{Composite\ Profitability\ Score + Leverage\ Score}{2}
\]

**Terms**

- \( Composite\ Profitability\ Score \): average of ROA, accruals, and change in ATO ranks
- \( Leverage\ Score \): rank based on industry-relative OPCFD

**Plain-English Explanation**  
This is FTSE's final preferred quality signal for non-financial companies.

**Why FTSE Uses It**  
This is one of the most important outcomes in the paper. FTSE explicitly tests whether the profitability block should be paired with growth or with leverage. The paper finds that growth is more correlated with profitability and adds less incremental benefit, while leverage is more independent and improves the composite more meaningfully. That is why the final quality definition becomes `profitability + leverage`, not `profitability + growth`. This formula is therefore the point where the research evidence gets turned into the final signal design.

**Interpretation**

- Higher score indicates stronger overall quality
- This is the central composite for the final index design

---

## 19. Factor Exposure

**Purpose**  
Measures how much total quality exposure the index has.

**Formula**

\[
Factor\ Exposure = \sum_{i=1}^{N} w_i z_i
\]

**Terms**

- \( w_i \): portfolio weight of stock \(i\)
- \( z_i \): factor z-score of stock \(i\)
- \( N \): number of stocks

**Plain-English Explanation**  
This is the weighted sum of stock-level factor scores across the portfolio.

**Why FTSE Uses It**  
Once FTSE moves from factor research into index construction, it needs to measure whether the final portfolio actually expresses the quality factor. A set of good stock scores is not enough; the weights matter. Factor exposure is the portfolio-level check that shows whether the broad or narrow index is meaningfully tilted toward quality. It is also what allows FTSE to compare how much extra quality exposure is gained when moving from a broad index to a narrower one.

**Interpretation**

- Higher positive values indicate stronger quality tilt
- A cap-weighted benchmark should have much less intentional factor exposure

---

## 20. Factor Contribution

**Purpose**  
Measures how much each stock contributes to total portfolio factor exposure.

**Formula**

\[
Factor\ Contribution_i = Benchmark\ Weight_i \times Z\text{-}Score_i
\]

**Terms**

- \( Factor\ Contribution_i \): contribution of stock \(i\) to factor exposure
- \( Benchmark\ Weight_i \): weight of stock \(i\) in the broad underlying index
- \( Z\text{-}Score_i \): normalized quality score of stock \(i\)

**Plain-English Explanation**  
This shows whether a stock meaningfully helps the index express the quality factor.

**Why FTSE Uses It**  
FTSE uses this in the narrowing step. A broad factor index still contains every stock in the benchmark, so some stocks barely help the factor exposure at all. Factor contribution gives FTSE a disciplined way to identify which names add the least to the quality tilt. Those names are removed first when constructing the narrow version. In other words, this metric is the mechanism that turns “keep the whole benchmark and tilt it” into “keep only the names that matter most for factor expression.”

---

## 21. Effective Number of Stocks

**Purpose**  
Measures the breadth or diversification of the portfolio.

**Formula**

\[
Effective\ N = \frac{1}{\sum_{i=1}^{N} w_i^2}
\]

**Terms**

- \( w_i \): portfolio weight of stock \(i\)
- \( N \): number of stocks

**Plain-English Explanation**  
This converts the weight distribution into the number of equally weighted stocks that would provide the same concentration level.

**Why FTSE Uses It**  
FTSE is trying to balance two competing goals: stronger quality exposure and acceptable diversification. Effective N is the paper’s main way of quantifying that tradeoff. Without a measure like this, FTSE could always improve factor purity by concentrating harder, but that would move the index away from being broadly investable. Effective N lets FTSE set an explicit diversification target when creating the narrow index.

**Interpretation**

- Higher Effective N means more diversification
- Lower Effective N means more concentration

---

## 22. Weighted Capacity Ratio (WCR)

**Purpose**  
Measures how investable the factor index is relative to the cap-weighted benchmark.

**Formula**

\[
WCR = \sum_{i=1}^{N} \frac{\hat{w}_i^2}{w_i}
\]

**Terms**

- \( \hat{w}_i \): weight of stock \(i\) in the factor index
- \( w_i \): weight of stock \(i\) in the cap-weighted benchmark
- \( N \): number of stocks

**Plain-English Explanation**  
This compares the factor portfolio's weight distribution to the benchmark's distribution in a way that highlights potential capacity stress.

**Why FTSE Uses It**  
FTSE is not building a paper-only ranking model. It is building something meant to function like a real index. That means it cares about whether the resulting weights imply capacity problems, especially if the factor tilt pushes too much weight into smaller or less benchmark-representative names. WCR is a practical implementation metric: it tells FTSE how far the portfolio has drifted from the capacity profile of the benchmark. This is why WCR sits alongside exposure and diversification in the paper. FTSE is explicitly showing that a factor index must be judged on implementability, not just backtest return.

**Interpretation**

- Lower WCR implies better capacity
- WCR near 1 means capacity similar to the benchmark
- Higher WCR implies more concentration relative to the benchmark and potentially lower capacity

---

## 23. Broad-to-Narrow Index Rule

**Purpose**  
Improves factor purity while preserving diversification.

**Rule**

FTSE starts with a broad quality index, calculates each stock's factor contribution, removes stocks with the smallest contribution, and repeats this until the narrow index reaches a diversification target equal to about 70% of the broad index's Effective N.

**Why FTSE Uses It**  
This rule is FTSE’s practical compromise between two extremes. At one extreme is the broad factor index, which is diversified and investable but not especially pure. At the other extreme is a very concentrated factor portfolio, which may have stronger exposure but worse turnover, diversification, and capacity. The broad-to-narrow rule lets FTSE move partway toward higher factor purity in a systematic way. It is therefore one of the main engineering choices in the paper, not just a cosmetic adjustment.

**Interpretation**

- Broad index: more diversified, lower exposure, lower turnover
- Narrow index: higher exposure, more concentration, higher turnover

---

## 24. Financials-Specific Adjustment

**Purpose**  
Adapts the quality framework for banks, insurers, and other financial firms.

**Rule**

For financials, FTSE does not use the usual accrual and leverage framework. Instead, it relies on:

\[
Composite\ Financials\ Quality = \frac{Rank(ROA) + Rank(ROA\text{-}GARP)}{2}
\]

**Why FTSE Uses It**  
FTSE treats financials separately because many of the standard non-financial quality signals do not transfer cleanly. Debt, working capital, operating cash flow, and capex mean different things for banks and insurers than they do for industrial businesses. If FTSE applied the same non-financial formulas to financials, the resulting ranks could be misleading rather than informative. So this adjustment is not a minor detail; it reflects FTSE’s view that factor design has to respect sector-specific accounting structures.

**Interpretation**

- Financials are treated as a special case
- This is important if you reuse the framework in your own factor-index design

---

## Key Takeaways from the Formulas

- FTSE's quality framework is mostly built from `ROA`, `Delta ATO`, `accruals`, and `OPCFD`
- The paper concludes that `profitability + leverage` is stronger than `profitability + growth`
- The final index methodology is not just factor research; it adds `z-scores`, `portfolio weights`, `factor exposure`, `capacity`, and `diversification` controls
- Lower accruals and lower leverage are generally interpreted as higher quality
- Financials require separate treatment
