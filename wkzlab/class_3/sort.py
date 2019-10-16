#随机快速排序
#coding: utf-8
import random
def random_quicksort(sort_list,left,right):
    if(left<right):
        mid = random_partition(sort_list,left,right)
        random_quicksort(sort_list,left,mid-1)
        random_quicksort(sort_list,mid+1,right)


def random_partition(sort_list,left,right):
    t_1 = random.randint(left,right)     #生成[left,right]之间的一个随机数
    t_2 = random.randint(left,right)
    t_3 = random.randint(left,right)

    #三个数中选择中位数
    max_t = max(sort_list[t_1], sort_list[t_2], sort_list[t_3])
    min_t = max(sort_list[t_1], sort_list[t_2], sort_list[t_3])
    list_t = [t_1, t_2, t_3]
    mid = 0
    for item in list_t:
        if sort_list[item] != max_t or sort_list[item] != min_t:
            mid = item

    mid_point = mid
    sort_list[mid_point],sort_list[right] = sort_list[right],sort_list[mid_point]
    x = sort_list[right]
    i = left-1                         #初始i指向一个空，保证0到i都小于等于 x
    for j in range(left,right):        #j用来寻找比x小的，找到就和i+1交换，保证i之前的都小于等于x
        if(sort_list[j]<=x):
            i = i+1
            sort_list[i],sort_list[j] = sort_list[j],sort_list[i]
    sort_list[i+1],sort_list[right] = sort_list[right],sort_list[i+1]  #0到i 都小于等于x ,所以x的最终位置就是i+1
    return i+1



sort_list_eg = [-1, 9,100,1321,-564,10,0]
random_quicksort(sort_list_eg,0,len(sort_list_eg)-1)
print (sort_list_eg)