This repo contains the Single Page App using Vue and Flask from the tutorial by Michael Herman: <br/>
<a href="https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/">Developing a Single Page App with Flask and Vue.js</a>

After cloning, ensure that Flask and Flask-CORS are installed by running <br>
(env)$ pip install Flask==2.2.3 Flask-Cors==3.0.10</br>
Install npm in the client folder using <br>
npm install
<p>
To run this application locally<br/>
1.  Navigate to server folder:<br/>
flask run --port=5001 --debug<br/><br/>
http://localhost:5001/ping  should return "pong"

2. Navigate to client folder:<br/>
<br/>
$ npm run dev<br/>
http://localhost:5173/ should display the Book application