Liste = [7, 10, 12, 9, 1, 5]

for i in range (len(Liste)):
    min = i
    for j in range(i+1, len(Liste)):
        if Liste[min] > Liste[j]:
            min = j
    Liste[i], Liste[min]= Liste[min], Liste[i]
    print ("sıralı dizi:")
    for i in range (len(Liste)):
        print(Liste[i])