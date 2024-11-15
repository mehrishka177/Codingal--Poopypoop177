class student:
    grade = 6
    print("Hi i am a student of grade", grade)
    
ob = student()

class Vehicle:
    
    def __init__(self, max_speed, mileage):
        
        
        self.max_speed = max_speed
        self.mileage = mileage    
          
modelX  = Vehicle(240, 18)

print("Model Max Speed:",modelX.max_speed)
print("model Mileage:", modelX.mileage)