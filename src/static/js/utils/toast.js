function showToast() {
    let toast = document.getElementById("messages");
    if (toast) {
        setTimeout(function () {
            toast.classList.add("hidden");
        }, 5000);
    };
}

showToast();
