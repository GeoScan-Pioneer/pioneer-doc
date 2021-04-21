Скрипт WASD_flight
==================

Скрипт WASD_flight является примером, того как можно управлять квадрокоптером Pioneer Mini с клавиатуры ПК. Служит для изучение методов
перемещения квадрокоптера и метода библиотеки OpenCV по работе с клавиатурой.

Скрипт позволяет управлять квадрокоптером при помощи клавиш "W","A","S","D","Q","E","H","L" и будет выполнятся до нажатия на клавишу "Escape".

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

  - | *command_x = float(0)* --- Переменная отвечающая за перемещение по оси X.



  - | *command_y = float(0)* --- Переменная отвечающая за перемещение по оси Y.

  - | *command_z = float(1)* --- Переменная отвечающая за перемещение по оси Z.

  - | *command_yaw = math.radians(float(0))* --- Переменная отвечающая за рысканье. Перевод из градусов в радианы.

  - | *increment_xy = float(0.2)* --- Шаг по осям X и Y, в метрах.

  - | *increment_z = float(0.1)* --- Шаг по высоте Z, в метрах.

  - | *increment_deg = math.radians(float(90))* --- Шаг по рысканью в 90 градусов.

  - | *new_command = False* --- Флаг на получение новых команд.

  .. code-block:: python

    command_x = float(0)
    command_y = float(0)
    command_z = float(1)
    command_yaw = math.radians(float(0))
    increment_xy = float(0.2)
    increment_z = float(0.1)
    increment_deg = math.radians(float(90))
    new_command = False

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

8. Создаём обработчик нажатий и привязываем к клавишам изменение координат и рысканья:

  .. code-block:: python

    key = cv2.waitKey(1)
    if key == 27:  # esc
        print('esc pressed')
        cv2.destroyAllWindows()
        pioneer_mini.land()
        break
    elif key == ord('w'):
        print('w')
        command_y += increment_xy
        new_command = True
    elif key == ord('s'):
        print('s')
        command_y -= increment_xy
        new_command = True
    elif key == ord('a'):
        print('a')
        command_x -= increment_xy
        new_command = True
    elif key == ord('d'):
        print('d')
        command_x += increment_xy
        new_command = True
    elif key == ord('q'):
        print('q')
        command_yaw += increment_deg
        new_command = True
    elif key == ord('e'):
        print('e')
        command_yaw -= increment_deg
        new_command = True
    elif key == ord('h'):
        print('h')
        command_z += increment_z
        new_command = True
    elif key == ord('l'):
        print('l')
        command_z -= increment_z
        new_command = True

9. Когда выполнятся одно из этих условий срабатывает триггер, который отслеживается в условии **if new_command:**. Далее, методом go_to_local_point(x, y, z, yaw)происходит перемещение в актуальные координаты, где:

  | x – Перемещение по оси Х, задаётся в метрах;
  | y – Перемещение по оси Y, задаётся в метрах;
  | z – Перемещение по оси Z, задаётся в метрах;
  | yaw – Рысканье, задаётся в радианах;

  В конце флаг необходимо сбросить. new_point = False

  .. code-block:: python

    if new_point:
      pioneer_mini.go_to_local_point(x=command_x, y=command_y, z=flight_height, yaw=command_yaw)
      new_point = False

Вопросы для самостоятельного разбора.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1) Дописать алгоритм, чтобы вместе с поворотом коптера по углу рысканья поворачивались оси X и Y.
| 2) Добавить чтобы при нажатии клавиши коптер не только менял свое направление движения, но и производил индикацию светодиодами.
| 3) Добавьте в данный скрипт возможность сохранения фотографии, используя в качестве примера скрипт get_camera_samples.
