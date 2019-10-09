import math
'''
作业：

x^6 - 6x^4 + x^3 + 12x + 根号3 = 0   求一个实解，精度10^-6  复数解
'''

def function( x:float ) -> float:
    return math.pow(x, 6) - 6*math.pow(x, 4) + math.pow(x, 3) + 12*x + math.sqrt(3)

def main():
    x1 =-1.0
    x2 = 1.0
    x3 = (x1 + x2) / 2
    y1 = function(x1)
    y2 = function(x2)
    y3 = function(x3)

    if y1 * y2 < 0:
        if y1 * y3 < 0:
            x2 = x3
            y2 = y3
        if y2 * y3 < 0:
            x1 = x3
            y1 = y3
        while math.fabs(y3) >= math.pow(10, -6):
            x3 = (x1 + x2) / 2
            y3 = function(x3)
            if y1 * y3 < 0:
                x2 = x3
                y2 = y3
            if y2 * y3 < 0:
                x1 = x3
                y1 = y3

    print(x3)
    print(y3)

#执行函数
main()