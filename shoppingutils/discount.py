def apply_discount(cart,discount):
    price=[]
    disc={}
    for i in cart:
       price.append(cart[i])
    for i in price:
        disc[cart[i]]=i-0.25
        return disc