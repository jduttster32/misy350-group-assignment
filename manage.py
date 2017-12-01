from flask_script import Manager
from myGroupProject import app, db, Player, Statistic

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()
