from flask import Flask, request, render_template_string

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def main_page():
    return '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>풋볼 마스터 2024</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
        }
        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .hero-image {
            width: 90%;
            height: auto;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://pbs.twimg.com/media/F0BbWf6XoAELn6X.jpg:large" alt="Football Image" class="hero-image">
        <h1>풋볼 마스터 2024</h1>
        <a href="/euro_prediction" class="button">유로 예측하기</a>
        <a href="/asian_cup_prediction" class="button">아시안컵 예측하기</a>
        <a href="/nations_cup_prediction" class="button">네이션스컵 예측하기</a>
        <a href="/copa_america_prediction" class="button">코파 아메리카 예측하기</a>
    </div>
</body>
</html>
'''

# 유로 예측 페이지
@app.route('/euro_prediction')
def euro_prediction():
    return '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>풋볼 마스터 2024 - 유로 예측</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
        }
        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .hero-image {
            width: 50%;
            height: auto;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/26/UEFA_Euro_2024_Logo.svg/640px-UEFA_Euro_2024_Logo.svg.png" alt="Euro Prediction" class="hero-image">
        <h1>풋볼 마스터 2024 - 유로 예측</h1>
        <a href="/logistic_regression" class="button">예측하기</a>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
'''

# 아시안컵 예측 페이지
@app.route('/asian_cup_prediction')
def asian_cup_prediction():
    return '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>풋볼 마스터 2024 - 아시안컵 예측</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
        }
        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .hero-image {
            width: 30%;
            height: auto;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.namu.wiki/i/gDzYSnre7YXvW5PR3gGzvZab3q8zVj_bgp3G2kF-NfpN39b2hjOs40t5Wl6Me798c4GgDFWSgIp1FFYo2vI8rQy_Svq-HvywA9Crr7t9m36Argfis2fZzRRikd5Ixdjm_hn5d2rgiIcInwuAo794Zw.svg" alt="Asian Cup Prediction" class="hero-image">
        <h1>풋볼 마스터 2024 - 아시안컵 예측</h1>
        <a href="/logistic_regression" class="button">예측하기</a>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
'''

# 네이션스컵 예측 페이지
@app.route('/nations_cup_prediction')
def nations_cup_prediction():
    return '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>풋볼 마스터 2024 - 네이션스컵 예측</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
        }
        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .hero-image {
            width: 50%;
            height: auto;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.namu.wiki/i/r4NIHS0Ru0xuU8GK7uCZheLzYe46c43xKq3WgG_wa2YmXZ_wT_tqRMjNZxgDscUVnp90TAj5l-JWWhL5TaWxNA.webp" alt="Nations Cup Prediction" class="hero-image">
        <h1>풋볼 마스터 2024 - 네이션스컵 예측</h1>
        <a href="/logistic_regression" class="button">예측하기</a>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
'''

# 코파 아메리카 예측 페이지
@app.route('/copa_america_prediction')
def copa_america_prediction():
    return '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>풋볼 마스터 2024 - 코파 아메리카 예측</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
            
        }
        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .hero-image {
            width: 60%;
            height: auto;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.namu.wiki/i/5U_x2VXRC_4GR_lrLUdWrUzavbZlCBbiYXrtstTheXpOwzv9roxwmhrAa6X_e_X4ZzII-UlgtU5WjGLABCbcQw.webp" alt="Copa America Prediction" class="hero-image">
        <h1>풋볼 마스터 2024 - 코파 아메리카 예측</h1>
        <a href="/logistic_regression" class="button">예측하기</a>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
'''

@app.route('/logistic_regression')
def prediction_page():
    return render_template_string('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>예측</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
        }
        form div {
            margin-bottom: 15px;
            text-align: left;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .teams {
            display: flex;
            justify-content: space-between;
        }
        .team-input {
            width: 48%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>경기 예측</h1>
        <form action="/submit_teams" method="post">
            <div class="teams">
                <div class="team-input">
                    <label for="home_team">홈팀:</label>
                    <input type="text" id="home_team1" name="home_team1" required>
                </div>
                <div class="team-input">
                    <label for="away_team">어웨이팀:</label>
                    <input type="text" id="away_team1" name="away_team1" required>
                </div>
            </div>
            <button type="submit">제출</button>
        </form>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
''')

