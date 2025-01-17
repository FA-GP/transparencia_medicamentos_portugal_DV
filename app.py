import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

path = 'databases/'
df_despesa_com_medicamentos_no_sns_por_ano_por_regiao = pd.DataFrame(data=pd.read_csv(path + 'despesa_com_medicamentos_no_sns_por_ano_por_regiao.csv'))

path = 'databases/'
df_despesa_com_medicamentos_no_sns_por_ano = pd.DataFrame(data=pd.read_csv(path + 'despesa_com_medicamentos_no_sns_por_ano.csv'))



path = 'databases/'
df_treemap = pd.DataFrame(data=pd.read_csv(path + 'dispensa-de-medicamentos-por-grupo-farmacoterapeutico-por-ano-por-regiao.csv'))
path = ''
df_bar_chart = pd.DataFrame(data=pd.read_csv(path + 'bar_chart_dummy.csv'))


#Total = Hospitalar + Ambulatório PVP
#Ambulatório PVP = Ambulatório Encargo Utentes + Ambulatório Comparticipalção SNS

dropdown_dispensa_medicamentos_tipo_1 = [
    {'label': 'Total', 'value': 'total'},
    {'label': 'Hospitalar', 'value': 'encargos_sns_hospitalar'},
    {'label': 'Ambulatório PVP', 'value': 'valor_pvp_ambulatorio'},
    {'label': 'Ambulatório Comparticipalção SNS', 'value': 'encargos_sns_ambulatorio'},
    {'label': 'Ambulatório Encargo Utentes', 'value': 'encargos_utentes_ambulatorio'},
]

dropdown_dispensa_medicamentos_regiao_2 = [
    {'label': 'Nacional', 'value': 'Nacional'},
    {'label': 'Norte', 'value': 'Norte'},
    {'label': 'Centro', 'value': 'Centro'},
    {'label': 'LVT', 'value': 'LVT'},
    {'label': 'Alentejo', 'value': 'Alentejo'},
    {'label': 'Algarve', 'value': 'Algarve'},
]

#Total = Hospitalar + Ambulatório PVP
#Ambulatório PVP = Ambulatório Encargo Utentes + Ambulatório Comparticipalção SNS

dropdown_dispensa_medicamentos_tipo_1 = [
    {'label': 'Total', 'value': 'total'},
    {'label': 'Hospitalar', 'value': 'encargos_sns_hospitalar'},
    {'label': 'Ambulatório PVP', 'value': 'valor_pvp_ambulatorio'},
    {'label': 'Ambulatório Comparticipalção SNS', 'value': 'encargos_sns_ambulatorio'},
    {'label': 'Ambulatório Encargo Utentes', 'value': 'encargos_utentes_ambulatorio'},
]

app = Dash(__name__)

## HTML em dash
app.layout = html.Div([
    html.Div([
        html.Div([

            html.H2('Medicamentos - Portal da Transparência')

            ],style={'width':'79%','position': 'center'}
        ),
        html.Div([
            html.Div([

                html.Img(src=app.get_asset_url('logo.png'),style={'width': '60px', 'position': 'center'})
            ], id='logo')

        ],style={'width':'25%'}),
    ],className='row container', style={'display': 'flex'}),

    html.Div([
        html.Div([

            html.H3('Explicação sobre o trabalho de DV'),
            html.Label('Explicações nevessárias sobre vários motivos e razões relativa a situações variadas e essenciais para uma boa relação entre as difrentes consistências ')

        ], className='row'),
    ]),

    html.Br(),

    html.Div([
        html.Div([
            html.H3('Gastos medicmaentos por ARS entre 2017 e 2021 texto grande so para testar coisas ')
        ], className='row', style={'display': 'flex','text-align': 'center'}),
        html.Br(),
        html.Div([
            html.Div([

                html.Div([
                    dcc.Dropdown(
                        id='dropdown_dispensa_medicamentos_tipo_1',
                        options=dropdown_dispensa_medicamentos_tipo_1,
                        value='total',
                        searchable=False,
                        clearable=False
                    )
                ],className='row', style={'display': 'flex','text-align': 'center'}),

                html.Br(),

                html.Div([
                    dcc.Graph(id='line_chart_dispensa_medicamentos_1')
                ], className='row', style={'display': 'flex'}),



            ], className='col2', style={'width':'49%','float':'left'}),
            html.Div([

                html.Div([
                    dcc.Dropdown(
                        id='dropdown_dispensa_medicamentos_regiao_2',
                        options=dropdown_dispensa_medicamentos_regiao_2,
                        value='Nacional',
                        searchable=False,
                        clearable=False
                    ),
                ],className='row', style={'display': 'flex','text-align': 'center'}),

                html.Br(),

                html.Div([
                    dcc.Graph(id='stacked_bar_chart_medicamentos_2'),
                ],className='row', style={'display': 'flex'}),

            ], className='col2', style={'width':'49%','float':'right'}),
        ],className='row', style={'display': 'flex'}),
    ], className='row container', style={'display': 'block'}),

    html.Br(),

    html.Div([
        html.Div([

            html.H3('Gastos medicmaentos por ARS entre 2017 e 2021 texto grande so para testar coisas ')

        ], className='row', style={'display': 'flex','text-align': 'center'}),
        html.Br(),
        html.Div([

        ],className='row', style={'display': 'flex'}),
    ], className='row container', style={'display': 'block'}),

    html.Br(),

    html.Div([
        html.Div([

            html.H3('considerações finais')

        ], className='row', style={'display': 'flex','text-align': 'center'}),
        html.Br(),
        html.Div([

            html.Label('tesxto bonito com as referencias')

        ], className='row', style={'display': 'flex','text-align': 'center'})
    ], className='row container', style={'display': 'block'}),
])

