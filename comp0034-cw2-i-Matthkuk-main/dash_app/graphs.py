from pathlib import Path
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

FOOTBALL_FILE_PATH1415 = Path(__file__).parent.joinpath(
    'data', 'fb_cleaned1415.csv')
FOOTBALL_FILE_PATH1516 = Path(__file__).parent.joinpath(
    'data', 'fb_cleaned1516.csv')
FOOTBALL_FILE_PATH1617 = Path(__file__).parent.joinpath(
    'data', 'fb_cleaned1617.csv')
FOOTBALL_FILE_PATH1718 = Path(__file__).parent.joinpath(
    'data', 'fb_cleaned1718.csv')
FOOTBALL_FILE_PATH1819 = Path(__file__).parent.joinpath(
    'data', 'fb_cleaned1819.csv')

df_path = [FOOTBALL_FILE_PATH1415, FOOTBALL_FILE_PATH1516,
           FOOTBALL_FILE_PATH1617, FOOTBALL_FILE_PATH1718, FOOTBALL_FILE_PATH1819]
df_list = []
home_goal_avg_list = []

# Read the data
for i in range(5):
    df_read = pd.read_csv(df_path[i])
    df_list.append(df_read)

    home_goal_sum = df_list[i]['FTHG'].sum(numeric_only=True)
    home_goal_average = home_goal_sum / 19
    home_goal_avg_list.append(home_goal_average)

bar_goals_list = []
# Create bar chart
for i in range(5):
    bar_goals = px.bar(df_list[i],
                       x='HomeTeam', y='FTHG',
                       labels={'FTHG': 'Home Team Goals',
                               'HomeTeam': 'Home Team'},
                       template='simple_white',
                       color='FTHG',
                       color_continuous_scale=px.colors.sequential.Blues
                       )
    bar_goals.update_yaxes(
        showgrid=True
    )

    bar_goals.add_shape(  # add a horizontal "target" line
        type="line", line_color="orange", line_width=3, opacity=1, line_dash="dot",
        x0=0, x1=1, xref="paper", y0=home_goal_avg_list[i], y1=home_goal_avg_list[i], yref="y"
    )

    bar_goals.add_annotation(  # add a text callout with arrow
        text="Average Goals", x=19/2, y=home_goal_avg_list[i] + 1.5, arrowhead=1, showarrow=True
    )
    bar_goals_list.append(bar_goals)

bar_goal_default = bar_goals_list[0]
home_top_score = []
home_top_goal = []
total_goals_year = []

for i in range(5):
    team_hg_year = df_list[i].groupby('HomeTeam')['FTHG'].sum()
    league_top_score = team_hg_year.idxmax()
    home_top_score.append(league_top_score)
    league_top_goals = team_hg_year.max()
    home_top_goal.append(league_top_goals)
    total_goals_year.append(team_hg_year)

# Graph code
default_team = 'Chelsea'
total_goals = pd.concat([total_goals_year[0], total_goals_year[1],
                        total_goals_year[2], total_goals_year[3], total_goals_year[4]], axis=1)
total_goals.columns = ['Season 14/15', 'Season 15/16',
                       'Season 16/17', 'Season 17/18', 'Season 18/19']
total_goals = total_goals.transpose().reset_index().fillna(0)
total_goals_graph = px.line(total_goals, x='index', y=default_team, labels={
                            'index': 'Season', default_team: 'Goals'})
# Drop down list code
teams_T = total_goals.transpose().reset_index()
teams = teams_T['HomeTeam'].tolist()
del teams[0]


