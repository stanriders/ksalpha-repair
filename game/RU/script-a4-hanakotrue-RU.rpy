label ru_HT1:

    #Yes! You heard it here first! The beginning of the true Hanako path!
    #Less death! No depressing H-scenes! Only happysex and rainbows!
    #Also I need to get back into my groove, so feedback plox.
    #except for you, TC.
    #XP

    #of course, this feeds directly on from the library scene.
    
    scene bg school_library at bgleft
    show hanako def_shock_close at centersit2
    with locationchange
    #with locationskip
    
    #play music music_daily fadein 4.0
        
    "Смутившись, Ханако закрывает книгу и неуклюже запихивает её в сумку, не прекращая изумлённо на меня таращиться."

    show hanako emb_blushing_close at centersit2
    with charachange
    
    ha "Л-ладно."
    
    show hanako emb_blushing_close at center
    with charamove

    "Повесив сумку на плечо, она встаёт, лишь слегка опираясь на мою руку."

    show hanako emb_blushtimid_close
    with charachange
    
    "Я ласково улыбаюсь ей, заставляя покраснеть ещё сильнее. Она не отводит от меня глаз."

    "Все вокруг перестали заниматься своими делами и стали смотреть на эту абсурдную сценку из всех любовных романов разом."

    "Мне приходится слегка потянуть её за руку, чтобы заставить двигаться вперёд."

    hi "Давай, пойдём подышим."
    
    show hanako emb_blushtimid_close at twoleft
    show bg school_library at bgright
    with charamove_slow

    "Всё ещё удивлённая, Ханако следует за мной к выходу из библиотеки…"
    
    play sound sfx_alarm_loud
    
    #centered "*BEEP BEEP BEEP*"
    
    show hanako defarms_worry_close at twoleft
    with vpunch

    "Когда мы проходим через металлодетектор, на нём загораются огни и начинает выть сирена."

    #not entirely sure what everyone else calls them, but you know those loss-prevention door things.
    
    show hanako def_shock_close at twoleft
    with charachange

    "Удивлённое выражение лица Ханако сменяется ужасом, как только она понимает, что сама вызвала эту напасть."
    
    show hanako def_shock at center
    show bg school_library at center
    with dissolvecharamovefast
    #with ease
    
    show hanako defarms_shock
    with charachange

    "Библиотекарь с интересом рассматривает её, пока она бежит к стойке и расстёгивает сумку."

    ha "Простите-простите-я забыла-я должна была-простите!"

    "С вежливой улыбкой библиотекарь достаёт книгу из кучи тетрадок Ханако и записывает её в систему."

    "Библиотекарь" "Хорошего дня."
    
    show hanako cover_worry
    with charachange

    ha "Я не хотела-простите-пожалуйста-простите…"

    "Ханако в спешке сгребает кучу книг и тетрадок в открытую пасть своей сумки."

    hi "Ладно, я думаю, что мы уже наделали столько шума, сколько вообще возможно."

    hi "Давай оставим этих людей в покое."
    
    show hanako emb_downtimid
    with charachange

    "Ханако удручённо опускает взгляд, и мы выходим из библиотеки."
    
    hide hanako
    scene bg school_gardens2 at bgright
    with locationskip
    
    play ambient sfx_park fadein 2.0

    "Мы бесцельно ходим по территории, пока не выходим к садам за главным зданием."
    
    show hanako emb_downtimid
    with charaenter

    "По пути я покупаю две банки холодного чая и даю одну всё ещё смущённой Ханако."

    hi "Держи, это отвлечёт тебя от раздумий."

    hi "Ничто так не успокаивает скачущие мысли, как чай."

    show hanako emb_timid
    with charachange
    ha "С-спасибо."

    "Не нужно быть гением, чтобы понять, что она всё ещё переживает."
    
    show bg school_gardens2 at bgleft
    show hanako emb_timid at twoleft
    with charamove
    
    with Pause(0.3)
    
    show hanako emb_timid at center
    with charamove
    
    play sound sfx_can

    "Я сажусь на ближайшую лавочку, и Ханако беззвучно повторяет мои действия, аккуратно ставя сумку рядом с лавкой, прежде чем открыть банку."

    hi "Знаешь, Лилли сильная. Я уверен, она уже скоро будет на ногах."

    hi "Операция была небольшая, так что она вернётся в школу, не успеешь и глазом моргнуть."
    
    show hanako emb_downtimid
    with charachange

    "Ханако медленно проводит пальцем по краю банки, вглядываясь в неё так, будто в ней есть ответ на любой вопрос."

    ha "Э-это я и так знаю."

    ha "Но… я не знаю, что делать. Я н-не знаю, что могу сделать."

    hi "М? Что ты имеешь в виду?"

    "Её палец останавливается, но по-прежнему упирается в край банки."
    
    show hanako basic_worry
    with charachange

    ha "Если… если бы кто-нибудь из нас оказался на её месте, Лилли наверняка бы что-нибудь сделала."

    hi "Кажется, я не совсем тебя понимаю."
    
    show hanako emb_timid
    with charachange

    "Ханако вздыхает и отпивает немного чая."

    ha "Я и сама себя не до конца понимаю."

    ha "Просто… хочу сделать для неё хоть что-то, но не могу."
    
    show hanako emb_downtimid
    with charachange

    ha "Я чувствую себя… бессильной."

    "Её слова насквозь пронизаны печалью, хотя есть в них и что-то ещё…"

    "Решимость?"

    "Скорее всего. Хоть Ханако и жалуется, что ничего не может сделать, в её голосе слышна невероятная сила."

    "В этот миг образ Ханако, который сложился у меня в голове, рассыпается в прах и воссоздаётся вновь."

    "Ей правда небезразлична Лилли, и она хочет помочь ей…"

    extend " несмотря ни на что."

    "Образ робкой Ханако рассеивается подобно утреннему туману."
    
    show hanako basic_worry
    with charachange

    ha "Ч-что-то не так?"

    "Вернувшись в реальность, я понимаю, что уже некоторое время смотрю на Ханако, витая в облаках."

    hi "А-а… э-э… ничего."

    hi "Подумал о том, что ты сильно изменилась с тех пор, как мы познакомились…"

    "Чёрт, я повторяю слова Лилли."

    "Но сейчас я понимаю, что она была права."
    
    show hanako basic_bashful
    with charachange

    #hanako blushing but happy

    ha "Ой, да п-прекрати."

    "Слабая улыбка, появляющаяся на губах Ханако, приносит мне облегчение."

    hi "Слушай, как насчёт того, чтобы сегодня вместе навестить Лилли?"

    "Ханако слегка кивает перед тем как отпить из банки."
    
    $ renpy.music.set_volume(0.4,1.0)
    play sound sfx_normalbell
    
    stop ambient fadeout 4.0

    "Наш отдых прерывает далёкий звон колокола, зовущего учеников обратно в классы."

    stop music fadeout 4.0
    
    hi "Нужно возвращаться. Поедем сразу после школы, да?"

    ha "Ладно."

    #*****************************************
    #inside classroom
    #a22, should you take offence, feel free to veto this next passage.
    #i just kinda got a bit excited of the new misha sprites and she popped up in my mind.
    #scene bg school_scienceroom at bgright
    hide hanako
    show bg school_scienceroom at bgright
    with locationskip
    
    $ renpy.music.set_volume(1.0,1.0)

    play music music_normal fadein 0.3
    
    "Войдя в класс, я первым делом замечаю задумчивую %(name_shizune)s, аккуратно протирающую очки."
    
    "В моей голове по какой-то причине всплывает напуганный вид того парня в инвалидной коляске, которого я видел в начале большой перемены."

    "Пока %(name_shizune)s занята, я шёпотом обращаюсь к Мише, шепча ей на ухо."

    show misha cross_smile
    with charaenter

    hi "Эй… Тот парень, он в порядке? Что она с ним сделала?"
    
    show misha cross_grin
    with charachange

    "Миша радостно улыбается в ответ на проявленный мной интерес, явственно горя желанием ответить."

    mi "Не знаю!"

    extend " Но!"

    hi "Стой, не надо…!"

    "Поздно."
    
    show misha sign_smile
    with charachange
    
    show bg school_scienceroom at center
    show misha sign_smile at twoleft
    with charamove

    show shizu basic_normal at tworight
    with charaenter

    "Миша уже развернулась и хлопает %(name_shizune)s по плечу."
    
    show misha sign_confused at twoleft
    with charachange

    "Я хватаю Мишу за руки, пока она не выдала меня."

    "Её тёплые, мягкие руки…"

    "Стоп! Сейчас не время фантазировать, нужно не дать ей передать мой вопрос %(name_shizune)s."

    mi "Ой! Хисао? Хочешь признаться? Мне?"

    hi "Нет! Не собирался я этого делать."
    
    show shizu behind_blank at tworight
    with charachange

    shi "…"
    
    show misha hips_frown at twoleft
    with charachange

    "Миша наигранно дуется."

    mi "Ты вредина."

    hi "Я всего лишь хотел остановить тебя прежде, чем ты задашь этот вопрос %(name_shizune)s."

    hi "Мне кажется, она неправильно его истрактует…"

    show misha hips_laugh at twoleft
    with charachange

    mi "Ва-ха-ха-ха~! %(name_hicchan)s! Ты так говоришь, будто она плохой человек!"

    mi "Посмотри на неё, разве она может быть плохой?"

    hi "Ты, главное, пообещай, что не будешь её о нём спрашивать."

    mi "Ла~адно!"
    
    show misha sign_smile at twoleft
    with charachange
    
    show shizu basic_normal at tworight
    with charachange

    "Я отпускаю её руки, и она сразу же начинает что-то говорить %(name_shizune)s."
    
    show shizu behind_frustrated at tworight
    with charachange
    
    $ renpy.music.set_volume(0.4,1.0)

    "Чёрт. Готов поспорить, %(name_shizune)s о чём-то догадывается, но я понятия не имею, о чём они говорят."
    
    "Но по выражению лица %(name_shizune)s могу догадаться."
    
    show shizu cross_angry at tworight
    with charachange

    "Кажется, я пробудил демона…"

    show misha cross_smile at twoleft
    with charachange
    
    mi "%(name_hicchan)s~! %(name_shizune)s хочет тебе кое-что сказать!"

    mi "Она хочет напомнить, что Школьный совет существует для того, чтобы помогать ученикам, а не для того, чтобы развлекаться!"

    mi "Все дисциплинарные взыскания применяются к ученикам исключительно ради их собственного блага, но никак не для развлечения членов Школьного совета."

    hi "Что именно ты ей сказала?"

    show misha cross_grin at twoleft
    with charachange
    
    mi "Ой, уже и забыла."
    
    show shizu behind_frown at tworight
    with charachange

    shi "…"

    mi "А, %(name_sicchan)s ещё хочет кое-что добавить."

    #Misha stern/serious
    show misha cross_frown at twoleft
    with charachange

    mi "Этот парень больше тебя не побеспокоит."

    "Кровь стынет в жилах от мыслей о том, что эти две могли сделать с тем парнем…"
    
    hide shizu
    hide misha
    with charaexit

    "Зашедший в класс учитель наконец избавляет меня от их пристальных взглядов."
    
    #*****************************************
    #timeskip
    scene bg school_scienceroom
    with shorttimeskip

    "Класс, как обычно, пустеет в мгновение ока."

    "Всего несколько секунд спустя мы с Ханако остаёмся наедине."
    
    stop music fadeout 3.0
    
    show hanako basic_smile
    with charaenter

    hi "Ну что, выдвигаемся?"

    "Ханако кивает, и мы отправляемся на автобусную остановку."
    
    scene bg city_busint at bgright
    show crowd 
    with shorttimeskip
    
    $ renpy.music.set_volume(0.29999999999999999, 0.0, channel='ambient') 
    play ambient sfx_crowd_indoors fadein 0.5
    
    play music music_pearly fadein 1.0

    "Первый автобус в город оказывается на удивление переполненным."

    "Видимо, большая часть учеников хочет поскорее уехать подальше от школы."
    
    #Curb was misspelled as kerb here. -md01
#    "Hanako and I manage to secure a seat, but by the time the bus pulls away from the kerb, not a single free seat remains."

    "Мы с Ханако успеваем занять места, но, когда автобус начинает отъезжать от остановки, ни одного свободного места не остаётся."

    "Скорее всего, разговорить Ханако в такой атмосфере не получится, поэтому я лезу в сумку, чтобы найти что-нибудь почитать."

    "Перебирая тетрадки и книги, я натыкаюсь на плюшевого медведя от класса 3-3 для Лилли."

    "Я совсем про него забыл."

    "Достав медведя из сумки, я снова осматриваю его."
    
    show bg city_busint at bgleft
    show crowd at bgleft
    with charamove
        
    show hanako basic_normal at tworight
    with charaenter

    ha "Э-это для Лилли?"

    hi "Чт— а, да."

    hi "Её одноклассники попросили ей передать."

    show hanako emb_downsad at tworight
    with charachange
    
    ha "А… Понятно."

    show hanako defarms_shock at tworight
    with vpunch
    #Hanako sad, followed by a happy-ish Hanako
    
    ha "Хисао!"

    "Внезапный окрик Ханако заставляет меня подскочить на месте и чуть не выпустить медведя из рук."

    hi "Что?"

    extend " Я хотел сказать, что случилось, Ханако?"
    
    show hanako defarms_worry at tworight
    with charachange
    
    ha "Нам тоже нужно ей что-нибудь подарить…"
    
    show hanako emb_emb at tworight
    with charachange

    ha "Причём что-то такое, чтобы этот медведь был не одинок."

    "«Одинок»…"

    "Опять это слово."

    "Наверняка то, что она его произнесла, всего лишь совпадение. Но что-то мне подсказывает, что не всё так просто."

    "Интересно…"

    extend " возможно ли, что Лилли говорила о себе и о Ханако?"

    hi "Хорошая идея. Рядом с больницей есть магазин сувениров, можем там что-нибудь прикупить."
    
    show hanako emb_downdetermined at tworight
    with charachange
    
    "Ханако качает головой, продолжая смотреть на медведя в моих руках."

    ha "Нет… У этих подарков нет… нет…"

    show hanako emb_determined at tworight
    with charachange
    
    ha "…души…"

    "И вновь её голос полон той же решимости, что и сегодня утром."

    "А глаза полыхают страстью."

    "Только в этот раз я разделяю её чувства."
    
    stop music fadeout 3.0

    hi "Ты права."

    hi "На самом деле я знаю, куда стоит отправиться за правильным подарком, но нам придётся сделать небольшой крюк…"
    
    stop ambient fadeout 0.5
    
    #*****************************************
    scene bg city_othello at bgleft
    with shorttimeskip
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    play sound sfx_storebell
    play music music_soothing fadein 0.5
    $ renpy.music.set_volume(1.0, 4.0, channel='ambient')
    #background Antique shop
    
    show hanako basic_distant
    with charaenter

    ha "Антиквариат… «Отелло»?"

    hi "Ага, я нашёл это место, когда искал подарок на день рождения Лилли."

    ha "Понятно…"
    
    scene bg city_othello at bgright 
    show hanako basic_distant at tworight
    with charamove

    "Я сразу же направляюсь к плюшевому медведю, которого увидел в прошлый раз."

    hi "Он немного дороговат, но я думаю…"

    show hanako emb_smile at tworight
    #show hanako somethingdeterminedorother
    with charachange
    #Hanako srsbsns

    ha "Отлично подходит."

    "Произносит Ханако, едва я приподнимаю медведя с полки."

    "Она медленно и аккуратно принимает игрушку у меня из рук и прижимает к себе."
    
    hide hanako
    with charaexit

    "Пока она стоит с закрытыми глазами, обнимая плюшевого медведя, мне вдруг становится немного печально, что я покупаю его для Лилли, а не для неё."
    
    "В моей голове начинают крутиться шестерёнки, и я принимаюсь считать."

    "Если я ограничу себя только водой и едой из школьной столовой, то денег должно хватить."

    "Я мысленно благодарю родителей за то, что дали мне на этот месяц немного больше денег на карманные расходы, чем обычно."
    
    show bg city_othello at bgleft
    with charamove
    
    "Пока Ханако ещё стоит с закрытыми глазами, я хватаю с полки ещё одну игрушку, машу владельцу лавки и сую её в свою сумку."
      
    show shopkeep neutral
    with charaenter

    "Я вытаскиваю из кошелька пачку денег и, указывая на Ханако, кладу их под ещё одного медведя на той же полке."

    show shopkeep surprised
    with charachange
    
    "Он озадаченно глядит на меня, и я отчаянно пытаюсь объяснить ему свои намерения языком жестов."

    "Я ведь сотню раз видел, как это делают %(name_shizune)s с Мишей."

    "Почему же он смотрит на меня как на припадочного?"

    "Я уже готов подойти к нему и всё объяснить словами, но тут Ханако открывает глаза и выпускает медведя из объятий."

    show bg city_othello at center
    show shopkeep surprised at tworight
    with charamove
    
    show hanako basic_smile at twoleft
    with charaenter
        
    ha "Извините, мы хотели бы это купить."
    
    show shopkeep happy at tworight
    with charachange

    "Продавец" "А… конечно, мисс."

    "Продавец" "Это для вас, Лилли?"
    
    show hanako defarms_shock at twoleft
    with charachange

    "Ханако ошарашенно смотрит на продавца, а я закрываю глаза, желая, чтобы всё это оказалось сном."

    ha "К-как вы узнали, что это для Лилли?"
    
    show shopkeep thinking at tworight
    with charachange

    "Продавец" "Ну, я помню, что молодой человек уже заходил сюда."
    
    show shopkeep neutral at tworight
    with charachange

    "Продавец" "Он попросил меня выгравировать «Лилли» на музыкальной шкатулке."

    "Продавец" "Так что я решил, что это, должно быть, вы… учитывая, что он… ой!"
    
    show shopkeep surprised at tworight
    with charachange

    "Похоже, до него, наконец, доходит."
    
    show hanako defarms_worry at twoleft
    with charachange

    hi "Лилли – наш общий друг, и она сейчас в больнице."

    hi "Но я удивлён, что вы это запомнили."
    
    show shopkeep happy at tworight
    with charachange

    "Продавец" "А, у меня хорошая память на лица."

    hi "И имена, видимо."

    "Продавец" "Ну, это был необычный заказ."
    
    show hanako cover_worry at twoleft
    with charachange

    ha "Итак… сколько мы вам должны?"

    "Продавец смотрит сначала на меня, потом на мою сумку, а после на полку с деньгами за медведя, которого я спрятал у себя."

    show shopkeep thinking at tworight
    with charachange
    
    "Продавец" "Давайте вот как: я сделаю вам скидку на подарок больному – с вас будет ровно шесть тысяч."

    "Я хмурюсь, зная, что оставил на полке как минимум вдвое больше."
    
    show hanako basic_bashful at twoleft
    with charaenter
    #Hanako happy

    "Ханако, однако, в восторге."

    ha "С-спасибо!"
    
    show shopkeep happy at tworight
    with charachange

    "Я улыбаюсь, доставая кошелёк во второй раз и отдавая продавцу остатки своих денег."

    "Продавец" "…и вот ваш чек. Передайте Лилли пожелания скорейшего выздоровления!"

    hi "Спасибо."

    ha "Спасибо вам огромное."
    
    show hanako basic_smile at twoleft
    with charachange
    
    show hanako basic_smile at Position( ypos=0.75)
    with ease

    with Pause(0.2)

    show hanako basic_smile at twoleft
    with ease
    #insert command for bowing

    "Ханако слегка кланяется. Впервые вижу, чтобы она делала столь формальный жест."

    "Это по-своему мило."
    
    show shopkeep thinking at tworight
    with charachange

    "Продавец" "Вам нужен пакет или…"
    
    show hanako cover_bashful at twoleft
    with charachange

    "Ханако качает головой."

    ha "Нет, спасибо, я сама понесу его."
    
    show hanako emb_downsmile at twoleft
    with charachange

    "В подтверждение своих слов, Ханако обнимает медведя, прижимая его к груди."
    
    hide shopkeep
    with charaexit
    
    show bg city_othello at bgleft
    show hanako emb_downsmile at center
    with charamove
    
    play sound sfx_storebell
    
    hide hanako
    with charaexit

    "Под звон дверного колокольчика я убираю кошелёк в карман."
    
    stop music fadeout 3.0

    "Я слегка вздыхаю, заметив, каким он стал лёгким."

    "Всё-таки порой я совершаю поистине глупые поступки."

    return

    #*****************************************
label ru_HT2:
    
    scene bg hosp_ext_ss at bgleft
    with locationskip
    
    play music music_night fadein 6.0

    "Мы с Ханако прибываем в больницу позже, чем планировали, но небольшое отклонение от маршрута точно того стоило."
    
    show akira basic_smile_ss at twoleftsit
    show yuuko neutral_up_ss at tworightsit
    with charaenter

    "На лавке рядом с главным входом сидят Юко с каким-то парнем, пьющим пиво."

    hi "Привет, Юко, а кто это с тобой?"

    #sorry delta, I wrote this at work and I can't access the wiki for the character codes and
    #I'll probably forget to change them at home…
    
    show yuuko neurotic_up_ss at tworightsit
    with charachange
    
    show yuuko neurotic_up_ss at tworight
    with charamove

    yu "Привет, Хисао, Ханако. Это… эм… её зовут…"

    "Её?"
    
    show akira basic_laugh_ss at twoleftsit
    with charachange
    
    show akira basic_laugh_ss at twoleft
    with charamove
    
    aki "Акира Сато. Здоров, ребятки."

    "Парень встаёт, и при ближайшем рассмотрении становится очевидно, что это и в самом деле девушка."
    
    show yuuko worried_down_ss at tworight
    with charachange

    hi "Э… Хисао Накай… Приятно познакомиться…"
    
    show akira basic_smile_ss at twoleft
    with charachange

    "Акира сжимает протянутую мной ладонь и энергично трясёт."

    aki "Привет, Ханако. Давно не виделись."
    
    show bg hosp_ext_ss at center
    show akira basic_smile_ss at center
    show yuuko worried_down_ss at right
    with charamove
    
    show hanako emb_downtimid_ss at left
    with charaenter

    ha "П-привет, Акира."

    "Меня слегка беспокоит, что Ханако и Юко избегают смотреть на Акиру."

    "Похоже, они не ладят."
    
    show akira basic_resigned_ss
    with charachange

    aki "Ладно, я вроде закончила, так что, пожалуй, пойду."
    
    show akira basic_smile_ss
    with charachange

    aki "Приятно было познакомиться, Хисао. Спасибо, что присматриваешь за сестрой…"

    "А, Сато! Сестра Лилли. Мог бы сразу догадаться, как только услышал фамилию, но внезапная смена пола застала меня врасплох."
    
    hide akira
    with charaexit
    
    #show bg hosp_ext_ss at bgright
    show hanako emb_downtimid_ss at twoleft
    show yuuko worried_down_ss at tworight
    with charamove

    "Больше мне не удаётся задать ни одного вопроса, потому что Акира останавливает такси, не обращая на нас никакого внимания."
    
    show hanako emb_timid_ss at twoleft
    with charachange

    hi "Сестра Лилли, значит?"
    
    show yuuko neutral_up_ss at tworight
    with charachange

    yu "Родители отправили её сюда, чтобы проведать Лилли."

    hi "А я думал, это твоя работа."
    
    show yuuko panic_down_ss at tworight
    with charachange

    yu "Ну, наверное, но… не знаю."

    "Юко выглядит так, будто её только что уволили: уныло и потеряно."

    hi "Может, она просто заботится о своей маленькой сестрёнке…"
    
    show hanako basic_worry_ss at twoleft
    show yuuko worried_up_ss at tworight
    with charachange

    "Ханако и Юко как-то странно на меня смотрят."

    ha "В-вообще-то Лилли её старшая сестра…"

    hi "Хм, вот как… Просто выглядит она старше, чем Лилли."
    
    show yuuko worried_down_ss at tworight
    with charachange
    
    yu "Лилли старше всего на год, и Акира постоянно пытается во всём её обойти."
    
    show hanako emb_timid_ss at twoleft
    with charachange

    yu "Думаю, я просто к этому уже привыкла, поэтому не обращаю внимания."

    hi "Логично. Я так понял, ты сегодня взяла отгул или что-то вроде того?"
    
    show yuuko panic_down_ss at tworight
    with charachange

    "Унылость Юко уходит в тень облака замешательства, растущего над ней."

    yu "Нет, с чего ты взял?"

    hi "Ну, я думал, ты в это время должна быть на работе."
    
    show yuuko panic_up_ss at tworight
    with charachange

    "Паника нарастает."
    
    yu "Я… мне… который час… о нет… мненадоидти!"
    
    show yuuko panic_up_ss at tworightoff
    with slice_in
    show yuuko panic_up_ss at closeright
    with ease
    show yuuko panic_up_ss at tworight
    with ease
    
    "Нервы Юко не выдерживают, и она прошмыгивает мимо нас с Ханако, копаясь на ходу в карманах."
    
    show yuuko neurotic_up_ss at tworight
    with charachange

    yu "Ключи… ключи… где мои…"

    extend " Ах да, Лилли завтра выписывают… Увидимсяпозже!"
    
    stop music fadeout 3.0
    
    hide yuuko
    with charaexit

    "Я машу паникующей Юко, пытающейся запрыгнуть на свой скутер."
    
    show bg hosp_ext_ss at bgright
    show hanako emb_timid_ss
    with charamove

    hi "Ну что ж… Пойдём к Лилли?"
    
    show hanako basic_bashful_ss
    with charachange

    ha "Да… пойдём."
   
   
    #*****************************************
    scene bg hosp_room2
    with locationskip
    #BG hospital Room
    
    play music music_lilly fadein 1.0
    
    show lilly basic_reminisce_pat at centersit
    with charaenter

    "Лилли сидит в кровати, читая пальцем какую-то книгу в твёрдом переплёте."

    "Возможно, мне кажется, но Лилли выглядит устало."

    hi "Привет, Лилли. Мы с Ханако пришли тебя навестить."
    
    show lilly basic_listen_pat at centersit
    with charaenter

    "Лилли отточенным движением кладёт закладку в книгу, убирает её на прикроватный столик и пробегает по нему пальцами, чтобы запомнить, где она лежит."

    #"For some reason, I find the little tricks people use to get around their disabilities fascinating."
    #Commented 'cause I'm not sure if that's Hisao or me.
    # That's you.
    
    show lilly basic_smile_pat
    with charachange

    li "День добрый, Хисао, Ханако. Как ваши дела?"

    "Она по-прежнему разговаривает практически шёпотом, но уже почти не хрипит."

    "По крайней мере, настроение у неё стало чуть получше."
    
    scene bg hosp_room2 at bgleft
    show lilly basic_smile_pat at twoleftsit
    with charamove
    
    show hanako basic_bashful at tworight
    with charaenter

    ha "Привет, Лилли. Мы… мы принесли подарки."

    #Lilly Smile
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange
    
    li "Меня скоро выписывают, не стоило беспокоиться."
    
    show lilly basic_smile_pat at twoleftsit
    with charachange

    hi "Ну, твои одноклассники купили тебе подарок, и мы решили, что и нам неплохо бы тебе что-нибудь подарить."

    "Я подхожу к кровати и достаю медведя, стараясь не дать Ханако заглянуть внутрь сумки."

    hi "Держи, это тебе от всех учеников твоего класса."

    hi "Даже от %(name_kenji)s."
    
    show lilly basic_giggle_pat at twoleftsit
    with charachange
    #lilly small laugh

    li "Ого, вот это сюрприз."

    "Я вкладываю медведя в её протянутую руку, и она сразу же зарывается пальцами в его густой мех."

    show lilly basic_smile_pat at twoleftsit
    with charachange
    
    li "Боже, он великолепен. Не могли бы вы передать одноклассникам мою благодарность?"
    
    show lilly basic_oops_pat at twoleftsit
    with charachange

    li "Меня, скорее всего, не будет в школе до следующей недели."

    hi "Конечно."
    
    show hanako emb_timid at tworight
    with charachange

    "Ханако делает неуверенный шаг к кровати, и я сразу же захлопываю сумку."

    ha "Э-это от нас с Хисао…"
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange
    
    show hanako emb_downtimid at tworight
    with charachange

    "Ханако чуть ли не с сожалением выпускает из объятий плюшевого медведя."

    "Лилли аккуратно сажает первого медведя на книгу, которую только что читала, и принимает игрушку из рук Ханако."

    show lilly basic_emb_pat at twoleftsit
    with charachange

    "Едва она касается второго медведя, тут же меняется в лице."

    li "Ох, Ханако… не стоило…"
    
    show hanako basic_bashful at tworight
    with charachange

    "На её лице появляется удивление, когда она проводит пальцами по медвежьей мордочке."

    "Лилли утыкается в игрушку носом."
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange

    li "Он… он пахнет тобой, Ханако."
    
    show hanako emb_blushtimid at tworight
    with charachange
    #Hanako blush

    "Порой я даже рад, что Лилли слепая, потому что сейчас я краснею даже сильнее, чем Ханако."

    show hanako cover_worry at tworight
    with charachange   
    
    ha "Я… а… мы…"

    hi "Ханако не выпускала его из рук с тех пор, как увидела. Как только этот мишка попался ей на глаза, стало понятно, что мы непременно должны подарить его тебе."

    #lilly Fufufu
    show hanako cover_smile at tworight
    with charachange  

    li "Спасибо. Право, не стоило."
    
    show lilly basic_pout_pat at twoleftsit
    with charachange

    li "И извините за то, что заставила вас волноваться."

    "По её лицу можно понять, насколько искренне её извинение."

    show hanako basic_normal at tworight
    with charachange
    #Hanako Relieved/neutral

    "Благо, Ханако не обращает на него внимания."

    "Не думаю, что смог бы ей объяснить свою небольшую фантазию, не вызвав скандал."

    ha "Всё в порядке, Лилли. Мы просто хотели сделать для тебя что-нибудь."

    hi "Да, мне было как-то неловко дарить чужой подарок, не подарив свой."

    hi "И то, что мы за тебя беспокоились, – вполне естественно, ведь ты наш друг."
    
    show lilly basic_smile_pat at twoleftsit
    with charachange

    li "Что ж, ещё раз спасибо. Ты отлично умеешь выбирать подарки, Хисао."

    hi "Честно говоря, это Ханако выбрала его…"
    
    show hanako def_worry at tworight
    with charachange

    ha "Но ты нашёл магазин…"
    
    show lilly basic_giggle_pat at twoleftsit
    with charachange

    li "Боже, вы вдвоем прямо настоящая команда."
    
    show hanako basic_bashful at tworight
    with charachange

    li "А я словно немного выпала из жизни."

    hi "В таком случае, как насчёт того, чтобы в следующий раз я сводил туда тебя, Лилли?"
    
    show lilly basic_smile_pat at twoleftsit
    with charachange

    li "Хм, было бы здорово."

    "Пока мы перекидываемся шуточками, я замечаю, что Лилли всё время крепко держит своего нового мишку."

    "Вспоминается последний мой визит в комнату Лилли. Кукол и мягких игрушек у неё там было совсем немного. Наверняка это всё были подарки от Ханако и родни."

    "Хоть у меня и есть подозрение, что она предпочла бы книгу в качестве подарка, для неё это становится неважно, потому что мишку подарили ей мы с Ханако."

    "Через некоторое время раздаётся стук в дверь и в палату заходит медсестра, которая привезла тележку с едой. Она напоминает нам, что время посещения заканчивается."

    hi "Увидимся, Лилли."
    
    show hanako basic_bashful at tworight
    with charachange

    ha "Пока, Лилли."
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange
    
    #That grammar gave me cancer -md01
    #li "Good bye, you two. I'll be back at the dorm by tomorrow, if things to go plan, so I'll see you at school next time."
    
    li "Всего вам доброго. Если всё будет хорошо, завтра я уже вернусь в «Ямаку», так что там и увидимся."

    li "И спасибо за подарок. Буду беречь его как зеницу ока."
    
    stop music fadeout 2.0
    
    hide lilly
    hide hanako
    with charaexit

    "Медсестра кланяется нам с Ханако на прощание и вкатывает тележку в палату."
    
    #*****************************************
    scene bg city_busint_ss at bgright
    with shorttimeskip
    
    $ renpy.music.set_volume(0.5, 0.0, channel='ambient') 
    play ambient sfx_businterior fadein 1.0
    #BG bus w/ fade through black

    "Поездка в автобусе проходит в молчании, что позволяет мне подумать о Лилли."

    "Её болезнь и последовавшая за ней операция сблизили нас троих, однако кажется, что ничего не изменилось."

    show bg city_busint_ss at bgleft
    with charamove
    
    show hanako def_smile_ss at tworight
    with charaenter
    
    "По сути после нашей встречи изменилась только Ханако."

    "Она стала более уверенной в себе. Даже Лилли с этим согласна."

    "Она научилась спокойно вести со мной беседу и не трястись от страха, когда рядом нет Лилли."

    "Лилли же остаётся всё той же Лилли, да и я прежний, только спать стал меньше."

    "Она, кажется, и вправду заботится обо всех и каждом, и не важно, сколь незначительны их трудности."

    "А к Ханако она вообще относится с материнской заботой."

    "Несмотря на это, за прошедший месяц каждая из них успела попросить меня приглядывать за другой."

    "И я им обеим пообещал, что так и сделаю. Вот только смогу ли?"
    
    stop ambient fadeout 0.5

    "Автобус останавливается, прерывая ход моих мыслей."
    
    scene bg school_gardens_ss
    with locationchange
    
    $ renpy.music.set_volume(0.7, 0.0)
    play music music_tranquil fadein 4.0

    "Мы с Ханако бредём к общежитиям в лучах гаснущего заката, а я всё выбираю момент, когда можно будет подарить Ханако её подарок."

    "Но неловкое молчание между нами не даёт такой возможности, так что мы просто расходимся, вежливо пожелав друг другу спокойной ночи."

    "Блин, почему человеку на больничной койке дарить подарки настолько легче?"

    scene bg school_dormhisao_ss
    with locationskip
    #BG room

    "Я падаю на кровать и впериваю взгляд в потолок."

    "Мозг устал, но что-то мне настойчиво подсказывает, что сегодня я тоже не высплюсь."

    "Как, впрочем, и во все предыдущие ночи."
    
    scene black
    with shuteyemed
    
    scene bg school_dormhisao_ss
    with openeyefast

    "Я моргаю, и перед глазами снова появляется синий всполох."

    "Я сажусь в кровати и пытаюсь проследить за его источником, но он быстро улетучивается в никуда."

    "Но теперь мой взгляд приковывает кое-что другое: раздувшийся портфель."

    "Думаю, нет смысла вечно держать у себя этого мишку."
    
    stop music fadeout 4.0

    "А если он пробудет у меня слишком долго, она, чего доброго, ещё сочтёт меня чудаком."

    "Кстати, я купил его ей только потому, что мы приобрели такой же для Лилли."
    
    "Я не вкладываю в него какого-нибудь скрытого смысла или чего-нибудь подобного."

    "Открыв сумку, я вытаскиваю мишку Ханако и выхожу на улицу."

    return

    #*****************************************
