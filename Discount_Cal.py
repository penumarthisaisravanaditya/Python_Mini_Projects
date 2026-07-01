amount=int(input("Enter amount:"))

if amount > 10000:
    discount = amount * 0.30
elif amount > 5000:
    discount = amount * 0.20
elif amount > 1000:
    discount = amount * 0.10
else:
    discount = 0
    
final_amount = amount - discount

print(f"Amount:{amount:.2f}")
print(f"Discount:{discount:.2f}")
print(f"Final amount:{final_amount:.2f}")
