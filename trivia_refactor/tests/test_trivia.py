from unittest import TestCase

from trivia_refactor import trivia


class TestTrivia(TestCase):

    def test_current_category(self):
        test_game = trivia.Game()
        self.assertEqual(test_game._current_category, "Pop")
