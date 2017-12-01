from flask_script import Manager
from myGroupProject import app, db, Player, Statistic

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    player1 = Player(name='James Dutton', height='6\'7\"', weight='219', position='PF')
    player2 = Player(name='Jack Jacobs', height='6\'1\"', weight='180', position='SG')
    db.session.add(player1)
    db.session.add(player2)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
