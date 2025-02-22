<<<<<<< HEAD
document.getElementById("orderForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page refresh

    let item = document.getElementById("item").value;

    fetch("http://127.0.0.1:5000/order", {  // Connecting to backend
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ item: item })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("bill").innerText = `Total Bill: ₹${data.bill}`;
    })
    .catch(error => console.error("Error:", error));
});
=======
document.getElementById("orderForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page refresh

    let item = document.getElementById("item").value;

    fetch("http://127.0.0.1:5000/order", {  // Connecting to backend
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ item: item })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("bill").innerText = `Total Bill: ₹${data.bill}`;
    })
    .catch(error => console.error("Error:", error));
});
>>>>>>> b9d09bf0d2360c5c6168b7e7a3f207706dd0803f
