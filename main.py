import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get("https://api.npoint.io/7c616e690b3c7d9c8027").json()


@app.route('/index.html')
@app.route('/')
def get_all_posts():
    return render_template("index.html", post_data=response)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
