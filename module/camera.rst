Камера для фото и видео съемки
==============================

В комплект для фото и видео-съёмки входит модуль с камерой RunCam Hybrid либо RunCam Split в ранней версии.
Модуль камеры RunCam Hybrid включает следующие компоненты: 

**Для Pioneer Base:**

1) Камера RunCam Hybrid (Модуль с объективами + Плата управления)
2) Текстолитовый кронштейн с фиксацией угла наклона с помощью винтов.
3) SD-карта объёмом 64Гб.

**Для Pioneer Max:**

1) Камера RunCam Hybrid (Модуль с объективами + Плата управления)
2) Кронштейн с автофиксацией угла наклона.
3) SD-карта объёмом 64Гб.

Монтаж RunCam Hybrid на Pioneer Base:
-------------------------------------

Модуль камеры подключается к плате расширения следующим образом.

1) 8-пиновые штырьевые разъемы устанавливаются в соответствующие гнёзда на плате расширения.
2) Модуль фиксируется с помощью двух стоек и двух винтов M3.
3) При помощи кабельной сборки подключаем модуль к разъему x7 на плате расширения.

.. figure:: /_static/images/PioBase_RCHybrid_mount.gif
	:align: center

Монтаж RunCam Hybrid на Pioneer Max:
------------------------------------

1) Передняя торцевая часть с установленным модулем фиксируется в нижней пластине по принципу шип-паз.
2) Боковые части рамы и торцевая часть прижимается верхней крышкой и фиксируются с помощью 4-х винтов.
3) При помощи кабельной сборки подключаем модуль к разъему x2 на плате распределения питания.

.. figure:: /_static/images/PIoMax_RCHybrid_mount.gif
	:align: center

Устройство камеры RunCam Hybrid
-------------------------------

Камера RunCam Hybrid состоит из следующих компонентов. Это модуль с двумя объективами и матрицами, плата управления и шлейф соединяющий их между собой.

.. figure:: /_static/images/RCH_descript.png
	:align: center

Начало работы и управление
--------------------------

1) Установите SD-карту в специальный слот на плате управления. Обратите внимание на следующие моменты: Объем накопителя не должен превышать **128 Гб**, а его класс должен быть не ниже **U1** для записи видео в разрешении 2.7К c частотой 60 кадров. Для записи в разрешении 1080p c частотой 120 кадров необходим накопитель класса **U3** или старше. Также следует отметить, что sd-карта должна быть отформатирована в **FAT32(exFAT)**.

2) **Включение** и **выключение** камеры осуществляется долгим нажатием на кнопку вкл/выкл. Также камера включится при подаче питания на квадрокоптер и моментально перейдёт в **режим записи** (если это возможно), сообщая об этом пользователю редким миганием синего светодиода.

3) Для **остановки записи** следует коротко нажать на кнопку питания. Камера перейдет в **режим ожидания**, синий светодиод при этом будет гореть постоянно.

4) **Переключение режимов** осуществляется с помощью долгого нажатия кнопки **MODE**. Переключение будет происходить циклично.

Ниже представлена таблица состояний камеры и их индикация с помощью светодиодов.
Быстро-мигающий синий светодиод предупреждает нас о проблемах с sd-картой либо о её отсутствии. Например карта может быть переполнена, не отформатирована или в целом не подходить для работы с камерой. Быстро-мигающий зелёный светодиод говорит о проблемах соединения камеры с платой управления. В таком случае, следует проверить шлейф на наличие повреждений и надёжность фиксации разъемов с обеих сторон.

.. figure:: /_static/images/RCH_indication.png
	:align: center

Работа с приложением RunCam
---------------------------

Для изменения параметров работы и настройки камеры необходимо перевести её в режим работы считывания QR-кода.
Для этого после её включения, удерживаейте несколько секунд кнопку MODE на плате управления, зелёный светодиод при этом должен гореть постоянно.
После того, как камера переведена в режим считывания, необходимо сгенерировать QR-код с настройками при помощи приложения RunCam.
Приложение доступно для скачивания в PlayMarket'е. Выполните следующие действия:

1) Запустите установленное приложение на вашем устройстве.
2) Из выпадающего списка выберите модель RunCam Hybrid и нажмите кнопку QR Code Configuration
3) Настройте необходимые параметры во вкладках Video и General после чего нажмите кнопку Apply. Приложение сгенерирует QR-код с настройками.
4) Расположите QR-код перед объективом камеры. Смена зелёного светодиода на синий сообщает о том, что настройки были приняты и сохранены в память камеры.

.. figure:: /_static/images/RCApp.png
	:align: center


Работа с модулем камеры RunCam Split (снято с производства)
-----------------------------------------------------------

.. image:: /_static/images/videocamera.png
	:align: center

Модуль подходит как для съемки видео, так и для полетов в режиме FPV. Камера Runcam Split закреплена на поворотном подвесе. В корпусе модуля спрятана плата с кнопками управления, разъемами и слотом, в который установлена карта microSD на 4 Гб. На ней по умолчанию сохраняются все фотографии и видеоролики.

Плата подключения дополнительных модулей не совместима с модулем камеры. Используйте стандартную крышку отсека аккумулятора. Снимите её с Пионера и притяните модуль камеры сверху четырьмя винтами. После этого снова установите крышку на Пионер так, чтобы модуль камеры оказался снизу. Снимите нижнюю крышку модуля, чтобы получить доступ к плате Runcam Split. 

Подключите коннектор камеры к разъему X1 на базовой плате квадрокоптера. Для дальнейшей настройки подключите аккумулятор Пионера.

Камерой Runcam Split удобно управлять со смартфона по сети Wi-Fi. Для этого нужно скачать и установить приложение Runcam:

+-----------------------+---------------------------+
|   `Версия для IOS`_   |   `Версия для Android`_   |
+-----------------------+---------------------------+


.. _Версия для IOS: https://itunes.apple.com/ru/app/runcam-app/id1015312292?mt=8

.. _Версия для Android: https://play.google.com/store/apps/details?id=com.runcam.runcam2&hl=ru

Для управления камерой на плате есть 2 кнопки - "питание" (прямо напротив задней стенки камеры) и "переключение режимов" (там же, ближе к углу платы). Если до них сложно достать, попробуйте нажимать их отверткой из комплекта Пионера. Чтобы включить режим Wi-Fi, один раз нажмите на "переключение режимов". Должен прозвучать одиночный сигнал. Теперь камера работает как точка доступа. Включите Wi-Fi на смартфоне и подключитесь к сети RCSplit. Пароль 1234567890. 

Запустите приложение Runcam. Выберите модель Split 2S и нажмите "Connect". Теперь изображение с камеры транслируется на экран смартфона, можно делать фотографии и управлять записью видео, настраивать параметры. Чтобы открыть альбом камеры и скопировать содержимое на смартфон, нажмите иконку слева от кнопки записи. Вы можете просматривать фото и видео на microSD-карте, удалять и копировать материалы прямо на microSD карте.

Если у вас остались вопросы по настройке камеры, скачайте `инструкцию к Runcam Split`_

.. _инструкцию к Runcam Split: https://www.runcam.com/download/split2/RunCam-Split2-EN.pdf
