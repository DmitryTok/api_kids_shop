from copy import deepcopy
import logging
import typing as t
from argparse import ArgumentParser

from django.core.management.base import BaseCommand
from django.db import (
    DEFAULT_DB_ALIAS,
    ConnectionHandler,
    OperationalError,
    ProgrammingError,
    connections,
)
from kids_shop import settings

log = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "--database",
            default=DEFAULT_DB_ALIAS,
            help=(
                'Nominates a database to synchronize. '
                'Defaults to the "default" database.'
            ),
        )
        parser.add_argument(
            '--recreate',
            action='store_true',
            help='Recreate database data',
        )

    def handle(self, *args: t.Any, **options: t.Any) -> None:

        database = options["database"]
        db_vendor = connections[database].vendor
        if not db_vendor == "postgresql":
            raise OperationalError("Only PostgreSQL databases are supported")

        db_config = settings.DATABASES[database]
        postgres_config = deepcopy(db_config)

        postgres_config["NAME"] = db_config["POSTGRES_DB"]

        handler = ConnectionHandler({DEFAULT_DB_ALIAS: postgres_config})
        db_name = db_config["NAME"]

        if options["recreate"]:
            with handler[DEFAULT_DB_ALIAS].cursor() as cursor:
                try:
                    cursor.execute(f"DROP DATABASE {db_name} WITH (FORCE);")
                except ProgrammingError:
                    self.stdout.write(f'DataBase {db_name} not EXISTS')
                else:
                    self.stdout.write(f'Database {db_name} drop')

        with handler[DEFAULT_DB_ALIAS].cursor() as cursor:
            try:
                cursor.execute(f"CREATE DATABASE {db_name}")
            except ProgrammingError:
                self.stdout.write(f'DataBase {db_name} EXISTS')
            else:
                self.stdout.write(f'Database {db_name} created successfully')
