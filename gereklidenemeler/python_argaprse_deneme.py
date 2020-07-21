import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r" , "--radius" , type = int,required = True ,help ="Radius of Cylinder" )
parser.add_argument("-H" , "--height" , type = int,required = True ,help ="Height of Cylinder" )
args = parser.parse_args()


def calculate_volume(radius , height):
    vol = (math.pi) *(radius **2 ) *(height)
    return vol

print(calculate_volume(args.radius,args.height))
print("is everything ok bro")
