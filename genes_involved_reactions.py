import random, cobra.io

def Reactions(fileName, gene_id):

	cobraModel = cobra.io.load_json_model('data/' + fileName)

	gene_inv=cobraModel.genes.get_by_id(gene_id)
	print(len(gene_inv.reactions) ,' Reactions involve gene ', gene_inv )

	reactions_inv = gene_inv.reactions
	frozen_set = reactions_inv
	

	a_list=[]
	
	for _ in range(0, len(frozen_set)*10):
		a=(random.sample(frozen_set, 1)[0])
		
		if _ is 0:
			a_list.append(a)
		else:
			
			for x in range(0,len(a_list)):
				if a != a_list[x]:
					flag=1
			
				else:
					flag=0
					break
			if(flag==1):
				a_list.append(a)
			
	for index in range(0, len(a_list)):
		print('reaction involved no. ', index+1, ' ',a_list[index])
		rxn=(a_list[index])
		print(rxn.reaction)
		print(rxn.name)
		print(rxn.lower_bound, ' < ', rxn.name , ' < ', rxn.upper_bound)
	return a_list