# Round 4 Final Writer Memo

Role: final Writer. Objective: absorb the Editor's conditional-pass notes so the editor is not the final voice in the pass.

## Changes Made

1. Added an explicit bridge before the finite-game tables: the mixed best-response diagnostic is the Proposition 1 diagnostic, while the endpoint check is weaker because it checks only pure opponent actions.

2. Split the finite-game table into two narrower tables:
   - Table 1A reports best-response diagnostics for the neutral and random-strategic routes.
   - Table 1B reports proxy-choice diagnostics for the aligned, independent, and misaligned proxy routes.

3. Shortened table headers to "Mixed BR," "Endpoint BR," "Outcome shift," and "Proxy loss." Splitting the table removed the need for `n/a` cells.

4. Fixed the WDI regression unit mismatch by writing the lagged internet control as \(D_{c,t-1}/100\), consistent with \(D_{c,t}\) being measured in percent and the regression using a 0-1 share.

5. Fixed the Section 7 active-set notation by naming a finite active set \(\mathcal L_0\subseteq\mathcal L\), defining shares over \(\mathcal L_0\), and summing average material payoff over \(k\in\mathcal L_0\).

6. Softened proxy-alignment language from evidentiary language to "computational illustration" language.

7. Replaced the suicide-mortality phrase "directionally favorable" with "opposite the simple harm narrative" so the empirical discussion does not imply a welfare conclusion from a noisy macro proxy.

## Deliberate Non-Changes

I did not edit code or result files. The Modeller's updated diagnostics and generated tables remain as they were.

## Check

Run after editing:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
HTMLParser().feed(open("paper/article_v1.html", encoding="utf-8").read())
print("HTML parser check passed")
PY
```
