import typing

import plotly.graph_objs as go
import plotly.io as pio

COLORWAY: typing.List[str] = [
    "#227c9d",
    "#fe6d73",
    "#87c38f",
    "#6a4c93",
    "#ffcb77",
    "#91e5f6",
    "#f84aa7",
    "#226f54",
    "#ffadad",
    "#ffd60a",
]

SANS_SERIF: str = "Sans-serif"
TITLE_FONT: str = "Open Sans, Serif"

LINE_COLOR: str = "#1b1e23"
GRID_COLOR: str = "#ebf0f8"
BACKGROUND_COLOR: str = "white"

pio.templates["morning_coffee"] = go.layout.Template(
    {
        "data": {
            "bar": [
                {
                    "error_x": {"color": LINE_COLOR},
                    "error_y": {"color": LINE_COLOR},
                    "marker": {
                        "line": {"color": BACKGROUND_COLOR, "width": 0.5},
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    },
                    "type": "bar",
                }
            ],
            "barpolar": [
                {
                    "marker": {
                        "line": {"color": BACKGROUND_COLOR, "width": 0.5},
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    },
                    "type": "barpolar",
                }
            ],
            "carpet": [
                {
                    "aaxis": {
                        "endlinecolor": LINE_COLOR,
                        "gridcolor": GRID_COLOR,
                        "linecolor": GRID_COLOR,
                        "minorgridcolor": GRID_COLOR,
                        "startlinecolor": LINE_COLOR,
                    },
                    "baxis": {
                        "endlinecolor": LINE_COLOR,
                        "gridcolor": GRID_COLOR,
                        "linecolor": GRID_COLOR,
                        "minorgridcolor": GRID_COLOR,
                        "startlinecolor": LINE_COLOR,
                    },
                    "type": "carpet",
                }
            ],
            "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}],
            "contour": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "contour",
                }
            ],
            "contourcarpet": [
                {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}
            ],
            "heatmap": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "heatmap",
                }
            ],
            "histogram": [
                {
                    "marker": {"pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2}},
                    "type": "histogram",
                }
            ],
            "histogram2d": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "histogram2d",
                }
            ],
            "histogram2dcontour": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "histogram2dcontour",
                }
            ],
            "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}],
            "parcoords": [
                {
                    "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "parcoords",
                }
            ],
            "pie": [{"automargin": True, "type": "pie"}],
            "scatter": [
                {
                    "line": {"width": 1.5},
                    "fillpattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    "type": "scatter",
                }
            ],
            "scatter3d": [
                {
                    "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatter3d",
                }
            ],
            "scattercarpet": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattercarpet",
                }
            ],
            "scattergeo": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattergeo",
                }
            ],
            "scattergl": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattergl",
                }
            ],
            "scattermapbox": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scattermapbox",
                }
            ],
            "scatterpolar": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterpolar",
                }
            ],
            "scatterpolargl": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterpolargl",
                }
            ],
            "scatterternary": [
                {
                    "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                    "type": "scatterternary",
                }
            ],
            "surface": [
                {
                    "colorbar": {"outlinewidth": 0, "ticks": ""},
                    "colorscale": [
                        [0.0, "#0d0887"],
                        [0.1111111111111111, "#46039f"],
                        [0.2222222222222222, "#7201a8"],
                        [0.3333333333333333, "#9c179e"],
                        [0.4444444444444444, "#bd3786"],
                        [0.5555555555555556, "#d8576b"],
                        [0.6666666666666666, "#ed7953"],
                        [0.7777777777777778, "#fb9f3a"],
                        [0.8888888888888888, "#fdca26"],
                        [1.0, "#f0f921"],
                    ],
                    "type": "surface",
                }
            ],
            "table": [
                {
                    "cells": {"fill": {"color": GRID_COLOR}, "line": {"color": BACKGROUND_COLOR}},
                    "header": {
                        "fill": {"color": GRID_COLOR},
                        "line": {"color": BACKGROUND_COLOR},
                    },
                    "type": "table",
                }
            ],
        },
        "layout": {
            "annotationdefaults": {
                "arrowcolor": LINE_COLOR,
                "arrowhead": 0,
                "arrowwidth": 1,
            },
            "autotypenumbers": "strict",
            "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
            "colorscale": {
                "diverging": [
                    [0, "#8e0152"],
                    [0.1, "#c51b7d"],
                    [0.2, "#de77ae"],
                    [0.3, "#f1b6da"],
                    [0.4, "#fde0ef"],
                    [0.5, "#f7f7f7"],
                    [0.6, "#e6f5d0"],
                    [0.7, "#b8e186"],
                    [0.8, "#7fbc41"],
                    [0.9, "#4d9221"],
                    [1, "#276419"],
                ],
                "sequential": [
                    [0.0, "#0d0887"],
                    [0.1111111111111111, "#46039f"],
                    [0.2222222222222222, "#7201a8"],
                    [0.3333333333333333, "#9c179e"],
                    [0.4444444444444444, "#bd3786"],
                    [0.5555555555555556, "#d8576b"],
                    [0.6666666666666666, "#ed7953"],
                    [0.7777777777777778, "#fb9f3a"],
                    [0.8888888888888888, "#fdca26"],
                    [1.0, "#f0f921"],
                ],
                "sequentialminus": [
                    [0.0, "#0d0887"],
                    [0.1111111111111111, "#46039f"],
                    [0.2222222222222222, "#7201a8"],
                    [0.3333333333333333, "#9c179e"],
                    [0.4444444444444444, "#bd3786"],
                    [0.5555555555555556, "#d8576b"],
                    [0.6666666666666666, "#ed7953"],
                    [0.7777777777777778, "#fb9f3a"],
                    [0.8888888888888888, "#fdca26"],
                    [1.0, "#f0f921"],
                ],
            },
            "colorway": COLORWAY,
            "font": {"color": LINE_COLOR, "family": SANS_SERIF, "size": 10},
            "geo": {
                "bgcolor": BACKGROUND_COLOR,
                "lakecolor": BACKGROUND_COLOR,
                "landcolor": BACKGROUND_COLOR,
                "showlakes": True,
                "showland": True,
                "subunitcolor": GRID_COLOR,
            },
            "hoverlabel": {
                "align": "left",
                "bgcolor": BACKGROUND_COLOR,
                "font_family": SANS_SERIF,
                "font_size": 10,
            },
            "hovermode": "x unified",
            "mapbox": {"style": "light"},
            "paper_bgcolor": BACKGROUND_COLOR,
            "plot_bgcolor": BACKGROUND_COLOR,
            "polar": {
                "angularaxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": GRID_COLOR,
                    "ticks": "",
                },
                "bgcolor": BACKGROUND_COLOR,
                "radialaxis": {
                    "gridcolor": GRID_COLOR,
                    "linecolor": GRID_COLOR,
                    "ticks": "",
                },
            },
            "scene": {
                "xaxis": {
                    "backgroundcolor": BACKGROUND_COLOR,
                    "gridcolor": GRID_COLOR,
                    "gridwidth": 2,
                    "linecolor": GRID_COLOR,
                    "showbackground": True,
                    "ticks": "",
                    "zerolinecolor": GRID_COLOR,
                },
                "yaxis": {
                    "backgroundcolor": BACKGROUND_COLOR,
                    "gridcolor": GRID_COLOR,
                    "gridwidth": 2,
                    "linecolor": GRID_COLOR,
                    "showbackground": True,
                    "ticks": "",
                    "zerolinecolor": GRID_COLOR,
                },
                "zaxis": {
                    "backgroundcolor": BACKGROUND_COLOR,
                    "gridcolor": GRID_COLOR,
                    "gridwidth": 2,
                    "linecolor": GRID_COLOR,
                    "showbackground": True,
                    "ticks": "",
                    "zerolinecolor": GRID_COLOR,
                },
            },
            "shapedefaults": {"line": {"color": LINE_COLOR}},
            "ternary": {
                "aaxis": {"gridcolor": GRID_COLOR, "linecolor": LINE_COLOR, "ticks": ""},
                "baxis": {"gridcolor": GRID_COLOR, "linecolor": LINE_COLOR, "ticks": ""},
                "bgcolor": BACKGROUND_COLOR,
                "caxis": {"gridcolor": GRID_COLOR, "linecolor": LINE_COLOR, "ticks": ""},
            },
            "title": {
                "font": {
                    "color": LINE_COLOR,
                    "family": TITLE_FONT,
                    "size": 14,
                },
                "xanchor": "center",
                "yanchor": "top",
            },
            "legend": {
                "title": {
                    "font": {
                        "color": LINE_COLOR,
                        "family": TITLE_FONT,
                        "size": 12,
                    }
                },
            },
            "margin": {"l": 0, "r": 0, "b": 0, "t": 20},
            "xaxis": {
                "automargin": True,
                "gridcolor": GRID_COLOR,
                "gridwidth": 1,
                "linecolor": LINE_COLOR,
                "rangeselector": {"font": {"size": 10}},
                "showline": True,
                "spikethickness": 1,
                "spikedash": "dot",
                "ticks": "outside",
                "tickson": "boundaries",
                "title": {"font": {"size": 10}, "standoff": 5},
                "zerolinecolor": GRID_COLOR,
                "zerolinewidth": 2,
            },
            "yaxis": {
                "automargin": True,
                "gridcolor": GRID_COLOR,
                "gridwidth": 1,
                "linecolor": LINE_COLOR,
                "showline": True,
                "ticks": "outside",
                "tickson": "boundaries",
                "title": {"font": {"size": 10}, "standoff": 5},
                "zerolinecolor": GRID_COLOR,
                "zerolinewidth": 2,
            },
        },
    }
)
