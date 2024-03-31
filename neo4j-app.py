from flask import Flask, request, render_template
from neo4j_operations import neo4j_conn

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form['text']
        neo4j_conn.create_sentence(user_input)
    return render_template('index.html', user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5052)
