from flask import Flask

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.search
import controllers.personal
import controllers.scheme
import controllers.compare
