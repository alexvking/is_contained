'''
is_contained(array, row, col)

Returns whether the point at [row][col] is contained inside the fence, where
the array is a bit array with 0s representing open space and 1s representing
a fence. There will be a single closed fence in the provided array and it will
have no hanging edges.

Example input array in Python format:

[[0,1,1,1,0],
 [0,1,0,1,0],
 [0,1,1,1,0],
 [0,0,0,0,0],
 [0,0,0,0,0]]

Approach: start at the point at (row, col) and iterate to the right,
ending when we reach the righthand boundary of the 2D array. Count number of
times the wall is crossed. If even, the point is outside of the fence. If odd,
the point is inside. This is due to some geometric principle.

The challenge of this problem is supporting the case where we walk along a wall
rather than across it.

Insight: even in simple "across the wall" cases, it only counts as crossing a
wall if you see wall above and below you. Consider the following three cases:

    1
->  1       # We go *across* the wall and see wall above and below us.
    1


->  11111   # We go *along* a "C shape" of the wall. Because we only
    1   1   # ever see wall below us, this means that once we're on the other
    1   1   # side of the wall, we haven't actually changed state. In continuous
            # math, this is analogous to grazing the wall tangent, which does
            # not change our state.


        1
        1
->  11111   # We go *along* a "Z shape" of the wall. We first see wall below,
    1       # then we eventually also see wall above. This means that once we
    1       # are on the other side, we have changed state. In continuous math,
            # this is analogous to crossing the wall at a single infinitesimally
            # small point.

'''
def is_contained(array, row, col):
    # We define a point on the fence to be contained in the fence.
    if array[row][col] == 1:
        return True

    num_rows = len(array)
    num_cols = len(array[0])

    num_crossings = 0
    seen_above = seen_below = False

    for i in range(col, num_cols):
        current_value = array[row][i]
        if current_value == 0:
            seen_above = seen_below = False
        if current_value == 1:
            # Avoid reaching outside of the array if we are moving along the
            # top or bottom row.
            if row == 0:
                seen_above = False
            elif array[row - 1][i] == 1:
                seen_above = True

            if row == num_rows - 1:
                seen_below = False
            elif array[row + 1][i] == 1:
                seen_below = True

            if seen_above and seen_below:
                num_crossings += 1

    # The point is contained only if we crossed through an odd number of walls.    
    return num_crossings % 2 == 1


# Tests.
test1 = [[0,1,1,1,0],
         [0,1,0,1,0],
         [0,1,1,1,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

test2 = [[0,1,1,1,1],
         [0,1,0,0,1],
         [0,1,1,0,1],
         [0,0,1,0,1],
         [0,0,1,1,1]]

test3 = [[1,1,1,0,0,0],
         [1,0,1,0,0,0],
         [1,0,1,1,1,1],
         [1,0,0,0,0,1],
         [1,1,1,1,1,1]]

print is_contained(test3, 0, 5)