import asyncio


class ExampleAsyncHandler:
    def __init__(self):
        self.is_stop_requested = False

    @staticmethod
    def log(message):
        print(message)

    async def run(self):
        while True:
            if self.is_stop_requested:
                self.log('Stop requested, exiting...')
                break
            await asyncio.sleep(5)
            self.log('Running...')
