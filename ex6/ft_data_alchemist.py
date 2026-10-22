import random


def main() -> None:
    player_list = [
        "Will", "Lucas_m", "maria", "Lucas_c", "Vini", "aughost", "Joao"]

    capitalized = [player.capitalize() for player in player_list]

    upper = [player for player in player_list if player == player.capitalize()]

    new_dict = {player: random.randrange(1000) for player in capitalized}

    high_score = {player: value for player, value in new_dict.items() if
                  value > sum(new_dict.values()) / len(new_dict)}

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {player_list}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {upper}")
    print(f"Score dict: {new_dict}")
    print(f"Score average is {sum(new_dict.values()) / len(new_dict):.2f}")
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()
