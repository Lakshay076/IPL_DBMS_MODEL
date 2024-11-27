from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
from Sports_League import mysql, bcrypt
from Sports_League.users.form import RegistrationForm, LoginForm, UpdateAccountForm
from Sports_League.users.utils import save_picture
from Sports_League.models import Admin
from MySQLdb.cursors import DictCursor

users = Blueprint('users', __name__)

def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

def get_dict_cursor():
    cur = mysql.connection.cursor()
    cur.row_factory = dict_factory 
    return cur

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO ADMIN (username, email, password) VALUES (%s, %s, %s)",
            (form.username.data, form.email.data, hashed_password)
        )
        mysql.connection.commit()
        cur.close() 
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor() 
        cur.execute(
            "SELECT * FROM ADMIN WHERE email = %s", (form.email.data,)
        )
        result = cur.fetchone()
        cur.close() 
        
        print(f"Fetched result: {result}")

        if result: 
            if bcrypt.check_password_hash(result[4], form.password.data): 
                user = Admin(result[0], result[1], result[2], result[3], result[4]) 
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            flash('No user found with that email.', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        picture_file = current_user.image_file 
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE ADMIN SET username = %s, email = %s, image_file = %s WHERE Admin_ID = %s",
            (form.username.data, form.email.data, picture_file, current_user.id)
        )
        mysql.connection.commit()
        cur.close() 
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + (current_user.image_file or 'images.jpg'))
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route('/add_team', methods=['GET', 'POST'])
@login_required
def add_team():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Stadium")
    stadiums = cursor.fetchall()
    cursor.close()

    if request.method == 'POST':
        team_name = request.form['team_name']
        city = request.form['city']
        founding_year = request.form['founding_year']
        stadium_id = request.form['stadium_id']
        dress_colour = request.form['dress_colour']
        team_logo = request.files['team_logo']
        team_link = request.form['team_link']

        if team_logo:
            logo_filename = save_picture(team_logo)
        else:
            logo_filename = None

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO Team (Team_Name, City, Team_Founding_Year, Home_Stadium_ID, Team_Logo, Team_Dress_Colour, Team_Website_Link)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (team_name, city, founding_year, stadium_id, logo_filename, dress_colour, team_link))
        mysql.connection.commit()
        cursor.close()

        flash('Team added successfully!', 'success')
        return redirect(url_for('team'))

    return render_template('add_team.html', stadiums=stadiums)

@users.route('/view_team')
@login_required
def view_team():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Team")
    teams = cursor.fetchall()
    
    if cursor.description:
        column_names = [desc[0] for desc in cursor.description]
        teams = [dict(zip(column_names, team)) for team in teams]
    else:
        teams = [] 

    cursor.close()
    return render_template('team_list.html', title='Teams', teams=teams)

@users.route('/edit_team/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Stadium")
    stadiums = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT * FROM Team WHERE Team_ID = %s", (team_id,))
    team = cursor.fetchone()

    if not team:
        flash('Team not found.', 'danger')
        return redirect(url_for('team'))

    if request.method == 'POST':
        team_name = request.form['team_name']
        city = request.form['city']
        founding_year = request.form['founding_year']
        stadium_id = request.form['stadium_id']
        dress_colour = request.form['dress_colour']
        team_logo = request.files['team_logo']
        team_link = request.form['team_link']


        if team_logo:
            logo_filename = save_picture(team_logo)
        else:
            logo_filename = None

        cursor.execute("""
            UPDATE Team SET Team_Name = %s, City = %s, Team_Founding_Year = %s, Home_Stadium_ID = %s, Team_Logo = %s, Team_Dress_Colour = %s, Team_Website_Link = %s
            WHERE Team_ID = %s
        """, (team_name, city, founding_year, stadium_id, logo_filename, dress_colour, team_link, team_id))
        mysql.connection.commit()
        cursor.close()

        flash('Team updated successfully!', 'success')
        return redirect(url_for('team'))

    cursor.close()
    return render_template('edit_team.html', team=team, stadiums=stadiums)

@users.route('/edit_player/<int:player_id>', methods=['GET', 'POST'])
@login_required
def edit_player(player_id):
    cursor = mysql.connection.cursor(DictCursor)
    
    cursor.execute("SELECT * FROM Player WHERE Player_ID = %s", (player_id,))
    player = cursor.fetchone()

    if not player:
        flash('Player not found.', 'danger')
        return redirect(url_for('team_players', team_id=player.get('Current_Team_ID', 0)))

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        nationality = request.form['nationality']
        role = request.form['role']
        batting_style = request.form['batting_style']
        bowling_style = request.form['bowling_style']
        
        cursor.execute("""
            UPDATE Player 
            SET First_Name = %s, Last_Name = %s, Nationality = %s, Role = %s, 
                Batting_Style = %s, Bowling_Style = %s 
            WHERE Player_ID = %s
        """, (first_name, last_name, nationality, role, batting_style, bowling_style, player_id))
        
        mysql.connection.commit()
        cursor.close()
        
        flash('Player details updated successfully!', 'success')
        return redirect(url_for('team_players', team_id=player['Current_Team_ID']))

    cursor.close()
    return render_template('edit_player.html', player=player)

@users.route('/view_player')
def view_player():
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT Player_ID, CONCAT(First_Name, ' ', Last_Name) AS Player_Name FROM Player")
    players = cursor.fetchall()
    cursor.close()

    return render_template('view_player.html', players=players)

@users.route('/add_match', methods=['GET', 'POST'])
@login_required
def add_match():
    
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT Team_ID, Team_Name FROM Team")
    teams = cursor.fetchall()
    

    cursor.execute("SELECT Stadium_ID, Stadium_Name FROM Stadium")
    stadiums = cursor.fetchall()
    

    cursor.execute("SELECT Season_ID, Year FROM Season ORDER BY Year DESC LIMIT 1")
    latest_season = cursor.fetchone()
    cursor.close()

    if not teams or not stadiums or not latest_season:
        flash('Ensure that teams, stadiums, and seasons are available before adding matches.', 'warning')
        return redirect(url_for('view_team'))

    if request.method == 'POST':
        team1_id = request.form['team1_id']
        team2_id = request.form['team2_id']
        stadium_id = request.form['stadium_id']
        season_id = latest_season['Season_ID']
        match_date = request.form['match_date']
        match_type = request.form['match_type']

        try:
           
            if team1_id == team2_id:
                flash('A match cannot be scheduled between the same team.', 'danger')
                return redirect(url_for('users.add_match'))

            
            match_date_obj = datetime.strptime(match_date, "%Y-%m-%dT%H:%M")
            if match_date_obj <= datetime.now():
                flash('Match date and time must be in the future.', 'danger')
                return redirect(url_for('users.add_match'))

            
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO Matches (Season_ID, Team1_ID, Team2_ID, Match_Date, Match_Type, Stadium_ID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (season_id, team1_id, team2_id, match_date, match_type, stadium_id))
            mysql.connection.commit()
            cursor.close()

            flash('Match added successfully!', 'success')
            return redirect(url_for('matches'))

        except ValueError as e:
            flash(f'Error in input: {e}', 'danger')
            return redirect(url_for('users.add_match'))

    return render_template('add_match.html', teams=teams, stadiums=stadiums, latest_season=latest_season)
