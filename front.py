class Node:
    def __init__(self,name) -> None:
        self.node_name = name
        self.node_treasure =[]
        self.node_next = []
    
    
# input
with open("maze.txt") as f:
    node = f.readline().rstrip('\n').split(" ")
    treasure = f.readline().rstrip('\n').split(" ")
    max_step = int(f.readline().rstrip('\n'))
    node_list=[]
    for item in node:
        info = f.readline().rstrip('\n').split(" ")
        pos1 = info.index("TREASURES")
        pos2 = info.index("NEXT")
        node = Node(info[0])
        node.node_treasure = info[pos1+1:pos2]
        node.node_next = info[pos2+1:]
        node_list.append(node)
atom_list = []

# output
with open ("cnf.txt","w") as f:
    # categories 1
    for t in range(max_step+1):
        for first_index in range(len(node_list)):
            atom = "At("+str(node_list[first_index].node_name)+","+str(t)+")"
            if atom not in atom_list:
                atom_list.append(atom)
            atom1_index = atom_list.index(atom)+1
            for second_index in range(first_index+1,len(node_list)):
                atom = "At("+str(node_list[second_index].node_name)+","+str(t)+")"
                if atom not in atom_list:
                    atom_list.append(atom)
                atom2_index = atom_list.index(atom)+1
                output= "-" + str(atom1_index)+" "+"-"+str(atom2_index)
                f.write(output)
                f.write("\n")
    # categories 2
    for t in range(max_step):
        for first_index in range(len(node_list)):
            atom = "At("+str(node_list[first_index].node_name)+","+str(t)+")"
            if atom not in atom_list:
                atom_list.append(atom)
            atom_index = atom_list.index(atom)+1
            output = "-"+str(atom_index)
            f.write(output)
            for item in node_list[first_index].node_next:
                atom = "At("+item+","+str(t+1)+")"
                if atom not in atom_list:
                    atom_list.append(atom)
                atom_index = atom_list.index(atom)+1
                output = " "+str(atom_index)
                f.write(output)
            f.write("\n")
    # categories 3
    for first_index in range(len(node_list)):
        if node_list[first_index].node_treasure is not None:
            for item in node_list[first_index].node_treasure:
                for t in range(max_step+1):
                    atom = "At("+str(node_list[first_index].node_name)+","+str(t)+")"
                    if atom not in atom_list:
                        atom_list.append(atom)
                    atom_index = atom_list.index(atom)+1
                    output = "-"+str(atom_index)
                    f.write(output)
                    atom = "Has("+item+","+str(t)+")"
                    if atom not in atom_list:
                        atom_list.append(atom)
                    atom_index = atom_list.index(atom)+1
                    output = " "+str(atom_index)
                    f.write(output)
                    f.write("\n")
    # categories 4
    for t in range(max_step):
        for item in treasure:
            atom1 = "Has("+item+","+str(t)+")"
            if atom1 not in atom_list:
                atom_list.append(atom1)
            atom1_index = atom_list.index(atom1)+1
            atom2 = "Has("+item+","+str(t+1)+")"
            if atom2 not in atom_list:
                atom_list.append(atom2)
            atom2_index = atom_list.index(atom2)+1
            output = "-"+str(atom1_index)+" "+str(atom2_index)
            f.write(output)
            f.write("\n")
    # categories 5
    for item in treasure:
        treasure_list = []
        for node in node_list:
            if item in node.node_treasure:
                treasure_list.append(node.node_name)
        for t in range(max_step):
            atom1 = "Has("+item+","+str(t)+")"
            if atom1 not in atom_list:
                atom_list.append(atom1)
            atom1_index = atom_list.index(atom1)+1
            atom2 = "Has("+item+","+str(t+1)+")"
            if atom2 not in atom_list:
                atom_list.append(atom2)
            atom2_index = atom_list.index(atom2)+1
            output = str(atom1_index)+" -"+str(atom2_index)  
            f.write(output)
            for node in treasure_list:
                atom = "At("+node+","+str(t+1)+")"
                if atom not in atom_list:
                    atom_list.append(atom)
                atom_index = atom_list.index(atom)+1
                output = " "+str(atom_index)
                f.write(output)
            f.write("\n")
    # categories 6
    atom = "At("+str(node_list[0].node_name)+","+str(0)+")"
    if atom not in atom_list:
        atom_list.append(atom)
    atom_index = atom_list.index(atom)+1
    output = str(atom_index)
    f.write(output)
    f.write("\n")
    # categories 7
    for item in treasure:
        atom = "Has("+item+","+str(0)+")"
        if atom not in atom_list:
            atom_list.append(atom)
        atom_index = atom_list.index(atom)+1
        output = "-"+str(atom_index)  
        f.write(output)
        f.write("\n")
    # categories 8
    for item in treasure:
        atom = "Has("+item+","+str(max_step)+")"
        if atom not in atom_list:
            atom_list.append(atom)
        atom_index = atom_list.index(atom)+1
        output = str(atom_index)  
        f.write(output)
        f.write("\n")

    f.write(str(0))
    f.write("\n")

    # list of atom with their name
    for atom in atom_list:
        index = atom_list.index(atom)+1
        output = str(index)+" "
        f.write(output)
        f.write(atom)
        f.write("\n")
