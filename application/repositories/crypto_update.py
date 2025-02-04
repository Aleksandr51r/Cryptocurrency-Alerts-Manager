import asyncio
from application.repositories.crypto_repository import CryptocurrencyRepository


class AutoUpdateService:
    def __init__(self, interval=10):
        self.crypto_storage = CryptocurrencyRepository()
        self.interval = interval

    async def start(self):
        i = 1
        while True:
            print('Updating cryptocurrency prices loop => ', i)
            self.crypto_storage.update_all_prices()
            await asyncio.sleep(self.interval)

            print(' => ', self.crypto_storage.currencies)
            # print(' => ', self.crypto_storage.get_currencies_in_use())
            # print(' => ', self.crypto_storage.get_currencies())
            i += 1


