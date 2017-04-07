import xlrd
import urllib.request
import re
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
file_location = "F:\class_sem_4\ma_mam\Flux_BA\sample2.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

for i in range(1433,1434) :
        gene =sheet.cell_value(i,3)
        print(gene)
        length=len(gene)
        for j in range(0,length-9):
                print(j)
                if(gene[j]=="m" and gene[j+8]=="'"):
                    string= ''.join([gene[j],gene[j+1],gene[j+2],gene[j+3],gene[j+4],gene[j+5],gene[j+6],gene[j+7]])
                    print(string)
                    print(length)
                    cell = 'D'+str(i)
                    ws[cell]= str(string)
                    i+=1
                    wb.save("final_list.xlsx")                    
    	
