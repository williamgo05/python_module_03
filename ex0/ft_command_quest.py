import sys


def main() -> None:
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if argc > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}:", sys.argv[i])
            i += 1
    else:
        print("No arguments provided!")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
