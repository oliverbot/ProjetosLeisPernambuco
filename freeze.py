from app import create_app
from flask_frozen import Freezer
from app.models import Proposicao

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def page():
    return [('app.page', {'num_page': int(page)}) for page in range(1, Proposicao.get_all_proposal_summary_paginated()['pagination'].pages + 1)]

@freezer.register_generator
def proposal():
    return [('app.proposal', {'id': int(proposal['id'])}) for proposal in Proposicao.get_all_proposal_summary()]


if __name__ == '__main__':
    freezer.freeze()