#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import logging
log = logging.Logger('P212-robot')

import wpilib
import commands2

from subsystems.example_ss import ExampleSubsystem
import constants


class TemplateCommand(commands2.Command):
    """
    This class is a template for how commands for your robot should be
    structured.
    """
    def __init__(self, example_ss: ExampleSubsystem) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        super().__init__()
        self.example_ss = example_ss

    def initialize(self):
        """
        Perform any setup to initialize the command.
        This method runs when the scheduler schedules the command.
        """

    def execute(self):
        """
        Performs the main bulk of the command.
        This method runs 50 times a second while the command is active.
        """
        self.example_ss.activate_actuator()

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """
        # stop the motor after 2 seconds
        return self.example_ss.sensor_value() > 5.0

    def end(self, interrupted: bool):
        """
        Perform any cleanup or final steps needed after the command finishes.
        If you need to do something different depending on whether the command
        completed normally or was interrupted (by another command), the
        :interrupted: parameter will be True if the command was interrupted.
        """
        self.example_ss.stop()

