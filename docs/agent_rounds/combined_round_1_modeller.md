# Combined Round 1: Modeller

Date: 2026-06-23

Role: exact, rigorous, mathematically skeptical.

Target: `paper/combined_fast_preference_closure_v1.html`

## Main Findings

1. The general manuscript leaned too strongly on unique global closure, while the social-feedback mechanism deliberately uses multiple attracting branches. The framework needed a branch-selection closure map.
2. The social-feedback state \(m\) needed to be embedded into the finite-game subjective utility \(U_i\), otherwise Section 8 was only a preference-dynamics model.
3. The hysteresis claims needed an explicit fast dynamic, not just a fixed-point equation.
4. The near-critical multiplier should state that amplification requires the exposure vector to load on the near-critical eigendirection.
5. The persistent-loss result should choose \(z\in(B_c-h,z_{\max})\) explicitly.

## Integrated Changes

- Introduced \(C_\ell(E,q,\zeta)\) as the general closure map.
- Kept \(\theta_\ell^\star(E)\) as the unique-closure abbreviation.
- Added the branch-selected reduced game \(\Gamma_{\ell,q,\zeta}^\star(E)\).
- Added social-feedback dynamics \(T_m\dot m_i=-m_i+\tanh(\cdot)\).
- Added a utility embedding \(U_i(a;m,E,\ell)=\nu_i^0(a;E,\ell)+\lambda_i m_i\mathbf 1\{a_i=F_i\}\).
- Tightened Propositions 5 and 7 and the Appendix B proof language.
