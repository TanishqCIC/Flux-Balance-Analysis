import xlrd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

print('Build started')

file_location = "/media/tanishqcic/New Volume/class_sem_4/ma_mam/Flux_BA/pathway_parse_trim_2.1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

index=0


for i in range(0,122) :

	distinct = 0

	pathway = sheet.cell_value(i,0)
	print(pathway)
	ws.cell(row=i+1, column=1).value = pathway
	length = sheet.cell_value(i,1)
	#print(length)
	alpha_index = (int(length))
	#print(alpha_index)
	j=4
	flag=0
	for beta_index in range(3, alpha_index-1):
		#print(beta_index)
		cell_gene = sheet.cell_value(i, beta_index)
		#print(cell_gene)
		if beta_index == 3:
			distinct = distinct+1
			ws.cell(row=i+1, column=j+1).value = cell_gene
			#print(cell_gene)
			j=j+1
			wb.save("pathway_distinct_genes_1.1.xlsx")
			#print('value saved')
		else:
			for gamma_index in range(3, beta_index):
				#print('chk loop')
				cell_gene_gamma = sheet.cell_value(i, gamma_index)
				#print(cell_gene_gamma)
				if cell_gene_gamma == cell_gene:
					flag=1				
				else:
					#print('value_not_same')
					row=i+1
					column=j+1
			if flag!=1:
				distinct = distinct+1
				ws.cell(row=i+1, column=j+1).value = cell_gene
				#print('col', column, 'row', row)
				j=j+1
				#print('value saved')
				wb.save("pathway_distinct_genes_1.1.xlsx")
			else:
				flag=0


		

	
	
	
	ws.cell(row=i+1, column=2).value = distinct
	print('Done ', i+1, ' out of 122')
