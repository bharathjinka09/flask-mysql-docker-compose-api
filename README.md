Code for a creating a docker app with Flask and MySQL tutorial

Command to run docker flask mysql api:-

```
Build and Run:-
==============
sudo docker-compose up --build

Only build:-
==========
sudo docker-compose build

Only run:-
==========
sudo docker-compose up
```

Refer to [blog post about creating a flask-mysql app with docker](https://stavshamir.github.io/python/dockerizing-a-flask-mysql-app-with-docker-compose/)

## GitLab CI

The [.gitlab-ci.yml](.gitlab-ci.yml) file can be used in GitLab to build,
test, and deploy the code, as in https://gitlab.com/TrendDotFarm/docker-tutorial
For more information, read the [Docker Compose Integration to GitLab
CI](GitLab-CI.md) guide.
