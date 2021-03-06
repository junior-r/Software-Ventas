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

    def add(self, producto, cantidad):
        id = str(producto.id)

        if id not in self.cart.keys():
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
            self.cart[id]['cantidad_vender'] = int(cantidad)
            self.cart[id]['monto_total'] = float(self.cart[id]['precio_v']) * self.cart[id]['cantidad_vender']
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

    def update_pv(self, producto, pv):
        id = str(producto.id)
        if id in self.cart.keys():
            self.cart[id]['precio_v'] = float(pv)
            self.cart[id]['monto_total'] = float(pv) * self.cart[id]['cantidad_vender']
        self.save()

    def clean(self):
        self.session['cart'] = {}
        self.session.modified = True
