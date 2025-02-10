└── Crypto Alert Manager
    │
    │
    ├── 📁application                    # Application layer
    │   ├── port                                # Business logic handling
    │   │   ├── alert_port.py                           # Alert repository abstract 
    │   │   └── cryptocurrency_port.py                  # Cryptocurrency repository abstract 
    │   │
    │   ├── 📁repositories                      # Repository for communication with external interfaces
    │   │   ├── alert_repository.py                     # Repository for alerts
    │   │   ├── crypto_repository.py                    # Repository for cryptocurrencies
    │   │   └── crypto_update.py                        # Repository for update rate of cryptocurrencies
    │   └── __init__.py
    │
    │
    ├── 📁auth                            # Auth
    │   ├── auth.py                                     # Realisation class User and User Register logic 
    │   └── __init__.py
    │
    │
    ├── 📁cli                              # Realisation CLI with click
    │   ├── alerts_manager_on_cli.py             # Principal 
    │   ├── auth.py                                     # Section Autharisation
    │   ├── create_alert.py                             # Section for create Alerts
    │   ├── info.py                                     # Section of Info
    │   ├── work_with_alert.py                          # Section for Modify Alerts 
    │   └── __init__.py
    │ 
    │
    ├── 📁domain                            # Domain layer core
    │   ├── 📁alert                             # Logic related to alerts
    │   │   ├── alert_ABC.py                            # Abstract class for alerts
    │   │   ├── alert_by_limit.py                       # Alert by limit entity
    │   │   ├── alert_by_percent.py                     # Alert by percentage entity
    │   │   └── __init__.py
    │   │
    │   ├── 📁crypto                            # Logic related to cryptocurrencies
    │   │   ├── cryptocurrency_ABC.py                   # Abstract class for cryptocurrencies
    │   │   ├── cryptocurrency.py                       # Cryptocurrency entity
    │   │   └── __init__.py
    │   └── __init__.py
    │ 
    │
    ├── 📁infrastracture                     # Infrastracture
    │   ├── 📁adapters                           # Adapters for repositories
    │   │   ├── alert_adapter.py                        # Adapter for alert_repository(crypto_repository)
    │   │   └── cryptocurrency_adapter.py               # NOT WORK cryptocurrency_adapter realised in alert_repository
    │   │
    │   ├── 📁api                               # Fetching to API
    │   │   ├── api_port.py                             # Abstract class for Rate Provider
    │   │   ├── api_service.py                          # Rate Provider FETCH Rate + Name
    │   │   └── __init__.py
    │   └── __init__.py
    │ 
    │
    ├── main.py                  # Application entry point
    ├── preset_new_user.py       # New User with presets for DEBUGING
    ├── coin_socket.py           # Coin web Socket   DEBUGING
    ├── tools.py                 # Functions for Help
    ├── requirements.txt         # Dependencies
    └── README.md                # Documentation


    Cryptocurrency Alerts Manager

        Clone the repository and navigate to the project directory:
            git clone https://github.com/Aleksandr51r/Cryptocurrency-Alerts-Manager
            cd crypto_alert_manager

    1. Install dependencies

        pip install -r requirements.txt

    2. Activate virtual environment

        On Windows:

        .\env\Scripts\activate

        On macOS/Linux:

        source env/bin/activate

    3. Run the application

        python main.py

        Use CLI for work with aplication

    Contributing
    Feel free to submit issues and pull requests. 