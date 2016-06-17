from flask import Flask
app = Flask(__name__)

@app route('/')
def homepage():
    return """
    <h1> An app that views Youtube videos</h1>
    <i frame src= "https://www.youtube.com/watch?v=YQHsXMglC9A width=853" height="480" frameborder="0" allowfullscreen></iframe>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)