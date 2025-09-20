import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# This ensures that your app models are discoverable
sys.path.append(os.getcwd())
from backend.app.core.config import settings
from backend.app.models.user import Base # Import your Base from models

# Interpret the config file for Python's standard logging.
# This sets up loggers basically.
fileConfig(context.config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py, 
# can be acquired: 
# my_important_option = context.config.get_main_option("my_important_option")
# ... or even acquire values from Python config determined by the config itself:
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an actual Engine, though an Engine is precisely what we get back
    from sqlalchemy.create_engine().  By configuring an Engine
    manually here, we avoid connecting to an actual database in this
    scenario.
    """
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario, we still need an Engine
    to connect to the database.  When called from 'alembic upgrade',
    the Engine is already present in the context.config object.
    However, when called from a script, we need to create one ourselves.
    """
    configuration = context.config.get_section(context.config.config_ini_section)
    configuration['sqlalchemy.url'] = settings.DATABASE_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()