class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)

def setSilentMode(t):
    t.volume = 2

myTV = Television(11, 10, True)
setSilentMode(myTV)
myTV.show()