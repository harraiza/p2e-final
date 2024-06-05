from word import Word
from pdf import PDF
from excel import Excel

class DocFactory:
    def __init__(self):
        pass
    def create_word(self,name,size,content):
        return Word(name,size,content)
    def create_excel(self,name,size,content):
        return Excel(name,size,content)
    def create_pdf(self,name,size,content):
        return PDF(name,size,content)
    
factory=DocFactory()

excel=factory.create_excel("sheets",56,";asldfjklash")
excel.save()