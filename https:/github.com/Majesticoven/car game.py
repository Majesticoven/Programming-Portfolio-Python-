#car game
car_started = 0
car_stopped = 1s
while True:
    user_input = input()
    user_input = user_input.lower()
    
    if user_input == "help":
        print ("""
Start - Start the car
Stop - Stop the car
Quit - quit the game""")
    elif user_input == "start":
        if car_started == 0:
            print("Car started ... Ready to Go!")
            car_started = 1
            car_stopped = 0
        else:
            print("Car is Already Started ...")
    elif user_input == "stop":
        if car_stopped == 0:
            print("Stopping the car")
            car_started = 0
            car_stopped = 1
        else:
            print("Car is already stopped")
    elif user_input == "quit":
        print("Quitting the game")
        break
    else:
        print("Sorry I don't understand this command!")
