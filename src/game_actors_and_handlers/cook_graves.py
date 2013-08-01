# coding=utf-8
import logging
from game_state.game_types import GameCookGrave, GameCookGraveWithBrains, GameCookItem, GameCookStart
from game_actors_and_handlers.workers import ResourcePicker
from game_actors_and_handlers.base import BaseActor

logger = logging.getLogger(__name__)


class BrewPicker(ResourcePicker):

    def get_worker_types(self):
        return [GameCookGrave.type, GameCookGraveWithBrains.type]

#Cookbot_alfa_version
class CookBot(BaseActor):
    def perform_action(self):
        cookGraves = self._get_game_location().get_all_objects_by_type(GameCookGrave.type)
        for cookGrave in cookGraves:
            lencp=2-len(cookGrave.pendingRecipes)
            if (hasattr(cookGrave, "currentRecipe") is False): lencp+=1
            if not cookGrave.isUp:
                logger.info(u'Повара отдыхают, запускаем работать.')
                cook_event = GameCookStart(cookGrave.id)
                self._get_events_sender().send_game_events([cook_event])
            for i in range(lencp):
                    if len(cookGrave.pendingRecipes)<2:
                        logger.info(u'Пустая корзина у поваров добавляем...')
                        cook_event = GameCookItem(unicode('RECIPE_02'),cookGrave.id)
                        self._get_events_sender().send_game_events([cook_event])
                        print 'Nothing Cook'

    def perform_action_with_brains(self):
        cookGraveWithBrains = self._get_game_location().get_all_objects_by_type(GameCookGraveWithBrains.type)
        for cookGraveWithBrain in cookGraveWithBrains:
            lencp=2-len(cookGrave.pendingRecipes)
            if (hasattr(cookGrave, "currentRecipe") is False): lencp+=1
            if not cookGraveWithBrain.isUp:
                cook_event = GameCookStart(cookGraveWithBrain.id)
                self._get_events_sender().send_game_events([cook_event])
            for i in range(lencp):
                    if len(cookGraveWithBrain.pendingRecipes)<2:
                        logger.info(u'Пустая корзина у мозговитых поваров добавляем...')
                        cook_event = GameCookItem(unicode('RECIPE_02'),cookGraveWithBrain.id)
                        self._get_events_sender().send_game_events([cook_event])
