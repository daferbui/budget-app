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
        a = 'Transfer to ' + category #aqui el hace category.name
        b = 'Transfer from ' + self.name
        self.withdraw(amount, a)
        self.deposit(amount, b)
        return True
      else :
        return False

  def check_funds (self,amount) :
    balance = 0
    for value in self.ledger :
      #chequeamos los fondos que tenemos
      balance = balance + value['amount']
      if amount > balance :
        return False  
      else:
        return True
  
  def imprimir (self,name) :
    for i in self.ledger:
      amount = i['amount']
      description = i['description']
      #alinear los resultados a la derecha en 30 espacios
      #alinear las descriptiones a la izquierda.
      #añadir que si en la lista está Transfer from que siga
      #añadir el total
        
    

def create_spend_chart(categories):
  return 'Not yet created'

food = Category('food')
food.deposit(1000,'ingreso')
print(food.withdraw(45,'palomitas'))
print(food.withdraw(23,'helado'))
print(food.get_balance())
print(food.check_funds(500))
print(food.transfer(50,'clothing'))






#https://forum.freecodecamp.org/t/python-budget-app-test-get-balance-fail/408769