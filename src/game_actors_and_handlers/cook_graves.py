# coding=utf-8
import logging
from game_state.game_types import GameCookGrave, GameCookGraveWithBrains, GameCookItem
from game_actors_and_handlers.workers import ResourcePicker
from game_actors_and_handlers.base import BaseActor

logger = logging.getLogger(__name__)


class BrewPicker(ResourcePicker):

    def get_worker_types(self):
        return [GameCookGrave.type, GameCookGraveWithBrains.type]

#Cookbot_alfa_version
class CookBot(BaseActor):

    def perform_action(self):
        cookGrave = self._get_game_location().get_all_objects_by_type(GameCookGrave.type)
        for cookGrave in list(cookGrave):
            if hasattr(cookGrave, "currentRecipe") is False:
                print 'Nothing Cook'
                logger.info(u'Ничего не варят')
                cook_item='RECIPE_02'
                cook_event = GameCookItem(unicode(cook_item),
                cookGrave.id)
                self._get_events_sender().send_game_events([cook_event])
            else:
                logger.info(u'Что-то варят')
                print 'Samsing Cook'
