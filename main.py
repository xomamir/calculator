from flask import(Flask,render_template, request)

app: Flask= Flask(__name__)


@app.route("/")
def main():
    return render_template("calculator.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number_one = request.form["number_one"]
    number_two = request.form["number_two"]
    operation = request.form["operation"]

    if operation == "add":
        result = float(number_one) + float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "subtract":
        result = float(number_one) - float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "multiply":
        result = float(number_one) * float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "divide":
        result = float(number_one) / float(number_two)
        return render_template("calculator.html", result=result)

    else:
        return render_template("calculator.html")

if __name__== '__main__':
    app.run(
        port=8080,
        debug=True
    )