document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.getElementById('ipo-table-body');

    // Function to fetch IPO data
    async function fetchIPOData() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/data/'); // Ensure the endpoint matches the URL pattern
            if (!response.ok) {
                console.error('Failed to fetch IPO data:', response.statusText);
                return;
            }
            const data = await response.json();
            updateTable(data);
        } catch (error) {
            console.error('Error fetching IPO data:', error);
        }
    }

    // Function to update the table with fetched data
    function updateTable(data) {
        tableBody.innerHTML = ''; // Clear the existing rows
        data.forEach(ipo => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${ipo.company_name}</td>
                <td>${ipo.ipo_date}</td>
                <td>${ipo.price}</td>
            `;
            tableBody.appendChild(row);
        });
    }

    // Fetch IPO data
    fetchIPOData();
    setInterval(fetchIPOData, 5000); // Auto-refresh every 5 seconds
});
