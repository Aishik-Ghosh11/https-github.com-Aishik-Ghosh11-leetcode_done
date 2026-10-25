from copy import deepcopy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # tupleList (int, bool) fal = left, true = right
        nums.sort()
        permutations = deepcopy(nums)
        arrows = []
        final = [nums]
        # initial permutation
        for num in permutations:
            arrows.append(False)
        max = 0
        #print(permutations)
       # print(arrows)

        while max != -99:            # permute
            #print("looped")
            max = -99  # int
            maxMobile = -99  # index
            for i in range(len(permutations)):
                if not arrows[i]:  # if left
                    if i == 0:
                        True
                        #print("left")
                    elif permutations[i - 1] < permutations[i]:  # if left is smaller
                        #print("leftIsSmaller")
                        if permutations[i] > max:
                            maxMobile = i
                            max = permutations[i]
                elif i != len(permutations) - 1:
                    if permutations[i + 1] < permutations[i]:  # if right is smaller
                        #print("right")
                        if permutations[i] > max:
                            #print("rightIsSmaller")
                            maxMobile = i
                            max = permutations[i]
            #print(maxMobile)
            if maxMobile == -99:
                break
            if not arrows[maxMobile]:  # if left swap
                permutations[maxMobile - 1], permutations[maxMobile] = permutations[maxMobile], permutations[maxMobile - 1]
                arrows[maxMobile - 1], arrows[maxMobile] = arrows[maxMobile], arrows[maxMobile - 1]
                maxMobile -= 1
                #print(f"swapped {permutations[maxMobile - 1]} and {permutations[maxMobile]}")
            else:
                permutations[maxMobile + 1], permutations[maxMobile] = permutations[maxMobile], permutations[maxMobile + 1]
                arrows[maxMobile + 1], arrows[maxMobile] = arrows[maxMobile], arrows[maxMobile + 1]
                maxMobile += 1
                #print(f"swapped {permutations[maxMobile - 1]} and {permutations[maxMobile]}")
            result = []
            #print(permutations)
            #print(arrows)
            #print(maxMobile, permutations, permutations[maxMobile])
            for i in range(len(permutations)):
                if permutations[i] > permutations[maxMobile]:
                    #print(f"flipping {permutations[i]} because {permutations[i]} > {permutations[maxMobile]}")
                    arrows[i] = not arrows[i]
            final.append(deepcopy(permutations))
            # permute end
        #print(f"nums: {nums}")
        return final
print(Solution().permute([1,2,3]))








