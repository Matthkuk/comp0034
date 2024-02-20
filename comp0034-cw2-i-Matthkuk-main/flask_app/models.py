from . import db


class Matches(db.Model):
    __tablename__ = "Matches"
    HomeTeam = db.Column(db.Text, nullable=False)
    AwayTeam = db.Column(db.Text, nullable=False)
    FTHG = db.Column(db.Integer,)
    FTAG = db.Column(db.Integer,)
    FTR = db.Column(db.Text, nullable=False)
    HS = db.Column(db.Integer,)
    AS = db.Column(db.Integer,)
    HST = db.Column(db.Integer,)
    AST = db.Column(db.Integer,)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.HomeTeam} vs {self.AwayTeam}>"


class Matches1516(db.Model):
    __bind_key__ = '1516'
    __tablename__ = "Matches"
    HomeTeam = db.Column(db.Text, nullable=False)
    AwayTeam = db.Column(db.Text, nullable=False)
    FTHG = db.Column(db.Integer,)
    FTAG = db.Column(db.Integer,)
    FTR = db.Column(db.Text, nullable=False)
    HS = db.Column(db.Integer,)
    AS = db.Column(db.Integer,)
    HST = db.Column(db.Integer,)
    AST = db.Column(db.Integer,)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.HomeTeam} vs {self.AwayTeam}>"


class Matches1617(db.Model):
    __bind_key__ = '1617'
    __tablename__ = "Matches"
    HomeTeam = db.Column(db.Text, nullable=False)
    AwayTeam = db.Column(db.Text, nullable=False)
    FTHG = db.Column(db.Integer,)
    FTAG = db.Column(db.Integer,)
    FTR = db.Column(db.Text, nullable=False)
    HS = db.Column(db.Integer,)
    AS = db.Column(db.Integer,)
    HST = db.Column(db.Integer,)
    AST = db.Column(db.Integer,)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.HomeTeam} vs {self.AwayTeam}>"


class Matches1718(db.Model):
    __bind_key__ = '1718'
    __tablename__ = "Matches"
    HomeTeam = db.Column(db.Text, nullable=False)
    AwayTeam = db.Column(db.Text, nullable=False)
    FTHG = db.Column(db.Integer,)
    FTAG = db.Column(db.Integer,)
    FTR = db.Column(db.Text, nullable=False)
    HS = db.Column(db.Integer,)
    AS = db.Column(db.Integer,)
    HST = db.Column(db.Integer,)
    AST = db.Column(db.Integer,)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.HomeTeam} vs {self.AwayTeam}>"


class Matches1819(db.Model):
    __bind_key__ = '1819'
    __tablename__ = "Matches"
    HomeTeam = db.Column(db.Text, nullable=False)
    AwayTeam = db.Column(db.Text, nullable=False)
    FTHG = db.Column(db.Integer,)
    FTAG = db.Column(db.Integer,)
    FTR = db.Column(db.Text, nullable=False)
    HS = db.Column(db.Integer,)
    AS = db.Column(db.Integer,)
    HST = db.Column(db.Integer,)
    AST = db.Column(db.Integer,)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.HomeTeam} vs {self.AwayTeam}>"
