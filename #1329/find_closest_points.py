import math


def find_closest_points(points):
    min_distance = float("inf")
    closest_point_1 = None
    closest_point_2 = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = math.sqrt(
                (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            )
            if distance < min_distance:
                min_distance = distance
                closest_point_1 = points[i]
                closest_point_2 = points[j]

    return [closest_point_1, closest_point_2]


if __name__ == "__main__":
    print(
        find_closest_points([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)])
    )  # Outputs [(1, 1), (-1, -1)]
