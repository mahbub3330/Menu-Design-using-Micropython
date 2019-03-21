import os

vertical_char="│"
horizontal_char ="─"
Top_left="┌"
Top_right="┐"
Bottom_left="└"
Bottom_right="┘"


def margin(character_Sign,total_times):
    margin_character = ""
    for i in range(total_times):
        margin_character= margin_character + character_Sign
    return ( margin_character)

def draw_menu(menu):
    main_menu = menu
    #find the highest number of string in the menu
    maximum_text_length = 0
    # print(main_menu['0'][0])
    for i in main_menu:
        present_text_length = len(main_menu[i][0])
        if present_text_length > maximum_text_length:
            maximum_text_length = present_text_length
    maximum_text_length = maximum_text_length + 2
    # print(maximum_text_length)

    #top margining from left to right
    maximum_text_size = maximum_text_length
    y = maximum_text_length
    top_margine_leftTOright = Top_left + margin(horizontal_char,y)+Top_right
    print(top_margine_leftTOright)

    #now in middle part
    for i in main_menu:
        free_space = maximum_text_size - len(main_menu[i][0])
        right_vartical_wall = margin(" ",free_space)+vertical_char
        print(vertical_char+main_menu[i][0]+right_vartical_wall)
    #now lower part
    lower_margin_leftToright = Bottom_left + margin(horizontal_char,y)+Bottom_right
    print(lower_margin_leftToright)

def sub_menuC():
    os.system('cls')
    menuC = {
        '0': ["[A] Access Point ", 'A', 'N'],
        '1': ["[B] Password ", 'B', 'N'],
        '2': ["[C] Back ", 'C', 'N']

    }
    print("Sub Menu C")
    print("============")
    draw_menu(menuC)
    select = input("=====>").upper()
    if select == 'C':
        menu()
    else:
        sub_menuC()

def sub_menuB():
    os.system('cls')
    menuB = {
        '0': ["[A] Menu 1", 'A', 'N'],
        '1': ["[B] Menu 2", 'B', 'N'],
        '2': ["[C] Menu 3", 'C', 'N'],
        '3': ["[E] Back ", 'E', 'B']

    }
    print("Sub Menu B")
    print("============")
    draw_menu(menuB)
    select = input("=====>").upper()
    if select == 'E':
        menu()
    else:
        sub_menuB()

def menu():
    os.system('cls')
    main_menu = {
        '0': ["[A] Menu 1", 'A', 'N'],
        '1': ["[B] Menu 2", 'B', 'N'],
        '2': ["[C] Menu 3", 'C', 'N'],
        '3': ["[D] Save ", 'D', 'S'],
        '4': ["[E] Exit", 'E', 'Q']
    }

    print("Main Menu")
    print("===========")
    draw_menu(main_menu)
    select = input("====>").upper()
    if select == 'B' :
        sub_menuB()
    elif select == 'C' :
        sub_menuC()
    else:
        menu()

if __name__ == '__main__':
    menu()