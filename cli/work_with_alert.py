from cli import valid_modify_commands, underline, try_to_update, options_header, warning, user_choose, header, prompt_input, get_numeric_input, success, description_id
import click
import time
import sys
import threading
from  application.repositories.crypto_update import AutoUpdateService

def work_with_alert(alerts, alert_adapter):
    while True:
        if not alerts:
            # sad kitty
            click.echo(
                '\t　　　　　   ____                                         ')
            click.echo('\t　　　　　／＞　　フ                                       ')
            click.echo('\t　　　　　| 　_　 _l                                      ')
            click.echo('\t　 　　　／` ミ＿xノ                                       ')
            click.echo('\t　　 　 /　　　 　 |                                       ')
            click.echo('\t　　　 /　 ヽ　　 ﾉ      There are not added alert         ')
            click.echo(
                '\t　 　 │　　|　|　|                                         ')
            click.echo('\t　／￣|　　 |　|　|                                        ')
            click.echo(
                '\t　| (￣ヽ＿ヽ)__) __)                                      ')
            click.echo(
                '\t　＼二つ                                                  ')
            return None
        
        
        alerts = alert_adapter.get_all_alerts()

        header('List of all alerts:')
        # print(*alerts, sep='\n')
        for alert in alerts:
            print(alert)  
        
        

        options_header("Choose the options:")
        action = prompt_input(f"\t1 - {underline('Modify')} the alert\n\n"
                              f"\t2 - {underline('Relance')}\n"
                              f"\t3 - {underline('Exit')}\n"
                              f"\n>> Your command: ",
                              valid_modify_commands['modify'])
        if action == 'back':
            return None
        elif action == 'relance':
            alert_adapter.repository.crypto_storage.update_all_prices()


        elif action == 'modify':
            choosen_alert = input('\n \t >> Please enter the ID of alert: ')
            choosen_alert = choosen_alert.upper()
            all_alerts = alert_adapter.repository.alerts

            if choosen_alert not in all_alerts:
                warning("Alert was not found")
            else:
                while choosen_alert:
                    print('\n\n', alert_adapter.get_alert(
                        choosen_alert), '\n\n')
                    alert_action = prompt_input(f"\t1 - Change a {underline('currency')} of the alert\n"
                                                f"\t2 - Change a {underline('value')} of triggering\n"
                                                f"\t3 - Change a {underline('direction')} of triggering\n"
                                                f"\t1234 - {underline('Delete')} the alert \n\n"
                                                f"\t5 - {underline('Back')} to the list of alerts\n\n"
                                                f"\n>> Your command: ", valid_modify_commands['alert_action'])
                    alert = alert_adapter.get_alert(choosen_alert)

                    if alert_action == 'currency':
                        new_currency = input(
                            "\nEnter the new currency: ").upper()
                        print('>>new_currency>>1', new_currency)
                        print('>>>>choosen_alert>>1', choosen_alert)
                        print('>>>old_cryptocurrency>>>>1',
                              all_alerts[f'{choosen_alert}'].cryptocurrency.cryptocurrency_id)
                        old_cryptocurrency = all_alerts[f'{choosen_alert}'].cryptocurrency.cryptocurrency_id

                        # print('>>>>>>>>>>>>>>1', dir(alert_adapter))

                        try:
                            new_currency = alert_adapter.repository.crypto_storage.get_or_create_currency(
                                new_currency)
                            print('>>>>>>>>>>>>>>2', new_currency)
                            alert_adapter.repository.crypto_storage.decrement_currencies_in_use(
                                old_cryptocurrency)
                            try_to_update(lambda: alert.update_cryptocurrency(
                                new_currency), choosen_alert)
                        except:

                            click.echo(warning(f"{new_currency}!"))

                    elif alert_action == 'value':

                        new_value = input("\nEnter the new triggering value: ")
                        if alert.alert_type == 'percent':
                            while not get_numeric_input(new_value, [0.001, 100]):
                                new_value = input(
                                    "\nEnter the new triggering value - integer or float between 0.001 and 100: ")
                        else:
                            while not get_numeric_input(new_value):
                                new_value = input(
                                    "\nEnter the new triggering value - integer or float: ")

                        try_to_update(lambda: alert.update_trigger_value(
                            float(new_value)), choosen_alert)

                    elif alert_action == 'direction':
                        if alert.alert_type == 'percent':
                            new_direction = prompt_input(f"\t1 - {underline('Increase')} \n"
                                                         f"\t2 - {underline('Decrease')}  \n"
                                                         f"\t3 - {underline('Any')}  \n\n"
                                                         f"\t4 - {underline('Back')} \n\n", valid_modify_commands[
                                                             'direction']['direction_percent']
                                                         )
                        else:
                            new_direction = prompt_input(f"\t >> Please choose new direction: \n\n"
                                                         f"\t1 - {underline('Above')} \n"
                                                         f"\t2 - {underline('Below')} \n\n"
                                                         f"\t3 - {underline('Back')} \n\n", valid_modify_commands[
                                                             'direction']['direction_limit']
                                                         )

                        if new_direction == 'back':
                            continue

                        try_to_update(lambda: alert.update_trigger_direction(
                            new_direction), choosen_alert)

                    elif alert_action == 'delete':
                        alert_adapter.delete_alert(
                            choosen_alert, alert.cryptocurrency.cryptocurrency_id)
                        alerts = alert_adapter.get_all_alerts()
                        click.echo(success(
                            f"Alert ID: {choosen_alert} for {alert.cryptocurrency.currency_name} was deleted."))
                        break

                    elif alert_action == 'back':
                        alerts = alert_adapter.get_all_alerts()
                        choosen_alert = None
                        break
        