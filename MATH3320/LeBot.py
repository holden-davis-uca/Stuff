#MATH 3320 - CRN 21867
#Holden Davis
#Group 9 Project - Fall 2021 - Dr. Le

#numpy for linear algebra calculations
import numpy as np
#matplotlib for visualization
import matplotlib.pyplot as plt

#Either input coordinates manually or use presets
cond = input("Manually enter components + coordinates (y/n)? --> ")
botx=0.0
boty=0.0
if cond == "y" or cond == "Y":
  destx = input("Enter destination x position --> ")
  desty = input("Enter destination y position --> ")
  ux = input("Enter vector U x component --> ")
  uy = input("Enter vector U y component --> ")
  vx = input("Enter vector V x component --> ")
  vy = input("Enter vector V y component --> ")
  #String to Integer conversion
  destx = int(destx)
  desty = int(desty)
  ux = int(ux)
  uy = int(uy)
  vx = int(vx)
  vy = int(vy)
else:
  destx=60.0
  desty=60.0
  ux = 5.0
  uy = 10.0
  vx = 10.0
  vy = 5.0

#Draw the origin and destination points
plt.scatter(botx, boty, label="Origin")
plt.scatter(destx, desty, label="Destination")

#Create two numpy arrays, one from the movement vectors and one from the destination point
a = np.array([[ux, vx],[uy ,vy]])
b = np.array([destx, desty])
try:
    #Solve for solution
    x = np.linalg.solve(a,b)
    print("\nStarting position is " + str(botx) + ", "+ str(boty) + "!")
    print("Destination position is " + str(destx) + ", " + str(desty) + "!")
    print("Movement  vector U = [" + str(ux) + ", " + str(uy) + "]" )
    print("Movement  vector V = [" + str(vx) + ", " + str(vy) + "]" )
    print("Solution is scalar " + str(x[0]) + " * vector U and scalar " + str(x[1]) + " * vector V!")
    
    print("\n\n<!---STARTING--->!\n\n")
    
    print("LeBot is at (" + str(botx) + ", " + str(boty) + "), Destination is at (" + str(destx) + ", " + str(desty) + ")")
    
    print("Moving " + str(x[0]) + " * [ " + str(ux) + ", " + str(uy) + "]")
    
    upointx = x[0] * ux
    upointy = x[0] * uy
    
    plt.plot((botx, upointx), (boty, upointy), label= str(x[0]) +" * U Vector")
    
    #Execute movement with U Vector first
    botx += x[0] * ux
    boty += x[0] * uy
    
    print("LeBot is at (" + str(botx) + ", " + str(boty) + "), Destination is at (" + str(destx) + ", " + str(desty) + ")")
    
    print("Moving " + str(x[1]) + " * [ " + str(vx) + ", " + str(vy) + "]")
    
    vpointx = botx + (x[1] * vx)
    vpointy = boty + (x[1] * vy)
    
    plt.plot((botx, vpointx), (boty, vpointy), label=str(x[1]) + " * V Vector")
    
    #Execute movement with V Vector next
    botx += x[1] * vx
    boty += x[1] * vy
    
    #Gimmick to allow us to arrive at the destination due to rounding issues
    botx = round(botx)
    boty = round(boty)
    
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend(loc="best")
    
    #Arrived
    if botx == destx or boty == desty:
      print("LeBot is at (" + str(botx) + ", " + str(boty) + "), Destination is at (" + str(destx) + ", " + str(desty) + ") - Destination Reached!")
      plt.title("LeBot's Successful Adventure!")
    else: 
        print("Unable to reach destination!")
        plt.title("LeBot's Unsuccessful Adventure!")
    plt.show()
    print("\n\n<!---STOPPING--->!\n\n")
    
    #Catch situation where one manually enters linearly dependent vectors
    #If that's the case, then LeBot's movement is the span of a single vector (a line), as opposed to the span of both vectors (the whole x-y plane)
except Exception:
    print("\nUnable to reach destination! - Linearly Dependent Movement Vectors")
    plt.title("LeBot's Unsuccessful Adventure!")
    plt.show()
    print("\n\n<!---STOPPING--->!\n\n")
    
