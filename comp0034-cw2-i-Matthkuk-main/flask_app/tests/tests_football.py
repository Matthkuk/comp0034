from flask_app import db
from flask_app.models import Matches, Matches1516, Matches1617, Matches1718, Matches1819

# --------------
# GET all matches
# --------------


def test_get_all_matches(test_client):
    response = test_client.get("/api/matches")
    assert response.status_code == 200
    assert b"Chelsea" in response.data
    assert response.content_type == "application/json"


def test_get_all_matches1516(test_client):
    response = test_client.get("/api/matches1516")
    assert response.status_code == 200
    assert b"Chelsea" in response.data
    assert response.content_type == "application/json"


def test_get_all_matches1617(test_client):
    response = test_client.get("/api/matches1617")
    assert response.status_code == 200
    assert b"Chelsea" in response.data
    assert response.content_type == "application/json"


def test_get_all_matches1718(test_client):
    response = test_client.get("/api/matches1718")
    assert response.status_code == 200
    assert b"Chelsea" in response.data
    assert response.content_type == "application/json"


def test_get_all_matches1819(test_client):
    response = test_client.get("/api/matches1819")
    assert response.status_code == 200
    assert b"Chelsea" in response.data
    assert response.content_type == "application/json"

# --------------
# GET single matches
# --------------


def test_get_matches(test_client):
    response = test_client.get("/api/matches/3")
    assert response.status_code == 200
    assert b"ManUnited" in response.data
    assert b"Swansea" in response.data
    assert response.content_type == "application/json"


def test_get_matches1516(test_client):
    response = test_client.get("/api/matches1516/7")
    assert response.status_code == 200
    assert b"Arsenal" in response.data
    assert b"WestHam" in response.data
    assert response.content_type == "application/json"


def test_get_matches1617(test_client):
    response = test_client.get("/api/matches1617/7")
    assert response.status_code == 200
    assert b"Southampton" in response.data
    assert b"Watford" in response.data
    assert response.content_type == "application/json"


def test_get_matches1718(test_client):
    response = test_client.get("/api/matches1718/7")
    assert response.status_code == 200
    assert b"Watford" in response.data
    assert b"Liverpool" in response.data
    assert response.content_type == "application/json"


def test_get_matches1819(test_client):
    response = test_client.get("/api/matches1819/7")
    assert response.status_code == 200
    assert b"Wolves" in response.data
    assert b"Everton" in response.data
    assert response.content_type == "application/json"

# --------------
# POST matches
# --------------


def test_add_match(test_client):
    match = Matches(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=39, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )

    match_json = {
        "HomeTeam": "New 1",
        "AwayTeam": "New 2",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    exists = db.session.execute(
        db.select(Matches).filter_by(id=match.id)
    ).scalar()
    if exists:
        db.session.execute(db.delete(Matches).where(Matches.id == match.id))
        db.session.commit()

    num_matchs_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(Matches)
    )

    response = test_client.post("/api/matches/39", json=match_json)
    num_matchs_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(Matches)
    )

    data = response.json
    assert response.status_code == 200
    assert "New 1" in data["HomeTeam"]
    assert "New 2" in data["AwayTeam"]
    assert (num_matchs_in_db_after - num_matchs_in_db) == 1


def test_add_match_fail(test_client):
    match = Matches(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=39, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )

    match_json = {
        "HomeTeam": "New 1",
        "AwayTeam": "New 2",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    exists = db.session.execute(
        db.select(Matches).filter_by(id=match.id)
    ).scalar()
    if exists:
        pass
    else:
        db.session.add(match)
        db.session.commit()

    response = test_client.post("/api/matches/39", json=match_json)

    assert response.status_code == 403


def test_add_match1516(test_client):
    match = Matches1516(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=20, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )

    match_json = {
        "HomeTeam": "New 1",
        "AwayTeam": "New 2",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    exists = db.session.execute(
        db.select(Matches1516).filter_by(id=match.id)
    ).scalar()
    if exists:
        db.session.execute(db.delete(Matches1516).where(
            Matches1516.id == match.id))
        db.session.commit()

    num_matchs_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1516)
    )

    response = test_client.post("/api/matches1516/20", json=match_json)
    num_matchs_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1516)
    )

    data = response.json
    assert response.status_code == 200
    assert "New 1" in data["HomeTeam"]
    assert "New 2" in data["AwayTeam"]
    assert (num_matchs_in_db_after - num_matchs_in_db) == 1


def test_add_match1617(test_client):
    match = Matches1617(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=20, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )

    match_json = {
        "HomeTeam": "New 1",
        "AwayTeam": "New 2",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    exists = db.session.execute(
        db.select(Matches1617).filter_by(id=match.id)
    ).scalar()
    if exists:
        db.session.execute(db.delete(Matches1617).where(
            Matches1617.id == match.id))
        db.session.commit()

    num_matchs_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1617)
    )

    response = test_client.post("/api/matches1617/20", json=match_json)
    num_matchs_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1617)
    )

    data = response.json
    assert response.status_code == 200
    assert "New 1" in data["HomeTeam"]
    assert "New 2" in data["AwayTeam"]
    assert (num_matchs_in_db_after - num_matchs_in_db) == 1


def test_add_match1718(test_client):
    match = Matches1718(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=20, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )

    match_json = {
        "HomeTeam": "New 1",
        "AwayTeam": "New 2",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    exists = db.session.execute(
        db.select(Matches1718).filter_by(id=match.id)
    ).scalar()
    if exists:
        db.session.execute(db.delete(Matches1718).where(
            Matches1718.id == match.id))
        db.session.commit()

    num_matchs_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1718)
    )

    response = test_client.post("/api/matches1718/20", json=match_json)
    num_matchs_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1718)
    )

    data = response.json
    assert response.status_code == 200
    assert "New 1" in data["HomeTeam"]
    assert "New 2" in data["AwayTeam"]
    assert (num_matchs_in_db_after - num_matchs_in_db) == 1


