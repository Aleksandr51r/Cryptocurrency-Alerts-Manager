└── 📁TechTest
    ├── 📁application            # Application layer
    │   ├── 📁services           # Services for business logic handling
    │   │   ├── alert_service.py # Alert management service
    │   │   └── crypto_service.py # Cryptocurrency management service
    │   ├── 📁ports              # Ports for communication with external interfaces
    │   │   ├── alert_port.py    # Port for alerts
    │   │   └── crypto_port.py   # Port for cryptocurrencies
    │   └── __init__.py
    ├── 📁domain                 # Domain layer
    │   ├── 📁alert              # Logic related to alerts
    │   │   ├── alert_ABC.py     # Abstract class for alerts
    │   │   ├── alert_by_limit.py # Alert by limit
    │   │   ├── alert_by_percent.py # Alert by percentage
    │   │   └── __init__.py
    │   ├── 📁crypto             # Logic related to cryptocurrencies
    │   │   ├── cryptocurrency_ABC.py # Abstract class for cryptocurrencies
    │   │   ├── cryptocurrency.py # Cryptocurrency entity
    │   │   └── __init__.py
    │   └── __init__.py
    ├── 📁infrastructure         # Infrastructure
    │   ├── 📁adapters           # Adapters for integration with external systems
    │   │   ├── alert_adapter.py # Adapter for working with alerts
    │   │   ├── api_adapter.py   # API adapter
    │   │   └── crypto_adapter.py # Cryptocurrency adapter
    │   ├── 📁repositories       # Repository implementations
    │   │   ├── alerts_repository.py # Alert repository
    │   │   └── crypto_repository.py # Cryptocurrency repository
    │   └── __init__.py
    ├── 📁interfaces             # Interfaces
    │   ├── 📁api                # API endpoints
    │   │   ├── api_port.py      # API port
    │   │   ├── fastapi_routes.py # API implementation
    │   │   └── __init__.py
    │   ├── 📁cli                # Command-line interface (if needed)
    │   │   ├── cli_commands.py  # CLI commands
    │   │   └── __init__.py
    │   └── __init__.py
    ├── main.py                  # Application entry point
    ├── requirements.txt         # Dependencies
    └── README.md                # Documentation
