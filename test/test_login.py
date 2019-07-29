def test_login(app):
    if app.session.is_logged_in() > 0:
        app.session.logout()
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
