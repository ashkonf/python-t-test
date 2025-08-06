from __future__ import annotations

import math
from typing import Sequence, Tuple

import numpy as np
from scipy import stats


def perform_t_test(
    points1: Sequence[float], points2: Sequence[float], two_sided: bool = True
) -> float:
    n1: float = float(len(points1))
    n2: float = float(len(points2))
    x1_bar: float = float(np.mean(points1))
    x2_bar: float = float(np.mean(points2))
    s1_sq: float = float(np.var(points1))
    s2_sq: float = float(np.var(points2))
    s: float = math.sqrt(s1_sq / n1 + s2_sq / n2)
    t: float = (x1_bar - x2_bar) / s
    df_num: float = (s1_sq / n1 + s2_sq / n2) ** 2
    df_den: float = (s1_sq / n1) ** 2 / (n1 - 1.0) + (s2_sq / n2) ** 2 / (n2 - 1.0)
    df: float = df_num / df_den

    probability: float = float(stats.t.cdf(t, df))
    if two_sided:
        p_val: float = 1.0 - probability if probability > 0.5 else probability
        probability = 1.0 - 2 * p_val

    p_value: float = 1.0 - probability
    return p_value


def calculate_confidence_interval(
    points: Sequence[float], confidence_threshold: float = 0.95
) -> Tuple[float, float]:
    n: float = float(len(points))
    v: float = n - 1.0
    x_bar: float = float(np.mean(points))
    s: float = math.sqrt(float(np.var(points)))
    A: float = float(stats.t.ppf(confidence_threshold, v))
    lower_bound: float = x_bar - A * s / math.sqrt(n)
    upper_bound: float = x_bar + A * s / math.sqrt(n)
    return (lower_bound, upper_bound)
