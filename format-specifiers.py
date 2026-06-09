#{value:flags}

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") #display two decimal places
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")
print()
print(f"Price 1 is ${price1:10}") #display 10 spaces
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
print()
print(f"Price 1 is ${price1:010}") #display 10 spaces with zero padding
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")
print()
print(f"Price 1 is ${price1:<10}") #display 10 spaces with left justify
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")
print()
print(f"Price 1 is ${price1:>10}") #display 10 spaces with right justify(Default)
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")
print()
print(f"Price 1 is ${price1:^10}") #display 10 spaces with center justify(Default)
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")
print()
print(f"Price 1 is ${price1:+}") #plus sign
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
print()
print(f"Price 1 is ${price1:+}") #plus sign
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
print()
price1 += 1000
price2 += 100000
price3 += 1000
print(f"Price 1 is ${price1:,}") #thousand seperator
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")