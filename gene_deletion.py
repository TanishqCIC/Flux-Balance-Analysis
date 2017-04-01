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
	
