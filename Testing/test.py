class Cat:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self):
        print(f"{self.name}: Meow")


my_Cat = Cat(name="Franklin", color="orange", weight=12)

print(f"{my_Cat.name}, {my_Cat.color}, {my_Cat.weight}")

my_Cat.meow()


class monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} is dead!")


my_monster = monster(name="Ulamog", health=13)

my_monster.decrease_health(13)
print(f"{my_monster.name} has {my_monster.health} health...")


class star:
    def __init__(self):
        print("a star is born")


class Monster_2:
    def __init__(self, name, health):
        self.name = name
        self.health = health


star1 = star()

new_monster = Monster_2("Ghalta", 12)

print(f"monsters name is: {new_monster.name} and his health is: {new_monster.health}")
