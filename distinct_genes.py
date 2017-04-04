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
