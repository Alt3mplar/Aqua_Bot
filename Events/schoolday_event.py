from events.base_event import BaseEvent
from utils import get_channel

from datetime import datetime

class ExampleEvent(BaseEvent):

    def __init__(self):
        interval_minutes = 60
        super().__init__(interval_minutes)

    async def run(self, client):
        now = datetime.now()
        
        if now.hour == 8 and now.minute == 30:
            msg = "It's school time!"
        elif now.hour == 9 and now.minute == 40 :
            msg = "It's period two!"
        elif now.hour == 10 and now.minute == 56:
            msg = "It's time for lunch!"
        if now.hour == 12 and now.minute == 15:
            msg = "It's high noon!(period 3)"

        elif now.hour == 13 and now.minute == 27:
            msg = "It's past high noon!(period 4)"
        elif now.hour == 15:
            msg = "It's home time"
        else:
            msg = f"It is {now.hour}:{now.minute}"

        channel = get_channel(client, "general")
        await client.send_message(channel, msg)
