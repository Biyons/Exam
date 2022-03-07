
def calc_lucase(str):
 ucnt = 0
 lcnt = 0
 for x in str:
   if x=="A""B""C""D""E""F""G""H""I""J""K""L""M""N""O""P""Q""R""S""T""U""V""W""X""Y""Z":
    ucnt==ucnt+1
   else:
     lcnt=lcnt+1
 print("Count of uppercase letter=",ucnt)
 print("Count of lowercase letter=",lcnt)

str=input("Enter the string :")
str1=calc_lucase(str)