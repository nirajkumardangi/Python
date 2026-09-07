class Wallet : 
    def __init__(self) : 
        # private attribute
        self.__balance = 0 

    # private method
    def __validate(self, amount) : 
        if amount < 0 : 
            raise ValueError('Amount must be positive') 

    def deposit(self, amount) : 
        self.__validate(amount) 
        self.__balance += amount 

    def withdraw(self, amount) : 
        self.__validate(amount) 
        if amount > self.__balance : 
            raise ValueError('Insufficient funds') 
        self.__balance -= amount 

    def get_balance(self) : 
        return self.__balance

acct_one = Wallet() 
acct_one.deposit(3) 
print(acct_one.get_balance()) # Output: 3 
acct_one.deposit(50) 
print(acct_one.get_balance()) # Output: 53 

# this will generate error:
# acct_one.deposit(-4) # ValueError: Amount must be positive 
# acct_one.withdraw(-8) # ValueError: Amount must be positive 
# acct_one.withdraw(58) # ValueError: Insufficient funds



"""
Getters and Setters Methods
"""

class Circle : 
    def __init__ ( self , radius ) : 
        self.radius = radius 

    # getter method
    @property 
    def radius ( self ) : 
        return self._radius 

    # setter method
    @radius.setter 
    def radius ( self , value ) : 
        if value <= 0 : 
            raise ValueError ( "Radius must be positive" ) 
        self._radius = value 

    # deleter method
    @radius.deleter 
    def radius ( self ) : 
        print ( "Deleting radius..." ) 
        del self._radius 

# Usage:
my_circle = Circle ( 33 ) 
print ( "Initial radius:" , my_circle.radius ) # 33 

del my_circle.radius # Triggers deleter -> prints "Deleting radius..."
print ( "Radius deleted!" ) # Radius deleted!