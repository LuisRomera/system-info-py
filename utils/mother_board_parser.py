from logger import logger

from model.fan import Fan
from utils.constans import MOTHER_BOARD


def get_children(json):
    return json.get('Children', {})


def parser_mother_board(sawzq):
    # Mother board
    mother_board = list(filter(lambda c: str(c.name) in MOTHER_BOARD, pc_componens))[0]
    try:
        properties_mother_board = mother_board.properties[0].get('Children', {})

        # Parser Fans mother board
        fans_dict = list(filter(lambda p: p.get('Text', {}) in 'Fans', properties_mother_board))[0]
        return list(map(lambda f: Fan().parse_fan(f, fans_dict.get('ImageURL')), get_children(fans_dict)))
    except Exception as ex:
        logger.debug("No mother board info")
        return None
