# coding=utf-8
import logging
from game_state.game_types import GameCookGrave, GameCookGraveWithBrains, GameCookItem, GameCookStart
from game_actors_and_handlers.workers import ResourcePicker
from game_actors_and_handlers.base import BaseActor

logger = logging.getLogger(__name__)


class BrewPicker(ResourcePicker):

    def get_worker_types(self):
        return [GameCookGrave.type, GameCookGraveWithBrains.type]

class CookBot(BaseActor):
    def perform_action(self):
        cookGraves = self._get_game_location().get_all_objects_by_type(GameCookGrave.type)
        print 'cookGraves = ' + str(cookGraves)
        for cookGrave in cookGraves:
            print 'current len = ' + str(len(cookGrave.pendingRecipes))
            if (hasattr(cookGrave, "currentRecipe") is False)and(len(cookGrave.pendingRecipes)==0):
                lencp=3
                print 'lencp = ' +str(lencp)
            else:
                lencp=2-len(cookGrave.pendingRecipes)
                print 'lencp = ' +str(lencp)
            if not cookGrave.isUp:
                print 'Povara otdihaut zapustim rabotat'
                cook_event = GameCookStart(cookGrave.id)
                self._get_events_sender().send_game_events([cook_event])
            for i in range(lencp):
                    print 'i= ' + str(i)
                    if len(cookGrave.pendingRecipes)<2:
                        print '2 Current len = ' + str(len(cookGrave.pendingRecipes))
                        logger.info(u'Пустая корзина у поваров добавляем...')
                        cook_event = GameCookItem(unicode('RECIPE_02'),cookGrave.id)
                        print 'cook_event = ' + str(cook_event)
                        self._get_events_sender().send_game_events([cook_event])
                        print 'Nothing Cook'

    def perform_action_with_brains(self):
        cookGraveWithBrains = self._get_game_location().get_all_objects_by_type(GameCookGraveWithBrains.type)
        for cookGraveWithBrain in cookGraveWithBrains:
            if (hasattr(cookGrave, "currentRecipe") is False)and(len(cookGrave.pendingRecipes)==0):
                lencp=3
            else:
                lencp=2-len(cookGrave.pendingRecipes)
            if not cookGraveWithBrain.isUp:
                cook_event = GameCookStart(cookGraveWithBrain.id)
                self._get_events_sender().send_game_events([cook_event])
            for i in range(lencp):
                    if len(cookGraveWithBrain.pendingRecipes)<2:
                        logger.info(u'Пустая корзина у мозговитых поваров добавляем...')
                        cook_event = GameCookItem(unicode('RECIPE_02'),cookGraveWithBrain.id)
                        self._get_events_sender().send_game_events([cook_event])
