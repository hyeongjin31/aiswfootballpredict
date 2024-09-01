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
        <a href="/logistic_regression" class="button">로지스틱 회귀 모델을 통한 예측</a>
        <a href="/random_forest" class="button">랜덤포레스트를 통한 예측</a>
        <a href="/xgboost" class="button">XGboost를 통한 예측</a>
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
        <a href="/logistic_regression" class="button">로지스틱 회귀 모델을 통한 예측</a>
        <a href="/random_forest" class="button">랜덤포레스트를 통한 예측</a>
        <a href="/xgboost" class="button">XGboost를 통한 예측</a>
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
        <a href="/logistic_regression" class="button">로지스틱 회귀 모델을 통한 예측</a>
        <a href="/random_forest" class="button">랜덤포레스트를 통한 예측</a>
        <a href="/xgboost" class="button">XGboost를 통한 예측</a>
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
        <a href="/logistic_regression" class="button">로지스틱 회귀 모델을 통한 예측</a>
        <a href="/random_forest" class="button">랜덤포레스트를 통한 예측</a>
        <a href="/xgboost" class="button">XGboost를 통한 예측</a>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
'''

# 예측 페이지 (로지스틱 회귀, 랜덤포레스트, XGboost)
@app.route('/logistic_regression')
@app.route('/random_forest')
@app.route('/xgboost')
def prediction_page():
    model_type = request.path.strip('/').replace('_', ' ').title()
    groups = ['A', 'B', 'C', 'D', 'E', 'F']
    return render_template_string('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ model_type }} 예측</title>
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
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ model_type }} 예측</h1>
        <form action="/submit_teams/{{ model_type }}" method="post">
            {% for group in groups %}
                <h2>조 {{ group }}</h2>
                {% for i in range(4) %}
                    <div>
                        <label for="team{{ i + (groups.index(group) * 4) + 1 }}">팀 {{ i + (groups.index(group) * 4) + 1 }}:</label>
                        <input type="text" id="team{{ i + (groups.index(group) * 4) + 1 }}" name="team{{ i + (groups.index(group) * 4) + 1 }}" required>
                    </div>
                {% endfor %}
            {% endfor %}
            <button type="submit">제출</button>
        </form>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
''', model_type=model_type, groups=groups)

# 제출 완료 페이지
@app.route('/submit_teams/<model_type>', methods=['POST'])
def submit_teams(model_type):
    teams = {}
    for i in range(1, 25):
        team_name = request.form.get(f"team{i}")
        if team_name:
            teams[f"팀 {i}"] = team_name
    
    return render_template_string('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>제출 완료</title>
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
        <h1>{{ model_type }} - 제출 완료</h1>
        <h2>입력한 팀들:</h2>
        <ul>
            {% for team, name in teams.items() %}
                <li>{{ team }}: {{ name }}</li>
            {% endfor %}
        </ul>
        <a href="/" class="button">메인 페이지로 돌아가기</a>
    </div>
</body>
</html>
''', model_type=model_type, teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
