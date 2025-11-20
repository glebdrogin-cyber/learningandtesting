from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-Memory-Liste für To-Dos
todos = []

@app.route('/')
def index():
    """Startseite – zeigt alle To-Dos an."""
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Route zum Hinzufügen eines neuen To-Dos."""
    if request.method == 'POST':
        task = request.form.get('task', '').strip()
        if task:
            todos.append(task)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)