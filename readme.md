This repo contains the Single Page App using Vue and Flask from the tutorial by Michael Herman: <br/>
<a href="https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/">Developing a Single Page App with Flask and Vue.js</a>

After cloning, ensure that Flask and Flask-CORS are installed by running <br>
(env)$ pip install Flask==2.2.3 Flask-Cors==3.0.10</br>
Install npm in the client folder using: <br>
npm install in the terminal
<p>
To run this application locally<br/>
1.  Navigate to server folder:<br/>
flask run --port=5001 --debug<br/><br/>
http://localhost:5001/ping  should return "pong"

2. Navigate to client folder:
<br/>
$ npm run dev<br/>
http://localhost:5173/ should display the Book application<br>

TODO Challenge List:
<ul><li>Automated Test for route http://localhost:5001/books <br>

[https://github.com/mjhea0/flaskr-tdd given as resource]
DONE:  pytest package installed, tests folder created in server directory <br>
still need to fix __init__ file and tests <br></li>
<li>
Use Alert Component to display errors<br>
Make alert dismissible (see bootstrap documentation)</li>
<li>
Use Same Modal for both POST and PUT Requests<br/>
Thoughts - modals have different click events, vmodal titles (edit vs add.)</li>
<li>
-Clean the component up by moving the methods that make HTTP calls to a utils or services file.<br>
-Combine some of the methods that contain similar logic, like handleAddSubmit and handleEditSubmit.</li>
<li>
-Add Confirmation Alert before Delete action<br>
-If Books[] is empty, message = "No Books!  Please Add one" </li>


</ul>
