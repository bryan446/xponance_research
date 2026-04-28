Yes — here is the cleaned version with the **paper names directly next to each topic**.

* **Foundation**

  * *A Five-Factor Asset Pricing Model* — Eugene F. Fama, Kenneth R. French
  * *International Tests of a Five-Factor Asset Pricing Model* — Eugene F. Fama, Kenneth R. French
    These are the base papers for value, profitability (ability to earn profits on assets/capital), and investment. ([SSRN][1])

* **Deep Value**

  * *Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers* — Joseph D. Piotroski
  * *In Search of Distress Risk* — John Y. Campbell, Jens Hilscher, Jan Szilagyi
    This is the “cheap first,
    
     then avoid junk/distress” literature. ([SSRN][2])

* **Quality Value**

  * *Quality Minus Junk* — Clifford S. Asness, Andrea Frazzini, Lasse H. Pedersen
  * *The Other Side of Value: Good Growth and the Gross Profitability Premium* — Robert Novy-Marx
  * *Fundamental Analysis: Combining the Search for Quality with the Search for Value* — Kevin K. Li, Partha S. Mohanram
  * *Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers* — Joseph D. Piotroski
    This is the strongest stack for “quality screen/floor + value selection.” ([SSRN][3])

* **Quality Growth**

  * *Quality Minus Junk* — Clifford S. Asness, Andrea Frazzini, Lasse H. Pedersen
  * *The Other Side of Value: Good Growth and the Gross Profitability Premium* — Robert Novy-Marx
  * *Separating Winners from Losers Among Low Book-to-Market Stocks Using Financial Statement Analysis* — Partha S. Mohanram
    This is the best literature for “quality first, then credible growth,” not hype growth. ([SSRN][3])

* **Aggressive Growth**

  * *Separating Winners from Losers Among Low Book-to-Market Stocks Using Financial Statement Analysis* — Partha S. Mohanram
  * *Momentum* — Narasimhan Jegadeesh, Sheridan Titman
  * *Profitability of Momentum Strategies: An Evaluation of Alternative Explanations* — Narasimhan Jegadeesh, Sheridan Titman
    This sleeve is the weakest academically. The literature supports growth + momentum more than raw “aggressive growth” as a clean standalone factor. ([SSRN][4])

* **Sector / region limits**

  * *Is Sector-neutrality in Factor Investing a Mistake?* — Sina Ehsani, Campbell R. Harvey, Feifei Li
  * *How Active is Your Fund Manager? A New Measure That Predicts Performance* — Martijn Cremers, Antti Petajisto
    These are the papers for sector neutrality (removing sector bets) and Active Share (how different holdings are from the benchmark). ([SSRN][5])

* **Portfolio construction: weighted rank vs integrated approach**

  * *Risk Management and the Optimal Combination of Equity Market Factors* — Roger G. Clarke, Harindra de Silva, Steven Thorley
  * *Combining Value and Momentum* — Gregg S. Fisher, Ronnie Shah, Sheridan Titman
  * *Long-Only Style Investing: Don’t Just Mix, Integrate* — Shaun Fitzgibbons, Jacques Friedman, Lukasz Pomorski, Laura Serban
    These are the main papers for how to combine factors in a long-only portfolio. ([SSRN][6])

* **Reality check / modern update**

  * *Profitability Retrospective: What Have We Learned?* — Mamdouh Medhat, Robert Novy-Marx
  * *An Intangibles-Adjusted Profitability Factor* — Ravi Jagannathan, Robert A. Korajczyk, Kai Wang
    These matter because newer work argues profitability may subsume much of what gets marketed as “quality,” and that intangibles-adjusted profitability can improve measurement. ([SSRN][7])

If you want the **tightest reading order**, it is:

1. Fama-French
2. Novy-Marx
3. QMJ
4. Piotroski
5. Campbell
6. Mohanram
7. Ehsani
8. Cremers/Petajisto
9. Clarke/de Silva/Thorley ([SSRN][1])

If you want, I can turn this into a **meeting-ready memo** with:
“topic → papers → what each paper implies for your index design.”

