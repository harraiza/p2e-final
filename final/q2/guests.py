from users import User
from properties import Property
from hosts import Host,hostlist
from bookings import Booking
class Guest(User):
    def __init__(self, name, phone_no, email):
        super().__init__(name, phone_no, email)
        self.bookings=[]
    def create_booking(self,booking_id,property,check_in,check_out,status):
        self.bookings.append(Booking(booking_id,self,property,check_in,check_out,status))
        property.availability=False

    def view_bookings(self):
        for booking in self.bookings:
            print()
            booking.view()
            print()

    def search_listings(self,word):
        shortlisting=[]
        for host in hostlist:
            for listing in host.listings:
                for key,value in listing.__dict__.items():
                    if str(value) == word:
                        shortlisting.append(listing)

        for listing in shortlisting:
            print()
            listing.view()
            print()

    def view_listings(self):
        for host in hostlist:
            host.view_listings()