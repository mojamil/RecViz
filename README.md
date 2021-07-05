# RecViz (https://recviz.herokuapp.com/)
## Introduction
This is a program that I made to understand preferences in television shows. It can create network graphs from people's imdb lists to see if the shows they have watched connect with each other in some way. The nodes of the graph are different TV shows and they have edges between them if one show would recommended to someone who watched the other. For example, there would be an edge between Loki and Wandavision as people would recommend one if someone had seen the other. There is an additional feature to find recommendations based on multiple shows. You can visit the link in the title to get a better idea about how the app works.

## How to run locally
- Make sure you have python3 on your system
- Create a virtual environment if you want to following these instructions: https://docs.python.org/3/library/venv.html
- Run `pip install -r requirements.txt` in the terminal
- Replace the key variable in utils/recs_tmdb.py with an API key from tmdb. Use these instructions to get the key: https://developers.themoviedb.org/3/getting-started/introduction
- Run `python app.py`
- That should start running the flask app on localhost
- Navigate to a browser using the link displayed in the terminal

## Future Plans
Recommendations are currently received from the tmdb api, however, they are not always accurate for new television shows as such I am think of other methods to get recommendations.
