# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


# ###### Single endpoints
@app.route("/add")
def add_query():
    """Adds together a & b query parameters"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return str(operations.add(a, b))


@app.route("/sub")
def sub_query():
    """Subtracts a & b query parameters"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return str(operations.sub(a, b))


@app.route("/mult")
def mult_query():
    """Multiplies together a & b query parameters"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return str(operations.mult(a, b))


@app.route("/div")
def div_query():
    """Divides a & b query parameters"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return str(operations.div(a, b))


# ###### All in One Endpoint
OPERATIONS = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div,
}


@app.route("/math/<operation>")
def perform_math(operation):
    """Takes an operation and performs it on query params a & b"""

    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return str(OPERATIONS[operation](a, b))
