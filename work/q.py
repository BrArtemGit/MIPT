import datetime
import sqlalchemy
import sqlalchemy.orm as dec

SqlAlchemyBase = dec.declarative_base()


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # user = orm.relationship('User')

    def __repr__(self):
        return (f'{self.id} {self.team_leader} {self.job} {self.work_size} {self.collaborators} {self.start_date}'
                f' {self.end_date} {self.is_finished}')
