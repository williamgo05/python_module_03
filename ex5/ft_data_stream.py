import random

def gen_event():
    players = ["Will", "Lucas_Camp", "Lucas_Math", "João", "Vini"]
    actions = ["Run", "Jump", "Sell", "Scream", "Sleep"]
    i = 0
    while (i < 1000):
        yield(random.choice(players), random.choice(actions))
        i += 1


def main():
    event = gen_event()
    while gen_event:
        print(next(event))


if __name__ == "__main__":
    main()