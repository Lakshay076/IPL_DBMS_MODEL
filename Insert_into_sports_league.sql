
INSERT INTO Stadium (Stadium_Name, City, Country, Capacity, Pitch_Type, Average_First_Innings_Score, Total_Matches_Hosted)
VALUES 
('Wankhede Stadium', 'Mumbai', 'India', 33108, 'Flat pitch', 165, 250),
('Eden Gardens', 'Kolkata', 'India', 68000, 'Balanced pitch', 160, 300),
('M. Chinnaswamy Stadium', 'Bangalore', 'India', 40000, 'Batting friendly', 175, 200),
('Narendra Modi Stadium', 'Ahmedabad', 'India', 132000, 'Pace-friendly', 170, 150),
('Arun Jaitley Stadium', 'Delhi', 'India', 41820, 'Balanced pitch', 155, 190);

INSERT INTO Coach (First_Name, Last_Name, Nationality, Coach_Role, Years_Of_Experience)
VALUES 
('Ricky', 'Ponting', 'Australia', 'Head Coach', 15),
('Mahela', 'Jayawardene', 'Sri Lanka', 'Batting Coach', 10),
('Shane', 'Bond', 'New Zealand', 'Bowling Coach', 8),
('Rahul', 'Dravid', 'India', 'Head Coach', 12),
('Lasith', 'Malinga', 'Sri Lanka', 'Bowling Coach', 7);

INSERT INTO Team (Team_Name, City, Coach_ID, Team_Founding_Year, Total_Titles_Won, Team_Dress_Colour, Team_Website_Link, Team_Net_Worth, Home_Stadium_ID)
VALUES 
('Mumbai Indians', 'Mumbai', 1, '2008-01-01', 5, 'Blue', 'https://www.mumbaiindians.com', 800000000.00, 1),
('Chennai Super Kings', 'Chennai', 4, '2008-01-01', 4, 'Yellow', 'https://www.chennaisuperkings.com', 750000000.00, 2),
('Royal Challengers Bangalore', 'Bangalore', 2, '2008-01-01', 0, 'Red', 'https://www.royalchallengers.com', 700000000.00, 3),
('Delhi Capitals', 'Delhi', 1, '2008-01-01', 0, 'Blue', 'https://www.delhicapitals.com', 600000000.00, 5),
('Gujarat Titans', 'Ahmedabad', 5, '2021-01-01', 1, 'Navy Blue', 'https://www.gujarattitansipl.com', 650000000.00, 4);

INSERT INTO Player (First_Name, Last_Name, Date_Of_Birth, Nationality, Role, Batting_Style, Bowling_Style, Total_Runs_Scored, Total_Wickets_Taken, Total_Catches_Taken, Total_Matches_Played, Total_Half_Centuries, Total_Centuries, Base_Price, Current_Team_ID, IPL_Debut_Year, International_Career_Start, Total_IPL_Trophies_Won)
VALUES 
('Virat', 'Kohli', '1988-11-05', 'India', 'Batsman', 'Right_handed', NULL, 7000, 0, 100, 230, 40, 7, 17000000, 3, '2008-01-01', '2008-08-18', 0),
('Rohit', 'Sharma', '1987-04-30', 'India', 'Batsman', 'Right_handed', NULL, 6200, 0, 80, 210, 35, 6, 15000000, 1, '2008-01-01', '2007-06-23', 5),
('MS', 'Dhoni', '1981-07-07', 'India', 'Wicketkeeper', 'Right_handed', NULL, 5000, 0, 150, 220, 25, 3, 12000000, 2, '2008-01-01', '2004-12-23', 4),
('Jasprit', 'Bumrah', '1993-12-06', 'India', 'Bowler', 'Right_handed', 'Right_arm Fast', 100, 180, 50, 90, 0, 0, 10000000, 1, '2013-01-01', '2016-01-23', 3),
('Hardik', 'Pandya', '1993-10-11', 'India', 'All-rounder', 'Right_handed', 'Right_arm Fast', 2500, 75, 40, 110, 10, 1, 12000000, 5, '2015-01-01', '2016-01-26', 1);

INSERT INTO Umpire (First_Name, Last_Name, Nationality, Total_Matches, Date_Of_Birth, Umpire_Rating)
VALUES 
('Nitin', 'Menon', 'India', 75, '1983-11-12', 9),
('Aleem', 'Dar', 'Pakistan', 85, '1968-06-06', 10),
('Kumar', 'Dharmasena', 'Sri Lanka', 70, '1971-04-24', 8),
('Sundaram', 'Ravi', 'India', 60, '1966-04-22', 7),
('Chris', 'Gaffaney', 'New Zealand', 50, '1975-11-30', 8);

