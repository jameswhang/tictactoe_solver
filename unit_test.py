import tictactoe
import unittest

class TestBoardMethods(unittest.TestCase):
    def test_determine_winner(self):
        user_win_board_one = ['x', 'x', 'x', 'o', 'x', 'o', 'o', 'o', 'x']
        user_win_board_two = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'o']
        user_win_board_three = ['x', 'o', 'x', 'o', 'x', 'o', 'x', ' ', 'o']

        draw_board_one = ['o', 'x', 'o', 'x', 'o', 'x', ' ', ' ', ' ']
        draw_board_two = ['o', 'x', 'x', 'x', 'o', 'o', 'x', 'o', 'x']
        draw_board_three = ['x', 'o', 'x', 'x', 'o', 'x', 'o', 'x', 'o']

        comp_win_board_one = ['o', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'x']
        comp_win_board_two = ['o', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'x']
        comp_win_board_three = ['o', 'x', 'o', 'x', 'o', 'x', 'o', ' ', 'x']

        self.assertEqual(tictactoe.determine_winner(user_win_board_one), 'u')
        self.assertEqual(tictactoe.determine_winner(user_win_board_two), 'u')
        self.assertEqual(tictactoe.determine_winner(user_win_board_three), 'u')

        self.assertEqual(tictactoe.determine_winner(draw_board_one), 'd')
        self.assertEqual(tictactoe.determine_winner(draw_board_two), 'd')
        self.assertEqual(tictactoe.determine_winner(draw_board_three), 'd')

        self.assertEqual(tictactoe.determine_winner(comp_win_board_one), 'c')
        self.assertEqual(tictactoe.determine_winner(comp_win_board_two), 'c')
        self.assertEqual(tictactoe.determine_winner(comp_win_board_three), 'c')

    def test_all_three_equal(self):
        self.assertTrue(tictactoe.all_three_equal(1, 1, 1))
        self.assertTrue(tictactoe.all_three_equal(2, 2, 2))
        self.assertTrue(tictactoe.all_three_equal('a', 'a', 'a'))
        self.assertTrue(tictactoe.all_three_equal('b', 'b', 'b'))
        self.assertTrue(tictactoe.all_three_equal('o', 'o', 'o'))

        self.assertFalse(tictactoe.all_three_equal('a', 'b', 'c'))
        self.assertFalse(tictactoe.all_three_equal('a', 'a', 'c'))
        self.assertFalse(tictactoe.all_three_equal(1, 2, 2))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBoardMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

