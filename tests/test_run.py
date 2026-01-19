from langchain_pdf.blocks import Heading, Paragraph, Bullet

def test_heading_block():
    h = Heading(text="Introduction", level=1)
    assert h.text == "Introduction"
    assert h.level == 1

def test_paragraph_block():
    p = Paragraph(text="This is a paragraph.")
    assert p.text.startswith("This is")

def test_bullet_block():
    b = Bullet(text="Item one")
    assert "Item" in b.text
