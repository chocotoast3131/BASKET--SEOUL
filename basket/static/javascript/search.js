$.ajax("http://127.0.0.1:8000/api/get/", {
    type: "GET", // HTTP method type(GET, POST) 형식.
    data: $("#formsearch"), // Json 형식의 데이터.
    dataType: "json",
}).done(function (json) {
    let items = json;

    let table_body = items
        .map(
            (item) => `<tr>
                    <td>${item.item_name}</td>
                    <td>${item.unit}</td>
                    <td>${item.past_month}</td>
                    <td>${item.today}</td>
                  </tr>`
        )
        .reduce((prev, curr) => prev + curr);

    $("#table tbody").html(table_body);
});