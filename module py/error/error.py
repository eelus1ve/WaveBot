import interactions

class Ext(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="command_in_ext",
        description="This command is in an Extension",
    )
    async def _ext_command(self, ctx: interactions.CommandContext):
        await ctx.send("This command is ran inside an Extension")

def setup(client):
    Ext(client)