let mychartOne = document.getElementById("myChartOne").getContext("2d");

let item = location.pathname.split("/")[3];

$.ajax(`/api/price/${item}`, {
  type: "GET",
  dataType: "json",
}).done(function (json) {
  let lineChart = new Chart(myChartOne, {
    type: "line",
    data: {
      labels: json.dates,
      datasets: json.graphs.map((graph, graph_ix) => {
        return {
          label: graph.label,
          data: graph.prices,
          borderColor: Utils.color(graph_ix), // 9번까지
        };
      }),
    },
  });
});

let json = {
  dates: [날짜정보],
  graphs: [
    { label: "품종명", prices: [날짜별가격] },
    { label: "품종명", prices: [날짜별가격] },
    { label: "품종명", prices: [날짜별가격] },
    { label: "품종명", prices: [날짜별가격] },
  ],
};
