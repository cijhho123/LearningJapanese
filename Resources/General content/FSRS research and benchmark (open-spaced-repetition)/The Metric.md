## Introduction
Root Mean Square Error in Bins (RMSE (bins)), Log Loss, and Area Under the Receiver Operating Characteristic Curve (AUC) are the three primary metrics used in the SRS Benchmark to judge how well an algorithm predicts recall probability. Together they cover calibration (how close predicted probabilities are to what actually happens) and discrimination (whether higher scores really mean higher success rates).

This page explains each metric, how RMSE (bins) evolved, and why the SRS Benchmark does **not** adopt the Universal Metric (UM) proposed by the SuperMemo team.

## Log Loss
Log Loss tells us how “surprised” the model should be when the real outcome shows up. Imagine the model places a probability bet on each review being remembered: if it says “90 % chance of success” and the learner succeeds, it earns a small penalty; if the learner fails, it pays a large penalty because it was confidently wrong. The only way to keep the average penalty low is to state honest probabilities that match reality.

Log Loss is also the negative log-likelihood of the data under a Bernoulli model. Minimising Log Loss is therefore equivalent to finding the probabilities that make the observed review sequence most likely.

$$
\text{LogLoss} = - \frac{1}{N} \sum_{i=1}^{N} \left(y_i \log p_i + (1 - y_i)\log(1 - p_i)\right)
$$

* $y_i$ is the observed outcome (Again = 0, Hard/Good/Easy = 1).
* $p_i$ is the algorithm’s predicted chance of success.

**Intuition**

- Keep betting high when you’re right and low when you’re wrong; that keeps the “surprise bill” small.
- Confident mistakes explode the bill, so the best strategy is to express genuine probabilities.
- The score depends only on the model’s own predictions and the observed outcomes, so other algorithms cannot distort it.

## AUC
The Area Under the ROC Curve measures how well an algorithm orders cards from easiest to hardest.

1. Sweep a decision threshold across 0–1 and plot True Positive Rate vs. False Positive Rate.
2. Compute the area under that curve: perfect ordering yields 1.0, random ordering ~0.5.

**Intuition**

- Threshold-free: it evaluates ranking quality across all cut-offs.
- Robust to class imbalance: useful when review decks are biased toward success or failure.
- Complements Log Loss: a model can rank cards well yet be poorly calibrated, so we track both.

## RMSE (bins)
RMSE (bins) measures calibration across regions of the review feature space instead of individual reviews.

### Old method
1. Group predicted probabilities into bins (e.g., 0.8–0.9).
2. Gather actual outcomes for each bin.
3. Compare the bin averages of prediction vs. outcome.
4. Weight by the number of reviews in each bin and compute:

$$
RMSE(bins) = \sqrt{\frac{\sum_{i=1}^{n} w_i \left(\overline{R}_{\text{predicted}, i} - \overline{R}_{\text{measured}, i}\right)^2}{\sum_{i=1}^{n} w_i}}
$$

### How it could be cheated (old method)
An algorithm could push most predictions into a single bin and output the dataset’s average recall rate. RMSE (bins) would then approach zero even though the model learned nothing. Reducing prediction variance similarly hides miscalibration.

![Calibration comparison](https://github.com/open-spaced-repetition/fsrs4anki/assets/83031600/338d8d81-9389-4d91-9cca-5b9b6551d548)

### New method
To resist gaming, bins are now defined by features independent of the algorithm’s predictions:

- Interval length
- Number of prior reviews
- Number of lapses

Each feature is rounded with fixed schedules; reviews sharing the same rounded tuple fall into the same bin.

```python
delta_t = round(2.48 * power(2.57, floor(log(x)/log(2.57))), 2)
n_reviews = round(1.52 * power(1.58, floor(log(x)/log(1.58))), 0)
n_lapses = round(1.4 * power(1.48, floor(log(x)/log(1.48))), 0) if x != 0 else 0
```

### Remaining weakness
The revised method can still be gamed if an adversarial algorithm records $\overline{R}_{\text{measured}}$ for each bin and deliberately sets predictions to keep $\overline{R} _{\text{predicted}}$ equal to that value. Hence RMSE (bins) is always read alongside Log Loss and AUC.

## Why the SRS Benchmark does not use the Universal Metric
The Universal Metric (UM) compares algorithms by letting each “referee” bin reviews using its own predictions. Although the idea is appealing, it clashes with the goals of an open benchmark:

1. **Dependence on referee predictions** — UM requires every competitor’s probabilities, tying a player’s score to another model’s behaviour.
2. **Group-level exploitability** — Because UM only checks bin averages, an adversary can track those averages and force its UM close to zero without understanding memory. Our `ADVERSARIAL` baseline demonstrates this in practice ([pull request #88](https://github.com/open-spaced-repetition/fsrs-vs-sm17/pull/88)).
3. **Causality issues** — In real deployments the referee’s prediction might not be known before the player has to respond.
4. **No discrimination signal** — UM ignores ranking ability; a model that nails bin averages but cannot tell cards apart gets a perfect score.
5. **Opaque specification** — SuperMemo has not published the exact evaluation code, which limits reproducibility.

For these reasons the SRS Benchmark emphasises metrics that:
- Depend only on the evaluated algorithm’s predictions and the observed outcomes (Log Loss, AUC).
- Use review context instead of other models’ outputs to build bins (RMSE (bins)).

## References
- SuperMemo, “[Universal metric for cross-comparison of spaced repetition algorithms](https://supermemo.guru/wiki/Universal_metric_for_cross-comparison_of_spaced_repetition_algorithms).”
- Open Spaced Repetition Community, “[Adversarial exploit of UM](https://github.com/open-spaced-repetition/fsrs-vs-sm17/pull/88).”
