#bike1 = Bike(200, "25mph")
class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def Displayinfo(self):
        print "price $ {}. Max Speed {}. Miles {}." .format(self.price, self.max_speed, self.miles)
        return self
        
    def Ride(self):
        self.miles +=10
        print "Riding {}" .format(self.miles)
    
    def Reverse(self):
        self.miles -=5
        print "Reversing {}" .format(self.miles)
    
    
bike1 = Bike(200, "25mph")
bike1.Displayinfo()
bike1.Ride(), bike1.Ride()
bike1.Reverse()