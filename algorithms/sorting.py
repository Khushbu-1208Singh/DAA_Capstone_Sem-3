
def merge_sort(parcels):

    # Base condition
    if len(parcels) <= 1:
        return parcels

    # Divide the list into two halves
    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    # Merge sorted halves
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare priority scores
    while i < len(left) and j < len(right):

        if left[i]["priority"] >= right[j]["priority"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

