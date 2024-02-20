from .models import Matches, Matches1516, Matches1617, Matches1718, Matches1819
from . import db, ma


# -------------------------
# Flask-Marshmallow Schemas
# See https://marshmallow-sqlalchemy.readthedocs.io/en/latest/#generate-marshmallow-schemas
# -------------------------


class MatchesSchema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating matches."""

    class Meta:
        model = Matches
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    HomeTeam = ma.auto_field()
    AwayTeam = ma.auto_field()
    FTHG = ma.auto_field()
    FTAG = ma.auto_field()
    FTR = ma.auto_field()
    HS = ma.auto_field()
    AS = ma.auto_field()
    HST = ma.auto_field()
    AST = ma.auto_field()
    id = ma.auto_field()


class Matches1516Schema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating matches."""

    class Meta:
        model = Matches1516
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    HomeTeam = ma.auto_field()
    AwayTeam = ma.auto_field()
    FTHG = ma.auto_field()
    FTAG = ma.auto_field()
    FTR = ma.auto_field()
    HS = ma.auto_field()
    AS = ma.auto_field()
    HST = ma.auto_field()
    AST = ma.auto_field()
    id = ma.auto_field()


class Matches1617Schema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating matches."""

    class Meta:
        model = Matches1617
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    HomeTeam = ma.auto_field()
    AwayTeam = ma.auto_field()
    FTHG = ma.auto_field()
    FTAG = ma.auto_field()
    FTR = ma.auto_field()
    HS = ma.auto_field()
    AS = ma.auto_field()
    HST = ma.auto_field()
    AST = ma.auto_field()
    id = ma.auto_field()


class Matches1718Schema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating matches."""

    class Meta:
        model = Matches1718
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    HomeTeam = ma.auto_field()
    AwayTeam = ma.auto_field()
    FTHG = ma.auto_field()
    FTAG = ma.auto_field()
    FTR = ma.auto_field()
    HS = ma.auto_field()
    AS = ma.auto_field()
    HST = ma.auto_field()
    AST = ma.auto_field()
    id = ma.auto_field()


class Matches1819Schema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating matches."""

    class Meta:
        model = Matches1819
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    HomeTeam = ma.auto_field()
    AwayTeam = ma.auto_field()
    FTHG = ma.auto_field()
    FTAG = ma.auto_field()
    FTR = ma.auto_field()
    HS = ma.auto_field()
    AS = ma.auto_field()
    HST = ma.auto_field()
    AST = ma.auto_field()
    id = ma.auto_field()
