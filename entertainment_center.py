#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fresh_tomatoes
import media

"""entertainment_center.py: This script allows to
create instances of movies an actors from static data.

We have Movies features like:

titles, prices, informations, trailers, posters, storylines, dates,

and Actors features like:

name, genders, nationality, age


__author__      = "Dayans R"
__copyright__   = "Copyright 2015, Dram IT"

"""

titles = [
    "the green mile",
    "the hunger games", "avatar",
    "divergent", "midnight in paris",
    "edge of the garden"]

prices = [13, 5.6, 20.5, 15, 18, 18]
informations = [
    "https://en.wikipedia.org/wiki/The_Green_Mile_(film)",
    "https://en.wikipedia.org/wiki/The_Hunger_Games:_Mockingjay_-_Part_2",
    "https://en.wikipedia.org/wiki/Avatar_(2009_film)",
    "https://en.wikipedia.org/wiki/Divergent_(film)",
    "https://en.wikipedia.org/wiki/Midnight_in_Paris",
    "http://es.scribd.com/doc/62992293/Edge-of-the-Garden-Synopsis#scribd"
    ]
trailers = [
    "https://www.youtube.com/watch?v=ctRK-4Vt7dA",
    "https://www.youtube.com/watch?v=n-7K_OjsDCQ",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "https://www.youtube.com/watch?v=e8UHUAdBl84",
    "https://www.youtube.com/watch?v=FAfR8omt-CY",
    "https://www.youtube.com/watch?v=D9Omwylqs5A"]
posters = [
    ("https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Green_mile.jpg/"
        "220px-Green_mile.jpg"),
    ("https://upload.wikimedia.org/wikipedia/en/thumb/4/42/"
        "HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg"),
    ("https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/"
        "Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg"),
    ("https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Divergent.jpg/"
        "220px-Divergent.jpg"),
    ("https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/"
        "Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg"),
    "http://www.cineol.net/galeria/carteles/bigtmp_25864.jpg"]
story_lines = [
    "In a Louisiana nursing home in 1999, Paul Edgecomb becomes nervous while"
    "watching the 1935 film Top Hat. He is with his elderly friend Elaine, who"
    "becomes concerned, and Paul tells her that the film reminded him of his"
    "past, when he was a prison officer in charge of death row inmates at the"
    "Cold Mountain Penitentiary during the summer of 1935.",
    "With the nation of Panem in a full-scale revolutionary war, Katniss ("
    "Jennifer Lawrence) confronts President Snow (Donald Sutherland) in the"
    "final showdown. Teamed with a group of her closest friends – including"
    "Gale(Liam Hemsworth), Finnick(Sam Claflin), Cressida(Natalie Dormer) and"
    "Peeta (Josh Hutcherson) – Katniss goes off on a mission with the District"
    "13 unit as they risk their lives to liberate the citizens of Panem, and"
    "stage an assassination attempt on President Snow who has become"
    "increasingly obsessed with destroying her. Although rebels - including"
    "fellow victors, Johanna (Jena Malone), Haymitch (Woody Harrelson), and"
    "Beetee (Jeffrey Wright)- now control most of Panem, the girl on fire must"
    "still overcome one last challenge to win President Snow's 'game' - to"
    "conquer the Capitol at the risk of losing her friends and loved ones. The"
    "mortal traps, enemies, and moral choices that await Katniss will"
    "challenge"
    "her more than any arena she faced in The Hunger Games as she realizes the"
    "stakes are no longer just for survival–they are for the future of Panem.",
    "By 2154, humans have depleted Earth's natural resources, leading to a"
    "severe energy crisis. The Resources Development Administration, RDA for"
    "short, mines for a valuable mineral – unobtanium – on Pandora, a densely"
    "forested habitable moon orbiting the gas giant Polyphemus in the Alpha"
    "Centauri star system. Pandora, whose atmosphere is poisonous to humans,"
    "is inhabited by the Na'vi, 10-foot tall (3.0 m), blue-skinned, sapient"
    "humanoids who live in harmony with nature and worship a mother goddess"
    "called Eywa.",
    "In a futuristic dystopian Chicago, the society is divided into five"
    "factions: Abnegation (the selfless), Amity (the peaceful), Candor (the"
    "honest), Dauntless (the brave), and Erudite (the intellectual). The"
    "remaining population are the Factionless, who have no status or privilege"
    "in this society. When children reach the age of 16, they undergo a serum-"
    "induced psychological test which indicates their best-suited faction,"
    "then"
    "are allowed to choose any faction as their permanent group at the"
    "subsequent Choosing Ceremony.",
    "Gil Pender, a successful but creatively unfulfilled Hollywood"
    "screenwriter, and his fiancée, Inez, are in Paris, vacationing with"
    "Inez's"
    "wealthy, conservative parents. Gil is struggling to finish his first"
    "novel,"
    "centered on a man who works in a nostalgia shop. Inez dismisses his"
    "ambition as a romantic daydream and encourages him to stick with"
    "lucrative"
    "screenwriting. Gil is considering moving to Paris(which he notes, much to"
    "the dismay of his fiancée, is at its most beautiful in the rain). Inez is"
    "intent on living in Malibu. By chance, they are joined by Inez's friend"
    "Paul who is described as both pedantic and a pseudo-intellectual, and who"
    "speaks with great authority but questionable accuracy on the history and"
    "art of Paris. Paul contradicts a tour guide at the Rodin Museum, and"
    "insists that his knowledge of Rodin's relationships is more accurate than"
    "that of the tour guide. Inez admires him; Gil finds him insufferable.",
    "A lonely businessman temporarily relocates to Maine after a bad breakup."
    "He moves into a rundown cottage, where he meets the beautiful spirit of a"
    "woman who lived in the house fifty years before. As they form a"
    "friendship,"
    "they begin to help each other in ways they never knew were possible, and"
    "change both their fortunes forever."
]
dates = ["1999", "2015", "2009", "2014", "2011", "2011"]

actors = [
    "Tom Hanks",
    "Jennifer Lawrence",
    "Zoe Saldaña",
    "Shailene Woodley",
    "Owen Wilson",
    "Rob Estes"]
actors_genders = ["male", "female", "female", "female", "male", "male"]
actors_nationalities = ["USA", "USA", "USA", "USA", "USA", "USA"]
actors_ages = ["59", "25", "37", "23", "46", "46"]

movies = []


# Here we create movies and actors instances from previous defined data.
# Moreover we append movies instances in a list.
for i in range(len(titles)):
    current_movie = media.Movie()
    current_movie.title = titles[i].title()
    current_movie.synopsis_url = informations[i]
    current_movie.story_line = (
        (story_lines[i][:500])
        if len(story_lines[i]) > 500
        else story_lines[i])
    current_movie.price = prices[i]
    current_movie.poster_image_url = posters[i]
    current_movie.trailer_youtube_url = trailers[i]
    current_movie.publishment_date = dates[i]

    current_actor = media.Actor(
        actors[i],
        actors_genders[i],
        actors_nationalities[i],
        actors_ages[i])
    current_movie.actor = current_actor
    movies.append(current_movie)

# Passing movies list to render in HTML structure.
fresh_tomatoes.open_movies_page(movies)
