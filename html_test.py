import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go


path = ''
df = pd.DataFrame(data=pd.read_csv(path + 'registo__doença_cardiaca.csv'))
#df = pd.DataFrame(data=pd.read_csv(path + 'heart_2020_cleaned.csv'))

radio_options_fumadores = [
    {'label': 'Todos', 'value': 'todos'},
    {'label': 'Não Fumadores', 'value': 'n_fumadores'},
    {'label': 'Fumadores', 'value': 'fumadores'}
]

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('TESTES')
    ], id='1_div', className='center', style={'display': 'flex', 'height': '8%'}),

    html.Div([
        html.H3('Analise doentes cardiacos, todos, fumadores e não fumadores'
                )
    ], id='2_div', className='center', style={'display': 'flex', 'height': '8%'}),

    html.Div([
        html.Div([

            html.Label('Filtros:'),
            dcc.RadioItems(
                id='radio_filtro_fumadores',
                options=radio_options_fumadores,
                value='todos'
            )
        ],id='filter', className='col3 center', style={'float': 'left'}),

        html.Div([
            dcc.Graph(id='pie_chart'),
        ],id='pie_chart_div',className='col3', style={'float':'center'}),
        html.Div([
            html.Label('Filtros:')
        ], id='filter_2', className='col3', style={'float': 'right'}),

    ],id='3_div',className='row', style={'display': 'flex','height':'30%'}),

    html.Div([
        html.H1('TESTES'),
    ], id='4_div', className='row', style={'display':'flex','height':'30%'})

])

@app.callback(
    Output("pie_chart", "figure"),
    Input("radio_filtro_fumadores", "value")
)

def generate_chart(radio_filtro_fumadores):

    tabela_freq = df.groupby(['HeartDisease', 'Smoking']).size().unstack()

    if radio_filtro_fumadores == 'todos':
        sem_dc = tabela_freq.loc['No']['No'] + tabela_freq.loc['No']['Yes']
        com_dc = tabela_freq.loc['Yes']['No'] + tabela_freq.loc['Yes']['Yes']
    if radio_filtro_fumadores == 'n_fumadores':
        sem_dc = tabela_freq.loc['No']['No']
        com_dc = tabela_freq.loc['Yes']['No']
    elif radio_filtro_fumadores == 'fumadores':
        sem_dc = tabela_freq.loc['No']['Yes']
        com_dc = tabela_freq.loc['Yes']['Yes']

    df_contagens = pd.DataFrame(data={'categoria': ['Sem DC', 'Com DC'], 'numero': [sem_dc, com_dc]})

    ## algumas configurações do piechart, mas segundo a documentação não tem o atributo especifico do layout, parece-me um pouco limitado...

    fig = go.Figure(
        data=[go.Pie(labels=df_contagens['categoria'], values=df_contagens['numero'], textinfo='label+percent',
                     insidetextorientation='horizontal')])
    return fig

app.run_server(debug=True)