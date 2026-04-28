# DevOps_10_k8s_tools
Практика: helm, kompose, kustomize
Берём за основу 2 docker-compose проекта из прошлых работ – flask-redis и
prometheus-grafana.
Задачи:
1. Из проекта prometheus-grafana создаём helm-chart и развёртываем в k8s
2. Из проекта flask-app создаём prod и dev окружения через kustomize

Удалим все ресурсы из предыдущих лабораторных, чтобы не было конфликтов
<img width="974" height="677" alt="image" src="https://github.com/user-attachments/assets/938d6d59-947b-4abc-8e32-7b90af8c6848" />
Установка HELM
<img width="974" height="278" alt="image" src="https://github.com/user-attachments/assets/c8a98faf-20f7-43d7-8cae-d356f1fb6cda" />
Установка Kompose

<img width="974" height="655" alt="image" src="https://github.com/user-attachments/assets/144ca073-3260-416e-b390-3d93cde366c7" />
<img width="974" height="430" alt="image" src="https://github.com/user-attachments/assets/30653327-b98a-445f-9527-a1665a2b8eda" />

Содержимое всех нужных файлов


<img width="974" height="437" alt="image" src="https://github.com/user-attachments/assets/964783f3-4881-4143-a4d9-860d392f1339" />

<img width="974" height="437" alt="image" src="https://github.com/user-attachments/assets/1f26580b-2141-4e02-92f3-f39a236cc7f4" />

<img width="974" height="714" alt="image" src="https://github.com/user-attachments/assets/077335cd-6a92-4114-9044-1843e1d68dec" />

Устанавливаем релиз с именем «promgra»
<img width="974" height="760" alt="image" src="https://github.com/user-attachments/assets/ce981b4e-66e4-4e56-acea-44fd5f8e808e" />
Не забываем пробросить туннель

<img width="974" height="204" alt="image" src="https://github.com/user-attachments/assets/20dc7e63-87e3-450f-ba3f-eea22cb0989b" />
Добавляем значения.yaml, меняем выходной порт на 3456 и проверяем работу

<img width="974" height="1075" alt="image" src="https://github.com/user-attachments/assets/411dca1d-5d4f-4573-9d74-9b757e95bcaa" />
Демонтаж релиза

<img width="974" height="100" alt="image" src="https://github.com/user-attachments/assets/5f60b7ab-6300-4c4d-9396-08af53ebc2ce" />


Задача: из одного базового проекта (flask-redis) развернуть две
инсталляции в прод и дев окружения
с кастомизированными параметрами (Kustomize)

<img width="974" height="591" alt="image" src="https://github.com/user-attachments/assets/dab6f7be-221e-4e1e-a231-098b2a67cf99" />
Рядом с каталогом base создаём еще два каталога:
prod и dev
В каждый новый каталог кладём файл
kustomization.yaml (в нем же у меня патчи)

<img width="974" height="1034" alt="image" src="https://github.com/user-attachments/assets/0bc40fdc-a424-411e-b3ef-85e03a446039" />

<img width="974" height="1189" alt="image" src="https://github.com/user-attachments/assets/9a33dacc-f6bc-4685-b9a3-fa0c07f4b64f" />

<img width="974" height="684" alt="image" src="https://github.com/user-attachments/assets/11ce8fea-4b43-4c64-8cb1-96eff3cf9110" />

<img width="974" height="803" alt="image" src="https://github.com/user-attachments/assets/69e6fb60-a88c-4c5f-ae5b-f708b392907d" />

<img width="974" height="216" alt="image" src="https://github.com/user-attachments/assets/ac3453e9-b37e-4b30-9bcd-cbd2ae3aa6f3" />

<img width="974" height="173" alt="image" src="https://github.com/user-attachments/assets/df2c0be0-24b4-4ef2-bdd5-58302f7ca3d3" />
Работает!



