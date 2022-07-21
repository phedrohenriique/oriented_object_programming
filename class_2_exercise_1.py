class Pen:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model", "")
        self.color = kwargs.get("color", "black")
        self.size = kwargs.get("size", 0.5)
        self.charge = kwargs.get("charge", 100)
        self.closed = kwargs.get("closed", True)

        pass

    def status(self):
        print(f"model : {self.model}")
        print(f"color : {self.color}")
        print(f"size : {self.size}")
        print(f"charge : {self.charge}")
        print(f"closed : {self.closed}")

    def open(self):
        self.closed = False
        pass

    def write(self, phrase=""):
        if(self.closed == False):
            print(phrase)
        else:
            print("the pen is not opened, open it first")
        pass
    
obj = Pen()

if __name__ == "__main__":
    obj.model = "Bic"
    obj.status()

    obj.open()
    obj.write("now i can write properly")

    pass