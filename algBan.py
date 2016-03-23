def comparaVet(vet1,vet2):
	vet1Menor=False
	for i in range(len(vet1)-1):
		if(vet1[i]<=vet2[i]):
			vet1Menor=True
		else:
			vet1Menor=False
			break
	return vet1Menor

def somaVet(vet1,vet2):
	soma=[]
	for i in range(len(vet1)-1):
		soma += [vet1[i]+vet2[i]]
	soma+=[False]
	return soma
	
#RECURSOS
recursos = [4,6,4,5,False]
disponivel = [2,3,2,2,False]
aloCorr = [[0,1,0,0,False],[1,1,2,1,False],[1,1,0,2,False]]
requi = [[3,5,3,4,False],[3,2,1,1,False],[0,1,2,2,False]]
j=0
end=[]
while(True):
	f=0
	j+=1
	cach=[]
	cach1=[]
	ini=requi
	print disponivel
	print 'inicio requi',requi
	
	for i in range(len(requi)):
		if(comparaVet(requi[i],disponivel)==True and requi[i][4]==False):
			
			disponivel=somaVet(disponivel,aloCorr[i])
			
			requi[i]=[0,0,0,0,True]
			aloCorr[i]=[0,0,0,0,True]
			cach1=requi[i:]
			break
		else:
			cach.append(requi[i])
	requi=cach+cach1
	print 'fim requi',requi,'\n'
	for i in range(len(requi)):
		f+=requi[i][4]
	if(len(requi)==f):
		print 'Todos os processos executaram'
		break
	elif(len(requi)>=f and j>f):
		print 'Deadlok'
		break
print '\n', disponivel