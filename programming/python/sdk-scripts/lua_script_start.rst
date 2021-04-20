Скрипт LUA_script_start
=======================

Скрипт LUA_script_start служит для ознакомления с методом управления LUA-скриптом, заранее загруженного на квадрокоптер Pioneer Mini.

Разбор скрипта
--------------

1. Импортируем необходимые библиотеки и определяем их назначение:

  - | **Pioneer_sdk** – библиотека для управления квадрокоптером;
    | Описание библиотеки Pioneer_sdk - https://pioneer-doc.readthedocs.io/ru/master/programming/python/pioneer-sdk-methods.html;

  - | **sys** – библиотека, которая обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python;
    | Описание библиотеки sys - https://docs.python.org/3/library/sys.html;

  .. code-block:: python

    from pioneer_sdk import Pioneer
    import sys

2. Далее используем конструкцию **if \__name_\_ == '__main__':**, которая является точкой входа в программу. Всё, что идёт до этого условия, выполнятся всегда: и при вызове в качестве модуля и при вызове, как исполняемый файл.

  | Подробное описание данной конструкции: https://docs.python.org/3/library/__main__.html

  .. code-block:: python

    if __name__ == '__main__':

3. Создаём экземпляр класса Pioneer, чтобы начать работать с квадрокоптером.

  .. code-block:: python

    pioneer_mini = Pioneer()

   С понятием, что такое класс и его экземпляры можно ознакомиться по ссылке https://docs.python.org/3/tutorial/classes.html

4. Методом **.lua_script_control()** Можно запустить или остановить выполнение LUA скрипта. Аргумент *(‘Start’)* – запускает скрипт, аргумент *(‘Stop’)* – останавливает скрипт.

  .. code-block:: python

    pioneer_mini.lua_script_control('Start')

5. После запуска скрипта запускаем бесконечный цикл, в котором используем следующую конструкцию:

  .. code-block:: python

    while True:
    try:
        pass
    except KeyboardInterrupt:
        pioneer_mini.lua_script_control('Stop')
        sys.exit()

  Т.е. LUA скрипт будет выполнятся до тех пор, пока не будет остановлен Python скрипт. Метод **KeyboardInterrupt** отслеживает прерывание скрипта (При помощи красного квадрата или Ctrl+C). В конце **sys.exit()** выходит из программы.
