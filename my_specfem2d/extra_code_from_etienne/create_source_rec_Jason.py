import numpy as np
import matplotlib.pyplot as plt

SOURCE_file0 = open("FORCESOLUTION","w")
STATIONS_file = open("STATIONS","w")


#rotation of the position
centre_rotation = np.array([0.2, 0.2])
n_rec = 21
angle = 360./n_rec
theta = (angle/180.) * np.pi
rot = np.array([ np.cos(theta), - np.sin(theta), np.sin(theta), np.cos(theta) ])
f0=100000

SOURCE_file0.write("FORCE  0\n")
SOURCE_file0.write("time shift:     0.0000")
SOURCE_file0.write("f0 = %f\n" % f0)
SOURCE_file0.write("latorUTM: = 0.3\n")
SOURCE_file0.write("longorUTM: = 0.2\n")
SOURCE_file0.write("depth: = 0.0\n")
SOURCE_file0.write("factor force source:             1.d0\n")
SOURCE_file0.write("component dir vect source E:     0.d0\n")
SOURCE_file0.write("component dir vect source N:     0.d0\n")
SOURCE_file0.write("component dir vect source Z_UP:  0.d0\n")

#p0 = np.array([0.3,0.2])
n=0
p0 = np.array([0.150,0.150])
STATIONS_file.write("%d AA %f %f 0.0 0.0022\n" % (n, p0[0], p0[1]))

station_store = np.zeros((n_rec,2))
station_store[n,:] = p0

for i in range(n_rec-1):
    n += 1    
 #   p0 -= centre_rotation
  #  ptemp = [p0[0]*rot[0] + p0[1]*rot[1] , p0[0]*rot[2] + p0[1]*rot[3]]
 #   p0 = ptemp + centre_rotation
#
    p0[0] += 0.1/(n_rec-1)
    station_store[n,:] = p0
    STATIONS_file.write("%d AA %f %f 0.0 0.0\n" % (n, p0[0], p0[1]))


plt.figure()
plt.plot(station_store[:,0],station_store[:,1], 'k*',label='stations')
plt.title('STATIONS', fontsize=20)
plt.legend()
plt.show()
