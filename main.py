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

  def cal_withdraw (self) :
    withdraw = 0
    for element in self.ledger :
      if element['amount'] < 0:
        withdraw = withdraw + element['amount']
      else :
        continue
    return -1 * withdraw


def create_spend_chart (categories) :
  lista1 = []
  lista2 = []
  total = 0
  count = 0
  for element in categories :
    #print (element.ledger)
    result = element.cal_withdraw () #llamamos a una funcion ()
    #print (result)
    lista1.append(result)
  print (lista1)

  # calculamos el porcentaje gastado
  for i in lista1 :
    total = total + i
  print (total)

  for element in categories :
    while count < 1 :
      for i in lista1 :
        percentage = 100 * float(i) / total
        tupla = (element.name, percentage)
        print (tupla)
        lista2.append(tupla)
        count = count + 1
  print (lista2) 
  





food = Category ('food')
entertainment = Category ('entertainment')
business = Category ('business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))

    