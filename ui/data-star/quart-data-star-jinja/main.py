import asyncio
from datetime import datetime

from datastar_py.quart import (
    DatastarResponse,
    ServerSentEventGenerator,
    read_signals,
)
from quart import Quart, render_template

app = Quart(__name__)


@app.route("/updates")
async def updates():
    # If you need to load the signals, the `read_signals helper` is available
    signals = await read_signals()
    print(signals)

    async def time_updates():
        while True:
            yield ServerSentEventGenerator.patch_elements(
                f"""<span id="currentTime">{datetime.now().isoformat()}"""
            )
            await asyncio.sleep(1)
            yield ServerSentEventGenerator.patch_signals(
                {"currentTime": f"{datetime.now().isoformat()}"}
            )
            await asyncio.sleep(1)

    return DatastarResponse(time_updates())


@app.route("/")
async def hello():
    return await render_template(
        "index.jinja", CURRENT_TIME=datetime.isoformat(datetime.now())
    )


if __name__ == "__main__":
    app.run()
