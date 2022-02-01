# 1 - the difference betweeen Guard Clauses and Input Validations

def guard_clauses(product):
    if product is None:
        raise Exception("product cannot be null")

    if product.quantity <= 0:
        raise Exception("quantity cannot be negative")
        
    # some statements to calculate discount

def validate_input_data(submitted_product):
    if submitted_product is None:
        return ["product cannot be null"]
    
    messages = []

    if submitted_product.quantity <= 0:
        messages.append("quantity cannot be negative")
    
    if submitted_product.price <= 0:
        messages.append("price cannot be negative")
    
    return messages

# 2 - Avoid else if (if-branching)
def get_item_price_range(price):
    if price == 0:
        return 'zero'
    else:
        if price > 0 and price <= 20:
            return '20 max'
        elif price >= 21:
            return '21 min'
        else:
            return 'negative'
        
def get_item_price_range(price):
    if price == 0:
        return 'zero'
    
    if price > 0 and price <= 20:
        return 'between 1 and 20'
    
    if price >= 21:
        return 'greater than 20'
    
    return('negative')