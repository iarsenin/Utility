# Round 1 Editor Memo

Date: 2026-06-20

Role: Editor agent for the Utility project.

## Editorial Bottom Line

The current project direction is promising only if the paper becomes a
theorem-first mathematical economics paper. A reputable economics or
math-econ venue will not accept the broad claim that preferences are
endogenous, that platforms shape tastes, or that engagement is not welfare.
Those claims are already occupied. The defensible contribution is narrower and
stronger:

```text
In the T_P -> 0 limit, fast preference closure replaces the original game by a
reduced subjective game. Nash equilibrium is computed after closure, material
evaluation is applied after closure, and selection operates on adaptation laws,
institutions, or induced systems rather than on initial preference states.
Material harm is not automatic. It depends on the alignment between the
preference-generating operator and material welfare.
```

This means the finite-game fast-closure route should be the spine. Platform
control should be the main application. The one-dimensional taste model should
be exposition and intuition, not the proof engine.

## 1. Venue Expectations

### Core Primitives Must Be Explicit

A theory venue will expect the paper to define the environment before making
claims. At minimum, the main model needs:

- finite player set `N`;
- finite action sets `A_i` and action profiles `a in A`;
- material payoff functions `pi_i(a; E, I)`;
- preference state or fast closure object `P`;
- subjective utility functions `U_i(a; P, E, I)`;
- environment and institution variables, named consistently as `E` and `I` or
  replaced by one simpler notation;
- a fast preference operator or correspondence with a well-stated closure
  condition;
- an equilibrium convention for the reduced game;
- a material evaluation or selection criterion, distinct from subjective
  utility;
- an institutional or adaptation-law index when selection is said to act on
  laws rather than preference states.

The paper cannot rely on verbal phrases such as "utility adapts" or "the
platform changes preferences" until these objects have been defined.

### Theorems Must Carry The Contribution

The main text should contain theorem statements with assumptions, not only
claims and simulations. The minimum publishable theorem sequence is:

1. Fast closure theorem: under stated closure assumptions, the `T_P -> 0`
   economy is represented by a reduced game with subjective payoffs
   `U_i(a; P^*(E, I), E, I)`.
2. Nash-invariance theorem: the material Nash set and the fast-adapted
   subjective Nash set coincide exactly under best-response correspondence
   equivalence, or under a clearly stated strategically irrelevant
   transformation.
3. Generic-shift proposition: outside strategically irrelevant transformations,
   fast preference closure changes best responses or equilibrium predictions on
   an open/dense, full-measure, or otherwise precise set of finite games.
4. Selection-target theorem: with common unique fast closure, selection over
   initial preference states is degenerate; selection, if present, acts on
   adaptation laws, institutions, populations, or induced systems.
5. Platform-alignment proposition: material loss is conditional on alignment
   between the platform proxy and material welfare. The aligned case must be a
   control, not an afterthought.

These results should be phrased as "under assumptions A1-Ak, conclusion C
follows." Avoid theorem titles that promise more than the proof establishes.

### The Literature Position Must Be Modest And Precise

The literature review must explicitly concede:

- endogenous preferences are old;
- indirect evolutionary preference theory already separates subjective
  preferences from material payoff;
- recommender feedback loops are known;
- engagement and welfare can diverge;
- welfare with endogenous preferences is already a major normative problem.

The contribution should then be stated as a specific formal synthesis:

```text
fast preference closure + finite-game Nash analysis + material evaluation after
closure + platform or institutional choice of adaptation law
```

Do not claim to have discovered endogenous utility, platform manipulation,
preference feedback, or the engagement-welfare gap.

### Examples Must Not Substitute For Proof

The one-dimensional taste model is useful because readers can see the mechanism.
It is also dangerous because the monotone structure can make the result look
built in. A venue referee will ask whether harm follows from the theorem or
from the chosen scalar functions. Therefore:

- use the one-dimensional taste model after the finite-game theorem;
- state exactly which assumptions make the harmful outcome appear;
- present the aligned-proxy control before claiming policy relevance;
- describe simulations as diagnostics and illustrations, not evidence for a
  universal theorem.

### Welfare Claims Need A Domain

Any welfare claim must specify the evaluator:

- current subjective utility;
- initial-preference welfare;
- final-preference welfare;
- material payoff or growth;
- meta-preference or autonomy criterion;
- constitutional restriction on admissible transition laws;
- welfare over allocation-preference paths.

The paper should not say "welfare falls" without saying for whom, under which
preference state, or according to which material/meta criterion.

### Empirical Claims Must Be Hypotheses

A theory paper may include empirical implications, but it should not overstate
what the current simulations or toy calibrations establish. Acceptable phrasing:

```text
The model suggests testing whether exposure changes future choice elasticities,
not merely current choices.
```

Risky phrasing:

```text
Platforms cause extinction.
```

The latter requires a real population model and evidence. Keep empirical
language conditional, model-bound, and testable.

## 2. Biggest Risks

### Argument Order Risk

The current materials sometimes lead with platforms, survival, extinction, and
calibrated toy examples before the general theorem is fully in place. That
order invites rejection. A referee will see a morally charged application and
then inspect the model for built-in conclusions.

