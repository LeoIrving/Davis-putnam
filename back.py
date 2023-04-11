atom_list = []
# input
with open("result.txt") as f:
    check = f.readline()
    if check == "0\n":
        print("NO SOLUTION")
    else:
        clause=check.rstrip("\n").split(" ")
        atom_list.append(clause)
        while True:
            info = f.readline()
            if info == "0\n":
                break
            clause =info.rstrip("\n").split(" ")
            atom_list.append(clause)
        for line in f:
            info = line.rstrip("\n").replace('(',' ').replace(',',' ').replace(')','').split(" ")
            atom_list[int(info[0])-1].append(info[1:])

result_list = []
for item in atom_list:
    if item[1] == 'T' and item[2][0]=='At':
        result_list.append(item[2])
for i in range(0,len(result_list)):
    for item in result_list:
        if int(item[2]) == i:
            print(item[1])
        