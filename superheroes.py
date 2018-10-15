import random

class Ability:
    def __init__(self, name, attack_strength):
        #Set ability name
        self.name = name
        #Set attack strength
        self.attack_strength = attack_strength
    def attack(self):
        #Return attack value
        lowestVal = (int(self.attack_strength))//2
        randoVal = random.randint(int(lowestVal), int(self.attack_strength))
        return randoVal
    def update_attack(self, attack_strength):
        #Update attack value
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        randoVal = random.randint(0, int(self.attack_strength))
        return randoVal

class Armor:
    def __init__(self, name, defense):
        #Instantiate name and defense strength!
        self.name = name
        self.defense = defense
    def defend(self):
        #Return a random value between 0 and the initialized defense strength.
        trulyRando = random.randint(0, int(self.defense))
        return trulyRando

class Hero:
    def __init__(self, name, health=100): #default value of 100 - optional when instantiating Hero class.
        #Initialize starting values
        self.abilities = list()
        self.name = name
        self.armors = list() #All variables starting from here were added on pg 4
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
    def defend(self): #Added pg 4
        #This method should run the defend method on each piece of armor and calculate the total defense.
        #If the hero's health is 0, the hero is out of play and should return 0 defense points
        total_defense = 0
        if len(self.armors) > 0 and self.health > 0:
            for piece in self.armors:
                total_defense += piece.defend()
        return total_defense #This isn't indented more bc it MUST return even if self.armors !> 0
    def take_damage(self, damage_amt): #Added pg 4
        #This method should subtract the damage amount from the hero's health
        #If the hero dies, update number of deaths
        self.health += damage_amt
        if self.health <= 0:
            self.deaths += 1
            return 1
        return 0
    def add_armor(self, armor):
        self.armors.append(armor)
    def add_kill(self, num_kills): #Added pg 4
        #This method should add the number of kills to self.kills
        # print(self.kills, num_kills) #small print test function
        self.kills += num_kills
    def add_ability(self, ability):
        #Add ability to abilities list
        self.abilities.append(ability)
    def attack(self):
        #Run attack() on every ability hero has
        #Add up and return the total of all attacks
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack #This isn't indented more bc it MUST return even if self.armors !> 0

class Team:
    def __init__(self, team_name):
        #Instantiate resources.
        self.name = team_name
        self.heroes = list()
        self.total_kills = 0
        self.dead_heroes = 0
    def add_hero(self, Hero):
        #Add Hero object to heroes list
        self.heroes.append(Hero)
    def total_health(self):
        health_val = 0
        for hero in self.heroes:
            health_val += hero.health
        return health_val
    def remove_hero(self, name):
        #Remove hero from heroes list. If Hero is not found, return 0.
        if self.heroes != []:
            for hero in self.heroes:
                if name in hero.name:
                    self.heroes.remove(hero)
                else:
                    return 0
        else:
            return 0
    def find_hero(self, name):
        #Find and return hero from heroes list. If hero isn't found return 0.
        if self.heroes != []:
            for hero in self.heroes:
                if name in hero.name:
                    return hero
                else:
                    return 0
        else:
            return 0
    def view_all_heroes(self):
        #Print out all heroes to the console.
        for hero in self.heroes:
            name = hero.name
            print (name)
    def attack(self, other_team):
        #This method should total our teams attack strength and call the defend() method on the rival team that is passed in
        #It should call add_kill() on each hero with the number of kills made
        total_attack = 0
        for hero in self.heroes:
            total_attack += hero.attack()
        slain_foes = other_team.defend(total_attack)
        for hero in self.heroes:
            hero.add_kill(slain_foes)
        return total_attack
    def defend(self, damage_amt):
        #This method should calculate our team's total defense
        #Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method
        #Return number of heroes killed in attacks
        slain_foes = 0
        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()
        if damage_amt > total_defense:
            self.deal_damage(total_defense - damage_amt)
        for hero in self.heroes:
            if hero.deaths > 0:
                slain_foes+=1
                self.dead_heroes += 1
        return slain_foes
    def deal_damage(self, damage):
        #Divide the total damage amongst all heroes
        #Return the number of heroes that died in attack
        dead_hero_counter = 0
        damage_per_hero = damage // len(self.heroes)
        for hero in self.heroes:
            if hero.health > 0:
                if damage_per_hero >= hero.health:
                    dead_hero_counter += 1
                    hero.take_damage(damage_per_hero)
                else:
                    hero.take_damage(damage_per_hero)
        return dead_hero_counter
    def revive_heroes(self, health=100):
        #This method should reset all heroes health to their original starting value
        for hero in self.heroes:
            hero.health = hero.start_health
    def stats(self):
        #This method should print the ratio of kills/deaths for each member of the team to the screen
        #This data must be output to the terminal
        heroic_stats = []
        for hero in self.heroes:
            if hero.deaths > 0:
                kd_ratio = hero.kills // hero.deaths
                heroic_stats.append(("The kills/deaths ratio of " + str(hero.name) + " was: " + str(kd_ratio)))
            else:
                heroic_stats.append(("Our hero " + str(hero.name) + " made " + str(hero.kills) + " kills and was never slain."))
        return heroic_stats
        print (heroic_stats)
    def update_kills(self):
        #This method should update each hero when there is a team kill
        for hero in self.heroes:
            self.total_kills += hero.kills
        return self.total_kills

