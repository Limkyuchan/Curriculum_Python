class TV:
    def __init__(self, brand):
        self.brand = brand
        self.power = False
        self.channel = 0
        self.volume = 0
    
    def power_btn(self):
        self.power = not self.power
        self.display()
    
    def channel_up(self):
        if self.power:
            self.channel += 1
        self.display()
    
    def volume_up(self):
        if self.power:
            self.volume += 1
        self.display()
    
    def channel_down(self):
        if self.power:
            self.channel -= 1
        self.display()
    
    def volume_down(self):
        if self.power:
            self.volume -= 1
        self.display()
    
    def display(self):
        if self.power:
            print('┏[%-8s]┓' % self.brand)
            print('┃ ch:%-6d┃' % self.channel)
            print('┃ vol:%-5d┃' % self.volume)
            print(f'┃ 방영중   ┃')
            print('┗━━━━━━━━━━┛')
        else:
            print('┏[%-8s]┓' % self.brand)
            print('┃■■■■■■■■■■┃')
            print('┃■■■■■■■■■■┃')
            print('┃■■■■■■■■■■┃')
            print('┗■■■■■■■■■■┛')            

tv1 = TV('LG')
tv1.channel_up()
tv1.power_btn()
tv1.channel_up()
tv1.channel_up()
tv1.volume_up()
tv1.volume_up()
tv1.channel_down()
tv1.power_btn()

tv2 = TV('Samsung')
tv2.power_btn()
tv2.channel_up()
tv2.channel_up()
tv2.volume_up()

print(id(tv1))
print(id(tv2))

tv1.power_btn()