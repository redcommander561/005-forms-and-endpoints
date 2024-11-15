from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/question",methods=["POST"])
def endpoint():
    data = request.form
    print(data)
    output = f"""
<!doctyle html>
<head>
  <title> Form Result </title>
  <style>
    .result {{
        color: blue;
        font-size: 2em;
    }}
  </style
</head>
<body>
  <div class='result'>hello, {data['fname']}!</div>
  You have successfully sent data to a form!
</body>
    """
    return output
    pass

@app.route("/", methods=["POST"] )
def anotherFunction():
    pass

app.run(port=5000)