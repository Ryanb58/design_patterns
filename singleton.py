
class Singleton:
    # Intialization of the instance and store the passed in function.
    def __init__(self, classToSinglize):
        self.singleClass = classToSinglize
        self.instance = None

    #On function call, ensure that only the single instance is being used.
    def __call__(self,*args,**kwds):
        if self.instance == None:
            # If the instance isn't already set, set it to this function with these arguments.
            self.instance = self.singleClass(*args,**kwds)
        return self.instance

class math(object):
    def __init__(self):
        self.num = 0
    def add(self, x):
        self.num = int(self.num) + x
    def sub(self, x):
        self.num = int(self.num) - x

    # Ensure when printing out this object, it prints the wanted information.
    def __str__(self):
        return str(self.num)

# Have our singleton class overwrite the default __init__ and __call__ func's.
math = Singleton(math)

# Setup different variables to the same class.
x=math()
y=math()
z=math()
x.add(2) # num = 2
y.add(4) # num = 6
z.sub(1) # num = 5
print(x)
print(y)
print(z)
print(x is y is z)
