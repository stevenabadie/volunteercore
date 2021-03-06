from volunteercore import create_app, db, cli
from volunteercore.auth.models import Role, User
from volunteercore.volops.models import Partner, Opportunity, \
    TagCategory, Tag

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Role': Role,
        'Partner': Partner,
        'Opportunity': Opportunity,
        'TagCategory': TagCategory,
        'Tag': Tag
    }
