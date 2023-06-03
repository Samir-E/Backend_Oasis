# Backend_Oasis
В данном репозитории хранится разработка Backend часть web-приложения Oasis

Установка зависимостей в виртуальную среду: 
python -m pip install -r requirements.txt

Старт:

Для начал читаем README.  
Открываем git bash в нужной папке, копируем команду из README.
Переходим в репозиторий (cd FQW/), и пишем команды в след. порядке:
(1) git branch develop
(2) git checkout develop
(3) git pull origin develop
Все теперь вы на рабочей ветке, с которой будем работать почти до самого конца, main мы вообще не трогаем.
Примечания:

Чтобы дальше работать вы создаете для своих таск ветки:
(1) git branch вашаветка - создать ветку
(2) git checkout вашаветка - перейти в ветку
(1) git checkout -b вашаветка - создать и перейти в ветку
Чтобы закинуть ваши изменения на gitHub:
(1) git add . (. - все ваши файлы подготовлены к коммиту)
(2) git commit -m "Ваш коммит (см. оформление коммитов в README)"
(3) git push origin вашаветка (смотрите, чтобы локально вы находились на вашей ветке - около пути справа название ветки)
*За pull request я отвечаю, вкратце, это что-то тип pull+merge в ветки на gitHub, поэтому следите, куда и что загружаете.
Чтобы, изменения грузить к себе локально:
(1) git pull origin веткакоторуюхотитезагрузить
*Внимательно с этой командой, так как изменения загрузятся в ветку, в которой вы находитесь.
Старайтесь в основном работать с одной-двумя ветками, а не создавать для каждой мини-задачки ветку, вообще, так как у нас проект маленький, то мне кажется достаточно одной ветки для каждого, для дизайна, функционала и машинного обучения, соответственно, и дальше я буду с вашей ветки мерджить изменения в develop.
*Но, если прям “припрет”:
(1) git push -d origin вашаветка - удалить в удаленном репозитории
(1) git branch -d вашаветка - удалить у вас локально
*Желательно находиться не в ветке, которую удаляете.
Также внимательно с папками, стараетесь создавать основные папки, как у меня, чтобы мне самому потом не разделять все ваши файлы в develop.
*К сожалению пустые папки gitHub не сохраняет, поэтому я их и не загрузил на gitHub, так как в них ничего нет, но вы просто можете создать их у себя.
