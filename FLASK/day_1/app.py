from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 템플릿에 전달할 데이터
    users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "백엔드 개발자", "name": "근우"},
    {"username": "gourmet", "name": "Chris"}
]

    # render_template을 사용하여 템플릿 파일을 렌더링
    # rendering 할 html 파일명 입력
    # html로 넘겨줄때 데이터 입력
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)