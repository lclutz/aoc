ifile = "example.txt"

with open(ifile, mode="r") as f:
    puzzle_input = [line.strip() for line in f]
    player_split = puzzle_input.index("")
    deck1 = [int(i) for i in puzzle_input[1:player_split]]
    deck2 = [int(i) for i in puzzle_input[player_split + 2:]]

history = list()


def score(deck):
    s = 0
    deck.reverse()
    for index, value in enumerate(deck, 1):
        s += index * value
    return s


def play(deck1, deck2):
    top_card_1, *deck1 = deck1
    top_card_2, *deck2 = deck2
    if top_card_1 > top_card_2:
        deck1.append(top_card_1)
        deck1.append(top_card_2)
    else:
        deck2.append(top_card_2)
        deck2.append(top_card_1)
    return (deck1, deck2)


while len(deck1) > 0 and len(deck2) > 0:

    if (deck1, deck2) in history:
        # player 1 wins
        print(f"part1: {score(deck1)}")
        break
    else:
        history.append((deck1,deck2))
        deck1, deck2 = play(deck1, deck2)
        if len(deck1) == 0:
            print(f"part1: {score(deck2)}")
            break
        if len(deck2) == 0:
            print(f"part1: {score(deck1)}")
            break



