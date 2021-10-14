#python program to remove duplicate char

def removeduplicate(str, n):
    index =0

    for i in range(0,n):
        for j in range (0, i+1):
            if (str[i] ==str[j]):
                break
        if (j==i):
            str[index] = str[i]
            index = index +1

        return " ".join(str[:index])

str = "shwwetha shruthi"
n =len(str)
print(removeduplicate(list(str), n))