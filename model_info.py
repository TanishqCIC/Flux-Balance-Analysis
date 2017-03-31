import cobra.io, json, os

def model(cobraModel):

	print('No. of reactions involved', len(cobraModel.reactions))
	print('No. of metabolites involved',len(cobraModel.metabolites))
	print('No. of genes involved',len(cobraModel.genes))
