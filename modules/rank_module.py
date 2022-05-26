from csv_functions import *

filePath = "./data/rank.csv"
header_model = ['id','nome','points']

def restart_index_ranks(ranks):
    index = 1
    for rank in ranks:
        rank['id'] = index
        index += 1
    return ranks


def save_rank(ranks,score, nome):
    ranks.append({'nome': nome, 'points': score})  
    restart_index_ranks(ranks)
    updateCsv(filePath,ranks,header_model,True)


def loadRanks():
    return loadCsv(filePath)