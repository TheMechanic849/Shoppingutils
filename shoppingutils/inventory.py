def check_availability(cart, inventory):
    for i in cart:
        for x in inventory:
         if cart[i]==inventory[x] and inventory[x]==0:
            return False
         else:
            return True