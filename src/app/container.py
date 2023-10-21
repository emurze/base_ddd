import csv
import io

from app.application import FormatService
from app.infrastructure import CSVRepository
from config.settings import BASE_DIR

CSV_PATH = BASE_DIR / 'files' / 'data.csv'


class ApplicationContainer:
    @staticmethod
    def run():
        out = io.StringIO()
        writer = csv.writer(out)
        csv_repository = CSVRepository(out=out, writer=writer)

        csv_service = FormatService(
            repository=csv_repository,
            path=CSV_PATH,
        )
        csv_service.run()

