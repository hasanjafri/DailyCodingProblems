def is_point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)

    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Check if the point is on the same side of the line as the interior of the polygon
        if (y > min(y1, y2)):
            if (y <= max(y1, y2)):
                if (x <= max(x1, x2)):
                    if (y1 != y2):
                        x_inters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if (x1 == x2 or x <= x_inters):
                        inside = not inside

    return inside


if __name__ == '__main__':
    print(is_point_in_polygon(
        (0, 0), [(0, 0), (1, 0), (1, 1), (0, 1)]))  # False
    print(is_point_in_polygon((0.5, 0.5), [
          (0, 0), (1, 0), (1, 1), (0, 1)]))  # True
    print(is_point_in_polygon((0.5, 0.5), [
          (0, 0), (1, 0), (1, 1), (0, 1), (0, 2)]))  # True
