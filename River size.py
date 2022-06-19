def river_size(array):
    """
    Return the lengths of the rivers. River is adjacent 1, not diagonal.
    For instance, in [
    [1,1,0],
    [0,1,0],
    [0,0,0]
    ]

    river is ..1,1..
               ..1..

    """
    rivers = []
    marked = set()
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == 1 and (x, y) not in marked:
                length = 1
                marked.add((x, y))
                stack = [(x, y)]

                while stack:
                    current = stack.pop()
                    neighbours = get_neighbours(current, array)
                    for n in neighbours:
                        pos_x, pos_y = n
                        if array[pos_x][pos_y] == 1 and (pos_x, pos_y) not in marked:
                            length += 1
                            stack.append(n)
                            marked.add((pos_x, pos_y))
                rivers.append(length)
    return rivers


def get_neighbours(pos, matrix):
    len_row = len(matrix)
    len_col = len(matrix[0])
    x, y = pos
    ns = []
    if (x >= 0) and (x < len_row - 1):
        ns.append((x+1, y))
    if (x > 0) and (x <= len_row - 1):
        ns.append((x-1, y))
    if (y >= 0) and (y < len_col - 1):
        ns.append((x, y+1))
    if (y > 0) and (y <= len_col - 1):
        ns.append((x, y-1))

    return ns


if __name__ == '__main__':
    river = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    river2 = [
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    river3 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print(river_size(river))
    print(river_size(river2))
    print(river_size(river3))
