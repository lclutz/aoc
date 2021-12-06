ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]
    player_split = puzzle_input.index("")
    deck1 = [int(i) for i in puzzle_input[1:player_split]]
    deck2 = [int(i) for i in puzzle_input[player_split + 2:]]

history = set()


def score(deck):
    s = 0
    deck.reverse()
    for index, value in enumerate(deck, 1):
        s += index * value
    return s


while len(deck1) > 0 and len(deck2) > 0:
    if (tuple(deck1),tuple(deck2)) in history:
        # player 1 wins
        print(f"part1: {score(deck1)}")
        break
    else:
        history.add((tuple(deck1),tuple(deck2)))
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]


if len(deck1) == 0:
    print(f"part1: {score(deck2)}")
if len(deck2) == 0:
    print(f"part1: {score(deck1)}")


deck1 = [int(i) for i in puzzle_input[1:player_split]]
deck2 = [int(i) for i in puzzle_input[player_split + 2:]]


def recursive_combat(deck1, deck2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    if len(deck1) >= card1 and len(deck2) >= card2:
        return recursive_combat(deck1[:card1], deck2[:card2])
    else:
        return 1 if card1 > card2 else 2


class Game:

    def __init__(self, deck1, deck2):
        self.history = set()
        self.deck1 = deck1
        self.deck2 = deck2

    def winner(self):
        while len(self.deck1) != 0 and len(self.deck2) != 0:
            if (tuple(self.deck1), tuple(self.deck2)) in self.history:
                return 1
            else:
                self.history.add((tuple(self.deck1), tuple(self.deck2)))
                card1 = self.deck1.pop(0)
                card2 = self.deck2.pop(0)
            if len(self.deck1) >= card1 and len(self.deck2) >= card2:
                winner = Game(self.deck1[:card1], self.deck2[:card2]).winner()
                if winner == 1:
                    self.deck1 += [card1, card2]
                else:
                    self.deck2 += [card2, card1]
            else:
                if card1 > card2:
                    self.deck1 += [card1, card2]
                else:
                    self.deck2 += [card2, card1]
        return 1 if len(self.deck2) == 0 else 2


g = Game(deck1, deck2)
if g.winner() == 1:
    print(f"part2: {score(g.deck1)}")
else:
    print(f"part2: {score(g.deck2)}")
