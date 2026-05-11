import click
from flask.cli import with_appcontext
from base import api, bcrypt
from models import db, Employees

@click.group()
def cli():
    pass

@click.command(name="seed_admin")
@with_appcontext
def seed_admin():
    """Seeds the database with a default admin user."""
    ADMIN_ID = 1
    ADMIN_EMAIL = "admin@demo.com"
    ADMIN_PASSWORD = "Admin12345"
    ADMIN_FIRST_NAME = "Ahmed"
    ADMIN_LAST_NAME = "Admin"
    ADMIN_PHONE = 70000000000
    ADMIN_DATE_HIRED = "2026-05-06"

    db.create_all()

    admin = Employees.query.filter_by(Email=ADMIN_EMAIL).first()

    if admin is None:
        hashed_password = bcrypt.generate_password_hash(ADMIN_PASSWORD).decode("utf-8")

        admin = Employees(
            Employeeid=ADMIN_ID,
            Email=ADMIN_EMAIL,
            Password=hashed_password,
            FirstName=ADMIN_FIRST_NAME,
            LastName=ADMIN_LAST_NAME,
            PhoneNumber=ADMIN_PHONE,
            Admin=True,
            DateHired=ADMIN_DATE_HIRED
        )

        db.session.add(admin)
        db.session.commit()
        print("Admin user created")
    else:
        admin.Password = bcrypt.generate_password_hash(ADMIN_PASSWORD).decode("utf-8")
        admin.Admin = True
        db.session.commit()
        print("Admin user already existed, password reset and admin enabled")

    print("Email:", ADMIN_EMAIL)
    print("Password:", ADMIN_PASSWORD)

@click.command(name="seed_user")
@with_appcontext
def seed_user():
    """Seeds the database with a default regular user."""
    USER_EMAIL = "worker@demo.com"
    USER_PASSWORD = "Worker12345"
    USER_FIRST_NAME = "Worker"
    USER_LAST_NAME = "Demo"
    USER_PHONE = 70000000000
    USER_DATE_HIRED = "2026-05-11"

    db.create_all()

    user = Employees.query.filter_by(Email=USER_EMAIL).first()

    if user is None:
        hashed_password = bcrypt.generate_password_hash(USER_PASSWORD).decode("utf-8")

        user = Employees(
            Email=USER_EMAIL,
            Password=hashed_password,
            FirstName=USER_FIRST_NAME,
            LastName=USER_LAST_NAME,
            PhoneNumber=USER_PHONE,
            Admin=False,
            DateHired=USER_DATE_HIRED
        )

        db.session.add(user)
        db.session.commit()
        print("User created")
    else:
        user.Password = bcrypt.generate_password_hash(USER_PASSWORD).decode("utf-8")
        user.Admin = False
        db.session.commit()
        print("User already existed, password reset")

    print("Email:", USER_EMAIL)
    print("Password:", USER_PASSWORD)

@click.command(name="seed_all")
@with_appcontext
def seed_all():
    """Runs all seeding commands."""
    seed_admin()
    seed_user()

cli.add_command(seed_admin)
cli.add_command(seed_user)
cli.add_command(seed_all)

if __name__ == "__main__":
    cli()
