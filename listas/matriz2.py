#Hallar y mostrar la suma de la DP, DS, MTI, MTS

#matriz de ejemplo
m = [[2,5,7,8,9],[3,4,2,2,2],[2,2,4,3,3],[1,7,6,4,4],[1,8,8,5,7]]

sdp = sds = sts = sti = 0

for i in range(0,5): #generar subíndices de las filas
    for j in range(0,5): #generar subíndices de las columnas
        if i == j:
            sdp = sdp + m[i][j]
        if (i+j) == 4: #i+j == nfilas - 1  o i+j == ncolumnas - 1
            sds = sds + m[i][j]
        if i > j:
            sts = sts + m[i][j]
        if i < j:
            sti = sti + m[i][j]
        
print(sdp)
print(sds)
print(sts)
print(sti)
