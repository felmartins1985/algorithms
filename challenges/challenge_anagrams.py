# https://codereview.stackexchange.com/questions/97320/recursive-and-iterative-approach-for-mergesort
def mergesort_recur(seq):
    if not seq:
        return []
    if len(seq) == 1:
        return [seq[0]]
    middle = len(seq) // 2
    left = mergesort_recur(seq[0:middle])
    right = mergesort_recur(seq[middle: len(seq)])
    return merge_recur(left, right)


def merge_recur(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] > lst2[0]:
        return [lst2[0]] + merge_recur(lst1, lst2[1:])
    else:
        return [lst1[0]] + merge_recur(lst1[1:], lst2)


def is_anagram(first_string, second_string):

    str1 = mergesort_recur(first_string.lower())  # retorn um array
    str2 = mergesort_recur(second_string.lower())

    if first_string == "" or second_string == "":
        return ("".join(str1), "".join(str2), False)

    for index, _ in enumerate(str1):
        if str1[index] != str2[index]:
            return ("".join(str1), "".join(str2), False)
    return ("".join(str1), "".join(str2), True)
