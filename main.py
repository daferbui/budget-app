class Category :
  ledger = list()
  def __init__ (self, category) :
    #repasar esto para que lo poniamos si abajo no hago referencia
    self.category = category
    #self.ledger = list ()
  
  def deposit (self, amount, description = '') :
    a = {"amount" : amount, "description" : description}
    self.ledger.append (a)
    return self.ledger

  def withdraw (self,amount) :
    #determinamos si hay fondos utilizando la funcion creada
    #check funds
    self.check_funds(amount)
    if True :
      b = {"amount" : -amount}
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
    #calculamos si tenemos fondos suficientes:
    fonds = 0
    for value in self.ledger :
      fonds = fonds + value['amount']
    if fonds > 0 :
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

income = Category('Money')
print(income.deposit(1000,'Initial deposit'))
groceries = Category ('Food')
print (groceries.withdraw(23.24))





#https://forum.freecodecamp.org/t/python-budget-app-test-get-balance-fail/408769