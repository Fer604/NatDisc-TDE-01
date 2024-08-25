file = open("Test_1.txt","r")
read = file.readlines()
modified=[]
operations = []




def the_thinker(operation,list1,list2):
    result =[]
    if operation == "U":
        result.extend(list1)
        result.extend(list2)
        result = list(set(result))
        print(f"União: conjunto 1 {list1}, conjunto 2{list2}.Resultado{result}\n")
    if operation == "I":
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] ==list2[j]:
                    result.append(list2[j])
        result = list(set(result))
        print(f"Intersecção: conjunto 1 {list1}, conjunto 2 {list2}.Resultado{result}\n")
    if operation == "D":
        intersecction = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] ==list2[j]:
                    intersecction.append(list2[j])
        intersecction = list(set(intersecction))
        result.extend(list2)
        result.extend(list1)
        result = list(set(result))
        for i in range(len(intersecction)):
            result.remove(intersecction[i])
        print(f"Diferença: conjunto 1 {list1}, conjunto 2 {list2}.Resultado{result}\n")

    if operation == "C":
        list1Save = list1
        list2Save = list2
        list1 = list(set(list1))
        list2 = list(set(list2))
        for i in range(len(list1)):
            for j in range(len(list2)):
                result.append([list1[i],list2[j]])
        print(f"Produto Cartesiano: conjunto 1 {list1Save}, conjunto 2 {list2Save}.Resultado{result}\n")

                





for line in read:
    modified.append(line.strip())
for i in range(len(modified)):
    modified[i] = modified[i].replace(" ","")
    modified[i] = modified[i].split(",")
for i in range(len(modified)):
    if (i-1) % 3 == 0:
        operations.append(modified[i][0])
for i in range(len(operations)):#roda a função 4 vezes(mais fcil)
    the_thinker(operations[i],modified[3*i+2],modified[3*i+3])


