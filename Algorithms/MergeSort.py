def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2

    list1 = merge_sort(list[:mid])
    list2 = merge_sort(list[mid:])

    return merge(list1, list2)

def merge(list1, list2):
    if list1[0] > list2[len(list2) - 1]:
        return list2 + list1
    else:
        return list1 + list2

if __name__ == "__main__":
    list = [38, 27, 43, 3, 9, 82, 10]

    print(merge_sort(list))