[1]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2287202&utm_source=chatgpt.com "A Five-Factor Asset Pricing Model by Eugene F. Fama, Kenneth R. French :: SSRN"
[2]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=249455&utm_source=chatgpt.com "Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers by Joseph D. Piotroski :: SSRN"
[3]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2312432&utm_source=chatgpt.com "Quality Minus Junk by Clifford S. Asness, Andrea Frazzini, Lasse Heje Pedersen :: SSRN"
[4]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=403180&utm_source=chatgpt.com "Separating Winners from Losers Among Low Book-to-Market Stocks Using Financial Statement Analysis by Partha S. Mohanram :: SSRN"
[5]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3959116&utm_source=chatgpt.com "Is Sector-neutrality in Factor Investing a Mistake? by Sina Ehsani, Campbell R. Harvey, Feifei Li :: SSRN"
[6]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3486035&utm_source=chatgpt.com "Risk Management and the Optimal Combination of Equity Market Factors by Roger G Clarke, Harindra de Silva, Steven Thorley :: SSRN"
[7]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5190788&utm_source=chatgpt.com "Profitability Retrospective: What Have We Learned? by Robert Novy-Marx, Mamdouh Medhat :: SSRN"

He is asking you to define the **methodology** (the rulebook) for a new family of factor indices.

In plain English, he wants you to do this:

1. Read the attached papers and learn how existing providers build **factor indices** (rule-based stock portfolios built around traits like value or quality).

2. Design 4 new indices:

   * Deep Value
   * Quality Value
   * Quality Growth
   * Aggressive Growth

3. Build them for 4 **benchmark** universes (reference market indexes):

   * Russell 1000
   * Russell 2000
   * MSCI EAFE
   * MSCI EM

4. Decide the exact **factors** (stock traits/signals) each index should use.
   Example: value, profitability, leverage, growth, revisions, momentum.

5. Decide the **model rules** (how the portfolio is built):

   * who is eligible
   * how stocks are scored
   * how many names to hold
   * how to weight them
   * sector/region limits
   * rebalance schedule
   * turnover controls (limits on how much the portfolio changes)

6. Compare two portfolio construction methods:

   * **multi-factor ranking** (one combined score from several traits)
   * **2-step approach** (screen first, then rank what survives)

7. Figure out which of those two methods better matches **active managers** (stock pickers trying to beat the market), especially for sector and region behavior.

8. Use actual active-manager holdings/exposures to set sector and region limits, instead of copying generic index-provider constraints.

9. Help define how these portfolios will update monthly and later be automated in Aapryl.

So the real deliverable is not “read the papers.”
It is:

**Design the factor definitions + portfolio construction framework + recommendation on ranking vs 2-step + active-manager-based constraint design.**

He is basically saying:

“Your first job is to architect these four indices properly.”

_________________________________________________________________

Yes. But if you want one paper that solves all of it, that does not exist.

The best papers for **your exact problem** are these:

1. **Multi-factor ranking vs integrated construction**

   * **Fisher, Shah, Titman — *Combining Value and Momentum***. Best pro-integration paper in long-only portfolios; it argues that combining signals simultaneously beats combining standalone sleeves, mainly because it uses bad information better and lowers trading costs. ([SSRN][1])
   * **Fitzgibbons, Friedman, Pomorski, Serban — *Long-Only Style Investing: Don’t Just Mix, Integrate***. Strong practitioner-academic case for integrating factors at the stock level instead of mixing separate factor portfolios. ([SSRN][2])
   * **Leippold, Rüegg — *The Mixed vs the Integrated Approach to Style Investing: Much Ado About Nothing?***. Direct pushback; they do **not** find robust evidence that integrated always wins. ([SSRN][3])
   * **Blitz, Vidojevic — *The Characteristics of Factor Investing***. Important reality check: a lot of the difference between “integrated” and “mixed” comes from the **characteristics** (actual trait exposures) you end up holding, not from the label itself. ([SSRN][4])

