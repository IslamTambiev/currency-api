async function convertCurrency() {
    var fromCurrency = document.getElementById("fromCurrency").value.toUpperCase();
    var toCurrency = document.getElementById("toCurrency").value.toUpperCase();
    var amount = document.getElementById("amount").value;

    // отправляет запрос и получаем ответ
    const response = await fetch("/currency/exchange/?" + new URLSearchParams({
        base: fromCurrency,
        quote: toCurrency,
        amount: amount,
    }),
        {
            method: "GET",
            credentials: "include",
            headers: { "Accept": "application/json" }
        });

    // JavaScript for displaying #result
    var resultDiv = document.getElementById("result");
    resultDiv.style.display = "block";

    // если запрос прошел нормально
    if (response.ok === true) {
        // получаем данные
        var data = await response.json();
        console.log(data);

        var result = amount + " " + fromCurrency + " равно " + data["result"] + " " + toCurrency;

        document.getElementById("result").innerText = result;
    }
    else if (response.status === 401) {
        var data = await response.json();
        console.log(data);
        document.getElementById("result").innerText = data.detail;

    }
    else{
        var data = await response.json();
        console.log(data);
        document.getElementById("result").innerText = data.message;
    }
}

async function loadCurrencies() {
    document.getElementById('loading').style.display = 'block';

    // Отправка запроса на API
    fetch("/currency/get_list/")
        .then(response => response.json())
        .then(data => {
        document.getElementById('loading').style.display = 'none';
        displayCurrencyList(data);
    })
        .catch(error => {
        document.getElementById('loading').style.display = 'none';
        console.error('Ошибка запроса:', error);
    });
}


function displayCurrencyList(data) {
    document.getElementById('loadCurrencies').style.display = 'none';
    var currencyListElement = document.getElementById('currency-list');

    var ul = document.createElement('ul');
    console.log(typeof data);
    for (var code in data) {
        var li = document.createElement('li');
        li.innerHTML = `<span>${code}</span> <span>${data[code]}</span>`;
        ul.appendChild(li);
    }

    currencyListElement.appendChild(ul);
}