[app]

# (str) Title of your application
title = Hello App

# (str) Package name
package.name = helloapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# Android specific
#

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) The Android arch to build for
android.arch = armeabi-v7a
