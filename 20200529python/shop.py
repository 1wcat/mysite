from flask import Flask, session, render_template, redirect, request, g

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'bob': {
        'uid': 'bob',
        'password': 'abcde',
        'name': 'bob',
        'email': 'test@test.com'
    }
}

def get_user():
  user_id = session.get('user_id')
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'uid': None, 'name': 'Guest' }

@app.route('/')
def index():
    get_user()
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    counter = session['counter']
        
    counter_msg =  'Counter is %d' % counter
    return render_template('home.html', counter_msg=counter_msg, user=g.user)

@app.route('/login', methods=['GET', 'POST'])
def login():
  # 如果已登入 (session['user_id'] 有資料) redirect ...
  if session.get('user_id'):
      return redirect('/')

  if request.method == 'POST':
      uid = request.form.get('uid')
      password = request.form.get('password')
      if not uid or not password:
          return 'login invalid inputs'
    
      user = users_db.get(uid)
      if not user:
          return 'user not found'

      if user['password'] != password:
          return 'invalid password'
    
      session['user_id'] = uid
      return redirect('/')

  return render_template('login.html')

@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if session.get('user_id'):
      return redirect('/')

  if request.method == 'POST':
      uid = request.form.get('uid')
      password = request.form.get('password')
      name = request.form.get('name')
      email = request.form.get('email')
      if not uid or not password or not name or not email:
          return 'invalid inputs'
    
      user = users_db.get(uid)
      if user:
          return 'username already in use'

      users_db[uid] = {
          'uid' : uid,
          'password' : password,
          'name' : name,
          'email' : email
      }
      session['user_id'] = uid
      return redirect('/')

  return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')