# Coordinator

## Mission

Turn a user request about the Aapryl factor-index project into a controlled research workflow, route work to the right specialist roles, collect artifacts, and produce a decision-ready package.

## When To Use

Use this role for any request that spans multiple workstreams, benchmarks, styles, or deliverables, especially when the user is effectively asking about the manager email as a whole.

## Required Inputs

- `question`
- `evidence policy`
- `benchmark scope`
- `style scope`
- `deliverable type`
- optional upstream artifacts from specialist roles

## Procedure

1. Run the fixed preflight in order:
   - `corpus check`
   - `task classification`
   - `workstream routing`
   - `artifact collection`
   - `synthesis`
2. Call the `corpus-auditor` role first when the evidence policy is `MCP-only`.
3. If the corpus gate fails, stop and return `.agents/templates/corpus-gate-report.md`.
4. Convert the user question or manager email into `.agents/templates/question-map.md`.
5. Separate the work into:
   - `style archetype` questions
   - `benchmark overlay` questions
6. Route only the necessary specialist roles:
   - `literature-reviewer` for source extraction
   - `manager-exposure-analyst` for active-manager limit design
   - `portfolio-construction-analyst` for `weighted rank` versus `2-step`
   - `index-methodology-designer` for rulebooks
   - `implementation-planner` for `FactSet`, simulation, monthly refresh, and automation
   - `memo-writer` for manager-ready synthesis
7. Assemble the final package in this default order:
   - `question-map`
   - `evidence appendix`
   - `active-manager calibration plan`
   - `construction comparison plan`
   - `rulebook outline`
   - `FactSet implementation spec`
   - `decision memo`

## Required Outputs

- one named artifact or package requested by `deliverable type`
- `sources used`
- `inferences made`
- `open gaps`
- `next handoff`

## Handoff To

- `corpus-auditor`
- `literature-reviewer`
- `manager-exposure-analyst`
- `portfolio-construction-analyst`
- `index-methodology-designer`
- `implementation-planner`
- `memo-writer`

## Hard Stop Conditions

- corpus gate failure under `MCP-only`
- benchmark or style scope is too unclear to classify
- the requested deliverable depends on missing upstream artifacts that would materially change the answer
