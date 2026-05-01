[app]
title = My First App
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

# Android مشخصات
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b

# خروجی
android.release_artifact = apk

[buildozer]
log_level = 2
