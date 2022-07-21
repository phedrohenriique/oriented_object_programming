class Film:

    def __init__(self, year, title, theme):
        self.year = year
        self.title = title
        self.theme = theme
        self._budget_min = 100000
        self._budget_max = 500000

        pass

    def _budget_average(self):
        budget = 0
        if self.year < 2000:
            budget = self._budget_min
        else:
            budget = self._budget_max 
        
        print(budget)

    def film_ads(self):
        pass
    

if __name__ == "__main__":

    obj = Film(2010, "Test", "action")
    print(obj.theme)
    obj.budget_average()

    pass