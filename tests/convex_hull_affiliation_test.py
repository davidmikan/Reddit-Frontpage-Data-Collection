import pandas as pd
import numpy as np
from scipy.spatial import Delaunay

# Hier den eigenen Path zum Datensatz angeben
path = 'datapoints_hot.csv'

# Wir laden die Datenpunkte der populären Posts aus der .csv Datei
hot_points = pd.read_csv(path)

# Die Datenpunkte werden nun mithilfe eines zufälligen numpy-Arrays 
# bestehend aus booleans im Verhältnis 8:2 aufgeteilt
# in ein Sample für die konvexe Hülle und eines zum Testen der Representativität dieser
mask = np.random.rand(len(hot_points)) < 0.8
hull_sample = hot_points[mask]
test_sample = hot_points[~mask]

# Mithilfe eines 2-dimensionellen numpy-Arrays der Werte 'Time' und 'Score'
# des hull_samples wird eine konvexe Hülle erstellt, mit der Berechnungen durchgeführt werden können
test_sample_npar = np.c_[test_sample['Time'], test_sample['Score']]
hull_sample_npar = np.c_[hull_sample['Time'], hull_sample['Score']]
hot_convex_hull = Delaunay(hull_sample_npar)

in_hull = []

# Es wird für jeden Punkt der Testprobe, der in der konvexen Hülle liegt,
# True angehängt, ansonsten False
for p in test_sample_npar:
    in_hull.append(hot_convex_hull.find_simplex(p)>=0) 
# Nach der Dokumentation von scipy [https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.find_simplex.html]
# liefert Delaunay.find_simplex einen Wert zwischen 0 und 1, wenn der Punkt in der 
# konvexen Hülle liegt, und -1 für Punkte außerhalb der Hülle

print(f'In konvexer Hülle liegende Punkte der Testprobe: {in_hull.count(True)}')
print(f'Außerhalb der konvexen Hülle liegende Punkte der Testprobe: {in_hull.count(False)}')