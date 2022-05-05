.. role:: raw-html(raw)
    :format: html

Рой дронов
==========

Спомощью **pioneer_sdk** можно управлять несколькими дронами одновременно. Для этого и компьютер, на котором будет запускаться программа, и все квадрокоптеры должны быть подключены к одной wi-fi сети.
:raw-html:`<br />` :doc:`connect_to_wi-fi` 


После того как все устройства подключены к wi-fi, можно запускать файл, управляющий всеми дронами. В программе при объявлении каждого дрона, нужно указать его ip адрес.

.. code-block:: python

	from pioneer_sdk import Pioneer
	
	pioneer_mini_1 = Pioneer(pioneer_ip='192.168.147.10') # Укажите ip вашего дрона
	pioneer_mini_2 = Pioneer(pioneer_ip='192.168.147.11') # Укажите ip вашего дрона
	
	...
 
:doc:`multiple_drones/multiple_drones_code_example` 

.. toctree::
	:maxdepth: 1
	:hidden:

	connect_to_wi-fi
	multiple_drones/multiple_drones_code_example