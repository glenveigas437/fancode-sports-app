from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from src.app import create_app, db
from src.config import config_dict

load_dotenv()

APP_ENV = os.getenv('ENV')

if APP_ENV == 'Development':
    APP_ENV = 'Debug'
else:
    APP_ENV = 'Testing'

app_config = config_dict[APP_ENV.capitalize()]

app = create_app(app_config)

Migrate(app, db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)