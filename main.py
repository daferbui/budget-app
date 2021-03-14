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
  my_dict1 = {}
  my_dict2 = {}
  total = 0
  lista = []
  lista2 = []
  lista3 = []
  frase = 'Percentage spent by category \n'

  for element in categories :
    result = element.cal_withdraw () #llamamos a una funcion ()
    my_dict1[element.name] = result
  print (my_dict1)

  # calculamos el total
  for k,v in my_dict1.items() :
    total = total + v
  
  #introducimos el porcentaje en el diccionario
  for k,v in my_dict1.items() :
    my_dict2[k] = v / total * 100
  print (my_dict2)

  #ordenamos de mayor a menor el diccionario
  for k,v in my_dict2.items() :
    tupla = (v,k)
    lista.append(tupla)
  lista.sort(reverse = True)
  print (lista)

  #falta solucionar esto
  x = 100
  for number in range (11) :
    a = f"{x}".rjust(3) + '| '
    for v,k in lista :
      if v >= x :
        a = a + 'o  '
      else :
        a = a + '  '
    frase = frase + a + '\n'
    x = x - 10

  #corregir esto
  for i in lista :
    guion = ''
    if lista.index(i) == 0 :
      guion = guion.rjust(4)
    elif lista.index(i) > 0 and lista.index(i) < len(lista) - 1 :
      guion = guion + '---'
    elif lista.index(i) == len(lista) - 1 :
      guion = guion + '------' + '\n'
    frase = frase + guion
  
  #encontramos el nombre más largo
  name_len = 0
  for v,k in lista :
    if len(k) > name_len :
      name_len = len (k)
    else :
      continue

  
  
  y = 0
  while y <= name_len :
    letter = '     '
    for v,k in lista :
      try :
        letter = letter + k[y] + '  '
      except :
        letter = letter + '   '
     
    
    if y <= name_len -1 :
      frase = frase + letter + '\n'
    else :
      frase = frase + letter.strip(' ')

    y = y + 1

  frase = frase.rstrip('\n')
    
  return frase



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

    