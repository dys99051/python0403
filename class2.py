#class2.py

str = "Not Class Member"

class GString:
    def __init__(self):
        self.str = "default"
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

g1 = GString()
g1.set("First Message")
g1.print()

g2 = GString()
g2.print()