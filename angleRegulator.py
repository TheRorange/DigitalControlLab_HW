# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
from cmath import cos
import math
from msilib.schema import Error  # noqa: F401
import time
# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot1(RCJSoccerRobot):
    def run(self):
        kp, ki, kd = 2, 0.1, 0
        kp_y, ki_y, kd_y = 2, 0.1, 0
        sum_Error = 0
        Error_back = 0
        sum_Error_y = 0
        Error_back_y = 0
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841
                t1 = time.time()
                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841

                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841

                # Get data from sonars
                sonar_values = self.get_sonar_values()  # noqa: F841

                phi_des = 0
                heading_deg = math.degrees(heading)
                Error = phi_des - heading_deg
                Error = math.atan2(math.sin(Error * math.pi / 180), math.cos(Error * math.pi / 180))
                sum_Error += Error * 0.1
                Error_d = (Error - Error_back) / 0.1
                Error_back = Error

                v = 0
                w = kp * Error + ki * sum_Error + kd * Error_d
                R = 0.02
                L = 0.08

                vr = (2 * v - L * w) / (2 * R)
                vl = (2 * v + L * w) / (2 * R)

                self.left_motor.setVelocity(vl)
                self.right_motor.setVelocity(vr)

                t2 = time.time()
                if t2 - t1 < 0.1:
                    time.sleep(0.1 - (t2 - t1))
                '''# Compute the speed for motors
                direction = utils.get_direction(ball_data["direction"])
                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 7
                    right_speed = 7
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4
                # Set the speed to motors
                # Send message to team robots
                self.send_data_to_team(self.player_id)'''