class Property:
    def __init__(self,id,name,location,description,PPN,availability):
        self.id=id
        self.name=name
        self.location=location
        self.description=description
        self.PPN=PPN
        self.availability=availability
    def view(self):
        for key,value in self.__dict__.items():
            print(key,": ",value)
