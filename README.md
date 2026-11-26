# ChessVision AI (Android APK Project)

Проект для автоматического компилирования Android APK с помощью GitHub Actions и Buildozer.

## Как собрать APK через GitHub:
1. Создай новый **публичный или приватный репозиторий** на GitHub.
2. Загрузи все файлы из этого архива в главную ветку (`main`).
3. Перейди во вкладку **Actions** в твоём репозитории на GitHub.
4. Выбери workflow **Build Android APK** и нажми **Run workflow**.
5. Через 10-15 минут сборка завершится, и готовый `.apk` появится в блоке **Artifacts** (внизу страницы выполненного workflow)!

## Структура проекта:
- `main.py` — исходный код приложения (Kivy + OpenCV).
- `buildozer.spec` — конфигурация сборки под Android (разрешения камеры, API, архитектура arm64-v8a).
- `.github/workflows/build.yml` — скрипт автоматической сборки APK на серверах GitHub (Cloud CI/CD).
