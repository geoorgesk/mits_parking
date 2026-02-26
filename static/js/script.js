// ===== AUTO UPPERCASE VEHICLE NUMBER =====
document.addEventListener("DOMContentLoaded", function () {
    const vehicleInputs = document.querySelectorAll("input[name='vehicle_number']");

    vehicleInputs.forEach(input => {
        input.addEventListener("input", function () {
            this.value = this.value.toUpperCase();
        });
    });
});


// ===== CONFIRM EXIT ACTION =====
const exitForm = document.querySelector("form");
if (exitForm && window.location.pathname.includes("exit")) {
    exitForm.addEventListener("submit", function (e) {
        const confirmExit = confirm("Are you sure you want to mark this vehicle as exited?");
        if (!confirmExit) {
            e.preventDefault();
        }
    });
}


// ===== SIMPLE PAGE FADE IN EFFECT =====
window.onload = function () {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 0.5s ease-in";
    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 100);
};


// ===== SIMPLE FORM VALIDATION =====
document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", function (e) {
        const inputs = form.querySelectorAll("input[required], select[required]");
        for (let input of inputs) {
            if (!input.value.trim()) {
                alert("Please fill all required fields.");
                e.preventDefault();
                return;
            }
        }
    });
});