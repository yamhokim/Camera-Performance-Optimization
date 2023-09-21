import datetime

class FPS:
    def __init__(self):
        self.startTime = 0
        self.endTime = 0
        self.numFrames = 0

    def start(self):
        self.startTime = datetime.datetime.now()
        return self
    
    def stop(self):
        self.endTime = datetime.datetime.now()

    def update(self):
        self.numFrames += 1

    def elapsed(self):
        return (self.endTime - self.startTime).total_seconds()
    
    def fps(self):
        return self.numFrames / self.elapsed()
    
    