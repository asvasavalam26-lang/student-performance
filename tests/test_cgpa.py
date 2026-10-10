import pytest

from src.cgpa import calculate_cgpa, performance_category


def test_calculate_cgpa_returns_average_rounded_to_two_decimal_places():
    assert calculate_cgpa([8, 7, 9]) == 8
    assert calculate_cgpa([8.125, 7.25]) == 7.69


def test_calculate_cgpa_accepts_boundary_grade_points():
    assert calculate_cgpa([0, 10]) == 5


def test_calculate_cgpa_rejects_empty_input():
    with pytest.raises(ValueError, match="Grade points cannot be empty"):
        calculate_cgpa([])


@pytest.mark.parametrize("grade_points", [[-1], [10.1], [-0.01, 5], [5, 10.01]])
def test_calculate_cgpa_rejects_invalid_grade_points(grade_points):
    with pytest.raises(ValueError, match="Grade points must be between 0 and 10"):
        calculate_cgpa(grade_points)


@pytest.mark.parametrize(
    ("cgpa", "expected_category"),
    [
        (9.5, "Excellent"),
        (8, "Excellent"),
        (7.99, "Good"),
        (6, "Good"),
        (5.99, "Average"),
        (5, "Average"),
        (4.99, "Needs Improvement"),
        (0, "Needs Improvement"),
    ],
)
def test_performance_category_handles_boundaries(cgpa, expected_category):
    assert performance_category(cgpa) == expected_category