2. **Sector limits and whether to neutralize sectors**

   * **Ehsani, Harvey, Li — *Is Sector-Neutrality in Factor Investing a Mistake?***. This is the key paper for your sector-bounds question. Their result is that **long-only** portfolios usually should **not** fully remove sector bets, while long-short portfolios benefit more from sector neutralization (removing sector bets). ([SSRN][5])

3. **Use real active-manager holdings, not labels**

   * **Cremers, Petajisto — *How Active Is Your Fund Manager? A New Measure That Predicts Performance***. Core paper for **Active Share** (how different a portfolio’s holdings are from its benchmark). This gives you the right language for measuring how “active-manager-like” your sleeve really is. ([SSRN][6])
   * **Cremers — *Active Share and the Three Pillars of Active Management***. Useful extension: Active Share reflects skill, conviction, and opportunity, so it is better than naïvely using fund names like “value” or “growth.” ([SSRN][7])

4. **Sector concentration behavior of real active managers**

   * **Kacperczyk, Sialm, Zheng — *On the Industry Concentration of Actively Managed Equity Mutual Funds***. Very important for you: managers with more industry concentration outperformed on average, which means blindly copying tight index-provider sector caps is not well supported. ([NBER][8])

5. **Region / country behavior of international managers**

   * **Jiao, Karolyi, Ng — *Country Rotation and International Mutual Fund Performance***. Best direct paper for your country/region question. It shows international funds add value by actively changing country allocations. ([SSRN][9])
   * **Broman, Fulkerson — *Variation in the Value of Active Share Across Regions of Investments***. Useful recent paper showing that within-region activeness matters differently across regions; it is stronger in Europe and Asia-Pacific than in the U.S. ([SSRN][10])

6. **Benchmark-aware implementation**

   * **Clarke, de Silva, Thorley — *Risk Management and the Optimal Combination of Equity Market Factors***. Best paper for building benchmark-anchored pure factor sleeves with an **active-risk target** (risk versus benchmark). ([SSRN][11])
   * **Jorion — *Portfolio Optimization with Tracking-Error Constraints***. Canonical paper for benchmark-relative active optimization under **tracking error** (volatility of return difference versus benchmark) constraints. ([SSRN][12])
   * **Baker, Bradley, Wurgler — *Benchmarks as Limits to Arbitrage***. Important because benchmark constraints shape manager behavior; that is exactly why your sector and country bands should be benchmark-aware. ([SSRN][13])

**My blunt take:**

* For **rank vs 2-step**, the most useful papers are Fisher, Fitzgibbons, Leippold, and Blitz. They will tell you the argument space, but they do **not** settle your exact question. Most of that literature is **integrated vs mixed sleeves**, not literally “hard screen then rank” versus “single composite score.” ([SSRN][1])
* For **matching active managers**, the must-reads are Ehsani, Cremers/Petajisto, Kacperczyk, and Jiao. That is the strongest path to empirical sector and country limits from holdings. ([SSRN][5])
* For **final portfolio construction**, Clarke and Jorion are the implementation papers. ([SSRN][11])

**What this implies for your project**
My inference from this literature is: do **not** ask “which method is best?” in the abstract. Build holdings-based peer sets by benchmark and style, compute Active Share, active sector weights, country weights, and concentration, then test **both** methods under the same turnover and tracking-error budgets. That is the only defensible way to answer your boss’s question. ([SSRN][6])

If you want, I’ll turn this into a tight reading list with:
**paper → why it matters → exactly what to extract for your model.**

