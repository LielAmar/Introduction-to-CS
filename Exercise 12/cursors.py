class Cursors:
    """
    An iterable object that returns the next cursor in the list
    """
    
    def __init__(self):
        self.index   = 0

        self.cursors = ["circle", "clock", "cross", "dotbox", "exchange", "fleur",
                "heart", "man", "mouse", "pirate", "plus", "shuttle", "sizing",
                "spider", "spraycan", "star", "target", "tcross", "trek", "watch", 
                "arrow"
        ]


    def __iter__(self):
        return self.cursors

    def __next__(self):
        self.index += 1

        if self.index >= len(self.cursors):
            self.index = 1

        return self.cursors[self.index-1]