import media
import fresh_tomatoes
import tmdbsimple as tmdb

#tmdb API key obtained from tmdb account used to make queries
tmdb.API_KEY = '14b69132b7d2d41575213348cceee8cd'

movies_to_display = []

#Extract movies and data in JSON format in decreasing order of popularity
discover_movies = tmdb.discover.Discover()
most_popular_movies = discover_movies.movie(page = 1,
    sort_by = 'popularity.desc')

#Extract top ten most popular movies
ten_most_popular = most_popular_movies['results'][:10]

for movie in ten_most_popular:
    # For each movie in ten most popular, extract the title, url of poster
    # and trailer in tmdb's database. Construct a movie object using all
    # extracted information, and append to movies to display
    movie_id = movie['id']
    title = movie['title']
    poster_url = 'https://image.tmdb.org/t/p/w300' + movie['poster_path']
    tmdb_movie = tmdb.Movies(movie_id)
    videos = tmdb_movie.videos()
    trailer = videos['results'][0]
    trailer_url = 'https://www.youtube.com/watch?v=' + trailer['key']
    displayed_movie = media.Movie(title,poster_url,trailer_url)
    movies_to_display.append(displayed_movie)

fresh_tomatoes.open_movies_page(movies_to_display)