import math

litertometer = 1e-3
grav = 9.81
density = 1.225
atmos = 101325 

PressureInitial = 551580.6
VolumeFinal = 0.002 #in meter^3

def dobetter(prompt):
  while True:
    try:
      val = float(input(prompt))
      if val > 0:
        return val
      print("Dude it gotta be not negative be smarter yo")
    except ValueError:
      print("Dude you put a number in frickin idiot yo")

def main():
  VolumeInitial = dobetter("Water Amount: ")
  VolumeInitial* = (2-VolumeInitial) * litertometer

#actual calculations
Pressure_Final = (PressureInitial * VolumeInitial*) / VolumeFinal

airdens = density * (Pressure_Final / atmos)

DynamicPressure = PressureInitial - Pressure_Final

PressureTotal = PressureInitial + DynamicPressure

v = math.sqrt(2.0 * DynamicPressure / airdens)

print("Velocity(in m/s): " + string(v))
print("DynamicPressure(in Pa): " + string(DynamicPressure))
