def isUnique(string):
    st = sorted(string)
    for i in range(1, len(st)):
        if st[i] == st[i-1]:
            return False
    return True

print(isUnique("aab"))
print(isUnique("bseab"))
print(isUnique("fgrewq"))


def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    st1 = sorted(str1)
    st2 = sorted(str2)
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            return False
    return True

print(checkPermutation("cab", "cba"))
print(checkPermutation("seesdf", "fesdse"))
print(checkPermutation("seesdf", "fesdsw"))


toUrlify = "Mr John Smith    "

def urlify(string, n):
    string = list(string)
    start_shift = n-1
    for i in range(n):
        if string[i] == ' ':
            shift(i, string, start_shift)
            start_shift += 2
            string[i] = '%'
            string[i+1] = '2'
            string[i+2] = '0'
    return string

def shift(i, string, start):
    iter = start
    while iter >= i:
        string[iter + 2] = string[iter]
        iter -= 1


print(urlify(toUrlify, 13))


def palindrome_permutation(permutation):
    permutation = permutation.lower()
    hmap = {}
    for p in permutation:
        if p != ' ':
            if p in hmap.keys():
                hmap[p] += 1
            else:
                hmap[p] = 1
    odd_count = 0
    for val in hmap.values():
        if val % 2 == 1:
            odd_count += 1
    return odd_count == 1 or odd_count == 0

print(palindrome_permutation("Tact Coa"))


def one_away(str1, str2):
    return count_diff(str1, str2) <= 1

def count_diff(s1, s2):
    hmap1 = {}
    hmap2 = {}
    count = 0
    for c in s1:
        if c in hmap1.keys():
            hmap1[c] += 1
        else:
            hmap1[c] = 1
    for c in s2:
        if c in hmap2.keys():
            hmap2[c] += 1
        else:
            hmap2[c] = 1
    for key in hmap1.keys():
        if key not in hmap2.keys():
            count += hmap1[key]
        elif hmap1[key] != hmap2[key]:
          count += abs(hmap1[key] - hmap2[key])
    return count


def one_edit_insert(s1, s2):
    index1 = 0
    index2 = 0
    while(index1 < len(s1) and index2 < len(s2)):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2+=1
        else:
            index1+=1
            index2+=1
    return True

one_edit_insert("pale", "pwles")


def one_edit_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first

    index1 = 0
    index2 = 0

    found_difference = False

    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True
            if len(s1) == len(s2):
                index1+=1
        else:
            index1+=1
        index2+=1

    return True


one_edit_away("pale", "pwles")