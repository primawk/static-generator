from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"


def markdown_to_blocks(markdown):
    result = []

    for block in markdown.split("\n\n"):
        result.append("\n".join(line.strip() for line in block.strip().splitlines()))
    return result

def block_to_block_type(markdown):
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown.startswith("```\n ") and markdown.endswith("```"):
        return BlockType.CODE
    if markdown.startswith((">", "> ")):
        return BlockType.QUOTE
    if markdown.startswith("- "):
        return BlockType.UNORDERED
    if markdown.startswith(re.match(r"^\d+\.")):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH
    

    