def create_dash_app(flask_app):
    dash_app = Dash(__name__,
                    server=flask_app,
                    url_base_pathname='/dashboard/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    meta_tags=[
                        {"name": "viewport",
                            "content": "width=device-width, initial-scale=1"},
                    ],
                    )

    dash_app.layout = dbc.Container([
        html.H1("Visualisations Dashboard", style={
                'background': '#2b5dba', 'color': 'white', 'margin-bottom': 0},),
        html.Div(
            id='menu_bar', children=[
                html.H3(
                    'The premium hub for football statistics', style={'text-align': 'center', 'color': 'white'}
                ),
            ],
            style={'background-color': 'Orange', 'height': 35, 'margin': 0}
        ),
        dbc.Row(
            [
                # This is for the season selector
                dbc.Col(width=3, children=[
                    html.H3("Select Season", style={'color': 'Blue'}),
                    dcc.Dropdown(
                        id='season_select',
                        options=[
                            {'label': '14/15', 'value': 0},
                            {'label': '15/16', 'value': 1},
                            {'label': '16/17', 'value': 2},
                            {'label': '17/18', 'value': 3},
                            {'label': '18/19', 'value': 4},
                        ],
                        value=4,
                        clearable=False,
                        style={'background-color': '#cfcfcf'}
                    ),
                    html.Br(),
                    html.Div(id='stats_card'),
                ],
                ),
                # This is for the figure.
                dbc.Col(width=9, children=[
                        dcc.Graph(
                            id='bar_HG',
                            figure=bar_goal_default)
                        ],
                        ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    width=8, children=[
                        dcc.Graph(
                            id='line_HG',
                            figure=total_goals_graph,
                        )
                    ]
                ),
                dbc.Col(
                    width=4, children=[
                        html.H3('Select Team', style={'color': 'Blue'}),
                        dcc.Dropdown(
                            id='team_select',
                            options=[
                                {'label': x, 'value': x}
                                for x in teams
                            ],
                            value='Chelsea',
                            clearable=False,
                            style={'background-color': '#cfcfcf'}
                        ),
                        html.Br(),
                        html.Div(id='team_stats_card'),
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    width=4, children=[
                        html.H3(
                            'Tell Us Your Thoughts'
                        ),
                        dcc.Textarea(
                            id='comments_box',
                            placeholder='Comments here...',
                            style={'width': '100%',
                                   'height': 125, 'resize': 'none'},
                            maxLength=300,
                        ),
                        html.Button(
                            'Submit',
                            id='comments_box_submit',
                            n_clicks=0,
                            style={'background-color': '#57a0eb', },
                        )
                    ]
                ),
                dbc.Col(
                    width=4, children=[
                        html.Div(
                            id='comments_section_output', style={'word-wrap': 'break-word', 'white-space': 'pre-line'},
                        )
                    ]
                ),
                dbc.Col(
                    width=4, children=[
                        html.H3(
                            'Please Rate Us'
                        ),
                        dcc.Slider(
                            0, 10, 1,
                            value=5,
                            id='ratings_slider'
                        ),
                        html.Div(
                            id='ratings_output',
                            style={'word-wrap': 'break-word',
                                   'white-space': 'pre-line'},
                        ),
                        html.Button(
                            'Submit',
                            id='ratings_submit',
                            n_clicks=0,
                            style={'background-color': 'DeepSkyBlue',
                                   'float': 'right'}
                        )
                    ]
                ),
            ]
        ),
    ],
        fluid=True,
    )

    @dash_app.callback(Output("bar_HG", "figure"), Input("season_select", "value"))
    def update_bar_chart(season_select):
        bar_goal_default = bar_goals_list[season_select]
        return bar_goal_default

    @dash_app.callback(Output("stats_card", "children"), Input("season_select", "value"))
    def render_stats_panel(season_select):
        card = dbc.Card(color='CornFlowerBlue', inverse=True, children=[
            dbc.CardBody([
                html.H3('Average Home Goals: '),
                html.H4(round(home_goal_avg_list[season_select], 2)),
                html.Br(),
                html.H3('Top Home Team Goal Scorers: '),
                html.H4(home_top_score[season_select]),
                html.Br(),
                html.H3('Goals: '),
                html.H4(home_top_goal[season_select]),
            ])
        ])
        return card

    @dash_app.callback(Output("line_HG", "figure"), Input("team_select", "value"))
    def update_bar_chart(team_select):
        total_goals_graph = px.line(total_goals, x='index', y=team_select, labels={
            'index': 'Season', team_select: 'Home Goals'})
        return total_goals_graph

    @dash_app.callback(Output("team_stats_card", "children"), Input("team_select", "value"))
    def render_stats_panel(team_select):
        present_goals = total_goals.loc[4, team_select]
        max_goals = total_goals[team_select].max()
        difference_goals = present_goals - max_goals
        old_average_goals = (
            total_goals[team_select].sum() - present_goals) / 4
        form = present_goals - old_average_goals
        if difference_goals == 0:
            difference_goals = 'This is their best performance yet!'
        else:
            difference_goals = round(difference_goals)
        if form < 0:
            source = 'https://cdn-icons-png.flaticon.com/512/20/20919.png'
        else:
            source = 'https://www.seekpng.com/png/full/15-155515_trending-up-arrow-chart-increase-comments-arrow-going.png'

        card1 = dbc.Card(color='Skyblue', inverse=True, children=[
            dbc.CardBody([
                html.H3('Difference Between Current and Best Season: '),
                html.H4(difference_goals),
                html.Br(),
                html.H3("Previous Season's Home Goal Average: "),
                html.H4(round(old_average_goals, 2)),
                html.Br(),
                html.H3('Current Home Playing Form: '),
                html.Img(src=source, width=100, height=80,)
            ])
        ])
        return card1

    @dash_app.callback(
        Output('comments_section_output', 'children'),
        Input('comments_box_submit', 'n_clicks'),
        State('comments_box', 'value')
    )
    def update_output_comments(n_clicks, value):
        if n_clicks > 0:
            return 'Comment: \n{}'.format(value)

    @dash_app.callback(
        Output('ratings_output', 'children'),
        Input('ratings_submit', 'n_clicks'),
        State('ratings_slider', 'value'))
    def update_output_ratings(n_clicks, value):
        if n_clicks > 0 and value > 4:
            return 'You Selected: {}'.format(value), '\nThank you for the kind rating!'
        elif n_clicks > 0 and value < 5:
            return 'You Selected: {}'.format(value), '\nTell us what we could have done better in the comments section.'
