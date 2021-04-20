Cкрипт Get_camera_samples
=========================

Скрипт Get_camera_samples калибрует камеру квадрокоптера Pioneer Mini для корректной работы функций компьютерного зрения. Для калибровки
необходимо напечатать на листе А4 «шахматную доску»: https://raw.githubusercontent.com/opencv/opencv/master/doc/pattern.png

Разбор скрипта
--------------

1. Импортируем необходимые библиотеки и определяем их назначение:

  - | **Pioneer_sdk** – библиотека для управления квадрокоптером;
    | Описание библиотеки Pioneer_sdk - https://pioneer-doc.readthedocs.io/ru/master/programming/python/pioneer-sdk-methods.html;

  - | **NumPy** – библиотека для работы с массивами данных;
    | Описание библиотеки NumPy - https://numpy.org/doc/stable/;

  - | **Cv2** – библиотека машинного зрения;
    | Описание библиотеки OpenCV - https://docs.opencv.org/master/index.html;

  - | **sys** – библиотека, которая обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python;
    | Описание библиотеки sys - https://docs.python.org/3/library/sys.html;

  - | **os** – библиотека, которая предоставляет множество функций для работы с операционной системой;
    | Описание библиотеки os - https://docs.python.org/3/library/os.html;

  - | **yaml** – библиотека для работы с форматом данных yaml;
    | Описание библиотеки yaml - https://pyyaml.org/wiki/PyYAMLDocumentation.

  .. code-block:: python

    from pioneer_sdk import Pioneer
    import os
    import sys
    import numpy as np
    import cv2
    import yaml

2. Создаём ряд переменных и массивов:

  - | *number_of_samples = 15* - выбранное количество снимков. Их должно быть не меньше 10.

  - | *number_of_hor_corners = 6* - кол-во углов используемых шахматной доской по горизонтали.

  - | *number_of_ver_corners = 9* - кол-во углов используемых шахматной доской по вертикали.

  - | *counter = 1* - счётчик снимков.
  
  - | *criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)* - критерий остановки калибровки.

  Мы используем шахматную доску с ранее указными параметрами.

  - | *obj_p = np.zeros((number_of_hor_corners*number_of_ver_corners, 3), np.float32)*
    | Функция zeros() возвращает новый массив указанной формы и типа, заполненный нулями.

  - | *np.float32* указывает на необходимый формат массива.

  - | *obj_p[:, :2] = np.mgrid[0:number_of_ver_corners, 0:number_of_hor_corners].T.reshape(-1, 2)*
    | Функция np.mgrid() создает массив точек размером равным количеству углов по вертикали и горизонтали, координаты которых
     соответствуют координатам точек на шахматной доске координатных векторов.

  Массивы для хранения объектов и точек всех изображений:

  - | *obj_points = []* - 3d - координаты точек шахматной доски в трёхмерном пространстве.

  - | *img_points = []* - 2d - точки на плоскости изображения.

  .. code-block:: python

    number_of_samples = 15

    number_of_hor_corners = 6
    number_of_ver_corners = 9

    counter = 1
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)
    obj_p = np.zeros((number_of_hor_corners*number_of_ver_corners, 3), np.float32)
    obj_p[:, :2] = np.mgrid[0:number_of_ver_corners, 0:number_of_hor_corners].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    obj_points = []  # 3d point in real world space
    img_points = []  # 2d points in image plane.

3. Далее используем конструкцию **if \__name_\_ == '__main__':**, которая является точкой входа в программу. Всё, что идёт до этого условия, выполнятся всегда: и при вызове в качестве модуля и при вызове, как исполняемый файл.

  | Подробное описание данной конструкции: https://docs.python.org/3/library/__main__.html

  .. code-block:: python

    if __name__ == '__main__':

4. Создаём экземпляр класса Pioneer, чтобы начать работать с квадрокоптером.

  .. code-block:: python

    pioneer_mini = Pioneer()

   С понятием, что такое класс и его экземпляры можно ознакомиться по ссылке https://docs.python.org/3/tutorial/classes.html

5. Далее создаём байтовую строку:

  .. code-block:: python

    video_frame = bytes()

  Что такое байтовые строки: https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview

6. Условием проверяем задано ли количество снимков более 10. Далее печатаем необходимую информацию.

  .. code-block:: python

    if number_of_samples < 10:
      print('Algorithm need at least 10 samples')
      sys.exit(0)
    print('press p to take samples, or esc for exit')
    print('by default they will be stored in ./camera_samples folder and the result file will appear in ./result folder')
    print('Defined number of samples is %d' % number_of_samples)


