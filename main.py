from cli.cli import alerts_manager_on_cli
import click
import asyncio


def main():

    alerts_manager_on_cli()
    # alerts_manager_on_cli(obj={"alert_adapter": user.alert_adapter})


if __name__ == '__main__':
    main()