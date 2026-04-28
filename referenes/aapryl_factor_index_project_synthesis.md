# Aapryl Factor Index Project Synthesis

This note ties the provider documents together around the actual project you were asked to plan. The goal is to keep the main idea of the work clear:

- define the factors
- choose the construction philosophy
- set the rules and constraints
- decide how the portfolios should update over time

It is easy for the source notes to drift into separate provider summaries. This note is meant to keep them connected to the Aapryl assignment.

## 1. What The Project Is Actually Asking

The email is asking for a methodology design, not immediate implementation. The decisions to make are:

- how to define `Deep Value`
- how to define `Quality Value`
- how to define `Quality Growth`
- how to define `Aggressive Growth`
- which parent universes to use:
  - `Russell 1000`
  - `Russell 2000`
  - `MSCI EAFE`
  - `MSCI EM`
- whether the portfolios should be built with:
  - a `multi-factor ranking / simultaneous tilt` approach
  - a `2-step / staged` approach
- how region and sector limits should be set
- how monthly updates should eventually work operationally

The documents you reviewed do **not** answer the whole assignment directly. They provide examples of how major providers solve different parts of the problem.

## 2. What Each Document Contributes

### FTSE Quality Factor Paper

Best use:
- defining the `quality` sleeve economically and empirically

Most important contributions:
- defines quality as durable future cash-flow generation
- tests `ROA`, `change in asset turnover`, `accruals`, `ROA growth / GARP`, and `OPCFD`
- concludes `profitability + leverage` is better than `profitability + growth`
- shows the evidence for that conclusion:
  - profitability-growth rank correlation is about `45%-50%`
  - profitability-leverage rank correlation is about `31%-36%`
  - growth adds little incremental Sharpe-ratio improvement
- shows the implementation trade-off:
  - research quintiles had turnover above `100%` at the high-quality end
  - broad practical quality indexes cut turnover to about `27%-37%`
  - narrow quality indexes raise exposure further at about `37%-61%` turnover

Why it matters for Aapryl:
- strongest document for the `quality` sleeve
- strongest research support for `composite ranking` inside quality itself

### Morningstar Global Factor Rulebook

Best use:
- learning how a provider operationalizes a factor into a live portfolio

Most important contributions:
- benchmark-relative parent universe design
- ranking by standardized factor exposure
- select until `30%` of parent float-adjusted market cap
- buffering:
  - top `20%` guaranteed
  - `20%-40%` zone gets retention preference
- factor-tilted benchmark weights
- optimizer minimizes deviation from target weights
- explicit stock, sector, and region constraints
- region/sector bands start at `+/- 2%` for quality/value/size/yield and can widen if needed

Why it matters for Aapryl:
- strongest document for `implementation mechanics`
- good template for buffering, optimization, and benchmark-relative constraint design

### MSCI Quality Methodology

Best use:
- learning how a provider builds a `pure quality` index with a clean selection-and-weighting framework

Most important contributions:
- quality defined as:
  - high `ROE`
  - low `Debt / Equity`
  - stable earnings
- `ROE` and `D/E` are mandatory as of the May 2025 update
- fixed-count constituent selection
- `20%` buffer around the target constituent count
- benchmark-relative weighting:
  - `Quality Score x Parent Weight`
- useful variants:
  - `Quality Tilt`
  - `Sector Neutral Quality`

Why it matters for Aapryl:
- strong template for a `quality` sleeve
- useful if you want to compare `selection + weighting` against `full-universe tilt`

### Fidelity Global Quality Value Methodology

Best use:
- understanding how a real provider constructs a blended `Quality Value` index

Most important contributions:
- one of the closest direct templates for `Quality Value`
- selection is done within `country+sector groups`
- `banks` are treated differently from non-banks
- bottom `5%` momentum names are removed before scoring
- staged logic:
  1. build `Quality`
  2. combine `Quality + ESG`
  3. eliminate negative `Quality + ESG` names
  4. rank survivors on `Value`
  5. adjust value with `Size`
- uses a target of roughly `250` stocks
- preserves neutrality structurally by assigning stock counts by country+sector group
- operational model is:
  - annual full reconstitution
  - lighter conditional monthly maintenance
- heavily dependent on `FactSet + MSCI` field mapping

Why it matters for Aapryl:
- strongest document for `Quality Value`
- strongest real-world evidence for the `2-step / staged` side of the construction debate

### FTSE Global Factor Ground Rules

Best use:
- understanding simultaneous multi-factor tilt architecture and production rules

Most important contributions:
- uses multiplicative benchmark-relative tilts, not simple top-bucket selection
- explicit z-score standardization and truncation
- explicit missing-data rules
- country and industry bands
- capacity, max-weight, min-weight, and turnover controls
- two architecture types:
  - `Fixed Tilt`
  - `Target Exposure`
