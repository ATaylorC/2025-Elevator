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
from constants import SW

from subsystems.motor_sub import ElevatorSubsystem

import constants
import logging

logger = logging.getLogger("aniyah")


class lift(commands2.Command):
    def __init__(self, motor_sub:ElevatorSubsystem ) -> None:
        super().__init__()
        self.motor = motor_sub
        self.addRequirements(self.motor)

    def initialize(self):
        logger.info("running Motor command")

    def execute(self):
        self.motor.lift()

    def isFinished(self):
        return True
    
    def end(self,interrupted):
        self.motor.stop()


class lower(commands2.Command):
    def __init__(self, motor_sub: ElevatorSubsystem) -> None: 
        super().__init__()
        self.motor = motor_sub
        self.addRequirements(self.motor)

    def execute(self):
        self.motor.lower()
    
    def isFinished(self):
        return True

    def end(self, interrupted):
        self.motor.stop()


class StopMotor(commands2.Command):
    def __init__(self, motor_sub: ElevatorSubsystem) -> None:
        super().__init__()
        self.motor = motor_sub
        self.addRequirements(self.motor)

    def intialize(self):
        logger.info

class UpdateEncoder(commands2.Command):
    def __init__(self, motor_sub: ElevatorSubsystem) -> None:
        super().__init__()
        self.motor = motor_sub

    def initialize(self):
        wpilib.SmartDashboard.putNumber("Encoder", self.motor_sub.encoder_value())

    def isFinished(self):
        return True
    
class ElevatorTeleop(commands2.Command):
    def __init__(self, motor_sub, joystick: commands2.button.CommandXboxController):
        super().__init__()
        self.motor = motor_sub
        self.stick = joystick
        self.addRequirements(self.motor)

    def execute(self):
        joystick_value = self.stick.getLeftY()
        self.motor.move(joystick_value)


class ElevatorAutonomous(commands2.Command):
     def __init__(self, motor_sub): 
        super().__init__()
        self.motor = motor_sub 
        self.addRequirements(self.motor)  

     def execute(self):
    
        self.motor.motor_down(SW.AutoArmDownSpeed)

