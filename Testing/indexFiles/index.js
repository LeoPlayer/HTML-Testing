function timedAlert() {
    while (true) {
        alert("wee");
    }
}

function date() {
    document.getElementById('dateText').innerHTML = Date();
}

function virus() {
    if (confirm("Please download virus")) {
        //virus downloading thing, or download random files automatically still not here because Justin shutdown the server
    } else {
        while (true) {
            alert("No")
        }
    }
}
