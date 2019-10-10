def LCS(string1, string2, index1, index2, table):
    # print(index1, index2)
    if index1 == len(string1) or index2 == len(string2) :
        return ""
    if table[index1][index2] != -1:
        return table[index1][index2]
    elif string1[index1] == string2[index2] :
        table[index1][index2] = string1[index1] + LCS(string1, string2, index1 + 1, index2 + 1, table)
        return table[index1][index2]
    else:
        seq1 = LCS(string1, string2, index1 + 1, index2, table)
        seq2 = LCS(string1, string2, index1, index2 + 1, table)
        if len(seq1) > len(seq2):
            seq = seq1
        else:
            seq = seq2
        table[index1][index2] = seq
        return table[index1][index2]

string1, string2 = input("Enter two strings").split()
table = [[-1 for i in range(len(string2))] for j in range(len(string1))]
# print(len(table))
# print(len(table[0]))
lcs = LCS(string1, string2, 0, 0, table)
print(lcs)