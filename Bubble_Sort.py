#Bubble sort


def BubbleSort(arr):

    arr_L = len(arr) - 1

    for i in range(arr_L):
        for j in range(arr_L):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def main():

    arr = [4, 2, 7, 9, 3, 1]

    result = BubbleSort(arr)
    print(result)


if __name__ == "__main__":
    main()