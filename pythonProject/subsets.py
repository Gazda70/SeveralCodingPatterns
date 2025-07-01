def subsets(set):
    subsets = [[]]
    for el in set:
        new_subsets = []
        for subs in subsets:
            new_subsets.append(subs + [el])
        subsets += new_subsets
    return subsets

print(subsets([1,3,5]))


def subsets_with_duplicates(set):
    set.sort()
    subsets = [[]]
    start = 0
    end = 0
    for i in range(len(set)):
        start = 0
        if i > 0 and set[i] == set[i-1]:
            start = end + 1
        end = len(subsets)-1
        for j in range(start, end + 1):
            subsets.append(subsets[j] + [set[i]])
    return subsets

print(subsets_with_duplicates([1, 3, 3]))


def permutations(set):
    result = []
    permuts = [[]]

    for i in range(len(set)):
        per_length = len(permuts)
        for p in range(per_length):
            for j in range(len(permuts[p]) + 1):
                new_permut = list(permuts[p])
                new_permut.insert(j, set[i])
                if len(new_permut) == len(set):
                    result.append(new_permut)
                else:
                    permuts.append(new_permut)
    return result

print(permutations([1, 2, 3]))

