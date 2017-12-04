from flask_script import Manager
from myGroupProject import app, db, Player, Statistic

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    player1 = Player(name='James Dutton', height='6\'7\"', weight='219', position='PF')
    player2 = Player(name='Jack Jacobs', height='6\'1\"', weight='180', position='SG')
    player3 = Player(name='Matt Sidor', height='5\'9\"', weight='175', position='PG')
    stat1 = Statistic(fgp='67.3', threepp='34.3', prating='87', player=player1)
    stat2 = Statistic(fgp='73.8', threepp='37.8', prating='88', player=player2)
    stat3 = Statistic(fgp='65.2', threepp='29.7', prating='79', player=player3)
    db.session.add(player1)
    db.session.add(player2)
    db.session.add(player3)
    db.session.add(stat1)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
