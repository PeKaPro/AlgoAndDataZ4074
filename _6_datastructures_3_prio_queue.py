

from queue import PriorityQueue

pq = PriorityQueue()

pq.put((5, "Brambory"))
pq.put((1, "Cesnek"))

pq.put((111, "Auto"))

pq.put((5, "Kvetak"))

print(pq.get())

pq.empty()
