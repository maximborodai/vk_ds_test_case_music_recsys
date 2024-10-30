# vk_ds_test_case_music_recsys
Тестовое задание для VK - рекомендательная система треков релевантных для пользователя

## Задание
![image](https://github.com/maximborodai/vk_ds_test_case_music_recsys/assets/96576515/cffe81e3-ae32-4ec7-9d53-fb9d95c8c8b9)

датасет: https://www.kaggle.com/competitions/kkbox-music-recommendation-challenge/data

## Лучший результат
**Лучший результат - NDCG@20 = 0.7695093120340937, с помощью XGBClassifier**

## Структура проекта

- EDA.ipynb - развернутый разведочный анализ данных датасета
- feature_engineering.ipynb - предобработка данных и, собственно, инжиниринг фичей
- models.ipynb - ноутбук с обучением нескольких моделей (на большее не хватило времени), и результатами
- service_func - модуль с служебными функиями, чтобы разгрузить ноутбуки от большого числа строк кода

