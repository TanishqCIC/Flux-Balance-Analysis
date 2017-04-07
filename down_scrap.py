import xlrd
import urllib.request
import re
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
file_location = "F:\class_sem_4\ma_mam\Flux_BA\sample2.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
