import datetime


def selector():

    print('1: Ще учим Английски!\n2: Искам да добавя нови думи.\n3: Покажи ми речника моля.\n4: Нищо, аз си знам думуте...')
    print()
    selection = input('Напиши избора си (1, 2, 3, 4): ')
    return selection


def select_player() -> tuple[int, str]:
    add =''
    print('Здравей, кой ще играе днес?\n1: 👦\n2: 👧\nИзбери "1" или "2"')
    while True:
        try:
            sex = int(input('Избери играч: '))
            if sex in (1, 2):
                break
            else:
                print('Трябва да избереш играч "1" или играч "2"')
        except ValueError:
            print('Избери си играч и напиши "1" или "2"')
    return sex, add


def get_name() -> str:
    user = input('Как се казваш?: ')
    return user


def show_dictionary(words_dict):
    for english_word, bulgarian_word in words_dict.items():
        print(f"{english_word} --> {bulgarian_word}")
    print(f"\nВ речника ви има {len(words_dict)} думи.")


def get_game_type(user, sex) -> str:
    add = ''
    if sex == '2':
        add = 'a'

    print(f'\nЗдравей {user.capitalize()}{add}. Нека проверим дали си знаеш думите по Английски.\n')
    print('Каво искаш да упражняваш този път?\n')
    print('1: превод от Английски към Български,\n2: превод от Български към Английски\n3: или и двата вида?\n')

    while True:
        try:
            type_of_game = input('Избирам... ')
            if type_of_game in ('1', '2', '3'):
                if type_of_game == '3':
                    print(f'\nОоо, чувстваш се смел{add} днес а?')
                print('Успех! Когато искаш да спреш просто въведи "стоп".\n')
                return type_of_game
            else:
                print('Трябва да избереш, какво искаш да тренираш и да въведеш "1","2" или "3"')
        except ValueError:
            print('Избери и напиши "1","2" или "3"')


def collect_new_english_word():
    english = input('Моля, напиши думата на английски: ')
    return english


def collect_new_bulgarian_word():
    bulgarian = input('Моля, напиши думата на български: ')
    return bulgarian


def record_session(name, translated, errors, words):
    now = datetime.datetime.now()
    with open(f'Sessions', 'a') as file:
        file.write(f"\nИграч: {name}\nДата: {now}\nпреведени думи: {translated}\nСгрешени думи: {errors}\n{', '.join(words)}")


if __name__ == "__main__":
    pass