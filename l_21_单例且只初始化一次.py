class MusicPlayer:

    instance = None

    init_flag = False

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:

            cls_instance = super().__new__(cls)
            return cls_instance

        return cls.instance

    def __init__(self):

        if MusicPlayer.init_flag:

            return

        print("初始化完成")
        MusicPlayer.init_flag = True



music1 = MusicPlayer()
music2 = MusicPlayer()

print(music1)
print(music2)