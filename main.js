console.log("Dashboard JS Loaded");

setInterval(() => {
    fetch("/api/sos_status")
        .then(res => res.json())
        .then(data => {
            document.getElementById("sosStatus").innerText = data.active ? "SOS TRIGGERED!" : "All Clear";
        });
}, 2000);
