from webapp import db
from webapp import create_app

app = create_app()
with app.app_context():
    db.create_all()

    
