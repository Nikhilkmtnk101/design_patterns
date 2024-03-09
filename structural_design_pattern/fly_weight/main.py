from robot_factory import RobotFactory

if __name__ == "__main__":
    robot_factory = RobotFactory()
    human_robot = robot_factory.get_robot("HUMANOID")
    human_robot1 = robot_factory.get_robot("HUMANOID")
    human_robot.display(1, 2)
