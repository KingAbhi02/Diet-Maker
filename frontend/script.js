async function fetchFoodOptions() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/food-options');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        displayFoodOptions(data);
    } catch (error) {
        console.error("Error fetching food options:", error);
    }
}

function displayFoodOptions(foodOptions) {
    const categories = ['breakfast', 'lunch', 'snacks', 'dinner'];
    const foodOptionsDiv = document.getElementById('foodOptions');

    categories.forEach(category => {
        const categoryDiv = document.createElement('div');
        const categoryHeader = document.createElement('h3');
        categoryHeader.textContent = category.charAt(0).toUpperCase() + category.slice(1);
        categoryDiv.appendChild(categoryHeader);

        foodOptions[category].forEach(food => {
            const foodDiv = document.createElement('div');
            foodDiv.innerHTML = `
                <label>${food.name} (${food.measurement}):</label>
                <input type="number" id="${category}-${food.name}" placeholder="Quantity">
                <button onclick="selectFood('${category}', '${food.name}', '${food.measurement}', ${food.calories})">Add</button>
            `;
            categoryDiv.appendChild(foodDiv);
        });

        foodOptionsDiv.appendChild(categoryDiv);
    });
}

function selectFood(category, name, measurement, calories) {
    const quantity = document.getElementById(`${category}-${name}`).value;
    if (quantity) {
        const selectedFoodsDiv = document.getElementById(`${category}Foods`);
        const foodDiv = document.createElement('div');
        foodDiv.textContent = `${name} x${quantity} (${measurement}) - ${calories * quantity} calories`;
        selectedFoodsDiv.appendChild(foodDiv);

        updateTotalCalories();
    }
}

function calculateCalories() {
    const age = document.getElementById('age').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const goal = document.getElementById('goal').value;

    if (age && weight && height) {
        const bmr = 10 * weight + 6.25 * height - 5 * age + 5;
        let caloriesRequired = bmr;
        if (goal === 'weight-loss') caloriesRequired -= 300;
        if (goal === 'weight-gain') caloriesRequired += 300;

        document.getElementById('caloriesRequired').textContent = `Calories Required: ${caloriesRequired}`;
    }
}

function updateTotalCalories() {
    const categories = ['breakfast', 'lunch', 'snacks', 'dinner'];
    categories.forEach(category => {
        const selectedFoodsDiv = document.getElementById(`${category}Foods`);
        let totalCalories = 0;
        selectedFoodsDiv.querySelectorAll('div').forEach(item => {
            const caloriesText = item.textContent.split('-')[1];
            if (caloriesText) {
                totalCalories += parseInt(caloriesText.replace(' calories', ''));
            }
        });
        selectedFoodsDiv.insertAdjacentHTML('beforeend', `<p>Total Calories: ${totalCalories}</p>`);
    });
}

fetchFoodOptions();
