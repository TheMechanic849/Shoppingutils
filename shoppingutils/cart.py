def calculate_total_price(cart):
    total=0
    for i in cart:
        total+=cart[i]
    print(f"Total = {total} euros")