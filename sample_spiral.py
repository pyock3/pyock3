import sys
sys.path.append('..')
import spiralDataGenerator as sdg
import matplotlib.pyplot as plt
import matplotlib.cbook as cbbok
points, classes = sdg.spiral_dataset_generator (density= 10, pointSigma= 0.15, spiralAngle= 360, numWings= 3, innerRadius= 0.5)

print('points  (numbers, dims) : ', points.shape, '\nclasses (numbers, dims) : ', classes.shape)

# fig, ax = plt.subplots()
plt.figure(figsize = (10, 10))
#markers = ['o','x','*']

for point in points:
    #if classes == 0:
    x, y = point    
    plt.scatter(x, y, s=50) # , marker= markers[idx])
plt.show()