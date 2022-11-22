Скрипт Manual_speed
===================

Скрипт Manual_speed служит для управления Пионером мини по векторам.

  .. code-block:: python

    from pioneer_sdk import Pioneer
    import time

    if __name__ == '__main__':
        print('start')
        pioneer_mini = Pioneer()
        pioneer_mini.arm()
        pioneer_mini.takeoff()
        t = time.time() # время старта
        while True: # 20 раз в сек отправляем команду полёта
            pioneer_mini.set_manual_speed(vx=0, vy=0, vz=1, yaw_rate=0)
            time.sleep(0.05)
            if time.time() - t > 1: # если прошло больше 1 секунды, выходим из цикла
                break
        time.sleep(4) # 4 секунды ничего не делаем (дрон в этот момент не должен никуда лететь)
        t = time.time() # обновляем время старта
        while True: # 20 раз в сек отправляем команду полёта
            pioneer_mini.set_manual_speed(vx=1, vy=0, vz=0, yaw_rate=0)
            time.sleep(0.05)
            if time.time() - t > 2: # если прошло больше 2 секунд, выходим из цикла
                break
        time.sleep(4) # 4 секунды ничего не делаем
        pioneer_mini.land()

Разбор скрипта
--------------

1. Импортируем необходимые библиотеки и определяем их назначение:

  - | **Pioneer_sdk** – библиотека для управления квадрокоптером;
    | Описание библиотеки Pioneer_sdk - https://pioneer-doc.readthedocs.io/ru/master/programming/python/pioneer-sdk-methods.html;

  - | **time** – библиотека для работы со временем;
    | Описание библиотеки time - https://docs.python.org/3/library/time.html.

  .. code-block:: python

    from pioneer_sdk import Pioneer
    import time

2. Далее используем конструкцию *if \__name_\_ == '__main__':*, которая является точкой входа в программу. Всё, что идёт до этого условия, выполнятся всегда: и при вызове в качестве модуля и при вызове, как исполняемый файл.
  | Подробное описание данной конструкции: https://docs.python.org/3/library/__main__.html

  .. code-block:: python

    if __name__ == '__main__':

3. Выводим строку'start'. Создаём экземпляр класса Pioneer, чтобы начать работать с квадрокоптером. 

  .. code-block:: python

    print('start')
    pioneer_mini = Pioneer()

4. Вызываем функцию *pioneer_mini.arm()* для запуска моторов. Вызываем функцию *pioneer_mini.takeoff()* для взлёта. Объявляем переменную 't' и присваиваем ей значение возвращаемое функцией *time.time().*

  .. code-block:: python

    pioneer_mini.arm()
    pioneer_mini.takeoff()
    t = time.time() # время старта

5. Запускаем цикл отправляющий 20 раз в секунду команду полёта.

  .. code-block:: python

      while True: # 20 раз в сек отправляем команду полёта
        pioneer_mini.set_manual_speed(vx=0, vy=0, vz=1, yaw_rate=0)
        time.sleep(0.05)
        if time.time() - t > 1: # если прошло больше 1 секунды, выходим из цикла
          break

6. Выставляем паузу в 4 секнды и обновляем время старта.

  .. code-block:: python

    time.sleep(4) # 4 секунды ничего не делаем (дрон в этот момент не должен никуда лететь)
    t = time.time() # обновляем время старта

7. Запускаем цикл отправляющий 20 раз в секунду команду полёта.

  .. code-block:: python

      while True: # 20 раз в сек отправляем команду полёта
        pioneer_mini.set_manual_speed(vx=1, vy=0, vz=0, yaw_rate=0)
        time.sleep(0.05)
        if time.time() - t > 2: # если прошло больше 2 секунд, выходим из цикла
          break

8. Выставляем паузу в 4 секунды и вызываем функцию посадки *pioneer_mini.land()*.

  .. code-block:: python

      time.sleep(4) # 4 секунды ничего не делаем
      pioneer_mini.land()