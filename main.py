import asyncio

async def process_command(command):
    print(f"Received command: {command}")

async def read_commands():
    while True:
        command = input("Enter command: ")
        await process_command(command)

async def main():
    await read_commands()

if __name__ == '__main__':
    asyncio.run(main())
