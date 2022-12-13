# Pavlo Yatluk
# dz_19
# 1. Вмкористовуючи дані із файлу "cities.csv", створіть список типу:
# cities = [['city1', city2, km]...],. З отриманого списку
# створіть граф. Візіалізуйте отриманий граф.

import networkx as nx
import matplotlib.pyplot as plt
import csv

with open("C:\projects sta\pythonProject\cities - cities.csv", 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

g = nx.Graph()
for edge in list_of_csv:
    g.add_edge(edge[0], edge[1], weight = int(edge[2]))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Random Graph Generation Example")
plt.show()

nx.draw_networkx(g)