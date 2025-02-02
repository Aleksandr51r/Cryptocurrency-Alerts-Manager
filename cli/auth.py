import click
from auth import UserRegistry, User
from cli import valid_auth_commands, underline, try_to_update, options_header, warning, user_choose, header, prompt_input, get_numeric_input, success, description_id
user_registry = UserRegistry()


def cheking_name(registration=False):

    while True:
        username = input(f"\n\t >> Please enter the name: ").lower()
        is_name_exist = user_registry.checking_the_name(username)
    # registration
        if registration and is_name_exist:
            click.echo(
                f"\n[!] User with the name '{username}' already exists.\n")
    # loging
        elif not registration and not is_name_exist:
            click.echo(
                f"\n[!] User with the name '{username}' was not found.\n")
        else:
            return username



def registration():
    username = cheking_name(registration=True)
    password = input(f"\n\t >> Please enter the password: ")
    new_user = user_registry.register_new_user(username, password)
    click.echo(f"\nUser {new_user.username} successfully registered!")
    return new_user


def login():
    username = cheking_name()
    password = input(f"\t >> Please enter your password: ")
    user = user_registry.authenticate_user(username.lower(), password)
    if user:
        click.echo(f"\n\tWelcome back, {user.username}!")
        return user
    else:
        click.echo("\n\tInvalid username or password.")
        return None


def auth():
    is_authorised = False
    click.echo("\n\n \t\tWelcome to Alerts Manager!")
    click.echo("----------------------------------------------------------\n")
    options_header("Choose the options:")
    auth_action = prompt_input(f"\t1 - {underline('Register')} the new user\n"
                               f"\t2 - {underline('Enter')} as register user\n\n"
                               f"\t3 - {underline('Exit')}\n"
                               f"\n>> Your command: ",
                               valid_auth_commands['auth_register'])

    if auth_action == 'exit':
        click.echo("\nGoodbye! :)\n")
        raise SystemExit()

    elif auth_action == 'register':
        user = registration()
        return user

    elif auth_action == 'enter':
        user = login()
        return user
