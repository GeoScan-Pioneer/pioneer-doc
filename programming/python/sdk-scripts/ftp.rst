Скрипт FTP
==========

Скрипт FTP служит для загрузки и запуска ранее созданного LUA-скрипта.

Разбор скрипта
--------------

  .. code-block:: python

    import pathlib, sys, os, time
    from pioneer_sdk.mavsub import ftp as mavftp
    from pioneer_sdk.piosdk import MavlinkConnectionFactory, Pioneer
    from pioneer_sdk.tools import lua


    def list_directory(mavlink_connection):
        ftp_wrapper = mavftp.FtpWrapper(mavlink_connection)
        print(ftp_wrapper.list_directory("/dev/"))


    def main():
        mavlink_connection = MavlinkConnectionFactory.make_connected_udp_instantiate()
        drone = Pioneer(mavlink_connection=mavlink_connection, logger=True)
        list_directory(mavlink_connection)
        drone.lua_script_upload("pioneer_led_blink.lua")
        drone.lua_script_control("Start")
        time.sleep(2)
        drone.lua_script_control("Stop")


    if __name__ == "__main__":
        main()


1. Импортируем необходимые библиотеки.

2. Создаём функцию 'def list_directory(mavlink_connection)'

3. Создаём функцию 'main()' в которой создаём MavLink-соединение с помощью метода make_connected_udp_instantiate() класса MavlinkConnectionFactory

4. Переменной 'drone' присвояем экземпляр класса Pioneer в который передаём созданное MavLink-соединение. 

5. List.Dir?

6. Вызываем функцию lua_script_upload и передаём путь до файла с LUA-скриптом.

7. После завершения передачи вызываем функцию lua_script_control("Start") которая запускает скрипт.

8. Спустя 2 секунды прерываем выполение скрипты вызовом функции lua_script_control("Stop")

9. Конструкцией 'if __name__ == "__main__":' указываем точку входа в программу и вызываем функцию main().