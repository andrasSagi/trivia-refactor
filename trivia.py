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
                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.in_penalty_box[self.current_player] = False
                self._move_current_player(roll)
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
        else:
            self._move_current_player(roll)

    def _move_current_player(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12

        print(self.players[self.current_player] + '\'s new location is ' +
              str(self.places[self.current_player]))
        self._ask_question()

    def _ask_question(self):
        category = self._current_category
        print("The category is %s" % category)
        if category == 'Pop':
            print(self.pop_questions.pop(0))
        elif category == 'Science':
            print(self.science_questions.pop(0))
        elif category == 'Sports':
            print(self.sports_questions.pop(0))
        elif category == 'Rock':
            print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        category_type = self.places[self.current_player] % 4
        if category_type == 0:
            return 'Pop'
        elif category_type == 1:
            return 'Science'
        elif category_type == 2:
            return 'Sports'
        elif category_type == 3:
            return 'Rock'

    def handle_correct_answer(self):
        if not self.in_penalty_box[self.current_player]:
            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + ' now has ' +
                  str(self.purses[self.current_player]) + ' Gold Coins.')

    def next_player(self):
        self.current_player += 1
        if self.current_player == self.number_of_players:
            self.current_player = 0

    def handle_wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

    def did_player_win(self):
        return self.purses[self.current_player] == 6


if __name__ == '__main__':
    game_over = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while not game_over:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            game.handle_wrong_answer()
        else:
            game.handle_correct_answer()
            game_over = game.did_player_win()
        game.next_player()
