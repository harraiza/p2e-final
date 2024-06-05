from interface import Interface
class Word(Interface):
    def __init__(self, name, size, content):
        super().__init__(name, size, content)

    def save(self):
        print("word saved")

    def open(self):
        print("word opened")

    def read(self):
        print("word read")