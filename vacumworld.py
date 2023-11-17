import random
class VacuumCleaner:
    def __init__(self):
        self.location = random.choice(['A', 'B'])
        self.performance = 0

    def clean(self):
        print(f"Vacuum cleaner is in room {self.location}.")

        if self.location == 'A':
            dirt = random.choice([True, False])
            if dirt:
                print("There is dirt in room A. Cleaning...")
                self.performance += 1
            else:
                print("Room A is clean.")
        else:
            dirt = random.choice([True, False])
            if dirt:
                print("There is dirt in room B. Cleaning...")
                self.performance += 1
            else:
                print("Room B is clean.")

    def move(self):
        print("Moving to the other room.")
        self.location = 'A' if self.location == 'B' else 'B'
        self.performance += 1

    def run(self, steps):
        for _ in range(steps):
            self.clean()
            self.move()

        print(f"Cleaning performance: {self.performance}")

if __name__ == "__main__":
    vacuum = VacuumCleaner()
    steps = 5  # You can change the number of steps as needed
    vacuum.run(steps)
