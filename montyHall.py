import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)


#x = np.random.randint(0, 3, 3, int)
#print(x)



def simulate_host(n):
    return np.random.randint(0, 3, n, int)

def simulate_guess(n):
    return np.zeros(n)

#x = simulate_host(nsim)
#y = simulate_guess(nsim)

#second_host = np.zeros(nsim)


def open_door(n, x, second_host):
    i = 0
    while i < n:
        if x[i] == 0:
            second_host[i] = np.random.randint(1, 3)
        elif x[i] == 1:
            second_host[i] = 2
        else:
            second_host[i] = 1
        i = i+1
    return


def second_guess(n, y, second_host):
    i = 0
    while i < n:
        if second_host[i] == 1:
            y[i] = 2
        else: y[i] = 1
        i = i+1
    return




def correct(n, x, y):
    count = 0
    i = 0
    while i< n:
        if x[i] == y[i]:
            count = count + 1;
        i = i+1
    return count

#def plot_result(numCorrect):


#execute the functions and store the obtained values in appropriate variables

simulations = 10000;

x1 = simulate_host(simulations)
x2 = simulate_guess(simulations)


second_chance = np.zeros(simulations)


open_door(simulations, x1, second_chance)



second_guess(simulations, x2, second_chance)


result = correct(simulations, x1, x2)


print(result)

labels = 'Correct Guess', 'Wrong Guess'
sizes = [ result, simulations - result]
colors = [ 'green', 'red']

plt.pie( sizes, labels=labels, colors=colors, startangle=140, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
