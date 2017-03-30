"""
@author: Tanishq Kumar Dhangar
@email: tanishqcic@gmail.com
"""

import cobra.io, json, os
from cobra.solvers import solver_dict, get_solver_name

Directory = os.listdir('data')

fileName = 'Mycobacterium_Tuberculosis_H37Rv_iNJ661.json'

def worker(fileName):
	# Uncomment to print number of processors being used
	# print(multiprocessing.cpu_count())

	cobraModel = cobra.io.load_json_model('data/' + fileName)
	print('No. of reactions involved', len(cobraModel.reactions))
	print('No. of metabolites involved',len(cobraModel.metabolites))
	print('No. of genes involved',len(cobraModel.genes))
		
		
	gene_inv=cobraModel.genes.get_by_id("Rv1484")
	print('Reactions that involve gene "Rv1484"', len(gene_inv.reactions))
	x_dict = cobraModel.optimize().x_dict
	print('Work on progress.. 36%')
	maxi = cobraModel.solution.f

	# Called by value
	reactionListFull = cobraModel.reactions[:]
	"""
	data = single_reaction_deletion(cobraModel, reactionListFull, maxi)
	print('Work on progress.. 96%')
	"""
	print(gene_inv.reactions)
	"""
	with open('result/' + fileName, 'w') as handle:
		json.dump(data, handle, sort_keys=True, indent=4)
	"""

def main(Path, fileName):
    worker(fileName)
    print('Done.. 100%')
    print('Finished with NO error')
    folder = "F:\class_sem_4\ma_mam\Flux_BA\result"
    print('Find your file with filename "', fileName, '" in folder "', folder, '"')
    
if  __name__ == '__main__':
	print("Build started!")
	print('Work on progress.. 18%')
	print(fileName)
	print(Directory)
	main(Directory, fileName)
