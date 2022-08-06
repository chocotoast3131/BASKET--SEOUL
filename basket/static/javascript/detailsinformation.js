//fetch('url')
//.then()은 서버와 통신 후 response 객체 return
function getTable(tab) {
    const category_code_map = {
        tab01: "#",
        tab02: "#",
        tab03: "#",
        tab04: "#",
        tab05: "#",
        tab06: "#",
        tab07: "#",
        tab08: "#",
        tab09: "#",
        tab10: "#",
        tab11: "#",
        tab12: "#",
        tab13: "#",
        tab14: "#",
        tab15: "#",
        tab16: "#",
        tab17: "#",
        tab18: "#",
        tab19: "#",
        tab20: "#",
        tab20: "#"
    };

    const paramsString =
        "name=" + category_code_map[tab];


    const searchParams = new URLSearchParams(paramsString);


    $.ajax("###", {
        type: "GET", // HTTP method type(GET, POST) 형식.
        data: searchParams.toString(), // Json 형식의 데이터.
        dataType: "json",
    }).done(function (json) {
        let items = json;

        let table_body = items
            .map(
                (item) => `<tr>
                            <td>${item.item_name}</td>
                            <td>${item.kind_name}</td>
                            <td>${item.unit}</td>
                            <td>${item.today}</td>
                            <td>${item.past_month}</td>
                            </tr>`
            )
            .reduce((prev, curr) => prev + curr);

        $("#table tbody").html(table_body);
    });
}