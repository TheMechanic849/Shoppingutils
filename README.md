Este package permite ajuda lo nas suas compras, por exemplo se necessitar de saber os discontos totais do seu carrinho
pode usar o apply_discount para saber esse disconto.

funções disponiveis:

from shoppingutil import cart  ---------------- calcular preços

cart={'bolacha':2 , 'maca':1} ----- sendo produto:preço

calculate_total_price(cart)

'---------------------------------------'
from shoppingutil import discount ----------- aplicar desontos

cart={'bolacha':2 , 'maca':1} ----- sendo produto:preço

apply_discount(cart,discount)  --- o desconto será igual para os produtos

'----------------------------------'
from shoppingutil import inventory ---------- para saber se os produtos existem em stock

cart={'bolacha':2 , 'maca':1} ----- sendo produto:preço
inevntory={'bolacha':3, ....} -------- sendo produto:quatidade

check_availability(cart, inventory)