# This is a placeholder for alembic/env.py
# You would typically run 'alembic init alembic' to generate the full alembic environment.

# from logging.config import fileConfig
# from sqlalchemy import engine_from_config, pool
# from alembic import context
# from backend.app.core.config import settings
# from backend.app.core.database import Base

# target_metadata = Base.metadata

# def run_migrations_offline():
#     """Run migrations in 'offline' mode."""
#     url = settings.DATABASE_URL
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()

# def run_migrations_online():
#     """Run migrations in 'online' mode."""
#     configuration = context.config

#     # overwrite the sqlalchemy.url configuration value with a custom one
#     configuration.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

#     connectable = engine_from_config(
#         configuration.get_section(configuration.config_ini_section),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()

# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()