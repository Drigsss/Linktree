from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Lista de links com nome e URL
    links = [
        {'name': 'Meu GitHub', 'url': 'https://github.com/Drigsss'},
        {'name': 'LinkedIn', 'url': 'https://www.linkedin.com/in/brayan-rodrigues-de-almeida-036171180/'},
        {'name': 'Youtube', 'url': 'https://www.youtube.com/@brayan_drigz'},
        {'name': 'Instagram', 'url': 'https://www.instagram.com/brayan.drigz/'}
    ]
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
