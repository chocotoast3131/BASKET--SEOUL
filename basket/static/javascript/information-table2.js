//fetch('url')
    //.then()은 서버와 통신 후 response 객체 return
    fetch('conbox', {
  method: 'POST',
  body: JSON.stringify({
    id:'품목',
    unit:'단위',
    price:'현재가',
    lastmonth:'전월가',
    variable:'변동가',
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
.then(function(res){
  res.json().then(function(json){
  	console.log(json);
    })
})