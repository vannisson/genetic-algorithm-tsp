import functions as fct
import matplotlib.pyplot as plt
from dataset import usc312, sgb128, wg59

auxList = []
fig, ax = plt.subplots()

for i in usc312:
  auxList.append(fct.City(x = i[0], y = i[1]))
  ax.scatter(x = i[0], y = i[1])

plt.show()
fct.geneticAlgorithmPlot(population=auxList, popSize=500, eliteSize=20, mutationRate=0.01, generations=500)


