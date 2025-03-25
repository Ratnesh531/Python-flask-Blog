from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Define Database Model
class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.description}"

# Initialize the database
with app.app_context():
    db.create_all()

# Root Route
@app.route('/')
def root():
    return "We are in root, Welcome Back!!"

# Function to populate the database
def populate_db():
    sample_data = [
        {"name": "Coke", "description": "Refreshing cola drink"},
        {"name": "Pepsi", "description": "Popular carbonated drink"},
        {"name": "Lemonade", "description": "Fresh lemon juice with sugar"},
        {"name": "Iced Tea", "description": "Chilled tea with lemon flavor"},
        {"name": "Orange Juice", "description": "Freshly squeezed orange juice"}
    ]

    for drink in sample_data:
        if not Drinks.query.filter_by(name=drink['name']).first():
            new_drink = Drinks(name=drink['name'], description=drink['description'])
            db.session.add(new_drink)

    db.session.commit()

# Drinks Route
@app.route('/drinks')
def get_drinks():
    drinks_list = Drinks.query.all()
    output = []

    for drink in drinks_list:
        drinks_list = Drinks.query.all()
    output = [{"id": drink.id, "name": drink.name, "description": drink.description} for drink in drinks_list]
    return jsonify(output), 200, {'Content-Type': 'application/json; charset=utf-8'}

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        populate_db()    # Populate with sample data
    app.run(debug=True)