from csv_functions import *

filePath = "./data/questions.csv"

alternatives_letters = ["A", "B", "C", "D"]
header_model = ['id','question','alternatives','letter']


def load_questions(self):
    return loadCsv(filePath)


def build_alternatives():
    alternatives = ""
    for i in alternatives_letters:
        alternative = input(
            "Digite o enunciado da letra {letter}: ".format(letter=i))
        alternatives += "{i}) {alternative}\\n".format(
            i=i, alternative=alternative)
    return alternatives




def add_question(questions):
    question = input("Digite o enunciado: ")
    alternatives = build_alternatives()
    letter = input("Digite a resposta correta para o enunciado: ").upper()
    question_save = {'id': len(questions) + 1, 'question': question,
                     'alternatives': alternatives, 'letter': letter}
    return addItemCsv(filePath,question_save)


def remove_question(questions, question):
    questionId = int(question['id'])
    for questionPop in questions:
        questionPopId = int(questionPop['id'])
        if(questionPopId == questionId):
            questions.remove(question)
    questions = restart_index_questions(questions)
    updateCsv(filePath, questions,header_model)
    return questions


def edit_question(questions, question):
    questionId = int(question['id'])
    for questionUpdate in questions:
        questionPopId = int(questionUpdate['id'])
        if(questionPopId == questionId):
            questionUpdate = question

    updateCsv(filePath,questions,header_model)
    return restart_index_questions(questions)


def search_question_id(questions, id):
    for question in questions:
        if(int(question['id']) == id):
            return question


def search_question_name(questions, name):
    item_search = [d for d in questions if d['question'] in name]
    return item_search


def restart_index_questions(questions):
    index = 1
    for question in questions:
        question['id'] = index
        index += 1
    return questions


def edit_selection(question):
    options = int(
        input("1: EDITAR ENUNCIADO - 2:EDITAR ALTERNATIVAS - 3:EDITAR RESPOSTA\n"))
    if(options == 1):
        enunciate = input("Digite o enunciado: ")
        question['question'] = enunciate
    elif(options == 2):
        alternatives = build_alternatives()
        question['alternatives'] = alternatives
    else:
        letter = input("Digite a nova resposta: ")
        question['letter'] = letter
    return question


def question_content_edit_mode(edit = False, questions = []):
    question = {}
    new_questions = []
    search_type = int(input("1: Pesquisar por ID, 2: Pesquisar por Enunciado\n"))
    if search_type == 1:
        id = int(input("Digite o id: "))
        question = search_question_id(questions,id)
    else:
        name = input("Digite o enunciado: ")
        question = search_question_name(questions,name)

    #fast fail
    if(question == None): print("Nada encontrado aqui\n" ); return

    if(edit):
      question = edit_selection(question)
      new_questions = edit_question(questions,question)
    else:
      new_questions = remove_question(questions,question)

    return new_questions
