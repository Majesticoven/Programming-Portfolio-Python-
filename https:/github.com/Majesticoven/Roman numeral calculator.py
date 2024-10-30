from IPython.display import clear_output

#------------
#                           Roman numeral calculator
#                           by Owen(2667074c)(release 1.0)
#
# The purpose of this exercise is to develop a calculator which can perform basic
# mathamtical operations with roman numerals, its uses almost exclusivly core python modules.
# It accepts digits from 1/12 to 3999 and 11/12 and can perform all core maths functions.
# Addition,subtraction,division,multiplication,modulous,exponents and integer division. 
# I hope you enjoy using this python program.
#------------

 # Dictionaries defined for when converting between roman and arabic numbers 
units = {1:'I',2:'II',3:'III',5:'V',6:'VI',7:'VII',8:'VIII'}
tens = {10:'X',20:'XX',30:'XXX',50:'L',60:'LX',70:'LXX',80:'LXXX'}
hundreds = {100:'C',200:'CC',300:'CCC',500:'D',600:'DC',700:'DCC',800:'DCCC'}                
special_chars = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}                             # special cases when converting numeral to decimal
decimal_convert = {0:'',0.08:'.',0.17:':',0.25:'∴',0.33:'∷',0.42:'⁙',0.5:'S',0.58:'S·',0.67:'S:',0.75:' S∴',0.83:'S∷',0.92:'S⁙'} #decimal dicitonary

#------------
# This is the main part of the program. 
# The program inputs roman numerals then sends them off to be converted,limit checks and then
# outputs the roman numeral answer


def numeral_calc_start():                                                                     #numeral inputs
    numeral_a =input('Please enter the the first numeral(not case sensitive)')
    converted_numeral_a = converters.numeral_to_number(numeral_a.upper())                     #enter the first number and convert it to decimal
    checkers.limits_check(float(converted_numeral_a))

    operator = input('please enter operator(+,-,*,/,//,**,%)')                                #operation input

    numeral_b = input('Please enter the the second numeral(not case sensitive)')              #enter second number and convert it to decimal
    converted_numeral_b = converters.numeral_to_number(numeral_b.upper())
    checkers.limits_check(float(converted_numeral_b))
    arabic_answer = eval(converted_numeral_a + operator + converted_numeral_b)                #the eval command takes in a decimal string input e.g.'1+1'and returns an interger e.g. 2
    
    checkers.limits_check(arabic_answer)

    arabic_integer = int(arabic_answer)
    print(f'Your answer is: {converters.number_to_numeral(str(arabic_integer))}{checkers.integer_check(arabic_answer)}')   # print the converted numeral and is the final answer
    
    new_calc = input('Would you like to perform another operation? N will return you to the main menu (Y or N)')
    
    if new_calc.upper() == 'Y':
        numeral_calc_start()
    
    else:
        Menus.menu()

#------------------------------
# The checkers class contains the limit,decimal points as well as error handling for invalid inputs
# This program checks to see if the number input is too big or too small
# It accepts digits from 1/12 to 3999 11/12
# the input command allows the user to exit the program if they wish instead of retrying
        
class checkers:        
    def limits_check(number):
        stopper = ''                                                                                #defining stopper
        if number >= 4000:                                                                          #upper limit check    
            stopper = input('The number is too high would you like to try again (Y or N)')          
        if number <= 0:                                                                             #lower limit check
            stopper = input('The number is too low would you like to try again (Y or N)')
        
        if stopper.lower() == 'y':                                                                  #restarts program is yes
            numeral_calc_start
        elif stopper.lower()=='n':
            exit()                                                                                  #exits the program


    def integer_check(arabic_answer):                                                               #checks to see if integer
        if arabic_answer != int(arabic_answer):
            arabic_float = arabic_answer - int(arabic_answer)                                       #gives just decimal
            roman_float = converters.round_nearest_twelfth(arabic_float)                            #returns the decimal in roman format
        
        else:
            roman_float = ''                                                                        #will return nothing if no decimal

        return str(roman_float)                                     
    

#------------
#The converters class contains the translators of the calculator. The two main functions are numeral_to_number 
#and number_to_numeral. This class also containes the round_nearest_twelfth function. Functions titles in this
#section are fairly self explaniatory. 
    
