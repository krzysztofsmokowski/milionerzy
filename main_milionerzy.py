import json
import os
import random

def files_list():
    '''Loading current path to list for future appending those objects'''
    list_of_files = []
    path = os.listdir(path='.')
    for file_name in path:
        if "milionerzy-" in file_name:
            list_of_files.append(file_name)
    return list_of_files

def questions_appender(fileslist):
    '''Appending jsons into list_of_answers in order to get every file in dir into one list'''
    list_of_questions =[]
    for file_name in fileslist:
        with open(file_name) as json_data:
            list_of_questions.append(json.load(json_data))
    return list_of_questions

def get_random_question(questions_list):
    '''
    Ta funkcja ma wyciagac jedno ptanie ze struktury pytan.

    Wejscie: struktura z pytaniami
    Wyjscie: jedno pytanie z odpowiedziami
    '''
    questions = random.choice(questions_list)['pytania']
    question = random.choice(questions)
    return question

def game_input(randomized_question):
    for exact_question in randomized_question:
        correct_answer = 0
        print(exact_question)
        for answer in randomized_question[exact_question]:
            print(answer)
            if randomized_question[exact_question][answer] == True:
                correct_answer = answer
    answer = input()
    if answer != correct_answer:
        print("you lose")
        return True
    else:
        print("gratuluje bryanku! to poprawna odpowiedz, czy chcesz grac dalej?")
        cont = input("Napisz Tak jesli chcesz kontynuowac gre")
        if cont != "Tak" or "tak":
            return False

def main():
    loaded_filenames = files_list()
    appender = questions_appender(loaded_filenames)
    #print("witam was wszystkich tutaj sebastian karynski, czas na zabawe w milionerow")
    #print("zagramy dzisiaj o duze pieniadze")
    #print("Przechodzimy wiec do pytan")
    game = True
    while game == True:
        quest = get_random_question(appender)
        game = game_input(quest)
        print(game)

if __name__ == "__main__":
    main()
