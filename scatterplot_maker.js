function makePlot() {

    try {

        // get input
        let xText = document.getElementById("x-values").value;
        let yText = document.getElementById("y-values").value;

        // string -> array
        let xValues = xText.split(",").map(Number);
        let yValues = yText.split(",").map(Number);

        // check lengths
        if (xValues.length !== yValues.length) {
            alert("X and Y must have same number of values.");
            return;
        }

        // check if number
        if (xValues.some(isNaN) || yValues.some(isNaN)) {
            alert("Please enter only numbers.");
            return;
        }

        // line of best fit
        const n = xValues.length;
        let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
        
        for (let i = 0; i < n; i++) {
            sumX += xValues[i];
            sumY += yValues[i];
            sumXY += xValues[i] * yValues[i];
            sumXX += xValues[i] * xValues[i];
        }

        // calculate slope and y-intercept
        const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;
        
        // generate y values of LOBF
        const bestFitY = xValues.map(val => (slope * val) + intercept);

        // create scatterplot
        let trace = {
            x: xValues,
            y: yValues,
            mode: "markers",
            type: "scatter",
            name: "Data Points",
            marker: {
                size: 12
            }
        };

        let traceBestFit = {
            x: xValues,
            y: bestFitY,
            mode: "lines",
            type: "scatter",
            name: "Best Fit",
            line: {
                color: "red",
                width: 2
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

        Plotly.newPlot("graph", [trace, traceBestFit], layout);

    }

    catch(error) {

        alert("Invalid input.");

        console.log(error);

    }

}
