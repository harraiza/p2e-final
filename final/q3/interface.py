from abc import ABC, abstractmethod

class Interface(ABC):
    def __init__(self,name,size,content):
        self.name=name
        self.size=size
        self.content=content
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def read(self):
        pass

        
