#Encapsulation preserves the Object state 
#Encapsulation avoids redundancy in code and facilitates the maintenance of the code

class AccountBank:
  
  def __init__(self, balance, status, type):
    self.balance = balance
    self.status = status
    self.type = type
    
  def get_available_amount_to_withdraw(self):
      if self.type == 'SilverCard':
          return self.balance - 20
      elif self.type == 'GoldenCard':
          return self.balance - 10
      else:
          return self.balance
    
my_account = AccountBank(1000, 'Active', 'GoldenCard')

print(my_account.get_available_amount_to_withdraw())