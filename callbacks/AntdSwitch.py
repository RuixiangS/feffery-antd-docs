import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('switch-demo-output', 'children'),
    Input('switch-demo', 'checked')
)
def switch_demo_callback(checked):
    time.sleep(0.5)
    return str(checked)
