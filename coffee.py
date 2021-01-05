class CoffeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        while True:
           self.action()

    def action(self):
        self.user_choice = input("Write action (buy, fill, take, remaining, exit): ").lower().strip()
        if self.user_choice == "buy":
            self.buy()
        elif self.user_choice == "fill":
            self.fill()
        elif self.user_choice == "take":
            self.take()
        elif self.user_choice == "remaining":
            self.remaining()
        elif self.user_choice == "exit":
            exit()
        else:
            print("Invalid input, please try again...")

    def reduced_supplies(self):
        self.water -= self.taken_supp[0]
        self.milk -= self.taken_supp[1]
        self.beans -= self.taken_supp[2]
        self.cups -= self.taken_supp[3]
        self.money += self.taken_supp[4]

    def check_resources(self):
        self.missing = ""

        if self.water - self.taken_supp[0] < 0:
            self.missing = "water"
        elif self.milk - self.taken_supp[1] < 0:
            self.missing = "milk"
        elif self.beans - self.taken_supp[2] < 0:
            self.missing = "beans"
        elif self.cups - self.taken_supp[3] < 0:
            self.missing = "cups"
        if self.missing != "":                        #...means something is missing
            print(f"Sorry, not enough {self.missing}!")
            return False
        else:                                         # if there is enough resources
            print("I have enough resources, making you a coffe!")
            return True

    def buy(self):
        self.coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if self.coffee_type == "1":
            self.taken_supp = [250, 0, 16, 1, 4]
            if self.check_resources():
                self.reduced_supplies()
        elif self.coffee_type == "2":
            self.taken_supp = [350, 75, 20, 1, 7]
            if self.check_resources():
                self.reduced_supplies()
        elif self.coffee_type == "3":
            self.taken_supp = [200, 100, 12, 1, 6]
            if self.check_resources():
                self.reduced_supplies()
        elif self.coffee_type == "back":
            self.action()
        else:
            print("Invalid input, try again!")
            self.buy()

    def fill(self):
        self.water_fill = int(input("Write how many ml of water do you want to add:"))
        self.water += self.water_fill
        self.milk_fill = int(input("Write how many ml of milk do you want to add: "))
        self.milk += self.milk_fill
        self.beans_fill = int(input("Write how many grams of coffee beans do you want to add: "))
        self.beans += self.beans_fill
        self.cup_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups += self.cup_fill

    def take(self):
        print(f"I gave you {self.money}$")
        self.money -= self.money

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} USD")

my_coffee = CoffeMachine()
