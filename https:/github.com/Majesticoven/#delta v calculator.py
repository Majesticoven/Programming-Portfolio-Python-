#delta v calculator
import math as m
def parameters():
    print("Leave blank or anything but an INT or FLOAT if you do not know the parameter or wish to work it out")
    delta_v = float(input("PLease input the required delta v for this stage"))
    exhaust_velocity = float(input("Please input the exhaust velocity"))
    inital_mass = float(input('please input the inital_mass'))
    final_mass = float(input('please enter the burnout mass'))
    return delta_v,exhaust_velocity,inital_mass,final_mass

def delta_calc(exhaust,initial,final):
    print(exhaust,initial,final)
    delta_v = exhaust*m.log(initial/final)
    return delta_v


def exhaust_v(delta_v,initial,final):
    exhaust_v = delta_v/m.log(initial/final)
    return exhaust_v


def initial_m(delta_v,exhaust,final):
    inital = m.exp(delta_v/exhaust)*final
    return inital


def final_m(delta_v,exhaust,inital):
    final=inital/m.exp(delta_v/exhaust)
    return final


parameters_found=parameters()
userinput = input('What would you like to work out DV EV IM FM (1,2,3,4)')

if userinput == '1':
    print(parameters_found)
    delta_v = delta_calc(parameters_found[1],parameters_found[2],parameters_found[3])
    print(delta_v)
elif userinput == '2':
    exhaust_vel=exhaust_v(parameters_found[1],parameters_found[2],parameters_found[3])
    print(exhaust_vel)
elif userinput == '3':
    initial_mass=initial_m(parameters_found[0],parameters_found[1],parameters_found[3])
    print(initial_mass)
else:
    final_mass=final_m(parameters_found[0],parameters_found[1],parameters_found[2])
    print(final_mass)