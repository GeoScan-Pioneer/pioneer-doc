Подготовка к программированию Pioneer Mini на Python
====================================================

Данная страница посвящена общей настройки среды для программирования PyCharm. Здесь описано как установить всё необходимое ПО, подключить проект pioneer_sdk, настроить квадрокоптер для корректной работы с ПК.


Используемое ПО
~~~~~~~~~~~~~~~

Необходимые программы:

* `Pioneer Station 1.11.; <https://dl.geoscan.aero/pioneer/upload/GCS/GEOSCAN_Pioneer_Station.exe>`__
* `PyCharm Community Edition. <https://www.jetbrains.com/ru-ru/pycharm/download/download-thanks.html?platform=windows&code=PCC>`__

Необходимые архивы и ПО для Пионера:

* Скачанный ZIP архив с GitHub;
* Прошивка и параметры для автопилота для Pioneer Mini;
* Актуальная прошивка ESP-32.


Процесс настройки
~~~~~~~~~~~~~~~~~

1.  Для начала необходимо установить среду разработки PyCharm Community

    Ссылка на `загрузку <https://www.jetbrains.com/ru-ru/pycharm/download/download-thanks.html?platform=windows&code=PCC>`__ PyCharm Community Edition.

.. figure:: media/image1.png
   :align: center

2. Далее необходимо скачать ZIP архив с библиотекой для Pioneer Mini с GitHub.

`Ссылка на архив pioneer_sdk <https://github.com/geoscan/pioneer_sdk>`__

|image2|\ |image1|

3. Данный архив необходимо распаковать в заранее созданную папку.
   Сделайте это в удобной для вас директории.

.. figure:: media/image4.png
   :align: center

4. Запускаем PyCharm и нажимаем кнопку “Open”, в качестве
   открываемой папки выбираем ранее распакованный архив.

.. figure:: media/image5.png
   :align: center


.. figure:: media/image6.png
   :align: center

Ожидаем пока PyCharm создаст и настроит виртуальную среду. Это можно отследить по полоске прогресса в нижнем правом углу программы.

.. figure:: media/image6-1.PNG
   :align: center


5. Чтобы коптер мог выполнять Python скрипты на нём должна быть установлена следующая прошивка “АП_mavlink.bin” и поставлены параметры “mavlink_param.properties”.

1) Ссылка на скачивание актуальных файлов:

Актуальное ПО на странице :doc:`../../downloads/software-d`

2) Как установить прошивку АП на Пионер Мини:

`Обновление прошивки автопилота <https://pioneer-doc.readthedocs.io/ru/master/instructions/pioneer-mini/settings/firmware_upgrade.html>`__

3) Если прошивка ESP32 устарела, то её необходимо обновить:

`Обновление прошивки ESP32 <https://pioneer-doc.readthedocs.io/ru/master/instructions/pioneer-mini/settings/esp32-update.html>`__

4) Как обновить параметры:

`Загрузка параметров АП <https://pioneer-doc.readthedocs.io/ru/master/instructions/pioneer-mini/settings/autopilot\_parameters.html>`__



6. Далее в актуальных параметрах автопилота необходимо изменить значение uMux с «1» на «3», тем самым коптер перейдёт из режима управления с телефона в режим выполнения python-скриптов.

.. figure:: media/image7.png
   :align: center

.. attention:: Переключите параметр uMux в "1", если снова хотите использовать приложение Geoscan Jump.


7.  Включаем Pioneer Mini и подключаемся к нему по Wi-Fi. Имя сети каждого коптера уникально! Но пароль у всех одинаковый: «12345678».

.. figure:: media/image8.png
   :align: center

.. attention:: Обратите внимание, профиль сети в настройках Windows должен быть **«частным»**, а не
               общественным. В противном случае передача данных между устройствами
               не будет работать должным образом!

.. figure:: media/image9.png
   :align: center

.. attention:: Также для данной сети необходимо отключить Брандмауэр Windows!

.. figure:: media/image10.png
   :align: center

8. Пример запуска скрипта

.. figure:: media/image11.png
   :align: center

Теперь коптер готов выполнять скрипты, самое время разобраться как их запускать! Первым делом необходимо произвести калибровку камеры нашего квадрокоптера. Для этого в PyCharm необходимо открыть скрипт «get\_camera\_samples.py».

9. Скрипт необходимо добавить в список конфигураций, который находится в правом верхнем углу.

.. figure:: media/image13.png
   :align: center

.. figure:: media/image12.png
   :align: center

Здесь необходимо указать путь к скрипту.

.. figure:: media/image14.png
   :align: center


10. После того, как в списке появился выбранный скрипт, можно нажимать кнопку старт.

.. figure:: media/image15.png
   :align: center

.. attention:: Внимательно смотрите за тем, какой скрипт у вас выбран в списке. Запускаемый код не всегда соответствует открытому в текущий момент коду.

11. Для калибровки камеры необходимо распечатать специальное изображение на листе А4. В процессе работы программы необходимо сделать 15 снимков листа. Снимки делаются на кнопку «P» на клавиатуре. По завершению выполнения программы в терминале появится сообщение об успешном завершении калибровки. А в папке проекта "result" появятся полученные фотографии (матрица камеры).

*  `Ссылка на скачивание изображения для калибровки камеры <https://raw.githubusercontent.com/opencv/opencv/master/doc/pattern.png>`__

*  :download:`Ссылка на скачивание aruco-маркера для скрипта aruco-flight <files/PioneerSDK-aruco.pdf>`

.. figure:: media/image16.png
   :align: center


.. |image0| image:: media/image1.png
   :width: 6.49653in
   :height: 3.99514in
.. |image1| image:: media/image2.png
   :width: 3.94792in
   :height: 3.71875in
.. |image2| image:: media/image3.png
   :width: 6.49653in
   :height: 3.60139in
.. |image3| image:: media/image4.png
   :width: 6.49653in
   :height: 3.86389in
.. |image4| image:: media/image5.png
   :width: 5.77083in
   :height: 4.29167in
.. |image5| image:: media/image6.png
   :width: 4.47917in
   :height: 5.15694in
.. |image6| image:: media/image7.png
   :width: 6.49653in
   :height: 3.35278in
.. |image7| image:: media/image8.png
   :width: 3.75000in
   :height: 1.76667in
.. |image8| image:: media/image9.png
   :width: 5.94792in
   :height: 4.94792in
.. |image9| image:: media/image10.png
   :width: 3.07292in
   :height: 4.13542in
.. |image10| image:: media/image11.png
   :width: 3.65833in
   :height: 1.58333in
.. |image11| image:: media/image12.png
   :width: 4.37500in
   :height: 3.42708in
.. |image12| image:: media/image13.png
   :width: 4.38542in
   :height: 1.65625in
.. |image13| image:: media/image14.png
   :width: 6.49653in
   :height: 1.18194in
.. |image14| image:: media/image15.png
   :width: 3.63542in
   :height: 0.94792in
.. |image15| image:: media/image16.png
   :width: 6.18264in
   :height: 3.47639in
