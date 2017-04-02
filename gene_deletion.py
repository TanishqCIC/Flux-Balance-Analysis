import cobra.io
from cobra.solvers import solver_dict, get_solver_name

def single_del(cobraModel, gene_id):

	rxn = cobraModel.reactions.get_by_id("biomass_Mtb_9_60atp")

	print("before Knock-Out: %4d < flux_rxn < %4d" % (rxn.lower_bound, rxn.upper_bound))
	print('before Knock-Out, the objective value is ', cobraModel.optimize())

	""" Deleting gene"""

	cobra.manipulation.delete_model_genes(cobraModel, [gene_id], cumulative_deletions=True)
	print("after Knock-Out: %4d < flux_rxn < %4d" % (rxn.lower_bound, rxn.upper_bound))
	solver = solver_dict[get_solver_name()]
	lp = solver.create_problem(cobraModel)
	solver.solve_problem(lp)
	print('after Knock-Out, the objective value is ', solver.get_objective_value(lp))
	
	"""	Undeleting gene	"""

	cobra.manipulation.undelete_model_genes(cobraModel)
	

def single_del_all(cobraModel, gene_id, essential_gene, genes_done):

	rxn = cobraModel.reactions.get_by_id("biomass_Mtb_9_60atp")
	cmo = cobraModel.solution.f
	print(cmo)
	

	""" Deleting gene"""

	cobra.manipulation.delete_model_genes(cobraModel, [gene_id], cumulative_deletions=True)

	rlow = rxn.lower_bound 
	rup = rxn.upper_bound 
	

	solver = solver_dict[get_solver_name()]
	lp = solver.create_problem(cobraModel)
	solver.solve_problem(lp)
	sgov = solver.get_objective_value(lp)
	print(sgov)
	"""	Undeleting gene	"""

	cobra.manipulation.undelete_model_genes(cobraModel)

	compare = 0.001*cmo
	if (sgov<(compare)):
		print(sgov)
		print('gene deleted is: ', gene_id)
		print("before Knock-Out: %4d < flux_rxn < %4d" % (rxn.lower_bound, rxn.upper_bound))
		print('before Knock-Out, the objective value is ', cmo)
		print("after Knock-Out: %4d < flux_rxn < %4d" % (rlow, rup))
		print('after Knock-Out, the objective value is ', sgov)	
		essential_gene.append(gene_id)

	genes_done.append(gene_id)
	print('No. of essential genes are', len(essential_gene), ' out of ', len(genes_done))
	return genes_done
