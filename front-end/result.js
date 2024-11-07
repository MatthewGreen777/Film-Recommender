document.addEventListener('DOMContentLoaded', () => {
    const resultsContainer = document.getElementById('movie-details');
    const movieResults = JSON.parse(localStorage.getItem('movieResults'));

    if (movieResults) {
        movieResults.forEach(movie => {
            // Create container for each movie
            const movieContainer = document.createElement('div');
            movieContainer.classList.add('movie-item');

            // Create poster element
            const poster = document.createElement('img');
            poster.src = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
            poster.alt = `${movie.title} Poster`;
            movieContainer.appendChild(poster);

            // Create title element
            const title = document.createElement('h2');
            title.textContent = movie.title;
            movieContainer.appendChild(title);

            // Append the movie container to the results container
            resultsContainer.appendChild(movieContainer);
        });
    } else {
        resultsContainer.textContent = 'No results found.';
    }
});