[1]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2472936&utm_source=chatgpt.com "Combining Value and Momentum by Gregg S. Fisher, Ronnie Shah, Sheridan Titman :: SSRN"
[2]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2802849&utm_source=chatgpt.com "Long-Only Style Investing: Don't Just Mix, Integrate by Shaun Fitzgibbons, Jacques Friedman, Lukasz Pomorski, Laura Serban :: SSRN"
[3]: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3018057_code156365.pdf?abstractid=2887117&utm_source=chatgpt.com "The Mixed vs the Integrated Approach to Style Investing: Much Ado About Nothing? by Markus Leippold, Roger Rüegg :: SSRN"
[4]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3206798&utm_source=chatgpt.com "The Characteristics of Factor Investing by David Blitz, Milan Vidojevic :: SSRN"
[5]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3959116&utm_source=chatgpt.com "Is Sector-neutrality in Factor Investing a Mistake? by Sina Ehsani, Campbell R. Harvey, Feifei Li :: SSRN"
[6]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=891719&utm_source=chatgpt.com "How Active is Your Fund Manager? A New Measure That Predicts Performance by Martijn Cremers, Antti Petajisto :: SSRN"
[7]: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2891072_code254417.pdf?abstractid=2860356&mirid=1&utm_source=chatgpt.com "Active Share and the Three Pillars of Active Management: Skill, Conviction and Opportunity by Martijn Cremers :: SSRN"
[8]: https://www.nber.org/papers/w10770?utm_source=chatgpt.com "On the Industry Concentration of Actively Managed Equity Mutual Funds | NBER"
[9]: https://papers.ssrn.com/sol3/Delivery.cfm/4052003.pdf?abstractid=4052003&mirid=1&utm_source=chatgpt.com "<p><span>Country Rotation and International Mutual Fund Performance</span><b><span></span></b></p> by Wei Jiao, George Andrew Karolyi, David T. Ng :: SSRN"
[10]: https://papers.ssrn.com/sol3/Delivery.cfm/4799404.pdf?abstractid=4799404&utm_source=chatgpt.com "Variation in the Value of Active Share Across Regions of Investments: Evidence from Global Equity Funds by Markus S. Broman, Jon A. Fulkerson :: SSRN"
[11]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3486035&utm_source=chatgpt.com "Risk Management and the Optimal Combination of Equity Market Factors by Roger G Clarke, Harindra de Silva, Steven Thorley :: SSRN"
[12]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=490804&utm_source=chatgpt.com "Portfolio Optimization with Tracking-Error Constraints by Philippe Jorion :: SSRN"
[13]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585031&utm_source=chatgpt.com "Benchmarks as Limits to Arbitrage: Understanding the Low Volatility Anomaly by Malcolm P. Baker, Brendan Bradley, Jeffrey Wurgler :: SSRN"



Yes. Here is the **tight reading list** for the exact question in his email.

First, the key caveat:

You are wrong if you treat this literature as a direct proof of **weighted rank vs 2-step screen-then-rank**. Most of it studies **integrated** construction (one stock-level combined score) versus **mixed** construction (blend separate sleeves). That is close to your problem, not identical. Use it as guidance, then test both methods on your data. ([SSRN][1])

## 1) Papers for multi-factor ranking vs 2-step

**1. Gregg Fisher, Ronnie Shah, Sheridan Titman — *Combining Value and Momentum***
Why it matters: strongest clean argument for **integrated** long-only construction. They find simultaneous construction beats mixing separate value and momentum portfolios, mainly because it lowers transaction costs and uses negative signals better.
What to extract:

* whether your composite score should **penalize bad exposures**, not just reward good ones
* how to combine **fast** signals like momentum with **slow** signals like value
* how much of the edge comes from **turnover** (portfolio trading) and cost control, not raw signal math alone. ([SSRN][1])

**2. Shaun Fitzgibbons, Jacques Friedman, Lukasz Pomorski, Laura Serban — *Long-Only Style Investing: Don’t Just Mix, Integrate***
Why it matters: practitioner-heavy but directly on point. They argue integrated portfolios improve return and **information ratio** (return per unit of active risk) by avoiding stocks with offsetting exposures and favoring names with balanced positive exposures.
What to extract:

* their exact definition of **integrated** vs **mix**
* how they deal with **offsetting exposures**
* how much the result depends on long-only implementation, not theory. ([SSRN][2])

**3. Markus Leippold, Roger Rüegg — *The Mixed vs the Integrated Approach to Style Investing: Much Ado About Nothing?***
Why it matters: this is the best pushback paper. They do **not** find robust evidence that integrated always wins.
What to extract:

* their robustness tests
* what disappears after stronger statistical testing
* whether any “integrated advantage” is actually just another hidden tilt. ([SSRN][3])

