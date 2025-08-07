from typing import List

import pytest
from scipy import stats

from ttest import calculate_confidence_interval, perform_t_test


def test_perform_t_test_positive() -> None:
    """Test two-sided t-test for positive difference."""
    points1: List[float] = [3.0, 3.1, 2.9, 3.2, 2.8]
    points2: List[float] = [1.0, 1.1, 0.9, 1.2, 0.8]
    expected: float = stats.ttest_ind(points1, points2, equal_var=False).pvalue
    assert perform_t_test(points1, points2) == pytest.approx(expected)


def test_perform_t_test_negative() -> None:
    """Test two-sided t-test for negative difference."""
    points1: List[float] = [1.0, 1.1, 0.9, 1.2, 0.8]
    points2: List[float] = [3.0, 3.1, 2.9, 3.2, 2.8]
    expected: float = stats.ttest_ind(points1, points2, equal_var=False).pvalue
    assert perform_t_test(points1, points2) == pytest.approx(expected)


def test_perform_t_test_one_sided() -> None:
    """Test one-sided t-test for greater-than alternative."""
    points1: List[float] = [3.0, 3.1, 2.9, 3.2, 2.8]
    points2: List[float] = [1.0, 1.1, 0.9, 1.2, 0.8]
    expected: float = stats.ttest_ind(
        points1, points2, equal_var=False, alternative="greater"
    ).pvalue
    assert perform_t_test(points1, points2, two_sided=False) == pytest.approx(expected)


def test_calculate_confidence_interval() -> None:
    """Test confidence interval contains sample mean."""
    points: List[float] = [1, 2, 3, 4, 5]
    lower: float
    upper: float
    lower, upper = calculate_confidence_interval(points)
    assert 1.4 < lower < 1.8
    assert 4.2 < upper < 4.6
    assert lower < 3.0 < upper  # Mean should be within interval


def test_calculate_confidence_interval_different_confidence() -> None:
    """Test confidence interval changes with confidence level."""
    points: List[float] = [10, 12, 14, 16, 18]
    lower: float
    upper: float
    lower, upper = calculate_confidence_interval(points, 0.90)
    assert lower < 14.0 < upper
    assert upper - lower < 10.0


def test_perform_t_test_edge_cases() -> None:
    """Test p-value lies within expected bounds."""
    points1: List[float] = [1.0, 2.0]
    points2: List[float] = [1.5, 2.5]
    p_value: float = perform_t_test(points1, points2)
    assert 0.0 <= p_value <= 1.0


def test_calculate_confidence_interval_single_point() -> None:
    """Test confidence interval is infinite for single sample."""
    points: List[float] = [5.0]
    lower: float
    upper: float
    lower, upper = calculate_confidence_interval(points)
    assert lower == float("-inf")
    assert upper == float("inf")
