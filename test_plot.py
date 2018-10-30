import matplotlib.pyplot as plt
import time
import random
import numpy as np

series_a = []
series_b = []

count = 10
def loop():
    global count
    while (count > 0) :
        time.sleep(random.randint(0,5))
        series_a.append(time.time())
        series_b.append(time.time() + random.randint(-10,10))
        count -= 1
        print(count)

def plot_me():
    plt.plot(series_a)
    plt.plot(series_b)

    plt.show()

def main():
    loop()
    plot_me()

main()
    
    
