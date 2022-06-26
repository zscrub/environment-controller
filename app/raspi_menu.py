from simple_term_menu import TerminalMenu

def main():
    menu_exit = False

    options = ["Temp", "Humidity", "Light", "Fan"]
    main_screen = ...

    while not menu_exit:

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}")
