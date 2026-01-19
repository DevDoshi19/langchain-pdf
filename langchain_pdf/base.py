from fpdf import FPDF
from pathlib import Path


class BasePDF(FPDF):
    """
    Base PDF with soft, readable typography using Inter.
    """

    FONT_FAMILY = "Inter"

    def __init__(self):
        super().__init__()
        self._register_fonts()

    def _register_fonts(self):
        fonts_dir = Path(__file__).parent / "fonts"

        self.add_font(
            self.FONT_FAMILY,
            "",
            str(fonts_dir / "Inter_18pt-Regular.ttf"),
            uni=True
        )

        self.add_font(
            self.FONT_FAMILY,
            "B",
            str(fonts_dir / "Inter_18pt-Bold.ttf"),
            uni=True
        )

    def set_body_font(self, size: float = 11):
        self.set_font(self.FONT_FAMILY, "", size)

    def set_heading_font(self, size: float):
        self.set_font(self.FONT_FAMILY, "B", size)