7. Указываем директории сохранения файлов:

  .. code-block:: python

    os.chdir(os.path.dirname(sys.argv[0]))  # script dir
    samples_folder = os.path.join(os.getcwd(), "camera_samples")
    yaml_folder = os.path.join(os.getcwd(), "result")


  Метод **os.path.join()** совмещает путь каталога и файла вместе.

  Далее проверяем является ли пути директориями, если нет то создаём директории по ранее указанным путям:

  .. code-block:: python

    if not os.path.isdir(samples_folder):
      os.mkdir(samples_folder)
    if not os.path.isdir(yaml_folder):
      os.mkdir(yaml_folder)


8. В бесконечном цикле будем получать изображение от коптера, по нажатию  на клавишу “p” делать снимок и обрабатывать его. Это будет выполнятся до нажатия на клавишу Escape, либо до успешно выполненной калибровки.

  | Более подробное описание алгоритма (Eng): https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html

  В переменную **camera_frame** передаём изображение от квадрокоптера:

  - | **cv2.imdecode(buf, flag)** – чтение изображения из указного массива, где:
    | *buf* – читаемый массив;
    | *flag* – тип изображения.

  - | **np.frombuffer(buffer,dtype)** - интерпретирует буфер как одномерный массив, где:
    | *buffer* - буфер-подобный объект;
    | *dtype* – тип данных которым будут интерпретироваться элементы буфера.

  - | **pioneer_sdk.get_raw_video_frame()** – возвращает массив байт представляющий собой jpg картнку.

  - | **cv2.imshow(name,image)** - метод вывода изображение на экран, где:
    | *name* – имя созываемого окна;
    | *image* - выводимое изображение

  .. code-block:: python

    while True:
      camera_frame = cv2.imdecode(np.frombuffer(pioneer_mini.get_raw_video_frame(), dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow('pioneer_camera_stream', camera_frame)

9. Создаём обработку нажатия клавиш и описываем условия посадки и выхода из программы:

   .. code-block:: python

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
      sys.exit(0)

10. При нажатии на клавишу “p” делаем фото и записываем его в jpg файл под порядковым номером в указанную директорию.

  .. code-block:: python

    if not cv2.imwrite(os.path.join(samples_folder, 'frame_%d.jpg' % counter), camera_frame):
      raise Exception("Could not write image")


  | Метод **cv2.imwrite(filename, img[, params])** записывает изображение в jpg формате, где:
  | *filename* – Имя файла;
  | *img[, params]* – Изображение;

11. Читаем изображение, создаём его в чёрно белом формате и используем метод нахождения «Шахматной доски»:

  .. code-block:: python

    img = cv2.imread(os.path.join(samples_folder, 'frame_%d.jpg' % counter))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (number_of_ver_corners, number_of_hor_corners), None)

12. Если обнаруживаем «Шахматную доску», то добавляем точки объекта и точки изображения:

  .. code-block:: python

    # If found, add object points, image points (after refining them)
    if ret:
      obj_points.append(obj_p)
      corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
      img_points.append(corners2)
      # Draw and display the corners
      img = cv2.drawChessboardCorners(img, (number_of_ver_corners, number_of_hor_corners), corners2, ret)
      cv2.imshow('img', img)
      print('There are %d photos left to take' % (number_of_samples - counter))
      counter += 1
      cv2.waitKey(500)
      cv2.destroyWindow('img')
    else:
      print('Bad sample, try again')

13. Как только мы прошли по всем фотографиям закрываем все окна и выходим из цикла:

  .. code-block:: python

    if counter == number_of_samples + 1:
      cv2.destroyAllWindows()
      break

14. Выполняем калибровку камеры путем передачи значения известных 3D-точек **(obj_points)** и соответствующие пиксельные координаты обнаруженных углов **(img_points)** и сохраняем полученный результат калибровки в табличку в папку result.

  .. code-block:: python

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
    print("Camera matrix : \n")
    print(mtx)
    print("dist : \n")
    print(dist)
    print("rvecs : \n")
    print(rvecs)
    print("tvecs : \n")
    print(tvecs)

    # transform the matrix and distortion coefficients to writable lists
    data = {'camera_matrix': np.asarray(mtx).tolist(), 'dist_coeff': np.asarray(dist).tolist()}

    # and save it to a file
    with open(os.path.join(yaml_folder, 'calibration_matrix.yaml'), "w") as f:
      yaml.dump(data, f)

