from collections import deque
import random
import time

a = deque(range(1,6))
b = deque()
c = deque()
def move(x,y):
    try:
        y.appendleft(x.popleft())
    except:
        pass

def avg_time(a,b,c):
    print(a,b,c)
    while True:
        iterations = 0
        a = deque(range(1,6))
        b = deque()
        c = deque()
        ts = time.time()
        while c != deque(range(1,6)):
            x,y = random.sample([a,b,c],2)
            move(x,y)
            iterations += 1
        if iterations > 50000:
            break
    te = time.time() - ts

    print(a,b,c)
    print(iterations, 'moves')
    print(te, 'seconds')

def one_round(a,b,c):
    print(a,b,c)
    iterations = 0
    while c != deque(range(1,6)):
        x,y = random.sample([a,b,c],2)
        move(x,y)
        iterations += 1
    print(a,b,c)
    print(iterations, 'moves')

# avg_time(a,b,c)
one_round(a,b,c)