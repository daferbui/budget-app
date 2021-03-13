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
  final = 'Percentage spent by category'
  for element in categories :
    result = element.cal_withdraw () #llamamos a una funcion ()
    lista1.append(result)

  # calculamos el porcentaje gastado
  for i in lista1 :
    total = total + i

  for element in categories :
    while count < 1 :
      for i in lista1 :
        percentage = 100 * float(i) / total
        tupla = (percentage,element.name)
        lista2.append(tupla)
        lista2.sort(reverse=True)
        count = count + 1

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
        b = '90|' + ' ' + 'o'
        sum = sum + 1
      b = b + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 80 :
      while sum < 1 :
        c = '80|' + ' ' + 'o'
        sum = sum + 1
      c = c + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 70 :
      while sum < 1 :
        d = '70|' + ' ' + 'o'
        sum = sum + 1
      d = d + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 60 :
      while sum < 1 :
        e = '60|' + ' ' + 'o'
        sum = sum + 1
      e = e + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 50 :
      while sum < 1 :
        f = '50|' + ' ' + 'o'
        sum = sum + 1
      f = f + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 40 :
      while sum < 1 :
        g = '40|' + ' ' + 'o'
        sum = sum + 1
      g = g + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 30 :
      while sum < 1 :
        h = '30|' + ' ' + 'o'
        sum = sum + 1
      h = h + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 20 :
      while sum < 1 :
        i = '20|' + ' ' + 'o'
        sum = sum + 1
      i = i + ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 10 :
      while sum < 1 :
        j = '10|' + ' ' + 'o'
        sum = sum + 1
      j = j +  ' ' + 'o'
  sum = 0
  for v,k in lista2 :
    if v >= 0 :
      while sum < 1 :
        k = '0|' + ' ' + 'o'
        sum = sum + 1
      k = k +  ' ' + 'o'

  return final + '\n' + f"{a.rjust(4)}'\n'{b.rjust(4)}'\n'{c.rjust(4)}'\n'{d.rjust(4)}'\n'{e.rjust(4)}'\n'{f.rjust(4)}'\n'{g.rjust(4)}'\n'{h.rjust(4)}'\n'{i.rjust(4)}'\n'{j.rjust(4)}'\n'{k.rjust(4)}"



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

    