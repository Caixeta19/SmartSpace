function toggleMenu() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active');

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navbar.classList.remove('active');
        });
    });
}
