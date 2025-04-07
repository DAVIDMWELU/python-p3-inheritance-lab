#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [  # ✅ Initialize with some info
            "Math basics",
            "History of Africa",
            "Python programming",
            "Photosynthesis",
            "The Solar System"
        ]

    def teach(self):
        return random.choice(self.knowledge)