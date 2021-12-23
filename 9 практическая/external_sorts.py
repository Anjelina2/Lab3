def merge_sort(list1, left_ind, right_ind):  # внутрення сортировка (сортировка слиянием)

    def merge_list(list1_2, start, middle, end):
        left = list1_2[start:middle]
        right = list1_2[middle:end]
        k = start
        i = 0
        j = 0
        while start + i < middle and middle + j < end:
            if left[i] <= right[j]:
                list1_2[k] = left[i]
                i += 1
            else:
                list1_2[k] = right[j]
                j += 1
            k += 1
        if start + i < middle:
            while k < end:
                list1_2[k] = left[i]
                i += 1
                k += 1
        else:
            while k < end:
                list1_2[k] = right[j]
                j += 1
                k += 1

    if right_ind - left_ind > 1:
        mid_i = (right_ind + left_ind) // 2
        merge_sort(list1, left_ind, mid_i)
        merge_sort(list1, mid_i, right_ind)
        merge_list(list1, left_ind, mid_i, right_ind)
