from js import window
from pyodide.ffi import create_proxy, to_js

document = window.document
Plotly = window.Plotly


def make_plot(event):

    try:
        x_text = document.getElementById("x-values").value
        y_text = document.getElementById("y-values").value

        x_values = [float(x.strip()) for x in x_text.split(",")]
        y_values = [float(y.strip()) for y in y_text.split(",")]

        if len(x_values) != len(y_values):
            print("Lengths must match")
            return

        trace = {
            "x": x_values,
            "y": y_values,
            "mode": "markers",
            "type": "scatter",
            "marker": {"size": 10}
        }

        layout = {
            "title": "Scatterplot",
            "xaxis": {"title": "X Values"},
            "yaxis": {"title": "Y Values"}
        }

        Plotly.newPlot(
            "graph",
            to_js([trace]),
            to_js(layout)
        )

    except Exception as e:
        print("ERROR:", e)


button = document.getElementById("plot-btn")

proxy = create_proxy(make_plot)

button.addEventListener("click", proxy)
