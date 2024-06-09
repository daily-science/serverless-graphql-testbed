"""Main module."""

from flask import Flask
from flask_cors import CORS
from graphql_server.flask import GraphQLView

import graphene
from graphene import relay


class QueryRoot(graphene.ObjectType):
    about = graphene.String(description="About this API ")
    def resolve_about(root, info, **args):
        return "Hello, I am testbed api "

    lxml = graphene.String(description="About lxml")
    def resolve_lxml(root, info, **args):
        import lxml
        return f"lxml version: {lxml.__version__}"


    objectify = graphene.String(description="About objectify")
    def resolve_objectify(root, info, **args):
        from lxml import objectify
        return f"lxml objectify version: {objectify.__version__}"



def create_app():
    """Function that creates our Flask application."""

    schema_root = graphene.Schema(query=QueryRoot, mutation=None, auto_camelcase=False)

    app = Flask(__name__)
    CORS(app)

    # app.before_first_request(migrate)

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema_root,
            graphiql=True,
        ),
    )
    return app


# pragma: no cover
app = create_app()


if __name__ == "__main__":
    app.run()
