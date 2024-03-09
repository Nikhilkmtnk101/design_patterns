from sprites import Sprites
from robot import Robot, HumanoidRobot, AnimalRobot


class RobotFactory:
    def __init__(self):
        self.robot_object_cache = {}

    def get_robot(self, robot_type: str) -> Robot:
        robot = self.robot_object_cache.get(robot_type, None)

        if robot:
            return robot
        else:
            sprites = Sprites()
            if robot_type == "HUMANOID":
                robot = HumanoidRobot(sprites)
            elif robot_type == "ANIMAL":
                robot = AnimalRobot(sprites)

            self.robot_object_cache[robot_type] = robot

        return robot
