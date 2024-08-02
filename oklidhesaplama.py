
import math

points = [(3, 5), (4, 6), (7, 9)]  

#Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(x1, x2):
    return math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2)

#Tüm nokta çiftleri arasındaki mesafeleri hesapla
distances= []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

#Minimum mesafeyi bulmak için
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")