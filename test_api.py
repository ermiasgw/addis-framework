
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
    