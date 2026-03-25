RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m" 

class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.energy = 5
        self.mood = "calm"
    
    def meow(self):
        print(f"{self.name} says: Meow!")

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            self.mood = "happy"
        elif self.energy == 0:
            print(f"{self.name} is too tired to play.")
        
        if self.energy == 0:
            self.mood = "tired"
            
    
    def sleep(self):
        self.energy += 2
        if self.energy > 10:
            self.energy = 10
        self.mood = "calm"


def status():
    print(f"{GREEN}Name: {cat1.name} Age: {cat1.age} Energy: {cat1.energy} Mood: {cat1.mood}{RESET}")
    print(f"{GREEN}Name: {cat2.name} Age: {cat2.age} Energy: {cat2.energy} Mood: {cat2.mood}{RESET}")
    print(f"{GREEN}Name: {cat3.name} Age: {cat3.age} Energy: {cat3.energy} Mood: {cat3.mood}{RESET}")

def test():
    print(f"{RED}There are 3 cats:{RESET}")
    status()
    print(f"{RED}Cats will meow:{RESET}")
    for i in range(2):
        cat1.meow()
    for i in range(3):
        cat2.meow()
    for i in range(4):
        cat3.meow()
    
    print(f"{RED}Cats will play:{RESET}")
    for i in range(3):
        cat2.play()
    for i in range(6):
        cat3.play()   
    print(f"{RED}{cat2.name} & {cat3.name} played 3 & 6 times (energy -1 per play):{RESET}")
    status()

    for i in range(5):
        cat2.sleep() 
    print(f"{RED}{cat2.name} slept 5 times (energy +2 per sleep):{RESET}")
    status()

cat1 = Cat("Kitty", 2)
cat2 = Cat("Hello", 3)
cat3 = Cat("Bobo", 4)
test()
