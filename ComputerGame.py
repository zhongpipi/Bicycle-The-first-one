#定义游戏类
class Game:
    #初始化
    def __init__(self):
        self.hp = 1000
        self.power = 200

    #定义fight方法
    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        #hp做比较，血量多的获胜
        if final_hp > enemy_final_hp:
            print("I win!")
        else:
            print("I lost..")

game = Game()
game.fight(999,201)

