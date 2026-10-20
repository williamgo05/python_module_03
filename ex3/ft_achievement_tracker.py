import random


def gen_player_achievements(achievements: list) -> set:

    quantity = random.randint(4, 6)
    player_achievements = set(random.sample(achievements, quantity))
    return (player_achievements)


def main() -> None:

    achievements = [
        "First Step",
        "Code Master",
        "Python Pro",
        "Linux User",
        "Problem Solver",
        "Fast Learner",
        "Project Builder",
        "Git Expert",
        "Algorithm Pro",
        "Top Performer"
    ]

    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements(achievements)
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements(achievements)
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements(achievements)
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements(achievements)
    print(f"Player Dylan: {dylan}")

    print(f"\nAll distinct achievements: {alice.union(bob, charlie, dylan)}")

    print(f"\nCommon achievements: {alice.intersection(bob, charlie, dylan)}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")

    all_achievements = set(achievements)

    print(f"\nAlice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
