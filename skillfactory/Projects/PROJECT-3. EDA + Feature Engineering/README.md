# **Проект 3. Предсказание рейтинга отеля на Booking**

## Оглавление
[1. Описание проекта](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#описание-проекта)

[2. Какой кейс решаем?](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#этапы-работы-над-проектом)

[5. Результат](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#результаты)

### Описание проекта
Определить ключевые закономерности в данных и создать эффективную модель, способную предсказывать настоящий рейтинг отеля.


:arrow_up:[к оглавлению](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#оглавление)


### Какой кейс решаем?
Представим, что мы работаем дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

:arrow_up:[к оглавлению](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/ProjectsPROJECT-3. EDA + Feature Engineering
/README.md#оглавление)


### Краткая информация о данных

Исходные данные:

https://disk.yandex.ru/d/27wdjC1V4RexYg
https://disk.yandex.ru/d/EijHyTF_mVCy_w

Данные хранятся по ссылке: 
Первоначальная версия датасета содержит 17 полей со следующей информацией:

* hotel_address — адрес отеля;
* review_date — дата, когда рецензент разместил соответствующий отзыв;
* average_score — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
* hotel_name — название отеля;
* reviewer_nationality — страна рецензента;
* negative_review — отрицательный отзыв, который рецензент дал отелю;
* review_total_negative_word_counts — общее количество слов в отрицательном отзыв;
* positive_review — положительный отзыв, который рецензент дал отелю;
* review_total_positive_word_counts — общее количество слов в положительном отзыве;
* reviewer_score — оценка, которую рецензент поставил отелю на основе своего опыта;
* total_number_of_reviews_reviewer_has_given — количество отзывов, которые рецензенты дали в прошлом;
* total_number_of_reviews — общее количество действительных отзывов об отеле;
* tags — теги, которые рецензент дал отелю;
* days_since_review — количество дней между датой проверки и датой очистки;
* additional_number_of_scoring — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
* lat — географическая широта отеля;
* lng — географическая долгота отеля.

:arrow_up:[к оглавлению](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#оглавление)


### Этапы работы над проектом
Проект будет состоять из 8 частей:

1. **Импорт библиотек и загрузка данных**  
   `pandas`, `numpy`, `matplotlib`, `seaborn` и др.

2. **Предварительный анализ структуры данных**  
   Размерность, типы признаков, наличие пропусков.

3. **Очистка данных**  
   Обработка пропусков, приведение к нужным форматам.

4. **Exploratory Data Analysis (EDA)**  
   Гистограммы, boxplot, тепловые карты корреляции, распределения, анализ категориальных признаков.

5. **Feature Engineering**  
   Создание новых признаков, логические признаки.

6. **Подготовка данных для модели**  
   - Кодирование категориальных переменных 
   - Оценка корреляций между признаками и целевой переменной  
   - Анализ важности признаков (feature importance)  
   - Удаление слабоинформативных или избыточных признаков
   - Нормализация

7. **Построение модели**  
   Выбор алгоритма Random Forest и обучение с подобранными параметрами.

8. **Оценка модели**  
   Оценка качества модели с помощью метрики MAPE.
   
:arrow_up:[к оглавлению](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#оглавление)


### Результаты
В результате работы над проектом были исследованы данные об отзывах на Booking, проведен предварительный анализ данных, очистка данных от пропусков, проанализированы и преобразованы имеющиеся признаки, созданы новые информативные признаки из имеющихся, создана модель машинного обучения и оценена с помощью метрики MAPE.

:arrow_up:[к оглавлению](https://github.com/Ksuchilda/sf_data_science/blob/main/skillfactory/Projects/PROJECT-3. EDA + Feature Engineering
/README.md#оглавление)

