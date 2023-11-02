# fantasy-premier-league

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

The following repo contains the code for a image number classification model powered by [tensorflow](https://www.tensorflow.org/) and visualised by [streamlit](https://streamlit.io/).

Streamlit dashboard for [fantasy premier league](https://fantasy.premierleague.com/) analysis. 

The codebase leverages premier league api endpoints to collect real time player, match and team data which is presented utilising plotly. 

The dashboard contains a total of 9 pages:

- 4 generic player and club overview pages
- 5 manager specific pages (pages hidden behind authentication)

Backed by a docker container, the dashboard can be viewed [here](https://fantasy-premier-league-streamlit.azurewebsites.net/). The latest container builds can be found under the following repositories:

- [DockerHub](https://hub.docker.com/r/powellrhys/fantasy-premier-league-streamlit)
- [GitHub Packages](https://github.com/powellrhys/fantasy-premier-league-streamlit/pkgs/container/fantasy-premier-league-streamlit)
