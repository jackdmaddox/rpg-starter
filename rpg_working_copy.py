class Character:
    
    
    def __init__(self, health, power, character_name):
        self.health = health
        self.power = power
        self.character_name = character_name

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to {}. " .format(self.character_name, self.power, enemy.character_name))
        if hero.health <= 0:
            print("You are dead.")
        elif goblin.health <= 0:
            print("The goblin is dead.")

class Zombie(Character):

    def print_status(self):
        print("The zombie has {} health and {} power".format(self.health, self.power))

class Hero(Character):

    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    # def attack(self, enemy):
    #     goblin.health -= hero.power
    #     print("You do %d damage to the goblin." % hero.power)
    #     if goblin.health <= 0:
    #         print("The goblin is dead.")

    # def alive(self):
    #     return self.health > 0

    def print_status(self):
        print("You have {} health and {} power".format(self.health, self.power))

class Goblin(Character):

    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    # def attack(self, enemy):
    #     hero.health -= goblin.power
    #     print("The goblin does %d damage to you." % goblin.power)
    #     if hero.health <= 0:
    #         print("You are dead.")

    # def alive(self):
    #     return self.health > 0

    def print_status(self):
        print("The goblin has {} health and {} power".format(self.health, self.power))


hero = Hero(10, 5, "hero")
goblin = Goblin(6,2, "goblin")
zombie = Zombie(9,1, "zombie")



def main():

    #while goblin.alive() andnhero.alive():
    while hero.alive():
        hero.print_status()
        #goblin.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
            # Goblin attacks hero
        zombie.attack(hero)

        # if goblin.health > 0:
        #     # Goblin attacks hero
        #     goblin.attack(hero)

main()
