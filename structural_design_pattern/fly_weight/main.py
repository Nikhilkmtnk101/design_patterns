from robot_factory import RobotFactory
from constants import RobotTypes

if __name__ == "__main__":
    robot_factory = RobotFactory()
    human_robot = robot_factory.get_robot(RobotTypes.HUMANOID.value)
    human_robot1 = robot_factory.get_robot(RobotTypes.HUMANOID.value)
    human_robot.display(1, 2)
