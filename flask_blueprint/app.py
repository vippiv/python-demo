from app import app
from exts import db
import config

app.config.from_object(config)
db.init_app(app)

if __name__ == "__main__":
    app.run()