label ru_HT3:
    scene bg school_gardens_ni
    with locationskip

    $ renpy.music.set_volume(0.1,0.0, 'ambient')

    play ambient sfx_cicadas fadein 0.3
    #BG Outside night

    "Вечер переходит в ночь, и стрекот цикад стихает."

    "В противовес жарким дням, ночь вполне себе прохладна."

    "Из-за этого, наверное, на улице никого нет."

    "Ну, и ещё из-за домашки."

    "Я корю себя за то, что не использую бессонные ночи, чтобы наверстать несделанную днём домашнюю работу."

    "Что ж, наверное, придётся всё делать в последнюю минуту перед экзаменами."

    "Раньше это прокатывало, так что всё будет нормально."
    
    stop ambient fadeout 2.0

    scene bg school_girlsdormhall at bgleft
    with locationchange
    #BG dorm hall

    "В коридорах общежития так же пустынно. Даже в фойе никого."

    "Обычно кто-нибудь из девчонок в это время смотрит телевизор, но сегодня – нет."

    "И мне от этого, честно говоря, немного легче."

    "Поспешив украдкой вынести подарок Ханако из магазина, я не додумался о том, чтобы купить для него подарочную упаковку."

    "Трудно было бы объяснить, почему я разгуливаю по женской общаге с плюшевым медведем в руках."

    "В коридоре, ведущем в комнаты Ханако и Лилли, даже тише, чем в остальной части здания."

    "Я даже слышу шум крови в ушах."

    "В отсутствие одного начинаешь чётче замечать другое."

    "Согласилась бы Лилли с этой мыслью?"
    
    show expression Solid('#00000022')
    show hanako_door_base at right 
    show hanako_door_door at left 
    with locationchange
    
    play sound sfx_doorknock2
    #BG Dorm door

    "Я тихонько стучу в дверь Ханако, но этот звук прокатывается по коридору оглушающим грохотом."

    "Ответа нет."

    "Сомневаюсь, что Ханако сейчас спит; она похожа на сову больше, чем кто-либо из прочих моих знакомых."
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound')
    play sound sfx_hammer
    "Я стучу чуть настойчивей, чтобы удостовериться, что она услышит."

    "И снова тишина."

    "Наверное, всё-таки она спит."

    "Ладно, можно будет вручить ей подарок и завтра. Например, в честь возвращения Лилли."

    "Я разворачиваюсь и направляюсь к лестнице."

    show bg school_girlsdormhall at bgleft
    with locationchange
    #BG dorm hall
    
    show bg school_girlsdormhall at center
    with charamove

    hi "Похоже, придётся тебе ещё немного помаяться в заключении, малыш."

    hi "Постарайся, чтобы тебя не увидели."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    play sound sfx_lock

    "И тут я замираю, услышав звук открывающихся замков на двери."

    "Я рефлекторно прячу медведя за спиной."

    "Но звук доносится не со стороны двери Ханако, а откуда-то ближе…"
    
    scene bg school_girlsdormhall at bgleft
    with charamove

    ha "Хи… Хисао?"

    ha "Это ты?"

    hi "Ханако? Прости, я тебя разбудил?"
    
    play sound sfx_dooropen

    scene bg school_dormlilly 
    show hanagown worry_close at twocenteroff
    show expression Solid('#00000022') 
    show hanako_door_base at right 
    show hanako_door_door at left
    with locationchange
    
    show hanako_door_door at leftdoor
    with charamove

    $ renpy.music.set_volume(1.0, 0.0)
    play music music_moonlight fadein 4.0
    #BG Dorm Door

    "Я оборачиваюсь и замечаю свет, идущий из-за приоткрытой двери в комнату Лилли."
    
    show hanagown distant_blush_close at twocenteroff
    with charachange

    ha "Н-не совсем."

    hi "Не против, если я зайду? У меня есть кое-что для тебя…"
        
    play sound sfx_door_creak

    show hanako_door_door at leftdooropen
    show hanako_door_base at rightwallopen
    show bg school_dormlilly at roomopen
    show hanagown distant_blush_close at twocenteroff2
    with charamove

    scene white 
    with dissolve

    with Pause(0.1)
    
    scene bg school_dormlilly 
    show hanagown distant_blush_close
    with dissolve

    "Дверь в комнату медленно открывается, и я вижу стоящую за ней Ханако."

    #Show Hanako sad

    "Она выглядит совершенно удручённой, её глаза опухли и покраснели, голова опущена."

    hi "Ханако? Что случилось? Это ведь комната Лилли?"
    
    show hanagown worry_blush
    with charachange

    "Ханако молча кивает и отходит от двери."

    "За ней я различаю кровать Лилли, простыни на которой чуть ли не в узел завязаны."

    "На покрывале лежит старый ободранный плюшевый кролик, которого я вижу впервые."

    #Fact check; I'm pretty sure Hisao hasn't seen Hanako's room before now. If he has, then use this line instead:

    #"Hanako's tattered plush rabbit sits atop the heap of linen."

    "Очевидно, Ханако только что поднялась с неё."
    
    show hanagown distant_blush
    with charachange

    ha "П…"
    
    extend " Прости."

    hi "Простить? За что?"

    ha "Мне здесь не место."
    
    show hanagown distant_cry
    with charachange

    ha "Но я просто не могла…"

    #hanako cry

    "Из её глаз начинают течь слёзы, оставляя на лице блестящие следы."
    
    show hanagown worry_cry
    with charachange

    "Она упорно старается не смотреть на меня – побочный эффект чувства вины."

    "При виде плачущей девушки любой мужчина наполняется состраданием."

    hi "Перестань, в этом же нет ничего плохого."
    
    show hanagown normal_cry
    with charachange

    hi "Я уверен, Лилли не была бы против."

    "Я понимаю, что по-прежнему прячу медведя от Ханако, действуя по наитию, пусть это и глупо."

    hi "Смотри, я принёс тебе подарок."
    
    show hanagown normal_cry2
    with charachange

    "Я показываю игрушку Ханако. Та поначалу чуть отстраняется от протянутых к ней рук."
    
    show hanagown worry_cry2
    with charachange
    #Hanako surprised
    
    "Но, как только её заплаканные глаза распознают, что это такое, на её лице появляется крайнее удивление."

    "Она пялится на него, не веря глазам, и кажется, будто весь мир замер."

    "Через некоторое время она трясущимися руками забирает у меня мишку."

    "Она обнимает его, словно мать новорождённое дитя, нежно и заботливо."

    hi "Так что ты—{w=.3}{nw}"
    
    show hanagown irritated_close
    with None
    
    play sound sfx_impact
    with vpunch
    
    extend " оох!"

    "Стоит мне только начать говорить, как Ханако прижимается ко мне, сдавливая медведя между нами."
    
    show hanagown irritated_alt
    with charachange

    ha "Как?.. Когда?.."

    hi "Ну, э, когда я смотрел на тебя в магазине, то понял, как здорово вы смотритесь вместе."

    hi "Поэтому я незаметно купил его тебе, пока ты отвлеклась."
    
    show hanagown smile_alt
    with charachange

    ha "Он… С-спасибо."
    
    show hanagown smile_blush
    with charachange

    "Ханако глядит на медведя, и выражение на её лице меняется со смущённого на задумчивое."

    #Hanako neutral

    hi "Что ж… Я, наверное, пойду…"
    
    show hanagown normal
    with charachange

    "Не успеваю я и глазом моргнуть, как она протягивает ко мне руку и хватает за рукав."
    
    stop music fadeout 14.0

    ha "Н-не уходи. Не сейчас…"

    "Как ни странно, она при этом не отрывает взгляда от медведя."

    hi "Хорошо. Думаю, я могу ненадолго остаться."

    hi "Давай я поставлю чайник."
    
    show hanagown distant
    with charachange

    "Ханако кивает и медленно отпускает мой рукав."
    
    show hanagown distant at tworight
    show bg school_dormlilly at bgright
    with charamove

    "Она отшатывается и неловко садится на кровать Лилли."

    "Пока я наливаю чайник и включаю его, она шарит рукой по простыне, пока не находит потрёпанного кролика."

    "Затем она привычным движением сажает кролика к себе на колени рядом с медведем."

    "Ну и странное мы, наверное, зрелище сейчас представляем: Ханако, с любовью глядящая на игрушки, и я, наблюдающий за ней с другого конца комнаты."

    "Вода вскипает, и я наливаю её в заварочный чайник."
    
    show hanagown distant
    show bg school_dormlilly at bgleft
    with charamove

    "Словно ведомый чьей-то невидимой рукой, я ставлю чайник на столик Лилли и присаживаюсь рядом с Ханако."

    "Я уже несколько раз был в комнате Лилли, но кровати касаюсь впервые."
    
    "Я сажусь на пол и под тихий скрип пружин прислоняюсь к кровати спиной, ощущая идущий от простыней лёгкий аромат Лилли."

    "Но сейчас нашей слепой подруги у меня в мыслях даже близко нет."

    "Что-то в реакции Ханако лишает меня всяческой способности думать."

    "Конечно, я не ждал, что она будет без ума от счастья, но и того, что она просто вот так замрёт, тоже не ожидал."

    "Но всё же она выглядит повеселее, чем когда только открыла дверь."

    "…Вроде бы."

    hi "Что ж, твой друг теперь не один, а?"
    
    show hanagown worry
    with charachange
    #Hanako Shocked

    ha "Э-э?"

    "Ханако слегка вздрагивает от моего вопроса, будто забыв, что она не одна в комнате."

    "Мне в голову не приходит ничего лучше, чем повторить предложение."

    hi "Твой друг, заяц. Он больше не один, так?"

    hi "К тому же он выглядит уже довольно старым."
    
    show hanagown normal
    with charachange
    #Hanako neutral

    ha "Н-наверное, ты прав."
      
    show hanagown distant
    with charachange
    
    play music music_hanako fadein 4.0

    ha "Просто… никто не дарил мне ничего такого…"
    
    extend " с тех самых пор."

    "Внутренний голос подсказывает мне, что эту тему лучше не развивать."

    hi "С тех самых пор?"

    "Похоже, мой внутренний голос не способен остановить внешний."
    
    show hanagown distant_alt
    with charachange
    with Pause(0.5)
    show hanagown normal
    with charachange

    "Ханако закрывает глаза и перед тем, как посмотреть на меня, на мгновение прижимает игрушки к себе."

    #Hanako srs bsns

    ha "Я росла с приёмными родителями."

    ha "Они хорошо ко мне относились, но я не могла заставить себя что-либо у них попросить."

    ha "Я и так была обязана им за то, что они позволяли мне жить с ними."
    
    show hanagown distant
    with charachange

    ha "Но прежде… прежде…"
    
    show hanagown worry
    with charachange
    #Hanako sad

    ha "Прежде мои настоящие родители купили мне Петру."

    "При упоминании родителей она чуть крепче обнимает кролика."

    ha "Мы с ним – единственные вещи, которые пережили пожар."

    hi "Вещи?"

    ha "Всё сгорело. Мой дом, мои игрушки, мои родители… всё."

    ha "Я почти ничего не помню, но, когда пожарный разбудил меня в снегу, всё, что у меня было, – это Петра."

    show hanagown distant
    with charachange
    
    ha "С тех пор только мы друг у друга и остались."

    #Hanako neutral

    hi "Ты… кому-нибудь об этом рассказывала?"
    
    show hanagown normal
    with charachange

    "Ханако качает головой."

    ha "Никому. Даже Лилли."

    hi "Правда?"

    ha "Правда."

    #Really? Really!

    #Also, so long 12.0 wpl

    "Я снова прислоняюсь к кровати Лилли."

    "Значит, Ханако рассказывала Лилли не всё."

    "Эта мысль не выходит у меня из головы."

    "Я помню, как Лилли говорила, что Ханако однажды рассказала ей о себе всё. Подумать только, она что-то от неё скрывала…"

    "Интересно, чего ещё Лилли не знает?"

    #And thusly, the Onee-sama intelligence network was brought into disrepute."

    hi "Кстати, а что ты тут делаешь?"
    
    show hanagown normal_blush
    with charachange
    #Hanako Embarrassed
    
    stop music fadeout 6.0

    ha "Эм-м-м… Я… М-мне показалось, что я услышала что-то… и… и зашла проверить…"

    hi "Ты не умеешь врать."

    hi "Мне больше нравится, когда ты говоришь честно."

    show hanagown distant_blush
    with charachange
    #Hanako Looing down embarrassed.

    "Ханако молчит, избегая моего взгляда."

    ha "У меня…"

    extend " лампочка перегорела."

    hi "Лампочка?"

    "По-прежнему избегая смотреть мне в глаза, она играется с длинными ушами Петры."

    ha "Я…"
    
    show hanagown normal_blush
    with charachange
    play music music_heart fadein 4.0

    ha "Обещай, что не будешь смеяться."

    "Становится интересно…"

    hi "Обещаю."
    
    ha "Я… боюсь темноты."

    hi "Правда? Но ведь во время фестиваля ты довольно долгое время провела в коридоре."

    hi "Там было достаточно темно, разве нет?"
    
    show hanagown distant_blush
    with charachange

    ha "Это… не то."

    ha "Я не могу спать без света."
    
    show hanagown worry_blush
    with charachange

    ha "Но сейчас лампочка перегорела."

    ha "Когда такое происходит, я обычно пробираюсь к Лилли, но…"

    #Hanako sad

    "Мне надо отвлечься… сейчас…"

    hi "Ах да, чай остывает, не желаешь чашечку?"

    "Я просто король учтивости."
    
    show hanagown normal
    with charachange
    #Hanako neutral

    ha "А… да, давай."

    "Я аккуратно разливаю чай по чашкам и передаю одну Ханако."

    "Она аккуратно его размешивает, внимательно следя за тем, чтобы оба её «друга», сидящие у неё на коленях, не упали."

    hi "Итак, лампочка перегорела, а Лилли нет."

    hi "Что же ты будешь делать?"
    
    show hanagown drunksmile
    with charachange

    ha "Ну… Лилли хранит для меня одну запасную на всякий случай."

    "Как это похоже на Лилли."

    hi "Понятно. То есть ты собираешься захватить её комнату?"
    
    show hanagown worry_alt
    with charachange
    #Hanako happy embarrassed

    ha "Н-нет, ничего такого."

    hi "Ну коне-ечно."
    
    show hanagown drunkpout
    with charachange
    #Hanako pout

    ha "Ты же сказал, что не будешь смеяться…"

    hi "А я и не смеюсь. Я просто пошутил."

    hi "Это две большие разницы, знаешь ли."
    
    show hanagown normal_alt
    with charachange
    #Hanako embarrassed/happy
    
    ha "Ну ты и вредина."

    hi "Раз так, то я не буду больше покупать тебе подарки."

    show hanagown smile
    with charachange
    #Hanako happy/smile

    ha "Вреднючий."

    "Я впервые вижу Ханако, улыбающуюся в отсутствие Лилли."

    "Это непривычно, но радует."

    "Я улыбаюсь и ставлю чашку на прикроватную тумбочку Лилли."
    
    play sound sfx_alarmclock

    "Часы" "Двадцать три часа четырнадцать минут."

    hi "Что? Уже так поздно?!"

    show hanagown worry_alt
    with charachange
    #Hanako shocked/worried

    ha "Я… извиняюсь. Совсем заболталась…"
    
    show hanagown normal
    with charachange
    
    hi "Нет, дело не в этом."
    
    hi "Я и так рисковал, идя сюда."

    hi "И если я сейчас уйду, то наверняка попадусь."

    ha "Ох…"

    ha "Ну…"
    
    show hanagown distant_blush
    with charachange

    ha "Ты можешь… остаться…"

    "Какогочёртаонатолькочтосказала?"

    "Спокойствие, только спокойствие."

    "Вряд ли она имела в виду…"

    hi "Конечно."

    show hanagown smile
    with charachange
    
    "Чёрт побери, опять?"

    "Надо учиться думать, прежде чем что-то говорить."

    hi "Посплю на полу."
    
    show hanagown distant_blush
    with charachange

    ha "Нет… Я не могу…"

    hi "Всё в порядке, бывало и хуже."

    hi "Да и девочки созданы, чтобы спать на кроватях, а мальчики – на полу. Это абсолютно нормально."

    show hanagown drunknormal
    with charachange
    #Hanako blush/embarrassed

    ha "Ну… ладно."
    
    show hanagown drunknormal at tworight
    show bg school_dormlilly at bgright
    with charamove

    "Я собираю всё со стола Лилли и перекладываю на её парту…"

    "Потом откатываю стол, что освобождает достаточно места."

    "И под ним не сказать чтобы голый бетон."
    
    show hanagown smile at tworight
    with charachange

    ha "Ой… секунду…"
    
    show hanagown smile at offscreenleft
    with charamove

    "Ханако кладёт игрушки на кровать Лилли и выбегает за дверь."
    
    show hanagown smile at center
    show bg school_dormlilly at center
    with charamove

    "Через несколько секунд она возвращается, неся в руках постельное бельё и одеяла."

    #Do you guys call them doonas or quilts? Or is it comforter?

    ha "Можешь… Можешь спать на этом."

    show hanagown drunkdistant
    with charachange
    
    ha "Это… это всё моё."

    "Ничего себе. То есть она пошла и просто сняла это всё со своей кровати."

    "Я сперва решил, что это запасной комплект или типа того."

    "…"

    "Постойте-ка… Это значит, что, когда она сказала, что пробирается в комнату Лилли…"

    "…Она пробирается к ней в кровать…"

    #BG flashback?

    li "О… Я знаю, что поможет тебе уснуть, Ханако…"

    #BG return

    "Так, а ну-ка, фантазия, гормоны, живо успокоились!"
    
    show hanagown smile
    with charachange
    
    hi "Б-большое спасибо."
    
    hide hanagown
    with charaexit
    
    show bg school_dormlilly at bgright
    with charamove
    
    play sound sfx_rustling
    
    "Я принимаю из рук Ханако эту гору белья и начинаю вить себе на полу гнёздышко."

    "Сегодня не очень-то жарко, так что постелю на пол ватное одеяло."
    
    play sound sfx_switch
    
    scene bg school_dormlilly_ni at bgright
    with locationchange

    "Закончив сооружение импровизированной кровати, я выключаю свет."

    "Из угла комнаты идёт слабое свечение; должно быть, Лилли всегда оставляет включённым небольшой ночничок для Ханако."

    "Его света едва хватает для того, чтобы можно было что-то разглядеть, но этого достаточно, чтобы отогнать тьму, и помешать мне спать он не должен."

    "Ханако наскоро поправляет бельё на кровати Лилли и залезает в неё, кладя рядом с собой Петру и своего плюшевого медведя."

    scene black
    with shuteye
    
    "Я ложусь и закрываю глаза."

    "Мысли затуманивает аромат Ханако, и мне приходится отгонять нахлынувшую волну головокружения."

    "Как я и думал, просто взять и заснуть у меня не получится."

    "В теле чувствуется усталость, однако разум сдаваться никак не намерен."
    
    stop music fadeout 6.0

    "Принятые мной лекарства вкупе с находящейся со мной в одной комнате девушкой не дают покоя."

    ha "У меня был ещё один друг."
    
    scene bg school_dormlilly_ni at bgleft
    show hanagown distant_ni at tworight
    with openeye

    hi "Хм?"

    ha "Он был хорошим другом."
    
    show hanagown distant_alt_ni at tworight
    with charachange

    ha "Я думаю… Я думаю, он любил меня."
    
    show hanagown normal_ni at tworight
    with charachange

    ha "Но… Когда я спросила его об этом, он сбежал."

    ha "Не пристань я к нему с расспросами, он бы до сих пор был рядом."

    ha "Хисао…"
    
    show hanagown worry_ni at tworight
    with charachange

    ha "Пожалуйста, не сбегай."

    hi "С чего бы мне сбегать?"
    
    show hanagown normal_ni at tworight
    with charachange

    ha "Просто… не делай этого."

    hi "Ладно."
    
    ha "Хисао?"

    hi "М?"
    
    show hanagown smile_ni at tworight
    with charachange
    
    ha "Спасибо."

    extend " За всё."
    
    scene black 
    with shuteye
    
    window hide
    
    with Pause(1.5)

    #Far out, there must be like an average of 2 wpl in this scene.
    # Farking dailouge.
    #Now, the question that has been gnawing at me for ages…
    #Will Hanako sneak into Hisao's bed tonight?
    #PS that won't mean H though.
    #Also there will be an omake thing unlocked after this, kinda like "Future"
    #it will be the whole Hanako's friend getting pwned by a truck.
    #that is, of course, if I keep the current ending.

    return

    #*****************************************
