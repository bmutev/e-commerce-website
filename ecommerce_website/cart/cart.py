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
