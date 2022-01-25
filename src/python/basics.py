# talk about try catch
# Guard Clauses
def calculate_discount(product):
    if product is None:
        raise Exception("product cannot be null")
        
    # some statements to calculate discount

def validate_input_data(product):
    if product is None:
        return ["product cannot be null"]
    
    messages = []
    if product.quantity <= 0:
        messages.append("quantity cannot be negative")
    
    if product.price <= 10:
        messages.appen("price is very low")
    
    return messages;

#avoid else if
def print_a(a):
    if a == 0:
        print('zero')
    else:
        if a > 0 and a <= 20:
            print('20 max')
        elif a >= 21:
            print('21 min')
        else:
            print('negative')
        
def print_a_second(a):
    if a == 0:
        print('zero')
        return
    
    if a > 0 and a <= 20:
        print('between 1 and 20')
        return
    
    if a >= 21:
        print('greater than 20')
        return
    
    print('negative')
    
print_a_second(21)