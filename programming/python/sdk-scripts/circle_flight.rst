Cкрипт Circle_flight
====================

Скрипт Circle_flight служит для изучение методов перемещения квадрокоптера, а также показывает один из вариантов задания полётного
маршрута для Pioneer Mini.

Разбор скрипта
--------------

1. Импортируем необходимые библиотеки и определяем их назначение:

  - | **Pioneer_sdk** – библиотека для управления квадрокоптером;
    | Описание библиотеки Pioneer_sdk - https://pioneer-doc.readthedocs.io/ru/master/programming/python/pioneer-sdk-methods.html;

  - | **NumPy** – библиотека для работы с массивами данных;
    | Описание библиотеки NumPy - https://numpy.org/doc/stable/;

  - | **Cv2** – библиотека машинного зрения;
    | Описание библиотеки OpenCV - https://docs.opencv.org/master/index.html;

  - | **Math** – библиотека для работы с математическими функциями;
    | Описание библиотеки math - https://docs.python.org/3/library/math.html.


  .. code-block:: python

    from pioneer_sdk import Pioneer
    import cv2
    import math
    import numpy as np


2. Создаём ряд переменных:

  - | *angle = float(0)* --- переменная отвечающая за текущий угол окружности;

  - | *number_of_points = 24* --- количество точек составляющих окружность;

  - | *increment = float(360 / number_of_points)* --- расчёт приращения в градусах;

  - | *radius = 0.6* --- указываем радиус окружности в метрах;

  - | *flight_height = float(1)* --- указываем высоту полёта в метрах;

  - | *last_point_reached = False* --- флаг на достижение последней точки;

  - | *command_x = radius \* math.cos(math.radians(angle))* --- координаты по оси X;

  - | *command_y = radius \* math.sin(math.radians(angle))* --- Координаты по оси Y;

  - | *command_yaw = math.radians(angle)* --- рысканье квадрокоптера.

  - | *new_point = True* --- флаг на получение новой точки;

  - | *p_r = False* --- флаг срабатывающий на достижение точки.

  .. code-block:: python

    angle = float(0)
    number_of_points = 24
    increment = float(360 / number_of_points)
    radius = 0.6
    flight_height = float(1)
    last_point_reached = False

    command_x = radius * math.cos(math.radians(angle))
    command_y = radius * math.sin(math.radians(angle))
    command_yaw = math.radians(angle)

    new_point = True
    p_r = False

3. Далее используем конструкцию **if \__name_\_ == '__main__':**, которая является точкой входа в программу. Всё, что идёт до этого условия, выполнятся всегда: и при вызове в качестве модуля и при вызове, как исполняемый файл.

  | Подробное описание данной конструкции: https://docs.python.org/3/library/__main__.html

  .. code-block:: python

    if __name__ == '__main__':

4. Сообщаем о запуске моторов:

  .. code-block:: python

    print('start')

  И создаём экземпляр класса Pioneer, чтобы начать работать с квадрокоптером.

  .. code-block:: python

    pioneer_mini = Pioneer()

  С понятием, что такое класс и его экземпляры можно ознакомиться по ссылке https://docs.python.org/3/tutorial/classes.html

5. Запускаем моторы и взлетаем:

  .. code-block:: python

    pioneer_mini.arm()
    pioneer_mini.takeoff()

  В бесконечном цикле будем отслеживать пройдённый маршрут, рассчитывать координаты и задавать перемещение квадрокоптеру, а также получать изображение от коптера и выводить его на экран. Это будет выполнятся до нажатия на клавишу Escape:

  .. code-block:: python

    while True:

6. В переменную **camera_frame** передаём изображение от квадрокоптера:

  - | **cv2.imdecode(buf, flag)** – чтение изображения из указного массива, где:
    | *buf* – читаемый массив;
    | *flag* – тип изображения.

  - | **np.frombuffer(buffer,dtype)** - интерпретирует буфер как одномерный массив, где:
    | *buffer* - буфер-подобный объект;
    | *dtype* – тип данных, которым будут интерпретироваться элементы массива.

  - | **pioneer_sdk.get_raw_video_frame()** – возвращает массив байт представляющий собой jpg картнку.

  Выходит, следующая строчка:

  .. code-block:: python

    camera_frame = cv2.imdecode(np.frombuffer(pioneer_mini.get_raw_video_frame(), dtype=np.uint8), cv2.IMREAD_COLOR)

7. Затем выводим camera_frame на экран:

  | **cv2.imshow(name,image)** – выводит изображение в окне, где:
  | *name* – имя создаваемого окна;
  | *image* - выводимое изображение.

  .. code-block:: python

    cv2.imshow('pioneer_camera_stream', camera_frame)

8. Если флаг на получение новой точки выставлен, то методом **go_to_local_point(x, y, z, yaw)** происходит перемещение в актуальные координаты, где:

  | x – Перемещение по оси Х, задаётся в метрах;
  | y – Перемещение по оси Y, задаётся в метрах;
  | z – Перемещение по оси Z, задаётся в метрах;
  | yaw – Рысканье, задаётся в радианах;

  В конце флаг необходимо сбросить. new_point = False

  .. code-block:: python

    if new_point:
      pioneer_mini.go_to_local_point(x=command_x, y=command_y, z=flight_height, yaw=command_yaw)
      new_point = False

9. Если точка достигнута, то выставляется флаг на перерасчёт координат. Метод **point_reached()** отслеживает достижение точки.

  .. code-block:: python

    if pioneer_mini.point_reached():
    p_r = True

10. Как только срабатывает триггер **p_r**, проверяем равен ли угол **angle** 360 градусам, т.е. завершена ли окружность. Если да, то выставляется
    флаг о достижении последней точки **last_point_reached**, иначе производится расчёт координат для новой точки:

  .. code-block:: python

    if p_r:
      if angle == 360:
          last_point_reached = True
      else:
        angle += increment
        command_x = radius * math.cos(math.radians(angle))
        command_y = radius * math.sin(math.radians(angle))
        command_yaw += math.radians(increment)
        new_point = True
      p_r = False

11. Описываем условия посадки и выхода из программы: Esc – преждевременная посадка и посадка по завершению окружности:

  .. code-block:: python

    key = cv2.waitKey(1)
    if (key == 27) | last_point_reached:  # esc
      print('esc pressed or mission complete')
      cv2.destroyAllWindows()
      pioneer_mini.land()
      exit(0)

Вопросы для самостоятельного разбора.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1) Напишите функцию позволяющую совершать полет по траектории "8" с заданными параметрами.
| 2) Напишите функцию позволяющую совершать полет по траектории "квадрат" с заданными параметрами.
| 3) Напишите алгоритм позволяющий коптеру пролетать по точкам из массива (X, Y, Z)
| 4) Добавьте в скрипт сохранение фотографий в заданных точках (не во всех, а только в заданных).
| 5) Удалите из скрипта вывод изображения без потери функциональности полета.
