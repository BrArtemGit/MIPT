from flask import Flask, url_for, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/carousel")
def carousel():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                              <ol class="carousel-indicators">
                                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                              </ol>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img class="d-block w-100" src="static/img/mars1.jpeg" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/mars2.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/mars4.jpeg" alt="Third slide">
                                </div>
                              </div>
                              <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

