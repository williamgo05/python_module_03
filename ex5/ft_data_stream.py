import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["Will", "Lucas_Camp", "Lucas_Math", "João", "Vini"]
    actions = ["Run", "Jump", "Sell", "Scream", "Sleep"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(new_list: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while len(new_list) > 0:
        index = random.randrange(len(new_list))
        removed = new_list.pop(index)
        yield (removed)


def main() -> None:
    event = gen_event()
    for i in range(0, 1000):
        print(f"Event {i}: {next(event)}")

    new_list = []
    for i in range(0, 10):
        new_list.append(next(event))
    print(f"\nBuilt list of 10 events: {new_list}")

    for event in consume_event(new_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {new_list}")


if __name__ == "__main__":
    main()
