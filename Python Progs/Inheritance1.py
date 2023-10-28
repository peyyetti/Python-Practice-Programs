class Human: 
    def __init__(self, teeth):  # 3. argument recieved which was passed in step 1
        self.eyes = 2
        self.__nose = 1
        self._hands = 2
        self.teeth = teeth

    def work(self):
        print("I can work ")

    def display(self):
        print(f"I have {self.__nose} nose, {self.eyes} eyes and {self.teeth} teeth")

    def get_num_teeth(self):                            #getter method
        print(f"Number of teeth are {self.teeth} and number of nose is {self.__nose} \n")

    def set_teeth(self, new_teeth):                     #setter method
        self.teeth=new_teeth
        print(f"New no of teeth are {self.teeth} \n")
    
class Male(Human):
    def __init__(self, teeth):     # 1.1 argument recieved by constructor of child class
        super().__init__(teeth)     # 2. argument to be passed to constructor of base constructor
        self.muscles = "Yes"
        print(f"How many muscles do you want? {self.muscles} \n")
        print(f"Hello I have {self.eyes} eyes and {self.teeth} teeth \n")

    def work(self):
        print("I can work as a male\n")

man1=Male(32)   # 1. passing argument here as constructor of child class called first

# man1.work()
# print(man1.__nose)             # not accessible to child class as the attribute is private 

# print(man1._hands)               # accessible to child class

man1.get_num_teeth()
man1.set_teeth(21)