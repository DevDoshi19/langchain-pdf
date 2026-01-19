from langchain_pdf.normalizer import TextNormalizer

def test_html_and_code_removed():
    raw = "<b>Hello</b>\n```python\nprint('hi')\n```"
    out = TextNormalizer().normalize(raw)
    assert "<b>" not in out
    assert "print" not in out

def test_heading_normalization():
    raw = "##Title\n# Another"
    out = TextNormalizer().normalize(raw)
    assert out.startswith("## Title")

def test_bullet_normalization():
    raw = "* item\n• item2\n-   item3"
    out = TextNormalizer().normalize(raw)
    assert out.count("- ") == 3
