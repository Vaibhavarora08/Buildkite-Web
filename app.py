from flask import Flask   # Flask is a library - like importing any Python module
                          # It gives you tools to handle web requests

app = Flask(__name__)     # Creates your web app. __name__ is just Python telling
                          # Flask "this file is the main one"

# This is a "route" - like a URL rule
# When someone visits localhost:5000/  the hello() function runs
@app.route("/")
def hello():
    return "<h1>Hello from Buildkite!</h1><p>Deployed successfully.</p>"

# Another route - localhost:5000/health
# Used by pipelines to check "is the app alive?"
@app.route("/health")
def health():
    return {"status": "ok", "message": "App is running"}  # returns JSON

# Another route with a variable in the URL
# localhost:5000/greet/Vaibhav  → shows "Hello Vaibhav!"
@app.route("/greet/<name>")
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    # debug=True means Flask auto-restarts when you change code
    # host="0.0.0.0" means accessible from your whole network not just localhost
    app.run(debug=True, host="0.0.0.0", port=5000)