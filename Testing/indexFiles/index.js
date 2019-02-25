function timedAlert() {
    while (true) {
        alert("wee");
    }
}

function date() {
    document.getElementById('dateText').innerHTML = Date();
}

function virus() {
    if (confirm("Press a button!")) {
        //virus downloading thing, or download random files automatically
    } else {
        while (true) {
            alert("No")
        }
    }
}
