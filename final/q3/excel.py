from interface import Interface
class Excel(Interface):
    def __init__(self, name, size, content):
        super().__init__(name, size, content)

    def save(self):
        print("excel saved")

    def open(self):
        print("excel opened")

    def read(self):
        print("excel read")