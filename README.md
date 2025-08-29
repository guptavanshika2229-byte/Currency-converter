# Currency-converter
function convertCurrency() {
    const amount = document.getElementById("amount").value;
    const baseCurrency = document.getElementById("base_currency").value;
    const targetCurrency = document.getElementById("target_currency").value;

    if (!amount) {
        alert("Please enter an amount");
        return;
    }

    fetch("/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            base_currency: baseCurrency,
            target_currency: targetCurrency,
            amount: amount
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.converted_amount) {
            document.getElementById("result").innerText = `Converted Amount: ${data.converted_amount.toFixed(2)} ${targetCurrency}`;
            fetchHistory();
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}

function fetchHistory() {
    fetch("/history")
    .then(response => response.json())
    .then(history => {
        const historyList = document.getElementById("history");
        historyList.innerHTML = "";
        history.forEach(entry => {
            const listItem = document.createElement("li");
            listItem.innerText = `${entry.amount} ${entry.base} → ${entry.converted.toFixed(2)} ${entry.target} (${entry.timestamp})`;
            historyList.appendChild(listItem);
        });
    })
    .catch(error => console.error("Error fetching history:", error));
}


document.addEventListener("DOMContentLoaded", fetchHistory);
