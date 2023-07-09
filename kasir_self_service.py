class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item_name(self, item_name, new_name):
        for item in self.items:
            if item[0] == item_name:
                item[0] = new_name
                break

    def update_item_qty(self, item_name, new_qty):
        for item in self.items:
            if item[0] == item_name:
                item[1] = new_qty
                break

    def update_item_price(self, item_name, new_price):
        for item in self.items:
            if item[0] == item_name:
                item[2] = new_price
                break

    def delete_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def reset_transaction(self):
        self.items = []

    def check_order(self):
        for item in self.items:
            if None in item:
                return "Terjadi kesalahan input data"
        return "Pemesanan sudah benar"

    def total_price(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]

        if total > 500000:
            total -= total * 0.1
        elif total > 300000:
            total -= total * 0.08
        elif total > 200000:
            total -= total * 0.05

        return total


# Contoh penggunaan program
trnect_123 = Transaction()

trnect_123.add_item(["Mobil", 2, 100000])
trnect_123.add_item(["Mie", 1, 5000])
trnect_123.add_item(["Tempe", 3, 3000])

trnect_123.update_item_name("Mobil", "Motor")
trnect_123.update_item_qty("Mie", 2)
trnect_123.update_item_price("Tempe", 3500)

trnect_123.delete_item("Mie")

print(trnect_123.check_order())

for item in trnect_123.items:
    print("| {:<4} | {:<12} | {:<13} | {:<12} | {:<13} |".format(
        trnect_123.items.index(item) + 1, item[0], item[1], item[2], item[1] * item[2]))

print("Total Harga: Rp", trnect_123.total_price())
