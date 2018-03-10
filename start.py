import packages.py
app = Flask(__name__)
@app.route('/')
def index():
    return 'this is the starting page'
@app.route("/start")
def start():
    return "the kings rise again -- you ride to save your republic!"
