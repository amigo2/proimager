# Proimager

Proimager project consists of a Dockerize django project with in mind capabilities of a future implementation from monolithic to microservices. The communication between microservices would be implemented with docker-compose
The project itself is an API with no front end, where you can upload multiple images at once. Those files will be then saved and uploaded to a db(mysql) with a name on it that can be accessible from a link, it can be saved in at least 2 formats jpeg and png.
Aswell you can create a User, login, logout, token capabilities from rest-auth.
The project uses the 2 main types of test, unitest and Pytest, to validate various aspects of the application.

## Installation

Prerequisites: Docker installed and Python 3+
Clone/ download from repo
Install dependencies
```bash
$docker-compose build
```
Docker run
```bash
$docker-compose run
```
We need to make migrations with Docker, open new terminal to find out our docker id
```bash
$docker ps
$docker exec -it <container id> python manage.py makemigrations
```
Migrate
```bash
$docker exec -it <container id> python manage.py migrate
```
Create superuser
```bash
$docker exec -it <container id> python manage.py createsuperuser
```
name
password

Access the Application, if never acces application before go to registration
http://0.0.0.0:8000/registration/
If already an user
http://0.0.0.0:8000/proimage.com/


## Usage

As an User mainly you want to upload multiple files in a row, over, the endpoint http://0.0.0.0:8000/photos/file/
Use Postman as shown to upload multiple files


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