class converters:
#Round nearest twelfth makes use of the round function to round to two decimal places then uses said number as a key for the decimal dictionary
#and then the program returns the decimal.
    
    def round_nearest_twelfth(arabic_float):
        arabic_float = round(arabic_float*12)/12
        rounded_arabic_float = decimal_convert[round(arabic_float,2)] 
        return rounded_arabic_float
    
#Numeral to number checks for special cases, adds their value to an integer then does simple 
#addition to get the sum total for the rest of the numerals.
    
    def numeral_to_number(numeral):                                                                 #converts numeral to number
        converted_numeral = 0                                                                       #defines converted numeral as integer
        for char in special_chars:                                                                  # goes through special chars list if the numeral contain any special chars it will be dealt with here
            if char in numeral:
                converted_numeral += special_chars[char]
                numeral = numeral.replace(char,'')                                                  #converts special char to int then cleans it from numeral
        for char in numeral:
                if char == 'X':
                    converted_numeral += 10
                elif char  == 'I':
                    converted_numeral += 1
                elif char == 'V':                                                                   #proccess numerals one by one and sums to the total decimal
                    converted_numeral += 5
                elif char == 'L':
                    converted_numeral += 50
                elif char == 'C':
                    converted_numeral += 100
                elif char == 'D':
                    converted_numeral += 500 
                elif char == 'M':
                    converted_numeral += 1000
                elif char == 'S':
                    converted_numeral += 0.5
                elif char == '.':
                    converted_numeral += 0.08
                else:
                    print('one or more charecters are not numerals try again')
                    numeral_calc_start()
                    exit()
        return str(converted_numeral)                                                             # return string output
    
#The number to numeral function uses 3 dicitionaries to convert each of up to 4 numbers to numerals then
#concatenates the results into a string which is returned to the numeral_calc_start function         

    def number_to_numeral(final_num):                                                             #converts number to numeral
        answer = ''                                                                               #final answer defined as string
        if len(final_num) ==4:                                                                    #this checks to see if final num is in the thousands
            answer += 'M'*int(final_num[0])                                                       #takes the first char in string which is the thousands and adds m input n times                                                                                                
            final_num = final_num[1:]                                                             #removes the first char from the string
        multiplier = 10**(len(final_num)-1)                                                       #defines a mulitplier

        for num in map(int,final_num):
            num = num*multiplier                                                                  #multiplies number by multiplier to match dictionaries
            if num in special_chars.values():                                                     # checks to see if in the special char dictionary values
                for key,value in special_chars.items():
                    if num == value:                                                              #will add the key to final answer and then contniue
                        answer += key 

            elif num in hundreds:
                answer += hundreds[num] 
            elif num in tens:
                answer += tens[num]                                                               #find the units tens and hundred and concatenates all into one big string 
            elif num in units:
                answer += units[num]

            multiplier //= 10                                                                     #divdes multiplier by ten i.e.1000 to 100 to 10 to 1
        return answer                                                                             #outputs final answer

#--------
# The menus class contains two functions that are mainly text based. They introduce and educate
# people in the use of this calculator 
    
class Menus:

    def help():
        stopper = input('''This is the help function of the calculator.
        Calculator mode: When using calculator mode you will be required to type in a roman numeral
        then an operator and then a second roman numeral.
        numerals must be formed correctly otherwise the program will no work
        Numbers can only be between 3999.11/12 and 1/12 as this is all the romans
        could demonstrate using there system. PRESS ENTER TO RETURN TO THE MENU''')               #stopper acts as stopper, stops menu loading as soon as help is called(for readability)
        clear_output
        Menus.menu()                                                                              # return to main menu
 

    def menu():
        menu_input = input('''Hello and Welcome to this Roman Numeral Calculator.
        Please select one of the operations below(not case sensitive)
                    
        Calculator(c)
        Help(h)
        Exit(e)
          ''')                                                                                    # This is the starting menu
    
        menu_input = menu_input.lower()     
                                                                                                  
        if menu_input == 'c':                                                                     #conditionals for options selected   
            numeral_calc_start()
        elif menu_input == 'h':
            help()
        elif menu_input == 'e':
            exit
        else:
            print('Im sorry but you have entered an incorrect menu input please try again')
            Menus.menu()                                                                          #if error then resest menu and try again
        clear_output                                                                              #clears console 


Menus.menu()                                                                                      #calls menu, starting the program