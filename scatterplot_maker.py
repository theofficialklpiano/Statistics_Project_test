from js import document, Plotly, Array, Object
from pyodide.ffi import create_proxy

proxy = None


def make_plot(event):

    try:
        x_text = document.getElementById("x-values").value
        y_text = document.getElementById("y-values").value

        x_py = [float(x.strip()) for x in x_text.split(",")]
        y_py = [float(y.strip()) for y in y_text.split(",")]

        if len(x_py) != len(y_py):
            print("Lengths must match")
            return

        # Convert Python lists -> REAL JS arrays
        x_js = Array.new()
        y_js = Array.new()

        for v in x_py:
            x_js.push(v)

        for v in y_py:
            y_js.push(v)

        # Create REAL JS trace object
        trace = Object.new()

        trace.x = x_js
        trace.y = y_js
        trace.mode = "markers"
        trace.type = "scatter"

        # JS array containing trace
        data = Array.new()
        data.push(trace)

        # REAL JS layout object
        layout = Object.new()
        layout.title = "Scatterplot"

        Plotly.newPlot("graph", data, layout)

    except Exception as e:
        print("ERROR:", e)


button = document.getElementById("plot-btn")

proxy = create_proxy(make_plot)

button.addEventListener("click", proxy)
