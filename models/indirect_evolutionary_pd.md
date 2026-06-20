# Indirect Evolutionary Prisoner's Dilemma With Mutable Social Preferences

## Benchmark

Material payoffs:

```text
        C      D
C     3,3    0,5
D     5,0    1,1
```

Subjective preferences:

```text
U_i = pi_i + lambda_i pi_j + b 1{C}
```

where:

- `pi_i` is material payoff,
- `lambda_i` is altruism or concern for the other player,
- `b` is a norm bonus for cooperation.

Agents choose actions according to subjective utility. Preference types reproduce according to material payoff.

## Endogenous Modification

Instead of fixed `lambda`, institutions or algorithms can shift the preference type:

```text
lambda' = lambda + eta(lambda_target - lambda)
```

The target may be prosocial or conflict-oriented. This gives a compact model of norm formation, moral education, outrage algorithms, and peer influence.

## Key Question

Does cooperation survive when preferences are mutable, and who controls the mutation target?

## Simulation Output

Run:

```bash
python3 scripts/run_toy_models.py
```

Then inspect:

- `results/tables/indirect_evolution_summary.csv`
- `results/toy_model_report.md`
