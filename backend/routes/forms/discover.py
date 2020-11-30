"""
Return a list of all publicly discoverable forms to unauthenticated users.
"""
from starlette.requests import Request
from starlette.responses import JSONResponse

from backend.route import Route


class DiscoverableFormsList(Route):
    """
    List all discoverable forms that should be shown on the homepage.
    """

    name = "discoverable_forms_list"
    path = "/discoverable"

    async def get(self, request: Request) -> JSONResponse:
        forms = []

        for form in request.state.db.forms.find({
            "features": "DISCOVERABLE"
        }):
            forms.append(form)

        return JSONResponse(
            forms
        )