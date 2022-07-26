let listObj = {
    con1: [
        {
            "id": "사과",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "배",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
        {
            "id": "참외",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
        {
            "id": "수박",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": false
        }
    ],
    con2: [
        {
            "id": "감자",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "고구마",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "당근",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "대파",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "당근",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "마늘",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "무",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "상추",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "양파",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "오이",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "콩나물",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
    ],
    con3: [
        {
            "id": "백미",
            "unit": "20kg/포",
            "price": "63,800",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "보리쌀",
            "unit": "1kg/포",
            "price": "3,490",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "찹쌀",
            "unit": "1kg/포",
            "price": "5,990",
            "lastmonth": "01-100-1001",
            "variable": true
        },
    ],
    con4: [
        {
            "id": "고등어",
            "unit": "",
            "price": "",
            "lastmonth": "01-100-1001",
            "variable": true
        },
        {
            "id": "갈치",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
        {
            "id": "오징어",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
        {
            "id": "조기",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
        {
            "id": "바지락",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
        {
            "id": "동태",
            "unit": "",
            "price": "",
            "lastmonth": "",
            "variable": true
        },
    ],
}

function getTableData(type) {
    let title = {
        "id": "품목",
        "unit": "단위",
        "price": "현재가격",
        "lastmonth": "전월비",
        "variable": "변동가"
    }

    let $table = document.createElement('table');
    let $thead = document.createElement('thead');
    let $tr = document.createElement('tr');

    for (let i in title) {
        let $th = document.createElement('th');
        $th.innerHTML = title[i];
        $tr.appendChild($th);
    }

    $thead.appendChild($tr);
    $table.appendChild($thead);

    listObj[type].map(obj => {
        let $tbody = document.createElement('tbody');
        let $tr = document.createElement('tr');
        for (let i in obj) {
            let $td = document.createElement('td');
            $td.innerHTML = obj[i];
            $tr.appendChild($td);
        }
        $tbody.appendChild($tr);
        $table.appendChild($tbody);
    })
    
    document.querySelector(`.${type}`).innerHTML = "";
    document.querySelector(`.${type}`).appendChild($table);
}

window.onload = function () {
    getTableData("con1");
    getTableData("con2");
    getTableData("con3");
    getTableData("con4");
}