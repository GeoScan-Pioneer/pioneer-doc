.. role:: raw-html(raw)
    :format: html

Установка **pioeer_sdk**
========================


На данный момент для корректной установки **pioneer_sdk** через **pip** нужно сначала установить **setuptools** и **wheel**.

.. code-block:: console

	pip install setuptools

.. code-block:: console

	pip install wheel

.. raw:: html

	<div style="border: 2px solid lightgray; padding: 5px; border-radius: 10px;">
	<details>
		<summary>Зачем устанавливать <b>setuptools</b> и <b>wheel</b>?</summary><br>
	Чтобы установить библиотеку <b>pymavlink</b> нужны <b>setuptools</b> и <b>wheel</b>. Но конфигурационном файле библиотеки <b>pymavlink</b> они не прописаны как необходимые, поэтому <b>pip</b> не подгружает их автоматически. Надеемся, что разработчики <b>pymavlink</b> исправят эту ошибку.
	</details>
	</div>
	<br>

Устанавливаем **pioneer_sdk**

.. code-block:: console

	pip install pioneer_sdk

Теперь, чтобы использовать **pioneer_sdk** в своей программе добавьте :code:`import pioneer_sdk` или же :code:`from pioneer_sdk import Pioneer` в совой код.

Пример использования:

.. code-block:: python

	from pioneer_sdk import Pioneer
	pioneer_mini = Pioneer()
	if __name__ == '__main__':

		...

Смотрите также:
:raw-html:`<br />` :doc:`pioneer-sdk` 
:raw-html:`<br />` :doc:`pioneer-sdk_examples`

Если у вас возникли проблемы с установкой **pioneer_sdk**, напишите нам в :doc:`Техподдержку </support/support_main>`.
