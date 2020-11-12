# Jacobi Algorithm
def get_value(arr, i, j):
    # if array out of bounds then return 0
    if i < 0 or i > 9 or j < 0 or j > 9:
        return 0
    else:
        return arr[i][j]


def stencil(arr, i, j):
    # if on the unchangeable corners return 35
    if (i == 9 and j == 9) or (i == 0 and j == 0):
        return 35
    sum = (get_value(arr, i-1, j) + get_value(arr, i+1, j) + get_value(arr, i, j-1) + get_value(arr, i, j+1))/4
    return sum


def get_iterations():
    try:
        iterations = int(input("Please enter number of iterations"))
    except:
        print("This is not an integer, try again.")
        iterations = get_iterations()
    return iterations


def convert_csr_matrix(v, vi, vj, c, r):
    # fill array with 0's
    arr = [[0 for i in range(c)] for j in range(r)]
    # fill out other values in array
    for val in range(len(v)):
        arr[vi[val]][vj[val]] = v[val]
    return arr


def implement_jacobi_print(iterations, rows, cols, arr):
    for i in range(iterations):
        for r in range(rows):
            for c in range(cols):
                arr[r][c] = stencil(arr, r, c)
    for r in range(rows):
        print(arr[r])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rows, cols = (10, 10)
    # fill array with 0's
    arr = [[0 for i in range(cols)] for j in range(rows)]
    # set 0,0 and 9,9 to 35
    arr[0][0] = 35
    arr[9][9] = 35
    iterations = get_iterations()
    implement_jacobi_print(iterations, rows, cols, arr)

    # Compressed Sparse Row representation
    print("CSR")
    v = [35, 35]
    vi = [0, 9]
    vj = [0, 9]
    arr = convert_csr_matrix(v, vi, vj, cols, rows)
    implement_jacobi_print(iterations, rows, cols, arr)


