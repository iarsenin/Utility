# Round 1 Writer Memo: Article Architecture And Narrative Spine

Date: 2026-06-20

## Objective

Prepare the next article architecture before new empirical work arrives. The
paper should now be organized around the finite-game fast-closure route. The
platform model should become the main application. The one-dimensional taste
model should become exposition and visualization.

The draft should be ambitious in implication but narrow in claim. The paper is
not proving that fast endogenous preferences always cause social collapse. It is
showing that when preferences close on a faster timescale than the rest of the
modeled economy, the objects to which Nash equilibrium, material selection, and
welfare analysis apply are no longer the usual ones.

## Central Contribution Sentence

In finite games with subjective preferences adapting on a vanishing timescale,
fast preference closure replaces utility as a primitive with an induced
preference map, so Nash equilibrium is computed in the fast-adapted subjective
game and material selection acts on the remaining heterogeneous adaptation laws
or institutions; material harm is a conditional result that depends on the
alignment between the preference-generating operator and material welfare.

This sentence is deliberately narrow. It does not claim that preferences are
newly endogenous, that platforms uniquely manipulate people, or that fast
adaptation mechanically lowers welfare.

## Proposed Publication-Ready Structure

### 1. Introduction: The Wrong Clock

Purpose: pose the paper's question in one sharp move. Standard economics can
allow changing preferences as long as preference movement is slow relative to
the allocation problem. The paper studies the opposite limit:

```text
T_P -> 0
```

The introduction should do four things:

- Define the central tension: mechanisms that allocate goods can also produce
  the utility functions used to evaluate those goods.
- State the limiting exercise: preference adaptation is fast, while the speeds
  of behavior, institutions, culture, and population are parameters, not
  assumptions.
- Preview the three object shifts: utility becomes a closure map, Nash moves to
  the induced subjective game, and selection moves to adaptation laws or
  institutions after closure.
- Flag the main caution: the theory predicts object shift generally, not harm
  generally.

Suggested opening example: a recommender system that does not merely infer a
user's utility function but changes the future utility representation on which
future choices are made. Keep it as motivation, then move quickly to the
general finite-game frame.

### 2. Related Work: What This Is Not Claiming

Purpose: reduce novelty risk early. This section should concede the obvious
overlaps before the reader raises them.

Organize the literature around five strands:

- Endogenous preferences, habits, addiction, consumption capital, and cultural
  transmission.
- Indirect evolutionary preferences, where subjective payoffs determine
  behavior and material payoffs determine selection.
- Two-speed dynamics and singular perturbation logic.
- Recommender feedback, engagement optimization, and platform welfare.
- Welfare with adaptive, chosen, meta-, or path-dependent preferences.

The section's payoff should be a contrast:

```text
The paper does not add "preferences move." It adds the singular limit in which
preference movement is the fast variable, then asks what Nash equilibrium,
selection, and welfare act on after that closure.
```

### 3. Finite-Game Environment

Purpose: replace the broad continuous-time notation with the clean theorem
laboratory.

Define:

- finite players `i = 1, ..., n`;
- finite action sets `A_i`;
- material payoffs `Pi_i(a; E, I)`;
- subjective payoffs `U_i(a; P_i, E, I)`;
- preference states `P_i`;
- economic or material state `E`;
- institution, platform rule, or adaptation environment `I`;
- fast preference dynamic or correspondence whose attracting branch is
  `P^star(E, I)`.

Keep the core separation visible:

```text
subjective payoff U_i  -> chosen behavior
material payoff Pi_i   -> growth, survival, or evaluation by selection
adaptation law         -> produces P^star
```

The finite-game version should appear before any scalar taste model. This makes
the paper harder to dismiss as a calibrated parable.

### 4. Fast Preference Closure

Purpose: state the reduction theorem and its economic interpretation.

If the fast preference subsystem has a unique attracting branch, then in the
`T_P -> 0` limit the preference state is not an independent slow state:

