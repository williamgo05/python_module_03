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
	raise ValueError(f"Error - invalid parameter '{arg}'")


def create_inventory() -> dict:
	complete_inventory = {}

	for arg in sys.argv[1:]:
		try:
			item = validate_item(arg)
		except ValueError as e:
			print(e)
			continue
		try:
			quantity = validate_quantity(arg)
		except ValueError as e:
			print(e)
			continue
		complete_inventory[item] = quantity

	return (complete_inventory)

def main() -> None:
	print("=== Inventory System Analysis ===")
	inventory = create_inventory()
	print(inventory)


if __name__ == "__main__":
	main()
