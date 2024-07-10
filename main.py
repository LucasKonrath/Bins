import matplotlib.pyplot as plt
import numpy as np

def plotBarGraph(bin_filled):
    plt.bar(np.arange(len(bin_filled)), bin_filled, label="Trash")
    plt.legend()

    plt.xlabel('Bin Number')
    plt.ylabel('Trash stored')
    plt.title('Bin allocation')

    plt.show()    

def firstFit(weights, capacity):
    bins = 0
    size = len(weights)
    bin_capacities = [0] * size
    bin_filled = [0] * size
    
    for i in range (size):
        currBin = 0
        
        while(currBin < bins):
            if (bin_capacities[currBin] >= weights[i]):
                bin_capacities[currBin] = bin_capacities[currBin] - weights[i]
                bin_filled[currBin] += weights[i]
                print("currBin " + str(currBin) + " i: " + str(i) + " capacity:" + str(bin_capacities[currBin]))
                plotBarGraph(bin_filled)
                break
            currBin += 1
        
        if(currBin == bins):
            bin_capacities[currBin] = capacity - weights[i]
            bin_filled[currBin] += weights[i]
            print("currBin " + str(currBin) + " i " + str(i) + " capacity:" + str(bin_capacities[currBin]))
            plotBarGraph(bin_filled)
            bins += 1
            
    return bins


trash = [ 3, 3, 3, 3, 2, 5, 1 ]
trash.sort(reverse = True)
cap = 5

print("Bins required: ", firstFit(trash, cap))
