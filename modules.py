from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ------------------ USER TABLE ------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Student / Faculty / HOD
    department = db.Column(db.String(50), nullable=False)

    vehicles = db.relationship("Vehicle", backref="owner", lazy=True)


# ------------------ VEHICLE TABLE ------------------
class Vehicle(db.Model):
    __tablename__ = "vehicles"

    vehicle_number = db.Column(db.String(20), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    vehicle_type = db.Column(db.String(10), nullable=False)  # Bike / Car

    parking_records = db.relationship("ParkingRecord", backref="vehicle", lazy=True)


# ------------------ PARKING SLOT TABLE ------------------
class ParkingSlot(db.Model):
    __tablename__ = "parking_slots"

    id = db.Column(db.Integer, primary_key=True)
    slot_type = db.Column(db.String(10), nullable=False)  # Bike / Car
    reserved_for = db.Column(db.String(20), nullable=False)  # HOD / Faculty / General
    status = db.Column(db.String(20), default="Available")

    parking_records = db.relationship("ParkingRecord", backref="slot", lazy=True)


# ------------------ PARKING RECORD TABLE ------------------
class ParkingRecord(db.Model):
    __tablename__ = "parking_records"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(
        db.String(20),
        db.ForeignKey("vehicles.vehicle_number"),
        nullable=False,
    )
    slot_id = db.Column(
        db.Integer,
        db.ForeignKey("parking_slots.id"),
        nullable=False,
    )
    entry_time = db.Column(db.DateTime, nullable=False)
    exit_time = db.Column(db.DateTime, nullable=True)