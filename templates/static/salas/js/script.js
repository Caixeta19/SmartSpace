function toggleMenu() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active');
    
    // Fechar menu ao clicar em um link (opcional)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navbar.classList.remove('active');
        });
    });
}