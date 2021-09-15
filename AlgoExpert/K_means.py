import random
import copy


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()

    # def get_users(self):
    #     return self.closest_users
    #
    # def remove_user(self):
    #     # removes user
    #
    # def add_user(self):
    #     # adding user
    #
    # def check_closest_users(self, list_of_all_the_users):
    #     #

    def __str__(self):
        return "%s" % self.location



# def update_centroids(centroids,num_features_per_user):
#     temp_centroid_lst = []
#     for i in range(len(centroids[0].closest_users)):
#         for j in range(num_features_per_user):
#             pass

def update_location(update_centroids, current_centroids, location):

    # print(location)
    for i in range(len(location)):
        for j in range(len(location[0])):
            temp_sum = []
            for key, value in user_feature_map.items():
                 if key in update_centroids[i]:
                    temp_sum.append(user_feature_map[key][j])
                        # print(user_feature_map[key][j])
                    print(temp_sum)
            location[i][j] = sum(temp_sum) / len(temp_sum)

    for key, value in update_centroids.items():
        current_centroids[key] = update_centroids[key]
        update_centroids[key] = set()

    return location, update_centroids, current_centroids


def get_k_means(user_feature_map, num_features_per_user, k):

    random.seed(42)

    initial_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)
    location = [copy.copy(user_feature_map.get(initial_centroid_users[i])) for i in range(k)]
    #location = [[-1, -2, -3, -4],[-1, -2, -2, 3]]
    current_centroids = {}
    update_centroids = {}

    for i in range(k):
        update_centroids[i] = set(initial_centroid_users[i].split(','))
        current_centroids[i] = set()


    for i in range(10):
        for key, value in user_feature_map.items():
            dist = []
            #if key not in update_centroids.items():
            for n in range(k):
                temp = 0
                for j in range(num_features_per_user):
                    temp += abs(user_feature_map[key][j] - location[n][j])
                dist.append(temp)
            shortest_dist = dist.index(min(dist))
            update_centroids[shortest_dist].add(key)

        location, update_centroids, current_centroids = update_location(update_centroids, current_centroids, location)
                # current_centroids[shortest_dist].append(update_centroids[shortest_dist])

    # print(update_centroids)
    # print(current_centroids)
    print(location)

    final_centroids = []
    for i in range(k):
        final_centroids.append(Centroid(location[i]))
        # final_centroids[-1].closest_users.add(current_centroids[i])


    # print(final_centroids[0].location)
    # print(current_centroids)
    #
    # print("c1")
    # print(centroids[0].closest_users)
    # print(centroids[0].location)
    #
    # print("c2")
    # print(centroids[1].closest_users)
    # print(centroids[1].location)
    #

    # print(centroids[0].closest_users)
    # print("-------------------")
    # print(centroids[1].closest_users)




    # for i in range(len(initial_centroid_users)):
    #     centroid.append(user_feature_map.get(initial_centroid_users[i]))

    distance = []
    val_lst = list(user_feature_map.values())

    # for i in range(len(val_lst)):
    #     temp_sum = 0
    #     for k in range(len(centroids)):
    #         for j in range(num_features_per_user):
    #             temp_sum += abs(val_lst[i][j] - centroids[k][j])
    #     if temp_sum != 0.0:
    #         distance.append(temp_sum)

    #
    # print(val_lst)
    # print(centroids)
    # print(distance)



    # print(distance)


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

    get_k_means(user_feature_map, 4, 2)