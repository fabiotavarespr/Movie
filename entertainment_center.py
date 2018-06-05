import media
import fresh_tomatoes

chef = media.Movie("Chef",
                    114,
                    "A head chef quits his restaurant job and buys a food truck in an effort to reclaim his creative promise, while piecing back together his estranged family.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                    "https://www.youtube.com/watch?v=L3OkPRRptgQ")

julieEJulia = media.Movie("Julie & Julia",
                    118,
                    "Julia Child's story of her start in the cooking profession is intertwined with blogger Julie Powell's 2002 challenge to cook all the recipes in Child's first book.",
                    "https://upload.wikimedia.org/wikipedia/en/0/00/Julie_and_julia.jpg",
                    "https://www.youtube.com/watch?v=qqQICUzdKbE")

jiro = media.Movie("Jiro Dreams of Sushi",
                    81,
                    "A documentary on 85-year-old sushi master Jiro Ono, his renowned Tokyo restaurant, and his relationship with his son and eventual heir, Yoshikazu.",
                    "https://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg",
                    "https://www.youtube.com/watch?v=Hi1jxRanimU")

toast = media.Movie("Toast",
                    96,
                    "The ultimate nostalgia trip through everything edible in 1960s Britain.",
                    "https://upload.wikimedia.org/wikipedia/commons/5/5d/71hnd8cRvPL._SL1500.jpg",
                    "https://www.youtube.com/watch?v=uj7aSMpQSeI")

burnt = media.Movie("Burnt",
                    101,
                    "Adam Jones is a chef who destroyed his career with drugs and diva behavior. He cleans up and returns to London, determined to redeem himself by spearheading a top restaurant that can gain three Michelin stars.",
                    "https://upload.wikimedia.org/wikipedia/en/2/21/Burnt_Poster_Updated.jpg",
                    "https://www.youtube.com/watch?v=HXaff0PpszM")

ratatouille = media.Movie("Ratatouille",
                    111,
                    "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant",
                    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                    "https://www.youtube.com/watch?v=PeFGdSrFTUw")

movies = [toast, chef, julieEJulia, burnt, jiro, ratatouille]
fresh_tomatoes.open_movies_page(movies)