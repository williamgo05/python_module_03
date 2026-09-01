import sys


def validate_arg(arg: str) -> int:
    return int(arg)


def create_new_list(arg: str, new_list: list) -> None:
    try:
        score = validate_arg(arg)
        new_list.append(score)
    except ValueError:
        print(f"Invalid parameter: '{arg}'")


def main() -> None:
    print("=== Player Score Analytics ===")

    new_list: list[int] = []
    i = 1
    while i < len(sys.argv):
        create_new_list(sys.argv[i], new_list)
        i += 1

    if len(new_list) == 0:
        print(f"No scores provided. Usage: "
              f"python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        print(f"Scores processed: {new_list}")
        print(f"Total players: {len(new_list)}")
        print(f"Total score: {sum(new_list)}")
        print(f"Average score: {sum(new_list) / len(new_list)}")
        print(f"High score: {max(new_list)}")
        print(f"Low score: {min(new_list)}")
        print(f"Score range: {max(new_list) - min(new_list)}")


if __name__ == "__main__":
    main()
