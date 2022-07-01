# DigitalControl_LAB_HW

## One Direction Motion
### purpose
In this code, robot moves from a given point A to a desired point B in 1 direction.
### Algorithm
the velocity of the right and left wheels should be the same and is calculated using equations.
### Controller Impact
P controller: is used to stabilize the unstable process.

PI controller: is used to eliminate the steady state error resulting from P controller.

PD controller: decreases the setteling time of the process using a derivative block.

PID controller: has the optimum control dynamics including zero steady state error, fast response (short rise time), no oscillations and higher stability.
### Disceteization Method
We can use the ZOH method, which consists of sampler with specific frequency.
### Deadzone Impact
It increases the process error. In other words there is no response from the motor til the the input becomes greater than a specific value.

## Angle Regulator
### purpose
In this code, the robot angle is set to the desired angle.
### Algorithm
the velocity of one of right or left wheel should be zero and the other one is calculated using equations.
### Controller Impact
P controller: is used to stabilize the unstable process.

PI controller: is used to eliminate the steady state error resulting from P controller.

PD controller: decreases the setteling time of the process using a derivative block.

PID controller: has the optimum control dynamics including zero steady state error, fast response (short rise time), no oscillations and higher stability.
### Disceteization Method
We can use the ZOH method, which consists of sampler with specific frequency.
### Deadzone Impact
It increases the process error. In other words there is no response from the motor til the the input becomes greater than a specific value.

## 2 Direction Controller
### purpose
In this code, robot moves from a given point A to a desired point B.
### Algorithm
First the angle is set, then the robot moves to the desired point in 1 direction.
### Controller Impact
P controller: is used to stabilize the unstable process.

PI controller: is used to eliminate the steady state error resulting from P controller.

PD controller: decreases the setteling time of the process using a derivative block.

PID controller: has the optimum control dynamics including zero steady state error, fast response (short rise time), no oscillations and higher stability.
### Disceteization Method
We can use the ZOH method, which consists of sampler with specific frequency.
### Deadzone Impact
It increases the process error. In other words there is no response from the motor til the the input becomes greater than a specific value.
### Creativity
only the angle and y data of the robot position is used to reach the desired point.

## Ball Tracking
### purpose
In this code, the robot tracks a ball.
### Algorithm
The position of the robot is set to the point behind the ball with the direction to the opponent goal.
### Controller Impact
P controller: is used to stabilize the unstable process.

PI controller: is used to eliminate the steady state error resulting from P controller.

PD controller: decreases the setteling time of the process using a derivative block.

PID controller: has the optimum control dynamics including zero steady state error, fast response (short rise time), no oscillations and higher stability.
### Disceteization Method
We can use the ZOH method, which consists of sampler with specific frequency.
### Deadzone Impact
It increases the process error. In other words there is no response from the motor til the the input becomes greater than a specific value.
