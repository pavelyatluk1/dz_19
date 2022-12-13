# Pavlo Yatluk
# dz_19
# 2. Напишіть фунцію знаходження найкоротшого маршруту між двома населеними пунктами
# яка приймає у якості аргументів об"єкт графу і пару населених пунктів,
# а повертає маршрут ш його протяжність.

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

city_1 = input()
city_2 = input()

print(nx.shortest_path(g, city_1, city_2 , weight='weight'))
print(nx.shortest_path_length(g, city_1, city_2, weight='weight'))

nx.draw_networkx(g)