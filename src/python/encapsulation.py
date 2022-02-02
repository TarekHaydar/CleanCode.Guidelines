# Encapsulation preserves the Object state
# Encapsulation avoids redundancy in code and facilitates the maintenance of the code

# unencapsulated the logic

class AccountBank:

    def __init__(self, balance, status, type):
        self.balance = balance
        self.status = status
        self.type = type


my_account = AccountBank(1000, 'Active', 'GoldenCard')


def get_available_amount_to_withdraw(my_account):
    if my_account.type == 'SilverCard':
        return my_account.balance - 20
    elif my_account.type == 'GoldenCard':
        return my_account.balance - 10
    else:
        return my_account.balance


print(my_account.get_available_amount_to_withdraw())

# Encapsulating the logic


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
