from mavsdk import System
import asyncio


async def run():
    
    drone = System(mavsdk_server_address="localhost", port=50051)

    await drone.connect()

    await drone.action.arm()
    
    for state in drone.connection_state():
        print(state)
        

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())