label ru_HT4:

    scene black 
    with dissolve
    #bg black
    play sound sfx_alarmclock

    "Часы" "Семь часов одна минута."

    "Часы" "Семь часов одна минута."

    scene bg school_dormlilly
    with openeye
    #bg dormlilly with eyes open

    "Эх. Сказать, что я как-то совсем не сладко спал прошлую ночь, значит ничего не сказать."

    scene bg school_dormlilly at bgright
    with charamove
    
    "Даже повернувшись набок и попытавшись встать, я чувствую боль в спине. Я словно старик."

    "Часы" "Семь часов две минуты."

    hi "Да-да, я знаю… Как эта штуковина отключается?"

    show hanagown smile at right
    with charaenter
    
    play music music_dreamy fadein 4.0
    #show Hanako neutral smile at right

    ha "О… Ты проснулся…"
    
    scene bg school_dormlilly at bgleft
    show hanagown smile at center
    with charamove

    "Я лежу на полу и смотрю вверх, на улыбающуюся Ханако."

    "Лучи утреннего солнца падают ей на лицо под странным углом."

    "Учитывая типичную… «ситуацию»… с которой по утрам сталкиваются все парни, я вот-вот засмущаюсь."

    hi "Э, ага… Это… часы… будильник…"

    "Я изо всех сил стараюсь закопаться поглубже в простыни, одновременно пытаясь успокоиться."
    
    show hanagown normal_alt
    with charachange

    ha "Лилли устанавливает будильник на довольно ранний час, да?"
    
    show hanagown smile
    with charachange
    
    show hanagown smile at twoleft
    with charamove

    "Ханако ползёт вдоль кровати, одетая во всё ту же ночную рубашку, что и вчера вечером."

    "Она нажимает несколько кнопок на часах, заставляя будильник замолчать."
    
    show hanagown normal at twoleft
    with charachange
    
    ha "Так мы хотя бы успеем прибраться перед началом уроков."

    hi "Ага. Давай-ка хорошенько тут приберёмся. Лилии возвращается сегодня, помнишь?"
    
    show hanagown smile at twoleft
    with charachange
    #hanako neutral bigsmile

    ha "Как я могу забыть?"
    
    play sound sfx_rustling
    
    show hanagown smile at center
    show bg school_dormlilly at center
    with charamove
    
    "Успокоившись и расслабившись, я откидываю одеяло Ханако и сажусь; при этом спина издаёт хруст."
       
    hi "Ай!"
    
    show hanagown worry
    with charachange
    #Hanako embarrassed concerned

    ha "С тобой всё в порядке?"

    hi "Да, всё нормально, просто спина немного затекла от лежания на полу."

    show hanagown distant_blush
    with charachange
    #Hanako neutral looking down

    ha "П-прости… Я не должна была заставлять тебя оставаться…"
    
    show hanagown irritated_alt
    with charachange

    "Я встаю и глажу Ханако по голове."

    hi "Не глупи. У меня не было выбора, помнишь?"

    hi "Вытерпеть боль в спине гораздо проще, чем объяснить, что я делал в женском общежитии посреди ночи."

    show hanagown normal
    with charachange
    
    ha "Я… думаю, что ты прав."

    hi "Давай приступим. Подготовим это место к триумфальному возвращению Лилли!"

    show hanagown smile
    with charachange
    #hanako embarrassed smile

    ha "Хорошо…"
             
    show bg school_dormlilly
    with shorttimeskip
    
    "Уборка в небольшой комнатке до типичного для неё блеска не занимает много времени."

    "Под конец Ханако собирает выданное ею мне на ночь постельное бельё и направляется к двери."

    #Hanako embarrassed look down smile
    show hanagown smile_blush
    with charaenter

    ha "Ну… Увидимся…"
    
    show hanagown smile
    with charachange

    ha "С-спасибо, что составил компанию."

    hi "Не за что."
    
    show bg school_dormlilly at bgright
    show hanagown smile at left
    with charamove
    
    play sound sfx_dooropen
    
    hide hanagown
    with charaexit
    
    play sound sfx_doorclose
    with Pause(1.5)

    "Не говоря больше ни слова, она выскакивает из комнаты Лилии и возвращается к себе в комнату, закрыв за собой дверь."

    #hide hanako
    
    show bg school_dormlilly at bgleft
    with charamove
    
    stop music fadeout 3.0

    "Я окидываю быстрым взглядом комнату Лилли."

    "Решив, что всё в порядке, я отправляюсь в свою комнату, чтобы успеть принять душ перед завтраком."
    
    #*****************************************
    scene bg school_hallway3 
    with shorttimeskip
    #bg classroom with ? some kinda timeskip?

    "Даже несмотря на ранний подъём, мне приходится спешить, чтобы успеть явиться в класс до начала занятий."

    "Думаю, собираясь в школу, я просто замешкался, зная, что времени на сборы у меня больше, чем обычно."
    
    play sound sfx_dooropen
    
    scene bg school_scienceroom at bgright
    show hanako cover_distant at left
    with locationchange
        
    "Ничего удивительного, что Ханако уже сидит на последней парте, лениво поглядывая в окно."

    "Я хотел подойти поздороваться, но внезапно на моём пути возникает препятствие."
    
    hide hanako cover_distant at left
    with charaexit
       
    mi "Хи–са–о~!"
    
    show bg school_scienceroom at center
    with charamove
    
    play music music_happiness fadein 4.0
    
    show misha hips_grin at twoleft
    show shizu behind_blank at tworight
    with charaenter
    #show misha at twoleft and shizune at tworight

    "Даже целых два препятствия."

    hi "Леди, чем я могу быть вам полезен этим замечательным утром?"
    
    show shizu basic_normal at tworight
    with charachange
    
    show misha sign_smile at twoleft
    with charachange

    "За этим следует ураганный обмен жестами, пока Миша наконец не озвучивает просьбу %(name_shizune)s."

    mi "Мы тут подумали, и я решила, что ты окажешь нам неоценимую услугу, если поможешь найти одного мальчика."

    hi "Что, правда? Ни за что бы не подумал, что кто-то из вас участвует в свиданиях вслепую."
    
    show misha perky_confused at twoleft
    with charachange

    "С некоторой задержкой Миша передаёт мой ответ %(name_shizune)s, но я получаю ожидаемый эффект."

    show shizu cross_angry at tworight
    with charachange
    # shizune pouting/angry
    
    show misha hips_laugh at twoleft
    with charachange

    mi "Ва-ха-ха-ха~! Хисао, это не так! Мне стоило бы тебя стукнуть за твою наглость!"
    
    show shizu adjust_smug at tworight
    show misha hips_smile at twoleft
    with charachange

    mi "Но сейчас нам нужна твоя помощь, поэтому я оставлю это на потом."

    "Какая-то часть меня хочет отшутиться от их просьбы, но где-то в глубине сердца я теперь боюсь поворачиваться спиной к любой из этих девушек."

    hi "Раз так, то я помогу. Кто тот паренёк, которого вы разыскиваете?"
    
    show misha perky_smile at twoleft
    show shizu behind_blank at tworight
    with charachange

    mi "В общем, этим утром какой-то мальчик вышел из женского общежития, однако до этого он туда не входил."
    
    show misha sign_smile at twoleft
    show shizu basic_normal at tworight
    with charachange

    mi "Ты не находишь это странным, Хисао?"

    hi "Не особо… А что в этом странного?"
    
    show misha cross_grin at twoleft
    with charachange

    mi "Ха-ха-ха~! Хисао! Просто подумай!"
    
    show misha sign_smile at twoleft
    with charachange

    mi "Если утром в общежитие не заходило ни одного мальчика, а один вышел…"
    
    show misha perky_smile at twoleft
    show shizu behind_blank at tworight
    with charachange

    mi "Это значит…"

    hi "Понятия не имею. Не могла бы ты просветить меня?.."

    show misha cross_laugh at twoleft
    play sound sfx_impact
    with vpunch
    #misha more lol

    "Миша бьёт меня по спине с такой силой, что от удара я чуть не ложусь на свою парту."

    mi "Это значит, что ты оставался в женском общежитии на ночь, ведь так?"

    "Мне стоило бы догадаться, что они тщательнейшим образом уже всё разузнали."

    hi "Возможно. Но вас-то почему это так беспокоит?"
    
    show misha sign_smile at twoleft
    with charachange
    show shizu basic_normal at tworight
    with charachange
    show misha perky_smile at twoleft
    with charachange
    #signing between the girls

    mi "Мы же Школьный совет, ты не забыл?"
    
    show shizu behind_blank at tworight
    with charachange

    mi "В наши обязанности также входит забота об образе жизни учеников."
    
    show shizu adjust_happy at tworight
    with charachange

    "Словно по команде Миши, %(name_shizune)s резким движением поправляет на носу очки, стараясь подчеркнуть важность сказанного."

    "Интересно, долго они репетировали этот жест?"

    hi "По-моему, вы суёте нос не в своё дело, тебе так не кажется?"
    
    show misha hips_grin at twoleft
    play sound sfx_impact
    with vpunch

    "И снова я получаю нехилый удар в спину."
    
    mi "Мы не суём нос не в своё дело, если это часть наших обязанностей, верно, верно?"
    
    stop music fadeout 3.0

    "К счастью, в этот момент появляется Муто и кладёт конец нападкам Миши."
    
    hide misha
    hide shizu
    with charaexit
    
    show bg school_scienceroom at bgleft
    with charamove
    
    show muto normal
    with charaenter
    
    #hide shizune and misha
    #show muto from right

    mu "Эх… теперь все… экзамены."

    mu "Готовьтесь."
    
    show muto smile
    with charachange

    mu "Итак, на сегодняшнем уроке…"
    
    "Такое вот пространное напоминание о грядущих экзаменах."

    "Как бы то ни было, он бубнит о них уже несколько недель кряду, так что, думаю, его они достали не меньше, чем нас."

    "С другой стороны, по нему не скажешь, что его это сильно волнует…"

    "И его бессвязные лекции, кажется, не претерпели ни малейшего изменения в этот нелёгкий для каждого ученика период."
    
    hide muto
    with charaexit
    #hide muto with dissolve

    "Под его монотонный бубнёж я непроизвольно возвращаюсь к событиям прошлого вечера."

    "Ханако вела себя довольно странно."

    "Даже несмотря на то, что позволила мне заглянуть в её прошлое, она выглядела весьма счастливой."

    "Как будто она поведала мне какую-то тайну, которая долгое время не давала ей покоя."

    "Этой исповедью был рассказ… о её друге, который «убежал»."

    "Я знаю, что не должен лезть не в своё дело, но я слишком любопытен, чтобы не делать этого."

    "Возможно, я потом поинтересуюсь у Лилли – вдруг она что-нибудь знает?"
    
    #*****************************************
    scene bg school_hallway3 
    show crowd
    with shorttimeskip
    play sound sfx_normalbell
    #sfx bells
       
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 0.5

    "Подобно стаду оленей, ученики несутся занимать лучшие места в столовой."
                
    show hanako basic_bashful
    with charaenter

    "В этой суматохе я поглядываю на Ханако, которая показывает пальцем вверх, отодвинув сумку так, чтобы я мог увидеть это."

    "Не надо быть семи пядей во лбу, чтобы догадаться, что это может значить."
    
    stop ambient fadeout 0.5
    
    scene bg school_staircase1 
    with locationskip

    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_rooftop

    "Я проталкиваюсь сквозь толпу и направляюсь к выходу на крышу."

    play sound sfx_door_creak
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')
    
    scene white 
    with dissolve

    with Pause(1.0)
    
    show bg school_roof at bgright
    with locationchange
    #bg roof1 with transition

    "Я поднимаюсь по лестнице раньше Ханако, но на крыше уже кто-то есть."
    
    play music music_emi fadein 4.0

    show emi excited_laugh at twoleft
    show rin basic_awayabsent at tworight
    with charaenter
    #show emi and rin
    #going for the record of sprites in a scene!

    emi "…а потом как – БАМ!!! – и всё прошло."
    
    show emi excited_happy at twoleft
    show rin relaxed_doubt at tworight
    with charachange

    $ i = renpy.random.randint(1,40)
    if i == 1:
      rin "Не знала, что так можно использовать лимоны…"
    else:
      rin "Не знала, что такое можно сделать с арахисовым маслом."
    
    show emi basic_happy at twoleft
    with charachange

    emi "О, привет, Хисао! Ты наверняка слышал эту историю! Я…"

    hi "Э… Что-то подсказывает мне, что лучше бы я её и не слышал…"

    show emi sad_shy at twoleft
    with charachange
    #emi ???

    emi "Правда? Ну ладно тогда."
    
    show rin basic_deadpansurprised at tworight
    with charachange

    rin "Если ты здесь не ради истории, тогда зачем ты здесь?"

    hi "Я просто собирался перекусить с…"

    ha "Х… Хисао? Ты здесь?"

    hi "…Ханако."
    
    show hanako defarms_worry at offscreenright
    with None
    
    show bg school_roof at center
    show emi sad_shy at left
    show rin basic_deadpansurprised at center
    show hanako defarms_worry at right
    with charamove
    #show Hanako, if she'll fit… surprised
    
    show emi basic_grin at left
    show rin basic_absent at center
    with charachange

    emi "О! Приветики, Ханако!"

    ha "Э… Эми… Рин… Здравствуйте…"

    "Похоже, Ханако не ожидала увидеть тут кого-то ещё, но уже через секунду она берёт себя в руки."

    show hanako basic_normal at right
    with charachange
    #hanako neutral.

    ha "Хисао… Если хочешь, у меня тут есть бутерброды…"
    
    show hanako cover_distant at right
    with charachange

    ha "Обычно я делаю их для Лилли, но я совсем забыла, что её нет, и…"

    hi "Звучит заманчиво. На моём месте было бы глупо отказываться, верно?"
    
    show emi basic_closedhappy at left
    with charachange
    #Emi delighted

    emi "Эхехехе! Она предлагает ему приготовленный своими руками ланч!"

    emi "Ну разве это не прекрасно, Рин?"
    
    show rin relaxed_nonchalant
    with charachange

    "Отсутствующим взглядом Рин окидывает раскинувшийся за забором городской пейзаж."
    
    rin "Раз ты так говоришь, то так оно и есть."

    show hanako emb_downtimid at right
    with charachange
    #haanko embarrassed looking down

    ha "Это… не то, что ты думаешь…"

    ha "Просто я приготовила больше, чем нужно…"
    
    show hanako emb_timid at right
    with charachange

    ha "…хочешь, я и с тобой поделюсь, Эми."
    
    show emi excited_amused at left
    with charachange
    #Emi big smile

    "Эми широко улыбается и наклоняется к Ханако, чтобы взять её подбородок в свои ладони."
    
    emi "Нет, нет, нет. Я просто хочу увидеть распускающийся прямо здесь и сейчас бутон романтических отношений."

    show hanako defarms_shock at right
    with charachange
    
    $ doublespeak(hi, ha, u"Это не то, что ты думаешь!", u"Это не то, что ты думаешь…")
    
    show emi excited_laugh at left
    with charachange
    #emi laughs

    emi "Просто классика…"
    
    show rin basic_absent
    show hanako def_worry at right
    with charachange

    rin "Так когда подлатают Лилли?"
    
    show emi basic_grin at left
    with charachange

    hi "Её выписывают сегодня, так что сюда она вернётся, наверное, вечером."
    
    show rin negative_spaciness
    with charachange

    rin "Это хорошо. А то застревать в одном месте надолго плохо."

    hi "Думаю, тут ты права."

    "Похоже, Рин избегает зрительного контакта со своим оппонентом."

    "Её взгляд теперь направлен вниз, на территорию школы, в бесконечном поиске… кто его знает чего."

    show emi sad_annoyed at left
    with charachange
    
    emi "Может, перестанешь уже менять тему?"
    
    show emi basic_happy at left
    with charachange

    emi "Я хочу посмотреть, как ты будешь есть её сэндвич!"
    
    show emi excited_joy at left
    with charachange

    emi "И не забудь сказать ей, что он восхитительный, даже если это не так!"
    
    show emi excited_proud at left
    with charachange

    emi "ТЕМ БОЛЕЕ, если это не так!"

    "Такое чувство, будто из-за этого Эми сама себя изводит, доводя до исступления, и я начинаю беспокоиться за нашу безопасность."

    "Не похоже, что ограждение способно сдержать разошедшуюся на полную катушку Эми."
    
    show hanako emb_downtimid at right
    with charachange

    ha "П… пожалуйста. Скорее всего, они не так уж и хороши…"
    
    show emi basic_happy at left
    with charachange

    emi "Вот оно! Отлично!"
    
    hi "Ну ладно. Ханако, я хотел бы попробовать один из твоих бутербродов."

    show hanako emb_smile at right
    with charachange
    #hanako embarrassed yet smiling, Emi expectant

    "Ханако разворачивает пакет и извлекает из него сэндвич."

    ha "Держи…"
    
    show emi basic_concentrate at left
    with charachange

    "Эми напоминает чайку, смотрящую на туристов, которые едят чипсы."

    "Её глаза пристально следят за тем, как я беру у Ханако бутерброд и медленно подношу его ко рту."

    "Я практически ощущаю её дыхание, когда откусываю кусочек, и повисшую в воздухе напряжённость, когда проглатываю его."

    hi "Неплохо. Совсем неплохо."
    
    show emi excited_circle at left
    show rin basic_surprised
    show hanako defarms_shock at right
    with vpunch
    #emi angry? Or something like that

    emi "СДЕЛАЙ ЭТО ПРАВИЛЬНО!"

    "Вспышка Эми заставляет всех подскочить на месте, включая даже безучастную к происходящему Рин."

    hi "Вау… Ладно, ладно…"

    hi "Он… восхитительный…"

    show emi basic_closedgrin at left
    show hanako def_worry at right
    with charachange
    #Emi :3

    emi "Видишь, так же гораздо лучше."
    
    emi "Теперь это самый настоящий любовный ланч на крыше."

    hi "Думаю, тебе стоит сходить провериться…"
    
    show rin basic_deadpanamused
    with charachange

    rin "Я который год говорю ей то же."

    "В устах Рин такое замечание звучит особенно обидно."

    "Но Эми даже не обращает на это внимания, будучи полностью погружённой в мир своих фантазий."

    hi "Теперь-то мы можем спокойно поесть?"

    show emi sad_grin at left
    with charachange
    #emi not :3

    emi "Что? Ах да, приступайте."
    
    stop music fadeout 6.0

    "Эми, увидевшая то, что так хотела, теперь, кажется, потеряла к нам всяческий интерес."
    
    hide emi
    hide rin
    with charaexit
    
    show bg school_roof at bgleft
    show hanako def_worry at center
    with charamove
    
    #hide emi and rin

    "Ханако присаживается напротив выхода на крышу, и я пристраиваюсь рядом."

    #Hanako neutral looking down

    "Но не настолько близко, чтобы снова привлечь нездоровое внимание со стороны Эми."
    
    play music music_another fadein 6.0

    hi "Спасибо большое. Этим утром я совершенно забыл про ланч."
    
    show hanako emb_emb
    with charachange

    #hanako embarrassed, looking down smiling

    ha "На здоровье. Я просто приготовила слишком много…"

    hi "Я так и понял. Это было сумасшедшее утро."
    
    show hanako emb_downsmile
    with charachange

    ha "Да уж."

    hi "Слушай, может устроим вечером небольшую вечеринку по поводу возвращения Лилли?"

    hi "Я могу пройтись по магазинам и купить торт и прочее, а ты пока подготовишь её комнату?"
    
    show hanako basic_smile
    with charachange

    #hanako neutral smile

    ha "Звучит заманчиво."

    hi "Тогда решено."
    
    #stop music fadeout 6.0

    hi "Встречаемся в комнате Лилли в шесть, хорошо?"
    
    show hanako cover_bashful
    with charachange

    ha "Хорошо, буду тебя там ждать."
    
    show emi sad_grin at leftdoor
    with vpunch
    #emi, at right, smile
    
    #play music music_emi fadein 0.000001

    emi "Там – это где?"
    
    show hanako cover_distant
    with charachange

    "Чёрт, совсем забыл, что она всё ещё здесь."
    
    show bg school_roof at center
    show emi sad_grin at twoleft
    show hanako cover_distant at tworight
    with charamove

    hi "Да ничего такого. Просто мы строим планы на вечер."

    emi "Ого! Уже свидание?! Но ведь она только-только начала готовить тебе ланчи!"
    
    show emi basic_happy at twoleft
    with charachange

    emi "Ты двигаешься уверенными темпами, Хисао!"

    hi "Нет же, дурочка. Это для Лилли."

    show emi excited_proud at twoleft
    with charachange
    #emi poke tounge

    emi "Я знаю. Но вас так прикольно дразнить."
    
    show emi basic_closedgrin at twoleft
    with charachange

    emi "Передавайте Лилли привет."
    
    show emi basic_closedgrin at offscreenleft
    with charamove
    
    #stop music fadeout 6.0

    "После этого Эми уходит, пройдя мимо меня и Ханако и волоча за собой за пустой рукав Рин."
    
    show bg school_roof at bgleft
    show hanako cover_distant at center
    with charamove

    "Я смотрю на Ханако, опасаясь, как бы она снова не замкнулась в себе."
    
    show hanako basic_smile
    with charachange
    #Hanako neutral, slight smile

    "Но, вопреки ожиданиям, она выглядит весьма довольной сложившейся ситуацией."

    hi "С тобой всё в порядке, Ханако?"
    
    show hanako basic_normal
    with charachange

    ha "А? Да…"
    
    show hanako basic_bashful
    with charachange

    ha "Я просто подумала, что она… хороший человек."

    hi "Кто?"

    ha "Эми. Она… хорошая."

    hi "Но она просто дразнила нас…"
    
    show hanako emb_emb
    with charachange

    "Ханако качает головой."

    ha "Просто это она так забавляется."

    ha "И она хороший друг для Рин."

    ha "Разве это не значит, что она хорошая?"

    hi "Пожалуй, ты права."

    hi "Однако нам пора бы уже возвращаться в класс."

    hi "С минуты на минуту прозвенит колокол, а тут его звон слышен очень громко."
    
    show hanako basic_smile
    with charachange

    ha "Эх… Ладно."
    
    stop music fadeout 8.0

    hi "Я тогда сразу после уроков пойду за тортом для Лилли, так что встречаемся у неё в комнате в шесть, ага?"

    ha "К… конечно."
    
    show hanako basic_bashful
    with charachange

    ha "Увидимся."
    
    hide hanako
    with charaexit
    
    play sound sfx_doorclose
    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    
    scene black
    with dissolve

    with Pause(1.0)
    
    scene bg school_staircase1
    with locationchange
    
    play sound sfx_normalbell

    #sfx bells
    #bg fade out
    
    stop ambient fadeout 2.0

    "Как только мы закрываем дверь, раздаётся звон колокола. Его оглушительный перезвон напоминает ученикам о предстоящих скучных уроках второй половины дня."

    return

    #*****************************************
label ru_HT5:
    
    scene bg school_staircase1
    with locationchange

    #aslo, this scene tok forever. If it fails, please let me know.
    #Yes, Hanako at the end is a little OOC. I'm not sure if it's overly so, nor do I intend to use "crazy" as an excuse.
    #Please let me know if it's too far over the top, or if it needs explaination or something.

    scene bg school_dormlilly 
    with shorttimeskip
    #bg dormlilly with timeskip
    show hanagown normal at tworightsit
    show lilly basic_smile_paj at twoleftsit
    with charaenter
    #show lilly and Hanko in pyjamas
    
    $ renpy.music.set_volume(0.80000000000000004, 1.0, channel='music')
    play music music_one fadein 4.0
    
    li "Боже, боже, и вовсе не стоило…"

    "Лилли, всё ещё охрипшая после операции, кажется несколько поражённой оказанным ей приёмом."

    hi "Ерунда. Это всего всего-навсего вечеринка в честь возвращения домой тех, кто рисковал своими жизнями."

    show lilly basic_giggle_paj at twoleftsit
    with charachange
    #lilly giggle

    li "Ох, я не думаю, что рисковала жизнью. Всё же это довольно распространённая операция…"

    show hanagown smile at tworightsit
    show lilly basic_smile_paj at twoleftsit
    with charachange
    #lilly restore

    ha "Я… мы просто очень рады, что ты вернулась."

    hi "Ладно, довольно формальностей! У меня тут есть торт, который почему-то всё ещё никто не ест…"
    
    show lilly basic_satisfied_paj at twoleftsit
    with charachange

    li "Великолепно! Последнюю неделю я не ела ничего, кроме больничной пищи, так что кусочек тортика придётся как нельзя кстати!"

    show lilly basic_smile_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange
    
    "Торт исчезает практически в тот же миг, что я его нарезаю."

    "Думаю, девушки действительно не могут ничего с собой поделать, когда дело доходит до сладкого…"

    "…"

    "Хотя я тоже съел свой кусочек, так что не мне их судить."
    
    show hanagown smile at tworightsit
    with charachange

    ha "Это… было очень вкусно."
    
    show lilly basic_cheerful_paj at twoleftsit
    with charachange

    li "Да уж, действительно. А где, говоришь, ты его покупал, Хисао?"

    hi "А? Да в продуктовом… Там ещё дисплей такой…"

    show hanagown distant at tworightsit
    show lilly basic_pout_paj at twoleftsit
    with charachange
    #both girls, looking displeased.

    li "Полноте, Хисао. Уж в этом вопросе нас обманывать не стоит."

    ha "Кто же покупает торты в таких магазинах?"

    hi "А? А что-то не так?"
    
    show lilly basic_listen_paj at twoleftsit
    with charachange

    li "Мне кажется, ты не очень-то разбираешься в некоторых жизненных тонкостях, Хисао."

    hi "Понятия не имею, что ты имеешь в виду."
    
    show hanagown irritated_alt at tworightsit
    with charachange

    ha "Торты нужно покупать в булочной."
    
    show lilly basic_cheerfulblush_paj at twoleftsit
    with charachange

    li "А не в продуктовом магазине."
    
    show hanagown normal_alt at tworightsit
    with charachange

    ha "Это аксиома."

    hi "Ну… ладно. Постараюсь запомнить на будущее."

    hi "Но разве он был так уж плох?"
    
    show lilly basic_pout_paj at twoleftsit
    with charachange

    li "Ну, раз уж ты об этом заговорил, он был несколько суховат…"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "И он мог бы быть и послаще…"

    hi "Хорошо, хорошо, я понял! Никогда больше так не поступлю! Простите!"
    
    show hanagown smile at tworightsit
    show lilly basic_planned_paj at twoleftsit
    with charachange
    #both girls, happy

    li "Я рада, что ты усвоил этот урок."

    li "Не стоит недооценивать важность таких вопросов."

    hi "Да понял я."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Хорошо. Не расскажет ли мне кто-нибудь о событиях, произошедших на этой неделе?"
    
    show lilly basic_oops_paj at twoleftsit
    with charachange

    li "А то у меня ощущение, будто все меня оставили далеко позади, а сами ушли вперёд."
    
    show hanagown normal at tworightsit
    with charachange

    hi "Да ничего интересного не было."

    ha "Разве что все о тебе беспокоились."

    hi "Ах да, и экзамены. Они будут уже на следующей неделе."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Что ж, полагаю, за учебную неделю действительно не так уж много может произойти."
    
    "На этом разговор неожиданно заходит в тупик."
    
    show hanagown distant at tworightsit
    with charachange

    "Лилли продолжает пить так изящно, как и всегда; прям картинка с обложки."

    "Ханако же держит свою чашку обеими руками, аккуратно поднося её к губам."

    "Она напоминает мне хомячка, грызущего кукурузные зёрнышки."
    
    play sound sfx_teacup

    "По привычке я начинаю подбирать остатки торта."
    
    hi "Лилли, вы с сестрой больше не общались?"
    
    show lilly basic_surprised_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange

    li "Так ты виделся с Акирой?"

    hi "Да, позавчера. Похоже, вы с ней не так часто встречаетесь."
    
    show lilly basic_sad_paj at twoleftsit
    with charachange
    #lilly sad

    li "Верно. Жаль, учитывая, что мы живём так далеко от дома."
    
    show lilly basic_reminisce_paj at twoleftsit
    with charachange

    li "Но, полагаю, мы все в одинаковой ситуации."
    
    show hanagown distant at tworightsit
    with charachange
    #Hanako …. quizzical? Whatever is closer.

    ha "…так или иначе…"

    show lilly basic_smile_paj at twoleftsit
    with charachange
    #lilly neutral

    li "Однако было здорово пообщаться и справиться о том, как идут дела у родных."

    hi "А ты не хотела бы повидать их во время каникул?"
    
    show lilly basic_listen_paj at twoleftsit
    with charachange

    li "Нет, не думаю. Уж больно они далеко."

    hi "Серьёзно? И как далеко?"

    li "Южная Африка."

    "Я в шоке замираю, чуть не выронив из рук тарелку с крошками."

    hi "Южная Африка? Ты имеешь в виду ту самую Африку?"
    
    show lilly basic_ara_paj at twoleftsit
    with charachange

    li "Да, та самая Африка, только Южная."
    
    show hanagown irritated_alt at tworightsit
    with charachange

    ha "А ты не знал?"
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Прости, что не сказала тебе раньше, Хисао."

    hi "Это… здорово, я полагаю…"

    hi "А чем в таком случае ты планируешь заниматься на каникулах?"

    #lilly/Hanako pondering
    show hanagown normal at tworightsit
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Думаю, надо бы съездить ненадолго в летний домик моей семьи на Хоккайдо."

    li "В нём есть всё необходимое, но, с другой стороны, он достаточно далеко от цивилизации, так что в нём очень спокойно."

    hi "Звучит здорово. А у тебя какие планы, Ханако?"

    show hanagown worry at tworightsit
    with charachange
    #hanako thinking

    ha "Я точно пока не знаю. Может, поеду с Лилли…"
    
    show lilly basic_cheerful_paj at twoleftsit
    with charachange

    li "Кстати, отличная мысль. Ты можешь отправиться вместе с нами, Хисао."
    
    show hanagown smile at tworightsit
    with charachange

    li "Чем больше народу, тем веселее."

    "Быть приглашённым посетить отдалённый летний домик с двумя девушками…"

    "Да какой же ненормальный откажется от такого предложения?"

    hi "Здорово. Я поговорю с родителями."

    ha "Было бы неплохо, если б они тебя отпустили."

    hi "Я уверен, что отпустят."

    "Но в этот момент меня осеняет, что у нас есть более насущные проблемы."
    
    show hanagown normal at tworightsit
    with charachange

    hi "Но… разве нам не стоит беспокоиться об экзаменах, прежде чем строить какие-либо планы?"
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Из-за операции у меня есть возможность отложить сдачу…"
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Но я не думаю, что ею воспользуюсь."

    "Лилли права. Одного взгляда на её комнату достаточно, чтобы понять, что она очень много читает."

    hi "Хех. Везучая. А что насчёт тебя, Ханако? Как обстоят дела у тебя?"
    
    show hanagown distant at tworightsit
    with charachange

    "Со стороны Ханако слышится странный звук, будто она закашлялась."

    "Похоже, мой вопрос застал её врасплох и чай попал ей не в то горло."
    
    show hanagown worry_blush at tworightsit
    with charachange
    #hanako embarrasseed
    
    $ renpy.music.set_volume(0.00000000000000004, 4.0, channel='music')

    ha "Я… я ещё не думала об этом."
    
    show hanagown distant_blush at tworightsit
    with charachange
    
    $ renpy.music.set_volume(0.00000000000000004, 1.0, channel='music')

    ha "Но, кажется, мне стоит подналечь на учёбу…{w=.3}{nw}"
    
    show hanagown worry_alt at tworightsit
    show lilly basic_concerned_paj at twoleftsit
    with vpunch
    play sound sfx_impact

    li "Егерхк!"

    #lilly shocked

    "Услышав это странное восклицание Лилли, Ханако замолкает."

    "Когда я поднимаю на неё глаза, Лилли ставит чашку на стол и хватается руками за горло."

    hi "Лилли? Что случилось?!"
    
    show lilly basic_displeased_paj at twoleftsit
    with charachange

    "Лилли требуется некоторое время, чтобы успокоиться, после чего она убирает руку от горла."

    show lilly basic_surprised_paj at twoleftsit
    show hanagown distant at tworightsit
    with charachange
    #lilly calm again
    
    li "Ах, прости меня, Хисао. Похоже, моё горло не до конца ещё зажило."

    li "Я сделала слишком большой глоток, вот оно и заболело."

    hi "Хочешь, я вызову медбрата?"
    
    show lilly basic_sad_paj at twoleftsit
    with charachange
    
    $ renpy.music.set_volume(0.80000000000000004, 6.0, channel='music')

    li "Нет, спасибо, я уже в порядке. Просто мне стоит быть аккуратнее."
    
    show hanagown normal at tworightsit
    with charachange

    ha "Точно?"

    li "Я уверена."

    #only fools are positive.

    #are you sure?

    #I'm positive.

    hi "Тем не менее тебе стоит отдохнуть. Как насчёт того, чтобы лечь спать?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Думаю, это хорошая идея, Лилли."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange
    #lilly Happy

    li "Ты прав. Сидение допоздна вряд ли пойдёт мне на пользу."
    
    show hanagown normal_blush at tworight
    with charamove

    "Ханако встаёт, и мы начинаем наводить порядок на столике."
    
    show lilly basic_weaksmile_paj at twoleft
    with charamove
    
    show bg school_dormlilly at bgright
    show lilly basic_weaksmile_paj at left
    show hanagown normal_blush at right
    with charamove

    "Лилли поднимается и начинает аккуратно ощупывать корешки стоящих на полке книг, на которые шрифтом Брайля нанесены их названия."

    "Наконец она находит искомую книгу и снимает её с полки."
    
    show hanagown normal_blush at tworight
    with charamove

    "Ханако расставляет посуду по местам и направляется к выходу из комнаты."

    ha "Спокойной ночи, Лилли."

    hi "Спокойной ночи, Лилли. Отдохни хорошенько."

    show lilly basic_smile_paj at left
    with charachange
    #lilly big smile
    
    stop music fadeout 6.0

    li "Постараюсь. Ещё раз спасибо вам."
    
    hide hanagown
    with charaexit
    
    play sound sfx_dooropen

    "Ханако выходит в холл, я следую за ней и закрываю за собой дверь."
    
    scene bg school_girlsdormhall
    with locationchange
    
    show hanagown distant
    with charaenter
    #bg dormhall
    #hanako looking down.
    
    play sound sfx_doorclose

    "Дверь захлопывается с характерным щелчком, и я сталкиваюсь лицом к лицу с Ханако, которая отводит взгляд."

    ha "М… Хисао?.."

    hi "Что случилось?"

    "Ханако нервно играется с волосами, накручивая несколько прядей вокруг пальцев."
    
    show hanagown distant_blush
    with charachange
       
    ha "М… Я просто хотела сказать с… спасибо."

    ha "Что не рассказал Лилли о прошлой ночи."

    hi "Всё в порядке. Если что, я так же виноват в этом, как и ты."
    
    show hanagown distant_alt
    with charachange
    
    with Pause(0.2)
    
    show hanagown distant_blush
    with charachange

    "Ханако качает головой, не переставая возиться с волосами."

    ha "Нет… нет, это была моя вина."

    ha "Поэтому… я… я хочу отблагодарить тебя по-настоящему."
    
    show hanagown normal_blush
    with charachange
    #Hanako Defiant

    "Ханако оставляет волосы в покое и переводит взгляд на меня."

    ha "Закрой глаза."

    hi "Ась?"

    ha "П-просто сделай это. Пожалуйста."

    "Я неохотно подчиняюсь."
    
    scene black 
    with shuteye

    #BG blackout with eyes closed.

    "Я слышу, как Ханако делает глубокий вдох и подходит ко мне."

    #it would be nice if there were an effect here, but I can live without it.
    
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    play music music_twinkle fadein 0.1

    "Я ощущаю тепло рядом с моим лицом, и Ханако чмокает меня в щёку."

    hi "Ась?"
    
    scene bg school_girlsdormhall
    show hanagown normal_blush
    with openeye

    #BG Dormhall with eyes open.
    #Hanako Embarrassed.

    ha "Я… Ли… Я думаю, что должна больше… больше…"
    
    show hanagown smile
    with charachange

    ha "Так я… благодарна тебе."

    "Я рад, что Ханако не молчит, потому что если бы она ждала моей реакции, то, боюсь, я не выдал бы ничего умного."

    "Но откуда это, чёрт возьми, взялось?"
    
    show hanagown normal_blush
    with charachange

    ha "Я думаю… Мне нужно перестать полагаться на вас двоих."

    hi "Полагаться на нас?"

    hi "Разве не для этого и нужны друзья?"
    
    show hanagown distant_blush
    with charachange

    ha "Да, но…"
        
    #"For some reason, I feel compelled to pat Hanako on the head."
    #I'm sorry, but I had to comment this out. Holy hell does crud like to make Hisao pat Hanako's head... -Alphabro

    hi "Не бери в голову."

    hi "Лилли немного неважно себя чувствует, но я уверен, что скоро всё нормализуется."

    ha "Ладно…"

    hi "Тебе тоже не помешало бы немного отдохнуть."
    
    show hanagown normal_blush
    with charachange

    ha "Ладно…"
    
    show bg school_girlsdormhall at bgleft
    show hanagown normal_blush at tworight
    with charamove

    "Ханако отворачивается и идёт к себе в комнату."

    hi "Ах да, Ханако…"

    "Она замирает, положив руку на ручку двери."

    hi "…Спасибо за это."
    
    show hanagown smile at tworight
    with charachange
    #Hanako embarrassed smile

    "Ханако неожиданно наклоняет голову и улыбается мне."
    
    stop music fadeout 6.0

    ha "Всегда пожалуйста!"
    
    play sound sfx_dooropen
    
    show hanagown smile at offscreenright
    with charamove
    
    "Прежде чем я успеваю хоть как-то отреагировать, она бросается к себе в комнату и закрывает за собой дверь."
    
    hide hanagown
    with None
    #hide Hanako with move right

    "Я стою один посреди коридора, на щеке осталось ощущение тепла губ Ханако."

    "Тот, кто сможет её понять, должен быть в некотором роде гением."

    "Я, словно зомби, направляюсь к себе в комнату, размышляя над тем, какая же Ханако загадочная."
    
    scene bg school_dormhallway
    with shorttimeskip
    #bg dormdoor

    "Я останавливаюсь перед дверью %(name_kenji)s, желая узнать его мнение о сложившейся ситуации…"

    #it would be good to get the following in some kind of flash-back or something…

    ke "Это заговор!"

    "Да уж. Всё же он не лучшим образом разбирается в такого рода вещах."

    "Мне кажется, что он так или иначе омрачит моё настроение."

    "Сейчас удобный момент сбежать с этой чайной вечеринки. Разговор об экзаменах выбил меня из колеи."

    "Полагаю, самое время предаться зубрёжке…"
    
    scene black
    with dissolve

    return

