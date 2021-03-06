'''
from commands.base_command  import BaseCommand

from commands import *

import settings

#register all available commands
COMMAND_HANDLERS = {c.__name__.lower(): c()
                    for c in BaseCommand.__subclasses__()}

##########


async def handle_command(command, args, message, bot_client):
#spam check
    if command not in COMMAND_HANDLERS:
        return

    print(f"{message.author.name}: {settings.COMMAND_PREFIX}{command} " 
          + " ".join(args))

    # Retrieve the command
    cmd_obj = COMMAND_HANDLERS[command]
    if cmd_obj.params and len(args) < len(cmd_obj.params):
        await bot_client.send_message(message.channel, message.author.mention
                                      + " Insufficient parameters!")
    else:
        await cmd_obj.handle(args, message, bot_client)
'''