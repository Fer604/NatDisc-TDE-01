file = open("Test_1.txt","r")
read = file.readlines()
modified=[]
operations = []

def the_thinker(operation,list1,list2):
    result =[]
    if operation == "U":
        pass

    if operation == "I":
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] ==list2[j]:
                    result.append(list2[j])
        result = list(set(result))
        print(f"Intersecção: conjunto 1 {list1}, conjunto 2 {list2}.Resultado{result}")
    if operation == "D":
        pass
    if operation == "C":
        pass





for line in read:
    modified.append(line.strip())
for i in range(len(modified)):
    modified[i] = modified[i].replace(" ","")
    modified[i] = modified[i].split(",")
print(modified)
for i in range(len(modified)):
    if (i-1) % 3 == 0:
        operations.append(modified[i][0])
print(operations)
for i in range(len(operations)):# em vez de pedir um QUARTO PARAMETRO eu só rodo a função 4 vezes(mais fcil)
    the_thinker(operations[i],modified[3*i+2],modified[3*i+3])


