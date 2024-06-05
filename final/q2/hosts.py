from users import User
from properties import Property
class Host(User):
    def __init__(self,name,phone_no,email):
        super().__init__(name,phone_no,email)
        self.listings=[]

    def add_listing(self,id,name,location,description,PPN,availability):
        self.listings.append(Property(id,name,location,description,PPN,availability))
    def view_listings(self):
        for prop in self.listings:
            print()
            prop.view()
            print()


            
hostlist=[Host("adeel",123456789,"blabla@blabla.com"),Host("adeela",123456789,"blabla@blabla.com")]
hostlist[1].add_listing(123,"haven","lahore","huge",1234,True)
hostlist[0].add_listing(456,"den","lahore","4bed4bath",123456,True)
hostlist[0].add_listing(123,"nest","lahore","2bed2bath",12345,True)
