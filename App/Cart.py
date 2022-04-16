class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
            self.cart = self.session['cart']
        else:
            self.cart = cart

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def add(self, producto):
        id = str(producto.id)
        if id not in self.cart.keys():
            print('NO aumentó la cantidad')
            self.cart[id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'description': producto.descripcion,
                'precio_v': float(producto.precio_venta),
                'monto_total': float(producto.precio_venta),
                'proveedor': str(producto.marca),
                'username': producto.username,
                'cantidad_vender': 1
            }
        else:
            print('aumentó la cantidad')
            self.cart[id]['cantidad_vender'] += int(1)
            self.cart[id]['monto_total'] += float(producto.precio_venta)
        self.save()

    def delete(self, producto):
        id = str(producto.id)
        if id in self.cart:
            del self.cart[id]
            self.save()

    def sub(self, producto):
        id = str(producto.id)
        if id in self.cart.keys():
            self.cart[id]['cantidad_vender'] -= int(1)
            self.cart[id]['monto_total'] -= float(producto.precio_venta)
            if self.cart[id]['cantidad_vender'] <= 0:
                self.delete(producto)
        self.save()

    def clean(self):
        self.session['cart'] = {}
        self.session.modified = True
