import csv
from csv import writer
import os

def model_item(item, rank = False):
    if(rank == True): 
        return [item['id'],item['nome'],item['points']]
    elif(rank == False):
        return [item['id'], item['question'], item['alternatives'], item['letter']]


def loadCsv(filePath=""):
    items = []
    with open(filePath, mode='r', encoding='latin-1') as inp:
        reader = csv.DictReader(inp)
        for record in reader:
            items.append(record)
    return items


def addItemCsv(filePath="", data={}):
    data = model_item(data)
    with open(filePath, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data)
        f_object.close()


def updateCsv(filePath="", data=[], model = [], rank = False):
    if(os.path.exists(filePath) and os.path.isfile(filePath)):
     os.remove(filePath)
    with open (filePath,'a') as f:
        wtr = writer(f)
        wtr.writerow(model)
        for item in data:
            dataForm = model_item(item,rank)
            wtr.writerow(dataForm)
        f.close()
