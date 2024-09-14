#!/usr/bin/python3
"""
Utility functions used by routes
"""
import secrets
import os
from PIL import Image
from appmodels import db, app
from appmodels.models import User
import smtplib
from email.message import EmailMessage

def save_picture(form_picture):
    """
    A function that saves the image uploaded to the system by users
    """
    random_hex = secrets.token_hex(6)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn
