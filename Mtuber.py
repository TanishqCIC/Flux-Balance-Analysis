"""
@author: Tanishq Kumar Dhangar
"""

import cobra.io, json, os
from cobra.solvers import solver_dict, get_solver_name
import genes_involved_reactions as gir
import model_info as mi
import gene_deletion as gd
import pandas

Directory = os.listdir('data')

fileName = 'Mycobacterium_Tuberculosis_H37Rv_iNJ661.json'


def worker(fileName):
	# Uncomment to print number of processors being used
	# print(multiprocessing.cpu_count())

	cobraModel = cobra.io.load_json_model('data/' + fileName)
		
	info=(mi.model(cobraModel))
	
	solution = cobraModel.optimize()
	print(solution)
	print(cobraModel.summary())
	x_dict = cobraModel.optimize().x_dict
	print('Work on progress.. 36%')
	maxi = cobraModel.solution.f

	# Called by value
	reactionListFull = cobraModel.reactions[:]
	"""
	data = gd(cobraModel, reactionListFull, maxi)
	"""
	
	
	"""
	Needed in case of getting rxns involved for a particular gene
	gene_id="Rv3800c"
	a_list=gir.Reactions(fileName, gene_id)
	"""
	rxn = cobraModel.reactions.get_by_id("biomass_Mtb_9_60atp")
	"""
	print(rxn.reaction)
	print(rxn.name)
	print(rxn.lower_bound, ' < ', rxn.name , ' < ', rxn.upper_bound)	
	print(rxn.reversibility)
	"""

	gene_id="Rv0904c"
	gn = cobraModel.genes.get_by_id(gene_id)
	print(gn.reactions)
	



	
	cobra.manipulation.delete_model_genes(cobraModel, ["Rv2524c"], cumulative_deletions=True)
	print("after Knock-Out: %4d < flux_rxn < %4d" % (rxn.lower_bound, rxn.upper_bound))
	rxn2 = cobraModel.reactions.get_by_id("ACCOAC")
	solver = solver_dict[get_solver_name()]
	lp = solver.create_problem(cobraModel)
	solver.solve_problem(lp)
	print(solver.get_objective_value(lp))
	
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
	main(Directory, fileName)
