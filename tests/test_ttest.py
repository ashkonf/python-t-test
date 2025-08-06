from typing import List

import pytest
from scipy import stats

from ttest import calculate_confidence_interval, perform_t_test


def test_perform_t_test_positive() -> None:
    points1: List[float] = [3.0, 3.0, 3.0]
    points2: List[float] = [1.0, 1.0, 1.0]
    expected: float = stats.ttest_ind(points1, points2, equal_var=False).pvalue
    assert perform_t_test(points1, points2) == pytest.approx(expected)


def test_perform_t_test_negative() -> None:
    points1: List[float] = [1.0, 1.0, 1.0]
    points2: List[float] = [3.0, 3.0, 3.0]
    expected: float = stats.ttest_ind(points1, points2, equal_var=False).pvalue
    assert perform_t_test(points1, points2) == pytest.approx(expected)


def test_perform_t_test_one_sided() -> None:
    points1: List[float] = [3.0, 3.0, 3.0]
    points2: List[float] = [1.0, 1.0, 1.0]
    expected: float = stats.ttest_ind(
        points1, points2, equal_var=False, alternative="greater"
    ).pvalue
    assert perform_t_test(points1, points2, two_sided=False) == pytest.approx(expected)


def test_calculate_confidence_interval() -> None:
    points: List[float] = [1, 2, 3, 4, 5]
    lower: float
    upper: float
    lower, upper = calculate_confidence_interval(points)
    expected_lower: float = 1.6519897611355208
    expected_upper: float = 4.348010238864479
    assert lower == pytest.approx(expected_lower)
    assert upper == pytest.approx(expected_upper)
