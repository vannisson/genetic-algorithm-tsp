import functions as fct
import matplotlib.pyplot as plt
import dataset

auxList = []
fig, ax = plt.subplots()

for i in dataset.usc312:
  auxList.append(fct.City(x = i[0], y = i[1]))
  ax.scatter(x = i[0], y = i[1])

plt.show()
fct.geneticAlgorithmPlot(population=auxList, popSize=100, eliteSize=20, mutationRate=0.01, generations=1000)


