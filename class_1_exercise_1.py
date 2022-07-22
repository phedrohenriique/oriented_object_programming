
class FirstClass:
    def __init__(self, *args, **kargs):
        self.attribute_one = kargs.get("attribute_one", '')

    def first_class(self):
        print("first class method")



obj = FirstClass(attribute_one=10)

if __name__ == "__main__" :
    print("inside executed code :")

    print(obj.attribute_one)
    obj.first_class()