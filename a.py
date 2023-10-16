from flask import Flask, render_template

a = Flask(__name__)

@a.route("/")
def home():
    return render_template("index.html")

@a.route("/pr_1/")
def one():
    return render_template("1.html")

@a.route("/pr_2/")
def two():
    return render_template("2.html")

@a.route("/pr_3/")
def three():
    return render_template("3.html")

@a.route("/br/")
def br():
    return render_template("br.html")

@a.route("/pr_4/")
def four():
    return render_template("4.html")

@a.route("/pr_5/")
def five():
    return render_template("5.html")

@a.route("/pr_6/")
def six():
    return render_template("6.html")

@a.route("/pr_7/")
def seven():
    return render_template("7.html")

@a.route("/pr_8/")
def eight():
    return render_template("8.html")

@a.route("/pr_9/")
def nine():
    return render_template("9.html")

@a.route("/pr_10/")
def ten():
    return render_template("10.html")

@a.route("/pr_11/")
def eleven():
    return render_template("11.html")

@a.route("/pr_12/")
def twelve():
    return render_template("12.html")

@a.route("/purchased/")
def purchased():
    return render_template("purchased.html")

@a.route("/about/")
def ab():
    return render_template("about.html")

@a.route("/services/")
def serv():
    return render_template("services.html")

@a.route("/contact/")
def con():
    return render_template("contact.html")

if __name__ == '__main__':
    a.run(debug=True, port=5000)