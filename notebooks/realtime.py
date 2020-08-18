#!/usr/bin/env python
# coding: utf-8

from deepface import DeepFace
DeepFace.stream(db_path="./database", model_name='Facenet')
#DeepFace.analyze("database/Motaz/Motaz 1.jpg", actions = ['age', 'gender', 'race', 'emotion'])




