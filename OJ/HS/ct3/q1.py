for t in range(int(input())):
    string = input()
    n = len(string)
    max_len = 0  # Initialize result

    # A 2D table where sum[i][j] stores
    # sum of digits from str[i] to str[j].
    # Only filled entries are the entries
    # where j >= i
    Sum = [[0 for x in range(n)]
           for y in range(n)]

    # Fill the diagonal values for
    # substrings of length 1
    for i in range(0, n):
        Sum[i][i] = int(string[i])

        # Fill entries for substrings
    # of length 2 to n
    for length in range(2, n + 1):

        # Pick i and j for current substring
        for i in range(0, n - length + 1):

            j = i + length - 1
            k = length // 2

            # Calculate value of sum[i][j]
            Sum[i][j] = (Sum[i][j - k] +
                         Sum[j - k + 1][j])

            # Update result if 'len' is even,
            # left and right sums are same and
            # len is more than maxlen
            if (length % 2 == 0 and
                    Sum[i][j - k] == Sum[(j - k + 1)][j] and
                    length > max_len):
                max_len = length

    print(max_len)

