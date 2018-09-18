from unittest import TestCase

import trivia


class TestTrivia(TestCase):

    def test_current_category(self):
        test_game = trivia.Game()
        self.assertEqual(test_game._current_category, "Pop")
