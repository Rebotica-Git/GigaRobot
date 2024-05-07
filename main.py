import random
import numpy as np
import time
from numba import jit


class Limb:
    def __init__(self):
        self.health = random.uniform(50, 100)
        self.functionality = random.uniform(50, 100)

    def move(self):
        raise NotImplementedError("Метод move() должен быть переопределен в подклассе.")


class Arm(Limb):
    def __init__(self):
        super().__init__()

    def grip(self):
        return "Рука сжала предмет."

    def pull_lever(self):
        return "Рука потянула за рычаг."


class Leg(Limb):
    def __init__(self):
        super().__init__()

    def walk(self):
        return "Робот начал движение."

    @staticmethod
    @jit(nopython=True)
    def calculate_walk_trajectory(steps, step_length, step_duration):
        num_steps = len(steps)
        x_values = np.zeros(num_steps)
        y_values = np.zeros(num_steps)

        # Начальные координаты
        x = 0
        y = 0

        for i in range(num_steps):
            # Рассчитываем перемещение по каждому шагу
            x_step = step_length * np.cos(steps[i])
            y_step = step_length * np.sin(steps[i])

            # Обновляем координаты
            x += x_step
            y += y_step

            x_values[i] = x
            y_values[i] = y


        return x_values, y_values


class Vision:
    def __init__(self):
        self.accuracy = random.uniform(50, 100)

    def analyze_environment(self):
        return "Робот проанализировал окружающую среду."


class Reactor:
    def __init__(self):
        self.energy_level = random.uniform(0, 100)

    def generate_power(self):
        return "Робот сгенерировал энергию из ядерного реактора."


class Robot(Arm, Leg, Vision, Reactor):
    def __init__(self):
        super().__init__()

    def operate(self, energy_level=None):
        if energy_level is None:
            energy_level = self.energy_level
        if energy_level >= 75:
            return "Робот работает в штатном режиме."
        elif energy_level >= 25:
            return "Робот работает в энергосберегающем режиме."
        else:
            return "Робот не работает."


class BulletTrajectoryCalculator:
    @staticmethod
    def calculate_trajectory(initial_velocity, launch_angle, gravity=9.8, time_step=0.1, duration=10):
        # Преобразование угла в радианы
        launch_angle_rad = np.radians(launch_angle)

        # Расчет компонент скорости
        vx = initial_velocity * np.cos(launch_angle_rad)
        vy = initial_velocity * np.sin(launch_angle_rad)

        # Массивы для хранения координат x и y
        x_values = []
        y_values = []

        # Начальные условия
        x = 0
        y = 0

        # Расчет траектории
        for t in np.arange(0, duration, time_step):
            x = vx * t
            y = vy * t - 0.5 * gravity * t ** 2

            if y < 0:
                break  # Пуля достигла земли, прекращаем расчет

            x_values.append(x)
            y_values.append(y)

        return x_values, y_values

    def test_velocity_calculator(self):
        initial_velocity = 500  # начальная скорость пули в м/с
        launch_angle = 45  # угол запуска в градусах

        start_time = time.time()
        x_values, y_values = self.calculate_trajectory(initial_velocity, launch_angle)
        end_time = time.time()

        print("Время расчета траектории:", end_time - start_time, "секунд")
        print("Траектория пули:")
        for x, y in zip(x_values, y_values):
            print(f"({x:.2f}, {y:.2f})")


if __name__ == "__main__":
    bullet_calculator = BulletTrajectoryCalculator()
    bullet_calculator.test_velocity_calculator()
    trajectory = Leg()
    trajectory = trajectory.calculate_walk_trajectory([x for x in range(20)], 120, 3)
    print(trajectory[0][:5].tolist())
