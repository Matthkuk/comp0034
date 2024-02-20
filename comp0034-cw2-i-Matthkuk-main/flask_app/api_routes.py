from flask import Blueprint, jsonify, make_response, request, render_template, abort, redirect, flash
from .models import Matches, Matches1516, Matches1617, Matches1718, Matches1819
from . import db
from .schemas import MatchesSchema, Matches1516Schema, Matches1617Schema, Matches1718Schema, Matches1819Schema


# -------
# Schemas
# -------

Matches_schema = MatchesSchema(many=True)
Match_schema = MatchesSchema()

Matches1516_schema = Matches1516Schema(many=True)
Match1516_schema = Matches1516Schema()

Matches1617_schema = Matches1617Schema(many=True)
Match1617_schema = Matches1617Schema()

Matches1718_schema = Matches1718Schema(many=True)
Match1718_schema = Matches1718Schema()

Matches1819_schema = Matches1819Schema(many=True)
Match1819_schema = Matches1819Schema()

bp = Blueprint("api", __name__, url_prefix="/api")
main_bp = Blueprint('main', __name__)

# -------
# All GET request
# -------


@bp.route('/matches')
def matches():
    result = get_matches()
    # Return the data
    return result


@bp.route('/matches1516')
def matches1516():
    result = get_matches1516()
    # Return the data
    return result


@bp.route('/matches1617')
def matches1617():
    result = get_matches1617()
    # Return the data
    return result


@bp.route('/matches1718')
def matches1718():
    result = get_matches1718()
    # Return the data
    return result


@bp.route('/matches1819')
def matches1819():
    result = get_matches1819()
    # Return the data
    return result

# -------
# Single GET request
# -------


@bp.get("/matches/<int:id>")
def team(id):
    team = db.session.execute(
        db.select(Matches).where(Matches.id == id)
    ).scalars()
    return Matches_schema.dump(team)


@bp.get("/matches1516/<int:id>")
def team1516(id):
    team = db.session.execute(
        db.select(Matches1516).where(Matches1516.id == id)
    ).scalars()
    return Matches_schema.dump(team)


@bp.get("/matches1617/<int:id>")
def team1617(id):
    team = db.session.execute(
        db.select(Matches1617).where(Matches1617.id == id)
    ).scalars()
    return Matches_schema.dump(team)


@bp.get("/matches1718/<int:id>")
def team1718(id):
    team = db.session.execute(
        db.select(Matches1718).where(Matches1718.id == id)
    ).scalars()
    return Matches_schema.dump(team)


@bp.get("/matches1819/<int:id>")
def team1819(id):
    team = db.session.execute(
        db.select(Matches1819).where(Matches1819.id == id)
    ).scalars()
    return Matches_schema.dump(team)

# -------
# DELETE request
# -------


@bp.delete("/matches/<int:id>")
def match_delete(id):
    # Query the database to find the record, return a 404 not found code it the record isn't found
    match = db.session.execute(
        db.select(Matches).filter_by(id=id)
    ).scalar_one_or_none()
    if match is None:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    # Delete the record you found
    db.session.delete(match)
    db.session.commit()
    # Return a JSON HTTP response to let the person know it was deleted
    text = jsonify({"Successfully deleted": id})
    response = make_response(text, 200)
    response.headers["Content-type"] = "application/json"
    return response


@bp.delete("/matches1516/<int:id>")
def match1516_delete(id):
    # Query the database to find the record, return a 404 not found code it the record isn't found
    match = db.session.execute(
        db.select(Matches1516).filter_by(id=id)
    ).scalar_one_or_none()
    if match is None:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    # Delete the record you found
    db.session.delete(match)
    db.session.commit()
    # Return a JSON HTTP response to let the person know it was deleted
    text = jsonify({"Successfully deleted": id})
    response = make_response(text, 200)
    response.headers["Content-type"] = "application/json"
    return response


@bp.delete("/matches1617/<int:id>")
def match1617_delete(id):
    # Query the database to find the record, return a 404 not found code it the record isn't found
    match = db.session.execute(
        db.select(Matches1617).filter_by(id=id)
    ).scalar_one_or_none()
    if match is None:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    # Delete the record you found
    db.session.delete(match)
    db.session.commit()
    # Return a JSON HTTP response to let the person know it was deleted
    text = jsonify({"Successfully deleted": id})
    response = make_response(text, 200)
    response.headers["Content-type"] = "application/json"
    return response


