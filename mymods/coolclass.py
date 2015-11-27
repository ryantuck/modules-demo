# this module contains the definition for a class

class CoolClass():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_stuff(self):

        print 'x: %s // y: %s' % (self.x, self.y)
