//fetch('url')
//.then()은 서버와 통신 후 response 객체 return
$(function() {
    var urls = $(location).attr('pathname').split('/');
  
    $.ajax({
      url:"http://127.0.0.1:8000/api/price/" + urls[2] + "/" + urls[3],
      type: "GET", // HTTP method type(GET, POST) 형식.
      dataType: "json",
    }).done(function (json) {
      let items = json;
  
      let table_body = items
        .map(
          (item) => `<tr>
                      <td>${item.item_name}</td>
                      <td>${item.kind_name}</td>
                      <td>${item.day1}</td>
                      <td>${item.today}</td>
                      <td>${item.past_month}</td>
                    </tr>`
        )
        .reduce((prev, curr) => prev + curr);
  
      $("#table tbody").html(table_body);
    });
  });