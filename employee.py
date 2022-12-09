"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class contractType(enumerate):
    salary = 1
    contract = 2

class CommissionType(enumerate):
    noCommission = 1
    bonus = 2
    contract = 3

class Employee:
    def __init__(self, name, contract, commission, numberOfContracts, ratePerContract, hours, rate, bonus):
        self.name = name
        self.contract = contract
        self.commission = commission 
        self.numberOfContracts = numberOfContracts
        self.ratePerContract = ratePerContract 
        self.hours = hours
        self.rate = rate
        self.bonus = bonus

    def get_pay(self):
        if(self.contract == contractType.salary and self.commission == CommissionType.noCommission):
            return int(self.rate)
        if(self.contract == contractType.contract and self.commission == CommissionType.noCommission):
            return int(self.hours * self.rate)
        if(self.contract == contractType.salary and self.commission == CommissionType.contract):
            return int(self.rate + self.numberOfContracts * self.ratePerContract)
        if(self.contract == contractType.contract and self.commission == CommissionType.contract):
            return int(self.rate * self.hours + self.numberOfContracts * self.ratePerContract)
        if(self.contract == contractType.salary and self.commission == CommissionType.bonus):
            return int(self.rate + self.bonus)
        if(self.contract == contractType.contract and self.commission == CommissionType.bonus):
            return int(self.rate * self.hours + self.bonus)

    def __str__(self):
        if(self.contract == contractType.salary and self.commission == CommissionType.noCommission):
            return f'{self.name} works on a monthly salary of {self.rate}. Their total pay is {self.get_pay()}.'
        if(self.contract == contractType.contract and self.commission == CommissionType.noCommission):
            return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.get_pay()}.'
        if(self.contract == contractType.salary and self.commission == CommissionType.contract):
            return f'{self.name} works on a monthly salary of {self.rate} and receives a commission for {self.numberOfContracts} contract(s) at {self.ratePerContract}/contract. Their total pay is {self.get_pay()}.'
        if(self.contract == contractType.contract and self.commission == CommissionType.contract):
            return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.numberOfContracts} contract(s) at {self.ratePerContract}/contract. Their total pay is {self.get_pay()}.'
        if(self.contract == contractType.salary and self.commission == CommissionType.bonus):
            return f'{self.name} works on a monthly salary of {self.rate} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}.'
        if(self.contract == contractType.contract and self.commission == CommissionType.bonus):
            return f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contractType.salary,CommissionType.noCommission,0,0,0,4000,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.s

charlie = Employee('Charlie', contractType.contract, CommissionType.noCommission, 0, 0, 100, 25, 0)

# # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contractType.salary, CommissionType.contract, 4, 200, 0, 3000, 0)

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contractType.contract, CommissionType.contract, 3,220,150,25,0 )

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.

robbie = Employee('Robbie', contractType.salary, CommissionType.bonus, 0, 0, 0, 2000, 1500)

# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contractType.contract, CommissionType.bonus, 0, 0, 120, 30,600 )