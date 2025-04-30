function toggleMenu() {
    const menu = document.getElementById("menu");
    const display = window.getComputedStyle(menu).display;

    if (display === "none") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}
