# ISM 2411 - Lists and Tuples Lab
# Reflection 1:
# The most surprising thing about Python lists is that they can be changed after
# they are created. Methods such as append(), remove(), and sort() update the
# existing list, while a tuple cannot be changed after it is created.
#
# Reflection 2:
# In a retail setting, a list could hold the quantities or prices of items sold
# during a shift. Python could quickly calculate totals, averages, and high-sales
# items instead of requiring someone to sort and calculate each value manually in Excel.

# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index practice
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])

# Exercise 3: Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Modify
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because their values cannot be changed accidentally.")

print(coords)

# Exercise 6: Average of a list of sales
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {best_day}")
print(f"Worst: {worst_day}")

# Exercise 7: Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)

# Exercise 8: Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

high_sales_count = len(high_sales)
high_sales_average = sum(high_sales) / high_sales_count

print(high_sales)
print(f"Count: {high_sales_count}")
print(f"Avg: {high_sales_average:.2f}")