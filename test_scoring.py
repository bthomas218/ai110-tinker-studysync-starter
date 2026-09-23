"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

import pytest

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"

def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"

def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"


@pytest.mark.parametrize("score, expected", [(0, "Skip"), (100, "Great")])
def test_session_rating_accepts_inclusive_score_bounds(score, expected):
    assert session_rating(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_session_rating_rejects_scores_outside_range(score):
    with pytest.raises(ValueError, match="between 0 and 100"):
        session_rating(score)


@pytest.mark.parametrize("score", [3.14, 53.5, True])
def test_session_rating_rejects_non_integer_scores(score):
    with pytest.raises(TypeError, match="must be an integer"):
        session_rating(score)
