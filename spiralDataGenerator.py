from math import pi, cos, sin
import numpy as np
import random

GPU = True

def spiral_dataset_generator (density=1, innerRadius= 0.2, maxRadius=0.99, numWings=3, spiralAngle= 360, pointSigma = 0.1):
    # density : number of points per each angle in degrees
    # innerRadius : center spacing by %
    # maxRadius : max reach in radius 
    # numWings : number of wings
    # spiralAngle : spiral rotating angle in degrees
    # pointSigma : random distribution range of points

    spirals_data = []
    spirals_class = []

    max_x = (spiralAngle/180 * pi) + 2* pointSigma + 2* innerRadius     
    max_y = (spiralAngle/180 * pi) + 2* pointSigma + 2* innerRadius
    
    mmax_x = 0
    mmax_y = 0

	# Generate points   
    for wingNum in range(numWings):

        angle_offset = 2*pi/numWings
        
        for angle in range(spiralAngle):	# 360도 한바퀴를 뺑 돈다.
            _radial = angle * pi/180
            _radius = _radial / maxRadius + innerRadius
            
            radial = _radial #random.normalvariate(_radial, _radial/30)
            radius = _radius #random.normalvariate(_radius, _radius/30)
            
            # Get x and y coordinates
            for i in range(density):
                x = random.normalvariate(radius * cos(radial + angle_offset * wingNum), pointSigma) / max_x
                y = random.normalvariate(radius * sin(radial + angle_offset * wingNum), pointSigma) / max_y
                
                if x > maxRadius:
                    x = maxRadius
                if y > maxRadius:
                    y = maxRadius
                
                if np.abs(x) > mmax_x:
                    mmax_x = np.abs(x)
                if np.abs(y) > mmax_y:
                    mmax_y = np.abs(y)
        
                # Format: 8.5f
                x = float(format(x, '8.5f'))
                y = float(format(y, '8.5f'))

                spirals_data.append([x, y])
                # spirals_class.append([wingNum])
                tmp = []
                for j in range(numWings-1) :
                    tmp.append(0)
                tmp.insert(wingNum, 1)
                spirals_class.append(tmp)                

        
    print('mmax_x : ', mmax_x)
    print('mmax_y : ', mmax_y)
 
    return  np.array(spirals_data, dtype= object), \
            np.array(spirals_class, dtype= object).reshape((-1, numWings))