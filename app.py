from flask import Flask, render_template, redirect, url_for
from models import db, Pet
from forms import PetForm

app = Flask(__name__)

# Configuration for SQLAlchemy and the secret key for forms
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db.init_app(app)

# Home route to display the form and list of pets
@app.route('/', methods=['GET', 'POST'])
def index():
    form = PetForm()
    if form.validate_on_submit():
        # Add new pet to the database
        pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('index'))
    
    # Retrieve all pets to display
    pets = Pet.query.all()
    return render_template('view_pets.html', form=form, pets=pets)

if __name__ == '__main__':
    app.run(debug=True)
