## Bank 

class Account:
    
    name = ''
    cpf = ''
    password = ''
    __balance = 0
    __investments = 0


    def __init__(self, name, cpf, password, **kwargs):
        print("account created")
        self.name = name
        self.cpf = cpf
        self.__password = password
        

    def account_deposit(self, value):
        self.__balance = self.__balance + value
        print(f" {value} deposited in account")

    def account_withdraw(self, value, password):
        if(password == self.__password):
            self.__balance = self.__balance - value
            print(f" {value} was taken from account")
        else:
            print("authentication invalid")
                
    def account_balance(self,  password):
        if ( password == self.__password):
            print(f"balance is {self.__balance} ")
        else:
            print("authentication invalid")

    def account_investments(self, value=0):
        if (value != 0):
            self.__investments = self.__investments + value
            print(f"total investments : {self.__investments} ")
        else:
            print(f"total investments : {self.__investments}")



if __name__ == "__main__":
    print("script running")

    account_1 = Account("pedro", "000", "123")
    account_1.account_deposit(100)

    account_2 = Account("henrique", "000", "123")
    account_2.account_deposit(200)
    account_2.account_balance("123")