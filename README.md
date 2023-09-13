# fantasy-premier-league

Streamlit dashboard for [fantasy premier league](https://fantasy.premierleague.com/) analysis. 

The codebase leverages premier league api endpoints to collect real time player, match and team data which is presented utilising plotly. 

The dashboard contains a total of 9 pages:

- 4 generic player and club overview pages
- 5 manager specific pages (pages hidden behind authentication)

Backed by a docker container, the dashboard can be viewed [here](https://fantasy-premier-league-streamlit.azurewebsites.net/). The latest container builds can be found under the following repositories:

- [DockerHub](https://hub.docker.com/r/powellrhys/fantasy-premier-league-streamlit)
- [GitHub Packages](https://github.com/powellrhys/fantasy-premier-league-streamlit/pkgs/container/fantasy-premier-league-streamlit)
