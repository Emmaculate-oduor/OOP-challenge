class Pet:

    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} ate some delicious food.")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} had a peaceful nap.")

    def age(self):
        self.energy = min(self.energy +5, 20)
        print(f"{self.name} is aging")

    def play(self):
        if self.energy >=2:
            self.energy -=2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger +1, 10)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play")

    def train(self, tricks):
        self.tricks.append(tricks)
        self.happiness = max(self.happiness - 1, 0)
        self.energy = max(self.energy - 2, 0)
        print(f"{self.name} learned a new trick: {tricks}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '. join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any trick yet")

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")