INSERT INTO Sponsorship (Team_ID, Sponsor_Name, Sponsorship_Type, Contract_Start_Year, Contract_End_Year, Sponsorship_Amount)
VALUES 
(1, 'Samsung', 'Jersey', '2020-01-01', '2024-01-01', 50000000.00),
(2, 'Aircel', 'Jersey', '2018-01-01', '2023-01-01', 30000000.00),
(3, 'Myntra', 'Jersey', '2019-01-01', '2024-01-01', 35000000.00),
(4, 'JSW Group', 'Jersey', '2019-01-01', '2024-01-01', 25000000.00),
(5, 'CRED', 'Jersey', '2022-01-01', '2026-01-01', 40000000.00);

INSERT INTO Contract (Player_ID, Contract_Start_Year, Contract_End_Year, Amount, Team_ID)
VALUES 
(1, '2020-01-01', '2025-01-01', 17000000.00, 3),
(2, '2019-01-01', '2024-01-01', 15000000.00, 1),
(3, '2018-01-01', '2023-01-01', 12000000.00, 2),
(4, '2021-01-01', '2025-01-01', 10000000.00, 1),
(5, '2021-01-01', '2026-01-01', 12000000.00, 5);

INSERT INTO Season (Year, Total_Matches_Played, Winning_Team_ID, Runner_Team_ID, Orange_Cap_Winner_ID, Purple_Cap_Winner_ID)
VALUES 
(2023, 74, 5, 1, 1, 4),
(2022, 74, 2, 3, 2, 4),
(2021, 60, 2, 1, 3, 5),
(2020, 60, 1, 2, 1, 5),
(2019, 60, 1, 3, 2, 4);

INSERT INTO Matches (Season_ID, Team1_ID, Team2_ID, Match_Date, Umpire1_ID, Umpire2_ID, Match_Result, Team1_Score, Team2_Score, Winning_Margin, Total_Overs_Bowled, Match_Type, Stadium_ID)
VALUES 
(1, 1, 2, '2023-05-29 20:00:00', 1, 2, 'Mumbai Indians won by 5 wickets', 160, 155, '5 wickets', 40, 'Final', 1),
(2, 2, 3, '2022-05-30 19:30:00', 3, 4, 'Chennai Super Kings won by 7 runs', 170, 163, '7 runs', 40, 'Final', 2),
(3, 1, 5, '2021-05-29 20:00:00', 1, 3, 'Delhi Capitals won by 10 wickets', 140, 139, '10 wickets', 40, 'Qualifier', 5),
(4, 4, 2, '2020-05-29 20:00:00', 4, 2, 'Gujarat Titans won by 6 wickets', 180, 179, '6 wickets', 40, 'Eliminator', 4),
(5, 3, 1, '2019-05-29 20:00:00', 1, 4, 'Mumbai Indians won by 1 run', 160, 159, '1 run', 40, 'Final', 1);

INSERT INTO Inning (Match_ID, Team_Batting_ID, Total_Runs, Total_Wickets, Overs_Faced, Inning_Number)
VALUES 
(1, 2, 155, 7, 20.0, '1st Inning'),
(1, 1, 160, 5, 19.3, '2nd Inning'),
(2, 2, 170, 8, 20.0, '1st Inning'),
(2, 3, 163, 9, 20.0, '2nd Inning'),
(3, 1, 140, 10, 19.5, '1st Inning'),
(3, 5, 141, 0, 14.0, '2nd Inning');

INSERT INTO Statistics (Player_ID, Season_ID, Matches_Played, Runs_Scored, Wickets_Taken, Catches_Taken, Fours, Sixes, Strike_Rate, Economy_Rate, Bowling_Average, Batting_Average)
VALUES 
(1, 1, 14, 550, 0, 15, 60, 25, 140.50, NULL, NULL, 45.83),
(2, 1, 13, 600, 0, 12, 65, 30, 135.20, NULL, NULL, 50.00),
(3, 1, 14, 400, 0, 18, 45, 15, 125.40, NULL, NULL, 35.50),
(4, 1, 12, 120, 20, 8, 10, 5, NULL, 6.80, 18.50, NULL),
(5, 1, 15, 300, 10, 7, 25, 10, 140.00, 7.50, 20.00, 30.00);

INSERT INTO Ball (Inning_ID, Bowler_ID, Batsman_ID, Non_striker_ID, Run_Scored, Is_Wicket, Is_NoBall, Is_Wide, Is_LegBye, Ball_Number)
VALUES 
(1, 4, 1, 3, 1, FALSE, FALSE, FALSE, FALSE, 1),
(1, 4, 2, 3, 0, TRUE, FALSE, FALSE, FALSE, 2),
(2, 5, 3, 2, 6, FALSE, FALSE, FALSE, FALSE, 1),
(2, 5, 1, 4, 1, FALSE, FALSE, FALSE, FALSE, 2),
(2, 4, 3, 2, 0, TRUE, FALSE, FALSE, FALSE, 3);

INSERT INTO TeamCaptain (Team_ID, Player_ID, Start_Date, End_Date)
VALUES 
(1, 2, '2013-01-01', NULL),
(2, 3, '2008-01-01', NULL),
(3, 1, '2013-01-01', NULL),
(5, 5, '2021-01-01', NULL),
(4, 1, '2020-01-01', NULL);
