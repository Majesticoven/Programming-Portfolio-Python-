#Clock
#1. settings
 #   time(s) set
  #  timezone set
   # alarm set
#2. time
 #   read time
  #  count time
   # express as integer
    #seconds
#3. timezone
 #   express timezones in array
#4. alarm
 #   take alarm from userinput
  #  express as integer
   # while loop to set off alarm
import time
import pandas as pd
stgerror = 1
while stgerror == 1:
    stgin = str(input(" settings \n timeset \n timezone \n alarm please type which setting you would like to choose"))
    stgin= stgin.lower()
    if stgin == "timeset":
        print("timeset")
        stgerror = 0 
    elif stgin == "timezone":
         print(" timezone ")
         stgerror = 0
         pd.read_csv
    elif stgin == "alarm":
         print("alarm")
         stgerror = 0
    else:
         print("error this is an incorrect value")

