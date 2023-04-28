import numpy as np

class Bakery_sales:
    name : str
    x : list
    sales : int
    distance : float

    def __init__(self, name, x, sales=0):
        self.name = name
        self.x = x
        self.sales = sales

    def __repr__(self):
        return f"{self.name}\n Features: {self.x}\n Sales: {self.sales} \n\n"

# Number of neighbors
K_Means = 4

A = Bakery_sales('A',[5,1,0],300)
B = Bakery_sales('B',[3,1,1],225)
C = Bakery_sales('C',[1,1,0],75)
D = Bakery_sales('D',[4,0,1],200)
E = Bakery_sales('E',[4,0,0],150)
F = Bakery_sales('F',[2,0,0],50)

sales = [A, B, C, D, E, F]

new_sale = Bakery_sales('N',[4,1,0])

def euclidean_distance(vector1, vector2):
    return sum((y-x)**2 for x, y in zip(vector1, vector2)) ** 0.5

for sale in sales:
    sale.distance = round(euclidean_distance(sale.x, new_sale.x),2)

sales.sort(key = lambda sale : sale.distance, reverse=False)

print(f"First {K_Means} neighbors:")
for sale in sales[:K_Means]:
    print(f'Distance from {sale.name} = {sale.distance}')

print("\nREGRESSION")
new_sale.sales = np.mean([sale.sales for sale in sales[:K_Means]])
print(f"New_sale estimated sales = {new_sale.sales}")
