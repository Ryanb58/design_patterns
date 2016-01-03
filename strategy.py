'''
Author: Taylor Brazelton
Updated: 1/2/2016
'''

class shape(object):
    def __init__(self, function=None):
        if function != None:
            self.type = function
    def type(self):
        print "Normal Shape"

def squareType():
    print "Square Shape"

def circleType():
    print "Circle Shapes"

# If not a module, then run this sequence of commands.
if __name__ == "__main__":
    # Each of the variables are assigned to an shape object instance.
    normal_shape = shape()
    square_shape = shape(squareType) # passing in the type of shape that it is.
    circle_shape = shape(circleType)

    # They return their respective types.
    normal_shape.type()
    square_shape.type()
    circle_shape.type()
