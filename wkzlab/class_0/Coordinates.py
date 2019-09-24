class Coordinates():
    '''
    象限问题：

    在坐标系的各个象限内寻找和 XO 点最近的点的平均值
    (前提： 没有在坐标轴上的点！)
    数据格式：
    input：  XO： (x1, x2, x3, ......)
             XN：[
             (x1, x2, x3, ......, y)
             (x1, x2, x3, ......, y)
             (x1, x2, x3, ......, y)
             ]

    output use;  nearest = [
                {'quadrant': *, 'distance': *, 'value': * }
             ]
    获得结果：
        返回平均值
    '''

    def __init__(self, XO: tuple, XN: list):
        self.XO = XO # 原点的坐标
        self.XN = XN # 坐标系上的所有点
        self.nearest = []

        if 0 == len(XO):
            print('原点的坐标不能为空')

        if 0 == len(XN):
            print('坐标系的点不能为空')

    def __transfer_binary(self, binary_list:list ) -> int:
        decimal_number = 0
        reversed_binary_list = binary_list[::-1]
        for index, val in enumerate(reversed_binary_list):
            power_num = index #次方数
            if bool(val):
                decimal_val = 1
                for n in range(0, power_num):
                    decimal_val *= 2
                decimal_number += decimal_val
        return decimal_number



    def __get_distrence_between_two_points(self, X1:tuple, X2:tuple) -> (int, float):
        '''
        两点之间距离
        :param X1: 第一个点坐标
        :param X2: 第二个点坐标
        :return: quadrant  象限, distance 距离  为了保持精度 不开根号 （这个距离只是对比大小 所以始终不用开根号）
        '''
        quadrant_list = []  # 计算象限的数组  (1, 0, 1, 1, ......)
        distance = 0.0 # 距离
        for n in range(0, len(X1)-1 ):  #最后一个值为y
            # 计算距离:
            distance += ( X1[n] - X2[n] ) * ( X1[n] - X2[n] )
            # 判断象限：
            quadrant_list.append( int( X1[n] > X2[n] ) )
        #计算象限：
        quadrant = self.__transfer_binary(quadrant_list) # 象限

        return quadrant, distance


    def get_result(self):
        '''
        返回最近的各个象限的点的平均值
        :return: result: float
        '''
        '''
        nearest = [{'quadrant': *, 'distance': *, 'value': * }, ......]
        '''
        nearest = []  #各个象限最近的点的集合
        for point in self.XN:
            quadrant, distance = self.__get_distrence_between_two_points(self.XO, point)
            value = point[-1]
            near = {'quadrant': quadrant, 'distance': distance, 'value': value} #该点的信息

            flag = False #是否有该象限的点
            for item in nearest:
                if item['quadrant'] == near['quadrant']:
                    flag = True
                    if near['distance'] > item['distance']:
                        item['distance'] = near['distance']
                        item['value'] = near['value']
            if not flag:
                nearest.append(near)
        average_value = 0 #平均数
        for item in nearest:
            average_value += item['value']
        average_value /= len(nearest)
        return average_value

    def generate_test_data(self, dimension_number, how_many_data):
        '''
        获得测试数据
        :param dimension_number: 维度数
        :param how_many_data: 生成多少数据
        :return:
        '''
        import random

        XN = []
        for num in range(0, how_many_data):
            point = []
            for num in range(0, dimension_number):
                point.append( round( (random.random()*10) , 2) )  # add x
            point.append( round( (random.random()*100) , 2) ) # add y
            point = tuple(point)
            XN.append(point)

        return XN





'''
测试 数据

二维：
XO = (5, 5 )
XN = [(3.6, 2.14, 40.15), (3.07, 5.04, 54.84), (2.98, 2.48, 17.25), (1.58, 1.6, 54.05), (3.18, 3.29, 98.66), (7.47, 1.8, 12.94), (1.44, 3.41, 78.52), (4.12, 4.32, 47.45), (6.6, 7.79, 52.87), (9.92, 2.12, 26.24), (6.3, 3.52, 42.7), (1.31, 7.82, 54.8), (2.01, 9.35, 74.17), (3.71, 3.96, 98.61), (5.33, 5.15, 15.99), (7.59, 6.14, 25.69), (8.93, 6.24, 70.85), (7.51, 4.25, 95.78), (5.49, 8.34, 23.8), (4.1, 1.61, 77.35)]



'''
