# Importing the frameworks

from flask import *
from datetime import datetime
import database

user_details = {}
session = {}
page = {}

# Initialise the application
app = Flask(__name__)
app.secret_key = 'aab12124d346928d14710610f'


#####################################################
##  INDEX
#####################################################

@app.route('/')
def index():
    # Check if the user is logged in
    if('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))
    page['title'] = 'Movie Recommender Company'
    
    return redirect(url_for('list_movie'))

    #return render_template('index.html', session=session, page=page, user=user_details)

#####################################################
##  LOGIN
#####################################################

@app.route('/login', methods=['POST', 'GET'])
def login():
    # Check if they are submitting details, or they are just logging in
    if (request.method == 'POST'):
        # submitting details
        login_return_data = check_login(request.form['id'], request.form['password'])

        # If they have incorrect details
        if login_return_data is None:
            page['bar'] = False
            flash("Incorrect login info, please try again.")
            return redirect(url_for('login'))

        # Log them in
        page['bar'] = True
        welcomestr = 'Welcome back, ' + login_return_data['firstname'] + ' ' + login_return_data['lastname']
        flash(welcomestr)
        session['logged_in'] = True

        # Store the user details
        global user_details
        user_details = login_return_data
        return redirect(url_for('index'))

    elif (request.method == 'GET'):
        return(render_template('login.html', page=page))

#####################################################
##  LOGOUT
#####################################################

@app.route('/logout')
def logout():
    session['logged_in'] = False
    page['bar'] = True
    flash('You have been logged out. See you soon!')
    return redirect(url_for('index'))

#####################################################
##  List Movie
#####################################################

@app.route('/list_movie', methods=['POST', 'GET'])
def list_movie():
    # Check if user is logged in
    if ('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))

    # User is just viewing the page
    if (request.method == 'GET'):
        # First check if specific movie
        movie_list = database.findMoviesByStaff(user_details['login'])
        if (movie_list is None):
            movie_list = []
            flash("There are no movies in the system for " + user_details['firstname'] + " " + user_details['lastname'])
            page['bar'] = False
        return render_template('movie_list.html', movie=movie_list, session=session, page=page)

    # Otherwise try to get from the database
    elif (request.method == 'POST'):
        search_term = request.form['search']
        if (search_term == ''):
            movie_list_find = database.findMoviesByStaff(user_details['login'])
        else:    
            movie_list_find = database.findMoviesByCriteria(search_term)
        if (movie_list_find is None):
            movie_list_find = []
            flash("Searching \'{}\' does not return any result".format(request.form['search']))
            page['bar'] = False
        return render_template('movie_list.html', movie=movie_list_find, session=session, page=page)

#####################################################
##  Add Movie
#####################################################

@app.route('/new_movie' , methods=['GET', 'POST'])
def new_movie():
    # Check if the user is logged in
    if ('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))

    # If we're just looking at the 'new movie' page
    if(request.method == 'GET'):
        times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        return render_template('new_movie.html', user=user_details, times=times, session=session, page=page)

	# If we're adding a new movie
    success = database.addMovie(request.form['title'],
                                 request.form['releasedate'],
                                 request.form['genre1'],
                                 request.form['genre2'],
                                 request.form['staff'],
                                 request.form['description'])
    if(success == True):
        page['bar'] = True
        flash("Movie added!")
        return(redirect(url_for('index')))
    else:
        page['bar'] = False
        flash("There was an error adding a new movie")
        return(redirect(url_for('new_movie')))

#####################################################
## Update Movie
#####################################################
@app.route('/update_movie', methods=['GET', 'POST'])
def update_movie():
    # Check if the user is logged in
    if ('logged_in' not in session or not session['logged_in']):
        return redirect(url_for('login'))

    # If we're just looking at the 'update movie' page
    if (request.method == 'GET'):
        # Get the movie
        genre2 = '' if len(request.args.get('genre').split(",")) < 2 else request.args.get('genre').split(",")[1]
        movie = {
            'movie_id': request.args.get('movie_id'),
            'title': request.args.get('title'),
            'releasedate': datetime.strptime(request.args.get('releasedate'), '%d-%m-%Y').date(),
            'avgrating': request.args.get('avgrating'),
            'genre1': request.args.get('genre').split(",")[0],
            'genre2': genre2,
            'staff': request.args.get('staff'),
            'description': request.args.get('description')
        }

        # If there is no movie
        if movie['movie_id'] is None:
            movie = []
		    # Do not allow viewing if there is no movie to update
            page['bar'] = False
            flash("You do not have access to update that record!")
            return(redirect(url_for('index')))

	    # Otherwise, if movie details can be retrieved
        times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        return render_template('update_movie.html', movieInfo=movie, user=user_details, times=times, session=session, page=page)

    # If we're updating movie
    success = database.updateMovie(request.form['movie_id'],
                                request.form['title'],
                                request.form['releasedate'],
                                request.form['avgrating'],
                                request.form['genre1'],
                                request.form['genre2'],
                                request.form['staff'],
                                request.form['description'])
    if (success == True):
        page['bar'] = True
        flash("Movie record updated!")
        return(redirect(url_for('index')))
    else:
        page['bar'] = False
        flash("There was an error updating the movie")
        return(redirect(url_for('index')))

def get_movie(movie_id, username):
    for movie in database.findMoviesByStaff(username):
        if movie['movie_id'] == movie_id:
            return movie
    return None

def check_login(username, password):
    userInfo = database.checkStaffCredentials(username, password)

    if userInfo is None:
        return None
    else:
        tuples = {
            'login': userInfo[0],
            'password': userInfo[1],
            'firstname': userInfo[2],
            'lastname': userInfo[3],
            'mobile': userInfo[4],
            'email': userInfo[5],
            'address': userInfo[6],
            'compensation': userInfo[7],
        }
        return tuples
