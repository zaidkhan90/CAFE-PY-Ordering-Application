let order = [];
let totalBill = 0;

function addItem(name, price) {
    order.push({ name, price });
    totalBill += price;
    updateOrderTable();
}

function removeItem(index) {
    totalBill -= order[index].price;
    order.splice(index, 1);
    updateOrderTable();
}

function clearOrder() {
    order = [];
    totalBill = 0;
    updateOrderTable();
}

function confirmOrder() {
    if (order.length === 0) {
        alert("Your cart is empty! Please add items before confirming.");
        return;
    }
    alert(`Order confirmed! Your total bill is $${totalBill}`);
}

function updateOrderTable() {
    let tableBody = document.getElementById("order-list");
    tableBody.innerHTML = "";

    order.forEach((item, index) => {
        let row = `<tr>
            <td>${item.name}</td>
            <td>$${item.price}</td>
            <td><button class="btn btn-danger btn-sm" onclick="removeItem(${index})">Remove</button></td>
        </tr>`;
        tableBody.innerHTML += row;
    });

    document.getElementById("total-bill").innerText = totalBill;
}

    .catch(error => console.error("Error:", error));
});
>>>>>>> b9d09bf0d2360c5c6168b7e7a3f207706dd0803f
