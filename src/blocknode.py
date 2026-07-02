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
    block = markdown_to_blocks(markdown)[0]
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith((">", "> ")):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED
    if re.match(r"^\d+\.", block):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH


    

    