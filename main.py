class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.balance -= amount
            self.ledger.append({"amount": -1*amount, "description": description})
            return True
        else:
            return False
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})      
        self.balance += amount

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            #print("Transfer Successful")
            return True
        if self.check_funds(amount) == False:
            return False
       
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
          return False 
        
    def __str__ (self): #esto lo hace para que la función se ejecute sin que nosotros
    #la llamemos
        objec = (self.name.center(30, "*") + "\n")
        for entry in self.ledger:
           objec = objec + f"{entry['description'][0:23].ljust(23)}{format(entry['amount'],'.2f').rjust(7)}\n"
        objec = objec + f"Total: {format(self.get_balance(), '.2f')}"
        return objec

    def total_withdrawn(self):
        subtotal = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                subtotal += entry["amount"]
        return subtotal

    
        

def create_spend_chart(categories):
    
    bar_chart = "Percentage spent by category\n"
    total = 0
    subtotals = {}
    percentages = {}
    name_length = 0   
   
# make a dictionary of category: subtotals and find the grand total spending
    for category in categories:
        subtotal = category.total_withdrawn() 
        subtotals[category.name] = subtotal
        total = total + subtotal

# find the rounded percentage that each category contributed to overall spending and add the dictionary category: percentage
    for name, subtotal in subtotals.items(): 
        percent = subtotal / total * 100
        percent = percent - (percent % 10)
        percentages[name] = percent
 

# create the y axis and add the values to the chart
    x = 100
    for number in range(11):
        bar_row = f"{x}".rjust(3) + "| "
        for name, percent in percentages.items():
            if percent >= (x):
                bar_row += "o  "
            else:
                bar_row += "   "
        bar_chart += bar_row + '\n'
        x -= 10
   
# add the x axis
    x_axis = "    -"
    for category in categories:
        x_axis += ("---")
    bar_chart += x_axis + "\n"

# determines the longest category name length
    for category in categories:
        if len(category.name) > name_length:
            name_length = len(category.name)
 
# add the category names for x axis values
    y = 0
    while y <= name_length:
        row = "     "
        for key, value in percentages.items(): 
            category_name = key
            try:    
                row +=  category_name[y] + "  "
            except: # for when the name has already been spelled out
                row += "   "
        
        if y <= name_length -1:
            bar_chart += row + '\n' 
        else:
            bar_chart += row.strip(" ")
            
                 
        y = y + 1
    bar_chart = bar_chart.rstrip("\n")
    return bar_chart
