def calculate_total_price(*prices, tax_rate=0.05):
    subtotal = sum(prices)
    total = subtotal * (1 + tax_rate)
    return total

total_price_1 = calculate_total_price(10.99, 5.99, 3.50)
total_price_2 = calculate_total_price(10.99, 5.99, 3.50, tax_rate=0.07)

print(f"Use default tax_rate {total_price_1}")
print(f"Without default tax_rate {total_price_2}")
