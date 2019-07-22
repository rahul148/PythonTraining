#simple way to check wether the string is persent in string
s=str(input("enter the string :"))
sub=str(input("enter the string to check it persent or not::"))
if sub in s:
    print("the given:",sub,"string is persent")
else:
    print("the given:",sub,"string not persent enter the otheer")
