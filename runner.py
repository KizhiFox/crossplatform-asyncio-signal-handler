import asyncio
import signal

from example_async_handler import ExampleAsyncHandler


def run():
    handler = ExampleAsyncHandler()

    def _handle_interrupt(*args):
        handler.log('SIGINT received: requesting stop...')
        handler.is_stop_requested = True

    signal.signal(signal.SIGINT, _handle_interrupt)

    try:
        asyncio.run(handler.run())
    finally:
        handler.log('Event loop closed. Exiting...')


if __name__ == '__main__':
    run()
