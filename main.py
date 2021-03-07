class Category :
  
  def __init__ (self, name) :
    self.name = name
    self.ledger = []
    
  def deposit (self, amount, description = '') :
    a = {"amount" : amount, "description" : description}
    self.ledger.append (a)
  
  def withdraw (self, amount, description = '') :
    if self.check_funds(amount) == True :
      b = {"amount" : -amount, "description" : description}
      self.ledger.append(b)
      return True
    else :
      return False
      
  def get_balance (self) :
    balance = 0
    for element in self.ledger :
      balance = balance + element['amount']
    return balance
  
  def transfer (self, amount, category) :
      if self.check_funds(amount) == True :
        a = 'Transfer to ' + category
        b = 'Transfer from ' + self.name
        self.withdraw(amount, a)
        self.deposit(amount, b)
        return True
      else :
        return False

  def check_funds (self,amount) :
    balance = 0
    for value in self.ledger :
      balance = balance + value['amount']
      if amount > balance :
        return False  
      else:
        return True
  
  def __str__(self) :
    balance = 0
    a = 30 - len(self.name)
    b = a / 2
    star = int(b) * '*'
    object = star + self.name + star + '\n'
    for i in self.ledger[0:-1] :
      object = object + f"{i['description'][0:23].ljust(23)}{format(i['amount'],'.2f').rjust(7)}" + '\n'
      balance = balance + i['amount']
    return object + f"{'Total: '}{format(balance,'.2f')}"

#empezamos con la otra parte del ejercicio
    
        
    

def create_spend_chart(categories):
  return 'Not yet created'

food = Category('food')
food.deposit(1000,'ingreso')
print(food.withdraw(45,'palomitas'))
print(food.withdraw(23,'helado'))
print(food.get_balance())
print(food.check_funds(500))
print(food.transfer(50,'clothingsssssssss'))
print(food)







#https://forum.freecodecamp.org/t/python-budget-app-test-get-balance-fail/408769
    