#!/usr/bin/env python3
"""
RobotMotorsControl - Basic module for controlling robot motors.
Initial version with simple start/stop functions.
"""

class MotorController:
    """A simple class to simulate robot motor control."""

    def __init__(self):
        self.is_moving = False
        self.speed = 0

    def start_motors(self):
        """Start the motors at a default speed."""
        if not self.is_moving:
            self.is_moving = True
            self.speed = 50
            print("Motors started. Speed: 50%")
        else:
            print("Motors are already running!")

    def stop_motors(self):
        """Stop the motors."""
        if self.is_moving:
            self.is_moving = False
            self.speed = 0
            print("Motors stopped.")
        else:
            print("Motors are already stopped!")

# Пример использования
if __name__ == "__main__":
    controller = MotorController()
    controller.start_motors()
    controller.stop_motors()