```text
P = P^star(E, I).
```

The induced subjective game is:

```text
Gamma^star(E, I) = <A_i, U_i(.; P_i^star(E, I), E, I)>.
```

This is the paper's first technical hinge. The star must be explained every
time it matters: it means "fast attracting branch," not "optimal preference."

### 5. Nash After Closure

Purpose: show that Nash remains a method but moves to a different object.

Define two games:

- the material game with payoffs `Pi_i`;
- the fast-adapted subjective game with payoffs `U_i(.; P_i^star(E, I), E, I)`.

Then state the invariance condition:

```text
BR_U(P^star(E, I), E, I) = BR_Pi(E, I).
```

The reader should leave this section with one crisp sentence:

```text
The fixed-point concept is unchanged; the payoff object has changed.
```

This section should include a small finite-game example or table showing a
material Nash prediction that changes after a non-neutral preference closure.
The example should be illustrative, not the proof.

### 6. Genericity And Neutral Controls

Purpose: make the result non-trivial. This is where the model-selection audit
belongs conceptually.

The section should distinguish:

- strategically irrelevant preference movement, which preserves best responses;
- strategically relevant preference closure, which can alter best responses;
- aligned proxy selection, where material losses are rare or absent by design;
- independent or misaligned proxy selection, where material losses become
  common.

The audit numbers can appear as a compact table or be saved for an appendix,
but the logic should be in the main text. The bad outcome should not be
automatic. The aligned-proxy control is rhetorically important because it makes
the theorem route honest.

### 7. Selection After Closure

Purpose: state the Darwinian or material-selection consequence without turning
the paper into biological reductionism.

The ordinary indirect-evolution chain is:

```text
preference type -> behavior -> material payoff -> type growth
```

The fast-limit chain is:

```text
initial preference -> P^star(E, I) -> behavior -> material payoff
```

If all agents share the same fast adaptation law and a unique attracting branch,
selection over initial preference states is degenerate. Selection can still act
on:

- adaptation laws;
- institutions;
- platform policies;
- resistance or susceptibility parameters;
- populations or systems with different closure maps.

This is one of the paper's most interesting conceptual consequences. It should
be stated as a target shift, not as a claim that selection disappears.

### 8. Platform Control As Main Application

Purpose: apply the theorem spine to the novel institutional setting.

The platform does not merely choose content or exposure. It chooses, constrains,
or optimizes over a preference-transition technology. In reduced form:

```text
I or m -> P_m^star(E) -> NE(U(P_m^star)) -> material outcome
```

The application should focus on proxy alignment:

- If the platform proxy is aligned with material welfare, the harmful result
  weakens.
- If the proxy is independent of material welfare, harm can arise without an
  explicitly anti-material objective.
- If the proxy is misaligned, the survival or material-loss result is strongest.

This section should be the place where recommender systems, engagement, AI
mediation, and policy relevance become vivid. The theory section earns the
right to make those claims; the platform section should not carry the theorem
burden alone.

### 9. Exposition Models

Purpose: give the reader intuition after the general theorem is already in
place.

Use two short examples:

- One-dimensional taste model: shows the phase diagram, fast closure, and
  survival frontier in a transparent scalar case.
- Indirect evolutionary Prisoner's Dilemma: bridges to the preference-evolution
  literature and shows why subjective equilibrium can diverge from material
  Nash.

These models should not be presented as the source of the main theorem. They
are pictures of the mechanism.

### 10. Welfare When Preferences Are Produced

Purpose: isolate the normative consequence without pretending to solve welfare
economics.

The key point is final-preference instability:

```text
produce P_1 -> satisfy P_1 -> cite P_1 as welfare evidence
```

The paper should show that several welfare criteria can disagree:

- initial preferences;
- final preferences;
- meta-preferences over preference change;
- material payoff or survival;
- constitutional constraints on admissible transition laws;
- welfare over the full allocation-preference path.

