decimal_convert = {0:'',0.08:'.',0.17:':',0.25:'∴',0.33:'∷',0.42:'⁙',0.5:'S',0.58:'S·',0.67:'S:',0.75:' S∴',0.83:'S∷',0.92:'S⁙'}
final_num = 1293.97
def round_nearest_twelth(number):
    num = round(number*12)/12
    if num  != int(num):
        num -= int(num)
        return decimal_convert[round(num,2)] , int(number)
    else:
        return 0,int(num)

number = 12.93

print(round_nearest_twelth(final_num)[1])