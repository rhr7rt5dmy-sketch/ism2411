"""
calculator.py
Python Operators & Business Formulas – Module Exercises

Self-Assessment Answers
-----------------------
1. If you forget to divide the discount percentage by 100 (using 10 instead of 0.10),
   Python will NOT crash. It will silently produce a wrong (usually negative or
   absurdly small) discounted revenue because the formula becomes
   price * (1 - 10) = price * (-9). This is a classic semantic error: the program
   runs but the business numbers are incorrect.

2. Another common business use of // and % is payroll or shift scheduling.
   Example: an employee worked 47 hours. With a standard 8-hour shift:
   full_shifts = 47 // 8  → 5 full shifts
   leftover_hours = 47 % 8 → 7 hours of overtime or partial shift.
   The same pattern appears in inventory batching, invoice line grouping,
   and subscription billing cycles.

3. Concept I feel least confident about: the precise interaction between
   floor division (//), modulo (%), and floating-point results when the
   numbers are not clean integers. Extra practice with packaging,
   break-even, and inventory problems that mix floats and integers
   would strengthen this.
"""

# --- Exercise 1 ---
# Revenue
price = 50
quantity = 12
revenue = price * quantity
print(f"Revenue: ${revenue:,.2f}")

# --- Exercise 2 ---
# Margin
cost = 32
price = 50
margin = (price - cost) / price
print(f"Margin: {margin:.1%}")

# --- Exercise 3 ---
# Two products – which has the higher margin?
price_a, cost_a = 80, 45
price_b, cost_b = 60, 28

margin_a = (price_a - cost_a) / price_a
margin_b = (price_b - cost_b) / price_b
product_a_wins = margin_a > margin_b

print(f"Product A margin: {margin_a:.1%}")
print(f"Product B margin: {margin_b:.1%}")
print(f"Product A has higher margin: {product_a_wins}")

# --- Exercise 4 ---
# Logical combo – is the product "premium"?
price = 120
margin = 0.35
is_premium = price > 100 and margin > 0.3
print(f"is_premium = {is_premium}")

# Change values so only one condition is true
price = 90          # fails price > 100
margin = 0.40       # still passes margin > 0.3
is_premium = price > 100 and margin > 0.3
print(f"is_premium (after change) = {is_premium}")

# --- Exercise 5 ---
# Common-mistake check: / vs // vs %
print(f"17 / 5  = {17 / 5}")    # 3.4  – true division, returns float
print(f"17 // 5 = {17 // 5}")   # 3    – floor division, whole number of groups
print(f"17 % 5  = {17 % 5}")    # 2    – remainder after filling full groups

# Written explanations:
# /  (true division) gives the exact mathematical result as a float.
#     Use it for rates, averages, and any continuous quantity (price, margin, tax).
# // (floor division) discards the fractional part and returns an int.
#     Use it when you need a whole-number count: full boxes, full shifts, complete orders.
# %  (modulo) returns the leftover after floor division.
#     Use it together with // for packaging, batching, or any “how many left over” problem.

# --- Exercise 6 ---
# Full pricing calculator (interactive)
print("\n--- Exercise 6: Full Pricing Calculator ---")
product_name = input("Product name: ")
retail_price = float(input("Retail price: "))
unit_cost = float(input("Unit cost: "))
quantity_sold = int(input("Quantity sold: "))
discount_pct = float(input("Discount percentage (e.g. 10 for 10%): "))

# Convert percentage to decimal
discount_rate = discount_pct / 100

revenue_before = retail_price * quantity_sold
discounted_revenue = revenue_before * (1 - discount_rate)
gross_margin = (retail_price - unit_cost) / retail_price
net_profit = discounted_revenue - (unit_cost * quantity_sold)

print(f"Product: {product_name}")
print(f"Revenue (before discount): ${revenue_before:,.2f}")
print(f"Discounted revenue:        ${discounted_revenue:,.2f}")
print(f"Gross margin:              {gross_margin:.1%}")
print(f"Net profit:                ${net_profit:,.2f}")

# --- Exercise 7 ---
# Packaging problem – boxes of 24
print("\n--- Exercise 7: Packaging Problem ---")
items_ordered = int(input("Number of items ordered: "))
box_size = 24

full_boxes = items_ordered // box_size
loose_items = items_ordered % box_size
exact_fit = loose_items == 0

print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

# Optional Stretch Challenges (commented out so the required script stays clean)
# Uncomment if you want to run them as well.

# # --- Stretch A: Break-even calculator ---
# print("\n--- Stretch A: Break-even Calculator ---")
# fixed_costs = float(input("Fixed costs: "))
# variable_cost = float(input("Variable cost per unit: "))
# retail_price = float(input("Retail price per unit: "))
#
# contribution = retail_price - variable_cost
# break_even_exact = fixed_costs / contribution
# break_even_whole = fixed_costs // contribution
# remainder_units = fixed_costs % contribution
#
# print(f"Break-even (exact): {break_even_exact:,.2f} units")
# print(f"Break-even (whole units): {break_even_whole:,.0f} units")
# print(f"Partial-unit remainder: {remainder_units:,.2f}")

# # --- Stretch B: Operator precedence traps ---
# print("\n--- Stretch B: Precedence Traps ---")
# # Example 1 – discount then tax
# price = 100
# print("Without ():", price * 1 - 0.15 * 1 + 0.07)          # wrong
# print("With ():   ", price * (1 - 0.15) * (1 + 0.07))      # correct
# # The version with parentheses applies discount first, then tax – the business intent.
