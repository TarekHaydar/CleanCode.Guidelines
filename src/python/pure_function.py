DISCOUNT_PERCENTAGE = 10

#unpure function
def get_discount_amount_unpure(item_price):
  return item_price * (DISCOUNT_PERCENTAGE / 100)

print('unpure discount functions')
print(f'discount amount: {get_discount_amount_unpure(1000)}')

DISCOUNT_PERCENTAGE = 15
print(f'discount amount: {get_discount_amount_unpure(1000)}')

#pure function
def get_discount_amount(item_price, discount_percentage):
  return item_price * (discount_percentage / 100)

print('')
print('pure discount functions')
print(f'discount amount: {get_discount_amount(1000,10)}')
print(f'discount amount: {get_discount_amount(1000,15)}')

cars = ["Mercedes","BMW"]

def add_car_unpure(car_name):
    cars.append(car_name)
    
add_car_unpure("Kia")

print('')
for car in cars:
  print(car)
  
add_car_unpure("Kia")

print('')
for car in cars:
  print(car)
  
colors = ["black","white"]

def add_color_pure(color_name):
    copied_colors = colors.copy()
    copied_colors.append(color_name)
    return copied_colors
    
print('')
for color in add_color_pure("red"):
    print(color)

print('')
for color in add_color_pure("red"):
    print(color)