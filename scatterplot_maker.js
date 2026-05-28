function makePlot() {

    try {

        // Get input values
        let xText = document.getElementById("x-values").value;
        let yText = document.getElementById("y-values").value;

        // Convert strings into arrays
        let xValues = xText.split(",").map(Number);
        let yValues = yText.split(",").map(Number);

        // Check lengths
        if (xValues.length !== yValues.length) {
            alert("X and Y must have same number of values.");
            return;
        }

        // Create scatterplot
        let trace = {
            x: xValues,
            y: yValues,

            mode: "markers",

            type: "scatter",

            marker: {
                size: 12
            }
        };

        let layout = {
            title: "Scatterplot",

            xaxis: {
                title: "X Values"
            },

            yaxis: {
                title: "Y Values"
            }
        };

        Plotly.newPlot("graph", [trace], layout);

    }

    catch(error) {

        alert("Invalid input.");

        console.log(error);

    }

}
