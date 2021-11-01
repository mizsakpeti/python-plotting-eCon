import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Div('Output on click:', id='my-state-output'),


])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)

@app.callback(
    Output(component_id='my-state-output', component_property='children'),
    State(component_id='my-input', component_property='value'),
    Input(component_id='submit-val', component_property='n_clicks')
)
def update_state_output(stated_input, n_clicks):
    return 'Output on click: {}'.format(stated_input)



if __name__ == '__main__':
    app.run_server(debug=True)