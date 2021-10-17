# find the subarray in the given array which has sum zero
# i/p: l = [1,4,13,-3,-10,5] <subarray: [13,-3,-10]> => o/p: True

def solution(l):
    # naive method
    # n = len(l)
    # for i in range(n):
    #     for j in range(i+1, n+1):
    #         if sum(l[i:j]) == 0:
    #             return True
    # return False # the time complexity becomes bigO(n^2)

    # efficient method: use of prefix_sum and hashing
    pre_sum = 0
    h = set()
    for i in range(len(l)):
        # updating the presum in every iteration
        pre_sum += l[i]
        # checking if presum is zero or is already present in h
        # by checking these conditions we can return True
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False # here the time complexity becomes linear (i.e bigO(n))


l = [4,3,-2,1,1]
print(solution(l))