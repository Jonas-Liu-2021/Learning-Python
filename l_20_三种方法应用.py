class Game:

    top_score = 0

    def __init__(self, name):

        self.player_name = name

    @staticmethod
    def game_help():

        print("游戏帮助： 让僵尸进入大门")

    @classmethod
    def show_top_score(cls):

        print("历史最高分： %s" % cls.top_score)

    def start_game(self):

        print("%s 开始游戏" % self.player_name)


Game.game_help()

Game.show_top_score()

xiaoming = Game("小明")

xiaoming.start_game()
