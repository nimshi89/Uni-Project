RIGHT = 1
LEFT = -1
REVERSE_DIRECTION = -6
FORWARD = 1
REVERSE = 0

#gears and allowable speeds are as follows:
    #zero (reverse) (speed -1 to -10). Max reverse speed of car is -10
    #one (speed 0 to 10)
    #two (speed 5 to 25)
    #three (speed 20 to 40)
    #four (speed 40 to 60)
    #five (speed 45 to 80). Max speed of car is 80
    #gears change automatically, one gear at a time

#direction values are similar to numbers on clock face
#0 = 12 = straight on. All other directions = 1-11

class Car:
    def __init__(self):
        self.speed = 0
        self.gear = 1
        self.direction = 0
        self.broken = False #indicates whether car is broken
        self.simulation = []
        self.simulation_loaded = False

    def accelerate(self, ACCELERATE):           
        if self.broken:         #checking is the car broken
            print("The car is broken....")
            return


        print("Accelerating....") #creating a condition and based on the car is in reverse or forward
                                    # the car will get either +5 or -5 to then speed.
        
        if self.gear == "REVERSE":
            self.speed -= 5
            self.change_gear("REVERSE")
        else:
            self.speed += 5
            self.change_gear("FORWARD")
        
        if self.speed > 80:         #setting up top speed limit for forward gear and reverse as well
            self.speed = 80
            print("You have reached the cars top speed!")
        if self.speed < -10:
            self.speed = -10
            print("You have reached the cars top reverse speed!")
            
        self.display_stats()
                

    def brake(self):        
        if self.broken:             #checking is the car broken
            print("The car is broken....")
            return
        
        if self.gear == "FORWARD":          #checking what gear that is currently in
            self.change_gear("FORWARD")
            print("The car is in forward gear")
            

        if self.gear == "REVERSE":
            self.change_gear("REVERSE")
            print("The car is in reverse!")

            
        print("Breaking...")        #braking which will either take or add 5 to the speed variable
                                    #based on the gear the car is in
        
        if self.speed < 0:
            self.speed += 5
        if self.speed > 0: 
            self.speed -= 5
        
        self.display_stats()
        

    def turn_steering_wheel(self, direction_change):    
        if self.broken:             #checking is the car broken
            print("The car is broken....")
            return
        
        if self.gear == REVERSE:         #checking what gear that is currently in
            print("Car is in reverse")
            

        if self.gear == FORWARD:
            print("Car is in forward gear")

        if direction_change == "LEFT":          #Changing the direction variable based on the incoming
            print("taking a left turn...")      #directions
            self.direction += LEFT
        if direction_change == "RIGHT":
            print("taking a right turn...")
            self.direction += RIGHT
        if direction_change == "REVERSE_DIRECTION":
            print("Reverse direction...")
            self.direction += REVERSE_DIRECTION
            
        
        self.display_stats()
        
            
    def change_gear(self, selected_gear): #selected_gear is either FORWARD or REVERSE
        if self.broken:         #checking is the car broken
            print("The car is broken....")
            return

        if selected_gear == "FORWARD" and self.speed < 0:           #setting up a condition that would brake the car if it's alredy in moovewment
            print("You have selected the wrong gear for the speed of the car")  
            self.broken = True
            return
        
        if selected_gear == "REVERSE" and self.speed > 0:
            print("You have selected the wrong gear for the speed of the car")
            self.broken = True
            return

        target_gear = 0             #creating a variable for the gearbox
        

        if self.speed < 0:          #creating the speed limits for each gear
            target_gear = 0
        if self.speed >= 0 and self.speed < 10:
            target_gear = 1
        if self.speed > 5 and self.speed < 25:
            target_gear = 2
        if self.speed > 20 and self.speed <= 40:
            target_gear = 3
        if self.speed > 40 and self.speed <= 60:
            target_gear = 4
        if self.speed > 45 and self.speed <= 80:
            target_gear = 5
    
        while self.gear != target_gear:         #creating a condition that would change the gear one-by-one
            if self.gear < target_gear:         #till it is in the required one, wile providing feedback to the user
                self.gear+= 1
                print("Changing up...")
                print(f"current gear {self.gear}")
            elif self.gear > target_gear:
                self.gear-=1
                print("Changing down....")
                print(f"current gear {self.gear}")
        

    def display_stats(self):
        print(f"Speed = {self.speed}, Gear = {self.gear}, Direction = {self.direction}")    #displaying the status of the car
        

    def load_simulation(self, filename):
        file = open(filename, 'r')  #loading in the file that contains the commands for the car
        line = file.readline()
        while line != "":
            line = line.strip()
            self.simulation.append(line)
            line = file.readline()
        file.close()
        
        return self.simulation
        

    def run_simulation(self):

        for x in self.simulation:       #calling in the functions of the class based on the type of command
            if x == "LEFT":
                self.turn_steering_wheel("LEFT")
            if x == "RIGHT":
                self.turn_steering_wheel("RIGHT")
            if x == "REVERSE_DIRECTION":
                self.turn_steering_wheel("REVERSE_DIRECTION")
            if x == "FORWARD":
                self.change_gear("FORWARD")
            if x == "REVERSE":
                self.change_gear("REVERSE")
            if x == "ACCELERATE":
                self.accelerate("ACCELERATE")
            if x == "BRAKE":
                self.brake()
                
        return self.turn_steering_wheel, self.change_gear, self.accelerate, self.brake

if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
    
