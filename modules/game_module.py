import random
from types import NoneType
from question_module import *

# CARREGA LEVEL DAS QUESTÕES

def level_game_load():

    choice = int(
        input("ESCOLHA A DIFICULDADE\n1: FÁCIL\n2:MÉDIA\n3:DIFÍCIL\n"))
    param = {
        1: 5,
        2: 8,
        3: 12,
    }[choice]
    return param


# Constroi o formato das questões
def build_question(questions, temp):
    questao = "ID: {id} - Enunciado:\n{question}\nalternativas:\n{alternatives}"
    if(questions == None):return {},{}
    choice_random = random.choice(questions)

    id = choice_random['id']
    question = choice_random['question']
    temp.append(id)

    alternatives = str(choice_random['alternatives']).split("\\n")
    answer = input(questao.format(id=id, question=question,
                                  alternatives='\n'.join(alternatives)))
    return answer, choice_random


# contador de pontos de acordo com acerto ou erro
def point_count(answer, choice_random):
    parcial_score = 0.0
    if(answer == choice_random['letter']):
        parcial_score += 3.0
    else:
        parcial_score -= 2.0
    if(parcial_score <= 0):
        parcial_score = 0
    return parcial_score

# Modo edição


def edit_mode(questions, question_content_edit_mode, add_question,temp):
    choice_edit = int(input("1: ADICIONAR - 2: REMOVER  - 3: RESTARTAR - 4:EDITAR\n"))
    if(choice_edit == 1):
        questions = add_question(questions)
    elif(choice_edit == 2):
        questions = question_content_edit_mode(False, questions)
    elif(choice_edit == 3):
        temp.clear()
        return
    else:
        questions = question_content_edit_mode(True, questions)
    return questions
