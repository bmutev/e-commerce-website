from . cart import Cart


# Return the default data from the Cart class
def cart(request):
    return {'cart': Cart(request)}
