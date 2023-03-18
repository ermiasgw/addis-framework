from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"

@app.route("/book")
class BooksHandler:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"

def handler(req, resp):
    resp.text = "YOLO"


def handler2(req, resp):
    resp.text = "YOLO2"

api.add_route("/home", handler)
api.add_route("/about", handler2)