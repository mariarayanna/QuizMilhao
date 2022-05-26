import sys
from turtle import position
import pprint

# path que deve ser acessado os módules
sys.path.append('./modules/')
from question_module import *
from game_module import *
from rank_module import *


# Carrega as questões do arquivo CSV
questions = load_questions("./data/questions.csv");

#Global VARS 
question_level = 0
start_end = 1
score = 0.0
count_answer = 0

temp_answer = []


# Nome do jogador
jogador1 = input("Insira o nome jogador: ")

#Looping do jogo
while(start_end != 3):
    if(questions == None): questions = load_questions("./data/questions.csv")

    not_in_choice = [d for d in questions if d['id'] not in temp_answer]   

    if(start_end == 2 or len(questions) == 0 or not_in_choice == []): questions =  edit_mode(questions,question_content_edit_mode,add_question,temp_answer)

    if(count_answer == 0): 
        question_level = level_game_load()
    if(not_in_choice == []):  continue

    answer, choice_random = build_question(not_in_choice,temp_answer)

    if(answer != {}):
        score += point_count(answer,choice_random)
        count_answer+=1

    if(count_answer == question_level): count_answer = 0; start_end =  int(input("1: Continuar Jogando, 2: Modo Edição, 3: Encerrar o jogo\n"))

ranks = loadRanks()
save_rank(ranks,score,jogador1)

print("RANK")

ranks = sorted(ranks, key=lambda x: float(x['points']), reverse=True)[:10]

for index, rank in enumerate(ranks):
       print('{position}º lugar - nome: {name} -  pontos: {points}'.format(position = index+1,name = rank['nome'], points = rank['points']))