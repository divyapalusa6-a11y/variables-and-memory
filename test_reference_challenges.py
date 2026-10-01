import io
import unittest
from contextlib import redirect_stdout

from challenges import reference_challenges


def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()


def test_challenge_01_prints_expected_values():
    output = capture_output(reference_challenges.challenge_01)

    assert "Before reassignment: apples=1729, papaya=1729" in output
    assert "After reassignment: apples=1771, papaya=1729" in output


def test_challenge_02_keeps_original_list_values():
    output = capture_output(reference_challenges.challenge_02)

    assert "Initially: bananas=[1729, 42], apples=1729, oranges=42" in output
    assert "After changing oranges: bananas=[1729, 42], oranges=52" in output


def test_challenge_03_mutates_list_in_helper():
    output = capture_output(reference_challenges.challenge_03)

    assert "Before helper: bananas=[1729, 42]" in output
    assert "Inside helper: kiwis=[1729, 42, 315], mangos=315" in output
    assert "After helper: bananas=[1729, 42, 315]" in output


def test_aliasing_changes_shared_list():
    a = [1, 2]
    b = a
    b.append(3)

    assert a == [1, 2, 3]
    assert b == [1, 2, 3]


def test_empty_list_can_be_mutated():
    items = []
    items.append("first")

    assert items == ["first"]


def test_strings_are_immutable():
    word = "apple"
    word = word + "s"

    assert word == "apples"


class TestReferenceChallenges(unittest.TestCase):
    def test_challenge_01(self):
        output = capture_output(reference_challenges.challenge_01)
        self.assertIn("apples=1771", output)
        self.assertIn("papaya=1729", output)

    def test_challenge_02(self):
        output = capture_output(reference_challenges.challenge_02)
        self.assertIn("bananas=[1729, 42]", output)
        self.assertIn("oranges=52", output)

    def test_challenge_03(self):
        output = capture_output(reference_challenges.challenge_03)
        self.assertIn("kiwis=[1729, 42, 315]", output)
        self.assertIn("After helper: bananas=[1729, 42, 315]", output)
