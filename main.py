from cli.cli import alerts_manager_on_cli
from cli.auth import auth


def main():
    while True:
        user = auth()
        if user:
            alerts_manager_on_cli(obj={"alert_adapter": user.alert_adapter})


if __name__ == '__main__':
    main()
