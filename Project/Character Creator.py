class Character:
    name = "Riza"
    phrase = "It's a me, Riza!"
    level = 1
    health = 100

    def greet(self):
        print(self.phrase)

    def level_up(self):
        self.level += 1
        print("Leveled up to", self.level)

    def dec_health(self):
        print("Health decreased from", self.health)
        self.health -= 10
        print("to", self.health)

Riza = Character()
Riza.greet()
Riza.level_up()
Riza.dec_health()
