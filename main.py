import random


class TinyIdiot:
    def __init__(self, name):
        self.name = name
        self.vibes = 10
        self.beans = 0
        self.age = 0

    def live_one_day(self):
        self.age += 1

        if random.random() < 0.5:
            self.beans += 1
            self.vibes += 2
            print(f"{self.name} found a bean. Vibes: {self.vibes}. Beans: {self.beans}.")
        else:
            self.vibes -= 3
            print(f"{self.name} perceived the horrors. Vibes: {self.vibes}.")

    def is_alive(self):
        return self.vibes > 0

    def reproduce(self):
        self.vibes -= 8
        baby_name = f"{self.name} Jr."
        print(f"{self.name} has committed unauthorized mitosis. {baby_name} enters the swamp.")
        return TinyIdiot(baby_name)


swamp = [
    TinyIdiot("Greg"),
    TinyIdiot("Susan"),
    TinyIdiot("Beanlord"),
    TinyIdiot("Fart Tuna Waffle Poop"),
    TinyIdiot("Kevin"),
    TinyIdiot("Mold Steve"),
    TinyIdiot("Soup"),
    TinyIdiot("Trash Oracle"),
    TinyIdiot("Linda"),
    TinyIdiot("Crumb"),
]

print("Tiny Idiots booting...")

for idiot in swamp:
    print(f"{idiot.name} has entered the swamp.")


for day in range(1, 21):
    print(f"\n--- Day {day} ---")

    for idiot in swamp:
        idiot.live_one_day()

    for idiot in swamp:
        if not idiot.is_alive():
            print(f"{idiot.name} has perished dramatically.")

    swamp = [idiot for idiot in swamp if idiot.is_alive()]

    babies = []

    for idiot in swamp:
        if idiot.vibes >= 16:
            babies.append(idiot.reproduce())

    swamp.extend(babies)

    total_beans = sum(idiot.beans for idiot in swamp)
    average_vibes = round(sum(idiot.vibes for idiot in swamp) / len(swamp), 2) if swamp else 0

    print("--- Dashboard ---")
    print(f"Population: {len(swamp)}")
    print(f"Total beans: {total_beans}")
    print(f"Average vibes: {average_vibes}")

    if len(swamp) == 0:
        print("The swamp has fallen silent.")
        break


print("\nSimulation complete.")