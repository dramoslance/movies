import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 10px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie-information{
            padding-left: 10px;
            padding-right: 10px;
            padding-top: 5px;
        }
        .movie-header-info{
            font-weight: bold;
            margin-right: 5px;
        }
        @media only screen and (max-width:720px){
            .modal{
                width: 100%;
            }
            #trailer .modal-dialog{
                width: 100%;
            }            
            .hanging-close{
                right: 10px;
            }
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {

            //Movie Fields
            $("#trailer-video-container").empty();
            $("#modal-movie-title").empty();
            $("#modal-movie-synopsis-url").empty();
            $("#modal-movie-story-line").empty();
            $("#movie-price-value").empty();
            $("#movie-date-value").empty();
            
            //Actor Fields
            $("#modal-movie-actor-name").empty();
            $("#movie-actor-gender-value").empty();
            $("#movie-actor-nationality-value").empty();
            $("#movie-actor-age-value").empty();

            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var movieSynopsisUrl = $(this).attr('data-movie-synopsis-url');
            var movieTitle = $(this).attr('data-movie-title');
            var movieStoryLine = $(this).attr('data-movie-story-line');
            var moviePrice = $(this).attr('data-movie-price');
            var moviePublishmentDate = $(this).attr('data-movie-publishment-date');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));

            var movieActorName = $(this).attr('data-movie-actor-name');
            var movieActorGender = $(this).attr('data-movie-actor-gender');
            var movieActorNationality = $(this).attr('data-movie-actor-nationality');
            var movieActorAge = $(this).attr('data-movie-actor-age');
    
            $("#modal-movie-title").text(movieTitle);
            $("#modal-movie-story-line").append(movieStoryLine+'<a id="modal-movie-synopsis-url" href="" target="_blank">...more</a>');
            $("#movie-price-value").text(moviePrice);
            $("#movie-date-value").text(moviePublishmentDate);
            $("#modal-movie-synopsis-url").attr("href", movieSynopsisUrl);
            

            $("#modal-movie-actor-name").text(movieActorName);
            $("#movie-actor-gender-value").text(movieActorGender);
            $("#movie-actor-nationality-value").text(movieActorNationality);
            $("#movie-actor-age-value").text(movieActorAge);

        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>

          <div id="carousel-movie" class="carousel slide" data-ride="carousel">
          <!-- Indicators -->
          <ol class="carousel-indicators">
            <li data-target="#carousel-movie" data-slide-to="0" class="active"></li>
            <li data-target="#carousel-movie" data-slide-to="1"></li>
          </ol>

          <!-- Wrapper for slides -->
          <div class="carousel-inner" role="listbox">
            <div class="item active">
                <div class="scale-media" id="trailer-video-container">
                </div>                
            </div>
            <div class="item">
                <div class="movie-information">
                    <h2 id="modal-movie-title"></h2>
                    <div class="movie-header-info">Synopsis</div>
                    <p id="modal-movie-story-line"></p>
                    <div id="modal-movie-price"><span class="movie-header-info">Price:</span><span class="movie-value-info" id="movie-price-value"></span></div>
                    <div id="modal-movie-publishment-date"><span class="movie-header-info">Publishment Date:</span><span class="movie-value-info" id="movie-date-value"></span></div>
                    <div id="modal-actors">
                        <h2 id="modal-movie-actor-name"></h2>
                        <div id="modal-movie-actor-gender"><span class="movie-header-info">Gender:</span><span class="movie-value-info" id="movie-actor-gender-value"></span></div>
                        <div id="modal-movie-actor-nationality"><span class="movie-header-info">Nationality:</span><span class="movie-value-info" id="movie-actor-nationality-value"></span></div>
                        <div id="modal-movie-actor-age"><span class="movie-header-info">Age:</span><span class="movie-value-info" id="movie-actor-age-value"></span></div>
                    </div>
                </div>
            </div>
            ...
          </div>

          <!-- Controls -->
          <a class="left carousel-control" href="#carousel-movie" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="right carousel-control" href="#carousel-movie" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
          
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailers Project</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" 
    data-trailer-youtube-id="{trailer_youtube_id}"
    data-movie-synopsis-url="{movie_synopsis_url}"
    data-movie-title="{movie_title}"
    data-movie-story-line="{movie_story_line}"
    data-movie-price="{movie_price}"
    data-movie-publishment-date="{movie_publishment_date}"
    data-movie-actor-name="{movie_actor_name}"
    data-movie-actor-gender="{movie_actor_gender}"
    data-movie-actor-nationality="{movie_actor_nationality}"
    data-movie-actor-age="{movie_actor_age}"
    data-toggle="modal"
    data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    """Render movies information in HTML structure

    Args:
        movies: Movies to be rendered.

    Returns:
        Content with movies information redered on HTML structure.

    Raises:
        Bad HTML structure error.
    """

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_synopsis_url=movie.synopsis_url,
            movie_price=movie.price,
            movie_story_line=movie.story_line,
            movie_publishment_date=movie.publishment_date,
            movie_actor_name=movie.actor.name,
            movie_actor_gender=movie.actor.gender,
            movie_actor_nationality=movie.actor.nationality,
            movie_actor_age=movie.actor.age,
        )        


    return content


def open_movies_page(movies):
    """Allows to publish movies in the HTML

    Args:
        movies: List of movies instances to renderer in HTML.

    Returns:
        None.

    Raises:
        FileError: An error ocurred while savig HTML redered file.
    """

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

