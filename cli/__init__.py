import click
from typing import List


command_for = {
    'exit': ['5', "exit", 'sys', 'quit', 'system', 'q'],
    'create': ['1', "create", "create alert"],
    'show': ['2', "show-alerts", "show alerts"],
    'info': ['3', "info"],
    'logout': ['4', "logout"]
}

valid_auth_commands = {
'auth_register': {'1': 'register', '2': 'enter', '3': 'exit', 'register': 'register', 'enter': 'enter', 'exit': 'exit'},
}

valid_commands = {
    'alert_type': {'1': 'limit', '2': 'percent', '3': 'back', 'limit': 'limit', 'percent': 'percent', 'back': 'back'},
    'direction_for_limit': {'1': 'above', '2': 'below', '3': 'back', 'above': 'above', 'below': 'below', 'back': 'back'},
    'direction_for_percent': {'1': 'increase', '2': 'decrease', '3': 'any', '4': 'back', 'increase': 'increase', 'decrease': 'decrease', 'any': 'any', 'back': 'back'}
}
valid_modify_commands = {'modify': {'1': 'modify', 'modify': 'modify', '2': 'back', 'back': 'back'},
                         'alert_action': {
    '1': 'currency',
    'currency': 'currency',
    '2': 'value',
    'value': 'value',
    '3': 'direction',
    'direction': 'direction',
    '1234': 'delete',
    'delete': 'delete',
    '5': 'back',
    'back': 'back'
},
    'direction': {

        'direction_percent': {
            '1': 'increase', 'increase': 'increase',
            '2': 'decrease', 'decrease': 'decrease',
            '3': 'any', 'any': 'any',
            '4': 'back',
            'back': 'back'
        },
        'direction_limit': {
            '1': 'above', 'above': 'above',
            '2': 'below', 'below': 'below',
            '3': 'back',
            'back': 'back'
        }
}
}
# ?  Function helps to che values for create or modify alert


def prompt_input(prompt_text, valid_options):
    """Checking entered values for parametrs of alert for cli creation and modify alert"""
    
    while True:
        user_input = input(prompt_text).strip().lower()
        if user_input in valid_options:
            return valid_options[user_input]
        click.echo(warning("Invalid input. Please try again."))

def get_numeric_input(user_input: str, restriction: List[int] = None) :
    """Checking entered values for parametrs of alert's trigger value % or limit """
    
    try:
        user_input = float(user_input)
    except ValueError:
        return False
    if restriction:
        return restriction[0] <= user_input <= restriction[1]
    return True

def try_to_update(func_param, choosen_alert):
    try:
        func_param()
        click.echo(success(f" Alert (ID: {choosen_alert}) was updated !"))
    except:
        warning(f'Fall to update Alert(ID: {choosen_alert})')


# ?  DECORATION OF CLI

def underline(text):
    return f"\033[4m{text}\033[0m"

def options_header(header):
    click.echo(f"\n\t--- \033[34m{header}\033[0m ---\n")

def header(text):
    click.echo(f"\n\t\t\033[32m{text}\033[0m")
    click.echo("\t---------------------------------\n")

def user_choose(text):
    return f"\033[95m{text}\033[0m"

def description_id(text):
    return f"\033[97m{underline(text)}\033[0m"

def description_status(status):
    if status == "ACTIVATE":
        return f"\033[42m{status}\033[0m"
    else:
        return f"\033[40m{status}\033[0m"


def success(text):
    return f"\n\n -------- \033[42m {text} \033[0m --------\n"

def warning(text):
    return f"\n\n -------- \033[41m {text} \033[0m --------\n"
    return f"\n -------- \033[91m {text} \033[0m --------\n"


def warning_message(text):
    return f"\n\n -------- \033[43m \033[30m {text} \033[0m --------\n"
