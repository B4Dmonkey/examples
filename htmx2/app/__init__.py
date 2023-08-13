from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app.config["TEMPLATES_AUTO_RELOAD"] = True

    @app.route('/')
    def home(request):
        return render_template("index.html")

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
