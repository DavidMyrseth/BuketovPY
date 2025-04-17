import random
import time

class Player:
    def __init__(self, hp, energy, food):
        self.hp = hp
        self.energy = energy
        self.food = food
        self.alive = True

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("Sa puhkasid. Energia taastatud (+3)")
        else:
            print("Pole piisavalt toitu!")

    def move(self):
        if self.energy > 0:
            self.energy -= 2
            print("Sa liikusid edasi. Energia vähenes (-2).")
            self.random_event()
        else:
            print("Pole piisavalt energiat liikumiseks!")

    def random_event(self):
        event = random.choice(["nothing", "food", "trap", "heal"])
        if event == "nothing":
            print("Midagi ei juhtunud.")
        elif event == "food":
            found = random.randint(1, 2)
            self.food += found
            print(f"Leidsid {found} toiduvaru!")
        elif event == "trap":
            damage = random.randint(2, 5)
            self.hp -= damage
            print(f"Jäid lõksu! Kaotasid {damage} HP.")
        elif event == "heal":
            heal = random.randint(1, 4)
            self.hp += heal
            print(f"Leidsid ravimikomplekti! HP taastatud (+{heal})")

        if self.hp <= 0:
            self.alive = False
            print("Said surma... Mäng läbi.")

    def status(self, day, max_days):
        print(f"\n Päev {day}/{max_days}")
        print(f" HP: {self.hp}, Energia: {self.energy}, Toit: {self.food}")

# 🕹️ Mängu algus
def game_loop():
    player = Player(hp=10, energy=5, food=3)
    total_days = 7
    current_day = 1

    print("🎮 Tere tulemast ellujäämismängu: Sundöö")
    print("Eesmärk: Ela üle 7 päeva, hallates ressursse ja vältides ohte!\n")

    while player.alive and current_day <= total_days:
        player.status(current_day, total_days)
        print("\nValikud:")
        print("1. Puhka (taastab energiat, kulutab toitu)")
        print("2. Liigu edasi (kulutab energiat, võib esineda sündmus)")
        print("3. Jäta päev vahele")

        choice = input("Sinu valik (1-3): ")

        if choice == "1":
            player.rest()
        elif choice == "2":
            player.move()
        elif choice == "3":
            print("Otsustasid päeva vahele jätta.")
        else:
            print("Vigane valik!")

        current_day += 1
        time.sleep(1)

    if player.alive:
        print("\n🎉 Palju õnne! Elasid Sundöö üle!")
    else:
        print("\n☠️ Kahjuks sa ei ellu jäänud.")

# Käivita mäng
if __name__ == "__main__":
    game_loop()
