import json

#variables
airpressure = 0.0
fueltankarea = 0.0
nosslearea = 0.0
fueltankvolume = 0.0
testwatercount = 0.0
testaircount = 0.0

#functions
def simulate(p, Fa, Na, Fv):
    p/Na = f

while True:
    airpressureinput = input("What is the air pressure(in pascals)? ")
    fueltankareainput = input("What is the fuel tank area(in square units)? ")
    nossleareainput = input("What is the nossle area(in square units)? ")
    fueltankvolumeinput = input("What is the fuel tank volume(in cubic units)? ")

    while True: #actuall loop
        testaircount = fueltankvolume - testwatercount
        
        #stroke up steps:
        testwatercount = testwatercount + 0.1
        
        simulate(airpressureinput, fueltankareainput, nossleareainput, fueltankvolumeinput)