Recommended order:

1. State the problem: what happens to Nash, selection, and welfare when
   preference states close infinitely fast?
2. Define the finite-game environment.
3. Prove fast closure and Nash-object shift.
4. Prove invariance conditions and generic non-invariance.
5. Prove selection-target shift.
6. Apply the theorem to platform control through proxy alignment.
7. Use one-dimensional taste and Prisoner's Dilemma examples for intuition.
8. Discuss welfare domains and empirical implications.

The reader should encounter the formal object before the vivid platform story.

### Novelty Risk

The paper is not novel if the contribution is stated as:

```text
Preferences are endogenous.
Platforms shape preferences.
Engagement is not welfare.
Final preferences may be normatively suspect.
```

The paper may be novel if the contribution is stated as:

```text
The singular limit T_P -> 0 changes the state space to which Nash equilibrium
and material selection apply, and platform-controlled preference-transition
operators can be analyzed as choices over reduced games.
```

The Writer must use this narrower claim consistently. Any broad rhetorical
claim will make the paper look less original, not more.

### Empirical And Policy Overreach Risk

The current project language sometimes moves quickly from model examples to
social media, AI, survival, collapse, and regulation. Those topics are
motivating, but they are also easy to overclaim.

High-risk statements:

- "fast endogenous preferences imply collapse";
- "platform optimization causes material extinction";
- "Darwinian selection cannot rescue the system" without specifying the
  admissible adaptation laws and population dynamics;
- "users are worse off" without specifying initial, final, meta, or material
  welfare;
- "empirical timescales show..." when the project currently has methods, not
  estimates.

Safer statements:

- "fast preference closure can change the reduced game";
- "material harm depends on proxy alignment";
- "in this application, a misaligned proxy selects an adaptation law that lowers
  the material criterion";
- "the model implies an empirical test: exposure should affect future
  preference parameters or choice elasticities."

### Notation Risk

The notation currently risks looking like several papers stitched together:
`theta`, `P`, `Phi`, `K_m`, `G`, `z`, `m`, `I`, `E`, `F`, `g`, `pi`, `U`,
platform value, welfare, and fitness all appear in nearby roles.

The Writer must choose one notation system for the article and keep it.
Recommended discipline:

- use `theta` for preference state in continuous or scalar examples;
- use `P` or `p` for finite-game preference closure only if there is a reason
  not to use `theta`;
- use `pi_i` for material payoff in games;
- use `U_i` for subjective utility;
- use `V` or `Pi^P` for platform objective, never `Pi_i` if `pi_i` is material
  payoff;
- use `g` only for growth in population examples;
- reserve `F` for a general material evaluator if the model is not explicitly
  evolutionary;
- use `I` for institution or platform policy, or use `m`, but not both in the
  same theorem unless their difference is essential;
- define every correspondence with domain and codomain.

The paper also needs one consistent timescale notation. Use `T_P` if that is
the title object. Do not alternate among `T`, `T_pref`, and `T_P` in theorem
statements.

### Equilibrium-Selection Risk

Finite games can have multiple equilibria. The current theorem route needs an
explicit convention:

- compare Nash sets rather than selected equilibria; or
- introduce a selection correspondence; or
- state all welfare/material comparisons as set-valued; or
- impose uniqueness in the relevant propositions.

Do not bury equilibrium selection in simulations. A theory referee will notice
immediately.

### Genericity Risk

"Generically changes the game" is a serious mathematical claim. The draft must
say what generic means:

- open and dense;
- full measure under a specified distribution;
- outside a lower-dimensional set;
- for all transformations except strategically irrelevant ones;
- in random finite games under a simulation design, explicitly labeled as
  numerical evidence rather than theorem.

If the proof only establishes non-invariance under some transformations, do not
call the result generic.

## 3. Style Rules For The Writer

### Be Explicit

- Define every primitive before using it.
- State the economic role of each object in the sentence immediately before or
  after its first display.
- Write every main claim in the form: "If assumptions A hold, then conclusion B
  follows."
- Distinguish assumption, definition, proposition, example, simulation, and
  interpretation.
- When saying "selection acts on X," identify the selection operator and the
  population or menu over which it acts.
- When saying "the platform chooses X," state its feasible set and objective.
- When saying "welfare," name the welfare criterion.

### Be Readable

- Use one idea per paragraph.
- Put the intuitive sentence before the equation when introducing a new object.
- Put the formal consequence after the equation.
- Keep displays short. If a displayed equation needs three verbal clauses to be
  understood, split it.
- Prefer "material payoff" in the main economics sections. Use "fitness" only
  in explicitly evolutionary sections.
- Use "reduced game" repeatedly and consistently; it is the reader's anchor.
- Use examples only after the theorem they illustrate.

### Do Not Be Dry Or Confusing

- Avoid abstract noun piles such as "post-closure selection target
  reallocation mechanism" when "selection acts on adaptation laws" is clearer.
- Avoid moralized verbs unless the model earns them. "Selects," "induces," and
  "lowers the material criterion" are better than "captures," "corrupts," or
  "destroys" in theorem sections.
