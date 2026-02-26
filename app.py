from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Vehicle, ParkingSlot, ParkingRecord
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


# ------------------ DASHBOARD ------------------
@app.route("/")
def dashboard():
    total_slots = ParkingSlot.query.count()
    available_slots = ParkingSlot.query.filter_by(status="Available").count()
    occupied_slots = ParkingSlot.query.filter_by(status="Occupied").count()
    active_vehicles = ParkingRecord.query.filter_by(exit_time=None).count()

    return render_template(
        "dashboard.html",
        total_slots=total_slots,
        available_slots=available_slots,
        occupied_slots=occupied_slots,
        active_vehicles=active_vehicles,
    )


# ------------------ VEHICLE ENTRY ------------------
@app.route("/entry", methods=["GET", "POST"])
def entry():
    if request.method == "POST":
        vehicle_number = request.form["vehicle_number"].upper()
        role = request.form["role"]

        # ROLE BASED SLOT ALLOCATION
        slot = ParkingSlot.query.filter_by(
            status="Available",
            reserved_for=role
        ).first()

        # If no reserved slot available, fallback to General
        if not slot:
            slot = ParkingSlot.query.filter_by(
                status="Available",
                reserved_for="General"
            ).first()

        if slot:
            slot.status = "Occupied"

            new_record = ParkingRecord(
                vehicle_number=vehicle_number,
                slot_id=slot.id,
                entry_time=datetime.now(),
            )

            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for("dashboard"))
        else:
            return "No Slots Available"

    return render_template("entry.html")


# ------------------ VEHICLE EXIT ------------------
@app.route("/exit", methods=["GET", "POST"])
def exit_vehicle():
    if request.method == "POST":
        vehicle_number = request.form["vehicle_number"].upper()

        record = ParkingRecord.query.filter_by(
            vehicle_number=vehicle_number,
            exit_time=None
        ).first()

        if record:
            record.exit_time = datetime.now()

            slot = ParkingSlot.query.get(record.slot_id)
            slot.status = "Available"

            db.session.commit()

            return redirect(url_for("dashboard"))
        else:
            return "Vehicle Not Found or Already Exited"

    return render_template("exit.html")


# ------------------ PARKING HISTORY ------------------
@app.route("/history")
def history():
    records = ParkingRecord.query.order_by(
        ParkingRecord.entry_time.desc()
    ).all()

    return render_template("history.html", records=records)


if __name__ == "__main__":
    app.run(debug=True)