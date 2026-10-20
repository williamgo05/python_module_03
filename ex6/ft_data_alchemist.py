def main():
    players_list = ["Will", "LucasM", "maria", "LucasC", "Vini", "aughost"]
    capitalized_list = []
    no_capitalized_list = []
    for player in players_list:
        if player == player.capitalize():
            print(f"Player capitalized = {player}")
            capitalized_list.append(player)
        else:
            print(f"Player no capitalized = {player}")
            no_capitalized_list.append(player)
    print(f"Players_list = {players_list}")
    print(f"Capitalized_list = {capitalized_list}")
    print(f"no_Capitalized_list = {no_capitalized_list}")


if __name__ == "__main__":
    main()