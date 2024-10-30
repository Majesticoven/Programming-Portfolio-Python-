import pandas as pd
import numpy as np 
from sympy import Symbol, solve, re

rate_of_angle_change =  np.linspace(0.00872665,0.0872665 ,100)

altitude_turn_start = np.linspace(1000, 100000, 100)
acceleration_gravity = -9.81

def altitude_time_solver(altitude):
    t = Symbol('t')
    expr = 0.0286 * t**3 + 5.9525 * t**2 - altitude
    solutions = solve(expr)
    for s in solutions:
        if re(s) > 0:
            return re(s)
        

def velocity_altitude_solver(time_to_alt):
    velocity = 0.0858 * time_to_alt**2 +11.905* time_to_alt 
    return velocity
    
        
def acceleration_altitude_solver(time_to_alt):

    acceleration = 0.1716 * time_to_alt + 11.905 
    return acceleration


for altitude_turn in altitude_turn_start: 
    time_to_alt = altitude_time_solver(altitude_turn)
    velocity = velocity_altitude_solver(time_to_alt) 
    acceleration = acceleration_altitude_solver(time_to_alt)
    #print(f"Altitude:{altitude_turn} Time:{altitude_time_solver(altitude_turn)} Velocity:{velocity} Acceleration: {acceleration} ")

    for angle_rate in rate_of_angle_change:
        time_to_horizontal = round(np.pi/(2*angle_rate),0)
        
        if time_to_horizontal + time_to_alt < 190:
             current_angle = angle_rate
             time_angle = int(round(np.pi/2*angle_rate,0))

             vertical_velocity = velocity
             horizontal_velocity = 0 
             vertical_position = altitude_turn
             horizontal_position = 0
             vertical_position  = altitude_turn

             for time_step in range(int(time_to_horizontal)):
                horizontal_acceleration = (0.1716*time_step+21.715)*np.sin(current_angle)
                vertical_acceleration = (0.1716*(time_step)+11.905)*np.cos(current_angle)
                vertical_velocity += vertical_acceleration
                vertical_position += vertical_velocity
                horizontal_velocity += horizontal_acceleration
                horizontal_position += horizontal_velocity
                altitude_projectile = vertical_position + (vertical_velocity)**2/(2*9.81)
                if altitude_projectile >199000 and altitude_projectile < 201000 and horizontal_velocity:
                    delta_v_left_core = 0
                    for time_left in range(190-81-time_step): # time left on core
                        horizontal_acceleration = (0.1716*time_step+21.715)
                        horizontal_velocity += horizontal_acceleration
                        if horizontal_velocity >4000:
                            print(f'Time left: {time_left} Altitude spent vertical:{altitude_turn} Final Altitude:{altitude_projectile} Horizontal Acceleration:{horizontal_acceleration} Vertical Acceleration:{vertical_acceleration} Vertical velocity:{vertical_velocity+velocity} Horizontal Velocity:{horizontal_velocity} Angle:{time_to_horizontal}')
                            break
                time_angle += 1
                current_angle += angle_rate
            
             
    
             
                
           
           