**4. David Blitz, Milan Vidojevic — *The Characteristics of Factor Investing***
Why it matters: this paper says the big driver is often the final **characteristics** (actual exposures/traits held), not the label “integrated” or “mixed.”
What to extract:

* compare resulting **value, quality, growth, momentum, size, beta** exposures
* compare **holdings overlap**
* compare accidental **low-volatility** spillover
  This is how you should judge your own test: not just return, but what the portfolio actually became. ([SSRN][4])

## 2) Papers for sector and region limits from real active managers

**5. Sina Ehsani, Campbell Harvey, Feifei Li — *Is Sector-Neutrality in Factor Investing a Mistake?***
Why it matters: probably the single most useful paper for your sector-bounds problem. Their result is that **long-only** investors usually should **not** fully neutralize sectors, while long-short investors benefit more from stripping sector bets out.
What to extract:

* do **not** set sector active weights to zero by default
* use **sector bands** (allowed deviations), not full sector neutrality
* test your sleeves both **with** and **without** sector neutralization. ([SSRN][5])

**6. Martijn Cremers, Antti Petajisto — *How Active Is Your Fund Manager? A New Measure That Predicts Performance***
Why it matters: this gives you **Active Share** (how different holdings are from the benchmark), which is the right language for “mirror active managers.”
What to extract:

* compute **Active Share** for each sleeve versus its parent benchmark
* build peer groups using **holdings**, not fund names
* compare your sleeves to active managers on actual **holdings difference**, not marketing labels. ([SSRN][6])

**7. Marcin Kacperczyk, Clemens Sialm, Lu Zheng — *On the Industry Concentration of Actively Managed Equity Mutual Funds***
Why it matters: more industry-concentrated active funds performed better on average after style and risk controls. That means blindly copying very tight sector caps from index providers is weakly justified.
What to extract:

* real managers may need **meaningful sector freedom**
* sector bands should probably be **style-specific**
* measure the distribution of active-manager **sector concentration** before setting your caps. ([NBER][7])

**8. Wei Jiao, Andrew Karolyi, David Ng — *Country Rotation and International Mutual Fund Performance***
Why it matters: international funds add value by actively changing **country allocations**. That is directly relevant for EAFE and EM.
What to extract:

* do **not** assume tight country neutrality is “more realistic”
* calibrate country limits from observed active-manager **country deviations**
* separate **country allocation skill** from stock-picking skill when you backtest. ([SSRN][8])

**9. Markus Broman, Jon Fulkerson — *Variation in the Value of Active Share Across Regions of Investments: Evidence from Global Equity Funds***
Why it matters: useful recent paper, not core canon. It finds within-region Active Share predicts better in Europe and Asia-Pacific than in the U.S.
What to extract:

* do **not** assume one activeness target fits all benchmarks
* Russell 1000/2000 may need different bounds from EAFE/EM
* region-specific calibration may matter. ([SSRN][9])

## 3) Papers for turning this into an optimizer rulebook

**10. Roger Clarke, Harindra de Silva, Steven Thorley — *Risk Management and the Optimal Combination of Equity Market Factors***
Why it matters: best paper here for actual implementation. They argue multi-factor portfolios work better when each sleeve is **pure** (clean exposure), **anchored to the benchmark**, and combined with an **active-risk target** (target risk versus benchmark).
What to extract:

* optimizer objective should be **benchmark-aware**
* each sleeve should stay **pure**, not blurred
* control active risk through time, not just score stocks once. ([SSRN][10])

**11. Philippe Jorion — *Portfolio Optimization with Tracking-Error Constraints***
Why it matters: classic warning paper. A **tracking error** constraint (volatility of return difference versus benchmark) alone can produce inefficient portfolios unless total risk is also controlled.
What to extract:

* do not rely on TE alone
* add total volatility, beta, and concentration controls
* benchmark-relative optimization can go wrong if you ignore total risk. ([SSRN][11])

