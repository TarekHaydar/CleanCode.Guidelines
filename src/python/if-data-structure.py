# Replace complicated if conditions with data structure.

class Invoice:
    def __init__(self, number, lines_count, total, balance):
        self.number = number
        self.lines_count = lines_count
        self.total = total
        self.balance = balance


invoice = Invoice("Inv0001", 10, 2000, 1000)

# here we have complex if conditions
# it might be more complicated
if 1 <= invoice.lines_count <= 10 and 1000 <= invoice.total <= 2000 and 500 <= invoice.balance <= 1000:
    print(invoice.total * 0.01)
elif invoice.lines_count > 10 and invoice.balance > 1000:
    print(invoice.total * 0.03)


def condition_one(invoice):
    return 1 <= invoice.lines_count <= 10 and 1000 <= invoice.total <= 2000 and 500 <= invoice.balance <= 1000


def condition_two(invoice):
    return invoice.lines_count > 10 and invoice.balance > 1000


def calculate_discount_one(invoice):
    return invoice.total * 0.01


def calculate_discount_two(invoice):
    return invoice.balance * 0.03

# a list for conditions and another one for calculations
conditions = [condition_one, condition_two]
calculate_discounts = [calculate_discount_one, calculate_discount_two]

for i in range(len(conditions)):
    if conditions[i](invoice):
        print(calculate_discounts[i](invoice))
        break
        
