from js import window

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
            "type": "scatter"
        }

        layout = {
            "title": "Scatterplot"
        }

        Plotly.newPlot("graph", [trace], layout)

    except Exception as e:
        print("ERROR:", e)


button = document.getElementById("plot-btn")
button.addEventListener("click", make_plot)