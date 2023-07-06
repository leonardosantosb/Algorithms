def is_anagram(first_string, second_string):
    def anagram_check(first_string, second_string):
        if first_string == "" or second_string == "":
            return sort_str(first_string), sort_str(second_string), False

        sorted_first = sort_str(first_string)
        sorted_second = sort_str(second_string)

        return sorted_first, sorted_second, sorted_first == sorted_second

    return anagram_check(first_string, second_string)


def sort_str(string):
    string = string.lower()
    sorted_string = list(string)
    sort_union(sorted_string)
    return "".join(sorted_string)


def sort_union(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l_half = arr[:mid]
        r_half = arr[mid:]

        sort_union(l_half)
        sort_union(r_half)

        union(arr, l_half, r_half)


def union(array, l_half, r_half):
    i = j = k = 0

    while i < len(l_half) and j < len(r_half):
        if l_half[i] <= r_half[j]:
            array[k] = l_half[i]
            i += 1
        else:
            array[k] = r_half[j]
            j += 1
        k += 1

    while i < len(l_half):
        array[k] = l_half[i]
        i += 1
        k += 1

    while j < len(r_half):
        array[k] = r_half[j]
        j += 1
        k += 1

    return array

    raise NotImplementedError
