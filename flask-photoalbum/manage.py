from flask_script import Manager
from project import create_app, db
import unittest
from project.api.models import Album, Image


app = create_app()
manager = Manager(app)

@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def seed_db():
    """Seeds the database."""
    img1 = Image(img='pigs3.jpg')
    img2 = Image(img='pigs4.jpg')
    img3 = Image(img='pigs7.jpg')
    img4 = Image(img='pigs8.jpg')
    album1 = Album(title='polina', description="Polina's album with many awesome pictures.", images=img1)
    album2 = Album(title='pofi', description="Pofi's cute pictures.", images=img2)
    # img3.albums.append(album1)
    # img4.albums.append(album2)
    db.session.add(album1)
    db.session.add(album2)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