@bp.delete("/matches1718/<int:id>")
def match1718_delete(id):
    # Query the database to find the record, return a 404 not found code it the record isn't found
    match = db.session.execute(
        db.select(Matches1718).filter_by(id=id)
    ).scalar_one_or_none()
    if match is None:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    # Delete the record you found
    db.session.delete(match)
    db.session.commit()
    # Return a JSON HTTP response to let the person know it was deleted
    text = jsonify({"Successfully deleted": id})
    response = make_response(text, 200)
    response.headers["Content-type"] = "application/json"
    return response


@bp.delete("/matches1819/<int:id>")
def match1819_delete(id):
    # Query the database to find the record, return a 404 not found code it the record isn't found
    match = db.session.execute(
        db.select(Matches1819).filter_by(id=id)
    ).scalar_one_or_none()
    if match is None:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    # Delete the record you found
    db.session.delete(match)
    db.session.commit()
    # Return a JSON HTTP response to let the person know it was deleted
    text = jsonify({"Successfully deleted": id})
    response = make_response(text, 200)
    response.headers["Content-type"] = "application/json"
    return response

# -------
# POST request
# -------


@bp.post("/matches/<int:id>")
def match_add(id):
    # Get the values of the JSON sent in the request
    match = getting_json(id)
    # Save the new match to the database or error
    selected_id = db.session.execute(
        db.select(Matches).filter_by(id=match.id)
    ).scalar_one_or_none()
    if selected_id is None:
        try:
            db.session.add(match)
            db.session.commit()
            result = Match_schema.jsonify(match)
        except ValueError:
            flash('ValueError - Maybe you entered a letter into a numeric field?')
            db.session.delete(match)
            db.session.commit()
            abort(400)
    else:
        flash('Error 403: Forbidden - There is already an entry here, maybe you tried the wrong id?')
        abort(403)
    return result


@bp.post("/matches1516/<int:id>")
def match1516_add(id):
    # Get the values of the JSON sent in the request
    match = getting_json1516(id)
    # Save the new match to the database or error
    selected_id = db.session.execute(
        db.select(Matches1516).filter_by(id=match.id)
    ).scalar_one_or_none()
    if selected_id is None:
        try:
            db.session.add(match)
            db.session.commit()
            result = Match_schema.jsonify(match)
        except ValueError:
            flash('ValueError - Maybe you entered a letter into a numeric field?')
            db.session.delete(match)
            db.session.commit()
            abort(400)
    else:
        flash('Error 403: Forbidden - There is already an entry here, maybe you tried the wrong id?')
        abort(403)
    return result


@bp.post("/matches1617/<int:id>")
def match1617_add(id):
    # Get the values of the JSON sent in the request
    match = getting_json1617(id)
    # Save the new match to the database or error
    selected_id = db.session.execute(
        db.select(Matches1617).filter_by(id=match.id)
    ).scalar_one_or_none()
    if selected_id is None:
        try:
            db.session.add(match)
            db.session.commit()
            result = Match_schema.jsonify(match)
        except ValueError:
            flash('ValueError - Maybe you entered a letter into a numeric field?')
            db.session.delete(match)
            db.session.commit()
            abort(400)
    else:
        flash('Error 403: Forbidden - There is already an entry here, maybe you tried the wrong id?')
        abort(403)
    return result


@bp.post("/matches1718/<int:id>")
def match1718_add(id):
    # Get the values of the JSON sent in the request
    match = getting_json1718(id)
    # Save the new match to the database or error
    selected_id = db.session.execute(
        db.select(Matches1718).filter_by(id=match.id)
    ).scalar_one_or_none()
    if selected_id is None:
        try:
            db.session.add(match)
            db.session.commit()
            result = Match_schema.jsonify(match)
        except ValueError:
            flash('ValueError - Maybe you entered a letter into a numeric field?')
            db.session.delete(match)
            db.session.commit()
            abort(400)
    else:
        flash('Error 403: Forbidden - There is already an entry here, maybe you tried the wrong id?')
        abort(403)
    return result


@bp.post("/matches1819/<int:id>")
def match1819_add(id):
    """Adds a new NOC record to the dataset."""
    # Get the values of the JSON sent in the request
    match = getting_json1819(id)
    # Save the new match to the database or error
    selected_id = db.session.execute(
        db.select(Matches1819).filter_by(id=match.id)
    ).scalar_one_or_none()
    if selected_id is None:
        try:
            db.session.add(match)
            db.session.commit()
            result = Match_schema.jsonify(match)
        except ValueError:
            flash('ValueError - Maybe you entered a letter into a numeric field?')
            db.session.delete(match)
            db.session.commit()
            abort(400)
    else:
        flash('Error 403: Forbidden - There is already an entry here, maybe you tried the wrong id?')
        abort(403)
    return result

