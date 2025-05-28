import os
from flask import Flask
from flask_session import Session
from flask_cors import CORS
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "super-secret-key")

# ✅ Configure session storage
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_FILE_DIR'] = os.path.join(app.root_path, 'flask_session')
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # ✅ Optional: Helps with browser session issues
app.config['SESSION_COOKIE_SECURE'] = False    # ✅ For localhost only

# ✅ Enable session and CORS
Session(app)
CORS(app, supports_credentials=True)

# ✅ Allow OAuth without HTTPS in local dev
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# ✅ Optional: Load additional config if exists
if os.path.exists("config.py"):
    app.config.from_pyfile("config.py")

# ✅ Optional DB init
try:
    from database.db_setup import init_db
    init_db()
    print("✅ Database initialized")
except Exception as e:
    print("⚠️ Skipped DB init:", e)

# ✅ Register Blueprints
from routes.auth import auth_blueprint
from routes.oauth import oauth_blueprint
from routes.analyze import analyze_blueprint
from routes.brands import brands_blueprint
from routes.influencers import influencer_bp

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(oauth_blueprint, url_prefix="/oauth")
app.register_blueprint(analyze_blueprint, url_prefix="/analyze")
app.register_blueprint(brands_blueprint, url_prefix="/brands")
app.register_blueprint(influencer_bp)  # No prefix to keep routes like /influencers/api

# ✅ Health check route
@app.route("/")
def index():
    return "✅ Flask server running with Auth, OAuth, Analyze, Brands, and Influencers routes!"

# ✅ Start the Flask server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