**12. Malcolm Baker, Brendan Bradley, Jeffrey Wurgler — *Benchmarks as Limits to Arbitrage: Understanding the Low-Volatility Anomaly***
Why it matters: this is the conceptual paper for why benchmark constraints shape manager behavior in the first place.
What to extract:

* judge “matches active managers” **relative to benchmark**
* sector and country limits should be benchmark-aware
* benchmark constraints are part of the product design, not a nuisance. ([SSRN][12])

## Read them in this order

1. Ehsani
2. Cremers/Petajisto
3. Fisher/Shah/Titman
4. Fitzgibbons et al.
5. Leippold/Rüegg
6. Blitz/Vidojevic
7. Kacperczyk/Sialm/Zheng
8. Jiao/Karolyi/Ng
9. Clarke/de Silva/Thorley
10. Jorion

## What to write down from every paper

For each paper, force yourself to extract only these 7 things:

* portfolio type: long-only or long-short
* benchmark used
* stock-level integration or sleeve mix
* sector/country treatment
* turnover/cost treatment
* risk control method
* what part is actually usable for **your** Russell 1000 / Russell 2000 / EAFE / EM problem

The practical takeaway is:

* **Ehsani + Cremers + Kacperczyk + Jiao** tell you how much sector/country freedom real managers plausibly use.
* **Fisher + Fitzgibbons + Leippold + Blitz** tell you how to think about weighted rank vs 2-step, but they do **not** settle it outright.
* **Clarke + Jorion** tell you how to implement the winning design in a benchmark-aware optimizer. ([SSRN][5])

Next, I would turn this into a **paper-by-paper extraction sheet** you can fill in while reading.

[1]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2472936&utm_source=chatgpt.com "Combining Value and Momentum by Gregg S. Fisher, Ronnie Shah, Sheridan Titman :: SSRN"
[2]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2802849&utm_source=chatgpt.com "Long-Only Style Investing: Don't Just Mix, Integrate by Shaun Fitzgibbons, Jacques Friedman, Lukasz Pomorski, Laura Serban :: SSRN"
[3]: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3018057_code156365.pdf?abstractid=2887117&utm_source=chatgpt.com "The Mixed vs the Integrated Approach to Style Investing: Much Ado About Nothing? by Markus Leippold, Roger Rüegg :: SSRN"
[4]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3206798&utm_source=chatgpt.com "The Characteristics of Factor Investing by David Blitz, Milan Vidojevic :: SSRN"
[5]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3959116&utm_source=chatgpt.com "Is Sector-neutrality in Factor Investing a Mistake? by Sina Ehsani, Campbell R. Harvey, Feifei Li :: SSRN"
[6]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=891719&utm_source=chatgpt.com "How Active is Your Fund Manager? A New Measure That Predicts Performance by Martijn Cremers, Antti Petajisto :: SSRN"
[7]: https://www.nber.org/papers/w10770?utm_source=chatgpt.com "On the Industry Concentration of Actively Managed Equity Mutual Funds | NBER"
[8]: https://papers.ssrn.com/sol3/Delivery.cfm/4052003.pdf?abstractid=4052003&mirid=1&utm_source=chatgpt.com "<p><span>Country Rotation and International Mutual Fund Performance</span><b><span></span></b></p> by Wei Jiao, George Andrew Karolyi, David T. Ng :: SSRN"
[9]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4799404&utm_source=chatgpt.com "Variation in the Value of Active Share Across Regions of Investments: Evidence from Global Equity Funds by Markus S. Broman, Jon A. Fulkerson :: SSRN"
[10]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3486035&utm_source=chatgpt.com "Risk Management and the Optimal Combination of Equity Market Factors by Roger G Clarke, Harindra de Silva, Steven Thorley :: SSRN"
[11]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=490804&utm_source=chatgpt.com "Portfolio Optimization with Tracking-Error Constraints by Philippe Jorion :: SSRN"
[12]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585031&utm_source=chatgpt.com "Benchmarks as Limits to Arbitrage: Understanding the Low Volatility Anomaly by Malcolm P. Baker, Brendan Bradley, Jeffrey Wurgler :: SSRN"
