class Booking:
    def __init__(self,booking_id,guest,property,check_in,check_out,status):
        self.booking_id=booking_id
        self.guest=guest
        self.property=property
        self.check_in=check_in
        self.check_out=check_out
        self.status=status
    def view(self):
        for key,value in self.__dict__.items():
            print(key,": ",value)