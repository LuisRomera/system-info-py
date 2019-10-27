import json

from flask import Flask
from logger import logger

from config.environment import get_config
from services.commander_pro_service import CommanderProService

app = Flask(__name__)
env = get_config()


@app.route("/commanderPro/")
def send_info_commander_pro():
    return json.dumps(CommanderProService(env['server']['path_corsair']).get_info_corsair_comamander())


logger.info("Init server ...")
app.run()
