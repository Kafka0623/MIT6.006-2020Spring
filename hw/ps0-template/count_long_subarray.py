def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    n = len(A)
    if n == 0:
        return 0

    max_len = 1      # 当前已知的最长递增子数组长度
    count = 0        # 达到 max_len 的段数
    curr = 1         # 当前递增段长度

    for i in range(1, n):
        if A[i] > A[i-1]:
            curr += 1
        else:
            # 递增段在 i-1 处结束，结算这一段
            if curr > max_len:
                max_len = curr
                count = 1
            elif curr == max_len:
                count += 1
            curr = 1  # 重新开始新的一段

    # 循环结束，结算最后一段
    if curr > max_len:
        max_len = curr
        count = 1
    elif curr == max_len:
        count += 1

    return count
