from flask import Flask, render_template, url_for, request, jsonify, redirect
import os
import main

app=Flask(__name__, template_folder='templates')

def get_states():
    with open("output_15:44:20.txt",'r') as f:
        f.read()


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    moves = [{'move' : None}]
    pos_x = 0
    pos_y = 0
    init_state=""
    if request.method == 'POST':
        init_state = request.values['initial_state']
        algo = request.form.get("selection")
        # init_state = init_state[-1:len(init_state)-8]
        # request.values['initial_state'] = None

        if init_state != '':
            try:
                moves = { 'move' : ",".join(main.main(algorithm=algo, board=init_state))}
                pos_x = str(init_state).split(',').index('0')%3
                pos_y = str(init_state).split(',').index('0')//3
            except Exception as e:
                print("Exception: ", e)
                return render_template('index.html', m={'move':'None'}
                                       , i_s={'init_state': init_state.split(',')},
                                       pos={'pos_x': pos_x, 'pos_y': pos_y})

        print(moves)
    return render_template('index.html',m = moves, i_s = {'init_state':init_state.split(',')},
                           pos={'pos_x':pos_x, 'pos_y':pos_y})




if __name__ == '__main__':
    app.debug = True
    app.run(debug=False, host='0.0.0.0', port='5000')


