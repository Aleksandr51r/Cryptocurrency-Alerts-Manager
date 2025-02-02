
from cli import valid_commands, underline, options_header, user_choose, success, warning
from cli import get_numeric_input, prompt_input
import click


def create_alert(alert_data):

    options_header("Choose the type of alert")
    alert_type = prompt_input(
        f"\t1 - {underline('Limit')}\n"
        f"\t2 - {underline('Percent')}\n\n"
        f"\t3 - {underline('Back')}\n"
        f"\n\t >> Please enter the  type of alert: ",
        valid_commands['alert_type']
    )
    if alert_type == 'back':
        return None

    options_header("Choose the cryptocurrency")
    cryptocurrency = input(
        f"\t >> Please enter the cryptocurrency: ").strip().upper()

    if alert_type == 'limit':
        options_header("Choose the limit of triggering:")
        limit = input(
            f"\t >> Please enter the limit for {user_choose(cryptocurrency)}: ")
        while not get_numeric_input(limit):
            limit = input(
                f"\t >> Please enter the correct value for limit (integer or float) for {user_choose(cryptocurrency)}: ")

        options_header(
            f"Alert will trigger when {cryptocurrency} will be:")
        direction = prompt_input(f"\t1 - {underline('Above')} {user_choose(limit)} $ \n"
                                 f"\t2 - {underline('Below')} {user_choose(limit)} $ \n\n"
                                 f"\t3 - {underline('Back')}\n"
                                 f"\n>> Your command: ", valid_commands['direction_for_limit'])

        if direction == 'back':
            return None

    elif alert_type == 'percent':
        options_header("Choose the limit of triggering:")
        limit = input(
            f"\t >> Please enter the limit for {user_choose(cryptocurrency)}: ")
        while not get_numeric_input(limit, [0.001, 100]):
            limit = input(
                f"\t >> Please enter the correct value (integer or float)for limit between 0.001 and 100.0 for {user_choose(cryptocurrency)}: ")

        options_header(
            f"Alert will trigger when % {cryptocurrency} will change in:")
        direction = prompt_input(f"\t1 - {underline('Increase')} {user_choose(limit)} %\n"
                                 f"\t2 - {underline('Decrease')} {user_choose(limit)} % \n"
                                 f"\t3 - {underline('Any')} direction\n\n"
                                 f"\t4 - {underline('Back')}\n"
                                 f"\n>> Your command: ", valid_commands['direction_for_percent'])
        if direction == 'back':
            return None

    alert_data['alert_type'] = alert_type
    alert_data['cryptocurrency'] = cryptocurrency
    alert_data['trigger_value'] = float(limit)
    alert_data['trigger_direction'] = direction

    return alert_data
