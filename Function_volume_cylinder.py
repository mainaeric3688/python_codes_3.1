'''
python program to calculate the volume of a cylinder
'''
def volume(radius,height):
  volume=(3.142*radius**2)*height
  return volume
#calls the function
volume=(3.142*7**2)*21  
print("volume of the cylinder is="+str(volume))    
 