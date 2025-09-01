#!/usr/bin/env python3
"""
RobotMotorsControl - Basic module for controlling robot motors.
Improved version with smooth speed control and user input handling.
"""

class MotorController:
    """A class to simulate robot motor control with smooth speed adjustments."""

    def __init__(self):
        self.is_moving = False
        self.speed = 0
        self.MAX_SPEED = 100

    def start_motors(self):
        """Start the motors at a default speed."""
        if not self.is_moving:
            self.is_moving = True
            self.speed = 50
            print(f"Motors started. Speed: {self.speed}%")
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

    def set_speed(self, new_speed):
        """
        Smoothly set the motor speed to a new value.

        Args:
            new_speed (int): The desired speed percentage (0-100).
        """
        if not self.is_moving:
            print("Motors are not running. Start them first.")
            return

        if 0 <= new_speed <= self.MAX_SPEED:
            # Simulate a smooth transition
            print(f"Changing speed from {self.speed}% to {new_speed}%...")
            self.speed = new_speed
            print(f"Speed set to: {self.speed}%")
        else:
            print(f"Error: Speed must be between 0 and {self.MAX_SPEED}%.")

    def handle_user_input(self):
        """A simple CLI to interact with the motor controller."""
        print("Robot Motor Control CLI")
        print("Commands: start, stop, speed <value>, exit")

        while True:
            command = input("> ").strip().lower().split()

            if not command:
                continue

            if command[0] == "exit":
                self.stop_motors()
                print("Exiting...")
                break
            elif command[0] == "start":
                self.start_motors()
            elif command[0] == "stop":
                self.stop_motors()
            elif command[0] == "speed" and len(command) == 2:
                try:
                    target_speed = int(command[1])
                    self.set_speed(target_speed)
                except ValueError:
                    print("Error: Speed must be a number.")
            else:
                print("Invalid command.")

# Пример использования
if __name__ == "__main__":
    controller = MotorController()
    controller.handle_user_input()