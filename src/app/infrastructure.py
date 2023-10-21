import _csv
import io
from dataclasses import dataclass
from typing import TypeAlias

import weasyprint

from app.domain import FormatRepository

Row: TypeAlias = list[str] | tuple[str]


@dataclass
class CSVRepository(FormatRepository):
    out: io.StringIO
    writer: '_csv._writer'

    def write(self, row: Row) -> None:
        self.writer.writerow(row)

    def get_data(self):
        return self.out.getvalue()


@dataclass
class PDFRepository(FormatRepository):
    out: io.StringIO
    weasyprint: weasyprint

    def write(self, row: Row) -> None:
        """Some realization"""

    def get_data(self):

        return self.out.getvalue()


# DAL - DATA ACCESS LAYER