class Arena:
    def __init__(self, team_size):
        self.team_size = team_size
        self.team_one = None
        self.team_two = None
    def build_team_one(self):
        # This method should allow a user to build team one
        demigod = ""
        power = ""
        protection = ""
        self.team_one = Team(input("Let's give a name to Team One: "))
        for i in range(self.team_size):
            demigod = Hero(input("Give your hero a name: "))
            self.team_one.add_hero(demigod)
            # Power time
            print ("Your hero has superpowers. When you have entered all the superpowers you want, just type 'y' when asked if you're 'DONE?'.")
            usersays = None
            while (usersays != "y"):
                power = Ability(input("Enter a name for a superpower: "), input("Enter an integer from 1-100 to calculate the superpower's strength: "))
                demigod.add_ability(power)
                usersays = input("DONE? If yes, type 'y'; if not, press enter ")
            # Weapon time
            print ("Your hero has weapons, too! Let's go equip them.")
            usersays = None
            while (usersays != "y"):
                sidearm = Weapon(input("Enter a name for the weapon: "), input("Enter an integer from 1-100 to calculate the weapon's strength: "))
                demigod.add_ability(sidearm)
                usersays = input("DONE? If yes, type 'y'; if not, press enter ")
            # Armor time
            print ("Your hero has armor for protection. Time to garb up.")
            usersays = None
            while (usersays != "y"):
                protection = Armor(input("Enter a name for the armor: "), input("Enter an integer from 1-100 to calculate the armor's strength: "))
                demigod.add_armor(protection)
                usersays = input("DONE? If yes, type 'y'; if not, press enter ")
    def build_team_two(self):
        # This method should allow a user to build team one
        demigod = ""
        power = ""
        protection = ""
        self.team_two = Team(input("Let's give a name to Team Two: "))
        for i in range(self.team_size):
            demigod = Hero(input("Give your hero a name: "))
            self.team_two.add_hero(demigod)
            # Power time
            print ("Your hero has superpowers. When you have entered all the superpowers you want, just type 'y' when asked if you're 'DONE?'.")
            usersays = None
            while (usersays != "y"):
                power = Ability(input("Enter a name for a superpower: "), input("Enter an integer from 1-100 to calculate the superpower's strength: "))
                demigod.add_ability(power)
                usersays = input("DONE? If yes, type 'y'; if not, press enter ")
            # Weapon time
            print ("Your hero has weapons. When you have entered all the weapons you want, type DONE in all caps.")
            usersays = None
            while (usersays != "y"):
                sidearm = Weapon(input("Enter a name for the weapon: "), input("Enter an integer from 1-100 to calculate the weapon's strength: "))
                demigod.add_ability(sidearm)
                usersays = input("DONE? If yes, type 'y'; if not, press enter ")
            # Armor time
            print ("Your hero has armor. When you have entered all the armor you want, type DONE in all caps.")
            usersays = None
            while (usersays != "y"):
                protection = Armor(input("Enter a name for the armor: "), input("Enter an integer from 1-100 to calculate the armor's strength: "))
                demigod.add_armor(protection)
                usersays = input("DONE? If yes, type 'y'; if not, press enter ")
    def team_battle(self):
        # This method should continue to battle teams until one or both teams are dead. Oh my
        # Something is wrong here
        while (self.team_one.total_health() > 0 or self.team_one.total_health() > 0):
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
    def show_stats(self):
        print("Stats!")
        # This method should print out the battle stats, including ea. hero's kill/death ratio
        print("How did Team One perform? Let's see: ")
        print(self.team_one.stats())
        print("How did Team Two perform? Let's see: ")
        print(self.team_two.stats())

fightTime = Arena(int(input("How many members do you want on each team? ")))
fightTime.build_team_one()
fightTime.build_team_two()
fightTime.team_battle()
fightTime.show_stats()
