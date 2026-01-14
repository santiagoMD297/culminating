class Backpack:
    def __init__(self, cap: int):
        """
        Initialize a new Backpack.

        Parameters:
            cap (int): The maximum number of non-rupee items
                       the backpack can hold (arrows, shields, etc.).
                       Rupees do NOT count toward this capacity.
        """
        # The items dictionary.
        # The "arrow" and "rupee" dictionaries should never be deleted.
        self.items = {
            "arrow": {"quantity": 0, "max": 20},
            "rupee": {"quantity": 0, "max": 500},
        }

        # Overall capacity for non-rupee items.
        self.capacity = cap

    def is_valid(self, name: str) -> bool:
        """
        Check whether an item name is valid.

        A valid item name:
            - Starts with a lowercase letter
            - Contains only lowercase letters, digits, or underscores
            - Has length at least 3

        Returns:
            True if the name is valid, False otherwise.
        """
        # At least 3 characters
        if len(name) < 3:
            return False

        # First character must be a lowercase letter
        first = name[0]
        if not ("a" <= first <= "z"):
            return False

        # All characters must be lowercase letters, digits, or underscores
        for ch in name:
            if ("a" <= ch <= "z") or ("0" <= ch <= "9") or ch == "_":
                continue
            return False

        return True

    def _add(self, dictionary: dict, item: str, capacity: int):
        """
        Internal helper method that does the real 'work' of adding an item.

        Parameters:
            dictionary (dict): The dictionary that stores item data.
                               (In this case, usually self.items.)
            item (str): The name of the item to add.
            capacity (int): The maximum number of non-rupee items allowed.

        This method:
            - Checks capacity using count()
            - Adds 1 to the item's quantity if there is room
            - Respects the 'max' value if it exists for that item
              (e.g., arrows and rupees)
        """
        # Only add if we are under capacity for non-rupee items
        if capacity > self.count():
            print("adding")

            if item in dictionary:
                # If item has a "max", respect it; otherwise treat as unlimited
                current_qty = dictionary[item]["quantity"]
                item_max = dictionary[item].get("max", float("inf"))

                if current_qty < item_max:
                    dictionary[item]["quantity"] += 1
            else:
                # New item starts at quantity 1
                dictionary[item] = {"quantity": 1}

    def add(self, item: str):
        """
        Public method to add one of an item to the backpack.

        Parameters:
            item (str): The name of the item to add.

        This method calls the internal helper _add(), which does the
        actual logic. This keeps add() simple and re-usable.
        """
        self._add(self.items, item, self.capacity)

    def remove(self, item: str):
        """
        Remove one of the given item from the backpack, if it exists.

        If the quantity of a removable item reaches 0:
            - If it's NOT 'rupee' or 'arrow', delete it from the dictionary.
            - If it IS 'rupee' or 'arrow', keep it with quantity 0.
        """
        if item in self.items:
            self.items[item]["quantity"] -= 1

            if self.items[item]["quantity"] == 0:

                if item not in ["rupee", "arrow"]:
                    del self.items[item]

    def count(self) -> int:
        """
        Return the total number of NON-rupee items in the backpack.

        This version uses RECURSION instead of a loop.
        Rupees are ignored when counting.
        """
        keys = list(self.items.keys())

        def helper(index: int) -> int:
            # Base case: no more keys to process
            if index == len(keys):
                return 0

            key = keys[index]

            # Skip rupees
            if key == "rupee":
                return helper(index + 1)

            # Count this item's quantity + the rest
            return self.items[key]["quantity"] + helper(index + 1)

        return helper(0)


# Example usage (you can keep or remove this in your final file)
if __name__ == "__main__":
    b = Backpack(10)

    b.add("arrow")
    b.add("arrow")

    for i in range(600):
        b.add("rupee")
    b.add("shield")

    print(b.items)
    print(b.count())
    b.remove("shield")
    print(b.items)