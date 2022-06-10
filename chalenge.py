def find_runner_up(scores : list):
    scores.sort()
    scores.reverse()
    # print("List start: ")
    first = scores[0]
    for num in scores:
        if num != first:
            return num
    #     print(num, end="")
    #     print(',', end="")
    # return scores[-2]

def solution2( scores : list):
    first = -101
    second = -101
    for num in scores:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
            

ls1 = [5,2,4,3,1]
ls2 = [-2,-5,0,5,20]
ls3 = [1,2,3,4,5,5]

print(solution2(ls1))
print(solution2(ls2))
print(solution2(ls3))