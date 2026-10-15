from flask import Flask

from controllers import produtos_bp

app = Flask(__name__, template_folder='views')

app.register_blueprint(produtos_bp)

app.run(debug=True)