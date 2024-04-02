# vk_ds_test_case_music_recsys
vk data sciece internship test case - music rec system

## Задание
![image](https://github.com/maximborodai/vk_ds_test_case_music_recsys/assets/96576515/cffe81e3-ae32-4ec7-9d53-fb9d95c8c8b9)


**Лучший результат - NDCG@20 = 0.7695093120340937, с помощью XGBClassifier**

## Структура проекта

- Файлы с данными - исходными и обработанными (8 Гб) - я решил не заливать
- EDA.ipynb - развернутый анализ данных датасета
- feature_engineering.ipynb - предобработка данных и, собственно, инжиниринг фичей
- models.ipynb - ноутбук с обучением нескольких моделей (на большее не хватило времени), и результатами
- service_func - модуль с служебными функиями, чтобы разгрузить ноутбуки от большого числа строк кода

