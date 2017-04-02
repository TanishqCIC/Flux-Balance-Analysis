import urllib.request
import re
from openpyxl import Workbook
wb = Workbook()
ws = wb.active



for i in range(1433,1435) :
    url = "http://www.genome.jp/kegg-bin/show_organism?menu_type=pathway_maps&org=mtu"
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    regex = b'show_pathway?(.+?)"'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    try:    
        raise Exception('X')
    except Exception as e:
        ("Error {0}".format(str(e.args[0])).encode("utf-8"))
    print(i)
    print(price)
    
    cell = 'D'+str(i)
    ws[cell]= str(price)
    i+=1
    wb.save("sample2.xlsx")
