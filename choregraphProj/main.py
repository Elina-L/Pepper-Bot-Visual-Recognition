#!/usr/bin/env python

import json
import os
import qi
import random
import requests
import signal
import sys
import time

class PythonAppMain(object):
    subscriber_list = []
    loaded_topic = ""

    def __init__(self, application):
        # Getting a session that will be reused everywhere
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)

        # Do some initializations before the service is registered to NAOqi
        self.logger.info("Initializing...")
        # @TODO: insert init functions here
        self.create_signals()
        self.logger.info("Initialized!")


    @qi.nobind
    def start_app(self):
        # do something when the service starts
        self.logger.info("Starting app...")

        try:
            ts = self.session.service("ALTabletService")
            ts.resetTablet()
            #ts.showWebview()
            self.logger.info("Tablet reset")
        except Exception, e:
            self.logger.info("Error while loading tablet: {}".format(e))

        self.show_screen()
        self.start_dialog()
        self.logger.info("Started!")


    @qi.nobind
    def stop_app(self):
        # To be used if internal methods need to stop the service from inside.
        # external NAOqi scripts should use ALServiceManager.stopService if they need to stop it.
        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!")


    @qi.nobind
    def cleanup(self):
        # called when your module is stopped
        self.logger.info("Cleaning...")
        # @TODO: insert cleaning functions here
        self.disconnect_signals()
        self.stop_dialog()
        self.hide_screen()
        self.logger.info("Cleaned!")


    @qi.nobind
    def create_signals(self):
        self.logger.info("Creating PlayGames events...")
        # When you can, prefer qi.Signals instead of ALMemory events
        memory = self.session.service("ALMemory")
        global platform_short
        global OS_short
        global type_short
        global size_short
        global first_time

        #first_time = "yes"
        first_time = "no"

        event_name = "PlayGames/PowerAiVision"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_power_ai_vision)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_PowerAiVision"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_power_ai_vision)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/TakePicture"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_take_picture)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_TakePicture"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_take_picture)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/PlayMore"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_play_more)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_PlayMore"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_play_more)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/PlayMoreYes"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_play_more_yes)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_PlayMoreYes"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_play_more_yes)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/IsCorrect"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_is_correct)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_IsCorrect"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_is_correct)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/IsCorrectYes"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_correct)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_IsCorrectYes"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_correct)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/IsCorrectNo"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_incorrect)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event power ai vision created")

        event_name = "Button_IsCorrectNo"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_incorrect)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("event button power ai vision created")

        event_name = "PlayGames/OnExit"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_exit)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("Events PlayJeopardy, TellMeAJoke & onExit created!")


    @qi.nobind
    def disconnect_signals(self):
        self.logger.info("Unsubscribing to all events...")
        for sub, i in self.subscriber_list :
            try:
                sub.signal.disconnect(i)
            except Exception, e:
                self.logger.info("Error unsubscribing: {}".format(e))
        self.logger.info("Unsubscribe done!")


    @qi.nobind
    def start_dialog(self):
        self.logger.info("Loading color dialog")
        dialog = self.session.service("ALDialog")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #topic_path1 = os.path.realpath(os.path.join(dir_path, "color", "color_enu.top"))
        #topic_path2 = os.path.realpath(os.path.join(dir_path, "edb", "edb_enu.top"))
        # self.logger.info("File is: {}".format(topic_path1))
        try:
            topic_path = os.path.realpath(os.path.join(dir_path, "color", "color_enu.top"))
            self.loaded_topic = dialog.loadTopic(topic_path)
            dialog.activateTopic(self.loaded_topic)
            self.logger.info("after loading and activating color")

            dialog.subscribe(self.service_name)
            self.logger.info("Dialogs loaded!")
        except Exception, e:
            self.logger.info("Error while loading dialog: {}".format(e))


    @qi.nobind
    def ready_picture_dialog(self):
        self.logger.info("Loading ready_picture dialog")
        dialog = self.session.service("ALDialog")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #topic_path1 = os.path.realpath(os.path.join(dir_path, "color", "color_enu.top"))
        #topic_path2 = os.path.realpath(os.path.join(dir_path, "edb", "edb_enu.top"))
        # self.logger.info("File is: {}".format(topic_path1))
        try:
            topic_path = os.path.realpath(os.path.join(dir_path, "ready_picture", "ready_picture_enu.top"))
            self.loaded_topic = dialog.loadTopic(topic_path)
            dialog.activateTopic(self.loaded_topic)
            self.logger.info("after loading and activating ready_picture")

            dialog.subscribe(self.service_name)
            self.logger.info("Dialogs loaded!")
        except Exception, e:
            self.logger.info("Error while loading dialog: {}".format(e))


    @qi.nobind
    def is_correct_dialog(self):
        self.logger.info("Loading is_correct_dialog dialog")
        dialog = self.session.service("ALDialog")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #topic_path1 = os.path.realpath(os.path.join(dir_path, "color", "color_enu.top"))
        #topic_path2 = os.path.realpath(os.path.join(dir_path, "edb", "edb_enu.top"))
        # self.logger.info("File is: {}".format(topic_path1))
        try:
            topic_path = os.path.realpath(os.path.join(dir_path, "is_correct", "is_correct_enu.top"))
            self.loaded_topic = dialog.loadTopic(topic_path)
            dialog.activateTopic(self.loaded_topic)
            self.logger.info("after loading and activating is_correct")

            dialog.subscribe(self.service_name)
            self.logger.info("Dialogs loaded!")
        except Exception, e:
            self.logger.info("Error while loading dialog: {}".format(e))


    @qi.nobind
    def play_more_dialog(self):
        self.logger.info("Loading play_more_dialog dialog")
        dialog = self.session.service("ALDialog")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #topic_path1 = os.path.realpath(os.path.join(dir_path, "color", "color_enu.top"))
        #topic_path2 = os.path.realpath(os.path.join(dir_path, "edb", "edb_enu.top"))
        # self.logger.info("File is: {}".format(topic_path1))
        try:
            topic_path = os.path.realpath(os.path.join(dir_path, "play_more", "play_more_enu.top"))
            self.loaded_topic = dialog.loadTopic(topic_path)
            dialog.activateTopic(self.loaded_topic)
            self.logger.info("after loading and activating play_more_dialog")

            dialog.subscribe(self.service_name)
            self.logger.info("Dialogs loaded!")
        except Exception, e:
            self.logger.info("Error while loading dialog: {}".format(e))


    @qi.nobind
    def activate_Main(self):
        self.logger.info("activating main dialog")
        dialog = self.session.service("ALDialog")
        dialog.activateTopic("color")
        dialog.setFocus("color")


    def deactivate_Main(self):
        self.logger.info("deactivating main dialog")
        dialog = self.session.service("ALDialog")
        try:
            dialog.deactivateTopic("color")
        except Exception, e:
            system.info.logger("color dialog not activated")


    def stop_dialog(self):
        self.logger.info("Unloading dialog")
        try:
            dialog = self.session.service("ALDialog")
            dialog.unsubscribe(self.service_name)
            dialog.deactivateTopic(self.loaded_topic)
            dialog.unloadTopic(self.loaded_topic)
            self.logger.info("Dialog unloaded!")
        except Exception, e:
            self.logger.info("Error while unloading dialog: {}".format(e))


    @qi.nobind
    def show_screen(self):
        folder = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.logger.info("Loading tablet page for app: {}".format(folder))
        try:
            ts = self.session.service("ALTabletService")
            ts.loadApplication(folder)
            ts.showWebview()
            self.logger.info("Tablet loaded!")
        except Exception, e:
            self.logger.info("Error while loading tablet: {}".format(e))


    @qi.bind(methodName="onShowPicture", paramsType=(qi.String,), returnType=qi.Void)
    def on_show_picture(self, value, value1):
        tablet = self.session.service("ALTabletService")
        # clear out what is on the tablet now
        # tablet.hideImage()
        package_id = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.logger.info("showing image: {}".format(package_id))
        tablet.setBackgroundColor(value1)
        tablet.showImageNoCache("http://198.18.0.1/apps/" + package_id + "/" + str(value))


    @qi.nobind
    def hide_screen(self):
        self.logger.info("hiding screen")
        try:
            tablet = self.session.service("ALTabletService")
            tablet.hide()
            #tablet.hideWebview()
            #tablet.cleanWebview()

        except Exception, e:
            self.logger.info("Error while unloading tablet: {}".format(e))


    @qi.nobind
    def hide_html(self):
        self.logger.info("hiding screen")
        try:
            tablet = self.session.service("ALTabletService")
            #tablet.hide()
            tablet.hideWebview()
            tablet.cleanWebview()

        except Exception, e:
            self.logger.info("Error while unloading tablet: {}".format(e))

    @qi.bind(methodName="onTakePicture", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_take_picture(self, value):
        if value:
            self.logger.info("TakePicture event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()
            tts.say("Smile and say CHEESE!")

            folder = os.path.dirname(os.path.realpath(__file__))
            self.logger.info("Taking the picture: {}".format(folder))
            resolutionMap = {
                '160 x 120': 0,
                '320 x 240': 1,
                '640 x 480': 2,
                '1280 x 960': 3
            }
            cameraMap = {
                'Top': 0,
                'Bottom': 1
            }

            recordFolder = folder + "/html/"

            resolution = resolutionMap['640 x 480']
            cameraID = cameraMap['Top']
            fileName = "photo"
            photocap = self.session.service("ALPhotoCapture")
            if photocap:
                photocap.setResolution(resolution)
                photocap.setCameraID(cameraID)
                photocap.setPictureFormat("jpg")
                photocap.takePicture( recordFolder, fileName )

            time.sleep(2)
            self.on_show_picture("photo.jpg", "#17202a")
            time.sleep(3)
            tts.say("Gotcha!")
            time.sleep(1)
            self.hide_screen()
            self.show_screen()

            ### ANALYZE PICTURE
            tts.say("All right, I'm analyzing your picture now.")

            import rest_client as rc
            response = rc.classify_image(recordFolder + "photo.jpg", True, self)
            tts.say(response)
            self.logger.info("classification is " + str(response))

            ### ASKING IF CORRECT
            self.is_correct_dialog()


    @qi.bind(methodName="onPowerAiVision", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_power_ai_vision(self, value):
        if value:
            self.logger.info("PowerAiVision event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()

            # Dialogue
            tts.say("Great! This is how the game works: first, I'll take a picture.")
            tts.say("Using IBM PowerAI Vision, I'll be able to analyze the picture.")
            tts.say("Right now, I can recognize if a banana is in the picture.")
            tts.say("After we're done playing, I'll delete any images I take")

            ## GET INPUT TO CHANGE ACTIONS
            self.ready_picture_dialog()


    @qi.bind(methodName="onPlayMoreYes", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_play_more_yes(self, value):
        ## GET INPUT TO CHANGE ACTIONS
        if value:
            self.logger.info("Playmore event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()

            ## GET INPUT TO CHANGE ACTIONS
            self.ready_picture_dialog()


    @qi.bind(methodName="onPlayMore", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_play_more(self, value):
        if value:
            self.logger.info("Playmore event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()

            ## GET INPUT TO CHANGE ACTIONS
            self.play_more_dialog()


    @qi.bind(methodName="onIsCorrect", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_is_correct(self, value):
        if value:
            self.logger.info("Playmore event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()

            ## GET INPUT TO CHANGE ACTIONS
            self.is_correct_dialog()


    @qi.bind(methodName="onIsCorrectYes", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_correct(self, value):
        if value:
            self.logger.info("PowerAiVision event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()

            # Dialogue
            tts.say("I'm right? So happy.")
            tts.say("Do you want to play some more?")

            ## GET INPUT TO CHANGE ACTIONS
            self.play_more_dialog()


    @qi.bind(methodName="onIsCorrectNo", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_incorrect(self, value):
        if value:
            self.logger.info("PowerAiVision event: {}".format(value))

            tts = self.session.service("ALTextToSpeech")
            self.stop_dialog()
            self.hide_screen()

            # Dialogue
            tts.say("I'm wrong? So sad.")

            tts.say("Do you still want to try your luck again?")

            ## GET INPUT TO CHANGE ACTIONS
            self.play_more_dialog()


    @qi.bind(methodName="onEventExit", returnType=qi.Void)
    def on_event_exit(self, value):
        ### DELETE ANY IMAGES TAKEN
        # Cool deleting code here
        ###
        self.stop_app()


if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python main.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = PythonAppMain(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.start_app()
    app.run()
    service_instance.cleanup()
    app.session.unregisterService(service_id)
