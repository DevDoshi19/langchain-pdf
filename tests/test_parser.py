from langchain_pdf.parser import BlockParser
from langchain_pdf.blocks import Heading, Paragraph, Bullet

def test_parser_creates_blocks():
    text = "# Title\n- item\nParagraph text"
    blocks = BlockParser().parse(text)

    assert isinstance(blocks[0], Heading)
    assert blocks[0].level == 1

    assert isinstance(blocks[1], Bullet)
    assert isinstance(blocks[2], Paragraph)

def test_empty_input():
    blocks = BlockParser().parse("")
    assert blocks == []

