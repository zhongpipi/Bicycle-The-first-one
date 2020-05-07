# 定义一个类
class TongLao:
    # 初始化,有血性、武力值通过参数传入
    def __init__(self, hp, power):
        # 实例化
        self.hp = hp
        self.power = power

    # 定义see_people方法,需传入name参数
    @staticmethod
    def see_people(name):
        # 通过传入的名称输出对应的结果
        if name == "WYZ":
            print("师弟！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("不认识")

    # 定义fight_zms方法，需要用到self.hp和self.power，并会传入参数enemy_hp，enemy_power
    def fight_zms(self, enemy_hp, enemy_power):
        self.power = 10 * self.power
        self.hp = self.hp / 2

        # 判断自己和敌人的血量
        if self.hp > enemy_hp:
            print("我赢了")
        elif self.hp < enemy_hp:
            print("敌人赢了")
        else:
            print("平局")


# 定义一个虚竹类，继承童姥
class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")


fight = XuZhu(1000, 100)
fight.see_people("WYZ")
fight.fight_zms(300, 2000)
fight.read()
