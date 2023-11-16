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
    console.log(response);
    // если запрос прошел нормально
    if (response.ok === true) {
        // получаем данные
        var data = await response.json();
        console.log(data);
    }

    var result = amount + " " + fromCurrency + " равно " + data["result"] + " " + toCurrency;

    document.getElementById("result").innerText = result;
}