The defensible claim is non-invariance, not a complete replacement welfare
criterion. Material survival is an evaluation object, not the whole good.

### 11. Timescales And Empirical Implications

Purpose: prevent the singular limit from sounding like an empirical assertion.

The theory sends only `T_P` to zero. It does not assume that algorithms,
institutions, action learning, culture, or populations are slow. Their ratios
should be estimated or varied:

```text
T_algorithm / T_population
T_action / T_population
T_culture / T_population
```

Empirical implications should be phrased as diagnostics:

- estimate latent preference half-lives;
- distinguish within-person preference drift from stable heterogeneity;
- use feed changes, deactivation experiments, or panel designs to separate
  preference change from belief, constraint, and attention changes;
- test whether platform proxies are aligned, independent, or misaligned with
  material welfare measures.

### 12. Limitations

Purpose: make the paper trustworthy.

State the main limits plainly:

- Endogenous preferences are not new.
- The singular limit is an analytical benchmark, not a literal universal claim.
- Fast closure may be multi-attractor, cyclic, or nonunique.
- Material harm requires a misalignment condition.
- Welfare non-invariance does not by itself identify the correct welfare
  criterion.
- Empirical identification is hard because behavior can change for many reasons
  besides preference change.

### 13. Conclusion

Purpose: return to the conceptual payoff.

The conclusion should not end on "platforms are bad." It should end on the
object shift:

```text
When utility adapts on the fastest clock, utility is not the primitive that
closes the model. It is the object closed by the model.
```

Then restate the three consequences: Nash is computed in the induced subjective
game, selection acts on what remains heterogeneous after closure, and welfare
analysis must evaluate preference-transition laws rather than only allocations
under final preferences.

## Propositions And Theorems The Paper Should State

### Definition 1: Fast-Preference Finite Game

A finite game with material payoffs `Pi_i`, subjective payoffs `U_i`, preference
state `P_i`, slow state `(E, I)`, and a fast preference subsystem whose
attracting branch or correspondence determines the reduced subjective game.

This definition should appear before theorems so readers know exactly which
object is being reduced.

### Theorem 1: Fast Preference Closure

If the fast preference subsystem has a unique globally attracting branch
`P^star(E, I)` for each relevant slow state, then as `T_P -> 0` the reduced
game is the subjective finite game induced by `P^star(E, I)`.

Main conclusion:

```text
NE acts on Gamma^star(E, I), not directly on the material game.
```

Use singular-perturbation language only as much as needed. The finite-game
statement can be cleaner than the smooth ODE version.

### Proposition 2: Nash Invariance Condition

The Nash equilibria of the fast-adapted subjective game coincide with the Nash
equilibria of the material-payoff game if the best-response correspondences
coincide:

```text
BR_U(P^star(E, I), E, I) = BR_Pi(E, I).
```

With a suitable equilibrium-selection convention, this condition is also the
right necessary condition for full invariance across games.

### Proposition 3: Generic Best-Response Shift

In finite games, preference closure that changes conditional action rankings is
generically best-response relevant. Strategically irrelevant transformations
preserve the material best-response correspondence; non-neutral transformations
typically do not.

This should be stated carefully. The generic claim should be about finite games
outside lower-dimensional indifference and rank-preserving cases, not about
every possible payoff transformation.

### Theorem 4: Selection Target Shift

If all agents of a selected class share the same fast adaptation law and the
fast subsystem has a unique attracting branch, then initial preference-state
heterogeneity is erased before material selection evaluates realized outcomes.
Selection over preference states is therefore degenerate in the fast limit.

If classes `j` differ in adaptation law, institution, resistance parameter, or
closure map, selection acts on:

```text
j -> P_j^star(E, I) -> NE(U(P_j^star)) -> G_j.
```

This is a central theorem target because it differentiates the paper from the
standard indirect evolutionary route.

### Proposition 5: Platform Proxy Alignment

