# Iteration Protocol

Each research iteration should update this repository in a way that makes the state recoverable from disk.

## Before Modeling

1. Write the question in `PROGRESS.md`.
2. Identify the benchmark exogenous-preference model.
3. State which axiom changes.
4. Record expected result and failure mode.

## During Modeling

1. Keep mathematical notes in `models/`.
2. Keep executable code in `src/` and `scripts/`.
3. Write generated outputs to `results/`.
4. Avoid manual edits to generated outputs unless explicitly marked.

## After Modeling

1. Summarize what changed in `PROGRESS.md`.
2. Classify results:
   - `artifact`: caused by coding or parameterization;
   - `fragile`: true only in a small parameter region;
   - `robust`: survives broad perturbation;
   - `theorem candidate`: looks analytically provable.
3. Commit with a message that names the model or theorem.

## Article Draft QA

For any article draft intended for the user to read:

1. Prefer HTML with MathJax for formulas when formulas are central.
2. Avoid fragile Unicode math ornamentation in the reader copy.
3. Render the article in a browser or the target reader.
4. Take a screenshot of the rendered page.
5. Inspect the screenshot for formula rendering, line wrapping, and visual
   artifacts before reporting the draft as ready.

## Evidence Standard

Bizarre conclusions are welcome only if:

- the primitive assumptions are visible,
- the mechanism is not hidden in parameter names,
- the exogenous benchmark is shown,
- the result is reproducible,
- the welfare criterion is explicit.
