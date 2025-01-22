import logging
log = logging.Logger('P212-robot')

import commands2
from constants import ELEC


class ExampleSubsystem(commands2.Subsystem):
    """
    This class represents an example subsystem for your robot.  Edit it to
    model your actual subsystems.
    """
    def __init__(self) -> None:
        """Creates a new ExampleSubsystem"""
        super().__init__()
        # Create sensors here, and assign them to instance variables.
        # (Define what DIO port your sensor uses in constants.py)
        self.my_sensor = DigitalIO(ELEC.my_sensor_DIO_port)

        # Create actuators here, and assign them to instance variables.
        # (Define what DIO port your actuator uses in constants.py)
        self.my_motor = rev.CANSparkMax(
            ELEC.my_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)

    def sensor_value(self):
        """
        Example method that reads a subsystem sensor.
        """
        return self.my_sensor.get()

    def activate_actuator(self, output_value):
        """
        Example method that activates a subsystem actuator
        """
        self.my_motor.set(output_value)

    def stop(self):
        """
        Example method that stops everything on the robot
        """
        self.my_motor.set(0.0)