- Do not write long paragraphs of literature names. Group literatures by the
  obstacle they pose and the role they play.
- Do not hide the paper's humility. A strong sentence like "This paper does not
  claim that endogenous preferences are new" will increase credibility.
- Do not use "utility" as both representation, welfare, and preference state.
  If `theta` moves, say `theta` moves. If `U(.; theta)` represents current
  preferences, say so.
- Avoid "can" when the result is an "if and only if," and avoid "must" when the
  result is conditional.

### Required Contribution Paragraph Template

The introduction should contain a paragraph close to this structure:

```text
The contribution is not the observation that preferences change, nor the claim
that engagement and welfare can diverge. The contribution is a singular-limit
analysis of games in which preference states close on a fast timescale. In the
limit T_P -> 0, Nash equilibrium is computed in a reduced subjective game, while
material evaluation is applied to the outcomes of that reduced game. This
separates three questions that are often conflated: which actions are locally
optimal under adapted preferences, which reduced systems are materially
selected, and which preference-transition laws are admissible for welfare
analysis.
```

The final article can refine the prose, but it should not weaken the
distinctions.

## 4. Pass/Fail Checklist For Future Draft Rounds

Each future draft round should be judged as pass or fail. A draft fails the
round if any required item for that round is missing, ambiguous, or only handled
verbally when a formal statement is needed.

### Round 2: Architecture And Contribution

Pass if:

- the finite-game fast-closure theorem route is the central spine;
- platform control is clearly an application, not the theorem spine;
- the one-dimensional taste model is labeled as exposition;
- the introduction states what is not novel before stating what is novel;
- the paper's main claim is conditional, not "fast preferences imply harm";
- the section order puts theorem before platform and toy examples.

Fail if:

- the draft opens as a broad AI/platform critique;
- novelty is pitched as endogenous preferences or engagement-welfare divergence;
- examples appear to prove the main theorem;
- collapse, extinction, or welfare loss is asserted before the model defines
  the relevant material criterion.

### Round 3: Formal Model And Theorems

Pass if:

- all primitives have domains and roles;
- `T_P -> 0` has a mathematically stated closure condition;
- the reduced game is formally defined;
- the Nash-invariance result is stated with best-response correspondences;
- equilibrium multiplicity is handled by sets, selection correspondences, or
  uniqueness assumptions;
- the selection-target shift is a proposition or theorem, not only prose;
- every theorem has assumptions that are strong enough for the conclusion.

Fail if:

- notation changes between theorem statements;
- "generic" is used without a definition;
- proof sketches rely on intuition from the scalar platform model;
- material payoff and subjective utility are not cleanly separated;
- selection over preference states is declared degenerate without specifying
  common closure and timing.

### Round 4: Platform Application

Pass if:

- the platform objective is formally defined;
- the platform chooses an adaptation law, proxy, or institution from a feasible
  set;
- alignment, independence, and misalignment are distinguished;
- the aligned-proxy case is used as a control;
- any material-loss claim is conditional on the proxy relation;
- policy language follows from comparative statics or propositions.

Fail if:

- the platform section restates "engagement is not welfare" without using
  endogenous preference transitions essentially;
- material harm is treated as automatic;
- simulations are presented as proof;
- regulation is discussed without specifying the constrained object;
- "users prefer it" and "users are better off" are conflated.

### Round 5: Welfare And Literature

Pass if:

- the welfare section separates initial, final, material, meta-preference, and
  path-based criteria;
- final-preference Pareto claims are stated as fragile or criterion-dependent,
  not simply false;
- the literature review directly addresses indirect evolutionary preferences,
  adaptive utility, cultural transmission, behavioral welfare, and recommender
  feedback;
- the closest papers are treated as serious competitors, not decorative cites;
- the contribution is restated after the literature in narrow formal terms.

Fail if:

- welfare is discussed without a domain;
- literature paragraphs become name lists;
- the draft suggests economics assumed fixed tastes in any broad historical
  sense;
- recommender-system feedback or engagement-welfare divergence is implied to be
  new;
- normative conclusions outrun the formal criteria.

### Round 6: Empirical Implications And Final Polish

Pass if:

- empirical implications are written as testable hypotheses;
- no causal empirical claim is made without data or citation;
- simulations are labeled as examples, numerical diagnostics, or robustness
  checks;
- notation is consistent across the introduction, theorem section, application,
  and conclusion;
- theorem claims, abstract claims, and conclusion claims match exactly;
- the prose is clear enough that a referee can summarize the contribution in
  three sentences.

Fail if:

- the abstract promises more than the theorems deliver;
- empirical discussion reads like evidence rather than implications;
- terms such as "fitness," "material payoff," "welfare," and "utility" are used
  interchangeably;
- the conclusion returns to broad claims that the paper carefully avoided;
- the paper is technically correct but rhetorically obscure.

## Final Editorial Instruction

The Writer should protect the paper from its own most exciting rhetoric. The
publishable version is not a manifesto about endogenous utility. It is a clean
singular-limit paper showing how fast preference closure changes the game,
where Nash and material evaluation land after closure, and why platform control
matters when it selects the transition law.
