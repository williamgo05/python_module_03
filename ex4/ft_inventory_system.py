import sys


def validate_quantity(arg: str) -> int:
    found = False
    quantity = ""
    for c in arg:
        if c == ':':
            found = True
            continue
        if found:
            quantity += c
    return int(quantity)


def validate_item(arg: str) -> str:
    current = ""
    item = ""

    for c in arg:
        if c == ':':
            item = current
            return item
        else:
            current += c
    return ""


def create_inventory() -> dict[str, int]:
    complete_inventory = {}

    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py item:quantity")

    for arg in sys.argv[1:]:

        signal_count = 0

        for c in arg:
            if c == ':':
                signal_count += 1

        if signal_count != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item = validate_item(arg)

        if not item:
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            quantity = validate_quantity(arg)
        except ValueError:
            print(f"Quantity error for '{item}'")
            continue

        if item in complete_inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        complete_inventory[item] = quantity
    return (complete_inventory)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = create_inventory()
    print(inventory)
    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if total_quantity > 0:
        for item in inventory.keys():
            percentage = round(inventory[item] / total_quantity * 100, 1)
            print(f"Item {item} represents {percentage}%")

    if inventory:
        most_item = list(inventory.keys())[0]
        least_item = list(inventory.keys())[0]

        for item in inventory.keys():
            if inventory[item] > inventory[most_item]:
                most_item = item
            if inventory[item] < inventory[least_item]:
                least_item = item

        print(f"Item most abundant: {most_item} "
              f"with quantity {inventory[most_item]}")
        print(f"Item least abundant: {least_item} "
              f"with quantity {inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