@app.callback(
    Output("line_chart_dispensa_medicamentos_1", "figure"),
    Output("stacked_bar_chart_medicamentos_2", "figure"),
    Input("dropdown_dispensa_medicamentos_tipo_1", "value"),
    Input("dropdown_dispensa_medicamentos_regiao_2", "value"),

)

def generate_chart(dropdown_dispensa_medicamentos_tipo_1,dropdown_dispensa_medicamentos_regiao_2,):
    
    # line_chart_dispensa_medicamentos_1

    gasto_medicamentos_nacional_por_ano = df_despesa_com_medicamentos_no_sns_por_ano.sort_values(by='ano', ascending=True)
    gasto_medicamentos_regiao_por_ano = df_despesa_com_medicamentos_no_sns_por_ano_por_regiao.sort_values(by='ano', ascending=True)

    gasto_medicamentos_regiao_por_ano_ordenado = gasto_medicamentos_regiao_por_ano.sort_values(by='total', ascending=False)
    lista_de_regioes = gasto_medicamentos_regiao_por_ano_ordenado['regiao'].tolist()
    lista_de_regioes = list(dict.fromkeys(lista_de_regioes))

    gasto_medicamentos_nacional_por_ano['ano'] = gasto_medicamentos_nacional_por_ano['ano'].apply(str)
    gasto_medicamentos_regiao_por_ano['ano'] = gasto_medicamentos_regiao_por_ano['ano'].apply(str)

    line_chart_dispensa_medicamentos_1 = go.Figure()
    line_chart_dispensa_medicamentos_1.add_trace(go.Scatter(x=gasto_medicamentos_nacional_por_ano['ano'],
                                      y=gasto_medicamentos_nacional_por_ano[dropdown_dispensa_medicamentos_tipo_1],
                                      mode='lines+markers',
                                      name='Nacional'))

    for regiao in lista_de_regioes:

        gastos_por_regiao = gasto_medicamentos_regiao_por_ano.loc[gasto_medicamentos_regiao_por_ano['regiao'] == regiao]

        line_chart_dispensa_medicamentos_1.add_trace(go.Scatter(x=gastos_por_regiao['ano'],
                                          y=gastos_por_regiao[dropdown_dispensa_medicamentos_tipo_1],
                                          mode='lines+markers',
                                          name=regiao
                                          ))

    line_chart_dispensa_medicamentos_1.update_layout(title='Evolução dos gastos em medicamentos entre 2017 e 2021',
                               xaxis_title='Anos',
                               yaxis_title='Gastos em milhões de €',
                               paper_bgcolor='#FFFFFF')


    # stacked_bar_chart_medicamentos_2
    ## filtro aplicado com a função .loc[] com logica para ter apenas dados da ars selecionada no dropdown menu correspondente


    if dropdown_dispensa_medicamentos_regiao_2 == 'Nacional':
        data_base = df_despesa_com_medicamentos_no_sns_por_ano.sort_values(by='ano', ascending=True)
    else:
        data_base = df_despesa_com_medicamentos_no_sns_por_ano_por_regiao.sort_values(by='ano', ascending=True)
        data_base = data_base.loc[data_base['regiao'] == dropdown_dispensa_medicamentos_regiao_2]

    layout_bar_1 = dict(title=dict(text='Gastros por categoria entre 2017 e 2021'),
                      yaxis=dict(title='% de Gastos por categoria'),
                      xaxis=dict(title='Ano'),
                      paper_bgcolor='#FFFFFF'
                      )

    y_encargos_sns_hospitalar = (((data_base['encargos_sns_hospitalar'] / data_base['total']).round(decimals = 3)*100).tolist())
    y_encargos_sns_ambulatorio = (((data_base['encargos_sns_ambulatorio'] / data_base['total']).round(decimals = 3)*100).tolist())
    y_encargos_utentes_ambulatorio = (((data_base['encargos_utentes_ambulatorio'] / data_base['total']).round(decimals = 3)*100).tolist())

    stacked_bar_chart_medicamentos_2 = go.Figure(
        data=[
            go.Bar(name='encargos_sns_hospitalar', x=data_base['ano'].tolist(), y=y_encargos_sns_hospitalar),
            go.Bar(name='encargos_sns_ambulatorio', x=data_base['ano'].tolist(), y=y_encargos_sns_ambulatorio),
            go.Bar(name='encargos_utentes_ambulatorio', x=data_base['ano'].tolist(), y=y_encargos_utentes_ambulatorio),
        ],layout=layout_bar_1,)

    stacked_bar_chart_medicamentos_2.update_layout(barmode='stack')

    # layout_yaxis_range=[0,max(gasto_medicamentos['encargos_sns_ambulatorio'])]


    return line_chart_dispensa_medicamentos_1, stacked_bar_chart_medicamentos_2



## linha necessária par execuar a app
if __name__ == '__main__':
    app.run_server(debug=True)