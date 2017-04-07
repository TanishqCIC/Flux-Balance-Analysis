import xml.etree.ElementTree
import xlrd
import xlwt
import json

wb = xlwt.Workbook()
ws = wb.add_sheet("Sheet 1")



def json_write(dest_file, p_name, gene, index):
	
	data = gene
	
	
	index=index+1

	with open('trim_1.txt', 'w') as outfile:
		json.dump(data, outfile)
	return index

index = 1
data = []
def parse(fileName, index):

	"""Writing name of .xml file into excel file cell 'A0'"""
	
	pathway=str(fileName[:-4])
	

	j = 0
	path=''.join(['pathways/', fileName])
	e = xml.etree.ElementTree.parse(path).getroot()
	
	i=0
	
	dest_file="pathway_parse_trim_3.1.txt"
	index = 0
	for atype in e.findall('entry'):
		leaf = (atype.get('type'))
		
		if(leaf =='gene'):
			gene_name = (atype.get('name'))
			i=i+1
			gene_name = trim(gene_name)
			print(len(gene_name))
			
			for beta_index in range(0, len(gene_name)):

				data.append({
					'pathway name': pathway,
					'gene name': str(gene_name[beta_index]),
					'nos': j
					})
				#print(beta_index)
				#print(gene_name[beta_index])
				j+=1
				print('j', j)
				
				
	index = json_write(dest_file ,pathway ,data, index)
	print('No. of genes found are ', i)

def trim(gene_name):

	gene = []

	for alpha_index in range(0, len(gene_name)-5):
		if(gene_name[alpha_index]=="m" and gene_name[alpha_index+3]==":"):
			if(len(gene_name)<11):
				gene.append(''.join([gene_name[alpha_index+4], gene_name[alpha_index+5], gene_name[alpha_index+6], gene_name[alpha_index+7], gene_name[alpha_index+8], gene_name[alpha_index+9]]))
			else:
				if(len(gene_name)>(alpha_index+10)):
					
					if(gene_name[alpha_index+10]=="c") :
						gene.append(''.join([gene_name[alpha_index+4], gene_name[alpha_index+5], gene_name[alpha_index+6], gene_name[alpha_index+7], gene_name[alpha_index+8], gene_name[alpha_index+9], gene_name[alpha_index+10]]))
					else:
						gene.append(''.join([gene_name[alpha_index+4], gene_name[alpha_index+5], gene_name[alpha_index+6], gene_name[alpha_index+7], gene_name[alpha_index+8], gene_name[alpha_index+9]]))
				else:
					gene.append(''.join([gene_name[alpha_index+4], gene_name[alpha_index+5], gene_name[alpha_index+6], gene_name[alpha_index+7], gene_name[alpha_index+8], gene_name[alpha_index+9]]))				
	return gene				

if  __name__ == '__main__':

	print('Build started')

	file_location = "/media/tanishqcic/New Volume/class_sem_4/ma_mam/Flux_BA/final_list.xlsx"
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	for i in range(0, 122) :
		pathway = sheet.cell_value(i,3)
		print(pathway)
		fileName = ''.join([pathway, '.xml'])
		parse(fileName, index)
		index+=1
		print('Done ', i+1, ' out of 122')

	print('Build Finished!')
