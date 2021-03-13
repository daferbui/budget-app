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
  frase = 'Percentage spent by category \n'
  for element in categories :
    result = element.cal_withdraw () #llamamos a una funcion ()
    lista1.append(result)
  print (lista1)

  # calculamos el porcentaje gastado
  for i in lista1 :
    total = total + i
  print (total)
  #corregir esto
  for element in categories :
    while count < 1 :
      for i in lista1 :
        percentage = 100 * float(i) / total
        tupla = (percentage,element.name)
        lista2.append(tupla)
        count = count + 1
  lista2.sort(reverse=True)
  print (lista2)

  sum = 0
  for v,k in lista2 :
    if v == 100 :
      while sum < 1 :
        a = '100|' + ' ' + 'o'
        sum = sum + 1
      a = a + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 90 :
      while sum < 1 :
        b = '90|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      b = b + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 80 :
      while sum < 1 :
        c = '80|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      c = c + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 70 :
      while sum < 1 :
        d = '70|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      d = d + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 60 :
      while sum < 1 :
        e = '60|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      e = e + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 50 :
      while sum < 1 :
        f = '50|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      f = f + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 40 :
      while sum < 1 :
        g = '40|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      g = g + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 30 :
      while sum < 1 :
        h = '30|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      h = h + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 20 :
      while sum < 1 :
        i = '20|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      i = i + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 10 :
      while sum < 1 :
        j = '10|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      j = j + ' ' + 'o'
    sum = 0
  for v,k in lista2 :
    if v >= 0 :
      while sum < 1 :
        k = '0|'.ljust(4) + ' ' + 'o'
        sum = sum + 1
      k = k + ' ' + 'o'

  final = frase + f"{a}'\n'{b}{c}{d}{e}"
  return final


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

    