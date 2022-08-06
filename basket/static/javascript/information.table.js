//fetch('url')
//.then()은 서버와 통신 후 response 객체 return
function getTable(tab) {
  const category_code_map = {
    tab01: "과일",
    tab02: "채소",
    tab03: "쌀/잡곡",
    tab04: "수산물",
  };

  const paramsString =
    "name="+category_code_map[tab];


  const searchParams = new URLSearchParams(paramsString);


  $.ajax("http://127.0.0.1:8000/api/price/", {
    type: "GET", // HTTP method type(GET, POST) 형식.
    data: searchParams.toString(), // Json 형식의 데이터.
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
}

