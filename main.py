import random


class TinyIdiot:
    def __init__(self, name):
        self.name = name
        self.vibes = 10
        self.beans = 0
        self.age = 0
        self.luck = random.randint(1, 10)
        self.resilience = random.randint(1, 10)
        self.greed = random.randint(1, 10)
        self.drama = random.randint(1, 10)

    def live_one_day(self):
        self.age += 1

        bean_chance = 0.3 + (self.luck * 0.04)

        if random.random() < bean_chance:
            beans_found = 1

            if random.random() < (self.greed / 20):
                beans_found += 1

            self.beans += beans_found
            self.vibes += 2

            print(f"{self.name} found {beans_found} bean(s). Vibes: {self.vibes}. Beans: {self.beans}.")
        else:
            vibe_loss = max(1, 5 - (self.resilience // 2))
            vibe_loss += self.drama // 5
            self.vibes -= vibe_loss

            print(f"{self.name} perceived the horrors and lost {vibe_loss} vibes. Vibes: {self.vibes}.")
        
        if self.drama >= 8 and random.random() < 0.15:
            self.vibes -= 2
            print(f"{self.name} dramatically overreacted to absolutely nothing. Vibes: {self.vibes}.")
    
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
    print(f"  Luck: {idiot.luck}, Resilience: {idiot.resilience}, Greed: {idiot.greed}, Drama: {idiot.drama}")


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