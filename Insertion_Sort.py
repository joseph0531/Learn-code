def Insertion_sort(arr):


    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr






def main():

    arr = [4, 2, 7, 9, 3, 1]

    result = Insertion_sort(arr)
    print(result)


if __name__ == "__main__":
    main()