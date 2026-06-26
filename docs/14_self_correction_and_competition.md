# Self-Correction And Competition Revision

## Reason For The Pivot

The previous material-capacity model showed self-correction, traps, and
collapse-prone dynamics, but it risked sounding like advice: build capacity,
avoid sinks, design bridges. The user clarified that the paper should analyze
objective reality and consequences, not give guidance.

This revision therefore asks a sharper question:

```text
Does an automatic corrective mechanism emerge from the model itself?
```

## Main Findings

### Current-drift signals do not generally correct traps

Add a signal of current material improvement or deterioration to the fast
subjective payoff:

```text
p_chi(K) = logistic(beta * (q + z - rho K + chi * Phi_chi(K)))
Phi_chi(K) = alpha + r K^2(1 - K) - d K - L p_chi(K)
```

At any steady state `Phi_chi(K) = 0`, so the current-drift signal is zero at the
very point where it would need to remove the trap. The roots of the scalar
capacity equation are invariant to this signal. In the baseline calibration,
the maximum numerical root displacement was about `1.19e-10`.

Interpretation: discomfort, warning, regret, or current pain can change speeds
and slopes, but is not enough by itself to remove a stable low-capacity state.

### Persistent stock feedback can correct the system

If material capacity itself changes the payoff map, the root pattern can change.
In the baseline trap calibration, raising the capacity-protection channel `rho`
removes the low trap at about `rho = 3.10` on the grid used by the audit.

Interpretation: in this diagnostic, the tested current-drift signal does not
correct the trap; the displayed capacity-protection channel can. Other vector-field
changes, such as lower exposure, lower damage, or higher repair, can also remove
the low root in other diagnostics.

### Competition selects rules under the operative metric

Competition is modeled as:

```text
sdot_l = omega * s_l * (S_l - sum_r s_r S_r)
Ndot = N * sum_r s_r g_r
```

Here `S_l` is the competitive score that changes relative prevalence, while
`g_l` is the material growth rate. This separates relative competition from
absolute survival.

In the two-rule audit:

- Under material-viability competition, the capacity-preserving bridge expands
  to share `0.999` at `omega = 1.2`, and population mass rises to `5.734`.
- Under engagement-proxy competition, the high-engagement sink expands to share
  effectively `1.000`, while population mass falls to `0.020`.

Interpretation: Darwinian competition is not automatically a truth machine. It
selects whatever competitive score governs reproduction, capital, attention,
users, or institutional prevalence. Absolute survival depends on material
growth, which may differ from the competitive score.

## Article Consequence

The paper should now lead with this result:

```text
Fast endogenous preferences can be objectively disciplined, but only by a
persistent material-state channel or by competition under a competitive score
aligned with material growth. Current deterioration signals alone do not remove
bad steady states, and competition over proxies can select the sink.
```

This is stronger than the previous bridge/sink discussion because it says when
correction exists, when it fails, and why Nash and Darwinian competition matter.