# -------
# PATCH
# -------


@bp.patch("/matches/<int:id>")
def match_update(id):
    existing_match = db.session.execute(
        db.select(Matches).filter_by(id=id)
    ).scalar_one_or_none()
    # Get the updated details from the json sent in the HTTP patch request
    match = getting_json(id)
    try:
        db.session.delete(existing_match)
    except Exception:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    db.session.add(match)
    db.session.commit()
    # Return json showing the updated record
    updated_match = db.session.execute(
        db.select(Matches).filter_by(id=id)
    ).scalar_one_or_none()
    try:
        result = Match_schema.jsonify(updated_match)
    except ValueError:
        flash("Error Code: 400 Bad Request - Maybe you didn't fill in or incorrectly filled an entry?")
        if updated_match is not None:
            db.session.delete(updated_match)
            db.session.commit()
        abort(400)
    except Exception:
        abort(500)
    return result


@bp.patch("/matches1516/<int:id>")
def match1516_update(id):
    existing_match = db.session.execute(
        db.select(Matches1516).filter_by(id=id)
    ).scalar_one_or_none()
    # Get the updated details from the json sent in the HTTP patch request
    match = getting_json1516(id)
    try:
        db.session.delete(existing_match)
    except Exception:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    db.session.add(match)
    db.session.commit()
    # Return json showing the updated record
    updated_match = db.session.execute(
        db.select(Matches1516).filter_by(id=id)
    ).scalar_one_or_none()
    try:
        result = Match1516_schema.jsonify(updated_match)
    except ValueError:
        flash("Error Code: 400 Bad Request - Maybe you didn't fill in or incorrectly filled an entry?")
        if updated_match is not None:
            db.session.delete(updated_match)
            db.session.commit()
        abort(400)
    except Exception:
        abort(500)
    return result


@bp.patch("/matches1617/<int:id>")
def match1617_update(id):
    existing_match = db.session.execute(
        db.select(Matches1617).filter_by(id=id)
    ).scalar_one_or_none()
    # Get the updated details from the json sent in the HTTP patch request
    match = getting_json1617(id)
    try:
        db.session.delete(existing_match)
    except Exception:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    db.session.add(match)
    db.session.commit()
    # Return json showing the updated record
    updated_match = db.session.execute(
        db.select(Matches1617).filter_by(id=id)
    ).scalar_one_or_none()
    try:
        result = Match1617_schema.jsonify(updated_match)
    except ValueError:
        flash("Error Code: 400 Bad Request - Maybe you didn't fill in or incorrectly filled an entry?")
        if updated_match is not None:
            db.session.delete(updated_match)
            db.session.commit()
        abort(400)
    except Exception:
        abort(500)
    return result


@bp.patch("/matches1718/<int:id>")
def match1718_update(id):
    existing_match = db.session.execute(
        db.select(Matches1718).filter_by(id=id)
    ).scalar_one_or_none()
    # Get the updated details from the json sent in the HTTP patch request
    match = getting_json1718(id)
    try:
        db.session.delete(existing_match)
    except Exception:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    db.session.add(match)
    db.session.commit()
    # Return json showing the updated record
    updated_match = db.session.execute(
        db.select(Matches1718).filter_by(id=id)
    ).scalar_one_or_none()
    try:
        result = Match1718_schema.jsonify(updated_match)
    except ValueError:
        flash("Error Code: 400 Bad Request - Maybe you didn't fill in or incorrectly filled an entry?")
        if updated_match is not None:
            db.session.delete(updated_match)
            db.session.commit()
        abort(400)
    except Exception:
        abort(500)
    return result


@bp.patch("/matches1819/<int:id>")
def match1819_update(id):
    existing_match = db.session.execute(
        db.select(Matches1819).filter_by(id=id)
    ).scalar_one_or_none()
    # Get the updated details from the json sent in the HTTP patch request
    match = getting_json1819(id)
    try:
        db.session.delete(existing_match)
    except Exception:
        flash('Error 404: Not found - This page is empty.')
        abort(404)
    db.session.add(match)
    db.session.commit()
    # Return json showing the updated record
    updated_match = db.session.execute(
        db.select(Matches1819).filter_by(id=id)
    ).scalar_one_or_none()
    try:
        result = Match1819_schema.jsonify(updated_match)
    except ValueError:
        flash("Error Code: 400 Bad Request - Maybe you didn't fill in or incorrectly filled an entry?")
        if updated_match is not None:
            db.session.delete(updated_match)
            db.session.commit()
        abort(400)
    except Exception:
        abort(500)
    return result


