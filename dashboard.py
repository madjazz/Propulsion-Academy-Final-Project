#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:34:43 2017

filename: dash_layout.py

description: Basic layout for dash application

author: Timo Klingler
"""
import manipulations

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col)
                    for col in dataframe.columns]
        )] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col])
                    for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))],

)

def panel_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([
            html.Td(dataframe.iloc[i][col])
                    for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))],

)


app = dash.Dash()

my_css_url = "https://codepen.io/madjazz/pen/awxxQK.css"
app.css.append_css({
    "external_url": my_css_url
})

app.layout = html.Div([# Container
        html.Div([# Header
                  html.Section([
                          html.H1([
                                  "LZH I-ELCAP Dashboard"
                                  ], id = "top-header", className = "title", style = {'text-align':'center', 'padding': '25px 0 25px 0'}),
                          ], className = "header"),
                ], className = "row"),

        html.Div([# Info-Panels
                  html.Div([# Panel 1
                            html.H5([
                                    "Total Number of Patients"
                                     ]),
                                html.H5([ "--"
                                        ])
                            ], className = "four columns panel", style = {'overflow-y': 'scroll'}),

                  html.Div([# Panel 2
                            html.H5([
                                    "Latest CT Evaluation"
                                     ]),
                            panel_table(manipulations.pan_ct, 1)
                          ], className = "four columns panel", style = {'overflow-y': 'scroll'}),

                  html.Div([# Panel 3
                            html.H5([
                                    "Next Scheduled Patient"
                                     ]),
                            panel_table(manipulations.pan_fod, 1)
                          ], className = "four columns panel", style = {'overflow-y': 'scroll'})
                ], className = "row", style = {"padding": "0 0 50px 0"}),

        html.Div([# Graph
                  html.Div([# Dropdown Figure
                            dcc.Dropdown(
                                    id='dropdown-graph',
                                    options=[
                                            {'label': 'New Patient Entries', 'value': 'manipulations.date_of_baseline_ct'},
                                            {'label': 'Total Number of Nodules (Baseline)', 'value': 'manipulations.bl_total_number_of_nodules'},
                                            {'label': 'Is it new? (Baseline)', 'value': 'manipulations.bl_new_all'},
                                            {'label': 'Endobronchial? (Baseline)', 'value': 'manipulations.bl_endo_all'},
                                            {'label': 'Most Likely Location (Baseline)', 'value': 'manipulations.bl_mll_all'},
                                            {'label': 'Nodule Consistency (Baseline)', 'value': 'manipulations.bl_nc_all'},
                                            {'label': 'Smooth Edges (Baseline)', 'value': 'manipulations.bl_sme_all'},
                                            {'label': 'Calcifications c/w Benignity (Baseline)', 'value': 'manipulations.bl_cab_all'},
                                            {'label': 'Spiculations/Pleural Tags (Baseline)', 'value': 'manipulations.bl_spic_all'},
                                            {'label': 'Parenchymal Abnormality within 1 cm (Baseline)', 'value': 'manipulations.bl_para_all'},
                                            {'label': 'Nodule Status (Baseline)', 'value': 'manipulations.bl_nods_all'},
                                            {'label': 'Action (Baseline)', 'value': 'manipulations.bl_act_all'},
                                            {'label': 'Cysts/Blebs/Bullae (Baseline)', 'value': 'manipulations.bl_cbb_all'},
                                            {'label': 'Small Airways Disease/Bronchiolectasis (Baseline)', 'value': 'manipulations.bl_sadb_all'},
                                            {'label': 'Bronchiectasis (Baseline)', 'value': 'manipulations.bl_bron_all'},
                                            {'label': 'Interstitial Lung Disease (Baseline)', 'value': 'manipulations.bl_ild_all'},
                                            {'label': 'Honeycombing (Baseline)', 'value': 'manipulations.bl_hon_all'},
                                            {'label': 'Regional or Diffuse Consolidation (Baseline)', 'value': 'manipulations.bl_rdc_all'},
                                            {'label': 'Scarring (Baseline)', 'value': 'manipulations.bl_scar_all'},
                                            {'label': 'Rounded Atelectasis (Baseline)', 'value': 'manipulations.bl_rat_all'},
                                            {'label': 'Other Atelectasis (Baseline)', 'value': 'manipulations.bl_oat_all'},
                                            {'label': 'Bronchial Resection Margin (Baseline)', 'value': 'manipulations.bl_brm_all'},
                                            {'label': 'Pleural Thickening/Fissural Plaques (Baseline)', 'value': 'manipulations.bl_ptf_all'},
                                            {'label': 'Coronary Calcification (Baseline)', 'value': 'manipulations.bl_cca_all'},
                                            {'label': 'Visual CAC Score (Baseline)', 'value': 'manipulations.bl_vcac_all'},
                                            {'label': 'Thyroid Abnormalities (Baseline)', 'value': 'manipulations.bl_thyr_all'},
                                            {'label': 'Lymph Nodes Enlarged (Baseline)', 'value': 'manipulations.bl_lnod_all'},
                                            {'label': 'Right Breast Abnormalities (Baseline)', 'value': 'manipulations.bl_rba_all'},
                                            {'label': 'Left Breast Abnormalities (Baseline)', 'value': 'manipulations.bl_lba_all'},
                                            {'label': 'Gall Bladder Abnormalities (Baseline)', 'value': 'manipulations.bl_gba_all'},
                                            {'label': 'Spleen Abnormalities (Baseline)', 'value': 'manipulations.bl_spa_all'},
                                            {'label': 'Liver Abnormalities (Baseline)', 'value': 'manipulations.bl_lia_all'},
                                            {'label': 'Pancreas Abnormalities (Baseline)', 'value': 'manipulations.bl_paa_all'},
                                            {'label': 'Adrenals Abnormalities (Baseline)', 'value': 'manipulations.bl_ada_all'},
                                            {'label': 'Kidneys Abnormalities (Baseline)', 'value': 'manipulations.bl_kia_all'},
                                            {'label': 'Follow-Up (Baseline)', 'value': 'manipulations.bl_fou_all'},
                                            {'label': 'When (Baseline)', 'value': 'manipulations.bl_when_all'},
                                            {'label': 'Impression Nodules (Baseline)', 'value': 'manipulations.bl_inod_all'}
                                            ],
                                    value='manipulations.date_of_baseline_ct'
                                    )
                          ], className = "twelve columns"),
                  html.Div([# Figure
                            dcc.Graph(id='display-graph')
                          ], className = "twelve columns")
                ], className = "row", style = {"padding": "0 0 50px 0"}),

        html.Div([# Tables
                  html.Div([# Admin
                          html.Div([# Dropdown Admin
                            html.H4(["Administration"
                                    ], style = {'text-align': 'center'}),
                            dcc.Dropdown(
                                    id='dropdown-admin',
                                    options=[
                                            {'label': 'CT Evaluations', 'value': 'manipulations.bl_cte_all'},
                                            {'label': 'Follow-up Dates', 'value': 'manipulations.bl_fod_all'}
                                            ],
                                    value='manipulations.bl_cte_all'
                                    )
                            ]),
                            html.Div(# Table Admin
                                     id = "table-admin", style = {'height':'250px', 'overflow-y':'scroll', 'padding': '0 0 50px 0'})], className = "six columns"),
                  html.Div([# Doctors
                            html.Div([# Dropdown Doctors
                                      html.H4(["Physicians"
                                    ], style = {'text-align': 'center'}),
                            dcc.Dropdown(
                                    id='dropdown-doctors',
                                    options=[
                                            {'label': 'Distance from the Costal Pleura (in mm) (Baseline)', 'value': 'manipulations.bl_stat_dist'},
                                            {'label': 'Nodule Length (in mm) (Baseline)', 'value': 'manipulations.bl_stat_nodl'},
                                            {'label': 'Maximum Nodule Width (in mm) (Baseline)', 'value': 'manipulations.bl_stat_nodw'},
                                            ],
                                    value='manipulations.bl_stat_dist'
                                    )
                            ]),
                  html.Div(# Table Doctors
                          id = "table-doctors", style = {'height':'260px', 'overflow-y':'scroll', 'padding': '0 0 50px 0'})
                            ], className = "six columns"),

                ], className = "row"),
        ], className = "container")

# Figure

@app.callback(Output('display-graph', 'figure'),
              [Input('dropdown-graph', 'value')])
def update_graph(selected_dropdown_value):

    if selected_dropdown_value == 'manipulations.date_of_baseline_ct':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Date of Baseline CT"],
                        'y' : selected_dropdown_value["Cumulative Sum"],
                        'name': 'Cumulative New Patient Entries',
                        'type': 'line'
                    },
                        {
                         'x': selected_dropdown_value["Date of Baseline CT"],
                         'y' : selected_dropdown_value["Count"],
                         'name': 'Absolute New Patient Entries',
                         'type': 'line'
                        }
                    ],

                    'layout': {
                              'title': 'New Patient Entries',
                              'xaxis': {'title' : 'Timeline'},
                              'yaxis' : {'title' : 'Count'}
                              }
                }

    elif selected_dropdown_value == 'manipulations.bl_total_number_of_nodules':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Total Number of Non-Calcified Nodules"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Total Number of Non-Calcified Nodules",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Total Number of Nodules"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Total Number of Nodules",
                         'type': "bar"
                        }
                    ],

                    'layout': {
                              'title': 'Total Number of Nodules (Baseline)',
                              'xaxis': {'title' : 'Number of Nodules'},
                              'yaxis' : {'title' : 'Count'},
                              'barmode': 'group',
                              'bargap' : 0.1
                              }
                }

    elif selected_dropdown_value == 'manipulations.bl_new_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Is it new? (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Is it new? (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Is it new? (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Is it new? (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Is it new? (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Is it new? (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Is it new? (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }
                }
    elif selected_dropdown_value == 'manipulations.bl_endo_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Endobronchial? (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Endobronchial? (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Endobronchial? (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Endobronchial? (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Endobronchial? (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Endobronchial? (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Endobronchial? (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_mll_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Most Likely Location (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Most Likely Location (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Most Likely Location (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Most Likely Location (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Most Likely Location (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Most Likely Location (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Most Likely Location (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_nc_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Nodule Consistency (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Nodule Consistency (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Consistency (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Consistency (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Consistency (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Consistency (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Nodule Consistency (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_sme_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Smooth Edges (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Smooth Edges (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Smooth Edges (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Smooth Edges (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Smooth Edges (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Smooth Edges (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Smooth Edges (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_cab_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Calcifications c/w Benignity (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Calcifications c/w Benignity (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Calcifications c/w Benignity (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Calcifications c/w Benignity (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Calcifications c/w Benignity (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Calcifications c/w Benignity (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Calcifications c/w Benignity (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_spic_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Spiculations /Pleural Tags (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Spiculations /Pleural Tags (Nodule 1)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Spiculations /Pleural Tags (Nodule 1)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Spiculations /Pleural Tags (Nodule 1)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Spiculations /Pleural Tags (Nodule 1)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Spiculations /Pleural Tags (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Spiculations/Pleural Tags (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_para_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Parenchymal Abnormality within 1 cm (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Parenchymal Abnormality within 1 cm (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Parenchymal Abnormality within 1 cm (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Parenchymal Abnormality within 1 cm (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Parenchymal Abnormality within 1 cm (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Parenchymal Abnormality within 1 cm (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Parenchymal Abnormality within 1 cm (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_nods_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Nodule Status (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Nodule Status (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Status (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Status (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Status (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Nodule Status (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Nodule Status (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_act_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Action (Nodule 1)"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Nodule 1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Action (Nodule 2)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 2",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Action (Nodule 3)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Action (Nodule 4)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 4",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Action (Nodule 5)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Nodule 5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Action (Additional Nodule)"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Additional Nodule",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Action (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_cbb_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Cysts/Blebs/Bullae RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Cysts/Blebs/Bullae RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Cysts/Blebs/Bullae RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Cysts/Blebs/Bullae LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Cysts/Blebs/Bullae LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Cysts/Blebs/Bullae (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_sadb_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Small Airways Disease/Bronchiolectasis RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Small Airways Disease/Bronchiolectasis RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Small Airways Disease/Bronchiolectasis RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Small Airways Disease/Bronchiolectasis LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Small Airways Disease/Bronchiolectasis LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Small Airways Disease/Bronchiolectasis (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_bron_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Bronchiectasis RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Bronchiectasis RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Bronchiectasis RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Bronchiectasis LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Bronchiectasis LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Bronchiectasis (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_ild_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Interstitial lung disease RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Interstitial lung disease RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Interstitial lung disease RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Interstitial lung disease LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Interstitial lung disease LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Interstitial Lung Disease (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_hon_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Honeycombing RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Honeycombing RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Honeycombing RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Honeycombing LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Honeycombing LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Honeycombing (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_rdc_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Regional or Diffuse Consolidation RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Regional or Diffuse Consolidation RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Regional or Diffuse Consolidation RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Regional or Diffuse Consolidation LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Regional or Diffuse Consolidation LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Regional or Diffuse Consolidation (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_scar_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Scarring RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Scarring RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Scarring RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Scarring LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Scarring LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Scarring (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_rat_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Rounded Atelectasis RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Rounded Atelectasis RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Rounded Atelectasis RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Rounded Atelectasis LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Rounded Atelectasis LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Other Atelectasis (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_oat_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Other Atelectasis RUL"],
                        'y': selected_dropdown_value["Count"],
                        'name': "RUL",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Other Atelectasis RML"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RML",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Other Atelectasis RLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RLL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Other Atelectasis LUL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LUL",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Other Atelectasis LLL"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LLL",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Other Atelectasis (Baseline)',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_brm_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Bronchial Resection Margin"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Bronchial Resection Margin",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Bronchial Resection Margin Left"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Left",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Bronchial Resection Margin Right"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Right",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Bronchial Resection Margin',
                              'xaxis': {'title' : 'Type/Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_ptf_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Pleural Thickening/Fissural Plaques Right"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Right",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Pleural Thickening/Fissural Plaques Left"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Left",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Pleural Thickening/Fissural Plaques Calcification"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Calcification",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Pleural Thickening/Fissural Plaques',
                              'xaxis': {'title' : 'Type/Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_cca_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Coronary Calcification Left Main"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Left Main",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Coronary Calcification LAD"],
                         'y': selected_dropdown_value["Count"],
                         'name': "LAD",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Coronary Calcification Circumflex"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Circumflex",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Coronary Calcification RCA"],
                         'y': selected_dropdown_value["Count"],
                         'name': "RCA",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Coronary Calcification Plaques',
                              'xaxis': {'title' : 'Location'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_vcac_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Visual CAC Score"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Visual CAC Score",
                        'type': 'bar'
                    }

                    ],

                    'layout': {
                              'title': 'Visual CAC Score',
                              'xaxis': {'title' : 'Score'},
                              'yaxis' : {'title' : 'Count'},
                              'barmode' : 'group',
                              'bargap' : 0.1
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_thyr_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Thyroid Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Thyroid Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Thyroid Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Thyroid Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Thyroid Abnormalities',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_lnod_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Lymph Nodes Enlarged N1"],
                        'y': selected_dropdown_value["Count"],
                        'name': "N1",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N2R"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N2L",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N2L"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N2R",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N3"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N3",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N4R"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N4R",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N4L"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N4L",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N5"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N5",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N6"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N6",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N7"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N7",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N8"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N8",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N9"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N9",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N10R"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N10R",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Lymph Nodes Enlarged N10L"],
                         'y': selected_dropdown_value["Count"],
                         'name': "N10L",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Lymph Nodes Enlarged (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_rba_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Right Breast Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Right Breast Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Right Breast Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Right Breast Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Right Breast Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_lba_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Left Breast Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Left Breast Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Left Breast Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Left Breast Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Left Breast Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_gba_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Gall Bladder Cholecystectomy"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Cholecystectomy",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Gall Bladder Stones"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Stones",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Gall Bladder Sludge"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Sludge",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Gall Bladder Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Gall Bladder Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_spa_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Spleen Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Spleen Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Spleen Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Spleen Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Spleen Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_lia_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Liver Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Liver Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Liver Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Liver Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Liver Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_paa_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Pancreas Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Pancreas Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Pancreas Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Pancreas Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Pancreas Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_ada_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Adrenals Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Adrenals Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Adrenals Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Adrenals Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Adrenals Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_kia_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Kidneys Calcification"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Calcification",
                        'type': 'bar'
                    },
                        {
                         'x': selected_dropdown_value["Kidneys Cyst"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Cyst",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Kidneys Mass"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Mass",
                         'type': "bar"
                    },
                        {
                         'x': selected_dropdown_value["Kidneys Other"],
                         'y': selected_dropdown_value["Count"],
                         'name': "Other",
                         'type': "bar"
                    }

                    ],

                    'layout': {
                              'title': 'Kidneys Abnormalities (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_fou_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Follow-up"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Follow-Up (Baseline)",
                        'type': 'bar'
                    }

                    ],

                    'layout': {
                              'title': 'Follow-Up (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_when_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["When"],
                        'y': selected_dropdown_value["Count"],
                        'name': "When (Baseline)",
                        'type': 'bar'
                    }

                    ],

                    'layout': {
                              'title': 'When (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

    elif selected_dropdown_value == 'manipulations.bl_inod_all':
        selected_dropdown_value = eval(selected_dropdown_value)
        return {
                    'data': [
                        {
                        'x': selected_dropdown_value["Impression Nodules"],
                        'y': selected_dropdown_value["Count"],
                        'name': "Impression Nodules (Baseline)",
                        'type': 'bar'
                    }

                    ],

                    'layout': {
                              'title': 'Impression Nodules (Baseline)',
                              'xaxis': {'title' : 'Type'},
                              'yaxis' : {'title' : 'Count'}
                              }

                }

# Admin Table

@app.callback(
    Output(component_id='table-admin', component_property='children'),
    [Input(component_id='dropdown-admin', component_property='value')]
)
def update_output_div(input_value):
    return generate_table(eval(input_value), 100),

# Doctor Table

@app.callback(
    Output(component_id='table-doctors', component_property='children'),
    [Input(component_id='dropdown-doctors', component_property='value')]
)
def update_output_div(input_value):
    return generate_table(round(eval(input_value), 2), 100)
