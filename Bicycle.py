#定义Bicycle类
class Bicycle:
    #定义run方法，参数km是里程数，通过调用返回
    def run(self,km):
        print("自行车骑行里程数km",km)

bike=Bicycle()
bike.run(10)

#定义EBicycle类,继承Bicycle
class EBicycle(Bicycle):
    #初始化电量
    def __init__(self,valume):
        #实例化
        self.valume1=valume

     #打印电池电量
    def get_valume(self):
        print("当前电量为",self.valume1)

    #定义充电电量方法
    def fill_charge(self,vol):
        print("充电电量为",vol)

    #定义里程run方法
    def run(self,km):
        #电量支持的里程数
        max_miles = self.valume1 * 10
        #通过传入的里程数和电量支持的里程数两个比较，判断是否需要骑行
        miles = km - max_miles
        if miles<0:
            print("电瓶车骑行里程数",km)
        else:
            #如果直接写self.run()，子run会覆盖父类的run
            #应该传入自行车骑行的里程数，即非电瓶车骑行的里程数
            super().run(miles)

#初始化类EBicycle时传入参数值
bike = EBicycle(1)
bike.run(100)