Let a platform or institution choose an adaptation law by maximizing a proxy
objective. If the proxy ranks adaptation laws exactly as material welfare ranks
them, proxy choice does not create material loss relative to the admissible set.
If the proxy is independent of or misaligned with material welfare, there exist
finite games and admissible laws in which proxy choice selects a materially
inferior closure map.

This should be the formal bridge from the finite-game theorem to the platform
application. The current audit supports the direction but should not be treated
as empirical evidence.

### Proposition 6: One-Dimensional Survival Frontier

In the scalar taste model with fixed exposure `s` and fast closure

```text
p^star(s) = s / (s + alpha),
```

survival occurs if and only if:

```text
g(p^star(s)) >= 0.
```

This proposition belongs after the general theorem as exposition. It should not
be the paper's main proof of the harm claim.

### Proposition 7: Welfare Non-Invariance

For a sufficiently rich preference-state space and admissible transition
technology, there exist paths whose rankings differ under initial preferences,
final preferences, meta-preferences, and material payoff or survival.

Main conclusion:

```text
Final-preference welfare is not invariant when the mechanism being evaluated can
produce the final preferences.
```

The proposition should be existential and modest. It should not claim that one
welfare criterion always dominates the others.

### Extension Proposition 8: Multi-Attractor Basin Economics

If the fast preference subsystem has multiple attracting branches, the reduced
object is a basin-selection problem rather than a single closure map. Small
changes in initial conditions or institutions can switch the induced subjective
game.

This can be a later section or appendix. It is interesting but should not slow
the main theorem route.

## How To Keep The Article Readable

Lead with the clock, not the platform. The novel abstraction is the timescale
limit. Platforms make it vivid, but the theorem should not depend on platform
color.

Use one repeated diagram throughout:

```text
adaptation law -> P^star -> subjective game -> action -> material outcome
```

Then show which operator acts where:

```text
Nash acts on the subjective game.
Selection acts on material consequences.
Welfare evaluates paths and transition laws.
```

Keep three objects visually distinct in notation and prose:

- `U`: subjective utility, the thing agents maximize;
- `Pi` or `G`: material payoff, growth, or selection criterion;
- `P^star`: fast preference closure, the induced preference state.

Do not let "preference," "utility," "welfare," "fitness," and "material payoff"
blur into one another. Most confusion in this paper will come from readers
thinking one of those words secretly means another.

Move the finite-game theorem before the scalar taste model. A reader should see
that the result is not caused by choosing a monotone platform taste variable and
a monotone material-loss function.

Make the aligned-proxy control prominent. It is the paper's best protection
against overclaiming. The message should be:

```text
Fast closure changes the game. Harm depends on alignment.
```

Use examples as lanterns, not load-bearing walls. The one-dimensional taste
model should illustrate the survival frontier. The Prisoner's Dilemma should
illustrate the subjective/material payoff split. The platform application should
illustrate institutional control of the closure map. None should be asked to
prove the whole paper.

Keep welfare modest. The paper can convincingly show that final-preference
welfare is unstable under endogenous preference production. It should not claim
to solve welfare economics. Say "the welfare domain must expand" before saying
"this is the right welfare criterion."

Put technical proof detail in appendices where possible. In the main text,
state each proposition in plain language, give the one mathematical condition
that matters, then explain its economic meaning.

End each major section with a one-sentence takeaway. Examples:

- "Fast closure turns utility from an input into an induced map."
- "Nash is unchanged as a fixed-point method; the game has changed."
- "Selection does not disappear; its target changes."
- "Material harm is not a theorem of speed alone, but of misalignment after
  speed has moved the choice object."

Avoid the strongest-sounding words unless the math earns them. Prefer
"non-invariance," "object shift," "misalignment," "selection target," and
"closure" over "collapse," "manipulation," "doom," or "false consciousness."

The paper should feel like a clean theorem with a disturbing application, not a
disturbing application looking for a theorem.
