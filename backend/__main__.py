from .app import app
from . import config
from .models import db
from .scheduler import start_scheduler
app.config.from_object(config.Config)
db.init_app(app)
with app.app_context():
    db.create_all()
start_scheduler(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