@app.route('/submit_teams', methods=['POST'])
def submit_teams():
    # 홈팀과 어웨이팀 이름 가져오기
    home_team1 = request.form.get("home_team1")
    away_team1 = request.form.get("away_team1")

    # 예측을 위한 데이터 준비
    teams = {
        "홈팀": home_team1,
        "어웨이팀": away_team1
    }
    
    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    from scipy.stats import poisson

    # Input data files are available in the read-only "../input/" directory
    # For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

    import os
    
    goal_scorers = 'C:/Users/hzin6/Downloads/goalscorers.csv'
    shootouts = 'C:/Users/hzin6/Downloads/shootouts.csv'
    results = 'C:/Users/hzin6/Downloads/results.csv'
    
    # 파일이 존재하는지 확인
    print(os.path.exists(goal_scorers))  # True이면 파일 존재, False이면 파일 없음
    print(os.path.exists(shootouts))
    print(os.path.exists(results))

    
    
    df_goal_scorers = pd.read_csv(goal_scorers)
    df_shootouts = pd.read_csv(shootouts)
    df_results = pd.read_csv(results)
    
    df_results.columns

    df_results['date'] = pd.to_datetime(df_results.date)
    
    df_results_1980 = df_results[df_results['date'].dt.year>=1980].reset_index(drop=True)
    
    df_results_1980.head()
    
    teams_2024 = ['Albania','Austria','Belgium','Croatia','Czech Republic','Denmark','England','France','Georgia','Germany','Hungary','Italy','Netherlands','Poland','Portugal','Romania','Scotland','Serbia','Slovakia','Slovenia','Spain','Switzerland','Turkey','Ukraine']
    
    df_na = df_results_1980.dropna()
    
    df_na.isna().sum()
    
    old_country_mapping = {'Czechoslovakia':'Czech Republic','West Germany':'Germany'}
    df_na['home_team'] = df_na['home_team'].map(lambda x: x.replace(x,old_country_mapping[x] if x in old_country_mapping else x))
    df_na['away_team'] = df_na['away_team'].map(lambda x: x.replace(x,old_country_mapping[x] if x in old_country_mapping else x))
    
    df_na = df_na[df_na['home_team'].isin(teams_2024)]
    df_na = df_na[df_na['away_team'].isin(teams_2024)]
    
    df_na.shape
    
    df_team_strength = df_na.groupby(['home_team']).agg({'home_score':'mean','away_score':'mean'})
    df_team_strength
    
    rankings = {'France':1840.59,'Belgium':1795.23,'England':1794.9,'Portugal':1748.11,'Netherlands':1742.29,'Spain':1727.5,'Italy':1724.6,'Croatia':1721.07,'Germany':1644.21,'Switzerland':1616.41,'Denmark':1602.72,'Ukraine':1568.86,'Austria':1554.86,'Hungary':1532.2,'Sweden':1531.68,'Poland':1531.49,'Wales':1531.38,'Serbia':1514.2,'Russia':1504.02,'Czech Republic':1501.47,'Scotland':1497.46,'Türkiye':1495.94,'Romania':1468.17,'Norway':1467.51,'Slovakia':1461.55,'Greece':1457.89,'Slovenia':1427.84,'Republic of Ireland':1399.74,'Finland':1394.44,'Albania':1375.1,'North Macedonia':1354.19,'Montenegro':1351.72,'Iceland':1346.82,'Northern Ireland':1341.05,'Bosnia and Herzegovina':1335.6,'Georgia':1333.76,'Israel':1311.39,'Bulgaria':1292.59,'Luxembourg':1277.94,'Armenia':1229.18,'Belarus':1226.54,'Kosovo':1205.85,'Kazakhstan':1203.64,'Azerbaijan':1177.83,'Estonia':1141.13,'Cyprus':1141.03,'Faroe Islands':1103.43,'Latvia':1095.91,'Lithuania':1095.23,'Moldova':1028.85,'Andorra':998.75,'Malta':973.14,'Liechtenstein':832.75,'Gibraltar':832.5,'San Marino':742.05}
    euro_rankings = {}
    for key,val in rankings.items():
        if key in teams_2024:
            euro_rankings[key] = val
            
    euro_rankings
            
    max_val = max(euro_rankings.values())
    for key,val in euro_rankings.items():
        
        euro_rankings[key] = val/max_val
        
    euro_rankings
        
    def predict_points(home, away):
        if home in df_team_strength.index and away in df_team_strength.index:
            # goals_scored * goals_conceded
            lamb_home = df_team_strength.at[home,'home_score'] * df_team_strength.at[away,'away_score']
            lamb_away = df_team_strength.at[away,'home_score'] * df_team_strength.at[home,'away_score']
            prob_home, prob_away, prob_draw = 0, 0, 0
            for x in range(0,11): #number of goals home team
                for y in range(0, 11): #number of goals away team
                    p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
                    if x == y:
                        prob_draw += p
                    elif x > y:
                        prob_home += p
                    else:
                        prob_away += p
            
            points_home = euro_rankings[home] * prob_home + prob_draw
            points_away = euro_rankings[away] * prob_away + prob_draw
            return (points_home, points_away)
        else:
            return (0, 0)
        
    prediction_result = predict_points(home_team1, away_team1)
    
    # 승리/무승부 판단 로직 추가
    home_points, away_points = prediction_result
    if home_points >= 0.6:
        match_result = f"{home_team1} 승리"
    elif away_points >= 0.6:
        match_result = f"{away_team1} 승리"
    elif abs(home_points - away_points) < 1e-5:  # 두 점수가 거의 같을 때
        match_result = "무승부"
    else:
        match_result = "결과를 판단할 수 없습니다."

    return render_template_string('''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>예측 결과</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 80%;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007BFF;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            padding: 8px 0;
            border-bottom: 1px solid #ddd;
        }
        .button {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>예측 결과</h1>
        <h2>입력한 팀들:</h2>
        <ul>
            <li>홈팀: {{ teams["홈팀"] }}</li>
            <li>어웨이팀: {{ teams["어웨이팀"] }}</li>
        </ul>
        
        <h3>예측 점수:</h3>
        <ul>
            <li>{{ teams["홈팀"] }} 예측 점수: {{ home_points }}</li>
            <li>{{ teams["어웨이팀"] }} 예측 점수: {{ away_points }}</li>
        </ul>

        <h3>최종 결과: {{ match_result }}</h3>
        
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
''', teams=teams, home_points=home_points, away_points=away_points, match_result=match_result)
if __name__ == '__main__':
    app.run(debug=True)
