from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_db
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True, nullable=False)
  password_hash = db.Column(db.String(60), nullable=False)

  def set_password(self, password):
      self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

  def check_password(self, password):
      return bcrypt.check_password_hash(self.password_hash, password)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      confirm_password = request.form['confirm_password']

      if password != confirm_password:
          flash('Passwords do not match.', 'error')
          return redirect(url_for('signup'))

      existing_user = User.query.filter_by(username=username).first()
      if existing_user:
          flash('Username already exists. Please choose a different one.', 'error')
          return redirect(url_for('signup'))

      new_user = User(username=username)
      new_user.set_password(password)
      db.session.add(new_user)
      db.session.commit()

      flash('Account created successfully. Please log in.', 'success')
      return redirect(url_for('login'))

  return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      user = User.query.filter_by(username=username).first()

      if user and user.check_password(password):
          flash('Login successful!', 'success')
          # You can add the logic to redirect the user to their profile or another page after login
          return redirect(url_for('index'))
      else:
          flash('Invalid username or password. Please try again.', 'error')

  return render_template('login.html')

if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)
