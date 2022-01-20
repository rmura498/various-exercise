"""Given a list of integers, find the nearest pair
that sum to a given target.
Nearest refers to the positions in the list"""

elements = [1, 5, 3, 6, 4, 2]
target = 7
distances = []
pairs = []


def compute_pairs(elements, target):
    n = len(elements)
    for idx0 in range(n):
        for idx1 in range(idx0 + 1, n):
            if elements[idx0] + elements[idx1] == target:
                distances_between_idx = idx1 - idx0
                distances.append(distances_between_idx)
                pairs.append((elements[idx0], elements[idx1]))
    return distances, pairs


def print_pair(distaces, pairs):
    for i in range(len(pairs)):
        print("pair: ", pairs[i], "distance: ", distaces[i])


def nearest_pairs(pairs, distances):

    nearest = min(distances)
    for i, distance in enumerate(distances):
        if nearest == distance:
            nearest_pair = pairs[i]
            near = [nearest]
            pair = [pairs[i]]
            return near, pair
    print("There aren't pairs")


distances, pairs = compute_pairs(elements, target)

print_pair(distances, pairs)
nearest, pair = nearest_pairs(pairs, distances)
print("The nearest pair:")
print_pair(nearest, pair)
