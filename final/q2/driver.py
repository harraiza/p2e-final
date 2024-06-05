from hosts import Host,hostlist
from guests import Guest
from bookings import Booking
from users import User
from properties import Property


guest1=Guest("ahmed",123456789,"bhai@bhai.com")

guest1.view_listings()

guest1.search_listings("123")

guest1.create_booking(54321,hostlist[0].listings[0],"kal","parson","confirmed")

guest1.view_bookings()

hostlist[0].view_listings()