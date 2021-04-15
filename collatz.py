from treelib import Node, Tree
from matplotlib import pyplot as plt
import pylab


def collatz(n):
    if (n%2 == 0):
        return int(n/2)
    else:
        return (n*3)+1

def create_collatz_step_list(n):
    step_list = [n]
    while (n != 1):
        next_step = collatz(n)
        step_list.append(next_step)
        n = next_step
    return step_list

def collatz_step_count(n):
    step_count = 0
    while (n != 1):
        n = collatz(n)
        step_count += 1
    return step_count

# in-terminal tree display of the value after each step, using:
# https://medium.com/analytics-vidhya/visualizing-the-collatz-conjecture-with-python-17242560ebac
def collatz_tree(n):
    tree = Tree()
    tree.create_node("1",1)
    step_list = [n]
    while (n != 1):
        n = collatz(n)
        step_list.insert(0,n)
    for i in range (1,len(step_list)):
        tree.create_node(str(step_list[i]), step_list[i], parent = step_list[i-1])
    tree.show()

# plots the value after each step until reaching 1, using starting value n
def collatz_plot(n):
    step_list = create_collatz_step_list(n)
    step_number_list = list(range(0,len(step_list)))
    plt.plot(step_number_list, step_list)
    plt.xlabel("number of steps")
    plt.show()
        
# plots the number of steps to reach 1 for the starting values up to n
def collatz_step_count_scatterplot(n):
    start_value = list(range(1,n+1))
    step_count = list(map(collatz_step_count,start_value))
    plt.scatter(start_value, step_count, s=5)
    plt.xlabel("starting number")
    plt.ylabel("steps")
    plt.show()
    
def main():
    #collatz_tree(10)
    #collatz_plot(27)
    collatz_step_count_scatterplot(100000)

if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        pass
