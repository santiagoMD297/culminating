class TrainCar:
    def __init__(self, animal):
        self.animal = animal
        self.next = None
        self.prev = None


class Train:
    def __init__(self):
        self.engine = None   # front (head)
        self.caboose = None  # back (tail)

    def add_front(self, animal):
        """Add a new TrainCar with the given animal to the front of the train."""
        new_car = TrainCar(animal)

        # If the train is empty
        if self.engine is None:
            self.engine = new_car
            self.caboose = new_car
        else:
            # Link new car in front of current engine
            new_car.next = self.engine
            self.engine.prev = new_car
            self.engine = new_car

    def add_back(self, animal):
        """Add a new TrainCar with the given animal to the back of the train."""
        new_car = TrainCar(animal)

        # If the train is empty
        if self.caboose is None:
            self.engine = new_car
            self.caboose = new_car
        else:
            # Link new car after current caboose
            new_car.prev = self.caboose
            self.caboose.next = new_car
            self.caboose = new_car

    def remove(self, animal):
        """Remove the first TrainCar that contains the given animal."""
        current = self.engine

        # Find first car with this animal
        while current is not None and current.animal != animal:
            current = current.next

        # Not found -> do nothing
        if current is None:
            return

        # If it's the only car
        if current is self.engine and current is self.caboose:
            self.engine = None
            self.caboose = None
        # If it's the engine (front)
        elif current is self.engine:
            self.engine = current.next
            if self.engine is not None:
                self.engine.prev = None
        # If it's the caboose (back)
        elif current is self.caboose:
            self.caboose = current.prev
            if self.caboose is not None:
                self.caboose.next = None
        else:
            # Middle car: bypass it
            current.prev.next = current.next
            current.next.prev = current.prev

    def display_forward(self):
        """Return a list of animal names from front to back."""
        animals = []
        current = self.engine
        while current is not None:
            animals.append(current.animal)
            current = current.next
        return animals

    def display_backward(self):
        """Return a list of animal names from back to front."""
        animals = []
        current = self.caboose
        while current is not None:
            animals.append(current.animal)
            current = current.prev
        return animals

    def __len__(self):
        """Return the number of TrainCars in the Train."""
        count = 0
        current = self.engine
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        """Return a string representation of the train in order."""
        # Example: "lion -> zebra -> cobra"
        return " -> ".join(self.display_forward())

    def __getitem__(self, index):
        """Return the animal at the given index. Raise IndexError if invalid."""
        if index < 0:
            raise IndexError("Negative indexes are not supported")

        current = self.engine
        current_index = 0

        while current is not None and current_index < index:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError("Train index out of range")

        return current.animal

    def __add__(self, other):
        """Return a new Train containing the cars from self followed by other."""
        new_train = Train()

        # Add all animals from self
        current = self.engine
        while current is not None:
            new_train.add_back(current.animal)
            current = current.next

        # Add all animals from other
        current = other.engine
        while current is not None:
            new_train.add_back(current.animal)
            current = current.next

        return new_train