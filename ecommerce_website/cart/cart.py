class Cart:

    def __init__(self, request):
        self.session = request.session

        # Returning user - obtain his existing session
        cart = self.session.get("session_key")

        # New user - generate a new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Fill the cart with the products that the user has put in it from older session
        # or set it to empty if a new user
        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] += product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
        self.session.modified = True

    def __len__(self):
        total_qty = 0
        for item in self.cart.values():
            total_qty += item['qty']

        return total_qty
        # return sum(item['qty'] for item in self.cart.values())