- target-exposure methodology has a real feasibility ladder:
  - iterate
  - reduce exposure targets by `2.5%`
  - then relax turnover
  - then continue relaxing if needed
- narrow indexes use explicit exposure, capacity, and `Effective N` conditions
- includes direct `Russell 1000` and `Russell 2000` examples, including:
  - `Russell 1000 2Qual/Val 5% Capped Factor Index`
  - `Russell 1000 Quality Factor Index`
  - `Russell 2000 Quality Factor Index`
  - `Russell 2000 0.4 Target Exposure Quality Factor Index`

Why it matters for Aapryl:
- strongest document for the `simultaneous tilt / multi-factor ranking` side of the debate
- strongest document for Russell-specific implementation thinking

## 3. What The Document Set Says About Ranking vs 2-Step

This is one of the main project questions, and the documents do **not** all point the same way.

Evidence for `composite ranking / simultaneous tilt`:
- FTSE Quality paper:
  - composite profitability score
  - composite quality score
  - benchmark-relative tilt implementation
- MSCI Quality:
  - descriptor z-scores averaged into one quality score
  - rank, select, then weight by score x benchmark weight
- Morningstar:
  - factor-score ranking
  - factor-tilted benchmark weights
  - optimization under constraints
- FTSE Ground Rules:
  - strongest provider example of simultaneous constrained tilting

Evidence for `2-step / staged`:
- Fidelity Global Quality Value:
  - `Quality + ESG` gate first
  - `Value` ranking second
  - `Size` adjustment after value

The practical conclusion is:

- `Fidelity` is your best institutional example of a staged `Quality Value` process
- `FTSE Ground Rules` is your best institutional example of simultaneous multi-factor tilting

That means your manager's question is real. Major providers genuinely use different construction philosophies.

## 4. What The Documents Collectively Imply About Good Index Design

Across the set, the providers repeatedly converge on the same implementation ideas:

- start from a `benchmark parent universe`
- standardize factor signals with `z-scores` or rank-based measures
- normalize relative to sensible peer groups:
  - region
  - industry
  - sector
  - country+sector
- treat `financials` or `banks` separately where needed
- avoid pure top-bucket equal weighting
- keep the portfolio investable through:
  - benchmark-relative weights
  - stock caps
  - sector and region controls
  - buffering
  - turnover limits
  - capacity controls
- separate `major reconstitution logic` from `interim maintenance logic`

Those are not one provider's quirks. They are the common design language of the document set.

## 5. What None Of The Documents Solve

These are still open project decisions:

- the factor definition for `Deep Value`
- the factor definition for `Aggressive Growth`
- the final Aapryl definition of `Quality Growth`
- whether active-manager exposures should set:
  - region limits
  - sector limits
- whether Aapryl should prefer:
  - staged selection
  - simultaneous tilt
  - a hybrid of the two
- how to translate the methodology into a repeatable `FactSet` workflow
- how the portfolios should update `monthly` in production

That last point matters. The documents show several operational models:

- annual rebalance
- semiannual rebalance
- annual rebuild plus lighter monthly maintenance
- phased review structures

But none of them directly answers the exact monthly operating model your team wants.

## 6. Best Working Interpretation For The Project

If you reduce the document set to the most useful planning message, it is this:

1. Build each index from a benchmark parent universe.
2. Define each factor sleeve with clear accounting or market-based signals.
3. Decide whether the combined strategy should be:
   - staged, like Fidelity
   - simultaneous, like FTSE
   - or hybrid
4. Keep country and sector risk under explicit control.
5. Use buffering, turnover limits, and caps so the result is implementable.
6. Treat monthly updating as an operational design choice, not as a given rebalance frequency.

## 7. What Seems Most Useful By Index Type

- `Quality Value`
  - most direct template: `Fidelity`
  - best simultaneous-tilt counterexample: `FTSE Ground Rules`

- `Quality Growth`
  - strongest quality sleeve references: `FTSE Quality` and `MSCI Quality`
  - strongest operational implementation reference: `MSCI` or `Morningstar`

- `Deep Value`
  - strongest value-construction mechanics: `Morningstar` and `FTSE Ground Rules`
  - still needs fresh design work; none of the provided docs is a direct Deep Value template

- `Aggressive Growth`
  - least directly covered by the provided set
  - will likely require the most original design work

## 8. Bottom Line

The research set is not telling you to copy one provider. It is giving you a menu of design philosophies:

- `FTSE Quality`:
  how to define quality well
- `Morningstar`:
  how to operationalize factor portfolios with optimization and constraints
- `MSCI`:
  how to build a clean provider-style quality index
- `Fidelity`:
  how to build a realistic staged `Quality Value` index
- `FTSE Ground Rules`:
  how to build simultaneous benchmark-relative multi-factor tilt portfolios, especially in Russell universes

The real project is to choose which of those ideas should drive Aapryl's own methodology.
