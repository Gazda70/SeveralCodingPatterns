def legoBlocks(n, m):
    # Write your code here
    # calculate the module value to limit the number
    # that will be our answer
    mod = 10 ** 9 + 7
    # let's think on how many ways we can build a wall
    # of given length - for example, a wall of length 0
    # can be build in one way - no bricks used, a wall
    # of length 1 also can be build in one way - using
    # one brick of size 1, a wall of size 2 - in two ways
    # using two bricks of size 1 or one brick of size 2, etc
    # we observe a pattern emerge - for every wall's length
    # the number of ways in which we can build a wall of given length is equal to the sum of ways we can build
    # last 4 walls of shorter length
    width = [1, 1, 2, 4]

    # if we want to get to know the number of ways to build a wall of given length, we must sum last 4 numbers
    # of ways to build a wall of shorter length, remember to use our modulo
    while len(width) <= m:
        width.append(sum(width[-4:]) % mod)

    # if we want to get to know the total number of valid combinations of building the wall, we have to raise
    # each number of ways to build a horizontal level of wall to the power of its height
    total = [pow(val, n, mod) for val in width]

    # now it's time to calculate the number of ways a invalid horizontal level of wall can be build
    invalid = [0, 0]

    # for every length of wall from two to our set length plus one
    for cur in range(2, m + 1):
        # temporary array for number of possible ways to build the level
        tmp = []
        # for every possible length of the left part of the level
        for lwidth in range(1, cur):
            # difference of possible ways of building a wall and of building and
            # invalid wall for the length of the left side
            l = total[lwidth] - invalid[lwidth]
            # number of possible ways of build a valid wall for the length of the right side
            # we have to consider only the number of valid ways, because the loop that sets the length
            # of invalid side iterates over the whole length of the level of the wall
            r = total[cur - lwidth]
            # append the sum of ways to build an invalid level to the temporary array -
            # - use the principle of multiplication
            tmp.append(l * r)
        # append the number of ways of building an invalid wall to the result array, modulo to stay witihn our range
        invalid.append(sum(tmp) % mod)
    # return the difference between the total number of ways we can build a wall minus the number of invalid ways
    # which gives us the number of valid ways, remember to use modulo
    return (total[m] - invalid[m]) % mod


legoBlocks(3, 2)