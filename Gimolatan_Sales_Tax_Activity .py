# Get the purchase amount from the user
purchase_amount = float(input("Enter the purchase amount: "))

# Calculate the sales tax (6%)
Sales_tax_rate = 0.06
Sales_tax_rate = purchase_amount * Sales_tax_rate

# Display the sales tax with two digits after the decimal point
print(f"Sales Tax (6%) : ${Sales_tax_rate:.2f}")
