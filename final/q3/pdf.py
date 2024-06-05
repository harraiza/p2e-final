from interface import Interface
class PDF(Interface):
    def __init__(self, name, size, content):
        super().__init__(name, size, content)

    def save(self):
        print("PDF saved")

    def open(self):
        print("PDf opened")

    def read(self):
        print("PDF read")