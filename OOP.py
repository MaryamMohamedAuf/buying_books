class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Invoice:
    def __init__(self, book, quantity):
        self.book = book
        self.quantity = quantity

    def calculate_total(self):
        return self.book.price * self.quantity


class InvoicePrinter:
    def __init__(self, invoice):
        self.invoice = invoice

    def print_invoice(self):
        print("Invoice:")
        print(f"Book: {self.invoice.book.name}")
        print(f"Quantity: {self.invoice.quantity}")
        print(f"Total: {self.invoice.calculate_total()}")


class InvoiceSaver:
    def __init__(self, invoice):
        self.invoice = invoice

    def save_invoice(self, filename):
        with open(filename, "w") as file:
            file.write("Invoice:\n")
            file.write(f"Book: {self.invoice.book.name}\n")
            file.write(f"Quantity: {self.invoice.quantity}\n")
            file.write(f"Total: {self.invoice.calculate_total()}\n")