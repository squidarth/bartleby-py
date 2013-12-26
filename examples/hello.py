import sys
from flask import Flask
import bartleby

class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

app = Flask(__name__)
app.debug = True

# This is how i get Tracer() in.
@app.before_request
def before_request():
  bartleby.Bartleby(["hello.py"])

@app.route("/")
def hello():
  x = 2
  bob = x
  alice = "Alice"
  plus = "+"
  hungry = False
  mydict = {"age": 23, "monkey": "babboon"} 
  coord = Coordinate(23, 12)
  plus = None
  return "Hello world joe %d" % coord.x

if __name__ == "__main__":
  app.run()
