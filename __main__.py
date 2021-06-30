from pacmangame import constants
from pacmangame.point import Point
from pacmangame.control_actors_action import ControlActorsAction
from pacmangame.draw_actors_action import DrawActorsAction
from pacmangame.handle_collisions_action import HandleCollisionsAction
from pacmangame.move_actors_action import MoveActorsAction
from pacmangame.input_service import ArcadeInputService
from pacmangame.output_service import ArcadeOutputService
from pacmangame.pacman import PacMan
from pacmangame.director import Director
from pacmangame.ghost import Ghost

import arcade
import random

def main():
    output_service = ArcadeOutputService()
    input_service = ArcadeInputService()
    
    #Creating Pac-Man and Ghosts
    cast = {}
    ghost_list = arcade.SpriteList()
    pacman = PacMan()
    
    #Adding images
    pinky = Ghost(constants.PINKY_IMAGE, constants.PINKY_X, constants.PINKY_Y)
    blinky = Ghost(constants.BLINKY_IMAGE, constants.BLINKY_X, constants.BLINKY_Y)
    clyde = Ghost(constants.CLYDE_IMAGE, constants.CLYEDE_X, constants. CLYEDE_Y)
    inky = Ghost(constants.INKY_IMAGE, constants.INKY_X, constants.INKY_Y)
    
    #Adding ghosts to ghost list
    ghost_list.append(blinky)
    ghost_list.append(clyde)
    ghost_list.append(inky)
    ghost_list.append(pinky)

    #Creating Map
    map = arcade.tilemap.read_tmx(constants.MAP)
    map_name = constants.MAP_NAME
    wall_list = arcade.tilemap.process_layer(map_object = map, layer_name = map_name, scaling = constants.ACTOR_SCALE, use_spatial_hash = True)
    physics_engine = arcade.PhysicsEnginePlatformer(pacman, wall_list)
    
    #Adding to cast dictionary
    cast['pacman'] = [pacman]
    cast['ghosts'] = ghost_list
    
    #Creating script
    script = {}
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    control_actors_action = ControlActorsAction(input_service)
    #Running script
    script["output"] = [draw_actors_action]
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]

    director = Director(cast, script, input_service, wall_list)
    director.setup()

    arcade.run()

if __name__ == '__main__':
    main()