import math
import string

litertometer = 1e-3
grav = 9.81
density = 1.225
atmos = 101325 
bottlemass = 0.1779
Area = 615.75e-6
Time𐤃= 0.0001

PressureInitial = 551580.6
VolumeFinal = 0.002 #in meter^3

def main():
  VolumeInitial = float(input("Water Amount: "))
  Volumemeters = VolumeInitial * litertometer
  watermass = VolumeInitial 

  airvolume = VolumeFinal - Volumemeters
  P_current = PressureInitial * (airvolume / VolumeFinal)

#actual calculations
  Pressure_Final = (PressureInitial * airvolume) / VolumeFinal
  v = 0.0

  while P_current > atmos and Volumemeters > 0:

    DynamicPressure = P_current - atmos

    vEXIT = math.sqrt(2.0 * DynamicPressure / 1000)
    thrust = 1000 * Area * vEXIT ** 2

    totalmass = bottlemass + watermass

    netforce = thrust - (totalmass * 6)

    accel = netforce / totalmass

    v += accel * Time𐤃

    deltaV = Area * vEXIT * Time𐤃 
    Volumemeters = max(0, Volumemeters -deltaV)

    watermass = VolumeFinal * 1000
    
    airvolume= VolumeFinal - Volumemeters

    P_current = PressureInitial * ((VolumeFinal - VolumeInitial * litertometer)/ airvolume) * (airvolume/ VolumeFinal)


  print("Velocity(in m/s): " + str(v))

while True:
  main()
