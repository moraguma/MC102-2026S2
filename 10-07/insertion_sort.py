import random


def insertion_sort(l):
    for i in range(1, len(l)):
        aux = l[i]
        j = i - 1
        while j >= 0:
            if l[j] > aux:
                l[j + 1] = l[j] 
            else:
                break

            j -= 1
        l[j + 1] = aux


l = [random.randint(0, 20) for i in range(10)]
print(l)

insertion_sort(l)
print(l)