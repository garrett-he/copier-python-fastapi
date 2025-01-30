from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
${imports if imports else ""}

revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "..."}


def downgrade() -> None:
    ${downgrades if downgrades else "..."}
