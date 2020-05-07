#定义类
class BubbleSort():
    #定义排序函数
    def bubble(self,list1):
        # 第一次排序n-1次，第二次排序n-2次，第三次排序n-3次，第n-1次排序1次（两个数）
        # 一共循环n-1次，第i次循环排序n-i次
        # 每次排序时，如果前面的数比后面的数大，则交换；若小或等于，则不变，继续往后面排序
        n = len(list1)
        # 有i次循环
        for i in range(n-1):
            #在第i次循环中排序
            for j in range(n-1-i):
                # 比较前后的大小然后两个数排序
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
                else:
                    continue
        print(list1)

#实例化
bubble_sort=BubbleSort()
#传参
bubble_sort.bubble([1,3,2,5,34,55,2,23,11])


# list=[1,3,2,5,34,55,2,23,11]
# n =len(list)
# for i in range(n-1):
#     for j in range(n-1-i):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
#         else:
#             continue
#
# print(list)

