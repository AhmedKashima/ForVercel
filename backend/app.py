# import os

# from base import api, socketio

# app = api


# @app.get("/")
# def health_check():
#     return {
#         "status": "ok",
#         "message": "Graduation backend is running"
#     }, 200


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))

#     socketio.run(
#         app,
#         host="0.0.0.0",
#         port=port,
#         debug=False,
#         allow_unsafe_werkzeug=True
#     )


import os

from base import api, socketio, bcrypt
from models import db, Employees

app = api


def seed_demo_admin():
    admin_email = "admin@demo.com"
    admin_password = "Admin12345"

    with app.app_context():
        db.create_all()

        admin = Employees.query.filter_by(Email=admin_email).first()

        if admin is None:
            admin = Employees(
                Employeeid=1,
                Email=admin_email,
                Password=bcrypt.generate_password_hash(admin_password).decode("utf-8"),
                FirstName="Ahmed",
                LastName="Admin",
                PhoneNumber="+70000000000",
                Admin=True,
                DateHired="2026-05-06"
            )
            db.session.add(admin)
            db.session.commit()
        else:
            admin.Admin = True
            db.session.commit()


seed_demo_admin()


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Graduation backend is running"
    }, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    socketio.run(
        app,
        host="0.0.0.0",
        port=port,
        debug=False,
        allow_unsafe_werkzeug=True
    )