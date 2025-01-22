#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib 
import wpimath.controller


import commands2
import commands2.button


from constants import OP, SW
import Subsystem.motor_sub
from Commands.rotate_motor import lift, lower, StopMotor, UpdateEncoder


class RobotContainer:

    def __init__(self):
        self.motor_sub = Subsystem.motor_sub.ElevatorSubsystem()

        self.stick = commands2.button.CommandXboxController(OP.joystick_port)

        self.configureButtonBindings()

    def configureButtonBindings(self):
        self.motor_sub.setDefaultCommand()
