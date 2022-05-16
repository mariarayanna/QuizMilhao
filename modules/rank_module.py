from csv_functions import *

filePath = "./data/rank.csv"
header_model = ['id','points']

def restart_index_ranks(ranks):
    index = 1
    for rank in ranks:
        rank['id'] = index
        index += 1
    return ranks


def save_rank(ranks,score):
    ranks.append({'points': score})
    ranks.sort(key=lambda x: str( x['points']), reverse=True)
    restart_index_ranks(ranks)
    updateCsv(filePath,ranks,header_model,True)


def loadRanks():
    return loadCsv(filePath)