from js import document, Plotly, Object, Array
from pyodide.ffi import create_proxy

# Keep proxy alive globally
plot_proxy = None


def make_plot(event):

    x_text = document.getElementById("x-values").value
    y_text = document.getElementById("y-values").value

    try:
        x_values = [float(x.strip()) for x in x_text.split(",")]
        y_values = [float(y.strip()) for y in y_text.split(",")]

        if len(x_values) != len(y_values):
            print("X and Y lengths must match")
            return

        # Create REAL JS objects manually
        trace = Object.fromEntries(Array.new([
            ["x", x_values],
            ["y", y_values],
            ["mode", "markers"],
            ["type", "scatter"]
        ]))

        layout = Object.fromEntries(Array.new([
            ["title", "Scatterplot"]
        ]))

        data = Array.new()
        data.push(trace)

        Plotly.newPlot("graph", data, layout)

    except Exception as e:
        print("ERROR:", e)


button = document.getElementById("plot-btn")

plot_proxy = create_proxy(make_plot)

button.addEventListener("click", plot_proxy)
