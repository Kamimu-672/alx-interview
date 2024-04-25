def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Pascal's triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle

def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Args:
        triangle (list of lists): Pascal's triangle represented as a list of lists of integers.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

