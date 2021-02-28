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
    my_dict = self.ledger[0]
    deposit = my_dict['amount']
    if deposit > amount :
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
    #decidimos si realizamos la transferencia
    if fonds > 0 :
      a = {"amount" : -amount, "Transfer to" : category}
      #Falta introducir Transfer from (entender porque)
      self.ledger(a)
      return True
    else :
      return False
    
  
  def check_funds (self) :
    return 'Not yet created'

def create_spend_chart(categories):
  return 'Not yet created'

income = Category('Money')
print(income.deposit(1000,'Initial deposit'))
groceries = Category ('Food')
print (groceries.withdraw(23.24))
print(groceries.get_balance())
Shirts = Category ('Clothing')
print(Shirts.transfer(23,'Clothing'))




#https://forum.freecodecamp.org/t/python-budget-app-test-get-balance-fail/408769