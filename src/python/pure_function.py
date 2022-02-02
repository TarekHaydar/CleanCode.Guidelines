# to consider a function as a pure function, it should apply the following conditions:
# 1 - the function return values are identical for identical arguments
# 2 - the function application has no side effects

# unpure function since it depends on a variable outside its parameters

DISCOUNT_PERCENTAGE = 10


def get_discount_amount_unpure(item_price):
    return item_price * (DISCOUNT_PERCENTAGE / 100)


print(f'discount amount: {get_discount_amount_unpure(1000)}')

DISCOUNT_PERCENTAGE = 15

print(f'discount amount: {get_discount_amount_unpure(1000)}')

# pure function


def get_discount_amount(item_price, discount_percentage):
    return item_price * (discount_percentage / 100)


print(f'discount amount: {get_discount_amount(1000,10)}')
print(f'discount amount: {get_discount_amount(1000,15)}')

# Another example
cars = ["Mercedes", "BMW"]


def add_car_unpure(car_name):
    cars.append(car_name)


add_car_unpure("Kia")

for car in cars:
    print(car)

add_car_unpure("Kia")

for car in cars:
    print(car)

colors = ["black", "white"]


def add_color_pure(colors, color_name):
    copied_colors = colors.copy()
    copied_colors.append(color_name)
    return copied_colors


for color in add_color_pure(colors, "red"):
    print(color)

for color in add_color_pure(colors, "red"):
    print(color)
