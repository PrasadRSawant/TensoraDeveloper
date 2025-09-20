# -*- coding: utf-8 -*-
"""${message}"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrade_ops}

def downgrade() -> None:
    ${downgrade_ops}
