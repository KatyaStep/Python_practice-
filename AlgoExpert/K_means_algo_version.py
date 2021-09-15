import random
import copy

from collections import defaultdict
N = 10 # how many iteration algorithm would perform

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_k_means(user_feature_map, num_features_per_user, k):

    random.seed(42)

    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)
    centroids = [Centroid(user_feature_map[inital_centroid_user]) for inital_centroid_user in inital_centroid_users]

    for iteration in range(N):
        for user, features in user_feature_map.items():
            closest_centroid_distance = float("inf")
            closest_centroid = None
            for centroid in centroids:
                feature_to_centroid_distance = get_manhattan_distance(features, centroid.location)
                if feature_to_centroid_distance < closest_centroid_distance:
                    closest_centroid_distance = feature_to_centroid_distance
                    closest_centroid = centroid
            closest_centroid.closest_users.add(user)

        for centroid in centroids:
            centroid.location = get_centroid_average(centroid, num_features_per_user, user_feature_map)
            if iteration < N-1:
                centroid.closest_users.clear()
            else:
                return [[centroid.location, centroid.closest_users] for centroid in centroids]


def get_centroid_average(centroid, num_features, users):
    centroid_average = [0] * num_features
    for i in range(num_features):
        for user in centroid.closest_users:
            centroid_average[i] = centroid_average[i] + users[user][i]

    return [centroid_point / len(centroid.closest_users) for centroid_point in centroid_average]


def get_manhattan_distance(user_features, other_features):
    absolute_difference = []

    for i in range(len(user_features)):
        absolute_difference.append(abs(user_features[i] - other_features[i]))

    return sum(absolute_difference)



if __name__ == '__main__':
    user_feature_map ={
        # "uid_0": [-1.4793, -1.8954, -2.0461, -1.7109],
        # "uid_1": [-1.8284, -1.7140, -0.9893, -1.5766],
        # "uid_2": [-1.8398, -1.7896, -1.1370, -1.021],
        # "uid_3": [-1.2322, -1.8447, -1.8496, -2.4720],
        "uid_0": [-1, -2, -3, -4],
        "uid_1": [-5, -1, -1, -2],
        "uid_2": [-2, 0, -1, -3],
        "uid_3": [-1, -2, -2, 3],
    }

    print(get_k_means(user_feature_map, 4, 2))