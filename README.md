# Asyncio Signal Handling Example

This project demonstrates a simple, cross-platform way to gracefully stop an asynchronous task in Python using `asyncio` and signal handling.  

It is especially useful on Windows, where signal support is limited and this approach is the most straightforward way to handle stop signals in asyncio applications.

## What does it do?

- Runs a long-lived asynchronous task (`ExampleAsyncHandler`) that periodically logs its status.
- Listens for a `SIGINT` (Ctrl+C) signal.
- On receiving the signal, sets a stop flag so the async task can finish cleanly.
- Ensures the event loop and resources are closed properly.

## Why this approach?

- **Cross-platform:** Works on both Unix-like systems and Windows.
- **Simplicity:** Uses only standard library modules (`asyncio`, `signal`).
- **Graceful shutdown:** The async task can finish its current work before exiting.

## Usage

1. Run `runner.py`:
   ```sh
   python runner.py
   ```
2. Press `Ctrl+C` to stop.  
   The handler will log the stop request and exit gracefully.

## Notes

- On Windows, only `SIGINT` and `SIGBREAK` are supported for signal handling in Python.
- Avoid blocking synchronous code in your async handler to ensure signals are processed promptly.

## Files

- `runner.py` — Entry point, sets up signal handling and runs the async handler.
- `example_async_handler.py` — Contains the example async handler logic.

> And yes, I wrote the README.md with AI help to speed up the writing of the summary. That's the only thing the AI ​​contributed to.
