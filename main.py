class Category :
  ledger = list()
  def __init__ (self, category) :
    self.category = category
    #self.ledger = []
  
  def deposit (self, amount, description = '') :
    a = {"amount" : amount, "description" : description}
    self.ledger.append (a)
    return self.ledger
    

  def withdraw (self, amount, description = '') :
    #determinamos si hay fondos utilizando la funcion creada
    #check funds
    self.check_funds(amount)
    if True :
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
  
  def transfer (self,amount,category) :
    #Entender esta función ya que dependerá del tipo de category del 
    #objeto, es decir no es solo introducirlo en la lista, sinó además
    #primero averiguar a que lista de que category hay que añadirlo?
    if self.check_funds(amount) == True :
      a = {"amount" : -amount, "Transfer to" : category}
      b = {"amount" : amount, "Transfer from" : category}
      self.ledger(a)
      self.ledger(b)
      return True
    else :
      return False
    
  
  def check_funds (self,amount) :
    balance = 0
    for value in self.ledger :
      #chequeamos los fondos que tenemos
      balance = balance + value['amount']
      if balance > amount :
        return True
      else:
        return False

    

def create_spend_chart(categories):
  return 'Not yet created'

chocolate = Category ('food')
peras = Category ('food')
print(peras.deposit(34.34,'Peras'))
print(chocolate.deposit(32,'Valor'))






#https://forum.freecodecamp.org/t/python-budget-app-test-get-balance-fail/408769