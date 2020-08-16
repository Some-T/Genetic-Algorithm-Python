import random

def crossover(parentA, parentB):
    splitLength = int(random.random() * int(len(parentA) - 1))
    child = substring(parentA, 0, splitLength) + substring(parentB, splitLength, len(parentB))
    
    return child

def fitness(individual):
    countOfOnes = 0
    for i in range(0, len(individual) - 1 + 1, 1):
        if individual[i] == "1":
            countOfOnes = countOfOnes + 1
    fitness = float(countOfOnes) / len(individual)
    
    return fitness

def mutate(individual):
    if int(random.random() * 2) == 0:
        pass
    else:
        changeIndex = int(random.random() * len(individual))
        if individual[changeIndex] == "0":
            changedCharacter = "1"
        else:
            changedCharacter = "0"
        individual = substring(individual, 0, changeIndex) + changedCharacter + substring(individual, changeIndex + 1, len(individual))
    
    return individual

def printArray(array):
    returnString = ""
    for i in range(0, len(array) - 1 + 1, 1):
        returnString = returnString + array[i] + "    "
    
    return returnString

def substring(s, start, end):
    substring = ""
    if start < len(s):
        if end > len(s):
            end = len(s)
        for index in range(start, end - 1 + 1, 1):
            substring = substring + s[index]
    
    return substring

# Main
population = [""] * (4)

population[0] = "00000000"
population[1] = "00000010"
population[2] = "00001000"
population[3] = "00100001"
generation = 0
maximumFitnessReached = False
while not maximumFitnessReached:
    print(str(generation) + "    " + printArray(population))
    bestFitness = 0
    bestIndex = 0
    secondBestIndex = 0
    for i in range(0, len(population) - 1 + 1, 1):
        currentFitness = fitness(population[i])
        if currentFitness == 1.0:
            maximumFitnessReached = True
        else:
            if currentFitness >= bestFitness:
                bestFitness = currentFitness
                secondBestIndex = bestIndex
                bestIndex = i
    for i in range(0, len(population) - 1 + 1, 1):
        population[i] = mutate(crossover(population[bestIndex], population[secondBestIndex]))
    generation = generation + 1
