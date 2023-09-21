from datetime import datetime

class CountsPerSec:

    def __init__(self):
        self.start_time = None
        self.num_occurences = 0

    def start(self):
        self.start_time = datetime.now()
        return self
    
    def increment(self):
        self.num_occurences += 1

    def countersPerSec(self):
        elapsed_time = (datetime.now() - self.start_time).total_seconds()
        return (self.num_occurences / elapsed_time)
