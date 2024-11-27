from flask import render_template, request, url_for, redirect, jsonify
from Sports_League import create_app, mysql  
from MySQLdb.cursors import DictCursor


app = create_app()
with app.app_context():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM Season")
    seasons = cur.fetchall()
    print(seasons)
    cur.close()

@app.route('/')
def welcome():
    return ("Welcome to our Website.")

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    
    cur.execute("SELECT * FROM Season")
    seasons = cur.fetchall()

    cur.execute("SELECT * FROM Team")
    teams = cur.fetchall()
    cur.close()

    return render_template('home.html', data=teams)


@app.route('/team')
def team():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Team")
    teams = cur.fetchall()
    cur.close()


    teams_with_logo = []
    for team in teams:
        team_logo_url = url_for('static', filename='profile_pics/' + (team[10] or 'images.jpeg'))
        team_with_logo = team + (team_logo_url,)  
        teams_with_logo.append(team_with_logo)

    return render_template('team.html', teams=teams_with_logo)



@app.route('/stadium')
def stadium():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Stadium")
    stadiums = cur.fetchall()
    cur.close()
    return render_template('stadium.html', stadiums=stadiums)

@app.route('/team/<int:team_id>')
def team_players(team_id):
    cursor = mysql.connection.cursor()
    query = """
        SELECT P.Player_ID, CONCAT(P.First_Name, ' ', P.Last_Name) AS Player_Name, P.Role 
        FROM Player P
        WHERE P.Current_Team_ID = %s
    """
    cursor.execute(query, (team_id,))
    players = cursor.fetchall()
    cursor.close()
    return render_template('team_players.html', players=players)

@app.route('/player/<int:player_id>')
def player_details(player_id):
    cursor = mysql.connection.cursor()
    query = """
        SELECT Player_ID, CONCAT(First_Name, ' ', Last_Name) AS Full_Name, Nationality, Role, 
               Batting_Style, Bowling_Style, Total_Runs_Scored, Total_Wickets_Taken, 
               Total_Catches_Taken, Total_Matches_Played, Total_Half_Centuries, Total_Centuries 
        FROM Player 
        WHERE Player_ID = %s
    """
    cursor.execute(query, (player_id,))
    player = cursor.fetchone()
    cursor.close()
    return render_template('player_details.html', player=player)

@app.route('/seasons', methods=['GET'])
def seasons():
    cursor = mysql.connection.cursor(DictCursor)
    

    query = """
        SELECT S.Season_ID, S.Year, S.Total_Matches_Played,
               WT.Team_Name AS Winning_Team, RT.Team_Name AS Runner_Team,
               OC.First_Name AS Orange_Cap_Winner_First_Name, OC.Last_Name AS Orange_Cap_Winner_Last_Name,
               PC.First_Name AS Purple_Cap_Winner_First_Name, PC.Last_Name AS Purple_Cap_Winner_Last_Name
        FROM Season S
        LEFT JOIN Team WT ON S.Winning_Team_ID = WT.Team_ID
        LEFT JOIN Team RT ON S.Runner_Team_ID = RT.Team_ID
        LEFT JOIN Player OC ON S.Orange_Cap_Winner_ID = OC.Player_ID
        LEFT JOIN Player PC ON S.Purple_Cap_Winner_ID = PC.Player_ID
    """
    cursor.execute(query)
    seasons = cursor.fetchall()
    cursor.close()
    

    return render_template('seasons.html', seasons=seasons)



@app.route('/matches')
def matches():
    cursor = mysql.connection.cursor(DictCursor)  # Use DictCursor
    query = """
        SELECT M.Match_ID,
               T1.Team_Name AS Team1_Name,
               T2.Team_Name AS Team2_Name,
               S.Stadium_Name,
               M.Match_Date
        FROM Matches M
        JOIN Team T1 ON M.Team1_ID = T1.Team_ID
        JOIN Team T2 ON M.Team2_ID = T2.Team_ID
        JOIN Stadium S ON M.Stadium_ID = S.Stadium_ID
    """
    cursor.execute(query)
    matches = cursor.fetchall()  # Rows will be dictionaries
    cursor.close()
    return render_template('matches.html', matches=matches)





if __name__ == "__main__":
    app.run(debug=True) 