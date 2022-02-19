import sys
sys.path.append("..")

from flask import Blueprint, request, render_template, redirect, url_for, json, jsonify
from ast import literal_eval
from static.src.rule import ruleData # get rule-base 

chatBotAPI = Blueprint('postsAPI', __name__, template_folder='templates')

@chatBotAPI.route('/', methods=['GET','POST'])
def base():
    if request.method == 'GET':
        return render_template('welcome.html')
    
    if request.method == 'POST':
        data = request.get_json()
        data = json.dumps({'msg':ruleData(data['msg'])}, ensure_ascii=False)
        data = literal_eval(data)
        return jsonify(result = "success", result2 = data)
