'''
1.0 象限问题
from wkzlab import Coordinates

XO = (5, 5)
XN = [(3.6, 2.14, 40.15), (3.07, 5.04, 54.84), (2.98, 2.48, 17.25), (1.58, 1.6, 54.05), (3.18, 3.29, 98.66), (7.47, 1.8, 12.94), (1.44, 3.41, 78.52), (4.12, 4.32, 47.45), (6.6, 7.79, 52.87), (9.92, 2.12, 26.24), (6.3, 3.52, 42.7), (1.31, 7.82, 54.8), (2.01, 9.35, 74.17), (3.71, 3.96, 98.61), (5.33, 5.15, 15.99), (7.59, 6.14, 25.69), (8.93, 6.24, 70.85), (7.51, 4.25, 95.78), (5.49, 8.34, 23.8), (4.1, 1.61, 77.35)]

coor = Coordinates(XO=XO, XN=XN)

'''


'''
2.2 组合工具

from wkzlab import Combination

comb = Combination(total=5, choose=3)
print( comb.getElite() )
while comb.next():
    print( comb.getElite() )

'''