import click
from cli import command_for, create_alert, underline, header, warning, success, options_header
from cli.create_alert import create_alert
from cli.work_with_alert import work_with_alert
from cli.info import app_info


@click.group(invoke_without_command=True)
@click.pass_context
def alerts_manager_on_cli(ctx):
    alert_adapter = ctx.obj.get("alert_adapter")

    if alert_adapter is None:
        click.echo("Error: alert_adapter is not properly configured.")
        raise SystemExit()

    click.echo("\n\n \t\tWelcome to Alerts Manager!")
    click.echo("----------------------------------------------------------\n")

    print(
        f"\tYou can use this application: \n\t\t - by typing underscored {underline('command')} (in any register)\n\t\t - or use a number - just before the command.\n\n")

    while True:
        options_header(f"Enter a command:")
        command = input(
            f"\t 1 - {underline('Create')} alert \n"
            f"\t 2 - {underline('Show')} alerts\n"
            f"\t 3 - {underline('Info')}\n"
            f"\t 4 - {underline('Logout')}\n\n"
            f"\t 5 - {underline('Exit')}\n"
            f"\n>> Your command: "
        )

        command = command.lower().strip()

#! Exit
        if command in command_for['exit']:
            click.echo("\nGoodbye! :)\n")
            raise SystemExit()
#! logout
        elif command in command_for['logout']:
            click.echo("\nLogging out...\n")
            return 

#! Create
        elif command in command_for['create']:
            alert_data = {}
            header('CREATE the ALERT')
            full_alert = create_alert(alert_data)
            if full_alert:
                try:
                    click.echo("try")
                    click.echo(full_alert)
                    alert_adapter.create_alert(full_alert)
                    click.echo(
                        success(f"Alert for  {full_alert['cryptocurrency']} was created!"))
                except:
                    click.echo("except")
                    click.echo(full_alert)
                    click.echo(
                        warning(f"Faluer to create an alert for {full_alert['cryptocurrency']}!"))
#! Show and modify
        elif command in command_for['show']:
            alerts = alert_adapter.get_all_alerts()
            work_with_alert(alerts, alert_adapter)
#! Info
        elif command in command_for['info']:
            app_info()
        else:
            click.echo(warning("Unknown command. Please try again."))

