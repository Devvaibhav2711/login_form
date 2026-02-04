from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Registration Form Template
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
    <style>
        body {
            font-family: Arial;
            background: #f2f2f2;
            padding: 30px;
        }
        form {
            background: white;
            padding: 20px;
            width: 350px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
        }
        button {
            width: 100%;
            padding: 10px;
            background: green;
            color: white;
            border: none;
        }
        h2 {
            text-align: center;
        }
    </style>
</head>
<body>

<form method="POST">
    <h2>Registration Form</h2>

    <input type="text" name="username" placeholder="Enter Username" required>
    <input type="email" name="email" placeholder="Enter Email" required>
    <input type="password" name="password" placeholder="Enter Password" required>

    <button type="submit">Register</button>

    {% if message %}
        <p style="color:blue; text-align:center;">{{ message }}</p>
    {% endif %}
</form>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        message = f"User {username} registered successfully with email {email}!"

    return render_template_string(form_template, message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
