document.addEventListener("DOMContentLoaded", () => {
    loadProducts();
});

function loadProducts() {
    fetch("static/products.json") // JSON 파일 불러오기
        .then((response) => response.json())
        .then((data) => {
            const productTable = document.getElementById("product_data_Table");
            productTable.innerHTML = ""; // 기존 데이터 초기화

            data.forEach((item) => {
                const row = productTable.insertRow();
                row.insertCell(0).innerHTML = item.category;
                row.insertCell(1).innerHTML = item.brand;
                row.insertCell(2).innerHTML = item.product;
                row.insertCell(3).innerHTML = item.price;
            });
        })
        .catch((error) => {
            console.error("❌ 데이터 로드 실패:", error);
        });
}