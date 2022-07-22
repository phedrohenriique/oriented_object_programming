class Film:

    x=10 ## variable used for all instances
    __budget_min = 100000 ## double underline makes the variable private, cant be used outside class
    __budget_max = 500000

    def __init__(self, year, title, theme):
        ## variables specific of each instance
        self.year = year
        self.title = title
        self.theme = theme
        self.film_created() ## everytime the object is instantiated it runs the function inside __init__

        pass

    def budget_average(self):
        budget = 0
        if self.year < 2000:
            budget = self.__budget_min
        else:
            budget = self.__budget_max 
        
        print(budget)

    def printer(self, text):
        print(text)
    
    def film_created(self):
        print("instance created")
        self.__private_method()

    def __private_method(self):
        print("private")

    def film_ads(self):
       self.theme = "ads"
       print(self.x) ## global variables in the scope shall be referenced with self.
       self.printer("im using another method") ## every method shall be referenced with self.
        
    

if __name__ == "__main__":

    obj = Film(2010, "Test", "action")
    #print(obj.theme, obj._budget_max)
    obj.budget_average()
    #obj.film_ads()
    #print(obj.theme)
    print(obj.x)
    ## print(obj.__budget_max)
    obj.__private_method()
    
    pass