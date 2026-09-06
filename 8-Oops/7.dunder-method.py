class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    # Special methods:
    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

# Loops through the cart using __iter__()
# for item in cart:
#     print(item, end=' ')
    # Output: Laptop Wireless mouse Ergo keyboard Monitor 

print(len(cart))            # Output: 4 (uses __len__)
print(cart[3])              # Output: Monitor (uses __getitem__)
print('Monitor' in cart)    # Output: True (uses __contains__)
print('banana' in cart)     # Output: False (uses __contains__)

cart.remove('Ergo keyboard')
print(cart.list_items())    # Output: ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana')       # Output: banana is not in cart

