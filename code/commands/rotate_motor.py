#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import phoenix6
import commands2
import commands2.cmd
import wpimath.controller

from Subsystem.motor_sub import MotorSubsystem

import constants
import logging

logger = logging.getLogger("aniyah")


class lift(commands2.Command):
    def __init__(self, motor_sub: MotorSubsystem ) -> None:
        super().__init__()
        self.motor = motor_sub

    def initialize(self):
        logger.info("running Motor command")

    def execute(self):
        self.motor.lift()

    def isFinished(self):
        return False
    
    def end(self,interrupted):
        self.motor.stop()


class lower(commands2.Command):
    def __init__(self, motor_sub: MotorSubsystem) -> None: 
        super().__init__()
        self.motor = motor_sub

    def execute(self):
        return False
    
    def isFinished(self):
        return False

    def end(self, interrupted):
        self.motor.stop()


class StopMotor(commands2.Command):
    def __init__(self, motor_sub: MotorSubsystem) -> None:
        super().__init__()
        self.motor = motor_sub

    def intialize(self):
        logger.info

class UpdateEncoder(commands2.command):
    def __init__(self, motor_sub: MotorSubsystem) -> None:
        super().__init__()
        self.motor = motor_sub

    def initialize(self):
        wpilib.SmartDashboard.putNumber("Encoder", self.motor_sub.encoder_value())

    def isFinished(self):
        return False
    
class ElevatorTeleop(commands2.Command):
    def __init__(self, motor_sub, joystick):
        super().__init__()
        self.motor = motor_sub
        self.stick = joystick
        self.addRequirements(self.motor)

    def execute(self):
        joystick_value = self.stick.getLeftYAxis()
        self.motor.move(joystick_value)