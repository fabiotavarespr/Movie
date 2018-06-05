import media
import fresh_tomatoes

toy_stoty = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

school_of_rock = media.Movie("School of Rock",
                     "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "While on a trip to Paris with his fiancee's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

chef = media.Movie("Chef",
                     "A head chef quits his restaurant job and buys a food truck in an effort to reclaim his creative promise, while piecing back together his estranged family.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                     "https://www.youtube.com/watch?v=L3OkPRRptgQ")

movies = [toy_stoty, avatar, matrix, school_of_rock, midnight_in_paris, chef]
fresh_tomatoes.open_movies_page(movies)
