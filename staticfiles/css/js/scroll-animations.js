document.addEventListener('DOMContentLoaded', () => {
    const username = 'GeraMartinez94';
    const url = `https://api.github.com/users/${username}/repos`;

    fetch(url)
        .then(response => response.json())
        .then(repos => {
            const statsContainer = document.getElementById('repo-stats');
            repos.forEach(repo => {
                const repoCard = document.createElement('div');
                repoCard.classList.add('repo-card', 'animate-on-scroll');
                repoCard.innerHTML = `
                    <h3><a href="${repo.html_url}" target="_blank">${repo.name}</a></h3>
                    <p><strong>Estrellas:</strong> ${repo.stargazers_count}</p>
                    <p><strong>Forks:</strong> ${repo.forks_count}</p>
                    <p><strong>Lenguaje:</strong> ${repo.language || 'N/A'}</p>
                `;
                statsContainer.appendChild(repoCard);
            });

            // Inicializa Intersection Observer para las nuevas tarjetas
            const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observerCallback = (entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('fade-in-up');
                        observer.unobserve(entry.target);
                    }
                });
            };

            const observer = new IntersectionObserver(observerCallback, observerOptions);
            elementsToAnimate.forEach(element => observer.observe(element));
        })
        .catch(error => console.error('Error al obtener los repositorios:', error));
});