@main_bp.route("/")
def index():
    return render_template("index.html")


def get_matches():
    # Select all the matches using Flask-SQLAlchemy
    all_matches = db.session.execute(db.select(Matches)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = Matches_schema.dump(all_matches)
    # Return the data
    return result


def get_matches1516():
    # Select all the matches using Flask-SQLAlchemy
    all_matches = db.session.execute(db.select(Matches1516)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = Matches1516_schema.dump(all_matches)
    # Return the data
    return result


def get_matches1617():
    # Select all the matches using Flask-SQLAlchemy
    all_matches = db.session.execute(db.select(Matches1617)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = Matches1617_schema.dump(all_matches)
    # Return the data
    return result


def get_matches1718():
    # Select all the matches using Flask-SQLAlchemy
    all_matches = db.session.execute(db.select(Matches1718)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = Matches1516_schema.dump(all_matches)
    # Return the data
    return result


def get_matches1819():
    # Select all the matches using Flask-SQLAlchemy
    all_matches = db.session.execute(db.select(Matches1819)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = Matches1516_schema.dump(all_matches)
    # Return the data
    return result


def getting_json(id):
    HomeTeam = request.json.get("HomeTeam", "")
    AwayTeam = request.json.get("AwayTeam", "")
    FTHG = request.json.get("FTHG", "")
    FTAG = request.json.get("FTAG", "")
    HS = request.json.get("HS", "")
    AS = request.json.get("AS", "")
    FTR = request.json.get("FTR", "")
    HST = request.json.get("HST", "")
    AST = request.json.get("AST", "")
    match = Matches(HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG,
                    FTAG=FTAG, HS=HS, AS=AS, id=id, FTR=FTR, HST=HST, AST=AST)
    return match


def getting_json1516(id):
    HomeTeam = request.json.get("HomeTeam", "")
    AwayTeam = request.json.get("AwayTeam", "")
    FTHG = request.json.get("FTHG", "")
    FTAG = request.json.get("FTAG", "")
    HS = request.json.get("HS", "")
    AS = request.json.get("AS", "")
    FTR = request.json.get("FTR", "")
    HST = request.json.get("HST", "")
    AST = request.json.get("AST", "")
    match = Matches1516(HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG,
                        FTAG=FTAG, HS=HS, AS=AS, id=id, FTR=FTR, HST=HST, AST=AST)
    return match


def getting_json1617(id):
    HomeTeam = request.json.get("HomeTeam", "")
    AwayTeam = request.json.get("AwayTeam", "")
    FTHG = request.json.get("FTHG", "")
    FTAG = request.json.get("FTAG", "")
    HS = request.json.get("HS", "")
    AS = request.json.get("AS", "")
    FTR = request.json.get("FTR", "")
    HST = request.json.get("HST", "")
    AST = request.json.get("AST", "")
    match = Matches1617(HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG,
                        FTAG=FTAG, HS=HS, AS=AS, id=id, FTR=FTR, HST=HST, AST=AST)
    return match


def getting_json1718(id):
    HomeTeam = request.json.get("HomeTeam", "")
    AwayTeam = request.json.get("AwayTeam", "")
    FTHG = request.json.get("FTHG", "")
    FTAG = request.json.get("FTAG", "")
    HS = request.json.get("HS", "")
    AS = request.json.get("AS", "")
    FTR = request.json.get("FTR", "")
    HST = request.json.get("HST", "")
    AST = request.json.get("AST", "")
    match = Matches1718(HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG,
                        FTAG=FTAG, HS=HS, AS=AS, id=id, FTR=FTR, HST=HST, AST=AST)
    return match


def getting_json1819(id):
    HomeTeam = request.json.get("HomeTeam", "")
    AwayTeam = request.json.get("AwayTeam", "")
    FTHG = request.json.get("FTHG", "")
    FTAG = request.json.get("FTAG", "")
    HS = request.json.get("HS", "")
    AS = request.json.get("AS", "")
    FTR = request.json.get("FTR", "")
    HST = request.json.get("HST", "")
    AST = request.json.get("AST", "")
    match = Matches1819(HomeTeam=HomeTeam, AwayTeam=AwayTeam, FTHG=FTHG,
                        FTAG=FTAG, HS=HS, AS=AS, id=id, FTR=FTR, HST=HST, AST=AST)
    return match
