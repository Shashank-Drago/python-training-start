# Name: Shashank S
# Date: 15-11-2026
# Module 2: Core Fundamentals

print('---Task 1: Identity vs Equality---')
# Task - 1
x=256
y=256
a=257
b=257

is_same_identity = a is b
is_same_value = a == b
status = None

# Using single f-string to display everything
print(f'x id: {id(x)} | y id: {id(y)} (These are the SAME address due to Integer Caching)')
print(f'a id: {id(a)} | b id: {id(b)} (These are DIFFERENT addresses)')
print(f"Is 'a' and 'b' the same object (a is b)? {is_same_identity}")
print(f"Is 'a' and 'b' the same value (a == b)? {is_same_value}")
print("\n--- TASK 2: Advanced I/O and Type Casting ---")
# Task - 2
# We use input() and cast them immediately
hourly_rate = float(input("Enter Hourly Rate (e.g., 20.50): "))
hours_worked = int(input("Enter Hours Worked (e.g., 40): "))
tax_bracket = float(input("Enter Tax Bracket (e.g., 0.2 for 20%): "))

gross_pay = hourly_rate * hours_worked
net_pay = gross_pay - (gross_pay * tax_bracket)

print(f"Type of hourly_rate: {type(hourly_rate)}")
print(f"Type of hours_worked: {type(hours_worked)}")
print(f"Type of tax_bracket: {type(tax_bracket)}")


print("\n--- TASK 3: Precision Engineering ---")
# Task - 3
# Header centered in 40 chars using = as filler
header = f"{'OFFICIAL PAYSLIP':=^40}"
# Divider line matching the width exactly
divider = "=" * 40

print(header)
print(divider)
# Labels left-aligned (<25), Values right-aligned (>10) with 3 decimal places and $
print(f"{'Hourly Rate:':<25} ${hourly_rate:>10.3f}")
print(f"{'Hours Worked:':<25} {hours_worked:>10} hrs")
print(f"{'Tax Bracket:':<25} {tax_bracket:>10.3%}")
print(divider)
print(f"{'Gross Pay:':<25} ${gross_pay:>10.3f}")
print(f"{'Net Pay:':<25} ${net_pay:>10.3f}")
print(divider)


print("\n--- TASK 4: Complex Expressions ---")
# Task - 4
a_val = 10
b_val = 5
c_val = 2
d_val = 3
e_val = 2
f_val = 8
g_val = 3

# Formula: (a + b * c) / (d ** e) - (f | g)
# Note: || in math often means OR. In Python bitwise OR is |
Result = (a_val + b_val * c_val) / (d_val ** e_val) - (f_val | g_val)

is_valid = (Result > 0) and (Result is not None)

print(f"Final Result: {Result}")
print(f"Is Valid? {is_valid}")


print("\n--- TASK 5: Bitwise Permissions ---")
# Task - 5
GUEST = 1       # 0001
USER = 2        # 0010
ADMIN = 4       # 0100
SUPERUSER = 8   # 1000

# Combine GUEST and USER
current_access = GUEST | USER

# Elevate ADMIN (left shift doubles the value)
NEW_SECURE_LEVEL = ADMIN << 1

# Check if current_access contains USER bit
has_user = (current_access & USER) == USER

# Toggle GUEST (removes it)
toggle_guest = current_access ^ GUEST

print(f"Current Access (Decimal): {current_access} | Binary: {bin(current_access)}")
print(f"New Secure Level (Decimal): {NEW_SECURE_LEVEL} | Binary: {bin(NEW_SECURE_LEVEL)}")
print(f"Has USER bit? {has_user}")
print(f"After Toggling Guest (Decimal): {toggle_guest} | Binary: {bin(toggle_guest)}")
