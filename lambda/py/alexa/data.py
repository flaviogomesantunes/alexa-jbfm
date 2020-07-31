# -*- coding: utf-8 -*-
import gettext

_ = gettext.gettext

WELCOME_MSG = _("Welcome to {}")
HELP_MSG = _("Welcome to {}. You can play, stop, resume listening.  How can I help you ?")
UNHANDLED_MSG = _("Sorry, I could not understand what you've just said.")
CANNOT_SKIP_MSG = _("This is radio, you have to wait for previous or next track to play.")
RESUME_MSG = _("Resuming {}")
NOT_POSSIBLE_MSG = _("This is radio, you can not do that.  You can ask me to stop or pause to stop listening.")
STOP_MSG = _("Goodbye.")
DEVICE_NOT_SUPPORTED = _("Sorry, this skill is not supported on this device")

TEST = _("test english")
TEST_PARAMS = _("test with parameters {} and {}")

jingle = {
    "db_table": "my_radio",
    "play_once_every": 1000*60*60*24  # 24 hours
}

pt = {
    "card": {
        "title": 'JBFM',
        "text": 'Rádio JBFM, Música e Informação.',
        "large_image_url": 'https://jb.fm/alexa/logo-512.png',
        "small_image_url": 'https://jb.fm/alexa/logo-108.png'
    },
    #"url": 'https://audio1.maxi80.com',
    "url": 'https://18443.live.streamtheworld.com/JBFMAAC.aac',
    "start_jingle": 'https://jb.fm/alexa/vinheta.m4a'
}

en = {
    "card": {
        "title": 'JBFM',
        "text": 'JBFM radio',
        "large_image_url": 'https://jb.fm/alexa/logo-512.png',
        "small_image_url": 'https://jb.fm/alexa/logo-108.png'
    },
    "url": 'https://18443.live.streamtheworld.com/JBFMAAC.aac',
    "start_jingle": 'https://jb.fm/alexa/vinheta.m4a'
}