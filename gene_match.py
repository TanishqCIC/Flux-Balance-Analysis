import xlrd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

file_location_lethal = "/media/tanishqcic/New Volume/class_sem_4/ma_mam/Flux_BA/lethal_genes_0.001.xlsx"
file_location_distinct = "/media/tanishqcic/New Volume/class_sem_4/ma_mam/Flux_BA/pathway_distinct_genes_1.1.xlsx"
file_location_all = "/media/tanishqcic/New Volume/class_sem_4/ma_mam/Flux_BA/pathway_parse_trim_2.2.xlsx"

workbook = xlrd.open_workbook(file_location_lethal)
sheet = workbook.sheet_by_index(0)

"""Saving lethal genes in list 'lethal_genes' """

lethal_genes = []

for index in range(0, 188):

	gene = sheet.cell_value(index,0)
	lethal_genes.append(gene)
"""
workbook = xlrd.open_workbook(file_location_distinct)
sheet = workbook.sheet_by_index(0)

hike=4
