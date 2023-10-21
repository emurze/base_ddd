import logging
from dataclasses import dataclass
from pathlib import Path

from app.domain import FormatRepository

lg = logging.getLogger(__name__)


@dataclass
class FormatService:
    repository: FormatRepository
    path: Path | str

    def write(self):
        self.repository.write(['hello', 'world'])
        self.repository.write(['...', '...'])

        content = self.repository.get_data()

        with open(self.path, 'w') as csv_file:
            csv_file.write(content)
