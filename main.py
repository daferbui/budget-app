class Category :
  
  def __init__ (self, category) :
    #repasar esto para que lo poniamos si abajo no hago referencia
    self.category = category
    self.ledger = list ()
  
  def deposit (self, amount, description = '') :
    a = {"amount" : amount, "description" : description}
    self.ledger.append (a)
    return self.ledger

  def withdraw (self,amount) :
    #no puedo self.deposit (este no es el objeto)
    if self.deposit(amount) < self.withdraw(amount) :
      b = {"amount" : -amount}
      self.ledger.append(b)
      return self.ledger
    else :
      return self.ledger
    
    return self.ledger
  
  def get_balance (self) :
    return 'Not yet created'
  
  def transfer (self) :
    return 'Not yet created'
  
  def check_funds (self) :
    return 'Not yet created'

def create_spend_chart(categories):
  return 'Not yet created'

income = Category('Money')
print(income.deposit(1000,'Initial deposit'))
groceries = Category ('Food')
print (groceries.withdraw(23.24))




#https://forum.freecodecamp.org/t/python-budget-app-test-get-balance-fail/408769