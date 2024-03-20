# In day 6 we will be doing some hurdle races to help reborg to reach his goal

# url to problem "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json"
#                            
#                         Hurdles race
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
#                        
                    #    What you need to know
# The functions move() and turn_left().
#                           
#                           Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
number_of_jump=6
while number_of_jump>0:
    jump()
    number_of_jump-=1