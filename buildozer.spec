[app]
title = ChessVision AI
package.name = chessvision
package.domain = org.chessvision
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ini
version = 0.1

requirements = python3,kivy,opencv,numpy

orientation = portrait
osx.kivy_version = 2.1.0

fullscreen = 0
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_build_tools_version = 1
