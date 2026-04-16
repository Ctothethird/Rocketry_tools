import math

litertometer = 1e-3
grav = 9.81
density = 1.225
atmos = 101325 

PressureInitial = 551580.6
VolumeFinal = 0.002 #in meter^3

def main():
  VolumeInitial = input("Water Amount: ")
  VolumeInitial* = (2-VolumeInitial) * litertometer

#actual calculations
  Pressure_Final = (PressureInitial * VolumeInitial*) / VolumeFinal

  airdens = density * (Pressure_Final / atmos)

  DynamicPressure = PressureInitial - Pressure_Final

  PressureTotal = PressureInitial + DynamicPressure

  v = math.sqrt(2.0 * DynamicPressure / airdens)

  print("Velocity(in m/s): " + string(v))
  print("DynamicPressure(in Pa): " + string(DynamicPressure))
