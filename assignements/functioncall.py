#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RGCET
#
# Created:     10/03/2018
# Copyright:   (c) RGCET 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(x,c,b,d):
    a=x
    if(a<20):
        print("Good Boy"+ c)
    elif(a>20 and a<30):
        print("Bad Boy"+ b)
    else:
        print("worst Boy"+ d)


if __name__ == '__main__':
    main(25,"Manish","Sudar","Pushparaj")
