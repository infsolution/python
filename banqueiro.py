class Processo:
	rec1=0
	rec2=0
	rec3=0
	rec4=0
	bitMar = False
	rAlo1=0
	rAlo2=0
	rAlo3=0
	rAlo4=0


def somaVet(vet1,vet2):
	ret=[]
	for i in range(len(vet1)):
		ret.append(vet1[i]+vet2[i])
	#print ret
	return ret
def aloc(p1,p2,p3,p4):
	p1,p2,p3,p4=[int(i) for i in raw_input('Informe a quantidade dos recursos do processo').split(',')]
reExist = [2,4,1,1]
reDispo = [0,2,1,0]
pa1 = [1,0,0,1]
pa2 = [1,0,0,0]
pa3 = [0,2,0,0]
alCorre = [pa1,pa2,pa3]

#print alCorre[1][3]
pro1=Processo()
aloc(pro1.rec1,pro1.rec2,pro1.rec3,pro1.rec4)
pro2=Processo()
aloc(pro2.rec1,pro2.rec2,pro2.rec3,pro2.rec4)
pro3=Processo()
aloc(pro3.rec1,pro3.rec2,pro3.rec3,pro3.rec4)

ps1 = [pro1.rec1,pro1.rec2,pro1.rec3,pro1.rec4]
ps2 = [pro2.rec1,pro2.rec2,pro2.rec3,pro2.rec4]
ps3 = [pro3.rec1,pro3.rec2,pro3.rec3,pro3.rec4]
soRec = [ps1,ps2,ps3]

for j in range(len(soRec)):
	if soRec[j] <= reDispo:	
		reDispo = somaVet(soRec[j],reDispo)
		print "OK"
	else:
		print "Deadlok"


print reDispo