def test_add_match1819(test_client):
    match = Matches1819(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=20, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )

    match_json = {
        "HomeTeam": "New 1",
        "AwayTeam": "New 2",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    exists = db.session.execute(
        db.select(Matches1819).filter_by(id=match.id)
    ).scalar()
    if exists:
        db.session.execute(db.delete(Matches1819).where(
            Matches1819.id == match.id))
        db.session.commit()

    num_matchs_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1819)
    )

    response = test_client.post("/api/matches1819/20", json=match_json)
    num_matchs_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(Matches1819)
    )

    data = response.json
    assert response.status_code == 200
    assert "New 1" in data["HomeTeam"]
    assert "New 2" in data["AwayTeam"]
    assert (num_matchs_in_db_after - num_matchs_in_db) == 1

# --------------
# DELETE matches
# --------------


def test_delete_match(test_client):
    new_match = Matches(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=5, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )
    match = db.session.execute(
        db.select(Matches).filter_by(id=5)
    ).scalar_one_or_none()
    if match is None:
        db.session.add(new_match)
        db.session.commit()
    response = test_client.delete("/api/matches/5")
    assert response.status_code == 200


def test_delete_match_fail(test_client):
    match = db.session.execute(
        db.select(Matches).filter_by(id=5)
    ).scalar_one_or_none()
    if match is not None:
        db.session.delete(match)
        db.session.commit()
    response = test_client.delete("/api/matches/5")
    assert response.status_code == 404


def test_delete_match1516(test_client):
    new_match = Matches1516(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=5, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )
    match = db.session.execute(
        db.select(Matches1516).filter_by(id=5)
    ).scalar_one_or_none()
    if match is None:
        db.session.add(new_match)
        db.session.commit()
    response = test_client.delete("/api/matches1516/5")
    assert response.status_code == 200


def test_delete_match1617(test_client):
    new_match = Matches1617(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=5, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )
    match = db.session.execute(
        db.select(Matches1617).filter_by(id=5)
    ).scalar_one_or_none()
    if match is None:
        db.session.add(new_match)
        db.session.commit()
    response = test_client.delete("/api/matches1617/5")
    assert response.status_code == 200


def test_delete_match1718(test_client):
    new_match = Matches1718(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=5, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )
    match = db.session.execute(
        db.select(Matches1718).filter_by(id=5)
    ).scalar_one_or_none()
    if match is None:
        db.session.add(new_match)
        db.session.commit()
    response = test_client.delete("/api/matches1718/5")
    assert response.status_code == 200


def test_delete_match1819(test_client):
    new_match = Matches1819(
        HomeTeam="New 1", AwayTeam="New 2", FTR="H", id=5, FTHG="1", FTAG="0", HS="2", AS="3", HST="1", AST="1"
    )
    match = db.session.execute(
        db.select(Matches1819).filter_by(id=5)
    ).scalar_one_or_none()
    if match is None:
        db.session.add(new_match)
        db.session.commit()
    response = test_client.delete("/api/matches1819/5")
    assert response.status_code == 200

# --------------
# PATCH matches
# --------------


def test_patch_match(test_client):
    match_json = {
        "HomeTeam": "Hello",
        "AwayTeam": "GoodBye",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    response = test_client.patch("/api/matches/9", json=match_json)
    data = response.json
    assert response.status_code == 200
    assert "Hello" in data["HomeTeam"]
    assert "GoodBye" in data["AwayTeam"]


def test_patch_match_fail(test_client):
    match_json = {
        "HomeTeam": "Hello",
        "AwayTeam": "GoodBye",
        "FTR": "H",
        "FTHG": "",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }
    match = db.session.execute(
        db.select(Matches).filter_by(id=30)
    ).scalar_one_or_none()
    response = test_client.patch("/api/matches/30", json=match_json)
    if match is not None:
        assert response.status_code == 400
    else:
        assert response.status_code == 404


def test_patch_match1516(test_client):
    match_json = {
        "HomeTeam": "Hello",
        "AwayTeam": "GoodBye",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    response = test_client.patch("/api/matches1516/9", json=match_json)
    data = response.json
    assert response.status_code == 200
    assert "Hello" in data["HomeTeam"]
    assert "GoodBye" in data["AwayTeam"]


def test_patch_match1617(test_client):
    match_json = {
        "HomeTeam": "Hello",
        "AwayTeam": "GoodBye",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    response = test_client.patch("/api/matches1617/9", json=match_json)
    data = response.json
    assert response.status_code == 200
    assert "Hello" in data["HomeTeam"]
    assert "GoodBye" in data["AwayTeam"]


def test_patch_match1718(test_client):
    match_json = {
        "HomeTeam": "Hello",
        "AwayTeam": "GoodBye",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    response = test_client.patch("/api/matches1718/9", json=match_json)
    data = response.json
    assert response.status_code == 200
    assert "Hello" in data["HomeTeam"]
    assert "GoodBye" in data["AwayTeam"]


def test_patch_match1819(test_client):
    match_json = {
        "HomeTeam": "Hello",
        "AwayTeam": "GoodBye",
        "FTR": "H",
        "FTHG": "1",
        "FTAG": "0",
        "HS": "2",
        "AS": "3",
        "HST": "1",
        "AST": "1"
    }

    response = test_client.patch("/api/matches1819/9", json=match_json)
    data = response.json
    assert response.status_code == 200
    assert "Hello" in data["HomeTeam"]
    assert "GoodBye" in data["AwayTeam"]
