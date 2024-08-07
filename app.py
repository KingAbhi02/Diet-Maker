from flask import Flask, jsonify, request

app = Flask(__name__)

# Updated food options with measurements
food_options = {
    'breakfast': [
        {'name': 'Oats', 'calories': 389, 'measurement': 'grams'},
        {'name': 'Boiled Egg', 'calories': 155, 'measurement': 'number'},
        {'name': 'Chia Seeds', 'calories': 486, 'measurement': 'grams'},
        {'name': 'Flax Seeds', 'calories': 534, 'measurement': 'grams'},
        {'name': 'Multigrain Bread', 'calories': 69, 'measurement': 'slice'},
        {'name': 'Paneer', 'calories': 296, 'measurement': 'grams'},
        {'name': 'Smoothie', 'calories': 200, 'measurement': 'cup'},
        {'name': 'Banana Smoothie', 'calories': 120, 'measurement': 'cup'}
    ],
    'lunch': [
        {'name': 'Brown Rice', 'calories': 111, 'measurement': 'grams'},
        {'name': 'Mixed Vegetables', 'calories': 50, 'measurement': 'grams'},
        {'name': 'Quinoa', 'calories': 120, 'measurement': 'grams'},
        {'name': 'Moong Dal', 'calories': 347, 'measurement': 'grams'},
        {'name': 'Khichdi', 'calories': 150, 'measurement': 'cup'},
        {'name': 'Poha', 'calories': 150, 'measurement': 'cup'},
        {'name': 'Upma', 'calories': 200, 'measurement': 'cup'},
        {'name': 'Dalia', 'calories': 150, 'measurement': 'cup'}
    ],
    'snacks': [
        {'name': 'Almond', 'calories': 579, 'measurement': 'grams'},
        {'name': 'Roasted Makhana', 'calories': 348, 'measurement': 'grams'},
        {'name': 'Walnut', 'calories': 654, 'measurement': 'grams'},
        {'name': 'Cashew', 'calories': 553, 'measurement': 'grams'},
        {'name': 'Flax Seeds', 'calories': 534, 'measurement': 'grams'},
        {'name': 'Chia Seeds', 'calories': 486, 'measurement': 'grams'},
        {'name': 'Papaya Smoothie', 'calories': 100, 'measurement': 'cup'},
        {'name': 'Coconut Water', 'calories': 19, 'measurement': 'cup'}
    ],
    'dinner': [
        {'name': 'Chicken', 'calories': 239, 'measurement': 'grams'},
        {'name': 'Fish', 'calories': 206, 'measurement': 'grams'},
        {'name': 'Boiled Chana', 'calories': 164, 'measurement': 'grams'},
        {'name': 'Curd', 'calories': 98, 'measurement': 'cup'},
        {'name': 'Roti', 'calories': 71, 'measurement': 'number'},
        {'name': 'Tadka', 'calories': 60, 'measurement': 'tablespoon'},
        {'name': 'Buttermilk', 'calories': 40, 'measurement': 'cup'},
        {'name': 'Green Tea', 'calories': 2, 'measurement': 'cup'}
    ]
}

@app.route('/api/food-options', methods=['GET'])
def get_food_options():
    return jsonify(food_options)

@app.route('/api/calculate-bmr', methods=['POST'])
def calculate_bmr():
    data = request.json
    age = data['age']
    weight = data['weight']
    height = data['height']
    goal = data['goal']
    
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    if goal == 'weight-loss':
        bmr -= 300
    elif goal == 'weight-gain':
        bmr += 300

    return jsonify({'bmr': bmr})

if __name__ == '__main__':
    app.run(debug=True)
