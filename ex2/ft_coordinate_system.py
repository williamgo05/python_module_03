import math


def get_player_pos() -> tuple:
    while True:

        coordinates = input("Enter new coordinates as "
                            "floats in format 'x,y,z': ")
        current = ""
        values = []
        size = 1

        for char in coordinates:
            if char == ',':
                values.append(current)
                current = ""
                size += 1
            else:
                current += char

        values.append(current)

        if size != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(values[0])
        except ValueError as e:
            print(f"Error on parameter '{values[0]}': {e}")
            continue

        try:
            y = float(values[1])
        except ValueError as e:
            print(f"Error on parameter '{values[1]}': {e}")
            continue

        try:
            z = float(values[2])
        except ValueError as e:
            print(f"Error on parameter '{values[2]}': {e}")
            continue

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {distance:.4f}\n")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    distance = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    main()