label ru_HT6:

    #Yet another song name for the title.
    #Transition from the last scene with eyes closed/eyes open
    #perhaps we could have a shot of books on a desk for this commonly recurring theme?
    #also, damn, 11 days between scenes. Freaking work
       
    scene black 
    with dissolve
          
    scene bg school_dormhisao
    with openeye
    #bg dormroom with eyes open.
    
    $ renpy.music.set_volume(0.80000000000000004, 6.0, channel='music')
    
    play music music_daily fadein 10.0

    "Хех. Просыпаюсь я до будильника."

    "Какая редкость."

    "Но пять минут погоды не сделают, так что снова засыпать нет никакого смысла."

    "Быстренько умываюсь и одеваюсь – и вот я готов к новым свершениям…"

    "…на добрых полчаса раньше, чем обычно."

    "Думаю, надо использовать эту редкую возможность, чтобы спокойно позавтракать."
    
    scene bg school_cafeteria
    with shorttimeskip
    #bg cafeteria with dissolve

    "Как и ожидалось, даже небольшая разница во времени имеет колоссальное влияние на заполненность столовой."

    "Это место кажется почти заброшенным, что означает, что я могу спокойно съесть довольно обильный завтрак."

    "Ну, почти заброшенным."
    
    show bg school_cafeteria at bgright
    with charamove

    hi "Привет, Лилли."

    show lilly basic_surprised
    with charaenter
    #show Lilly generic

    li "Хисао?"

    hi "Ага, это я."
    
    show lilly basic_cheerful
    with charachange

    li "Доброе утро. Непривычно видеть тебя так рано."

    hi "Да вот как-то так получилось… Как твоё горло?"

    show lilly basic_smile
    with charachange
    #show Lilly smiling

    li "Гораздо лучше, спасибо."

    hi "Приятно слышать. Не хотелось бы видеть тебя долго недееспособной."

    hi "Это угнетает…"

    show lilly basic_ara
    with charachange
    #show lilly laugh

    li "Полно, Хисао, ты говоришь так, будто у меня какая-то страшная болезнь. И Ханако говорит точно так же."

    "Упоминание Ханако вызывает в памяти наше вчерашнее странное расставание."

    hi "Скажи, Лилли… Вы с Ханако общались в последнее время?"
    
    show lilly basic_weaksmile
    with charachange

    li "Да, разумеется. Что именно тебя интересует?"

    hi "М… Не замечала ли ты каких-нибудь странностей в её поведении? Или каких-нибудь перемен?"

    show lilly basic_oops
    with charachange
    #show lilly concerned

    li "Да ничего вроде не приходит в голову. А что, что-то случилось?"

    hi "Ну, да… нет…"
    
    show lilly basic_planned
    with charachange
    
    li "Наверное?"

    hi "Э?"
    
    show lilly basic_weaksmile
    with charachange

    li "Прости, просто я закончила шаблон за тебя."

    hi "А, понятно."
    
    show lilly basic_smile
    with charachange

    "Чёрт возьми, я сбился с мысли. Думаю, нужно просто рассказать всё как есть."

    hi "В общем… Вчера вечером Ханако… Она…"

    hi "Она меня поцеловала."
    
    show lilly basic_ara
    with charachange
    #show Lilly happy

    #"Kareha" "ままま!" <- This is the kind of face I was thinking of.

    li "Боже, боже, вот так поворот!"

    li "Пожалуйста, расскажи подробнее!"

    "Лилли выглядит очень довольной этим. Как будто она смотрит мелодраму."

    "Это как-то даже на неё не похоже."

    "Как бы то ни было, я обильно краснею. Слава богу, поблизости никого нет."

    hi "Ничего такого, правда."

    hi "Просто чмокнула меня в щёку."

    hi "Но это было так неожиданно… Вот я и решил поинтересоваться, может ты ей что-то такое сказала… или что-то…"

    "Хоть она и не может видеть моё лицо, но мой растерянный голос наверняка выдаёт моё смущение."
    
    show lilly basic_cheerful
    with charachange

    li "Что ж, это действительно неожиданно."
    
    show lilly basic_smile
    with charachange

    li "Похоже, пока я была в больнице, Ханако взяла инициативу в свои руки."

    "Полагаю… такое вполне возможно."

    "Чёрт возьми, всё же я не понимаю женщин."

    #Could not resist.

    hi "Понятно… А утром вы сегодня не встречались?"
    
    show lilly basic_weaksmile
    with charachange

    li "Нет, не встречались. Я ушла прежде, чем она проснулась."

    hi "Вот как. Значит, мы с ней ещё увидимся."
    
    show lilly basic_smile
    with charachange

    li "Вряд ли у неё есть повод не приходить на занятия."

    hi "И то верно. Однако завтрак остывает. Если ты не против, я бы поел."
    
    li "Приятного аппетита."
    
    $ renpy.music.set_volume(0.39999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 2.0
    
    hide lilly
    with charaexit
    
    show bg school_cafeteria at center
    with charamove

    "Слишком поздно. Наша беседа с Лилли слишком затянулась, и мой фантастический завтрак уже остыл."
    
    "И, в завершение всего, столовая медленно заполнялась учениками и все лучшие завтраки наверняка уже разобраны."

    "И это воспринимается как плохое предзнаменование."

    "Я без особого энтузиазма закидываю в рот остывшую пищу; Лилли просто сидит напротив, позволяя мне спокойно поесть."

    "Чтобы хоть как-то уменьшить дискомфорт от потребления холодной еды, я заглатываю её практически не жуя."

    "Но это не очень-то помогает."

    extend " Даже, скорее, наоборот."
    
    show lilly basic_cheerful at centersit
    with charaenter

    li "Ты, видимо, очень голоден, раз так ешь."

    hi "Нет, я просто хочу поскорее разделаться с завтраком."

    hi "Ты сейчас к себе в класс пойдёшь? Тебя проводить?"
    
    show lilly basic_ara at centersit
    with charachange

    li "Ох, Хисао, это так по-джентльменски. Какая женщина сможет тебе отказать?"

    hi "Э… Я не знаю."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Правильный ответ: невежливая."

    hi "И то верно."
    
    hide lilly
    with charaexit
    
    show bg school_cafeteria at bgleft
    with charamove
    
    stop music fadeout 6.0

    "Размышляя о том, как я умудрился не ответить на такой простой вопрос, я собираю тарелки и отношу их в окошко буфета."

    #Yeah, I get it, none of you will know what a scullery is, either. Gimme a replacement, please.
    
    show bg school_cafeteria at center
    with charamove
    
    show lilly cane_smile
    with charaenter
    
    "К тому времени, как я возвращаюсь к Лилли, она уже взяла свою сумку и трость и ждёт меня."

    #bg school hallway
    
    stop ambient fadeout 1.0
    
    scene bg school_hallway3
    show lilly cane_smile
    with locationskip

    li "Что ж, тут мы расстанемся, Хисао."
    
    show lilly cane_weaksmile
    with charachange

    li "Не стоит сильно переживать насчёт Ханако. Благодаря тебе она стала гораздо самоувереннее."

    "Пользуясь тем, что Лилли не видит, как я покраснел, я спешу закончить этот разговор."

    hi "Непременно. Увидимся после уроков."
    
    play sound sfx_dooropen
    
    hide lilly
    with charaexit

    "Лилли исчезает в дверях своего класса, а я иду дальше, в свой."

    scene bg school_scienceroom at bgleft
    with locationchange
    #bg classroom
    
    $ renpy.music.set_volume(1.0, 0.1, channel='music')
    
    play music music_normal fadein 8.0

    "Пока пришли только самые прилежные ученики, они спешат воспользоваться тишиной и покоем, уткнувшись в учебники."

    "Нет ни %(name_shizune)s, ни Миши. Что даже странно."

    "Зато есть кое-кто, чьё присутствие меня удивляет."
    
    show bg school_scienceroom at center
    with charamove
    
    show hanako emb_downtimid at twoleft
    with charaenter
    #show Hanako distracted/neutral

    hi "Привет, Ханако. Как дела с утра пораньше?"
    
    show hanako defarms_shock at twoleft
    with vpunch
    #show Hanako embarrassed

    ha "А… Хисао… Д–доброе утро."

    "Ханако аж подпрыгивает на звук моего голоса, смутившись чуть больше обычного."

    hi "Всё в порядке?"
    
    show hanako emb_blushtimid at twoleft
    with charachange
    #Show Hanako panicked

    ha "Где? А… Ага, я в порядке. А… ты… как?"

    hi "Я… в порядке. Ты уверена, что у тебя всё хорошо?"
    
    show hanako emb_downtimid at twoleft
    with charachange

    "Ханако паникует, словно кролик, пойманный в клетку; она отчаянно оглядывается, ища повод сменить тему."

    show bg school_scienceroom at bgright
    show hanako emb_downtimid at center
    with charamove

    show hanako emb_downtimid_close
    with charachange
    
    "Я наклоняюсь к ней и заговорщицки шепчу."

    hi "Эй, послушай, если это из-за произошедшего вчера, то не беспокойся."

    hi "Мне… даже понравилось."
    
    show hanako defarms_blush_close
    with charachange
    #hanako Mega panic.

    "Бешено крутящаяся по сторонам голова Ханако замирает, её лицо заливается румянцем."
    
    show misha perky_smile behind hanako
    with charaenter
    
    stop music fadeout 3.0

    "Только теперь я замечаю по другую сторону Ханако склонившееся так же близко, как и я, ещё одно лицо."

    #show Misha neutral/serious

    mi "Думаю, ей это тоже понравилось, да?"
    
    play sound sfx_impact
    
    show bg school_scienceroom at bgleft
    show misha cross_laugh at twoleft
    show hanako defarms_worry at tworight
    with vpunch
    
    play music music_running fadein 2.0

    "Я как ужаленный отскакиваю назад, едва не снося стоящую у меня за спиной парту."

    hi "М–М–Миша! Когда ты подошла?"
    
    show misha sign_smile at twoleft
    with charachange
    
    "Миша встаёт, оставляя застывшую в состоянии шока Ханако."

    mi "Вижу, я пришла как раз вовремя, чтобы услышать кое-что интересненькое, а?"

    show misha hips_grin at twoleft
    with charachange
    #misha lol

    mi "Ах, Хисао и Ханако~"

    mi "Кое-чем занимались этой ночью~"

    mi "Мне не терпится рассказать %(name_shizune)s."
    
    show hanako emb_blushtimid at tworight
    with charachange

    hi "Нет, подожди! Ты не можешь…"

    "Слишком поздно."
    
    play sound sfx_impact2
    
    with Pause(0.5)
    
    play sound sfx_footsteps_hard

    "За спиной я слышу звук с силой брошенной на стол сумки и последующий за этим разгневанный топот."
    
    show misha hips_grin at left
    show hanako emb_blushtimid at right
    with charamove
    
    show shizu cross_angry
    with charaenter
    #show Shizune, angry.

    shi "…"
    
    show misha sign_smile at left
    with charachange
    
    show shizu basic_angry
    with charachange
    
    show misha perky_smile at left
    with charachange
    #shizune and Misha signing

    mi "%(name_shizune)s хочет сказать, что… хм… «братание»… в общественных местах не допускается."

    mi "Она также считает, что заниматься личными делами накануне экзаменов – плохая идея."

    show misha hips_smile at left
    with charachange
    
    mi "А ещё она думает, что если вы хотите передать друг другу записки, то стоит пользоваться более цивилизованным способом доставки…"
    
    show hanako emb_downtimid at right
    with charachange

    hi "Постой, ты сейчас вообще о чём?"

    hi "Ты всё поняла неправильно, между нами ничего такого нет…"

    hi "Стоп… Записки?"
    
    show misha sign_smile at left
    with charachange
    show shizu behind_frown
    with charachange
    show misha perky_smile at left
    with charachange

    "Миша быстро что-то показывает %(name_shizune)s, которая на это предъявляет маленькую записку."

    "Сверху неразборчивым почерком написано «Для Хисао»."

    mi "Ты оставила это на столе, где каждый может это увидеть."
    
    show misha cross_frown at left
    show shizu adjust_frown
    with charachange

    mi "Меня не волнует, чем вы занимаетесь в свободное время, но не нужно заниматься этим в классе."

    mi "Всё ясно?"

    "Иногда я задаюсь вопросом: считает ли %(name_shizune)s Мишу своим другом или она ей нужна исключительно для озвучивания её мыслей?"
    
    show hanako emb_blushing at right
    with charachange

    "Я вырываю записку из руки %(name_shizune)s и замечаю, как при этом вздрогнула Ханако."

    hi "Хорошо, я понял."

    hi "Да уж, вы знаете толк в том, как неверно истрактовать ситуацию."

    hi "Никакого «кое-что» между нами не было."
    
    show misha cross_grin at left
    with charachange
    #misha :p

    mi "Ра~зумеется, ничего такого не было."
    
    show misha perky_smile at left
    with charachange

    mi "Как бы то ни было, похоже у вас есть какие-то дела друг к другу, так что пока оставим вас наедине."

    mi "Верно, %(name_shizune)s?"
    
    show shizu basic_angry
    with charachange

    shi "…"
    
    hide shizu
    hide misha
    with charaexit
    
    stop music fadeout 4.0
    
    $ renpy.music.set_volume(0.39999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 2.0
    
    show bg school_scienceroom at center
    show hanako emb_blushing at center
    with charamove
    
    "Я с облегчением выдыхаю, когда Миша утаскивает %(name_shizune)s к их местам, оставив меня с потрясённой Ханако."

    "Она выглядит слишком напряжённой для продолжения разговора, так что я решаю сперва прочитать записку."

    play sound sfx_impact

    show hanako defarms_shock
    with vpunch
    #Hanako Embarrased/defiant
        
    stop ambient fadeout 1.0

    ha "НЕЧИТАЙЭТО!"
    
    "В классе воцаряется тишина: всем интересно, что стало причиной этой внезапной вспышки."

    hi "Э… Ладно…"

    hi "Мне её вернуть?"

    ha "Нет!"

    hi "Э… Хорошо. То есть мне просто не читать её?"
    
    show hanako emb_downtimid
    with charachange
    #Hanako looking down, embarrassed

    ha "Н… нет. Просто… не читай её сейчас."
    
    play sound sfx_normalbell
    
    #Wrong kind of peal. -md01
    #"The school bells peel throughout the classroom, and I am forced to return to my seat…"
    "Звон колокола разносится по классу, и я вынужден вернуться на своё место."

    #"…but not before I pat Hanako on the head."
    #Holy hell, crud... It doesn't even make sense here- Alphabro
    
    hide hanako
    with charaexit
    #hide Hanako

    "Пока урок в самом разгаре и %(name_shizune)s с Мишей ожесточённо конспектируют, я разворачиваю крошечное письмецо."

    $ written_note(u"Дорогой Хисао,\n Я хочу кое-что тебе сказать.\nПожалуйста, давай встретимся после уроков за общежитиями.")
    #lawl, be there or i'll {s}kill you{/s} go home? d.

    "Хех, не подписано."

    "С другой стороны, несложно сообразить, кто именно его написал."

    "Убедившись, что учитель повёрнут лицом к доске, я оборачиваюсь к Ханако."
    
    show bg school_scienceroom at bgright
    with charamove
    
    show hanako emb_blushing at twoleft
    with charaenter

    #show Hanako Embarrassed

    "Привлечь её внимание оказывается совсем несложно; такое чувство, будто она всё утро только и делает, это смотрит мне в спину."

    "Я киваю на записку, а потом показываю ей поднятый вверх большой палец."
    
    show hanako emb_downsmile at twoleft
    with charachange

    #Show Hanako embarrassed looking down, smiling

    "Она отворачивается, делая вид, что не замечает меня."
    
    show hanako emb_smile at twoleft
    with charachange
    
    with Pause(0.6)
    
    show hanako emb_downsmile at twoleft
    with charachange

    "Но, спустя мгновение, бросает на меня короткий взгляд, показывает мне большой палец в ответ и вновь притворяется, что не обращает на меня внимания."

    "Учитель" "Накай! Смотри на доску!"
    
    hide hanako
    with charaexit
    
    show bg school_scienceroom at bgleft
    with charamove

    hi "Простите…"

    "Учитель" "Одними извинениями не отделаешься. Я хочу, чтобы ты открыл свой учебник на странице 54…"

    "Хех, полагаю, именно об этом пытался меня предупредить мой остывший завтрак…"

    return
    
label ru_HT7:
    
    scene bg school_scienceroom at bgleft
    with locationchange
    
    scene bg school_scienceroom
    with shorttimeskip

    "К моему облегчению, тот момент, когда я без лишней скромности мог бы назваться звездой класса, довольно быстро проходит."

    "Учитель" "Так, ладно. Давайте продолжим…"

    "Слова одно за другим вылетают изо рта учителя, но я чувствую, что ничего не понимаю."

    "Проходит пол-урока, я смотрю на свои конспекты и вижу только феерию каракулей."

    "Даже здесь, где мои мысли обретают какую-то форму, нет никакого порядка, только хаотичное нагромождение кракозябр и загогулин."
    
    play sound sfx_normalbell

    "К счастью, звучит колокол, спасая меня от этой напасти."
    
    show bg school_scienceroom at bgleft
    with charamove
    
    show hanako emb_timid at right
    with charaenter
    
    with Pause(0.6)
    
    show hanako emb_timid at offscreenright
    with charamove

    "Я поворачиваюсь, чтобы поговорить с Ханако, но только и вижу, как она исчезает за дверью класса."

    "Похоже, она ещё не готова к разговору со мной."

    "С другой стороны, это даёт мне некоторое время, чтобы навести в голове порядок."

    "Мне нужно с кем-нибудь поделиться терзающими меня мыслями, и я знаю только одного человека, способного справиться с этой задачей."

    scene bg school_miyagi at bgright
    with locationskip
    #bg school roof- nah, I've been tainted by the Final route. Make this the tearoom
    
    play music music_friendship fadein 4.0
    
    show lilly basic_smile at tworightsit
    with charaenter
    #show Lilly neutral

    hi "Лилли, можешь уделить минутку?"
    
    li "Ну конечно. Что случилось, Хисао?"

    #"Thankfully, Lilly is the only person on the roof today. I don't know what I would do if Rin and Emi were here today."
    "К счастью, в чайной комнате сегодня одна только Лилли. Я не знаю, что бы я делал, окажись здесь Ханако."

    hi "Эм… Это насчёт Ханако…"

    show lilly basic_oops at tworightsit
    with charachange
    #show lilly concerned.

    li "Что-то пошло не так?"

    hi "Ну… Не совсем."

    hi "Она… э… вручила мне что-то типа… письма."

    li "Письма? Какого письма?"

    "Я начинаю нервно ёрзать."

    "Это довольно очевидно, о чём Ханако хочет со мной поговорить, но, несмотря на это, меня распирает от любопытства."

    hi "Как бы это… В общем, она попросила встретится с ней после уроков."

    li "В письме? Но почему она просто не подошла и не сказала?"

    hi "Вот об этом… я и хотел спросить у тебя."

    hi "Помнишь, я утром спрашивал тебя о Ханако?"
    
    show lilly basic_weaksmile at tworightsit
    with charachange

    li "Конечно."

    hi "Мне кажется, что, возможно… ну, не знаю…"
    
    li "А может быть, ты ей просто нравишься?"

    "Меня накрывает волна эмоций."

    "Не то чтобы это известие было для меня неожиданным, но всё же…"

    "Но услышать такое из чьих-то уст довольно волнительно."

    hi "Да, что-то в этом роде."
    
    show bg school_miyagi at bgleft
    show lilly basic_weaksmile at centersit
    with charamove
    
    #show lilly basic_weaksmile
    #with charamove

    "В растерянности я присаживаюсь рядом с Лилли."
    
    show lilly basic_smile at centersit
    with charachange

    li "И это вся проблема?"

    hi "Я… не знаю."

    hi "Я ещё не думал об этом."

    "Не находя себе места, я запускаю руку в карман и извлекаю оттуда записку Ханако."

    "Просто подержав её пару секунд в руке, я испытываю совершенно иные эмоции."

    hi "Знаешь…"

    extend " Это не первый раз, когда я получаю такого рода записку…"

    show lilly basic_planned at centersit
    with charachange
    # lilly curious, or something like that.

    li "Серьёзно? Ты, должно быть, красавчик, Хисао."

    hi "Это совсем не то, что я хотел сказать."
    
    $ renpy.music.set_volume(0.00000000000000001, 4.0, channel='music')
    
    "Ещё немного, и мною овладеет паника. И, прежде чем я успеваю это осознать…"

    hi "Это произошло в моей старой школе…"

    "…Я рассказываю Лилли о том, как в прошлый раз получил подобное письмо."

    hi "Я получил записку, в которой было указано время и место, и потом оказалось, что оно было от девушки, которая мне нравилась."
    
    show lilly basic_listen at centersit
    with charachange

    hi "Собственно, тогда-то и случился сердечный приступ."

    hi "Врачи узнали об этом и сказали, что во всём был виноват стресс…"

    li "Ясно."

    li "Было бы печально, если бы подобное повторилось снова."

    li "Но в этот раз ты хотя бы знаешь, от кого это письмо, да?"

    hi "Ну, если я не ошибаюсь, то да."
        
    show lilly basic_weaksmile at centersit
    with charachange

    li "Так что от части сюрпризов ты уже избавлен, да?"

    hi "Полагаю, что так."
    
    show lilly basic_smile at centersit
    with charachange
    
    $ renpy.music.set_volume(1.0, 4.0, channel='music')

    li "С другой стороны, возможно, потребуется проделать некоторую дополнительную работу."

    hi "С другой стороны?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Ну, тебе действительно нравится Ханако?"

    "Лилли произносит это так буднично, будто спросила у меня, который сейчас час."

    "Я хочу ответить ей также непринуждённо."

    hi "М… Ну… Она мне нравится. Но и ты мне нравишься тоже."

    show lilly basic_displeased at centersit
    with charachange
    #lilly sad/frustrated/thinking/something like that.

    "Лилли вздыхает."

    li "Давай попробуем подойти с другой стороны."
    
    show lilly basic_oops at centersit
    with charachange

    li "Что ты думаешь делать после окончания школы?"

    hi "А? Поступать в институт, вероятно."

    hi "Но причём тут это?"
    
    show lilly basic_listen at centersit
    with charachange

    "Лилли игнорирует мой вопрос и продолжает:"

    li "На кого ты намерен учиться?"

    hi "Наверное, естественные науки."

    hi "Но…"

    li "Но почему?"

    "Лилли просто движется дальше; полагаю, мне просто нужно с этим смириться."

    hi "Я не совсем уверен. Просто это то, что мне нравится."
        
    show lilly basic_smile at centersit
    with charachange

    li "То-то и оно."

    hi "А? Что?"
    
    show lilly basic_planned at centersit
    with charachange
    #lilly whimsical, or something.

    li "Ты планируешь собственную жизнь, собираясь пойти по пути наименьшего сопротивления."

    li "Так какой смысл столько размышлять над чем-то столь тривиальным, как школьный роман?"

    "Я пытаюсь как-то опровергнуть её слова, но не могу."

    "В её словах есть смысл, как бы цинично это не звучало."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Я так понимаю, что тебе это кажется… ну… несколько прямолинейно?"

    hi "Да… пожалуй."

    li "Хорошо. Просто ответь мне на один вопрос:"

    extend " Есть ли у тебя какая-нибудь неприязнь к Ханако?"

    hi "Нет… Она действительно мне нравится."

    hi "С чего ты взяла, что я испытываю к ней неприязнь?"
    
    show lilly basic_smile at centersit
    with charachange

    li "Тогда я думаю, что ты только что сам развеял свои сомнения."

    show lilly basic_ara at centersit
    with charachange
    #lilly coquettish or something like that

    li "Разве что у тебя больше нет никого на примете."

    hi "А? Нет, что ты."
    
    show lilly basic_smile at centersit
    with charachange

    li "Тогда я предлагаю тебе не отказываться от предложения Ханако."

    li "Это вам обоим пойдёт на пользу."

    li "Это поможет тебе справиться с последствиями твоего сердечного приступа, а ей – вылезти из своей скорлупы."

    hi "Но… я всё ещё не уверен…"

    show lilly basic_weaksmile at centersit
    with charachange
    #lilly small smile

    "Лилли поворачивается ко мне и затем, ощупав меня чуткими пальцами, кладёт свои руки мне на плечи."

    li "Тебе нужна уверенность?"
    
    li "Полагаю, это будет волнующе: с головой броситься в омут отношений в таком-то возрасте."

    #lawl nympho Lilly appears

    li "А если что-то не сложится, всегда можно будет вернуться к тому, чтобы быть друзьями."

    li "Я всегда буду рада вас поддержать."

    hi "Спасибо, Лилли."

    show lilly basic_smile at centersit
    with charachange
    #Lilly Smiles

    li "Всегда пожалуйста, Хисао."

    li "Однако, если я не ошибаюсь, нам уже пора."

    #li "We should leave here before the bells start. It's awfully loud from here…"
    li "Нам нужно выйти до конца перемены, чтобы без толчеи добраться до класса."

    hi "Согласен. Давай я тебе помогу…"
    
    #show lilly basic_smile at centersit
    #with charamove
    
    show bg school_miyagi at bgright
    show lilly basic_smile at tworightsit
    with charamove
    
    show lilly basic_smile at tworight
    with charamove

    "Я быстро встаю на ноги и нежно беру Лилли за руку, помогая ей подняться."
    
    play sound sfx_doorclose
        
    scene bg school_hallway3
    show lilly basic_smile
    with locationchange
    
    stop music fadeout 4.0
   
    with Pause(0.4)
    
    play sound sfx_normalbell
    
    
    #"It seems that Lilly's sense of time is correct; as soon as I close the door to the stairwell, the bells clamour into life."
    "Кажется, чувство времени Лилли не подвело; как только я закрываю за нами дверь в чайную комнату, по школе проносится колокольный звон."

    #BG hallway

    "Второй раз за сегодня мы с Лилли расстаёмся в коридоре."
    
    show lilly back_giggle
    with charachange

    "Она машет мне рукой на прощание, и я без задних мыслей машу ей в ответ."
    
    hide lilly
    with charaexit
    

    "Упрекнув себя за столь необдуманный поступок, я просто говорю ей вслед:"

    hi "Увидимся, Лилли. И снова спасибо."

    #bg classroom
    scene bg school_scienceroom
    with locationchange
    
    play ambient sfx_paperruffling

    "В моём классе царит привычная суматоха: ученики пытаются успеть как можно больше в оставшееся до начала урока время."

    "Как будто они сачковали всю перемену, а теперь норовят наверстать упущенное до прихода учителя."

    stop ambient fadeout 0.5

    "Не важно, что это: чесание языками или списывание домашки, – они просто обязаны оставить всё на последний момент."
    
    #Eh, placeholder for some extra "deep" should I want to put it in later.
    #something about how this reflects on Hisao x Hanako and what Lilly said.

    "Но одного персонажа в этой нескончаемой драме всё же не хватает."
    
    "Месту в последнем ряду у окна явно не достаёт Ханако."

    "Думаю, она избегает меня из-за смущения… или типа того."
    
    show bg school_scienceroom at bgleft
    with charamove

    "Я не спускаю глаз с двери, ожидая её появления."
    
    play sound sfx_dooropen
    
    show hanako emb_timid at offscreenright
    with None
    
    show hanako emb_timid at right
    with charamove
    
    #with Pause(0.4)
    
    show hanako emb_timid at rightsit
    with charamove
    
    hide hanako
    with charaexit

    "В тот же миг, как учитель начал открывать одну дверь класса, в другую дверь просачивается Ханако и бежит к своей парте."

    "Видимо, она до самого последнего момента караулила в коридоре."
    
    show bg school_scienceroom at center
    with charamove

    "Не желая повторить собственную участь, что постигла меня сегодня, я не отвлекаюсь и смотрю на доску, конспектируя по мере необходимости."

    "Благодаря ободряющим словам Лилли, я чувствую себя удивительно собранным, причём не только по поводу предстоящего свидания с Ханако, но и по части учёбы."
    
    
    show bg school_scienceroom_ss
    with shorttimeskip
    
    play sound sfx_normalbell

    "Так что я немало удивляюсь, когда раздаётся звон колокола, извещающий об окончании урока."
    
    show bg school_scienceroom_ss at bgleft
    with charamove
       
    show hanako emb_timid_ss at right
    with charaenter
    
    #with Pause(0.4)
    
    show hanako emb_timid_ss at offscreenright
    with ease

    "Со скоростью, которой позавидовала бы даже газель, Ханако скрывается за дверью прежде, чем я успеваю к ней повернуться."

    "Стресс, я полагаю."

    "Что ж, в этом нет ничего странного."

    #BG Hanako's wall from Act 1. I know we're not using that scene anymore, but I like that shot.
    
    scene bg school_dormext_full_ss at bgleft
    with locationskip
    
    $ renpy.music.set_volume(0.1, 0.0, channel='ambient')
    play ambient sfx_crowd_outdoors

    "За общежитиями царит прохлада и покой."

    "Неподалёку слышатся приглушённые голоса учеников, болтающих о том о сём."

    "Ободряющие возгласы со стороны спортивных клубов, звуки готовки и уборки со стороны общежитий."
    
    stop ambient fadeout 3.0

    "Но всё это кажется таким… далёким."

    "Словно какой-то невидимый барьер препятствует внешнему миру просачиваться в этот всеми забытый клочок земли между зданиями общежитий и забором интерната."

    "Но я здесь не один; проходит несколько мгновений, прежде чем я замечаю сгорбленную фигуру, прислонившуюся к каменной стене."
    
    show bg school_dormext_full_ss at bgright
    with charamove
    
    show hanako emb_blushing_ss
    with charaenter
    #Show Hanako embarrassed
    
    hi "Так всё же это была твоя записка?"

    ha "М… э… да. Думаю, ты знал об этом, верно?"

    hi "Я догадывался…"
    
    "Над нами проносится птичья трель, давая Ханако возможность собраться с духом."
    
    show hanako emb_downtimid_ss
    with charachange

    ha "М… Х–Хисао?.."

    hi "Да?"
    
    show hanako emb_blushtimid_ss
    with charachange
    #Hanako Embarrased, looking down. Or perhaps a super embarrassed.

    ha "Ч… что ты обо мне думаешь?"

    "Полагаю, спрашивать напрямую не так просто, но столь расплывчатая постановка вопроса слишком даже для Ханако."

    hi "Ну… Ты мне нравишься. Ты хороший друг."
    
    show hanako emb_blushing_ss
    with charachange

    ha "И… это всё?"

    "У меня такое чувство, что это всё же далеко не всё."

    hi "А что ты думаешь обо мне, Ханако?"
    
    show hanako basic_worry_ss
    with charachange
    #Hanako embarrassed, surprised

    ha "Я?"

    ha "Думаю о тебе…"
    
    show hanako emb_blushtimid_ss
    with charachange

    ha "Ум… Э…"

    hi "Не спеши… У нас весь день впереди."
    
    show hanako emb_downtimid_ss
    with charachange

    "Ханако глубоко вздыхает."
    
    show hanako emb_blushtimid_ss
    with charachange

    ha "Ты тоже мне нравишься, Хисао."

    hi "Приятно слышать."

    hi "Так о чём ты хотела со мной поговорить?"

    "Ханако оглядывается, по-видимому чтобы убедиться, что никто не подглядывает."
    
    show hanako basic_worry_ss
    with charachange

    ha "Ты… ты помнишь, что я говорила, что когда-то у меня был друг?"

    "Я напрягаю память, но почти сразу вспоминаю её слова, которые она сказала тогда в комнате Лилли."

    hi "А, что у тебя был друг?"

    "Ханако просто кивает в ответ."

    #It is quite possible that this bit will change a little, depending on if I keep the whole
    #"dead boyfriend" thing. I dunno.
    
    show hanako emb_blushtimid_ss
    with charachange
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    
    play music music_innocence fadein 3.0

    ha "Он… он тоже сказал, что я хороший друг…"

    extend " когда я вот так же спросила его."
    
    show hanako emb_downtimid_ss
    with charachange

    ha "Но я… я убежала."

    ha "Я убежала, а он гонялся за мной."

    #Hanako crying
    
    show hanako emb_downtimid_cry_ss
    with charachange

    ha "И… и потом…"
    
    show bg school_dormext_full_ss at center
    show hanako emb_downtimid_cry_ss at twocenteroff3
    with charamove

    "Ноги Ханако подкашиваются, и она начинает медленно падать."
    
    show bg school_dormext_full_ss at bgleft
    show hanako emb_downtimid_cry_ss at center
    with ease
    
    show hanako emb_downtimid_cry_close_ss
    with charachange
    
    "Инстинктивно я бросаюсь к ней и ловлю её, прижимая к своей груди."

    ha "Пообещай мне… Обещай, что ты не умрёшь, как…"

    hi "Я… обещаю."
    
    show hanako emb_sad_cry_close_ss
    with charachange

    "Ханако тяжело всхлипывает, уткнувшись в мою грудь, а потом, вся красная, поднимает взгляд на меня."

    ha "Хисао…"
    
    show hanako emb_timid_cry_close_ss
    with charachange

    ha "Я люблю тебя."

    "Совет Лилли проносится по моему мозгу со скоростью миллиона километров в секунду, как и воспоминания о времени, проведённом с Ханако."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    show ev hanako_kiss_scroll:
        xalign 0.5 yalign 0.5 ypos 0.0
        linear 6.0 ypos 0.65
    with dissolve

    "Но, прежде чем принять взвешенное решение, я наклоняюсь и крепко обнимаю Ханако."
    
#    play sound sfx_whiteout
#    
#    scene white 
#    with dissolve
#    
#    show ev hanako_kiss_easein
#    with dissolve

    "Соль её слёз смешивается с нейтральным вкусом её гигиенической помады, когда мы целуемся."
    
    "Я чувствую, как Ханако обняла меня, всё сильнее сжимая в своих объятиях."
    
    with Pause (0.5)
    
    scene white 
    with dissolve
    
    scene bg school_dormext_full_ss at bgright
    show hanako basic_bashful_close_ss
    with dissolve
           
    "Когда мы отрываемся от губ друг друга, кажется, будто прошла вечность; мы смотрим друг другу в глаза."

    hi "Такой ответ тебя устроит?"

    show hanako emb_smile_close_ss
    with charachange
    #Hanako happy embarrassed

    ha "Я… я думаю, что вполне."
    
    hi "Что ты собираешься делать завтра после уроков?"
    
    #show hanako emb_timid_close_ss
    #with charachange

    ha "Н–ничего."

    hi "Хочешь, давай куда-нибудь выберемся?"
    
    show hanako basic_bashful_close_ss
    with charachange
    #Hanako smile

    ha "Да… И, кажется, я знаю отличное местечко."

    hi "Серьёзно? Какое?"
    
    show hanako cover_bashful_close_ss
    with charachange

    ha "Это… моё секретное место."
    
    ha "Я отведу тебя туда."

    hi "Звучит здорово. Что мне взять с собой?"
    
    show hanako basic_normal_close_ss
    with charachange

    "Ханако выглядит так, словно получает доступ к редко используемым ячейкам памяти."

    ha "Может, чего-нибудь поесть?"

    hi "Считай, уже сделано."

    hi "Но… чем займёмся сейчас?"

    show hanako emb_smile_close_ss
    with charachange
    #Hanako defiant smile

    ha "М… У меня есть идея…"

    "И Ханако снова притягивает меня к себе и призывно тянется своими губами к моим."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
#    show ev hanako_kiss2
#    with dissolve

    show ev hanako_kiss_outside
    with dissolve

    "Учитывая, что чуть более трёх часов назад у меня были сомнения по этому поводу, я практически не сопротивляюсь."

    return

label ru_HT8:
    
    scene bg school_dormext_full_ss
    show hanako emb_smile_close_ss
    with dissolve

    "Неровно дыша, мы с Ханако отрываемся друг от друга."

    hi "Ух… вау."
    
    show hanako emb_downsmile_close_ss
    with charachange
    #Hanako Look down smile

    ha "Ага… вау."

    hi "Ну, увидимся завтра."

    ha "Ага… в… классе…"

    hi "Да, в классе, точно."

    "На мгновение мы замираем, не зная, что сказать, и просто стоим, стараясь не глядеть друг на друга, чтобы снова не потерять над собой контроль."
    
    show hanako emb_smile_close_ss
    with charachange

    ha "Я… пожалуй, пойду."

    hi "Да, я тоже. Если мы собираемся завтра прогуляться, то сегодня нужно будет сделать домашнее задание за два дня."
    
    show hanako defarms_shock_close_ss
    with charachange
    #hanako shocked

    ha "О, точно! Надо готовиться!"
    
    show hanako defarms_worry_close_ss
    with charachange

    ha "И я должна постараться… тоже."
    
    show hanako def_smile_close_ss
    with charachange
    #hanako slight smile

    ha "Спокойной ночи, Хисао."
    
    stop music fadeout 6.0

    hi "И тебе, Ханако."
    
    hide hanako
    with charaexit

    "Этот неловкий момент расставания; мы расходимся, исчезая за разными углами здания, которое только что скрывало нас от всего окружающего мира."

    #bg dormhall
    scene bg school_dormhallway
    with locationskip
    
    "Когда я прохожу мимо двери комнаты %(name_kenji)s, во мне разгорается желание поговорить с кем-нибудь о своих новообретённых отношениях."

    "Даже ценой выслушивания лекции о фашистской природе противоположного пола."

    "Сперва я хочу осторожно постучаться…"

    #bg dorm door
    show bg school_dormhallway at bgright
    with charamove
    
    play sound sfx_doorknock

    "Но вспоминаю, о чём мне говорил %(name_kenji)s, и начинаю лупить в его дверь что есть мочи."

    "Ответа нет."

    "Возможно, опять смотрит что-то сомнительное в своих наушниках."
    
    play sound sfx_doorknock

    "Я снова и снова молочу кулаком с дверь, пока моя рука не начинает болеть."

    "Ну ладно, полагаю, что я всё же смогу держать распирающие меня эмоции в себе."

    "Раз так, то самое время предаться учёбе…"

    #BG dormroom
    scene bg school_dormhisao_ss
    with locationchange
    
    play music music_comfort fadein 3.0

    "Неудивительно, что я не могу сосредоточиться."

    "Я открываю учебник, щёлкаю механическим карандашом и, прислонив его к лицу, погружаюсь в чтение…"

    "Мои губы…"

    "Чёрт. Я смог целых пятнадцать секунд не думать о том, что сегодня произошло."

    "Но я должен собраться. Я собираюсь завтра вторую половину дня провести с Ханако, а это значит, что до домашнего задания я доберусь только поздно вечером."

    "Экзамены очень важны… Верно?"

    "Я снова возвращаюсь в мыслях к дневной беседе с Лилли."

    "Чем я планирую заниматься после школы?"

    "Что, если годы, потраченные на учёбу, окажутся всего лишь пустой тратой времени?"

    "Если у меня нет какой-то конкретной цели, то какой смысл вот так выкладываться?"

    "…"

    "Ладно, уже прошло добрых десять минут, нужно возвращаться к книгам."

    "Я не хочу завтра, гуляя с Ханако, думать только об отставании в учёбе…"

    "С другой стороны, а что, если из-за этого всё пойдёт наперекосяк?.."

    "Ничего не получается. Мне нужно успокоиться."
    
    stop music fadeout 4.0

    "Может, мне прилечь на пару секунд?.."
    
    scene black
    with shuteye
    
    window hide
    
    with Pause(2.0)
    
    play sound sfx_alarmclock
    
    with Pause(0.6)
    
    window show
    
    scene bg school_dormhisao
    with openeye
    #bg bedroom with eyesopen

    "Так, это тоже не работает."

    "Похоже, учёбу придётся отложить до завтра."

    "Я выключаю будильник и иду в душ."

    "Я как раз успею по-быстрому перекусить перед уроками, если успею принять душ быстрее, чем за три минуты…"

    "Погнали!"

    scene bg school_dormbathroom
    show steam
    show steam2
    with shorttimeskip
    #bg bathroom

    "Похоже, я всё-таки останусь без завтрака."
    
    hide steam
    with charaexit
    
    "Ладно, переживу. Сегодня ж уроки только до обеда и мы, судя по надвигающимся экзаменам, ничего, кроме повторения, делать не будем."
    
    hide steam2
    with charaexit
    
    "По крайней мере, я мог бы компенсировать потерянное вчера время."

    scene bg school_scienceroom at bgleft
    with shorttimeskip

    play music music_normal fadein 0.3
    play ambient sfx_crowd_indoors fadein 0.3
    #bg classroom

    "Каждый раз, когда я захожу в класс в субботу, вспоминаю клетку в зоопарке."

    "На самом деле животным в клетках в зоопарке хорошо."

    "У них есть пища, забота, защита от хищников, участие в селекционных программах…"

    "Всё отлично, как ни крути."

    "Но их дикая сущность всё равно будет заставлять их сопротивляться до последнего, скакать вокруг, шуметь и набрасываться на служителей зоопарка."

    "То же и с классной комнатой."

    "В действительности мы находимся здесь для нашего же блага, но ни один ученик не хочет находиться здесь, тем более когда весь остальной мир наслаждается выходными."

    "Собеседники говорят всё громче, начинают перекрикивать друг друга, пока привычный утренний гомон не превращается в белый шум."

    "Но в дальнем углу класса, лениво глядя в окно, сидит одна ученица."

    "Я бы позвал её, но сомневаюсь, что мне хватит дыхалки перекричать этот гвалт."
    
    show bg school_scienceroom at bgright
    with charamove
    
    stop ambient fadeout 10.0

    "Некоторое время у меня уходит на то, чтобы расчистить путь и пробраться к её парте."
    
    show hanako basic_smile
    with charaenter

    #Hanako basic happy

    hi "Доброго утречка."

    ha "Д… доброе утро."

    hi "Как спалось?"
    
    show hanako basic_normal
    with charachange

    ha "Нормально. А тебе?"

    hi "Без задних ног."

    hi "Кажется, лекарства снова сыграли со мной злую шутку."
    
    show hanako emb_smile
    with charachange
    #Hanako laughs a little

    ha "Будь аккуратнее, порой приём лекарств может привести к непредсказуемому результату."

    hi "Буду иметь это в виду."
    
    show hanako emb_timid
    with charachange

    mi "Иметь в виду что?"
    
    show bg school_scienceroom at bgleft
    show hanako emb_timid at left
    with charamove
    
    show misha hips_grin
    show shizu behind_blank at right
    with charaenter
    #Misha/Shiszune curious

    hi "Нет, ничего, просто говорим о разных лекарствах."

    mi "Лекарствах, да?"
    
    show misha hips_smile
    with charachange

    mi "Полагаю, это достаточно важная тема."

    hi "Что ж, спасибо за твоё одобрение."
    
    show misha perky_smile
    with charachange

    mi "Не за что."
    
    show misha cross_frown
    show shizu basic_normal2 at right
    with charachange

    mi "А что это вы тут вдвоём уединились?"
    
    #Misha pout

    mi "Это как-то не по-дружески."

    hi "Я просто хотел поздороваться с Ханако."
    
    show misha cross_smile
    with charachange

    mi "Ясно, ясно…"
    
    show hanako basic_worry at left
    with charachange

    ha "А я хотела обсудить планы нашего сегодняшнего свидания…"

    mi "Ясно, ясно…"

    show misha perky_confused
    with charachange
    #misha Surprised

    mi "Стоп! Что?!"
    
    show shizu adjust_frown at right
    with charachange

    shi "…"
    
    show misha perky_sad
    with charachange

    mi "Ой, правда, извините…"
    
    show misha sign_confused
    with charachange

    "Миша, которая только что рефлекторно размахивала руками, останавливается на середине предложения и поспешно подходит к %(name_shizune)s."

    #shizune smile
    show shizu behind_smile at right
    show misha perky_smile
    with charachange

    #eh, just trying this out for shits and giggles

    $ doublespeak(shi, mi, "…", u"М… Думаю, вас надо поздравить.")
    
    show shizu adjust_happy at right
    show misha hips_smile
    with charachange

    $ doublespeak(shi, mi, "…", u"Я рада, что вы так хорошо ладите.")

    hi "Вы же… не сошли с ума или типа того?"
    
    show shizu basic_normal at right
    show misha cross_smile
    with charachange

    $ doublespeak(shi, mi, "…", u"С чего бы?")

    hi "Полагаю… что вы правы."
    
    show misha cross_grin
    with charachange

    mi "Ага, отличная работа, Хисао~!"

    mi "Я имею в виду, что вы нам так часто помогали в последнее время, но это не проблема."
    
    show misha perky_smile_close
    with charachange

    "Миша наклоняется ко мне и шепчет на ухо, словно пытаясь скрыть что-то от %(name_shizune)s."

    mi "Между нами говоря, мне кажется, что %(name_shizune)s всё равно выполнила большую часть работы, которую вам поручила."

    show shizu behind_blank at right
    show misha hips_laugh
    with charachange
    #Shizune neutral and misha laughing

    mi "Но теперь Ханако сможет дружить со всеми, верно? Верно?!"
    
    show hanako cover_worry at left
    with charachange

    ha "Я… надеюсь."
    
    show misha hips_grin
    with charachange

    mi "Вот видите! Я думаю, что так будет лучше для всех."
    
    show misha sign_smile
    with charachange

    mi "Приглядывай за ней, Хисао. Хорошо?"

    hi "Ладно, ладно, я понял."

    hi "А теперь не хочешь ли ты обратить внимание на человека, уже некоторое время стоящего перед классом?"
    
    show shizu basic_normal2 at right
    show misha perky_confused
    with charachange
    #misha/Shizune ? faces

    mi "А? О чём ты, Хисао?"
    
    show muto irritated behind misha at tworight
    with charaenter

    mu "Что-то мне подсказывает, мисс %(name_shiina)s, что он имеет в виду меня."

    show shizu basic_normal at right
    show misha perky_sad
    with charachange
    #Misha/Shizune sad
    
    stop music fadeout 6.0

    "Похоже, пока Миша и %(name_shizune)s были увлечены мной и Ханако, Муто уже навёл тишину в классе."
    
    show misha sign_sad
    with charachange
    
    with Pause(0.2)
    
    hide misha
    with charaexit

    "Смущённая, Миша медленно поворачивается к доске, глуповато кланяется и направляется к своему месту."
    
    show shizu behind_blank at right
    with charachange
    
    with Pause(0.2)
    
    hide shizu
    with charaexit

    "%(name_shizune)s следует её примеру, только не кланяется, а просто кивает головой."

    mu "Что ж, теперь, когда вы развили скорость классных сплетен, я попробую разогнать вас до скорости закона относительности…"

    #LOL physics joke. I doubt even people who care will get this one.

    "Пока Миша и %(name_shizune)s расходятся по своим местам, я нежно глажу руку Ханако."
    
    hide hanako
    hide muto
    with charaexit
    
    show bg school_scienceroom at bgright
    with charamove

    #hide Hanako
    
    play music music_another fadein 6.0

    "Я не могу поверить, что они так спокойно восприняли это известие."

    "Хотя, возможно, тот факт, что им об этом рассказала сама Ханако, сыграл определённую роль."

    "Вскоре Муто увлекается собственной лекцией, и я пользуюсь его рассеянностью, чтобы шепнуть Мише…"

    hi "Пс! Миша!"
    
    show misha perky_smile at twoleft
    with charaenter

    #Misha Smile

    mi "Чего тебе?"

    hi "Вы с %(name_shizune)s что, не злитесь?"
    
    show misha perky_confused at twoleft
    with charachange

    mi "На что?"

    hi "Ну, что мы с Ханако встречаемся?"

    #misha small lol
    show misha cross_grin at twoleft
    with charachange

    mi "Ва-ха-ха-ха~! Конечно нет!"

    mi "Ведь %(name_shizune)s сама сказала об этом; с чего бы?"

    hi "Я… не знаю."
    
    show misha cross_smile at twoleft
    with charachange
    #Misha Srsbsns

    mi "Слушай, мы, возможно, и не её друзья, но ведь у неё вообще нет друзей."

    mi "Тем не менее все мы хотим ей добра, верно?"

    mi "Так что если благодаря тебе она станет более общительной, то это ведь прекрасно."

    hi "Звучит логично…"
    
    show misha hips_laugh at twoleft
    with charachange
    #misha big lulz

    mi "Разумеется! Как я и сказала!"

    mi "Ва-ха-ха-ха—{w=.3}{nw}"
    
    show muto irritated behind misha at rightwallopen
    with charaenter

    mu "%(name_shiina)s!.."
    
    show misha perky_sad at twoleft
    with charachange
    #Misha "uh-oh"

    mi "…ха. Простите."

    "Миша возвращается к режиму «прилежная ученица», и Муто продолжает свой бубнёж."
    
    hide misha
    hide muto
    with charaexit
    
    show bg school_scienceroom at bgleft
    with shorttimeskip

    "Как ни странно, очень скоро урок подходит к концу."
    
    show muto normal
    with charaenter

    mu "…на этом всё. Ещё раз напоминаю, что это практически последний урок перед предстоящими на следующей неделе экзаменами."

    mu "В понедельник и во вторник у нас будут дополнительные занятия, так что если у вас возникнут вопросы, то не стесняйтесь и спрашивайте."

    mu "Расписание экзаменов будет вывешено сегодня на доске объявлений, так что, пожалуйста, внимательно с ним ознакомьтесь."

    mu "И…"
    
    play sound sfx_normalbell
    #sfx bells
    
    show muto smile
    with charaenter

    mu "…удачных выходных."

    "К моменту, когда Муто заканчивает предложение, класс уже практически пуст."

    "Прежде чем уйти, он загадочно мне салютует."
    
    hide muto
    with charaexit

    "Полагаю, что чрезмерное увлечение наукой действительно делает людей безумными."
    
    show bg school_scienceroom at bgright
    with charamove
    
    show hanako basic_normal
    with charaenter

    #Hanako, basic

    hi "Итак, где мы встречаемся?"
    
    show hanako cover_distant
    with charaenter

    ha "М… Если тебе не сложно, то давай встретимся через час у Зелёной двери?"

    "Я напрягаю мозг, чтобы понять, о каком именно месте говорит Ханако."

    hi "Зелёная дверь… А, ты имеешь в виду дверь, выходящую на лес за интернатом?"
    
    show hanako basic_smile
    with charachange
    #hanako slight smile

    ha "Верно. Ну как?"
    
    stop music fadeout 6.0

    hi "Отлично. А я пока пойду переоденусь."
    
    ha "Я тоже."

    hi "Увидимся."
    
    show hanako basic_bashful
    with charachange
    #hanako big smile

    ha "Ага."
    
    scene black
    with dissolve

    #Chapter end. Close on a timeskip or something.

    return

label ru_HT9:

    #Splitting this scene to help the H-tagging

    #HT9 – Lullaby for Strain

    #Well, here it is, the fated H-scene scene. It'll take a bit of getting to, but it's there.
    #And I may also have a second one planned.
    #So ner.

    #BG Greendoor with timeskip
    scene bg school_greendoor at bgleft
    with locationchange
    
    play music music_happiness fadein 2.0

    "В этот раз я благодарен тому, что девушки, кажется, могут собираться целую вечность."

    "То, что я вчера так рано уснул, говорит о том, что я не приготовил на сегодня никакой еды, тем самым нарушив данное Ханако обещание."

    "К счастью, у меня ещё осталось кое-что после последнего похода в магазин, так что я поспешно собираю это всё в корзину для пикника."

    "Тем не менее я добрые пятнадцать минут жду прихода Ханако перед небольшой зелёной дверью."

    #Show Hanako casual basic
    show hanako emb_smile_sun
    with charaenter

    ha "П… привет. Давно ждёшь?"

    hi "Не очень. Минут пятнадцать, может…"

    hi "Я тут прихватил немного еды… Хоть я и не знал, куда мы идём, но подумал…"

    "Отличный ход; теперь не имеет значения, что все упаковки вскрыты."

    ha "Думаю, сгодится всё."
    
    show hanako emb_blushtimid_sun
    with charachange

    ha "Но всё ли с тобой будет нормально – тащить всё это?"

    hi "А почему нет? Мы же не полезем в горы или что-то в этом роде, верно?"

    show hanako emb_downtimid_sun
    with charachange
    #hanako look down

    "Ханако отводит взгляд, будто не желая отвечать на этот вопрос."

    hi "…Ведь не полезем ведь, да?"
    
    show hanako emb_blushtimid_sun
    with charachange

    ha "Ну, не совсем… Но… просто немного прогуляемся."

    "Я осматриваю Ханако в её жёлтом платье."
    
    # Inserted dialogue to force the dress to make sense. Sue me. -Alphabro
    "Я несколько удивлён тому, какое платье она выбрала; до сих пор я ни разу не видел, чтобы её шрамы были настолько видны."
    
    "Её волосы скрывают правую часть тела, и она держится от меня немного поодаль. Мне кажется, она стесняется своих ожогов."
    
    "С другой стороны, она решила одеть на наше свидание платье. Это ведь тоже кое о чём говорит, правда?"

    "Как бы то ни было, не похоже, что она собирается подниматься в гору."

    "Может быть, она просто излишне беспокоится обо мне?"

    hi "Что ж, раз так, то не пора ли нам отправляться?"

    hi "А то так и день закончится…"
    
    show hanako emb_emb_sun
    with charachange
    #Hanako casual surprised

    ha "Ах! И правда! Нам нужно идти…"
    
    play sound sfx_door_creak
    
    hide hanako
    with charaexit

    "Ханако распахивает дверь, и в ноздри бьёт прохладный лесной воздух."
    
    scene bg school_forest1
    with locationchange
    
    play ambient sfx_park fadein 2.0
    #bg woods1

    "Мы только вышли под сень леса, а я уже чувствую расслабленность."

    hi "Итак… Куда пойдём?"
    
    show hanako emb_emb_sun at tworight
    with charaenter

    ha "Я хочу показать тебе одно место."

    ha "До него придётся прогуляться, но оно того стоит."

    hi "Хорошо, как скажешь, босс…"
    
    show hanako emb_smile_sun at right
    with dissolvecharamovefast
    
    hide hanako
    with charaexit

    "Ханако улыбается, затем начинает идти в довольно шустром темпе."
    
    scene bg school_forest2
    with locationchange

    "Мне приходится чуть ли не бежать трусцой, чтобы от неё не отставать, при этом смотря под ноги, так как попадающиеся корни так и норовят мне помешать."

    "Но время от времени, оказавшись на более-менее ровном участке пути, мне удаётся некоторое время смотреть на Ханако."
    
    show hanako emb_emb_sun
    with charachange

    "В отличие от меня, она идёт с высоко поднятой головой, но не это привлекает мой взгляд."

    "Она скользит по корням, которые так мне мешают, и каждое движение вызывает волны, пробегающие по её одежде и волосам."

    "Я впервые так к ней присматриваюсь, но мой намётанный взгляд подсказывает мне, что под её свободной одеждой кроется весьма хорошая фигура."

    "Если только…{w=.3}{nw}"
    
    play sound sfx_impact
    show bg school_forest2 at bgright
    show hanako emb_blushtimid_sun at tworight
    with vpunch
    
    with Pause(0.2)
    
    "И в этот момент моя нога зацепляется за очередной корень и я плашмя падаю на землю."

    ha "Ты в порядке?"

    hi "Ага. Я просто не смотрел под ноги, вот и споткнулся обо что-то…"

    "Ханако садится передо мной на корточки и протягивает мне руку."

    "Я должен смотреть под ноги, а не предаваться сексуальным фантазиям."

    "Иначе это может плохо для меня закончится…"

    ha "Я очень быстро иду?"
    
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "Просто я подумала, что мы можем не успеть…"

    hi "Нет, нет, всё в порядке. Я буду внимательнее. Спасибо…"
    
    show hanako emb_blushtimid_sun at tworight
    with charachange

    "Ханако помогает мне подняться, и я собираю высыпавшееся содержимое корзины обратно."

    hi "Так-с, продолжим?"
    
    show hanako emb_emb_sun at tworight
    with charachange

    ha "Хорошо."
    
    hide hanako
    with charaexit

    "Ханако разворачивается на каблуках, и я на мгновение заворожённо замираю, глядя на её развивающиеся волосы и платье."

    "Встряхнув головой, чтобы взять себя в руки, я иду за ней следом."
    
    scene bg school_forestclearing
    with locationchange
    #BG woods 2

    "Мы пробираемся через лес целую вечность."

    "Утоптанная тропинка, по которой мы шли до этого, становится всё менее заметной, пока окончательно не исчезает в траве."
    
    show hanako emb_emb_sun
    with charaenter

    "Но Ханако не сбавляет шаг."

    "Она ловко раздвигает попадающиеся на дороге ветки, тогда как мне каждый шаг даётся всё тяжелее и тяжелее."

    "Думаю, это из-за того, что я рос в городе."

    "Оказавшись на небольшой полянке, мне удаётся посмотреть на часы."

    "Мы идём уже около часа."

    hi "Так…"

    extend " сколько нам ещё идти?"
    
    show hanako emb_smile_sun
    with charachange

    ha "Ещё немного, скоро мы уже это увидим…"
    
    play sound sfx_rustling
    
    hide hanako
    with charaexit

    "Ханако исчезает в густой растительности, и я быстро её догоняю."

    "Я понятия не имею, как отсюда вернуться обратно, если я заблужусь."

    "Но, несмотря на все мои усилия, фигура в жёлтом в итоге исчезает за стеной деревьев."

    hi "Ханако?"

    ha "Я здесь, Хисао… чуть дальше…"
    
    show bg school_forestclearing at bgleft
    with charamove

    "Я иду в окружении бурной растительности на её голос."
    
    stop music fadeout 4.0

    hi "Где? Я тебя не вижу…"
    
    stop music fadeout 1.5

    "Я слышу неровное дыхание Ханако."

    hi "Ханако? С тобой всё в порядке?"
    
    play sound sfx_rustling

    "Я ломлюсь сквозь ветки деревьев, не особо заботясь о возможных последствиях."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    #bg white

    "Яркий свет бьёт мне в глаза, ослепляя после царящего в лесу полумрака."

    ha "Вот мы и пришли."
    
    scene bg school_picnic
    with whiteout

    #bg valley with fade
    
    play music music_twinkle

    "Постепенно зрение возвращается ко мне, и я вижу раскинувшуюся под нами долину."

    "Зелень деревьев тянется покуда хватает глаз, и не видно ни единого признака присутствия человека."

    hi "Где… мы?"
    
    show hanako emb_emb_sun at tworight
    with charachange

    ha "На другой стороне горы."

    hi "Какой прекрасный вид. Как ты нашла это место?"
    
    show hanako emb_downsmile_sun at tworight
    with charachange

    ha "Ну, я часто прогуливала уроки и однажды набрела на него…"
    
    show bg school_picnic at bgright
    show hanako emb_downsmile_sun at right
    with charamove_slow

    "Я отвожу глаза от Ханако, чтобы ещё раз насладиться открывающимся видом на долину."

    "Мы находимся по другую сторону холма, на котором расположен интернат, в противоположной стороне от города."
    
    show hanako emb_smile_sun at right
    with charachange
    
    show bg school_picnic at center
    show hanako emb_smile_sun at tworight
    with charamove

    ha "Тут так просто представить, что на планете больше нет ни одного человека, да?"

    hi "Ага… Да уж…"

    "Мы в полной тишине стоим рядом друг с другом и смотрим на раскинувшийся перед нами вид."

    "Моя рука непроизвольно тянется в сторону, и я чувствую тепло, когда обнимаю Ханако."

    "Я не могу сказать с уверенностью, хочу ли я установить с ней своего рода связь или просто ощутить её присутствие, но я чувствую, что поступаю правильно."

    "Я делаю шаг к обрыву, желая подойти поближе, но Ханако тянет меня за руку обратно."
    
    show hanako emb_blushtimid_sun at tworight
    with charachange

    ha "Не стоит… подходить слишком близко к краю…"

    ha "Это будет долгое падение."
    
    scene bg school_picniccliff at bgleft
    with locationchange

    "Опустив глаза, я понимаю, что она имеет в виду."

    "Мы стоим на чём-то типа поляны, всего в нескольких метрах от края утёса, возвышающегося над обрывом."

    "Покатый зелёный склон искажает перспективу, создавая видимость того, что край дальше, чем есть на самом деле."
    
    scene bg school_picnic
    show hanako emb_emb_sun at tworight
    with locationchange

    hi "Точно. Вас понял."

    hi "Раз так, то, может, перекусим?"

    "По правде говоря, мне очень хочется есть. Пропускать завтрак было не лучшей идеей."
    
    show hanako emb_smile_sun at tworight
    with charachange

    ha "С удовольствием."
    
    show bg school_picnic at bgleft
    show hanako emb_smile_sun at center
    with charamove
    
    show hanako emb_smile_sun at centersit
    with charamove

    "Ханако расправляет платье и садится на траву, а я начинаю распаковывать корзину."

    hi "Тут немного, но я надеюсь, что нам хватит."
    
    show hanako emb_blushtimid_sun at centersit
    with charachange

    ha "Я… не против."
    
    show hanako emb_smile_sun at centersit
    with charachange

    ha "Главное, что мы здесь…"

    "Я наблюдаю за тем, как Ханако ест, не отводя глаз от пейзажа перед нами."

    "И я её понимаю; трудно поверить, что это Япония."

    "Мы довольно быстро разделываемся с имевшимися припасами. Всё же такие вещи, как подготовка к пикнику, лучше доверять девушкам."

    "Я закрываю корзину и снова сажусь рядом с Ханако."
    
    show hanako emb_downsmile_sun at centersit
    with charachange

    "К моему удивлению, она кладёт голову мне на плечо."
    
    show bg school_picnic at center
    show hanako emb_downsmile_sun at tworightsit
    with charamove

    "Я осторожно обнимаю её, и мы просто сидим и смотрим на долину."

    hi "Слушай, Ханако…"
    
    show hanako emb_smile_sun at tworightsit
    with charachange

    ha "Да?"

    hi "Чем ты планируешь заниматься после окончания учёбы?"
    
    show hanako emb_blushing_sun at tworightsit
    with charachange

    "Ханако не двигается, но мне кажется, что я плечом ощущаю ход её мысли."
    
    show hanako emb_blushtimid_sun at tworightsit
    with charachange

    ha "Я пока не думала об этом."

    ha "Может, что-то связанное с медициной…"

    hi "С медициной? А ты сможешь набрать проходной балл?"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Не знаю. А там тоже нужны хорошие оценки?"

    hi "Полагаю, что да."
    
    show hanako emb_blushing_sun at tworightsit
    with charachange

    ha "Ну, не думаю, что у меня такие уж плохие оценки."

    ha "Нужно будет изучить этот вопрос."
    
    "И на этом тема себя изживает."

    "Всё же, несмотря на бросающиеся в глаза очевидные различия, у Ханако и Лилли много общего."

    "И обе они правы."

    "В последнее время моя жизнь кардинально изменилась."

    "У меня всё ещё полно времени до окончания школы."

    "А потом ещё несколько лет до выпуска из университета."

    hi "Жизнь никуда не денется. Я хочу делать то, что мне хочется сейчас."
    
    show hanako emb_emb_sun at tworightsit
    with charachange

    ha "Хм… Какая глубокая мысль, Хисао."

    "Чёрт! Сам того не замечая, я думал вслух."

    hi "Спасибо. Я просто размышлял над тем, что сказала мне вчера Лилли."
    
    show hanako emb_blushtimid_sun at tworightsit
    with charachange

    ha "А? Лилли и с тобой разговаривала?"

    hi "Ага, она как раз рассказывала о том, что не всегда полезно слишком задумываться о чём-либо."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    #hanako ?

    ha "Странно… На днях она сказала мне примерно то же."

    hi "Хех, вот так совпадение."

    ha "Да уж… О…"
    
    show hanako emb_smile_sun at tworightsit
    with charachange
    #Hanako Happy
    ha "Сейчас начнётся!"
    #Had to change the above to a normal line because an extend was not working properly. -md01
    
    
    hi "А? Что?"

    "Ханако ничего не отвечает, а просто кивает в сторону долины."
    
    stop ambient fadeout 4.0

    hi "Что? Я ничего не вижу…"

    ha "Шшш…"

    "Мгновение кажется, будто ничего не изменилось."
    
    $ renpy.music.set_volume(0.15, 0.0, channel='ambient')
    
    play ambient sfx_cicadas fadein 3.0

    "Но потом я замечаю, как всё громче стрекочут цикады."

    "Слетаются стаи птиц, кружа над кронами деревьев…"
    
    scene bg school_picnic_ss at center
    show hanako emb_smile_sun_ss at tworightsit
    with dissolvecharamoveslow

    "А затем на долину падает и начинает ползти тень."

    hi "Закат…"

    ha "Верно. Отсюда можно наблюдать за тем, как ночь сменяет день."

    "Граница тени проходит по дну долины; тонкая линия между светом и тьмой."

    "По одну её сторону лес уже отходит ко сну, по другую – он всё ещё полон сил и энергии."

    hi "Круто…"

    ha "Правда?"

    hi "Но не пора ли нам выдвигаться обратно?"

    hi "Меня совершенно не прельщает перспектива возвращаться в темноте…"
    
    show hanako emb_downtimid_sun_ss at tworightsit
    with charachange

    #Hanako pouts

    ha "Хорошо…"
    
    show hanako emb_blushtimid_sun_ss at tworightsit
    with charachange

    ha "Я просто хотела показать тебе это."

    ha "Я больше никому этого не показывала."

    hi "Спасибо, Ханако. Не думаю, что кто-либо раньше делал для меня что-то подобное."
    
    show hanako emb_smile_sun_ss at tworightsit
    with charachange
    #hanako smiles

    ha "Всегда пожалуйста."

    hi "Пойдём?"

    ha "Ага."
    
    show bg school_picnic_ss at bgleft
    show hanako emb_smile_sun_ss at centersit
    with charamove
    
    show hanako emb_smile_sun_ss
    with charamove

    "В одну руку я беру корзину для пикника, а другую подаю Ханако."

    "Кажется, она не против, но её быстрый темп говорит о том, что ей приходится фактически тащить меня всю обратную дорогу."

    return

label ru_HT10:
    
    scene bg school_greendoor_ni at bgleft
    show hanako emb_smile_sun_ni
    with locationskip
    #bg green door.
    
    stop music fadeout 3.0

    "К тому времени, как мы возвращаемся к Зелёной двери, уже темно, хоть глаз выколи."

    "Дорога обратно заняла у нас гораздо больше времени, прежде всего благодаря опускающейся темноте."

    hi "Слушай, уже довольно поздно, так что столовая, наверное, уже закрыта."
    
    show hanako emb_downtimid_sun_ni
    with charachange

    ha "У меня… есть немного еды в комнате."
    
    show hanako emb_blushtimid_sun_ni
    with charachange
    #Hanako embarrassed

    ha "Н–н–не хочешь перекусить?"

    hi "Было бы здорово. Все мои припасы пошли нам на пикник."
    
    show hanako emb_smile_sun_ni
    with charachange
    #Hanako Releived
    
    stop ambient fadeout 2.0

    ha "Х… хорошо. Пойдём, я тоже проголодалась."
    
    scene bg school_dormhanako
    with shorttimeskip
    
    #"NOTICE" "This is the point at which the art/scene direction for Release #1 ends. You can either wait for the next Release, hopefully within 1/2 weeks, or you can read on (keeping in mind that there will be no art or sound beyond this point)."
    #bg dormhanako
    
    play music music_heart fadein 4.0

    "В комнате Ханако царит привычная спартанская обстановка."

    "На кровати лежат игрушечные кролик и мишка, которого я ей подарил."
    
    "Она подходит к столу и делает несколько сэндвичей."
    
    show hanako emb_timid_sun at tworight
    with charaenter

    ha "Прости, что так мало, но если мы появимся на кухне, нас могут заметить…"

    hi "Всё в порядке, я успел немного перехватить днём…"
    
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "Но это некрасиво с моей стороны: пригласить тебя, когда у меня для тебя ничего нет."

    hi "Не глупи, мы ведь ходим на свидания, так?"

    hi "Для нас ведь естественно гулять вместе, верно?"
    
    show hanako emb_smile_sun at tworight
    with charachange
    #Hanako embarrassed

    ha "Да… Думаю, да."

    "На то, чтобы расправиться с бутербродами, у нас уходит совсем немного времени, и после небольшой уборки комната Ханако возвращается к своему обычному скучному виду."

    "Стрелки часов говорят, что скоро девять."

    "Полагаю, в эти выходные мне стоит позаниматься."

    "Но сперва мне нужно постараться сделать ещё кое-то."

    hi "Послушай, я, пожалуй, пойду, но сначала…"

    show hanako emb_blushing_sun at tworight
    with charachange
    #hanako mega embarrassed

    ha "Д… да?"

    hi "Я подумал, что мы могли бы… ну… что мы делали вчера…"
    
    show hanako emb_blushtimid_sun at tworight
    with charachange

    ha "А?"

    "Теперь настала моя очередь смущаться."

    "Я ведь никогда раньше с девушками не встречался, поэтому не знаю, как поступать в такого рода ситуации."

    hi "Я подумал, что если ты не против, то я мог бы поцеловать тебя на ночь…"

    "Блин, это худший момент в моей жизни."

    ha "К… конечно."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    scene ev hanako_kiss
    with dissolve

    "Ханако закрывает глаза и тянется ко мне губами, прижав руки к груди."

    "Нервничая, я наклоняюсь к ней и осторожно целую."

    "Поцелуй занимает несколько больше времени, чем я рассчитывал, и, прежде чем я успеваю осознать это, Ханако уже обнимает меня."
    
    scene bg school_dormhanako
    show hanako emb_blushing_sun
    with dissolve

    "Переводя дыхание, мы отстраняемся друг от друга."

    "Однако Ханако выглядит несколько насторожённой."

    hi "Что-то случилось? Я был слишком настойчив?"
    
    show hanako emb_downtimid_sun
    with charachange

    ha "Нет… Не в этом дело."
    
    show hanako emb_blushtimid_sun
    with charachange

    ha "М… Хисао?"

    hi "Да?"
    
    stop music fadeout 6.0

    ha "Я… хочу тебе кое-что показать… Так что не уходи пока, ладно?"

    hi "Х… хорошо."
    
    show hanako emb_blushing_sun
    with charachange

    ha "Только… Присядь-ка сюда на минутку."
    
    play sound sfx_impact
    
    show hanako emb_blushing_sun at twocenteroff3
    show bg school_dormhanako at bgright
    with vpunch

    "Ханако подталкивает меня в сторону кровати так, что я чуть не заваливаюсь на спину."
    
    show hanako invis at twoleft
    with dissolvecharamove
    
    play sound sfx_lock
    
    with Pause(0.5)
    
    play sound sfx_switch
    scene bg school_dormhanako_ni at bgright
    hide hanako
    with locationchange    

    "Прежде чем я успеваю что-то сказать, она подходит к двери и запирает её, после чего выключает свет."

    hi "Э… Ханако? В чём дело?"

    ha "Шшш…"

    "Судя по голосу, она стоит в центре комнаты спиной ко мне."

    "Комнату освещает только сумрачный свет ночного неба, льющийся из окна."

    "Комнату наполняют причудливые тени, и я едва могу рассмотреть, что Ханако…"
    
    "Она…"

    return

label ru_HT10h:
    
    play music music_hanakohscene fadein 4.0
    
    play sound sfx_whiteout
    scene ev hanako_scars_dark
    with whiteout

    "Платье с её плеч соскальзывает на пол, издав приятный тихий шорох."

    hi "Х… Ханако?"

    ha "Шшш…"

    ha "Я… Я хочу, чтобы ты это увидел…"
    
    show ev hanako_scars
    with dissolvecharamoveslow

    "Мои глаза всё больше привыкают к темноте, и фигура Ханако видна всё чётче."

    "Я вижу, как она убирает волосы со спины и закидывает через плечо."

    ha "Это… это я. Такая вот я."
    
    show ev hanako_scars_large_move
    with locationchange

    "Я моргаю, и вдруг всё вокруг начинает словно проясняться."

    "Кожа на спине Ханако не такая гладкая, как у большинства людей."

    "Обожжённая кожа, натянутая словно барабан, тянется от шеи, по всей спине и дальше вниз по правой ноге."

    ha "Я… в огне… Свернулась…"

    ha "Я свернулась калачиком, так что моей спине досталось больше всего."

    ha "Так… Что ты думаешь?"

    "У меня нет слов, поэтому я просто встаю и кладу свои руки ей на спину."

    "Хоть она и выглядит как кожа, на ощупь она абсолютно гладкая."
    
    stop music fadeout 4.0

    "Я нежно глажу её ожог, а Ханако дрожит мелкой дрожью."

    "Я наклоняю голову к её шее; её запах наполняет мои ноздри, и по спине бегут мурашки."

    #"Almost unconsciously, I unclasp her bra and let it fall to the floor, where it lands atop the yellow dress."
    
    play music music_romance fadein 4.0

    hi "Ханако…"

    extend " Ты выглядишь великолепно!"

    "Я солгал бы, если б сказал что-то другое."

    "Как я и думал, фигура у Ханако практически идеальная."
    
    scene bg school_dormhanako_ni 
    show hanagown stockworry_blush_close_ni
    with locationchange

    "Мои руки достигают границы шрама, и пальцы скользят вверх по шее; Ханако инстинктивно поворачивается лицом ко мне."

    "Её глаза красные, но она не плачет."
    
    "Я чувствую, как Ханако расстёгивает пуговицы моей рубашки; ещё мгновение, и рубашка отправляется в растущую на глазах гору одежды."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    scene ev hanako_kiss_night
    with dissolve
    
    "Мы снова сливаемся в поцелуе, а моя рука пытается совладать со штанами."
    
    scene bg school_dormhanako_ni 
    show hanagown nudeworry_blush_close_ni
    with locationchange

    "Через несколько мгновений мы с Ханако стоим друг против друга в одном нижнем белье."
    
    show hanagown nudenormal_blush_close_ni
    with charachange

    "Я продолжаю смотреть на её ожоги."
    
    show hanagown nudeworry_blush_close_ni
    with charachange

    "Когда я касаюсь её груди, она издаёт глубокий вдох, и я решаю пойти обходным путём."
    
    #Got rid of this line because lol non-canon -md01
    #"Guided by instinct, we fall backwards onto the bed. I begin to massage her nipple, which hardens almost instantly under my touch."
    
    "Ведомый инстинктом, я мну её сосок, который мгновенно затвердевает под моими пальцами."
    
    show hanagown nude_moan_close_ni
    with charachange

    "Вздох Ханако переходит в нежный стон, который я прерываю поцелуем."
    
    show hanagown nude_moan2_close_ni
    with charachange

    "Я оставляю сосок и веду пальцами сверху вниз по линии шрама; на её коже выступают мурашки."

    "Боюсь, я сам пребываю в таком же состоянии; я не могу унять дрожь, а в голове вертятся тысячи мыслей."

    "Сейчас мои действия подчинены чувствам и животному инстинкту; ничто более не имеет значения, только стоящее передо мной обнажённое женское тело."
    
    show hanagown nudesmile_close_ni
    with charachange

    "Покуда моя рука опускается к её трусикам, она пятится назад и тянет меня следом."
    
    #lol non-canon -md01
    #"She sits on the bed, and tugs at my underwear with nervous hands."
    
    "Она садится на парту и пытается трясущимися руками стянуть с меня трусы."
    
    scene white
    with dissolve
    
    show ev hanako_kiss_night
    with dissolve

    "Мы снова сливаемся в спонтанном поцелуе, а я помогаю ей снять с меня последний элемент одежды."
    
#    scene evh hanako_missionary_underwear 
#    with whiteout

    play sound sfx_whiteout    
    
    scene white
    with dissolve

    show evh hanako_miss1
    with dissolve

    "И вот она сидит на столе, а я, голый, нависаю над ней."

    "Очевидно, что мы полностью готовы к тому, что сейчас произойдёт."

    ha "Ты… кажется, готов…"

    hi "Мы действительно собираемся это сделать?"

    "Сердце бьётся в груди как сумасшедшее. Я никогда не чувствовал ничего подобного, даже во время приступа."

    "Ханако резко и отрывисто дышит."

    "Она закидывает одну руку мне за шею, а другой нежно гладит мой член."

    "Гормоны бушуют, и требуется вся моя сила воли, чтобы сдерживать себя."

    "Слова застревают в горле, и я вынужден сглотнуть, прежде чем что-то произнести."

    hi "Готова?"
    
#    scene evh hanako_missionary_glance 
#    with charachange

    show evh hanako_miss2
    with dissolve

    "Ханако кротко кивает и закусывает нижнюю губу."
    
#    scene evh hanako_missionary_closed 
#    with charachange

    "Я наклоняюсь к ней и отвожу в сторону её промокшие трусики."

    "Она рукой обхватывает мой член, чтобы направить его, но даже так я соскальзываю и попадаю не с первого раза."
    
#    scene evh hanako_missionary_clench 
#    with charachange

    ha "Давай… Сделай это…"

    "Я начинаю медленно входить в неё; её ногти впиваются в мою спину."

    "Я чувствую некоторое сопротивление, но инстинкты заставляют меня двигаться дальше."
    
    show evh hanako_miss3
    with dissolve

    "Она резко вдыхает, когда наши бёдра соприкасаются."

    hi "С тобой всё в порядке?"
    
#    scene evh hanako_missionary_glance 
#    with charachange

    ha "Д… да… Просто… помедленнее…"
    
    "Меня переполняет нервное напряжение, когда я начинаю двигаться."
    
#    scene evh hanako_missionary_clench 
#    with charachange

    show evh hanako_miss4
    with dissolve

    "Она обхватывает меня руками, притягивая поближе к себе."

    "Её тепло окружает меня как внутри, так и снаружи."

    "Она двигает бёдрами в такт моим толчкам, и мы увеличиваем темп."
    
#    scene evh hanako_missionary_open
#    with charachange

    show evh hanako_miss5
    with dissolve

    ha "Б… быстрее… Пожалуйста… Быстрее…"

    "Пот бисером покрывает наши тела, и я чувствую, как хватка её рук на моей спине ослабевает."
    
#    scene evh hanako_missionary_closed 
#    with charachange

    show evh hanako_miss6
    with dissolve

    "Она тоже замечает это, обхватывает меня ногами так, что её лодыжки оказываются у меня на уровне поясницы, и подталкивает меня к себе."
    
    show evh hanako_miss7
    with dissolve

    "Спину пронзает резкая боль, когда её ногти впиваются в меня ещё с пущей силой, но это лишь разжигает во мне возбуждение."

    "Я прижимаюсь к Ханако, моя покрытая потом грудь скользит по её груди."
    
    show evh hanako_miss8
    with dissolve

    "Я тянусь к ней, чтобы поцеловать, но она откинула голову в экстазе, поэтому поцелуй приходится в её покрытую шрамом шею, и я снова чувствую солёный привкус."
    
#    scene evh hanako_missionary_clenchs 
#    with charachange

    ha "Не… не останавливайся…"

    hi "Я не могу… Я почти…"

    "Я чувствую нарастающую пульсацию в паху и пытаюсь выйти из Ханако, пока не стало слишком поздно."

    hi "Ханако… Я сейчас…"
    
#    scene evh hanako_missionary_closed 
#    with charachange

    ha "Не останавливайся!"
    
    show evh hanako_miss9
    with dissolve

    "Ханако не позволяет мне выйти из себя, удерживая меня ногами."

    hi "Я правда сейчас…"
    
#    scene evh hanako_missionary_open
#    with charachange

    ha "Кончай!"

    "Я крепко стискиваю зубы, но смесь удовольствия и боли берёт верх."

    "Меня ослепляют ощущения, которые я испытываю, входя в Ханако, и когда она двигается в такт моим движениям."

    "Она напрягает руки, и я чувствую, как её ногти пронзают мою кожу."
    
#    scene evh hanako_missionary_closed 
#    with charachange

    "Её ноги заставляют меня войти в неё полностью."

    "Она выгибает спину, её растрёпанные волосы отливают фиолетовым цветом."
    
#    scene evh hanako_missionary_ending
#    with charachange

    "Я больше не могу держаться и выплёскиваюсь глубоко внутри Ханако. В такт волнам оргазма, моё тело сотрясают судороги."
    
    #window hide

#    scene bg school_dormhanako_ni 
#    show white 
#    with Dissolve(3.0)

    #window show
    
    stop music fadeout 10.0

    "Тяжело дышащие, покрытые потом, крепко обняв друг друга, мы остаёмся в таком положении, пока медленно приходим в себя."
    
    show evh hanako_miss10
    with dissolve

    "Ханако медленно открывает глаза и смотрит на меня."

    "Это один из редких случаев, когда я вижу оба её глаза. И оба они, кажется, говорят одно и то же."
    
    show evh hanako_miss11
    with dissolve

    ha "Я люблю тебя, Хисао."

    hi "Я тоже тебя люблю, но…"

    "Не успеваю я закончить предложение, как Ханако целует меня, медленно и размеренно, а не страстно, как раньше."

    "Мне удаётся оторваться от неё на миг, чтобы успеть вставить слово."

    hi "Ханако… Я… в тебя…"

    return

label ru_HT10x:
    
    scene ev hanako_after_smile 
    with locationchange

    play music music_twinkle fadein 1.0

    "Мы медленно выпускаем друг друга из объятий."

    "Вся кровать мокрая от пота – доказательство только что произошедшего."

    "Ханако тянется к своим влажным, перекрученным трусикам."
    
    scene ev hanako_after_worry 
    with locationchange

    ha "Я знаю. Я не пошла бы на это, если бы не знала…"

    hi "Не знала о чём?"

    ha "О возможных последствиях."
    
    scene ev hanako_after_smile 
    with locationchange

    ha "Но я думаю, что всё будет в порядке."

    "Я не знаю, на чём основывается её предположение, но я слишком устал, чтобы беспокоиться об этом."
    
    stop music fadeout 8.0

    hi "Скажи, могу я…"
    
    window hide

    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.8)

    window show

    "Глаза заволакивает серая пелена, и я чувствую головокружение."
    
    scene ev hanako_after_worry 
    with locationchange
    
    $ i = renpy.random.randint(1,30)
    if i == 1:
      hi "Ё-моё…"
    elif i == 2:
      hi "Вот блин…"
    else:
      hi "Ох…"

    "Я сажусь на кровати и выставляю в сторону руку, чтобы не упасть."

    ha "Хисао? Что случилось?"

    $ i = renpy.random.randint(1,20)
    if i == 1:
      hi "Я… не знаю… Просто чего-то приуныл…"
    else:
      hi "Я… не знаю… Просто знобит немного…"
    
    $ i = renpy.random.randint(1,100)
    if i == 1:
      hi "Перетрах, да?"
    else:
      hi "Устал."
    
    scene ev hanako_after_smile 
    with locationchange
    
    with Pause(1.0)
    
    show black
    with shuteye

    "Я выдавливаю улыбку, и Ханако улыбается в ответ, после чего я отключаюсь."

    return
    
label ru_HT11:

    #HT11, wherein I please my back-washing desires.
    #I could not recommend getting yourself washed in this manner enough.
    #The title is from the Poltergeist CD (Ghost Hound OP)
    #Anyway, it'll probably be done with 2-3 CGs
    #Or we can cut it.
    scene black
    with dissolve
    
    show bg school_dormhanako_ss
    #show hanagown
    with openeye
    #Bg dormhana with eyes open and timeskip. Or skip to black then open later
    
    play music music_serene fadein 2.0

    "Просыпаюсь я от тёплого прикосновения к моему животу."

    hi "Ч… что случилось?"
    
    show hanagown worry_blush_close_ss
    with charaenter
    #show Hanako pyjamas neutral
    
    "Ханако, явно не ожидавшая, что я проснусь, быстро убирает руку."

    ha "Ой… Я просто проверяла…"

    ha "Медбрат сказал мне присматривать за тобой."

    hi "Медбрат?"

    "Перед глазами проносятся события прошедшей ночи."

    "Не знаю, о чём из произошедшего мне не было бы неловко рассказывать фельдшеру."
    
    show hanagown normal_close_ss
    with charachange

    ha "Ну, после того, как ты упал в обморок, я позвала Лилли."

    "И Лилли тоже? Сдаётся мне, что скоро мне придётся объясняться…"

    hi "Лилли… так… А потом?"

    ha "Она пришла, проверила твоё состояние и вызвала медбрата."
    
    show hanagown distant_close_ss
    with charachange

    ha "Он интересовался, чем мы занимались весь день, и попросил её измерить твой пульс."
    
    show hanagown normal_close_ss
    with charachange

    ha "Он сказал, что у тебя просто небольшое обезвоживание, но попросил нас за тобой приглядывать."

    "Сонливость понемногу рассеивается, и я начинаю замечать некоторые вещи."

    "Во-первых, по периметру шторы виднеется тусклый предрассветный свет."

    "Быстрый осмотр комнаты показывает, что наша одежда валяется ровно там, где мы её и оставили, – разбросана по полу."

    "Секундочку…"

    "Я откидываю простыни, являя свету своё обнажённое тело."

    hi "Ханако… Ты говоришь, Лилли была здесь?"
    
    #Hanako puzzled

    ha "Да."

    hi "Когда я был… голый?"
    
    show hanagown drunkworry_close_ss
    with charachange
    #hanako embarrassed

    ha "Я… я не думаю, что она это заметила."

    hi "Хех, думаю, что ты права. Но ты могла бы хотя бы штаны на меня надеть…"
    
    show hanagown distant_close_ss
    with charachange

    ha "Прости. Я немного запаниковала."
    
    show hanagown normal_close_ss
    with charachange

    "Я кладу руку Ханако на плечо."

    hi "Всё в порядке. Спасибо, что приглядывала за мной."
    
    show hanagown smile_close_ss
    with charachange
    #Hanako smile

    ha "Нет проблем. А, медбрат ещё хотел поскорее тебя увидеть; он сказал, что будет у себя в семь утра."

    "Часы в изголовье кровати Ханако говорят, что это примерно через полтора часа."

    hi "Отличная мысль. Я думаю, что в любом случае отправился бы к нему."
    
    show hanagown drunkpout_close_ss
    with charachange

    "Ханако протяжно зевает."

    hi "Устала?"
    
    show hanagown drunknormal_close_ss
    with charachange

    "Она сонно кивает."

    ha "Я всю ночь не спала и присматривала за тобой, как и просил медбрат."

    "Я понимаю, что Ханако сказала это без какого-либо подтекста, но я не могу отделаться от беспокойства, что кто-то приглядывал за мной, пока я спал."

    hi "Спасибо, Ханако. Ты просто замечательная девушка."
    
    show hanagown smile_close_ss
    with charachange
    #Hanako embarrassed

    ha "Ой, да ладно…"
    
    show hanagown smile_ss
    with charachange
    
    "Я встаю с кровати и начинаю одеваться."

    hi "Я хочу вернуться к себе и подготовиться к встрече с медбратом."

    hi "Тебе стоит хоть немного поспать."
    
    show hanagown normal_ss
    with charachange

    ha "Хорошо. Мы же потом увидимся?"

    hi "Конечно! Я зайду за тобой, когда закончу, ладно?"
    
    show hanagown smile_ss
    with charachange

    ha "Ага."
    
    hide hanagown
    with charaexit
    
    "Ханако укладывается поудобнее и накрывается простынёй."
    
    hi "Спокойной ночи."
    
    #show bg school_dormhanako at bgleft
    #show hanagown smile_close
    #with dissolvecharamove
    
    #show bg school_dormhanako
    #show hanagown smile at tworightsit
    #with dissolvecharamove

    "Я наклоняюсь к ней и целую."

    ha "Спасибо."

    "Я беру корзину для пикников, выхожу в коридор и закрываю за собой дверь настолько тихо, насколько могу."
    
    scene bg school_dormhisao
    with shorttimeskip
    
    stop music fadeout 3.0

    #BG bathroom

    "Так как время ещё есть, я решаю привести себя в порядок перед встречей с медбратом."
    
    scene bg school_dormbathroom
    with locationchange

    "Я складываю грязную одежду в корзину для белья, вхожу в душевую и открываю горячую воду."

    "Не желая беспокоить %(name_kenji)s, вместо принятия душа я решаю просто помыться в тазике."

    "Давненько я так не мылся."

    "После чего достаю небольшой табурет из шкафа; теперь я полностью готов."
    
    play ambient sfx_shower fadein 1.0
    
    show steam 
    show steam2
    with dissolve

    "Есть что-то расслабляющее в такого рода водных процедурах, что придаёт новые силы."

    "Когда я мою ноги, слышу звук открывающегося дверного замка."

    hi "А, %(name_kenji)s, это я. Мне ещё немного осталось."

    ha "Я… Я не %(name_kenji)s…"
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    play music music_heart fadein 3.0

    "В дверном проёме стоит Ханако, обнажённая и с полотенцем в руках."

    hi "Ханако? Что ты тут делаешь?"

    #Hanako embarrassed/CG

    ha "Я… не смогла заснуть."

    ha "Так что я решила вместе с тобой сходить к медбрату, но ты оказался здесь."

    ha "Мы… можем ведь пойти вместе?"

    hi "Ну… да. Полагаю."

    "Ханако улыбается, вешает полотенце и опускается позади меня на колени."

    #CG switch, Hanako kneeling behind Hisao. Perhaps a chain for different expressions?
    #Also lol where the hell is weee?

    ha "Я думаю, мне стоит пойти первой…"

    "Ханако наклоняется, прижимаясь к моей спине."

    "Она протягивает руку и берёт мою мочалку, мочит её в раковине и начинает тереть мне спину."

    ha "Как тебе?"

    "Я спокоен, я совершенно спокоен… Это так важно в подобных ситуациях…"

    hi "Оху… рошо."

    ha "Охурошо?"

    hi "Я хотел сказать «хорошо»…"

    "Если отбросить смущение, это довольно приятно."

    "Примерно как когда кто-то начинает чесать спину, только когда вы оба нагишом."

    "Впрочем, это не лучшее сравнение."

    "Ханако снова наклоняется, чтобы намочить мочалку, но на сей раз она так и остаётся прижатой к моей спине."

    "Она обхватывает меня руками и начинает мыть мне грудь, потом живот… и…"

    #Chain CG (maybe) Of Hanako now pressed into Hisao

    hi "Х… Ханако!"

    ha "А? Разве не нужно помыть и там?"

    hi "Не в… этом дело. Просто я…"

    "Ханако уже вовсю трёт там мочалкой, и я чувствую, как моё естество отзывается на её прикосновения."

    hi "Япростонехочусноваотрубиться."

    "Ханако останавливается и убирает мочалку."

    ha "Ты… ты прав. Тебе стоит показаться медбрату, прежде чем мы… будем заниматься такими вещами."

    "Я хватаю тазик с водой и опрокидываю его на нас."

    # Chain CG, Hanako wet

    ha "Эй!"

    hi "Хех, хотя мы ещё можем немного пошалить. Вот, теперь твоя очередь."

    "Я поворачиваюсь на табурете, отбираю мочалку у Ханако и начинаю тереть её плечи."

    hi "Так, теперь моя очередь."

    "Мы меняемся местами. Теперь на стуле сидит Ханако, а я тру ей спину."

    # Chain CG (if you want) Hanako on the bath stool

    "Несмотря на то что она сидит ко мне спиной, руки так и тянуться вперёд, чтобы дотянуться до её груди."

    ha "Мне показалось, или ты сказал, что нам не стоит…"

    hi "Я сказал, что мне не стоит…"

    "Подражая тому, как она делала это ранее, мои руки скользят вниз, между её бёдер."

    ha "Хи… Хисао…"

    "Она сводит их вместе, вынуждая мою покрытую пеной руку довольствоваться её ногами."

    "Ханако вскрикивает от удивления и удовольствия, и я мгновенно вспоминаю, где мы находимся."

    "Если бы %(name_kenji)s узнал про всё это, он бы мне мозг выел нотациями."

    hi "Думаю, ты права. И мне стоит отправиться к медбрату как можно скорее."

    ha "Д… да."

    "Я наклоняюсь над Ханако, включаю душ и начинаю смывать с нас мыло."
    
    stop ambient fadeout 2.0

    "Поигрались и хватит. Мы быстро вытираемся и одеваемся."
    
    scene bg school_dormhisao
    show hanako emb_timid_cas
    with locationskip
    #BG dormhisao
    #show Hanako casual embarrassed

    #"Hanako wears a new outfit that I haven't seen before. With hat and all, it's definitely a more concealing get-up than yesterday's attire."
    
    "Ханако одета так же, как и несколько дней назад: на ней шляпа и так далее."

    ha "Я спешила, а оно попалось под руку, так что…"

    hi "Не переживай, мне нравится."

    hi "Тебе идёт…"
    
    show hanako basic_smile_cas
    with charachange
    #Hanako casual smile
    
    stop music fadeout 4.0

    ha "С… спасибо."

    "Я приобнимаю Ханако за талию, и мы направляемся в медицинский кабинет."
    
    scene bg school_nurseoffice
    show nurse neutral
    with shorttimeskip
    #BG nurse office w/fade
    
    play music music_nurse fadein 2.0

    "Медбрат убирает стетоскоп от моей груди, и я застёгиваю рубашку."

    nk "Итак, расскажи-ка, что вчера произошло."

    hi "Ну, мы просто немного погуляли по лесу, а потом, когда вернулись обратно, я почувствовал усталость; больше я ничего не помню."
    
    show nurse concern
    with charachange

    "Медбрат смотрит на меня с подозрением."

    nk "Что, на этой… прогулке… ты не перенапрягался?"

    hi "Хм… Да нет."

    nk "А что ты вчера ел?"

    hi "Я немного перехватывал в обед и на ужин, но вот завтрак я пропустил."

    nk "А что насчёт питья?"

    hi "Если честно, я не могу вспомнить, много ли я пил."

    "Медбрат постукивает ручкой по планшету, ни на секунду не сводя с меня глаз."

    "После короткой паузы он протягивает мне маленький контейнер."

    nk "За этой дверью – туалет. Я хочу, чтобы ты наполнил её."

    hi "Ладно…"
    
    show nurse neutral
    with charachange

    nk "Среднюю порцию, пожалуйста."
    
    show bg school_nurseoffice
    show nurse neutral
    with shorttimeskip

    "Есть что-то неестественное в анализах мочи."

    "Давать тёплую ёмкость того, что обычно смывается в унитаз, это… неправильно."

    "Но медбрат берёт контейнер так, будто в нём обычная вода, и опускает в него несколько полосок бумаги."

    "Он размешивает ими жёлтую жидкость, стряхивает излишки и пристально на них смотрит."
    
    show nurse concern
    with charachange

    nk "Хм, как я и думал."
    
    show nurse neutral
    with charachange

    nk "Уровень сахара в крови очень низкий; похоже, у тебя было обезвоживание."
    
    show nurse grin
    with charachange

    nk "Тебе стоит заботиться о своём организме, особенно если планируешь и впредь практиковать «прогулки по лесу»…"
    
    show nurse fabulous
    with charachange
    #nurse smile

    nk "Ты понимаешь, на что я намекаю?"

    "Сдаётся мне, что скрыть от него что-то просто невозможно."

    hi "Конечно."
    
    show nurse neutral
    with charachange

    nk "А теперь иди и плотно позавтракай, а ещё тебе нужно за сегодня выпить несколько литров воды."

    nk "Но не всё сразу, разумеется. Просто несколько бутылок в течение дня."

    hi "Ясно."
    
    show nurse concern
    with charachange

    nk "А, и ещё кое-что…"

    hi "Хм?"
    
    show nurse neutral
    with charachange

    nk "Я знаю, что ты уже знаешь об этом… но не делай ничего такого, о чём потом придётся сожалеть."

    nk "Я про эти ваши «прогулки»."

    hi "М, хорошо. Я буду аккуратен."
    
    stop music fadeout 3.0

    nk "Да уж, постарайся. Увидимся."
    
    scene bg school_nursehall
    show hanako basic_worry_cas
    with locationchange
    #BG corridor.
    #show Hanako casual concerned/neutral

    "За дверью меня терпеливо ждёт Ханако."

    ha "И? Что случилось?"

    hi "А, да ничего. К счастью, ничего связанного с сердцем."
    
    show hanako basic_bashful_cas
    with charachange
    #Hanako Smiles

    ha "Это отличная новость!"

    ha "Итак, чем займёмся?"

    hi "Ну, мне только что было приказано плотно позавтракать… Составишь компанию?"
    
    show hanako basic_normal_cas
    with charachange

    ha "Звучит здорово, но я не уверена, что столовая уже открыта…"

    hi "На самом деле я думаю, что мы могли бы прогуляться в «Шанхай». Что ты на это скажешь?"

    ha "Хо… хорошо. Пойдём."

    return

label ru_HT12:

    #This is the first of the scenes written since the changes to the Hanako paths.
    #I'll finish the HT path as per the new plan, then rewrite.
    #I just hate leaving things unfinished.
    #also, not entirely sure on Hanakos reaction at the end.
    
    scene bg suburb_shanghaiint 
    show hanako emb_emb_cas
    with locationskip

    play music music_dreamy fadein 2.0
    #bg shanghai with dissolve

    "Как и ожидалось, в «Шанхае» хоть шаром покати."
    
    "Упавшая духом Юко сидит в глубине кафе, её глаза все красные."
    
    show bg suburb_shanghaiint at bgright
    show hanako emb_emb_cas at tworight
    with charamove
    
    hi "Должно быть, у тебя была трудная ночь."
    
    show yuukoshang panic_up at twoleft
    with charaenter
    
    yu "Да нет, просто я поздно легла."
    
    show yuukoshang worried_down at twoleft
    with charachange

    yu "Я тусовалась… м… с другом."

    "Эта её пауза говорит лучше всяких слов, но в интересах её спокойствия я не развиваю эту тему."

    hi "Ну и славно. Надеюсь, ты хорошо провела время."
    
    show yuukoshang happy_up at twoleft
    with charachange

    yu "О, да… В этом я могу вас заверить…"
    
    show yuukoshang panic_down at twoleft
    with charachange

    "Юко обильно краснеет, словно осознав, что она только что сказала."

    "Надо бы сменить тему, да как можно скорее…"

    hi "Ты как, готова принести нам завтрак?"
    
    show yuukoshang worried_up at twoleft
    with charachange

    yu "Конечно. У нас в меню традиционные завтраки и завтраки в западном стиле."

    hi "Тогда мне, пожалуйста, большой европейский завтрак."
    
    show hanako basic_smile_cas at tworight
    with charachange

    ha "И мне тоже, пожалуйста."
    
    show yuukoshang neutral_up at twoleft
    with charachange

    yu "Итак, два завтрака…"
    
    hide yuukoshang
    with charaexit
    
    show bg suburb_shanghaiint at bgleft
    show hanako basic_smile_cas at center
    with charamove
    
    show hanako basic_smile_cas at centersit
    with charamove

    "Юко исчезает в задней части кафе, а мы с Ханако занимаем свои места."

    hi "Как ты себя чувствуешь? Устала?"
    
    show hanako emb_timid_cas at centersit
    with charachange

    ha "Немножко."
    
    show hanako emb_smile_cas at centersit
    with charachange
    #Hanako smile

    ha "Но главное, что с тобой всё в порядке."

    hi "Да уж, я тоже. Я немного побаивался, что медбрат запретит мне… это… ну, ты понимаешь…"
    
    show hanako emb_downtimid_cas at centersit
    with charachange
    #Hanako Embarrassed looking down

    ha "А… ага."

    "Ханако отводит взгляд в сторону; всё же мы ещё не готовы говорить об этом на публике."
    
    show yuukoshang invis at left
    with None

    "Хотя и я чувствую, как румянец заливает моё лицо при воспоминании о событиях вчерашнего вечера."
    
    show bg suburb_shanghaiint at center
    show yuukoshang worried_up at Motion(trembleleft,8.0,repeat=True)
    show hanako emb_timid_cas at tworightsit
    with dissolvecharamove

    "Но наше неловкое молчание продолжается недолго, так как появляется Юко, несущая два заполненных едой подноса."

    "Я готовлюсь уворачиваться, так как подносы в руках Юко пляшут и дрожат так, будто ещё чуть-чуть и она их уронит."

    hi "Может, тебе помочь?"

    yu "Н–нет, я в порядке, я просто—{w=.3}{nw}"
    
    play sound sfx_impact2
    
    show yuukoshang worried_down at twoleftsit
    show hanako defarms_shock_cas at tworightsit
    with vpunch
    
    with Pause(0.2)
    
    show yuukoshang neurotic_up at twoleft
    with dissolvecharamove

    "Она так опускает подносы на стол, что мне на секунду кажется, будто сейчас они расколются, прям вместе со столом."
    
    show hanako def_worry_cas at tworightsit
    with charachange

    "Как ни странно, всё на местах, разве что немного перемешалось."
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "Вот и мы, как заказано."

    hi "Спасибо."
    
    show yuukoshang worried_up at twoleft
    with charachange

    yu "Скажите, а Лилли сегодня не с вами?"

    hi "Мы решили дать ей выходной. Она всегда так о нас заботится, что справедливо дать ей от нас отдохнуть."
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    ha "Порой… люди хотят побыть в одиночестве…"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "Звучит довольно разумно."

    yu "Но это же не оправдание вашего желания побыть наедине, да?"
    
    show hanako cover_worry_cas at tworightsit
    with charachange
    #Hanako embarrassed

    $doublespeak (ha, hi, u"Н-ну, может…", u"Мде, вполне возможно…")
    
    show yuukoshang happy_down at twoleft
    with charachange
    #Yuuko Happy

    yu "О-хо! Это значит, что вы двое…"

    hi "Полагаю, можно и так сказать."
    
    show yuukoshang closedhappy_up at twoleft
    with charachange

    yu "Ха! Я знала!"
    
    show yuukoshang happy_up at twoleft
    with charachange

    yu "Не волнуйтесь, я умею хранить секреты."
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    "В памяти всплывает последний раз, когда Юко обещала что-то держать в секрете."

    "Сдаётся мне, что это не лучшая идея."

    hi "В этом нет нужды, это не такой уж и секрет."
    
    show yuukoshang worried_down at twoleft
    with charachange
    #Yuuko saddened

    yu "А, хорошо. Но я всё же не сплетница."

    "Это как-то не согласуется с реальностью, но не буду акцентировать на этом внимание."

    hi "Как ещё у тебя дела, Юко?"
    
    show yuukoshang happy_up at twoleft
    with charachange
    #Yuuko happy

    yu "Нормально. Я снова нашла своего парня!"

    hi "Нашла? Снова?"
    
    show yuukoshang neutral_up at twoleft
    with charachange

    yu "Да! Я снова его нашла."

    yu "Я думала, что он переехал или типа того, а он просто стал отшельником."

    hi "Это намного лучше?"
    
    show yuukoshang closedhappy_up at twoleft
    with charachange

    yu "Он не мёртв!"

    hi "Это такой дополнительный бонус, надо понимать."
    
    show hanako basic_normal_cas at tworightsit
    with charachange

    ha "И где ты его нашла?"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "На днях я собиралась навестить Лилли после уроков, и там-то я с ним и столкнулась."
    
    hi "Что, интересно, он делал в школе?"
    
    show yuukoshang happy_up at twoleft
    with charachange

    yu "А, он же тут учится!"
    
    show hanako def_worry_cas at tworightsit
    with charachange

    ha "Не помню, чтобы ты навещала Лилли…"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "Я немного увлеклась тогда, у %(name_kenji)s оказалось столько всего интересного…"

    hi "%(name_kenji)s?"

    hi "Речь о воинственном антифеминистском жилье отшельника слепого-как-летучая-мышь %(name_kenji)s?"
    
    show yuukoshang happy_down at twoleft
    with charachange

    yu "А, так вы знакомы!"

    "Я незаметно щипаю себя, надеясь, что боль поможет мне вернуться в реальность."
    
    show yuukoshang neutral_down at twoleft
    with charachange

    hi "То есть ты утверждаешь, что твой приятель – мой сосед по общежитию, парень в очках такой толщины, что они весят, наверное, тонну?"
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    ha "И который немного не в себе…"

    hi "И ты бывала у меня в комнате, которая находится рядом с его, и даже ничего не заметила?"
    
    show yuukoshang worried_down at twoleft
    with charachange

    yu "Ну, я просто особо не приглядывалась…"

    hi "Ерунда какая-то."
    
    show yuukoshang panic_up at twoleft
    with charachange
    #Yuuko confused

    yu "А почему бы и нет?"

    hi "Потому что этого не может быть, вот почему."

    hi "Потому что этот парень крайне редко покидает свою комнату, даже на уроки ходит… постойте-ка…"

    hi "Я тут недавно стучался в его дверь…"
    
    show yuukoshang worried_up at twoleft
    with charachange

    yu "А, так это был ты? Он сказал, что это приставучий задрот, который уйдёт, если сохранять тишину…"

    hi "Бред какой-то."

    "Мой мозг не хочет в это верить."

    "Я помню, что и Юко, и %(name_kenji)s упоминали, что расстались со своими партнёрами, но это всё равно какая-то ерунда."

    "И, наоборот, их одиночество вполне объяснимо."

    "Моя хрупкая психика отказывается воспринимать это, так что я начинаю сосредоточенно уплетать свой завтрак."
    
    show hanako basic_normal_cas at tworightsit
    with charachange

    ha "А как вы сейчас встретились?"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "Ну, он время от времени приходил сюда, и при этом всегда был один, так что я начала разговаривать с ним."

    yu "Потом мы всю ночь тусовались и пили, и вот…"
    
    show yuukoshang smile_up at twoleft
    with charachange

    yu "Просто он с такой страстью рассказывал обо всём, что его увлекало, что я не могла оставить его одного…"

    yu "Ты же знаешь, женщин часто привлекают увлечённые мужчины."

    hi "Настолько увлечённые, что он пропал, даже не сообщив тебе куда?"
    
    show yuukoshang worried_down at twoleft
    with charachange

    yu "Что я могу сказать?.. Иногда людям становится тесно…"

    "Что-то говорит мне, что Юко и %(name_kenji)s, несмотря ни на что… просто созданы друг для друга."

    "Но явно не созданы для меня."

    "От самого этого чудовищного открытия у меня начала болеть голова, поэтому, когда мы заканчиваем свой завтрак, у нас нет причин здесь задерживаться."

    hi "Ну, я бы рад посидеть тут и поболтать, но у нас свидание."
    
    show hanako emb_timid_cas at tworightsit
    with charachange
    #Hanako confused

    ha "Да?"
    
    show yuukoshang smile_down at twoleft
    with charachange

    yu "О, это так мило! Всё, больше вас не задерживаю."

    hi "Спасибо. Вот, сдачи не надо."
    
    show bg suburb_shanghaiint at bgleft
    show yuukoshang invis at left
    show hanako emb_timid_cas at center
    with dissolvecharamove

    "Я беру Ханако за руку, и мы уходим ещё до того, как Юко успевает сказать нам что-нибудь странное на прощание."
    
    play sound sfx_storebell
    
    scene bg suburb_shanghaiext
    show hanako basic_normal_cas
    with locationchange
    #bg street

    hi "Итак, куда теперь?"
    
    show hanako cover_worry_cas
    with charachange

    ha "Я не знаю. Если честно, я немного устала."

    "Я её понимаю; обильный завтрак в животе и волнения последних суток заставляют и меня испытывать усталость."

    "Я могу только представить, что бы со мной было, если бы я не спал всю ночь."
    
    stop music fadeout 5.0

    hi "Как насчёт того, чтобы просто немного посидеть? Здесь парк недалеко."
    
    show hanako basic_bashful_cas
    with charachange

    ha "Звучит здорово."

    scene bg suburb_park
    #show hanako basic_normal_cas
    with locationskip
    #bg picnic park
    
    play ambient sfx_park fadein 3.0
    
    "Небольшой парк раскинулся буквально в паре минут ходьбы от «Шанхая»."

    "Так как ещё слишком рано, единственные посетители парка – редкие бегуны."

    "Я бы не удивился, если бы увидел тут Эми на своих спортивных протезах; сдаётся мне, она относится к тому типу людей, которые готовы променять сладкий утренний сон на пробежку."

    scene bg suburb_park at bgleft
    with charamove
    
    show hanako emb_emb_cas at tworightsit
    with charaenter
    
    "Мы находим небольшую скамеечку под деревом и присаживаемся на неё."

    "Прохлада тени освежает; здесь особенно ощущается, что лето не за горами."
    
    show hanako emb_downsmile_cas_close at tworightsit
    with charachange

    "Я приобнимаю Ханако, и она кладёт голову мне на плечо."
    
    show hanako emb_timid_cas_close at tworightsit
    with charachange

    ha "Я рада, что ты не умер."

    hi "Ты даже не представляешь, как я этому рад."
    
    show hanako emb_emb_cas_close at tworightsit
    with charachange

    "Ханако негромко смеётся, но в её смехе ощущается нервозность."
    
    show hanako emb_blushtimid_cas_close at tworightsit
    with charachange

    ha "Я… немного не это имела в виду."
    
    show hanako emb_downsad_cas_close at tworightsit
    with charachange

    ha "Этой ночью… Я думала, что это моя вина."

    ha "Будто всё произошло из-за того, что я…"

    hi "Ты имеешь в виду то, что между нами было? Полагаю, это результат… совместных усилий."
    
    show hanako emb_smile_cas_close at tworightsit
    with charachange
    #Hanako embarrassed.

    ha "Это… было здорово."

    hi "Я… не сделал тебе больно?"
    
    show hanako emb_timid_cas_close at tworightsit
    with charachange

    ha "Самую малость, в самом начале."

    hi "Прости."
    
    show hanako emb_smile_cas_close at tworightsit
    with charachange

    ha "Всё в порядке. Не думаю, что так будет каждый раз."

    hi "Наверное, ты права."
    
    show hanako emb_sleep_cas_close at tworightsit
    with charachange
    
    "…"

    hi "Ханако?"

    "Но Ханако не отвечает, она крепко спит на моём плече."

    "Она заслужила этот отдых, поэтому я не прочь поработать подушкой."

    "Кроме того, существует много более бессмысленных способов потратить воскресенье, нежели провести его рядом со спящей на твоём плече девушкой."
    
    scene bg suburb_park
    show hanako emb_sleep_cas_close at rightsit
    with shorttimeskip
    #timeskip?
    
    play music music_daily fadein 5.0
    
    show hanako emb_downtimid_cas_close at rightsit
    with charachange

    "Утро медленно уступает место полуденному солнцу, когда Ханако начинает ворочаться и, издав негромкий стон, открывает глаза."
    
    show bg suburb_park at bgleft
    show hanako emb_downtimid_cas_close at tworightsit
    with charamove

    hi "Утречка, соня."
    
    show hanako emb_timid_cas_close at tworightsit
    with charachange

    ha "А? Где это я?.."

    hi "В парке. Ты заснула после завтрака."
    
    show hanako cover_worry_cas_close at tworightsit
    with charachange
    #hanako embarrassed

    ha "Ох… Прости…"

    hi "Не стоит; ты присматривала за мной всю прошлую ночь, так что тебе надо было отдохнуть."

    ha "Но всё равно это как-то… невежливо."

    hi "Не переживай. Ну как, зайдём на обратной дороге в магазин, купим чего-нибудь перекусить?"
    
    show hanako basic_bashful_cas_close at tworightsit
    with charachange
    
    stop ambient fadeout 1.0

    ha "Х-хорошо."
    
    scene bg suburb_konbiniint
    show hanako emb_emb_cas
    with locationskip
    #bg Auramart
    
    $ renpy.music.set_volume(0.33, 0.0, channel='ambient')
    
    play ambient sfx_crowd_indoors fadein 0.5

    "В магазине на удивление многолюдно."

    "Мы с Ханако ходим по узким проходам между стеллажами, хаотично набирая попадающиеся под руки закуски."
    
    show bg suburb_konbiniint at bgright
    show hanako emb_emb_cas at tworight
    with charamove

    "Когда мы проходим мимо секции туалетных принадлежностей, я что-то замечаю краем глаза; что-то, заставляющее моё сердце ускорить свой бег."

    hi "Хм, Ханако?"
    
    show hanako basic_normal_cas at tworight
    with charachange

    ha "М-м-м?"

    hi "Послушай, я забыл взять… э… шоколадное молоко. Не могла бы ты сходить за ним?"
    
    show hanako def_worry_cas at tworight
    with charachange
    #hanako puzzled

    ha "К-конечно."
    
    show hanako invis at right
    with dissolvecharamove

    "Ханако с озадаченным видом разворачивается и уходит."

    "Тем временем я переключаю всё своё внимание на туалетные принадлежности, в частности на одну из полок."

    "Я надеялся, что выбрать будет несложно и это займёт немного времени, но вместо этого у меня аж глаза разбегаются."

    "Тонкие, толстые, с разными вкусами, светящиеся в темноте, ребристые, текстурированные, с вибрацией, ассорти…"

    "Маленькие ярко окрашенные упаковки заполняют всё пространство между зубной пастой и дезодорантами."

    "Я совершенно потерялся в этом новом и неизведанном мире, как вдруг…"
    
    show hanako emb_timid_cas at tworight
    with dissolvecharamove
    #Hanako appears
    
    stop music fadeout 4.0

    ha "Ах вот ты где, Хисао, я принесла…"
    
    extend " на что это ты смотришь?"
    
    show bg suburb_konbiniint
    show hanako emb_timid_cas
    with ease

    hi "А? М… Э… не на что…"
    
    show hanako defarms_shock_cas
    with charachange

    ha "Презервативы?"
    
    stop ambient fadeout 0.5

    "И в этот момент глаза всех присутствующих обращаются на нас."

    "Я чувствую, как у меня на лбу выступает испарина."

    hi "Ну, я подумал, что…"
    
    show hanako emb_timid_cas
    with charachange

    ha "Я… Я считаю, что это хорошая идея."
    
    show bg suburb_konbiniint at bgright
    show hanako emb_timid_cas at twoleft
    with charamove

    "Ханако протягивает руку, берёт упаковку с надписью «Ассорти» и кладёт её в нашу корзину."

    "Удивительно, но она кажется гораздо менее смущённой, чем я."

    hi "Тебя разве это не беспокоит? Все эти люди смотрят на нас!"
    
    show hanako def_worry_cas at twoleft
    with charachange

    ha "А? Кто?"

    "Ханако поднимает глаза и наконец замечает направленные на нас взгляды."
    
    show hanako defarms_shock_cas at twoleft
    with charachange
    #hanako deep embarrassed

    ha "Я… ну… Мненужноидти."
    
    show bg suburb_konbiniint
    show hanako defarms_shock_cas
    with ease

    "Ханако заливается краской, хватает меня за рукав и мчится к кассе."

    "Кассир быстро пробивает товары и складывает их в пакет. После чего, хихикая, достаёт из нашей корзины небольшую коробочку."

    "Ни я, ни Ханако не можем посмотреть ему в лицо. И, как только расплачиваемся, мы максимально быстро направляемся к выходу."
    
    scene bg suburb_konbiniext
    show hanako emb_downtimid_cas
    with locationchange
    #bg street

    #hanako embarrassed looking down
    
    play music music_another fadein 3.0

    "Когда мы оказываемся снаружи, я могу поклясться, что слышу в магазине за спиной громкий смех."

    ha "Почему ты не сказал мне, что они смотрят?"

    hi "Ну, они не смотрели, пока ты не сказала… это."
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "Презервативы?"

    hi "Да."
    
    show hanako emb_blushing_cas
    with charachange
    
    ha "Но что в этом странного?"

    hi "Ничего… я думаю. Но это не повод кричать на весь магазин…"
    
    show hanako emb_downtimid_cas
    with charachange
    #hanako deep embarrassed

    ha "П… прости."

    "Я глажу Ханако по голове."

    hi "Не волнуйся, всё уже позади. И мы всё же их заполучили…"
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "Точно… Не стоит забывать о безопасности."

    hi "Ага."

    "…"

    hi "Может, нам уже…"
    
    show hanako emb_blushing_cas
    with charachange
    
    stop music fadeout 3.0

    ha "Да, пойдём обратно."
    
    hide hanako
    with charaexit

    "И мы с Ханако нервным быстрым шагом направляемся обратно в интернат."

    "Мы уходим, так ни разу и не оглянувшись на этот злосчастный магазинчик."

    return

label ru_HT13:
    
    scene bg suburb_konbiniext
    with locationchange

    scene bg school_dormhanako
    with shorttimeskip
    #bg hanadorm
    
    play music music_one fadein 2.0

    "Ноги сами несут нас прямиком в комнату Ханако."
    
    play sound sfx_lock
    
    show hanako basic_bashful_cas
    with charaenter
    #Hanako bashful ?

    "Она запирает за нами дверь, не сводя с меня пристального взгляда."

    ha "Я… я думаю, ты хочешь ополоснуться после такого напряжённого дня?"

    hi "А? Но я… эх."

    hi "Ты права. Надо помыться."
    
    show hanako basic_bashful_cas:
        xalign 0.5 alpha 1.0
        linear 1.0 xpos 0.0 alpha 0.0

    "Я кладу сумку с покупками и расстёгиваю рубашку, пока Ханако возится со своей блузкой."
    
    play sound sfx_switch
    
    scene bg school_dormhanako_nl     
    
    "Она выключает свет, когда её одежда в который раз за последнее время падает на пол."
    
    show hanagown nudenormal_blush_close_nl
    with charaenter

    "Я перешагиваю быстро растущую гору одежды, чтобы прижать к себе Ханако; её кожа такая тёплая и нежная."

    ha "Разве нам не стоит сперва сходить в ду…"
    
    scene ev hanako_kiss_day
    with dissolve

    "Я прерываю её долгим пламенным поцелуем."

    "Мгновение она сопротивляется, но потом впивается в мои губы с неменьшей свирепостью."
    
    scene bg school_dormhanako_nl
    show hanagown nudesmile_close_nl
    with locationchange

    "Когда мы отстраняемся друг от друга, она прикусывает мою нижнюю губу и, прежде чем отпустить, слегка оттягивает её."

    "Я, пританцовывая, освобождаюсь от штанов."

    "Потому что ещё немного, и либо мои штаны порвутся, либо мой член сломается, не найдя выхода на свободу."
    
    show hanagown nudeworry_blush_close_nl
    with charachange

    "Ханако шарит вокруг в поисках той небольшой коробочки, которая вызвала чуть ранее такой переполох."

    "По комнате разлетаются пакеты с закусками, пока она наконец не находит искомое."
    
    show hanagown nudenormal_blush_close_nl
    with charachange

    ha "Так, э… как мы?.."

    hi "Я думаю, в этом нет ничего сложного… нужно просто надеть… его… на него."

    hi "Наверное…"
    
    show hanagown nudeworry_blush_close_nl
    with charachange

    "Ханако трясущимися руками открывает коробку, рассыпая по комнате блестящие пакетики."

    ha "Упс…"

    hi "Спокойнее…"

    "Мой дрожащий голос не обладает тем успокаивающим эффектом, на который я так надеялся."

    return

label ru_HT13h:

    hide hanagown
    with charaexit

    "Я собрался было помочь Ханако с её поисками, но лицезрение её извивающегося на полу обнажённого тела оказывается куда более увлекательным занятием."

    #Perhaps a cg?

    "Сегодня освещение лучше, чем было вчера, и я могу чётко видеть различия между её родной и имплантированной кожей."

    "Как она и сказала, большая часть шрамов сосредоточена у неё на спине, и только в верхней части правого бедра есть ещё немного рубцов."

    "Её левая нога невероятно бледная и гладкая."

    "Благодаря постоянному ношению одежды, скрывающей её шрамы, её кожа была защищена от разрушительного влияния солнца."

    #Damn, even I do not know what the fuck I am talking about anymore.

    scene white
    with dissolve
    
    show evh hanako_finger_close #:
        #xalign 0.5 yalign 0.5 zoom 0.4 # my my, instead of resizing cg you used ingame zooming?.. [str]
    with dissolve

    "Я не могу больше на это смотреть, так что опускаюсь на колени и разворачиваю Ханако на спину, лицом ко мне."

    "Она тяжело дышит, но я набрасываюсь на неё как дикое животное."

    "Я целую её в шею, пока одна рука нащупывает бёдра, которые только что так меня очаровали."
    
    show evh hanako_finger_1:
        xalign 0.5 yalign 0.5 zoom 1.0
    with dissolve
    
    "Она рефлекторно сводит ноги вместе, но сразу немного расслабляет, и мои пальцы скользят всё глубже и глубже в её пучок волос на лобке."
    
    show evh hanako_finger_2
    with dissolve

    "Я чувствую на них тёплую влагу и продвигаюсь дальше."

    "Она постанывает, покуда мои пальцы ласкают её изнутри."
    
    show evh hanako_finger_3
    with dissolve

    ha "Х–Х–Хи-и-и-исао."
    
    show evh hanako_finger_close_scroll:
        xalign 0.5 yalign 0.0
        linear 8.0 yalign 1.0
    with dissolve

    "Я покрываю её шею поцелуями, опускаясь к её груди, чувствуя, как изменяется текстура кожи, когда заканчивается имплантированная и начинается её не пострадавшая от ожога кожа."
    
    show evh hanako_finger_3
    with dissolve

    "Я начинаю массировать её интимное место чуть сильнее и нежно прикусываю набухший сосок, что вызывает вскрик удовольствия лежащей подо мной девушки."
    
    scene bg misc_ceiling
    with locationchange
    
    play sound sfx_impact
    with vpunch

    "Внезапно мир переворачивается, и я нахожу себя смотрящим в потолок."

    "Ханако каким-то образом удалось опрокинуть меня и усесться сверху."

    #too much?

    "Её лобковые волосы щекочут мне кожу, она наклоняется, ведёт влажным язычком по моей шее, а потом прикусывает мне мочку уха."

    "Я думаю, это месть за сосок."
    
    scene white
    with dissolve
    
    show evh hanako_cowgirl_1
    with dissolve

    "Она на секунду перестаёт дышать, а затем откидывается назад и привычным движением смахивает с лица волосы."

    "Её тёмные глаза фокусируются на мне, и некоторое время мы просто смотрим друг на друга."
    
    show evh hanako_cowgirl_2
    with dissolve

    ha "Я… я полагаю, самое время."
    
    show evh hanako_cowgirl_3
    with dissolve

    "Оперевшись на колени, она трётся об мой возбуждённый член, поднимает с пола пакетик из фольги и вскрывает его."

    hi "Я не думаю…"

    "Слишком поздно."

    "Резиновое колечко выскальзывает из упаковки и падает где-то посреди разбросанных на полу закусок и одежды."
    
    show evh hanako_cowgirl_4
    with dissolve

    "Ханако начинает суетиться и пытается подобрать его, но оно снова выскальзывает."

    "Меня забавляет эта картина."

    "Ещё секунду назад Ханако была полностью поглощена мыслями о сексе, а теперь вернулась к своему обычному смущённому состоянию."
    
    show evh hanako_cowgirl_5
    with dissolve

    ha "Н–не смейся. Он очень скользкий…"
    
    show evh hanako_cowgirl_6
    with dissolve

    hi "Думаю, надо было делать как-то так…"
    
    show evh hanako_cowgirl_7
    with dissolve

    "Я беру с пола ещё одну упаковку, разрываю её, достаю оттуда презерватив, прислоняю его к члену и уже собираюсь его надеть…"
    
    show evh hanako_cowgirl_8
    with dissolve

    ha "Можно… я?"

    hi "А? Пожалуйста…"

    "Ханако наклоняется, обхватывает пальцами мой член и аккуратно разворачивает свёрнутый латекс."

    "Я сглатываю, поскольку, по мере того как она надевает презерватив, я чувствую некоторое давление по всей длине ствола."
    
    show evh hanako_cowgirl_7
    with dissolve

    "Но это испытание быстро заканчивается, и Ханако не тратит времени даром; всё ещё сжимая рукой мой член, она садится на него сверху."

    #damn it why am I always ripping off the Lilly path?

    ha "Я… Я делаю это…"

    "Она медленно опускается, направляя меня в себя."

    hi "И… каково это?"
    
    show evh hanako_cowgirl_9
    with dissolve

    ha "Ощущения другие… но приятные…"

    "Она опускается на меня, обхватив мою шею и прижимая моё лицо к своей груди."

    "Я начинаю поднимать и опускать бёдра."

    "Ощущения несколько иные, чем без презерватива, но её тепло всё так же окутывает меня со всех сторон."

    "На каждый мой толчок бёдра Ханако отзываются встречным движением, и я всё глубже в неё вхожу."

    "Я протягиваю руки и беру её за попу, помогая ей двигаться."
    
    show evh hanako_cowgirl_10
    with dissolve

    "Она прижимает меня ещё сильнее к своей груди."

    "Слова сменяются вздохами, а те – вскриками."
    
    show evh hanako_cowgirl_11
    with dissolve

    ha "Х… Хи… Хиса-а-а-а-а-а-о-о-о-о-о-о-о-о-о…"

    ha "Хи-Хи-Хи… Хи-Хи-са-о…"
    
    show evh hanako_cowgirl_12
    with dissolve

    "Пот выступает у меня на лбу только для того, чтобы быть стёртым её грудями; мои пальцы медленно скользят по нежной коже её попы."

    "Я со всей силы сжимаю руки, и Ханако теряет всякую способность говорить."

    ha "Хи-и-и-ха-ха-ха-ха-ха-а-а-а-а-а-а…"
    
    show evh hanako_cowgirl_13
    with dissolve
    
    $ renpy.music.set_volume(0.0, 1.0, channel='music')
    
    play sound sfx_doorknock2

    "…"

    li "Ханако? Ханако? С тобой всё в порядке?"

    li "Мне кажется, я что-то слышала… Я вхожу…"
    
    show evh hanako_cowgirl_14
    with dissolve

    "Мы с Ханако замираем и слышим, как Лилли отчаянно дёргает закрытую ручку двери."

    "Слышится стук в дверь, после чего наступает тишина."
    
    "…"

    "Голоса Лилли больше не слышно, и мы облегчённо вздыхаем."
    
    $ renpy.music.set_volume(1.0, 5.0, channel='music')

    hi "Эм, стоит ли нам продолжать?"
    
    show evh hanako_cowgirl_15
    with dissolve

    "Ханако, потерявшая дар речи, просто заваливается на меня."

    "Мы так близко, и сложившаяся ситуация заставляет наши сердца бешено биться."

    "Нас переполняет нервная энергия, и мы ускоряем наши толчки."

    "Я слышу, как Ханако пытается сдерживать стоны, но влажные шлепки скрыть не получается."
    
    show evh hanako_cowgirl_16
    with dissolve

    ha "Хисао… Я… Я…"

    hi "Я тоже… Ещё немного…"

    "Мои мышцы напряжены, руки сжимаются ещё сильнее, и мы ускоряем наши движения."

    ha "Хисао… Я… Я…"

    hi "Ещё… немно–о–о–го…"
    
    show evh hanako_cowgirl_17
    with dissolve

    "Ханако обхватывает меня и крепко сжимает ноги."

    ha "Я… кончаю!"
    
    show evh hanako_cowgirl_18
    with dissolve

    "Мои ногти вонзаются в зад Ханако, я выгибаю спину и теряю над собой контроль."

    "Я чувствую, как горячая сперма заполняет презерватив; не самое приятное ощущение, честно говоря."

    "Я выхожу из Ханако и снимаю презерватив, весь покрытый нашими соками."

    hi "Э…"

    return

label ru_HT13x:

    scene bg misc_ceiling
    with locationchange

    "Ханако сползает с меня и ложится рядом."

    ha "Это было… здорово."
    
    stop music fadeout 3.0

    hi "Да уж, но… полагаю, мне надо в душ."
    
    scene bg school_dormbathroom at bgleft
    with locationchange

    "Я беру двумя пальцами использованный презерватив и несу его в ванную."
    
    show lilly basic_listen_close
    with charaenter
    
    play sound sfx_impact
    
    show bg school_dormbathroom
    show lilly basic_pout at centersit
    with vpunch
    
    play music music_running fadein 1.0

    "Я не глядя захожу, и едва не спотыкаюсь об Лилли."

    hi "Лилли?!"
    
    show lilly basic_surprised at centersit
    with charachange

    li "Х–Хисао? Ч–что ты тут делаешь?"
    
    show lilly basic_surprised
    with ease

    "Лилли пытается подняться как можно быстрее, но в итоге чуть не падает."

    #Lilly Surprised

    "Инстинктивно я протягиваю руку, чтобы ей помочь, но в последнюю секунду убираю её."

    "Довольно сложно объяснить, что я здесь делаю, не говоря уже о том, что я с головы до ног покрыт своими соками и соками Ханако."
    
    show lilly basic_emb
    with charachange

    "Она справляется сама, но не может скрыть написанного на лице смущения."

    hi "С тобой всё в порядке?"
    
    show lilly basic_concerned
    with charachange

    li "Я… слышала какие-то странные стоны и подумала, что с Ханако что-то случилось."
    
    show lilly basic_listen
    with charachange

    li "Вчера у неё была трудная ночь, поэтому я решила проверить её."

    li "А так как я давно её не слышала, ей могло быть плохо."
    
    show lilly basic_emb
    with charachange
    
    li "Входная дверь была заперта, и я решила попробовать пробраться к ней через ванную комнату…"
        
    extend " нотеперьяпонимаючтопроблемнетспокойнойночи."
    
    stop music fadeout 4.0
    
    hide lilly
    with charaexit

    "Лилли слишком смущена, чтобы остаться в нашей компании; она кланяется и ретируется в свою комнату."
    
    play ambient sfx_shower fadein 1.0
    
    show steam 
    show steam2
    with dissolve

    "Чтобы исключить дальнейшие возможные неудачи, я смываю презерватив в унитаз и включаю душ."

    "Я смываю с себя пот, а потом меняюсь местами с Ханако."
    
    stop ambient fadeout 1.0

    "Вытираемся мы в полной тишине."
    
    scene bg school_dormhanako
    with locationchange

    "Ханако надевает пижаму, и я тоже переодеваюсь."
    
    show hanagown normal
    with charaenter
    #Hanako pjs embarrassed looking down.

    "Потом мы застенчиво смотрим друг на друга, кажется, что целый час."
    
    show hanagown distant_blush
    with charachange

    "За это время каждый из нас несколько раз порывается что-то сказать, но в итоге мы храним молчание."

    "Мы слишком смущены, чтобы что-то делать, поэтому просто сидим."
    
    play sound sfx_doorknock2
    
    show bg school_dormhanako at bgright
    show hanagown normal_blush at tworight
    with dissolvecharamove

    "Спустя некоторое время раздаётся робкий стук в дверь, сопровождаемый тихим шёпотом."

    li "Хисао, Ханако, я тут чай заварила, не хотите ли присоединиться?"

    "Точно зачарованные словами Лилли, мы с Ханако встаём и открываем дверь."
    
    play sound sfx_dooropen
    
    scene bg school_girlsdormhall
    show lilly basic_concerned at twoleft
    show hanagown worry at tworight
    with locationskip
    #bg dormhall
    
    play music music_comfort fadein 1.0

    hi "Лилли… Прости…"

    ha "Такого больше не повторится."
    
    show lilly basic_smile at twoleft
    with charachange
    #Lilly Smile

    li "Это я должна извиниться за то, что вторглась в вашу частную жизнь."

    hi "Но мы…"
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Вы делали то, что и должны делать любящие друг друга люди."
    
    show lilly basic_oops at twoleft
    with charachange

    li "Но стоило ли этим заниматься после того, что случилось вчера ночью?"
    
    show hanagown normal at tworight
    with charachange

    ha "Но медбрат сказал…"
    
    show lilly basic_pout at twoleft
    with charachange
    #Lilly surprised

    li "Вы спрашивали его, можно ли вам заниматься сексом?"

    hi "Ну… Не совсем, но думаю, что он догадался…"
    
    show lilly basic_emb at twoleft
    with charachange
    #Lilly blush

    li "Так вчера ночью вы…"
    
    show hanagown distant_blush at tworight
    with charachange

    ha "Прости, я не рассказала тебе…"

    li "А я думала, что обморок был следствием вашей долгой прогулки…"
    
    show lilly basic_weaksmile at twoleft
    with charachange
    #lilly smile

    "Лилли качает головой, словно пытаясь осознать услышанное."

    li "Пойдёмте, чай остывает."
    
    scene bg school_dormlilly
    show lilly basic_smile at twoleftsit
    show hanagown distant at tworightsit
    with locationskip
    #bg dormlilly

    "Мы втроём сидим за маленьким столиком в комнате Лилли и в неловком молчании пьём чай."

    "Ханако и я сидим со смущёнными лицами, тогда как Лилли, судя по всему, весьма довольна сложившейся ситуацией."
    
    show lilly basic_planned at twoleftsit
    with charachange

    li "Полагаю, я была неправа относительно вас двоих."
    
    show hanagown normal at tworightsit
    with charachange

    hi "А? Что ты имеешь в виду?"
    
    show lilly basic_smileclosed at twoleftsit
    with charachange
    #Lol convenient plot-tie up phase GET. And you thought this was just porn.

    "Улыбка Лилли становится шире; такая улыбка бывает у того, кто вспоминает своё детство."

    li "Когда вы с Ханако встретились впервые, я подумала, что это отличный шанс для неё найти кого-то, что был бы ей больше чем другом."
    
    show lilly basic_listen at twoleftsit
    with charachange

    li "Но после фестиваля и того пикника я подумала, что ты не интересуешь её в этом плане."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "Поэтому я решила, что пусть всё идёт своим чередом. Любое вмешательство в такого рода дела до добра не доводит."

    hi "Я не понимаю, что ты имеешь в виду…"
    
    show hanagown worry at tworightsit
    with charachange

    ha "Ты… хотела свести нас?"
    
    show lilly basic_weaksmile at twoleftsit
    with charachange

    li "Ну, не то чтобы… Я просто хотела подтолкнуть вас друг к другу."

    li "Однако похоже, что мне ничего не пришлось делать."

    hi "Думаю, это не совсем так."

    hi "Если бы ты не заболела, то мы с Ханако вряд ли были бы сейчас вместе."
    
    show hanagown smile at tworightsit
    with charachange

    ha "Я тоже так думаю."

    hi "И ты всё так же наш друг… И будешь им так долго, сколько пожелаешь."
    
    show lilly basic_ara at twoleftsit
    with charachange
    #Lilly insulted? Or happy

    li "Боже, боже, разумеется. Я так рада за Ханако."
    
    show lilly basic_weaksmile at twoleftsit
    with charachange
    
    li "Ей пришлось нелегко. Когда она впервые попала сюда, я думала, что она никогда никому не откроется."

    li "Прошло примерно два месяца, прежде чем она со мной заговорила."

    hi "Серьёзно? Но вы выглядите как лучшие подруги…"
    
    show hanagown normal at tworightsit
    with charachange

    ha "Лилли всегда была добра ко мне, просто поначалу я немного боялась…"

    hi "Ну да, это довольно сложно – перевестись в новую школу, тем более такую, как эта."

    hi "Я до сих пор не могу поверить в то, что так быстро со всеми тут поладил."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "Новые места – новые знакомства, так было всегда."

    li "И нет ничего странного в том, что ты нашёл столько новых друзей в таком месте, где все равны, потому что они отличны от других."

    #too much?

    "Я открываю рот, чтобы возразить, но вместо этого только долго зеваю."

    hi "Ох… Прошу прощения…"
    
    show lilly basic_planned at twoleftsit
    show hanagown smile at tworightsit
    with charachange
    #Lilly and Hanko smile

    li "Ничего страшного."

    li "Могу представить, как ты устал."
    
    show hanagown normal_blush at tworightsit
    with charachange
    #Hanako embarrassed

    hi "Ага, и я ведь даже не притрагивался к урокам…"
    
    show lilly basic_oops at twoleftsit
    show hanagown worry_alt at tworightsit
    with charachange
    #Hanako shokku!

    ha "Экзамены! Я совсем забыла!"
    
    show hanagown worry_blush at tworightsit
    with charachange
    #dicking-induced amnesia. Happens all the time.

    "Я глажу Ханако по голове."

    hi "Вот что: завтра вечером мы позанимаемся вместе. Идёт?"
    
    show hanagown smile_blush at tworightsit
    with charachange
    #Hanako embarrassed happy

    ha "Хо–хорошо."
    
    show lilly basic_giggle at twoleftsit
    with charachange

    li "Ой-ой, звучит любопытно."

    hi "Как бы то ни было, нам нужно готовиться."

    hi "Мы в одном классе, так что в этом есть смысл, верно?"
    
    show hanagown worry_blush at tworightsit
    with charachange

    ha "Верно?"
    
    show lilly basic_oops at twoleftsit
    with charachange

    li "…"

    hi "Честно! Это не то чтобы…"
    
    show lilly basic_weaksmile at twoleftsit
    with charachange
    #Lilly smile/ fufufu

    li "Отлично, поверю тебе на слово."
    
    show hanagown normal_blush at tworightsit
    with charachange

    li "Однако теперь, полагаю, тебе стоит вернуться к себе в комнату, чтобы не причинять нам ещё больших проблем."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "Спокойной ночи, Хисао."
    
    show hanagown normal_blush at tworight
    with ease
    
    show bg school_dormlilly at bgleft
    show hanagown normal_blush at center
    show lilly basic_smile at leftsit
    with charamove

    "Я поднимаюсь, и Ханако вскакивает на ноги."
    
    show hanagown smile_blush
    with charachange

    ha "С… спокойной ночи, Хисао…"
    
    show hanagown smile_close
    with charachange

    "Она наклоняется вперёд, едва не зацепившись за стоящий перед ней стол."

    "Она целует меня в щёку и широко улыбается."

    ha "Я… Увидимся завтра на уроках."

    hi "Спокойной, Ханако."

    ha "Хисао?"
    
    stop music fadeout 4.0

    hi "М?"

    ha "Я люблю тебя."

    hi "Я тоже тебя люблю, Ханако."
    
    scene black
    with dissolve

    #Fade to black.

    return
