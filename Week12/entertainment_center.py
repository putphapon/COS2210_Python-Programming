#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

movie_1 = media.Movie("13 Reasons Why",
                        "Follows teenager Clay Jensen, in his quest to uncover the story behind his classmate and crush, Hannah, and her decision to end her life.",
                        "https://m.media-amazon.com/images/M/MV5BMDYzZTRlNGEtZDc2Mi00ZGNjLTlmZDAtMmVjMDZkOThiODEwXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_QL75_UX380_CR0,0,380,562_.jpg",
                        "https://www.youtube.com/watch?v=poUq9ypynKs")

movie_2 = media.Movie("Sex Education",
                     "A teenage boy with a sex therapist mother teams up with a high school classmate to set up an underground sex therapy clinic at school.",
                     "https://m.media-amazon.com/images/M/MV5BZjgyMzFiMDgtNWNmMS00ZDEyLTkzYzgtMjMzZjk4YjhjZWUxXkEyXkFqcGdeQXVyNDg4MjkzNDk@._V1_QL75_UY562_CR35,0,380,562_.jpg",
                     "https://www.youtube.com/watch?v=7oeGbdbUQQs")

movie_3 = media.Movie("Money Heist", 
                             "An unusual group of robbers attempt to carry out the most perfect robbery in Spanish history - stealing 2.4 billion euros from the Royal Mint of Spain.",
                             "https://m.media-amazon.com/images/M/MV5BZDcxOGI0MDYtNTc5NS00NDUzLWFkOTItNDIxZjI0OTllNTljXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UY720_.jpg",
                             "https://www.youtube.com/watch?v=p_PJbmrX4uk")

movie_4 = media.Movie("The Haunting of Bly Manor",
                          "After an au pair’s tragic death, Henry hires a young American nanny to care for his orphaned niece and nephew who reside at Bly Manor with the chef Owen, groundskeeper Jamie and housekeeper, Mrs. Grose.",
                          "https://m.media-amazon.com/images/M/MV5BZGJkMDRiOWUtZTMzZC00YzYzLWI1NDAtODc4ZGFiN2Q2MmJlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_FMjpg_UX1080_.jpg",
                          "https://www.youtube.com/watch?v=cxeiY2W03Mc")

movie_5 = media.Movie("Stranger Things",
                          "When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back.",
                          "https://m.media-amazon.com/images/M/MV5BN2ZmYjg1YmItNWQ4OC00YWM0LWE0ZDktYThjOTZiZjhhN2Q2XkEyXkFqcGdeQXVyNjgxNTQ3Mjk@._V1_FMjpg_UY720_.jpg",
                          "https://www.youtube.com/watch?v=ILwLN6hV-X8")

movie_6 = media.Movie("The Crown",
                                "Follows the political rivalries and romance of Queen Elizabeth II's reign and the events that shaped the second half of the twentieth century.",
                                "https://m.media-amazon.com/images/M/MV5BZmY0MzBlNjctNTRmNy00Njk3LWFjMzctMWQwZDAwMGJmY2MyXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_FMjpg_UX675_.jpg",
                                "https://www.youtube.com/watch?v=OiXEpminPms")


movies = [
    movie_1,
    movie_2,
    movie_3,
    movie_4,
    movie_5,
    movie_6
]

fresh_tomatoes.open_movies_page(movies)
