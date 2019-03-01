def apply_async(func, args, *, callback):
    # callback need to record the used number of func. 
    result = func(*args)
    callback(result)

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, x):
        self.count += 1
        print("The result is {}, \
               The function has been called {}".\
               format(x, self.count))

def add(x, y):
    return x + y

if __name__ == "__main__":
    x, y = 0, 0
    counter = Counter()
    
    for idx in range(100):
        apply_async(add, (x, y), callback=counter)
        x += 1
        y += 1




