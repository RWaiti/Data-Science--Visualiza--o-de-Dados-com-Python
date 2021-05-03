def bioInformatica(archive):
    archiveEntrada = open(archive+".fasta").read().replace("\n", "")
    archiveSaida = open(archive+".html", "w")
    myDict = {}
    for i in ['A', 'T', 'C', 'G']:
        for j in ['A', 'T', 'C', 'G']:
            myDict[i+j] = 0

    for k in range(len(archiveEntrada)-1):
        myDict[archiveEntrada[k]+archiveEntrada[k+1]] += 1
    print(myDict)

    #html
    i = 1
    archiveSaida.write("<html>\n<body style='background-color:white;'>\n")
    for k in myDict:
        transparent = str(myDict[k]/max(myDict.values()))
        archiveSaida.write("<div style= 'width:100px; border:1px solid #000; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, " + transparent +"')>"+ k +"</div>\n")
        if i%4 == 0:
            archiveSaida.write("<div style='clear:both'></div>\n")
        i+=1
    archiveSaida.write("</body>\n</html>")
    archiveSaida.close()

option = int(input("1-Humano\n2-Bacteria\nOutros valores para fechar\n"))

if(option ==   1):
    bioInformatica("human")
    print("human.html Gerado")
elif(option ==   2): 
    bioInformatica("bacteria")
    print("bacteria.html Gerado")