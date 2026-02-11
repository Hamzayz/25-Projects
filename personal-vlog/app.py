from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this!

# Configuration
ARTICLES_DIR = 'articles'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password123'  # Change this!

# Ensure articles directory exists
if not os.path.exists(ARTICLES_DIR):
    os.makedirs(ARTICLES_DIR)

# Helper Functions
def get_all_articles():
    """Get all articles from the filesystem"""
    articles = []
    if os.path.exists(ARTICLES_DIR):
        for filename in os.listdir(ARTICLES_DIR):
            if filename.endswith('.json'):
                with open(os.path.join(ARTICLES_DIR, filename), 'r') as f:
                    article = json.load(f)
                    article['id'] = filename.replace('.json', '')
                    articles.append(article)
    # Sort by date (newest first)
    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles

def get_article_by_id(article_id):
    """Get a specific article by ID"""
    filepath = os.path.join(ARTICLES_DIR, f"{article_id}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            article = json.load(f)
            article['id'] = article_id
            return article
    return None

def save_article(article_id, title, content, date):
    """Save an article to the filesystem"""
    article = {
        'title': title,
        'content': content,
        'date': date
    }
    filepath = os.path.join(ARTICLES_DIR, f"{article_id}.json")
    with open(filepath, 'w') as f:
        json.dump(article, f, indent=2)

def delete_article(article_id):
    """Delete an article from the filesystem"""
    filepath = os.path.join(ARTICLES_DIR, f"{article_id}.json")
    if os.path.exists(filepath):
        os.remove(filepath)

def generate_article_id(title):
    """Generate a unique ID from title"""
    # Create a simple ID from title
    base_id = title.lower().replace(' ', '-')
    # Remove special characters
    base_id = ''.join(c for c in base_id if c.isalnum() or c == '-')
    
    # Check if ID exists, if so, add a number
    counter = 1
    article_id = base_id
    while os.path.exists(os.path.join(ARTICLES_DIR, f"{article_id}.json")):
        article_id = f"{base_id}-{counter}"
        counter += 1
    
    return article_id

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes - Guest Section
@app.route('/')
def home():
    """Home page showing all published articles"""
    articles = get_all_articles()
    return render_template('home.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    """Individual article page"""
    article = get_article_by_id(article_id)
    if article:
        return render_template('article.html', article=article)
    return "Article not found", 404

# Routes - Admin Section
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page for admin"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout admin"""
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    """Admin dashboard showing all articles with edit/delete options"""
    articles = get_all_articles()
    return render_template('admin.html', articles=articles)

@app.route('/admin/new', methods=['GET', 'POST'])
@login_required
def new_article():
    """Create a new article"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        date = request.form.get('date')
        
        if title and content and date:
            article_id = generate_article_id(title)
            save_article(article_id, title, content, date)
            return redirect(url_for('admin'))
    
    # Default date to today
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('new_article.html', today=today)

@app.route('/admin/edit/<article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    """Edit an existing article"""
    article = get_article_by_id(article_id)
    
    if not article:
        return "Article not found", 404
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        date = request.form.get('date')
        
        if title and content and date:
            save_article(article_id, title, content, date)
            return redirect(url_for('admin'))
    
    return render_template('edit_article.html', article=article)

@app.route('/admin/delete/<article_id>', methods=['POST'])
@login_required
def delete_article_route(article_id):
    """Delete an article"""
    delete_article(article_id)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)