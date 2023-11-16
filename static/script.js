function convertCurrency() {
    var fromCurrency = document.getElementById("fromCurrency").value.toUpperCase();
    var toCurrency = document.getElementById("toCurrency").value.toUpperCase();
    var amount = document.getElementById("amount").value;

    // Здесь можно добавить код для отправки запроса на сервер и получения результата
    // Например, с использованием AJAX или Fetch API

    // Вместо следующей строки, вы можете добавить код для отправки запроса на сервер
    var result = amount + " " + fromCurrency + " равно " + (amount * Math.random()).toFixed(2) + " " + toCurrency;

    document.getElementById("result").innerText = result;
}
