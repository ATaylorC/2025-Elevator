import wpilib
import phoenix6
import commands2

from constants import ELEC


class ElevatorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.motor = phoenix6.hardware.TalonFX(ELEC.motor_CAN_ID)
        self.controller = wpilib.XboxController

    def move(self, speed):
        self.motor.set(0.4*speed)
    
    def stop(self):
        self.motor.set(0)

    def is_stopped(self):
        motor_speed = self.motor.get()
        if motor_speed == 0:
            return True
        else:
            return False
    
    def encoder_value(self):
        status_signal = self.motor.get_rotor_position()
        return status_signal.value