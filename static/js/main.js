var dataJson = [{
    key: "Cumulative Return",
    values: []
}];

d3.json('get-cities', function (error, data) {
    if (error) return console.warn(error);
    data.cities.map(function (d) {
        dataJson[0].values.push({"city": d.city, "population": d.pop});
    });
});

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart();
    chart.x(function(d) { return d.city; });
    chart.y(function(d) { return d.population; });
    chart.staggerLabels(true);
    chart.tooltips(false);
    chart.showValues(true);
    chart.duration(350);

    d3.select("#chart1 svg")
        .datum(dataJson)
        .call(chart);

    nv.utils.windowResize(chart.update);

    return chart;
});