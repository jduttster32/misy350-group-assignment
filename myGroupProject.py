import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    position = db.Column(db.String(64))
    statistics = db.relationship('Statistic', backref='player')

class Statistic(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    fgp = db.Column(db.Integer)
    threepp = db.Column(db.Integer)
    prating = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))


@app.route('/')
def home():
    #return '<h1>Welcome to James first server. Thanks for checking it out.</h1>'
    return render_template('index.html')

@app.route('/players')
def show_all_players():
    players = Player.query.all()
    return render_template('player-all.html', players=players)

@app.route('/player/add', methods=['GET', 'POST'])
def add_players():
    if request.method == 'GET':
        return render_template('player-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        position = request.form['position']
        # insert the data into the database
        player = Player(name=name, height=height, weight=weight, position=position)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('show_all_players'))

@app.route('/api/player/add', methods=['POST'])
def add_ajax_players():
    # get data from the form
    name = request.form['name']
    height = request.form['height']
    weight = request.form['weight']
    position = request.form['position']

    player = Player(name=name, height=height, weight=weight, position=position)
    db.session.add(player)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Player Inserted', 'success')
    return jsonify({"id": str(player.id), "name": player.name})

@app.route('/player/edit/<int:id>', methods=['GET', 'POST'])
def edit_player(id):
    player = Player.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('player-edit.html', player=player)
    if request.method == 'POST':
        # update data based on the form data
        player.name = request.form['name']
        player.height = request.form['height']
        player.weight = request.form['weight']
        player.position = request.form['position']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_players'))

@app.route('/player/delete/<int:id>', methods=['GET', 'POST'])
def delete_player(id):
    player = Player.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('player-delete.html', player=player)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(player)
        db.session.commit()
        return redirect(url_for('show_all_players'))

@app.route('/api/player/<int:id>', methods=['DELETE'])
def delete_ajax_player(id):
    player = Player.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    return jsonify({"id": str(player.id), "name": player.name})

@app.route('/statistics')
def show_all_statistics():
    statistics = Statistic.query.all()
    return render_template('statistic-all.html', statistics=statistics)

@app.route('/statistic/add', methods=['GET', 'POST'])
def add_statistics():
    if request.method == 'GET':
        players = Player.query.all()
        return render_template('statistic-add.html', players=players)
    if request.method == 'POST':
        # get data from the form
        fgp = request.form['fgp']
        threepp = request.form['threepp']
        prating = request.form['prating']
        player_name = request.form['player']
        player = Player.query.filter_by(name=player_name).first()
        statistic = Statistic( fgp=fgp, threepp=threepp, prating=prating, player=player)

        # insert the data into the database
        db.session.add(statistic)
        db.session.commit()
        return redirect(url_for('show_all_statistics'))


@app.route('/statistic/edit/<int:id>', methods=['GET', 'POST'])
def edit_stat(id):
    statistic = Statistic.query.filter_by(id=id).first()
    players = Player.query.all()
    if request.method == 'GET':
        return render_template('statistic-edit.html', statistic=statistic, players=players)
    if request.method == 'POST':
        # update data based on the form data
        statistic.fgp = request.form['fgp']
        statistic.threepp = request.form['threepp']
        statistic.prating = request.form['prating']
        player_name = request.form['player']
        player = Player.query.filter_by(name=player_name).first()
        statistic.player = player
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_statistics'))

@app.route('/statistic/delete/<int:id>', methods=['GET', 'POST'])
def delete_statistic(id):
    statistic = Statistic.query.filter_by(id=id).first()
    players = Player.query.all()
    if request.method == 'GET':
        return render_template('statistic-delete.html', statistic=statistic, players=players)
    if request.method == 'POST':
        # use the id to delete the song
        # song.query.filter_by(id=id).delete()
        db.session.delete(statistic)
        db.session.commit()
        return redirect(url_for('show_all_statistics'))

@app.route('/api/statistic/<int:id>', methods=['DELETE'])
def delete_ajax_stats(id):
    statistic = Statistic.query.get_or_404(id)
    db.session.delete(statistic)
    db.session.commit()
    return jsonify({"id": str(statistic.id), "name": statistic.player.name})

@app.route('/members')
def get_member():
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('members.html')


if __name__ == "__main__":
    app.run(debug=True);
