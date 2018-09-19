#!/usr/bin/env python
from random import randrange


class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [False] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def add(self, player_name):
        self.players.append(player_name)
        print(player_name + " was added")
        print("They are player number %s" % self.number_of_players)

    @property
    def number_of_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self._move_current_player(roll)
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self._move_current_player(roll)

    def _move_current_player(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12

        print(self.players[self.current_player] +
              '\'s new location is ' +
              str(self.places[self.current_player]))
        print("The category is %s" % self._current_category)
        self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop':
            print(self.pop_questions.pop(0))
        if self._current_category == 'Science':
            print(self.science_questions.pop(0))
        if self._current_category == 'Sports':
            print(self.sports_questions.pop(0))
        if self._current_category == 'Rock':
            print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] % 4 == 0:
            return 'Pop'
        elif self.places[self.current_player] % 4 == 1:
            return 'Science'
        elif self.places[self.current_player] % 4 == 2:
            return 'Sports'
        else:
            return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] +
                      ' now has ' +
                      str(self.purses[self.current_player]) +
                      ' Gold Coins.')

                winner = self._did_player_win()
                return winner
            else:
                return True

        else:

            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] +
                  ' now has ' +
                  str(self.purses[self.current_player]) +
                  ' Gold Coins.')

            winner = self._did_player_win()
            return winner

    def next_player(self):
        self.current_player += 1
        if self.current_player == self.number_of_players:
            self.current_player = 0

    def handle_wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = True
            game.handle_wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        game.next_player()
        if not not_a_winner:
            break
