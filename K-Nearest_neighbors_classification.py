class User:
    name : str
    reviews : list
    distance : float

    def __init__(self, name, reviews):
        self.name = name
        self.reviews = reviews
        self.distance = 0

    def __repr__(self):
        return f"Name: {self.name}\n reviews: {self.reviews}\n distance: {self.distance}\n\n"

# Number of neighbors
K_Means = 3

Andrea_r = [3, 4, 4, 1, 4]
Justin_r = [4, 3, 5, 1, 5]
Morphe_r = [2, 5, 1, 3, 1]
Antonio_r = [1, 1, 4, 3, 2]

users = []

for (name, review) in zip(["Andrea","Justin","Morphie","Antonio"], [Andrea_r, Justin_r, Morphe_r, Antonio_r]):
    users.append(User(name, review))


new_user = User("Roberto",[4, 3, 5, 2, 5])

def euclidean_distance(vector1, vector2):
    return sum((y-x)**2 for x, y in zip(vector1, vector2)) ** 0.5

for user in users:
    user.distance = round(euclidean_distance(user.reviews, new_user.reviews),2)

users.sort(key = lambda user : user.distance, reverse=False)

print(f"First {K_Means} neighbors:")
for user in users[:K_Means]:
    print(f'Distance from {new_user.name} to {user.name} = {user.distance}')

print("\nIf one of this neighbor like a movie recommend it to the new user")