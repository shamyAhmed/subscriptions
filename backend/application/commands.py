from models.utils.user_utils import create_single_user


def register_commands(app):
    @app.cli.command("create-single-user")
    def create_single_user_cmd():
        """Create a single user."""
        create_single_user()
