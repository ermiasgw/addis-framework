
from conftest import api, client
import inspect
def test_basic_route(api):
    @api.route("/home")
    def home(req, resp):
        resp.text = "YOLO"

def test_baic_route(api):
    @api.route("/home")
    def home2(req, resp):
        resp.text = "YOLO"
    
def test_bumbo_test_client_can_send_requests(api, client):
    RESPONSE_TEXT = "THIS IS COOL"

    @api.route("/hey")
    def cool(req, resp):
        resp.text = RESPONSE_TEXT

    #assert client.get("http://testserver/hey").text == RESPONSE_TEXT

def test_parameterized_route(api, client):
    @api.route("/{name}")
    def hello(req, resp, name):
        resp.text = f"hey {name}"

    assert client.get("http://testserver/matthew").text == "hey matthew"
    assert client.get("http://testserver/ashley").text == "hey ashley"

def test_default_404_response(client):
    response = client.get("http://testserver/doesnotexist")

    assert response.status_code == 404
    assert response.text == "Not found."