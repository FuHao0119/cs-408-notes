from flask import Flask, render_template, request, redirect, url_for, session
import random
from formula_data import data  # 导入题库

app = Flask(__name__)
# 必须设置密钥才能使用 session，这里随便写一个字符串即可
app.secret_key = 'math_master_2026_secret_key'

@app.route('/')
def index():
    """欢迎页：显示开始按钮"""
    # 清除之前的进度，准备新开始
    session.clear()
    return render_template('welcome.html', total_count=len(data))

@app.route('/start')
def start_quiz():
    """初始化逻辑：随机抽取10道题"""
    # 设定题目数量，默认10道，如果题库不够则全选
    quiz_count = 10
    total_questions = len(data)
    real_count = min(quiz_count, total_questions)

    # 随机抽取 real_count 个不重复的索引
    selected_indices = random.sample(range(total_questions), real_count)

    # 将数据存入 session (类似于浏览器的临时缓存)
    session['quiz_indices'] = selected_indices # 题目ID列表
    session['current_step'] = 0                # 当前做到第几题 (0开始)
    session['total_steps'] = real_count        # 总题数

    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    """做题页面"""
    # 如果没有开始过，踢回首页
    if 'quiz_indices' not in session:
        return redirect(url_for('index'))

    step = session['current_step']
    indices = session['quiz_indices']
    total = session['total_steps']

    # 如果已经做完所有题，跳转到结束页
    if step >= total:
        return redirect(url_for('finish'))

    # 获取当前题目的数据
    question_id = indices[step]
    problem = data[question_id]

    return render_template('quiz.html', 
                           problem=problem, 
                           current=step + 1, 
                           total=total)

@app.route('/next')
def next_question():
    """进入下一题的逻辑"""
    if 'current_step' in session:
        session['current_step'] += 1
    return redirect(url_for('quiz'))

@app.route('/finish')
def finish():
    """结束页面"""
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
