# Aapryl Factor Research Orchestration

This repo contains a repo-local Codex agent system for the Aapryl factor-index project.

## Core Objective

Translate the manager email into a full `research -> design -> implementation` program for:

- `Deep Value`
- `Quality Value`
- `Quality Growth`
- `Aggressive Growth`

Each style must be implemented as a benchmark-relative methodology for:

- `Russell 1000`
- `Russell 2000`
- `MSCI EAFE`
- `MSCI EM`

The system is optimized for:

- factor definition and signal design
- active-manager-informed sector and region limits
- `weighted rank` versus `2-step screen-then-rank`
- provider-style rulebook design
- `FactSet` implementation planning
- monthly automation readiness

## Default Evidence Policy

- Default evidence policy is `MCP-only`.
- Before any substantive research, call `get_xponance_research_index_status()`.
- Treat `C:\Users\bryan\OneDrive\Desktop\xponance_research\knowledge_base` as the intended default knowledge base unless the user explicitly names a different corpus.
- Do not use general knowledge or direct file reads as evidence when the evidence policy is `MCP-only`.
- Distinguish `evidence` from `inference` in every artifact.
- Use one confidence tag for every conclusion or recommendation:
  - `evidence-backed`
  - `directionally supported`
  - `requires FactSet test`
  - `unsupported by current MCP corpus`

## Hard Evidence Gate

Under `MCP-only`, research must stop and return a `corpus_mismatch` result when any of these are true:

- active `data_dir` does not match the intended knowledge base
- `sources_available_locally` does not match `last_synced_documents`
- the user named a source path that is not present in the active MCP corpus
- the MCP is unavailable or does not expose the required corpus state

The correct output in that case is `.agents/templates/corpus-gate-report.md`, not a partial research answer.

## Coordinator Contract

The coordinator must run this fixed preflight:

1. `corpus check`
2. `task classification`
3. `workstream routing`
4. `artifact collection`
5. `synthesis`

The coordinator must decompose every substantive project request into two layers:

- `style archetype` work: define `Deep Value`, `Quality Value`, `Quality Growth`, and `Aggressive Growth` once
- `benchmark overlay` work: adapt those styles to `Russell 1000`, `Russell 2000`, `MSCI EAFE`, and `MSCI EM`

The default end-to-end workflow is:

1. validate corpus
2. extract a project question map
3. define style archetypes
4. extract provider and academic evidence
5. build an active-manager calibration plan
6. compare construction methods
7. draft benchmark overlays
8. draft a FactSet and monthly implementation plan
9. produce a manager-ready memo

The default final package is:

- one `decision memo`
- one `evidence appendix`
- one `construction comparison plan`
- one `active-manager calibration plan`
- one `rulebook outline`
- one `FactSet implementation spec`

## Agent Registry

Load `.agents/roles/coordinator.md` first for multi-step project work, then only the relevant specialist roles:

- `.agents/roles/corpus-auditor.md`
- `.agents/roles/literature-reviewer.md`
- `.agents/roles/manager-exposure-analyst.md`
- `.agents/roles/portfolio-construction-analyst.md`
- `.agents/roles/index-methodology-designer.md`
- `.agents/roles/implementation-planner.md`
- `.agents/roles/memo-writer.md`

Use the templates below as artifact contracts:

- `.agents/templates/question-map.md`
- `.agents/templates/corpus-gate-report.md`
- `.agents/templates/paper-extraction-sheet.md`
- `.agents/templates/evidence-appendix-outline.md`
- `.agents/templates/active-manager-calibration-plan.md`
- `.agents/templates/rank-vs-two-step-test-plan.md`
- `.agents/templates/index-rulebook-outline.md`
- `.agents/templates/factset-implementation-spec.md`
- `.agents/templates/manager-memo-outline.md`

## Working Rules

- Prefer primary sources: provider rulebooks, methodology notes, white papers, and academic papers.
- Do not let methodology recommendations outrun the evidence.
- Do not treat `integrated vs mixed sleeves` as identical to `rank vs 2-step`.
- For active-manager questions, separate `what literature suggests` from `what FactSet holdings analysis must confirm`.
- For methodology design, prefer explicit rules, formulas, and decision logic over vague prose.
