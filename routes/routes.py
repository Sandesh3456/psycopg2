from flask import Flask,
import flask


app= Flask(
    __name__,
    static_url_path="",
    template_folder="../UI/templates/",
    static_folder = "../UI/static/",
    )

app.secret_key="duw283rgdwq"

