# Fashion, Influencer, Meme, And Bubble Literature Pass

This note records the literature check for the standalone fashion-preference
module. It is not yet incorporated into the main article.

## What The Literature Already Gives Us

| Strand | Representative sources | Useful formal object | What it contributes |
| --- | --- | --- | --- |
| Bandwagon demand | Leibenstein (1950), "Bandwagon, Snob, and Veblen Effects in the Theory of Consumers' Demand" | Demand depends on other consumers' demand | A direct economics precedent for "being in style" as a demand shifter. |
| Informational fads | Bikhchandani, Hirshleifer, and Welch (1992), "A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades" | Sequential actions and private signals | Fads and crashes can arise when people rationally ignore private information after observing others. |
| Threshold contagion | Granovetter (1978), "Threshold Models of Collective Behavior"; Watts (2002), "A Simple Model of Global Cascades on Random Networks"; Morris (2000), "Contagion" | Adoption thresholds on populations or networks | Small seeds can stop or cascade depending on threshold distributions and network structure. |
| Social-interaction discrete choice | Brock and Durlauf (2001), "Discrete Choice with Social Interactions" | Logit choice with conformity payoffs | Logistic social interactions can produce multiple self-consistent average behaviors above a threshold. |
| Influence maximization | Kempe, Kleinberg, and Tardos (2003), "Maximizing the Spread of Influence through a Social Network" | Targeted seed sets and diffusion | Influencers are a formal object: targeted nodes can trigger disproportionate cascades. |
| Recommender feedback | Chaney, Stewart, and Engelhardt (2018); Jiang et al. (2019); Kleinberg, Mullainathan, and Raghavan (2024); Ashton and Franklin (2022) | Feedback between recommendations, behavior, beliefs, preferences, and proxy objectives | Platform exposure can change behavior or preferences and then train on its own induced data. |

## Gap For This Project

The literature already explains fads and contagion as belief, action, demand, or
diffusion dynamics. The useful project move is different:

1. Treat fashion, influencers, memes, and bubbles as inputs into a fast
   preference-formation law.
2. Let preferences close before the slower economic state moves.
3. Ask when the closure law is single-valued and harmlessly continuous, and
   when it becomes multi-valued, history-dependent, and sensitive to temporary
   shocks.

In short: the existing literature supplies the social-feedback mechanisms; the
new module embeds them in the endogenous-utility fast-closure framework.

## Chosen Formal Setup

The cleanest candidate is a binary logit social-interactions closure:

\[
  m = \tanh\!\bigl(\beta(h+\eta Wm+\Phi z)\bigr).
\]

Here:

- \(m\) is the vector of post-closure taste/adoption intensities.
- \(h\) is the baseline material or intrinsic field.
- \(W\) is an attention/influence network.
- \(\eta\) is social reinforcement.
- \(z\) is a meme, fashion, influencer, or platform-exposure field.
- \(\beta\) is preference responsiveness.

This is close enough to Brock-Durlauf and Ising/threshold models to be
recognizable, but it is used differently: the fixed point is not merely a
choice equilibrium. It is the utility-relevant state that closes before the
main economic game is analyzed.

## Sources Checked

- Bikhchandani, Sushil, David Hirshleifer, and Ivo Welch. 1992. "A Theory of
  Fads, Fashion, Custom, and Cultural Change as Informational Cascades."
  Journal of Political Economy 100(5): 992-1026.
  https://snap.stanford.edu/class/cs224w-readings/bikhchandani92fads.pdf
- Brock, William A., and Steven N. Durlauf. 2001. "Discrete Choice with Social
  Interactions." Review of Economic Studies 68(2): 235-260.
  https://hceconomics.uchicago.edu/sites/default/files/pdf/events/Brock_Durlauf_2001_REStud_v68-N2.pdf
- Granovetter, Mark. 1978. "Threshold Models of Collective Behavior."
  American Journal of Sociology 83(6): 1420-1443.
  https://www2.cs.siu.edu/~hexmoor/classes/CS539-F10/Collective-Behavior.pdf
- Kempe, David, Jon Kleinberg, and Eva Tardos. 2003. "Maximizing the Spread of
  Influence through a Social Network." KDD 2003.
  https://www.cs.cornell.edu/home/kleinber/kdd03-inf.pdf
- Leibenstein, Harvey. 1950. "Bandwagon, Snob, and Veblen Effects in the
  Theory of Consumers' Demand." Quarterly Journal of Economics 64(2):
  183-207. https://gwern.net/doc/sociology/1950-leibenstein.pdf
- Morris, Stephen. 2000. "Contagion." Review of Economic Studies 67(1):
  57-78. https://snap.stanford.edu/class/cs224w-readings/morris98contagion.pdf
- Watts, Duncan J. 2002. "A Simple Model of Global Cascades on Random
  Networks." PNAS 99(9): 5766-5771.
  https://www.stat.berkeley.edu/~aldous/260-FMIE/Papers/watts.pdf
- Chaney, Allison J. B., Brandon M. Stewart, and Barbara E. Engelhardt. 2018.
  "How Algorithmic Confounding in Recommendation Systems Increases Homogeneity
  and Decreases Utility." https://arxiv.org/abs/1710.11214
- Jiang, Ray, Silvia Chiappa, Tor Lattimore, Andras Gyorgy, and Pushmeet Kohli.
  2019. "Degenerate Feedback Loops in Recommender Systems."
  https://arxiv.org/abs/1902.10730
- Kleinberg, Jon, Sendhil Mullainathan, and Manish Raghavan. 2024. "The
  Challenge of Understanding What Users Want: Inconsistent Preferences and
  Engagement Optimization." Management Science 70(9): 6336-6355.
  https://arxiv.org/abs/2202.11776
