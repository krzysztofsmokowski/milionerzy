import json
import os
import re
import random
boolean_fifty = True
game_itself = True

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

def game_questions(randomized_question):
    for exact_question in randomized_question:
        correct_answer = 0
        bad_answers = []
        print(exact_question)
        for answer in randomized_question[exact_question]:
            print(answer)
            if randomized_question[exact_question][answer] == True:
                correct_answer = answer
            if randomized_question[exact_question][answer] == False:
                bad_answers.append(answer)
    return(correct_answer, bad_answers)

def fifty_fifty(answers_tuple):
    print("czy chcesz skorzystac z 50/50?")
    correct_answer = answers_tuple[0]
    bad_answers = answers_tuple[1]
    answer = input()
    if answer == "tak":
        boolean_fifty = False
        print(random.choice(bad_answers))
        print(correct_answer)
        return boolean_fifty
    print("ktora z odpowiedzi jest poprawna?")

def game(answers_tuple):
    correct_answer = answers_tuple[0]
    answer = input()
    if answer != correct_answer:
        print("you lose")
        print("\n")
        return False
    else:
        print("gratuluje bryanku! wygrales, czy chcesz grac dalej? ")
        cont = input("Napisz Tak jesli chcesz kontynuowac gre \n")
        if re.match(r'[tT]ak', cont):
            print('Potwierdzam dalsza gre')
            return True
        else:
            print('Potwierdzam koniec')
            return False

def main():
    global boolean_fifty
    global game_itself
    prize = ['1000', '5000', '10000', '20000', '50000', '100000', '250000', '1000000']
    answer_counter = 0
    loaded_filenames = files_list()
    appender = questions_appender(loaded_filenames)
    print("witam was wszystkich tutaj JA, czas na zabawe w milionerow")
    print("zagramy dzisiaj o duze pieniadze")
    print("Przechodzimy wiec do pytan")
    while game_itself == True:
        quest = get_random_question(appender)
        game_quests = game_questions(quest)
        if boolean_fifty == True:
            boolean_fifty = fifty_fifty(game_quests)
        game_itself = game(game_quests)
        if game_itself == True:
            answer_counter +=1
            print(prize[-1+answer_counter])
            if answer_counter%3==0:
                print("czy chcesz odejsc z obecna wygrana?")
                answer = input("napisz tak lub nie")
                if answer == "tak":
                    print("gratuluje, wygrales", prize[-1+answer_counter])
                    return True
        if answer_counter == len(prize):
            print("gratuluje wygrales glowna nagrode, noc z filipem krajzerem")
            return True
        print(game_itself)

if __name__ == "__main__":
    main()
