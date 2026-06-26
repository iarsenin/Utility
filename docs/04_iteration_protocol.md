# Iteration Protocol

Each research iteration should leave the repository recoverable from disk.
Active memory should be concise and durable; detailed logs belong in
`docs/archive/`.

## Before Modeling

1. State the question in `PROGRESS.md`.
2. Identify the benchmark model or existing result.
3. Name the primitives that change.
4. State the expected result and failure mode.

## During Modeling

1. Keep mathematical notes in `models/`.
2. Keep executable code in `src/` and `scripts/`.
3. Write generated outputs to `results/`.
4. Do not hand-edit generated outputs unless clearly marked.

## After Modeling

1. Update `PROGRESS.md` with the durable result, not a diary.
2. Classify the result:
   - `artifact`: caused by code or parameterization;
   - `fragile`: true only in a small parameter region;
   - `robust`: survives broad perturbation;
   - `theorem candidate`: analytically provable with clear assumptions;
   - `empirical hypothesis`: needs data and identification.
3. Update the active plan if the result changes the paper's direction.
4. Archive detailed agent/editorial notes under `docs/archive/`.

## Article Draft QA

For any article draft intended for reading:

1. Generate the article from source.
2. Open it in the target browser or reader.
3. Take a screenshot.
4. Inspect the screenshot for formula rendering, line wrapping, visual
   artifacts, and stale language.
5. Record the screenshot path in `PROGRESS.md` for substantive updates.

## Evidence Standard

Strange conclusions are welcome only when:

- primitive assumptions are explicit;
- the mechanism is visible;
- the benchmark is stated;
- the result is reproducible;
- the welfare or material criterion is named;
- topical examples are treated as tests, not proof.
