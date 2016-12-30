label ru_HT14:

    #Classic Kotoko.
    #also Lol yuri themes.
    
    window hide None
    
    scene bg school_scienceroom
    with locationchange
    #bg Classroom

    #Act 5 (?) title card… I need to think of a title. Not really good at that. Something "final".
    
    play music music_night fadein 4.0
    
    nvl show dissolve

    n "\n\nНу и выходные. После возвращения из комнаты Лилли я сразу же лёг спать…"

    n "…забыв включить будильник."

    n "\nЕсли бы одна не в меру громкая птица меня не разбудила, я бы точно опоздал на урок."

    n "Пробежка до класса заставляет моё сердце пылать, в плохом смысле этого слова."

    n "Некоторые шутят, что так можно и инфаркт заработать."

    n "Но это перестаёт быть смешным, когда становится частью твоей жизни."

    n "\nНо это не главное."

    n "Из-за опоздания я не успеваю поговорить с Ханако и у меня остаётся лишь несколько секунд перед началом урока, чтобы с ней поздороваться."

    n "…среди всего прочего."
    
    nvl hide dissolve

    nvl clear
    
    window show

    "Муто заканчивает писать на доске расписание экзаменов и откладывает в сторонку мел."
    
    show muto normal
    with charaenter
    #Mutou serious

    mu "На этом наши уроки заканчиваются. С этого момента и до конца экзаменов – неучебное время."

    mu "Я и другие учителя готовы помочь вам в подготовке."
    
    show muto irritated
    with charachange
    #Mutou contemplative

    mu "Но если вы до сего момента не учили материал, то не думаю, что мы сможем вам чем-нибудь помочь."
    
    play sound sfx_normalbell
    
    hide muto
    with charaexit
    
    stop music fadeout 4.0

    "Звонит колокол, Муто покидает класс, но никто не шевелится."

    "Серьёзность его слов, кажется, задела за живое довольно большое количество учеников."

    "Все сидят с бледными лицами, но пуще прочих побледнела ученица, сидящая ко мне ближе всех."
    
    show bg school_scienceroom at bgright
    with charamove
    
    play music music_comedy fadein 1.0
    
    show misha sign_confused
    with charaenter
    #misha sad/heh…. heh… heh

    mi "Ха… ха…"

    mi "Эй, Хисао…"
    
    show misha perky_confused
    with charachange

    mi "Он же шутит, да? Ха… ха…"

    "Ого, не думал, что кому-то под силу выбить Мишу из седла."

    "Она продолжает улыбаться своей идиотской улыбкой, но глаза у неё пусты."

    "Нет, даже ещё хуже."

    "Миша сейчас больше напоминает зомби."

    hi "Наверняка всё не так уж и плохо."

    hi "Я имею в виду, что ты ведь как-то умудрялась до этого момента сдавать зачёты, верно?"

    "Никакой реакции."

    "Что ж, каждый получает то, что заслуживает."
    
    show shizu invis at right
    with None
    
    show bg school_scienceroom at center
    show shizu cross_angry at tworight
    show misha perky_sad at twoleft
    with dissolvecharamove
    #Shizune pissed off

    "У Миши за спиной %(name_shizune)s нетерпеливо постукивает по парте."

    "Однако Миша никак не реагирует, так что я перевожу взгляд на %(name_shizune)s."

    "Я жестами пытаюсь поинтересоваться, что случилось, но безрезультатно."
    
    show shizu behind_frown at tworight
    with charachange

    shi "…"
    
    show shizu adjust_frown at tworight
    with charachange

    "Она вздыхает, поправляет очки на носу и указывает на что-то позади меня."

    hi "Э?"

    ha "Доброе утро, Хисао!"
    
    show hanako invis at offscreenright
    with None
    
    show bg school_scienceroom at bgleft
    show shizu behind_blank at center
    show misha perky_sad at left
    show hanako basic_smile at right
    with dissolvecharamove
    #Show Hanako Happy

    hi "Ханако! Прости, я отвлёкся и опоздал сегодня утром, и… мде…"

    ha "В–всё в порядке. Я хотела поговорить и с Мишей с %(name_shizune)s."

    hi "Хм?"

    #Misha Eh?
    
    show misha sign_confused at left
    with charachange

    "Миша перегружается и выходит из задумчивости."

    mi "Ты хочешь поговорить с нами?"
    
    show hanako emb_timid at right
    with charachange
    #hanako embarrassed

    ha "Ну, как бы… Я сегодня слишком много приготовила, а вы с %(name_shizune)s часто общаетесь с Хисао… вот я и…"
    
    show hanako emb_blushtimid at right
    with charachange
    #mabye a more embarrassed Hanako?

    ha "Вот я и подумала… Не захотите ли вы составить нам компанию… Перекусить и готовиться к экзаменам…"

    extend " может быть…"

    extend " если вы не против…"
    
    show misha hips_grin at left
    with charachange
    #misha excited

    mi "А? Что? Ты предлагаешь нам пойти с тобой?!"

    mi "Но ты же ни с кем не разговариваешь!"
    
    show hanako emb_blushing at right
    with charachange

    ha "Ну, я подумала, что вам с %(name_shizune)s будет скучно вдвоём…"

    ha "Ведь в Совете никого больше нет…"

    hi "Мне кажется, ты говорила, что в Школьном совете много людей?"
    
    show misha sign_smile at left
    with charachange

    mi "Это и так, и не так."
    
    show misha cross_smile at left
    with charachange

    mi "Как-то так."

    hi "А, я понял."

    "Ничего я не понял."
    
    show misha cross_laugh at left
    with charachange

    mi "Но это отличная новость! Ланч! Учёба!"

    mi "Мы в деле!"

    hi "Э… А не хочешь сперва у %(name_shizune)s спросить?"

    "%(name_shizune)s сидит прямо за Мишей, которая, кажется, на обращает на её присутствие никакого внимания."

    "Я думаю, что на моей памяти это самый длительный диалог в исполнении Миши, когда она ничего не жестикулирует."
    
    show misha cross_grin at left
    with charachange

    mi "Что? Ва-ха-ха-ха~! Она сделает вид, что против, но на самом деле придёт."
    
    show misha cross_smile at left
    with charachange

    mi "Мы видели, насколько ты силён в естественных науках."

    mi "Нам нужен кто-то вроде тебя, кто разбирался бы в этом."

    "Миша понижает голос."
    
    show misha perky_smile at left
    with charachange

    mi "%(name_sicchan)s никогда в этом не признается, но у неё туго с естественными науками."
    
    show misha hips_laugh at left
    with charachange

    mi "Только не говорите ей, что я вам это сказала~!"
    
    show shizu behind_frustrated
    with charachange

    "За спиной Миши поднимается тень."

    "Постукивание по столу не работает."

    "Постукивание по плечу не работает тоже."

    "В словаре глухих это означает «простите» и «эй, Миша!»."

    "Но Миша не обращает никакого внимания."
    
    play sound sfx_impact
    
    show misha perky_sad at left
    show shizu cross_rage at center
    show hanako defarms_shock at right
    with vpunch

    "Тень начинает злиться и изображает «Я с тобой разговариваю, чёрт побери!», причём наиболее выразительным образом из всех, что я когда-либо видел."

    #Misha cry/rubbing head

    mi "Оу… %(name_shizune)s~"
    
    show hanako def_worry at right
    with charachange

    mi "Ты не должна была делать этого."
    
    show shizu behind_frustrated
    with charachange

    mi "Да, я так делала, но ты не обращала внимания."
        
    mi "Но я говорила с Хисао…"
    
    show shizu basic_angry
    with charachange

    mi "О чём?"
    
    show misha sign_sad at left
    with charachange

    mi "Хм…"

    "Миша замолкает, однако её руки, кажется, живут своей жизнью и выкладывают все её мысли %(name_shizune)s."
    
    show shizu behind_frown
    with charachange

    mi "Я должна снова вас ударить за то, что вы так обнаглели. Теперь скажите мне, что происходит?"
    
    show misha hips_grin at left
    with charachange

    mi "А, Хисао и Ханако хотят готовиться к экзаменам вместе с нами! Разве не здорово?"

    show shizu adjust_blush
    with charachange
    #Shizune blush

    mi "Правда?"
    
    show shizu behind_blank
    with charachange
    
    extend " Ну, на период экзаменов деятельность Школьного совета сводится к минимуму, так что это хорошая идея."
    
    show misha sign_smile at left
    with charachange

    mi "Послушай, %(name_sicchan)s, можем ли мы использовать кабинет Совета?"
    
    mi "А почему бы и нет? Хисао, что скажешь?"

    hi "Ась?"

    "Я был настолько зачарован её монологом, что не сразу сообразил, что она меня о чём-то спрашивает."
    
    show hanako emb_emb at right
    with charachange

    ha "Звучит заманчиво."

    hi "Ага, конечно. Но сперва давайте поедим."
    
    show misha cross_grin at left
    show shizu adjust_happy
    with charachange

    mi "Йюппи~! Еда! Нам надо поесть, верно?"

    mi "Учиться лучше на сытый желудок, да?"

    "Я не знаю даже, кто из них что говорит."
    
    show misha hips_smile at left
    with charachange

    mi "Итак, куда мы идём?"

    ha "Ну, я попросила Лилли встретить нас в обычном месте, так что, может…"

    mi "А это где?"

    hi "На крыше. Это в некотором роде наше тайное место: туда никто никогда не ходит."
    
    show misha sign_smile at left
    with charachange

    mi "Ты прав, никогда там не была."
    
    show shizu behind_frown
    with charachange

    mi "Потому что это запрещено."
    
    show misha perky_sad at left
    with charachange

    mi "Бу-у, не будь такой занудой. Хана пригласила нас, так что неприлично будет сказать «нет»."
    
    show shizu basic_normal
    with charachange

    mi "Ханако пригласила нас?"
    
    show hanako cover_worry at right
    with charachange

    ha "Д–да."
    
    show shizu behind_smile
    with charachange

    mi "Хех. Я думаю, мы не можем отказаться."
    
    show misha hips_grin at left
    with charachange

    mi "Прекрасно! Веди нас, Хисао!"
    
    stop music fadeout 3.0

    hi "Ну… Ладно."

    "Чуть смутившись, я первым поднимаюсь по лестнице, ведущей на крышу."
    
    scene bg school_roof at bgleft
    with locationskip
    
    play music music_ease fadein 4.0
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')
    play ambient sfx_rooftop fadein 1.0

    #bg roof.
    #The following scene was originally going to be my finale.
    #It will require a lot of direction.
    #hopefully we can get away without my panning and zooming.
    #You know, like a certain other rooftop scene.
    #I'll include bits that *need* to be seen.

    "Полуденное солнце ослепляет, но всё же я могу разглядеть три сидящие рядом фигуры."

    hi "О, все уже тут…"

    mi "Все?"
    
    show emi sad_grin at left
    show rin relaxed_nonchalant
    show lilly basic_smileclosed at right
    with charaenter

    li "А, Ханако, Хисао, это вы?"

    ha "Д-да, Лилли. Мы… привели друзей."
    
    show lilly basic_surprised at right
    show emi sad_shy at left
    show rin relaxed_surprised
    with charachange

    emi "Друзей?"
    
    rin "Привели?"
    
    show misha perky_confused at offscreenleft
    with None
    
    show bg school_roof at center
    show lilly basic_surprised at offscreenright
    show misha perky_confused at left
    show emi sad_shy at center
    show rin relaxed_surprised at right
    with dissolvecharamove

    mi "Эй, я тебя знаю."
    
    show emi basic_confused
    show rin basic_surprised at right
    with charachange

    $doublespeak (rin, emi, u"Кого?", u"Кого?")

    mi "А, ты не помнишь? В кабинете кружка рисования?"
    
    show emi basic_shock
    show rin basic_deadpan at right
    with charachange
    #Emi embarrassed/ O_O

    rin "Не думаю, что я что-то такое помню."

    emi "Только не говорите мне…"
    
    show misha hips_grin at left
    with charachange

    mi "Я так и думала! Там было темно, так что…"
    
    show emi excited_sad
    with charachange

    emi "Это ошибка!"

    hi "Дамочки, вы о чём?"
    
    show misha cross_smile at left
    show emi basic_closedsweat
    with charachange
    #Misha ultra happy/ Emi Ultra O_O

    $doublespeak (mi, emi, u"Это секрет.", u"Это секрет.")
    
    show rin relaxed_doubt at right
    with charachange

    rin "Это было дважды, Эми…"
    
    show emi excited_sad
    with charachange

    emi "Это было только один раз!"
    
    show shizu basic_normal2 at offscreenleft
    with None
    
    show bg school_roof at bgright
    show shizu basic_normal2 at left
    show misha cross_smile at twocenteroff2
    show emi excited_sad at tworight
    show rin relaxed_doubt at right
    with dissolvecharamove

    mi "Что было один раз?"
    
    show misha perky_smile at twocenteroff2
    with charachange

    mi "А, не обращай внимания, мы просто однажды уже встречались."
    
    show emi sad_shy at tworight
    with charachange

    emi "Я искала Рин и…"
    
    show rin basic_deadpan at right
    with charachange

    rin "Ты искала меня в кружке рисования?"

    hi "Я думал, ты там живёшь…"

    ha "Ты проводишь там много времени."

    li "Если мне нужно тебя найти, я в первую очередь иду туда."
    
    show rin basic_awayabsent at right
    with charachange

    rin "Хех. А я бы прежде всего искала там, где я есть."
    
    show misha cross_smile at twocenteroff2
    with charachange

    mi "Логично!"
    
    show emi basic_grin at tworight
    with charachange

    emi "Это всё здорово… Но зачем мы, собственно, здесь собрались?"
    
    show misha hips_grin at twocenteroff2
    show shizu adjust_happy at left
    with charachange

    mi "Нас пригласила Ханако."
    
    show hanako emb_timid at offscreenright
    show lilly invis at right
    with None
    
    show shizu invis at offscreenleft
    show rin invis at tworight
    show emi invis at center
    show bg school_roof at bgleft
    show misha hips_grin at left
    show lilly basic_surprised at twocenteroff3
    show hanako emb_blushing at right
    with dissolvecharamove

    li "Ханако?"
    
    show hanako emb_blushtimid at right
    with charachange

    ha "Я… Я подумала, что нам стоит готовиться вместе…"
    
    show hanako cover_worry at right
    with charachange
    
    ha "Всем нам предстоит сдавать экзамены…"
    
    show misha sign_smile at left
    with charachange

    mi "И мы можем это делать в кабинете Школьного совета."
    
    show lilly basic_ara at twocenteroff3
    with charachange

    li "Ох, я не думаю, что это заставит вас взяться за учёбу. Да, Ханако, Хисао?"
    
    show hanako emb_smile at right
    with charachange
    #Hanako Happy blush

    ha "М… может быть."
        
    show bg school_roof at bgright
    show lilly invis at right
    show hanako invis at offscreenright
    show shizu behind_blank at left
    show rin relaxed_doubt at right
    show misha perky_smile at center
    with dissolvecharamove

    rin "Вы не можете учиться, если не находитесь в кабинете Школьного совета?"
    
    show rin basic_absent at right
    with charachange

    rin "Полагаю, со мной та же история."

    rin "Я никогда до сих пор не готовилась к экзаменам, но и в кабинете Совета ни разу не была."
    
    show misha cross_smile
    with charachange

    mi "Логично."
    
    show shizu basic_frown at left
    with charachange

    shi "…"
    
    show misha perky_confused
    with charachange

    mi "Хотя нет, извини."
    
    show rin basic_deadpan at right
    with charachange

    rin "Как быстро ты изменила своё мнение."

    hi "Она говорит за двоих, а думает за никого."
    
    show misha cross_grin
    with charachange

    mi "Именно так!"
    
    show misha hips_frown
    show shizu adjust_frown at left
    with charachange

    mi "Эй!"

    hi "Видишь?"
    
    show rin relaxed_surprised at right
    with charachange

    rin "Интересно. Ты кто?"
    
    show misha sign_smile
    show shizu behind_smile at left
    with charachange

    mi "%(name_shizune)s."
    
    show misha hips_grin
    with charachange

    mi "А я Миша~!"
    
    show rin basic_surprised at right
    with charachange

    rin "Можем мы подружиться?"
    
    show misha perky_smile
    with charachange

    mi "Почему бы и нет?"
    
    show emi invis at tworight
    with None
    
    show bg school_roof at center
    show shizu invis at offscreenleft
    show rin basic_absent at right
    show misha perky_smile at left
    show emi sad_shy at center
    with dissolvecharamove

    emi "Ей… вы там полегче!"

    hi "А что не так?"
    
    show emi basic_hes
    with charachange
    #emi embarrassed

    emi "Ничего!"

    hi "Э… Ну ладно."
    
    show bg school_roof at bgleft
    show rin invis at tworight
    show emi basic_grin at twocenteroff2
    show misha perky_smile at left
    show lilly basic_smile at tworight
    show hanako emb_emb at right
    with dissolvecharamove

    li "Итак, правильно ли я понимаю, что мы будем готовиться к экзаменам все вместе?"
    
    show hanako emb_timid at right
    with charachange

    ha "Итак, Хисао хорошо разбирается в естественных науках, а ты – в музыке."
    
    show emi sad_shy at twocenteroff2
    with charachange

    emi "Правда? Я совершенно не разбираюсь в естественных науках. Можешь мне помочь?"

    hi "Ну, да… но…"
    
    show misha cross_smile at left
    with charachange

    mi "О, точно! Муто же всегда просит тебя помочь с объяснениями."
    
    show hanako basic_worry at right
    with charachange

    ha "Пожалуйста."

    hi "Похоже, что у меня нет выбора, да?"
    
    show lilly basic_oops at tworight
    with charachange

    li "Хватит ли в кабинете Совета нам места?"
    
    show misha sign_smile at left
    with charachange

    mi "Должно хватить. Мы можем прихватить с собой всяких закусок, чтобы трескать их во время подготовки."
    
    show lilly basic_cheerful at tworight
    with charachange

    li "Прекрасно. Могу я принести свой чайный сервиз?"
    
    show emi basic_happy at twocenteroff2
    with charachange

    emi "У тебя есть чайный сервиз?"

    hi "Ага, причём отличный."
    
    show hanako emb_smile at right
    with charachange

    ha "Мы постоянно им пользуемся."
    
    show emi basic_confused at twocenteroff2
    show misha perky_confused at left
    with charachange

    emi "Подожди-ка, вы встречаетесь?"

    hi "Да. Извини, не успел сообщить."
    
    show bg school_roof at center
    show rin basic_absent at closeright
    show emi basic_grin at center
    show misha perky_smile at left
    show lilly invis at right
    show hanako invis at offscreenright
    with dissolvecharamove

    rin "Зачем вы делаете это?"
    
    show misha cross_grin at left
    with charachange

    mi "А! Так вот почему вы были вместе."

    hi "А ты не заметила?"
    
    show rin basic_deadpanamused at closeright
    with charachange

    rin "Она просто ни о чём не думает."
    
    show rin negative_spaciness at closeright
    with charachange

    rin "Или это другая сказала?"

    "Рин недоумённо, но с интересом смотрит на двойной разум Миши и %(name_shizune)s."

    "Я впервые вижу её такой оживлённой."
    
    show lilly invis at right
    with None
    
    show bg school_roof at bgleft
    show misha invis at offscreenleft
    show rin negative_spaciness at twocenteroff2
    show emi basic_grin at left
    show lilly basic_smile at tworight
    show hanako emb_timid at right
    with dissolvecharamove

    li "Итак, %(name_hakamichi)s и %(name_shiina)s…"
    
    show emi sad_shy at left
    with charachange

    emi "Кто?"

    hi "%(name_shizune)s и Миша…"
    
    show emi sad_grin at left    
    show rin basic_awayabsent at twocenteroff2
    with charachange

    rin "Так вот как их зовут…"
    
    show lilly basic_listen at tworight
    with charachange

    li "…Как я уже говорила, %(name_shizune)s и Миша предоставляют помещение, Хисао – помощь в освоении материала, я – чай."
    
    show hanako emb_smile at right
    with charachange

    ha "Я могу приготовить ещё бутербродов…"

    hi "Отлично…"
    
    show lilly basic_smile at tworight
    with charachange

    li "…Ханако снабжает нас едой…"
    
    show emi excited_happy at left
    with charachange

    emi "А я могу быстро-быстро сгонять в магазин за вкусняшками."
    
    show rin relaxed_surprised at twocenteroff2
    with charachange

    rin "Я не буду учиться, я просто хочу увидеть %(name_shizukichi)s и %(name_shii_sha)s… ещё раз."
    
    show rin relaxed_doubt at twocenteroff2
    with charachange

    rin "%(name_shi_chi_shii_sha)s."
    
    show rin basic_deadpandelight at twocenteroff2
    with charachange

    rin "Ты звучишь как танец."
    
    show bg school_roof at center
    show misha sign_confused at twocenteroff2
    show shizu basic_normal at leftoff
    show rin basic_deadpandelight at tworight
    show emi invis at twoleft
    show lilly basic_oops at rightedge
    show hanako invis at offscreenright
    with dissolvecharamove

    mi "Э?"

    shi "…"

    "Неутомимые руки Миши порхают без устали, пытаясь поспевать за бубнением Рин."
    
    show lilly basic_cheerful at rightedge
    with charachange

    li "Что ж, с этим разобрались. Когда начнём, учитель?"
    
    show rin basic_absent at tworight
    show misha perky_smile at twocenteroff2
    show shizu behind_blank at left
    with charachange

    "На меня смотрят шесть пар глаз, причём каждая следующая выглядит более заинтригованной, чем предыдущая."

    hi "Эм, ну давайте в три?"
    
    show bg school_roof at bgright
    show misha perky_smile at twoleft
    show shizu basic_normal at leftdoor
    show rin basic_absent at right
    show emi basic_happy at twocenteroff3
    show lilly invis at offscreenright
    with dissolvecharamove

    emi "В три! Отлично, я скоро вернусь! Займите мне место!"
    
    show emi basic_grin at tworight
    show rin basic_surprised at right
    with dissolvecharamovefast

    "Эми быстро съедает остатки ланча, хватает Рин за рукав и мчится к лестнице."

    rin "Эм? А мне зачем идти? Я хочу остаться с танцовщицами…"
    
    show emi basic_hes at tworight
    with charachange

    emi "Потому что у меня нет де~енег."
    
    show rin basic_deadpandelight at right
    with charachange

    rin "Я вернусь, %(name_shichishiisha)s."
    
    hide rin
    hide emi
    with charaexit
    
    show bg school_roof at center
    show misha perky_confused at twocenteroff2
    show shizu behind_blank at left
    show lilly basic_smile at tworight
    show hanako emb_emb at right
    with dissolvecharamove

    mi "Э-э?"

    "Пока Мишин мозг изо всех сил пытается усвоить полученную информацию, Ханако раскладывает еду на небольшом пледе."

    "Она была права: тут слишком много даже для двух человек."

    mi "О, ты и правда много наготовила. Всё в порядке?"
    
    show hanako emb_timid at right
    with charachange

    ha "П–пожалуйста, угощайтесь."
    
    show misha cross_grin at twocenteroff2
    with charachange

    mi "Не откажусь!"
    
    show misha cross_smile at twocenteroff2
    with charachange

    mi "Спасибо за еду, Ханако."

    ha "Всегда пожалуйста."
    
    show misha perky_smile at twocenteroff2
    show shizu behind_smile at left
    with charachange

    mi "М-м, вкусно!"

    hi "Говорил же."
    
    show hanako emb_smile at right
    with charachange

    ha "С–спасибо."
    
    show lilly behind_cheerful at tworight
    with charachange

    li "Нет, это тебе спасибо, Ханако."
    
    show bg school_roof at bgleft
    show misha perky_smile at twoleft
    show shizu behind_smile at leftoff
    show lilly behind_cheerful at center
    show hanako basic_normal_close at tworight
    with dissolvecharamove

    "Пока остальные самозабвенно жуют, я наклоняюсь к Ханако."

    hi "Ты уверена, что это была хорошая идея?"
    
    show hanako basic_worry_close at tworight
    with charachange

    ha "Я… Я подумала, что будет лучше, если будет много людей."

    hi "Ты имеешь в виду, чтобы мы учились вместо… ну, этого…"
    
    show hanako basic_bashful_close at tworight
    with charachange

    #Hanako blush

    ha "Т–типа того. Но я… Я всё-таки в том же классе, что и %(name_shizune)s с Мишей."

    ha "И они разговаривали с тобой… Так что теперь я хочу поговорить с ними тоже."

    "Я чувствую, как на моём лице появляется улыбка, и краем глаза замечаю, что Лилли тоже улыбается."

    "Несмотря на немаленькое количество еды, заканчивается она на удивление быстро."
    
    show bg school_roof at center
    show misha perky_smile at twocenteroff2
    show shizu behind_smile at left
    show lilly basic_smile at tworight
    show hanako emb_emb at right
    with dissolvecharamove

    mi "Спасибо."

    ha "На здоровье."
    
    show misha hips_smile at twocenteroff2
    with charachange

    mi "Ой, нам же нужно подготовить комнату Совета для приёма такого числа посетителей. Прошу прощения…"

    hi "Идите, мне всё равно нужно вернуться в общежитие за конспектами."

    mi "Тогда ждём вас в три."
    
    hide misha
    hide shizu
    with charaexit
    
    show bg school_roof at bgleft
    show lilly basic_smile at twoleft
    show hanako emb_emb at tworight
    with dissolvecharamove

    "%(name_shizune)s едва заметно кланяется, и Миша пропускает её вперёд."
    
    show lilly basic_ara at twoleft
    with charachange

    li "Боже, боже, жизнь бьёт ключом!"

    hi "И то верно."
    
    show hanako emb_smile at tworight
    with charachange
    #hanako blush smile

    ha "Я думаю… это было весело."

    hi "А?"

    ha "Это немного напрягало, но было весело."

    hi "Да уж, ты права."
    
    show lilly basic_smile at twoleft
    with charachange

    li "Ты как, готов к учебным сессиям?"

    hi "Сессиям?"
    
    show lilly basic_oops at twoleft
    show hanako emb_timid at tworight
    with charachange

    li "Разумеется. Ты же не думал, что мы заварили эту кашу ради единственного дня, половина которого уже прошла?"

    "Внутри меня что-то оборвалось; неужто я на следующие две недели застряну тут в качестве учителя этих шести девушек?"

    ha "Мне… мне кажется, будет здорово."

    ha "И это меньше отвлекает, чем… чем…"

    show hanako emb_blushtimid at tworight
    show lilly basic_weaksmile at twoleft
    with charachange
    #Hanako super embarrassed

    #Lilly slight blush

    li "Эх, полагаю, что ты права."

    hi "Что ж, как я понимаю, выбора у меня нет."

    hi "Довольно сложно порой спрятаться от одного человека, чего уж говорить о пяти…"
    
    show lilly basic_pout at twoleft
    with charachange

    li "Я не подглядывала…"

    hi "Значит, подслушивала."
    
    show lilly basic_listen at twoleft
    with charachange

    li "Хисао Накай, уж не намекаешь ли ты, что я в некотором роде вуайерист?"

    hi "Нет, ни в коем разе! Но ты…"
    
    play sound sfx_impact
    
    show lilly basic_displeased at twoleft
    with vpunch

    "Лилли направляется ко мне и награждает меня шуточным ударом по спине."

    "Но я всё же не могу не покривляться."

    hi "Эй, оу…"
    
    show lilly basic_planned at twoleft
    with charachange

    li "Молчал бы уж. Я знаю, что это не больно."
    
    show hanako emb_smile at tworight
    with charachange
    #Lilly smile, Hanako laugh

    "Попытка Лилли казаться серьёзной заставляет меня и Ханако разразиться смехом, а потом к нам присоединяется и сама Лилли."
    
    show lilly basic_smile at twoleft
    with charachange

    li "Пойдём, хватит валять дурака. Сколько времени ещё осталось?"

    hi "Эм, чуть меньше часа."
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Что ж, не думаешь ли ты, что стоит подготовиться?"

    hi "Да, ты права. Ханако, тебе нужно с чем-нибудь помочь?"
    
    show hanako basic_bashful at tworight
    with charachange

    ha "Нет, всё в порядке. Увидимся там."
    
    hide hanako
    hide lilly
    with charaexit
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0

    "Я наклоняюсь и целую Ханако, после чего иду собирать свои конспекты."

    "И как, чёрт возьми, я оказался втянут во всё это?"

    return

label ru_HT15:

    scene bg school_council at bgright
    with locationskip
    #bg Student council office.
    #Also Lol directing again.
    play music music_shizune fadein 3.0

    "Я вхожу в кабинет Школьного совета и удивляюсь произошедшим с последнего моего появления здесь изменениям."

    "Точнее, изменениям, произошедшим в последний час."
    
    show shizu behind_smile at tworight
    show misha hips_grin at twoleft
    with charaenter

    mi "Та-да! Как тебе?"

    hi "Я… поражён. Где вы взяли…"
    
    show misha hips_smile at twoleft
    with charachange

    mi "Классы."

    hi "И…"

    mi "Учительская."

    "От абсурдности увиденного я качаю головой."

    "Стол %(name_shizune)s отодвинут в сторону, а на его месте красуются шесть парт, расставленные в два ряда."

    "Рядом с дверью стоит небольшая доска на колёсиках, укомплектованная мелом, губкой и деревянной линейкой."

    show shizu behind_smile at tworight
    show misha hips_grin at twoleft
    with charaenter
    #Misha ultra happy

    mi "Надевай пиджак! Давай!"

    hi "Э, ладно… но чей он?"
    
    show shizu adjust_happy at tworight
    with charachange

    shi "…"
    
    show misha cross_smile at twoleft
    with charachange

    mi "Хватит задавать глупые вопросы."

    mi "Когда берёшься за какую-то такую вот работу, антураж – одна из самых важный частей."
    
    show misha sign_smile at twoleft
    with charachange

    mi "Кроме того, если ты будешь учить нас в своей школьной форме, мы не сможем воспринимать тебя всерьёз."

    hi "Я почему-то думал, что это будет учебная сессия…"
    
    show shizu basic_happy at tworight
    with charachange

    shi "…"

    mi "А это и будет учебная сессия. Для нас."

    mi "Всё верно, Хисао. Ты же собираешься помочь нам с подготовкой!"

    hi "Мне правда надо надевать этот пиджак?"
    
    show misha hips_frown at twoleft
    show shizu behind_frown at tworight
    with charachange

    $doublespeak (shi, mi, "…", u"ДА!")

    "С неохотой я накидываю пиджак на плечи."

    "Он пахнет сигаретным дымом и алкоголем."

    "Сдаётся мне, что кто-то из наших учителей является завсегдатаем местных баров."
    
    show misha cross_grin at twoleft
    with charachange
    
    stop music fadeout 3.0

    mi "Отлично сидит, правда, %(name_sicchan)s?"
    
    show shizu adjust_smug at tworight
    with charachange

    mi "Ага. Как по тебе сшит."
    
    li "Это правда здесь?"
    
    show lilly cane_smile at offscreenright
    show hanako emb_emb at offscreenright
    with None

    show shizu basic_normal2 at twoleft
    show misha perky_smile at left
    show lilly cane_smile at tworight
    #insert flipped version of Lilly sprite here
    show hanako emb_emb at right
    show bg school_council at center
    with dissolvecharamove
    
    play music music_lilly fadein 0.5

    "В дверях появляются Лилли с Ханако, неся огромное количество съестного."

    hi "Да, здесь, входите."

    show hanako basic_bashful at right
    with charachange
    
    ha "Т-ты выглядишь глупо, Хисао."

    hi "Это ты им скажи. Они заставили меня надеть это."
    
    show misha hips_smile at left
    with charachange

    mi "Он идеален, правда, Ханако?"

    "Чем лучше я узнаю Мишу, тем больше уверяюсь в том, что без %(name_shizune)s она просто перестанет функционировать."

    show hanako basic_worry at right
    with charachange
    
    ha "Хм… выглядит знакомо…"

    hi "Это пиджак кого-то из учителей…"
    
    show hanako def_worry at right
    with charachange
    #Hanako thinking/whimsical/something

    ha "Нет, я не об этом."

    ha "Он как будто… из прошлого."
    
    show lilly cane_concerned at tworight
    with charachange

    "Я пытаюсь по лицу понять её мысли, но безрезультатно."

    "Как будто она пытается что-то вспомнить, но не уверена, действительно ли этого хочет."
    
    stop music fadeout 4.0

    hi "Если хочешь, я могу его снять…"
    
    show hanako basic_bashful at right
    with charachange

    ha "Н-нет. Он тебе идёт."
    
    show misha cross_laugh at left
    with charachange

    mi "Говорила же!"
    
    show rin negative_spaciness at offscreenright
    show emi sad_shy at offscreenright
    with None
      
    show misha cross_laugh at offscreenleft
    show shizu basic_normal2 at offscreenleft
    show lilly cane_surprised at left
    show hanako defarms_shock at twoleft
    show emi sad_shy at center
    show rin negative_spaciness at right
    show bg school_council at bgleft
    with dissolveeaseaccel
    play sound sfx_impact
    with vpunch
    
    play music music_emi fadein 0.3

    "Внезапно Ханако подаётся вперёд, едва не роняя чайник."
    
    show emi basic_closedsweat
    with charachange
    
    show emi basic_closedsweat at tworight
    with charamove

    emi "Ой, прости, я тебя не заметила!"
    
    show hanako emb_timid at twoleft
    with charachange

    ha "В-всё в порядке…"
    
    show rin basic_deadpan at right
    with charachange

    rin "Я же говорила, что она очень быстрая."
    
    show emi sad_depressed at tworight
    with charachange
    #Emi Tee-hee/loli tap-self-on-head

    emi "Я всё испортила?"
    
    show hanako def_worry at twoleft
    with charachange

    ha "Нет, всё в порядке."

    "Говоря это, Ханако старается как можно скорее расставить чайный сервиз Лилли на столе %(name_shizune)s."
    
    show emi basic_grin at tworight
    show rin basic_absent at right
    with charachange

    "Следом за ней и Эми вываливает содержимое двух хозяйственных сумок на этот же стол."

    emi "Угощайтесь! Рин удалось накопить немного денег, так что я все их потратила!"
    
    show rin basic_deadpanupset at right
    with charachange

    rin "Я никогда не говорила, что это наши общие деньги…"

    mi "Поздняк метаться!"
    
    show lilly cane_smile at offscreenleft
    show hanako def_worry at offscreenleft
    show misha sign_smile at center
    show shizu basic_normal2 at left
    show emi sad_grin at offscreenright
    #show emi sad_grin at tworight
    show rin basic_deadpanupset at right
    show bg school_council at center
    with dissolvecharamove

    "Миша открывает первую попавшуюся коробку и достаёт печенюшку, покрытую шоколадной глазурью, после чего передаёт коробку %(name_shizune)s."

    show rin relaxed_surprised at right
    with charachange
    
    "Рин замерла в недоумении."
    
    rin "Вы обе едите?"
    
    show shizu cross_wut at left
    with charachange

    shi "…"
    
    show misha perky_confused
    with charachange

    mi "Само собой, а ты как думала?"
    
    show rin basic_sad at right
    with charachange

    rin "Ну… не знаю."
    
    stop music fadeout 1.5

    hi "Эй, мы учиться собираемся или так и будем стоять тут и печенье трескать?"
    
    show misha sign_smile
    show shizu behind_blank at left
    #show emi sad_shy at tworight
    with charachange

    mi "Простите, учитель! Все! Рассаживайтесь по своим местам!"
    
    show misha sign_smile at offscreenleft
    show shizu basic_normal2 at offscreenleft
    #show emi sad_shy at offscreenright
    show rin basic_absent at offscreenright
    show bg school_council at bgleft
    with dissolvecharamove
    
    show bg school_council at center
    with charamove

    "Повинуясь условному рефлексу, девушки садятся за парты."
    
    hide hanako
    hide lilly
    hide misha
    hide shizu
    hide emi
    hide rin
    
    play music music_normal fadein 0.3

    hi "Эм, спасибо, Миша."
    
    show misha sign_smile
    with charaenter

    mi "Без проблем, я ведь староста."

    hi "Ты староста?"
    
    show misha hips_grin
    with charachange

    mi "Больше ни у кого из присутствующих нет подходящей квалификации!"
    
    show misha hips_smile
    with charachange

    mi "Кроме того, %(name_shizune)s ведь постоянно заставляет меня произносить за неё подобающие старосте вещи."

    hi "Понятно… что ж…"

    hi "С чего начнём?"
    
    show emi excited_happy at offscreenright
    #show rin basic_deadpan at offscreenright
    with None
    
    show misha hips_smile at twoleft
    show emi excited_happy at tworight
    show bg school_council at bgleft
    with charamove

    emi "С истории!"
    
    show misha perky_smile at twoleft
    with charachange
    
    hi "Я думал, мы собираемся заняться естественными науками?"
    
    show emi basic_confused at tworight
    with charachange
    #Emi ???

    emi "А разве история это не наука?"
    
    show rin basic_deadpan at right
    with charaenter

    rin "История – это прошлое."

    hi "Думаю, ты права. Есть ещё предложения?"
    
    show misha perky_smile at center
    show emi basic_confused at offscreenright
    show rin basic_deadpan at offscreenright
    show bg school_council at center
    with charamove
    
    show misha sign_sad
    with charachange

    mi "Я не разбираюсь в силе тяжести."

    mi "Там типа всё через mg или через эти «M&M's»?"

    hi "«M&M's»?"
    
    show misha sign_confused
    with charachange
    #Misha confused

    #I should note, I didn't intend to write a 3-page lecture on gravity.
    #Stupid degree.
    #Is it worth keeping? Where should I cut it?

    mi "Ну, сила притяжения всегда вычислялась через mg, а теперь через… какую-то MM."
    
    show lilly basic_pout at offscreenleft
    with None
    
    show misha sign_confused at tworight
    show lilly basic_pout at twoleft
    show bg school_council at bgright
    with charamove

    li "Плагаю, Миша имеет в виду уравнение, в котором сила равна произведению G на m1 и на m2, делёному на r в квадрате."

    show misha cross_smile at tworight
    with charachange
    
    mi "Ага, правило M&M."
    
    show lilly basic_smile at twoleft
    with charachange

    hi "Э… Ну да. Ладно, как-то так я и сам это запоминаю."

    "Я механически беру мел и рисую на доске две окружности."

    "Но из-за нехватки опыта окружности больше напоминают овалы."

    hi "Представьте два шара в космосе."
    
    show shizu behind_blank at offscreenright
    with None
    
    show lilly basic_smile at offscreenleft
    show misha cross_smile at twoleft
    show shizu basic_normal2 at tworight
    show bg school_council at center
    with charamove

    shi "…"
    
    show misha perky_confused at twoleft
    show shizu behind_blank at tworight
    with charachange

    mi "Почему в космосе?"

    hi "Ну, потому что там не нужно будет беспокоиться о внешних факторах."
    
    show misha cross_smile at twoleft
    with charachange

    mi "Понятно."

    hi "Итак, что в данном случае будет иметь значение?"
    
    show misha cross_smile at left
    show shizu behind_blank at center
    show emi basic_confused at right
    show bg school_council at bgleft
    with charamove

    emi "Значение?"

    hi "Я имею в виду, что, по-вашему, может повлиять на силу притяжения?"
    
    show emi sad_annoyed at right
    show misha perky_confused at left
    with charachange

    "Передо мной картина: шесть пустых взглядов."

    "Преподавать сложно."

    hi "Хорошо, давайте по-другому. Что мы знаем об этих шарах?"
    
    show rin basic_deadpanamused at offscreenright
    with None
    
    show emi sad_annoyed at tworight
    show rin basic_deadpanamused at right
    with charamove

    rin "Ни один из них не похож на шар."

    hi "Думаю, это больше связано с моим неумением рисовать."
    
    show emi sad_shy at tworight
    with charachange

    emi "Мы знаем… силу притяжения?"

    hi "Не совсем, её-то мы как раз и пытаемся найти."
    
    show hanako emb_timid at offscreenleft
    with None
    
    show emi sad_shy at offscreenright
    show rin basic_deadpanamused at offscreenright
    show shizu behind_blank at offscreenright
    show hanako emb_timid at left
    show lilly basic_surprised at center
    show misha perky_confused at right
    show bg school_council at bgright
    with charamove

    li "Массу шаров?"

    hi "Бинго."
    
    show lilly basic_smile
    with charachange

    "Я пишу букву «М» под каждым овалом."
    
    show hanako basic_normal at left
    with charachange

    ha "Р-расстояние между ними?"

    hi "Верно. А ещё что?"
    
    show lilly basic_concerned
    with charachange

    "Опять пустые взгляды."

    hi "Ну, в общем-то, больше ничего."

    hi "Теперь поразмыслите вот над чем: если масса одного из шаров увеличится, увеличится ли вместе с тем и сила притяжения или уменьшится?"
    
    show hanako basic_normal at offscreenleft
    show lilly basic_concerned at offscreenleft
    show misha perky_confused at twoleft
    show shizu behind_blank at tworight
    show bg school_council at center
    with charamove
    
    show misha sign_confused at twoleft
    with charachange

    mi "Умень…"
    
    show shizu adjust_frown at tworight
    with charachange

    shi "…"
    
    show misha sign_smile at twoleft
    with charachange

    mi "Увеличится."

    hi "Вовремя подсказала."
    
    show misha cross_grin at twoleft
    show shizu adjust_smug at tworight
    with charachange

    $doublespeak (shi, mi, "…", u"Уже привыкла к этому.")

    hi "Так, а теперь к расстоянию. Если они отдалятся друг от друга, сила притяжения увеличится или уменьшится?"
    
    show shizu adjust_smug at offscreenright
    show hanako basic_normal at twoleft
    show misha cross_smile at tworight
    show bg school_council at bgright
    with charamove

    ha "Уменьшится?"

    hi "И снова верно."
    
    show hanako basic_bashful at twoleft
    with charachange
    
    hi "А теперь нам нужно всё это совместить. Кто-нибудь знает как?"
    
    show hanako basic_bashful at offscreenleft
    show misha cross_smile at twoleft
    show rin basic_absent at tworight
    show bg school_council at bgleft
    with charamove

    rin "GMm на r в квадрате."

    hi "Э, верно. Откуда ты узнала?"
    
    show rin basic_deadpanamused at tworight
    with charachange

    rin "Она уже об этом говорила."

    hi "Точно. Но почему так? Почему мы не r делим на GMm?"
    
    show rin basic_absent at tworight
    with charachange
    
    show lilly basic_surprised at left
    show misha cross_smile at center
    show rin basic_absent at right
    show bg school_council at center
    with charamove

    li "Поскольку сила притяжения уменьшается с расстоянием… мы должны делить, а не умножать?"

    hi "Верно подмечено."

    show lilly basic_cheerful at left
    with charachange
    
    hi "Вам всё понятно?"
    
    show lilly basic_cheerful at offscreenleft
    show misha cross_smile at twoleft
    show rin basic_absent at tworight
    show bg school_council at bgleft
    with charamove
    
    show misha sign_confused at twoleft
    with charachange

    mi "А что тогда G?"

    hi "Это просто константа. Что-то, что связывает остальные элементы."
    
    show rin relaxed_surprised at tworight
    with charachange

    rin "Как белый цвет."
    
    show misha perky_confused at twoleft
    with charachange

    hi "Э?"
    
    show rin negative_spaciness at tworight
    with charachange

    rin "Белый ничего не означает, но он заполняет пустоту."
    
    show rin basic_surprised at tworight
    with charachange

    rin "Но, если бы белого цвета не было, всё остальное не имело бы значения."
    
    show misha hips_laugh at twoleft
    with charachange

    mi "О, я поняла!"

    hi "Правда?"
    
    show misha hips_grin at twoleft
    with charachange

    mi "Ага. Ты такая умная, Рин!"
    
    show rin basic_deadpan at tworight
    with charachange

    rin "Но я могу одновременно разговаривать только с одним человеком."

    hi "Ну что, все довольны?"
    
    show rin basic_deadpan at offscreenright
    show hanako emb_timid at twoleft
    show misha hips_grin at tworight
    show bg school_council at bgright
    with charamove

    ha "Эм… тогда что такое mg один?"
    
    show misha perky_confused at tworight
    with charachange
    #Misha confused

    mi "Да, почему оно меняется?"

    hi "Вообще-то оно не меняется."

    "Я обвожу часть уравнения, описывающего силу притяжения."

    hi "Если вы находитесь на земле, то эти части будут равны, так?"

    hi "G - константа, масса Земли не меняется, а Земля - сфера, поэтому r повсюду одинакова, верно?"

    show hanako emb_timid at offscreenleft
    show misha perky_confused at twoleft
    show emi basic_grin at tworight
    show bg school_council at center
    with charamove
    
    emi "Верно."

    hi "Итак, вся эта часть вместе представляет собой g."

    hi "И если вы g умножите на m, то получите то же самое, что написано здесь."
    
    show misha sign_smile at twoleft
    with charachange

    mi "О-оу."

    mi "Я почти это запомнила."

    hi "Почти?"
    
    show misha perky_sad at twoleft
    with charachange

    mi "Я ничего не записала."

    "Я вдруг осознаю, что у Миши нет времени записывать, потому что ей приходится жестикулировать, чтобы передать %(name_shizune)s лекцию."

    "Мне её даже немного жаль."

    "С другой стороны, мне кажется, что записи %(name_shizune)s будут гораздо более ёмкими и краткими, а всем известно, что Миша их просто спишет."

    "Не перестаю удивляться тому, насколько органичны отношения между ними."
    
    hide misha
    hide emi
    with charaexit

    "Когда девушки заканчивают делать записи, я стираю с доски свои каракули и перехожу к следующему вопросу."

    "Теперь, когда мы задали тон занятия, все, кажется, немного расслабились и мы начинаем в бодром темпе переходить от одного вопроса к другому. Причём вопросы достаточно объёмные."

    "Электростатика, стехиометрия, окислительно-восстановительный потенциал…"

    "Полный курс лекций по естественным наукам за один день."

    "Но после каждого моего скомканного объяснения я вижу всё больше понимания на лицах девушек."
    
    stop music fadeout 4.0

    "Порой произнесение мыслей вслух помогает мне думать."

    "Так гораздо проще, чем читать учебник."
    
    scene bg school_council_ss
    with shorttimeskip
    
    play music music_daily fadein 1.0

    "Мы работаем до самого вечера, время от времени передавая по кругу различные закуски, пока я пишу одну формулу за другой на небольшой классной доске."
    
    show bg school_council_ni
    with Dissolvemove(3.0)

    "Небо снаружи темнеет, и нас заставляет прерваться приближение комендантского часа."

    hi "Думаю, пора расходиться, а то уже поздно."
    
    show misha cross_smile
    with charaenter

    mi "А ещё нам нужно прибраться."
    
    show lilly basic_smile at left
    with charaenter

    li "Мы все могли бы помочь."
    
    show emi basic_grin at right
    with charaenter

    emi "Да, что нужно сделать, учитель?"

    "Хоть я понятия не имею, куда всё это девать, все обращаются ко мне по праву присвоенной ими же должности."

    hi "Эм, полагаю, нужно вернуть на место парты и доску."
    
    show shizu invis behind misha at tworight
    show rin invis at offscreenright
    with None
    
    show bg school_council_ni at bgleft
    show lilly invis at offscreenleft
    show misha cross_smile at left
    show shizu behind_blank at twocenteroff2
    show emi basic_grin at tworight
    show rin basic_deadpan at right
    with dissolvecharamove

    rin "А пиджак больше не твой."

    hi "Э?"
    
    show misha perky_smile at left
    with charachange

    mi "Ты всё ещё в этом пиджаке."

    hi "А? Точно, я и забыл."
    
    show shizu basic_normal at twocenteroff2
    with charachange

    "%(name_shizune)s протягивает мне руку."

    shi "…"
    
    show misha sign_smile at left
    with charachange

    mi "Давай, я отнесу на место. Ключ от кладовки только у меня."
    
    show misha perky_smile at left
    show shizu adjust_happy at twocenteroff2
    with charachange

    mi "Парты нужно отнести в класс 3-2. Увидимся завтра на уроках."

    hi "А, спасибо."

    "Я снимаю пиджак и передаю его %(name_shizune)s."

    hi "Ладно, давайте отнесём всё в класс 2-3."

    emi "Хорошо!"
    
    hide misha
    hide shizu
    with charaexit
    
    hide rin
    hide emi
    hide lilly
    with charaexit
    
    show bg school_council_ni at center
    with charamove

    "%(name_shizune)s с Мишей уходят, чтобы вернуть пиджак на место, а тем временем мы с Ханако и Эми начинаем таскать парты в тот класс, из которого мы их взяли."

    "Лилли предлагает помочь, но мы и втроём можем справиться."

    "Рин мгновение наблюдает за нами, а потом устремляется за Мишей. Скорее всего, для того, чтобы «раскрыть их секрет» или ещё чего-то невероятного."

    "Вернув парты, мы выкидываем остатки закусок и собираем чайный сервиз Лилли."

    "После чего покидаем комнату и направляемся к общежитиям."
    
    show bg school_dormext_full_ni
    with locationskip
    #BG night, outside dorms
    
    $ renpy.music.set_volume(0.1,0.0, 'ambient')
    play ambient sfx_cicadas fadein 0.3
    
    show lilly basic_smile_ni at left
    show emi basic_grin_ni at center
    show hanako basic_smile_ni at right
    with charaenter

    emi "Ты здорово справился."

    hi "Эм, да не особо, но спасибо…"

    li "Нет, правда. Тебе удалось объяснить сложные вещи простым языком…"
    
    show hanako emb_emb_ni at right
    with charachange

    ha "П… притом более простым, чем у Муто."
    
    show emi sad_angry_ni
    with charachange

    emi "Вот и я о чём! Он вечно всё усложняет!"
    
    show emi excited_circle_ni
    with charachange

    emi "«Интегрируй это!», «Дифференцируй то!»"
    
    show emi basic_annoyed_ni
    with charachange

    emi "Это просто невозможно…"

    hi "На самом деле не так уж это всё трудно, но его стиль преподавания простым не назовёшь."
    
    show lilly basic_surprised_ni at left
    with charachange

    li "Ты никогда не думал сделать это своей профессией?"

    hi "Что, преподавание?"
    
    
    show emi basic_grin_ni
    show lilly basic_planned_ni at left
    with charachange

    li "Да. У тебя здорово получается."

    hi "Правда?"
    
    show hanako basic_bashful_ni at right
    show lilly basic_smile_ni at left
    with charachange

    ha "Ты правда хорош."

    hi "Вот как… Никогда об этом не думал."

    hi "Но было вроде как весело."
    
    show hanako emb_blushtimid_ni at right
    with charachange
    #Hanako embarrassed

    ha "И ты… выглядел уверенно."

    hi "В таком случае, наверное, мне стоит купить себе новый пиджак."
    
    show hanako emb_smile_ni at right
    with charachange
    #Hanako embarrassed smile

    ha "Мы… как-нибудь сходим в магазин."
    
    show emi excited_amused_ni
    with charachange
    #Emi excited

    emi "О-о-о-о хо хо-о! Свидание! Свидание!"
    
    show emi excited_joy_ni
    with charachange

    emi "Это же свидание, а?!"

    hi "Да."

    extend " И ты с нами не идёшь."
    
    show emi sad_pout_ni
    with charachange
    #Emi :<

    emi "Эй, но я люблю ходить по магазинам."

    hi "Какая жалость."
    
    show emi excited_proud_ni
    with charachange

    emi "Значит, в другой раз. Мы с тобой пойдём в магазин в следующий раз, учитель."

    hi "Учитель?"
    
    show emi basic_happy_ni
    with charachange

    emi "Ага, прикольно."
    
    show lilly behind_cheerful_ni at left
    with charachange

    li "Вполне уместное обращение, особенно если мы будем часто вот так собираться."

    hi "Эй, я не говорил, что мы будем собираться…"
    
    show hanako basic_worry_ni at right
    with charachange

    ha "Кажется, уже поздно…"

    "После этих её слов я бросаю взгляд на свои часы."
    
    show emi basic_grin_ni
    with charachange

    hi "Чёрт, и правда, уже поздно, только в другом смысле слова."

    hi "Надо бежать, а то не успею до комендантского часа."
    
    show hanako emb_timid_ni at right
    with charachange

    ha "Да… вряд ли тебе удастся оставаться каждую ночь."
    
    show emi basic_confused_ni
    with charachange
    #Emi confused

    emi "Оставаться?"
    
    show lilly basic_pout_ni at left
    show hanako emb_blushing_ni at right
    with charachange

    hi "Да… э… ничего такого. Мы просто…"
    
    show lilly basic_weaksmile_ni at left
    with charachange

    li "Мы с Ханако и Хисао вчера засиделись за уроками до позднего вечера и сами не заметили, как уснули."

    show emi sad_shy_ni
    with charachange
    #emi disappointed

    emi "А, а я подумала, что ты имеешь в виду… кое-что другое."

    hi "Хех, о чём ты? Мы же учащиеся старших классов…"

    extend " и мне действительно нужно идти."
    
    show bg school_dormext_full_ni at bgleft
    show hanako basic_bashful_close_ni at tworight
    show lilly basic_smile_ni at leftoff
    show emi sad_shy_ni at twocenteroff2
    with dissolvecharamove
    
    "Я приобнимаю Ханако и целую её, остальным машу рукой на прощание."

    ha "Спокойной ночи, Хисао."
    
    li "Спокойной ночи."
    
    show emi sad_grin_ni at twocenteroff2
    with charachange

    emi "Вы что, действительно учились?"
    
    show lilly basic_smileclosed_ni at leftoff
    with charachange

    li "Да."

    li "Теперь давайте поторопимся, мы же не хотим, чтобы нас поймали."
    
    show emi basic_grin_ni at twocenteroff2
    with charachange

    emi "Ладно, ладно. Спокойной, учитель. Спасибо."

    hi "Не за что."
    
    hide lilly
    hide emi
    hide hanako
    with charaexit

    "Девушки скрываются в общежитии и закрывают за собой дверь."
    
    stop music fadeout 4.0
    stop ambient fadeout 4.0

    "Мне ничего не остаётся, как вернуться в свою комнату."

    "По правде говоря, я смертельно устал."

    "Не думаю, что я сегодня буду мучиться бессонницей."
    
    scene black
    with dissolve

    return
    
label ru_HT16:

    #Welcome to my nightmare; the two-week timeskip
    #I hate doing this, but slightly less than how much I hate writing about everyone playing
    #school.

    #also, supersized party scene. 50% larger than most other scenes.
    #Upside, almost done with the path.

    #BG Classroom with fade
    play music music_normal fadein 1.0
    
    scene bg school_scienceroom
    show muto irritated
    with locationchange

    mu "И-и-и-и-и-и…"

    extend " время!"
    
    show muto normal
    with charachange

    mu "Откладывайте ручки и сидите на своих местах, я сейчас соберу ваши работы."
    
    hide muto
    with charaexit

    "Муто ходит между партами, ученики передают ему листочки, словно подношения какому-то пророку."

    "Кажется, что за прошедшие две недели он разработал оптимальный алгоритм обхода класса, чтобы собрать все работы за один проход."

    "Он бросает большую стопку бумаг на свой стол, раздаётся громкий глухой звук."
    
    show muto smile
    with charaenter

    mu "Вот и всё. Увидимся после летних каникул."

    "Класс взрывается аплодисментами. Впереди нас ждёт четыре недели отдыха."

    #I'm pretty sure that the summer vacation is only 4 weeks long in Japan.
    
    hide muto
    with charaexit

    "Через феерию конечностей и тел ко мне пробиваются две знакомые фигуры."
    
    show misha perky_smile at twoleft
    show shizu behind_smile at tworight
    with charaenter
    #Show misha/Shizune happy

    mi "Хм, Хисао, мы хотим тебя поблагодарить."

    hi "Серьёзно? Я так понимаю, что наша подготовка не прошла даром?"
    
    show misha hips_laugh at twoleft
    with charachange

    mi "Да-да-да! Не думаю, что я когда-либо так хорошо сдавала экзамены по естественным наукам."
    
    show misha hips_grin at twoleft
    with charachange

    mi "Я смогла это сделать даже с первой попытки!"

    hi "Ну, мне тоже было весело. Думаю, я тоже получу высший балл."
    
    show shizu adjust_blush at tworight
    with charachange
    #Shizune blush

    shi "…"
    
    show misha sign_smile at twoleft
    with charachange

    mi "О, точно! И %(name_shizune)s тоже хочет сказать тебе «спасибо»."
    
    show misha perky_smile at twoleft    
    show shizu adjust_happy at tworight
    with charachange

    mi "Ей очень сложно признаться в этом, но ты ей действительно очень помог."
    
    show hanako invis at offscreenright
    with None
    
    show bg school_scienceroom at bgleft
    show misha perky_smile at left    
    show shizu adjust_happy at center
    show hanako cover_smile at right
    with dissolvecharamove

    #show Hanako generic (not embarrassed)

    ha "Привет, Миша, %(name_shizune)s."
    
    show misha hips_smile at left 
    show shizu basic_normal
    with charachange

    mi "Хана! Добрый день! Как твои успехи?"

    ha "Нормально… я полагаю. А у тебя?"

    #Misha semi lols?
    
    show misha cross_grin at left 
    with charachange

    mi "Просто замечательно! На этот раз наверняка все сдали!"
    
    show hanako basic_smile at right
    with charachange
    #Hanako relieved

    ha "Это хорошо."
    
    show shizu behind_smile
    with charachange
    #Shizune Oh!

    shi "…"
    
    show misha perky_smile at left 
    with charachange

    mi "А! Точно же!"
    
    show misha sign_smile at left 
    show shizu basic_happy
    with charachange

    mi "Сегодня вечером состоится собрание Школьного совета, и они хотели бы пригласить вас…"

    hi "Э… Ты имеешь в виду себя и %(name_shizune)s–э—"
    
    play sound sfx_impact
    
    show misha cross_laugh at left
    show shizu basic_normal
    show hanako basic_normal at right
    with vpunch

    "Резкая боль в груди мешает мне продолжить."

    "Так называемый «Синдром мишиного локтя» мешает мне закончить фразу."

    #Misha Lols

    mi "Ва-ха-ха-ха~! Конечно, это не только мы!"
    
    show misha cross_smile at left
    show shizu adjust_happy
    with charachange

    mi "Вы можете тратить фонды Совета только на официальные мероприятия!"

    mi "Устраивать вечеринки и приглашать друзей строжайше запрещено!"

    hi "Понятно. Значит, это просто собрание, да?"
    
    show shizu behind_smile
    show misha perky_smile at left
    with charachange

    mi "Верно!"

    hi "Я так понимаю, там будут прохладительные напитки, на этом собрании, да?"
    
    show misha hips_smile at left
    with charachange

    mi "Верно!"

    hi "И, вероятно, чтобы вас немного развлечь, мы должны сделать вид, что некоторое время раздумываем, принимать ли ваше приглашение, да?"
    
    show misha hips_grin at left
    with charachange

    mi "Верно!"

    hi "Так какая повестка дня этого собрания?"
    
    show misha perky_confused at left
    with charachange
    #misha ???

    mi "Ась?"
    
    show shizu basic_sparkle
    with charachange

    shi "…"
    
    show misha sign_smile at left
    with charachange

    mi "Ах да, точно."
    
    show shizu adjust_smug behind misha
    show misha perky_smile at left
    with charachange

    mi "Это будет инструктаж о пользе коллегиальной подготовки к экзаменам и взаимопомощи."
    
    show shizu adjust_happy behind misha
    show misha cross_grin at left
    with charachange

    mi "%(name_shizune)s знает толк в придумывании такого рода названий."
    
    show hanako cover_worry at right
    with charachange

    ha "И кто там ожидается?"
    
    show shizu behind_smile
    with charachange

    shi "…"
    
    show misha cross_smile at left
    with charachange

    mi "Все, кто участвовал в эксперименте. Это единственный способ получить объективные результаты."
    
    show shizu basic_happy
    with charachange

    mi "Я думаю, что наша дискуссия может затянуться, поэтому для присутствующих отменяется действие комендантского часа."
    
    show misha perky_confused at left
    with charachange

    mi "Серьёзно?"
    
    show shizu behind_smile
    with charachange

    mi "Я считаю это необходимым."

    hi "А такое возможно?"
    
    show misha perky_smile at left
    show shizu adjust_smug
    with charachange

    mi "Если я разрешила, значит это возможно."

    hi "Звучит разумно."
    
    show shizu adjust_happy
    with charachange

    mi "Логика – одно из величайших достижений человечества."
    
    show hanako basic_worry at right
    with charachange

    ha "Вы остальных уже оповестили?"
    
    show misha sign_smile at left
    show shizu behind_smile
    with charachange

    mi "Их мы пригласили ещё вчера; они закончили раньше нас."
    
    show hanako emb_timid at right
    with charachange
    #hanako concerned

    ha "Даже Лилли?"
    
    show misha cross_smile at left
    with charachange

    mi "Конечно."

    hi "Почему? С Лилли что-то случилось?"
    
    show hanako cover_worry at right
    with charachange

    ha "Нет, дело не в этом, просто…"
    
    show hanako emb_timid at right
    with charachange
    
    stop music fadeout 4.0
    
    ha "А, не важно."

    hi "Ты уверена?"
    
    show hanako basic_normal at right
    with charachange

    ha "Да, ничего такого."

    ha "Сомневаюсь, что она стала бы делать что-нибудь…"
    
    scene bg school_council at bgleft
    show lilly basic_smile
    with shorttimeskip
    
    play music music_shizune fadein 1.0

    #BG Councilroom (direct cut)

    li "Добро пожаловать! Я взяла на себя смелость взять на себя подготовку этой встречи!"
    
    show bg school_council at center
    show lilly basic_smile at tworight
    with dissolvecharamove

    "Уже в который раз комната Школьного совета полностью преобразилась."

    "Тарелки с едой и банки с напитками покрывают практически каждую пядь всех имеющихся в помещении столов."

    "Из глубины комнаты доносится музыка, там у Эми с Рин развернулась нешуточная борьба за то, какая песня будет играть следующей."

    "По центру комнаты, в окружении стены из чашек, располагается большая ёмкость с красной жидкостью."

    "Кусочки фруктов и кубики льда всплывают на поверхность и снова погружаются, как будто судно, сделанное из консервированных фруктов налетело на айсберг."

    "Даже от двери я чувствую приторно-сладкий запах."
    
    show hanako def_worry at twoleft
    with charaenter

    #Hanako shocked/worried

    ha "Ух-ох."

    hi "Ух-ох?"

    hi "Это то, из-за чего ты так беспокоилась?"
    
    show hanako emb_timid at twoleft
    with charachange

    "Ханако просто кивает и в страхе обхватывает мою руку."
    
    show shizu invis at offscreenright
    show misha invis at rightedge
    with None
    
    show bg school_council at bgright
    show hanako emb_timid at left
    show lilly basic_smile at twocenteroff
    show misha hips_grin at twocenteroff3
    show shizu behind_smile at right
    with dissolvecharamove

    mi "Похоже, все здесь!"
    
    show lilly basic_cheerful at twocenteroff
    with charachange

    li "Ах, %(name_shizune)s, Миша, добро пожаловать! Как ваши экзамены?"
    
    show misha cross_smile at twocenteroff3
    with charachange

    mi "Отлично-отлично! А твои?"
    
    show lilly basic_ara at twocenteroff
    with charachange

    li "Думаю, что тоже неплохо. Хисао – хороший учитель, не так ли?"

    hi "Да ладно вам…"
    
    show hanako emb_emb at left
    show lilly basic_smile at twocenteroff
    show misha perky_smile at twocenteroff3
    show shizu basic_happy at right
    with charachange

    li "Тост за Хисао!"

    "При этих словах Эми и Рин вскакивают на ноги."

    "Только сейчас я замечаю полупустые бокалы, стоящие рядом с местом их недавних боевых действий."

    "Эми быстро разливает пунш по ещё пяти бокалам и передаёт их нам."

    emi "За Хисао!"

    hi "Ура!"
    
    show hanako basic_smile at left
    show lilly basic_planned at twocenteroff
    show misha cross_smile at twocenteroff3
    show shizu behind_smile at right
    with charachange

    "За исключением Рин, все поднимают бокалы вверх."

    "А затем все, как один, быстро их опустошают."
    
    show lilly basic_smile at twocenteroff
    show hanako emb_downtimid at left
    show shizu cross_stunned at right
    show misha perky_confused at twocenteroff3
    with charachange

    "%(name_shizune)s и Миша бледнеют."

    #shizune angry, misha confused

    mi "Что это?"
    
    show hanako emb_timid at left
    with charachange

    ha "То, чего я так боялась…"
    
    show shizu behind_blank at right
    with charachange

    "И тут меня осеняет…"

    hi "Лилли, ты готовила этот пунш?"
    
    show lilly behind_cheerful at twocenteroff
    with charachange

    li "О, так он тебе понравился? Это фамильный рецепт."
    
    show hanako basic_worry at left
    with charachange

    ha "Это тот самый пунш, да?"
    
    show lilly basic_weaksmile at twocenteroff
    with charachange

    li "Да, так и есть, Ханако. Я подумала, что у нас большой праздник, поэтому я приготовила его достаточно…"

    extend " ик!"

    hi "«Ик»? Лилли, ты что, икаешь?"
    
    show lilly basic_pout at twocenteroff
    with charachange

    li "…Ик…"
    
    show lilly basic_oops at twocenteroff
    with charachange

    li "Нет."
    
    show rin invis at offscreenleft
    with None
    
    show bg school_council at bgright
    show hanako emb_timid at twocenteroff3
    show lilly basic_oops at right
    show misha invis at rightedge
    show shizu invis at offscreenright
    show rin basic_absent at closeleft2
    with dissolvecharamove

    "Не думаю, что смогу от неё чего-нибудь добиться, поэтому я обращаюсь к Ханако."

    hi "Так из чего пунш-то?"
    
    show hanako emb_blushtimid
    with charachange

    ha "Ну, я точно не знаю, но он очень забористый."

    hi "Боже."

    hi "Мы рискуем получить ещё одну вечеринку в честь дня рождения?"

    mi "Это что ещё за вечеринка?"

    hi "Не-не, ничего."
    
    show rin relaxed_nonchalant at closeleft2
    with charachange

    rin "У меня день рождения, но без вечеринки. Это считается?"

    hi "Нет, я говорю о Лилли…"
    
    show bg school_council at bgleft
    show rin invis at offscreenleft
    show hanako emb_timid at left
    show lilly basic_oops at twocenteroff
    show misha perky_confused at twocenteroff3
    show shizu behind_frown at right
    with dissolvecharamove

    shi "…"
    
    show misha sign_smile at twocenteroff3
    with charachange

    mi "Вы не о том ли случае, когда видели развратную женщину, покидающую вашу комнату?"
    
    show lilly basic_listen at twocenteroff
    with charachange

    hi "Ну…"

    extend " да."
    
    show shizu behind_blank at right
    with charachange

    "%(name_shizune)s на мгновение замирает, чтобы это обдумать."
    
    show shizu adjust_happy at right
    show misha cross_smile at twocenteroff3
    with charachange
    
    stop music fadeout 5.0

    mi "Если это так, то передайте-ка мне ещё стаканчик, пожалуйста."

    emi "Будет сделано!"
    
    show misha hips_grin at twocenteroff3
    with charachange

    mi "И мне тоже!"
    
    scene bg school_council_ni at bgleft
    with shorttimeskip
    
    play music music_ease fadein 1.0

    "На то, чтобы выпить весь пунш, у нас не уходит много времени, после чего мы переходим к другим напиткам, которые приготовила Лилли."

    "Тяжелее всего приходится, кажется, Эми и Рин."

    "Это началось тогда, когда Рин оказалась не в состоянии удерживать ногами чашку."

    "Эми, не желая, чтобы её подруга пропускала этот праздник жизни, начала сама поить её."

    "И, прикрываясь оправданием, что она теперь пьёт за двоих, Эми только и успевала подливать себе пунша."

    "Вскоре после этого эти двое пришли в состояние излишней активности; они начали скакать, что-то напевать и вообще создавать много шума."

    "%(name_shizune)s, напротив, расслабилась; когда алкоголь начал действовать, её щёки зарделись румянцем."

    "Миша просто по-дурацки лыбилась не переставая."

    "Большую часть времени она была занята тем, что переводила всё %(name_shizune)s, но порой отвлекалась на скачущих вокруг Рин и Эми."

    "Вскоре %(name_shizune)s перестала её беспокоить, организовав каким-то образом соревнование кто кого перепьёт с Ханако."

    "Вскоре после этого они обе вырубились в уголочке."

    "Это было даже в некотором роде мило: наблюдать, как они обнимают друг дружку во сне."

    "Но я был единственным, кто это заметил."
    
    show misha hips_grin
    with charaenter

    mi "Ох, это греет тебе душу?"

    hi "А?"
    
    show misha perky_smile
    with charachange

    mi "Эти двое."
    
    show misha sign_smile
    with charachange

    mi "Не находишь ли ты милым, что эти две немногословные девушки теперь лучшие друзья?"

    hi "Да… пожалуй."
    
    show misha hips_grin
    with charachange
    #Misha lol

    mi "Или ты думаешь о чём-то непристойном?"

    hi "Что?! Нет!"
    
    show misha cross_laugh
    with charachange
    
    mi "Ва-ха-ха-ха~! Да всё нормально, Хисао."
    
    show misha cross_smile
    with charachange

    mi "Все мы знаем о тебе и Хане…"

    hi "Что? Откуда?"
    
    show misha hips_grin
    with charachange

    mi "Что вы занимались ТАКИМИ вещами!"

    "Какая-то часть меня хочет с ней поспорить, но выпитый алкоголь притупляет мою волю к борьбе."

    hi "Да уж, было немного. Но не во время подготовки к экзаменам."
    
    show lilly invis at left
    with None
    
    li "И это хорошо, потому что трудно было заснуть, когда вы… ну…"
    
    show bg school_council_ni at center
    show lilly basic_weaksmile at twoleft
    show misha perky_smile at tworight
    with dissolvecharamove

    "Лилли пробирается к Мише, и я отрываюсь от созерцания Рин и Эми, которые пытаются пристроить один из протезов Эми к плечу Рин."
    
    show misha cross_laugh at tworight
    with charachange

    mi "О-хо-хо! Так вам нравится заниматься этим перед публикой!"
    
    show lilly basic_emb at twoleft
    with charachange

    hi "Нет, вовсе нет! Мы просто… просто…"
    
    play sound sfx_impact
    
    show misha hips_grin at tworight
    with vpunch

    "Миша хлопает меня по спине, едва не выбив из меня дух."

    mi "Так держать, Хисао! Настоящий мужик! Повезло же ей с тобой!"

    hi "Хм, спасибо."
    
    show lilly basic_smile at twoleft
    show misha perky_smile at tworight
    with charachange

    mi "Итак, какие у вас планы на каникулы?"

    hi "Ну, Ханако некуда ехать, так что мы решили немного погостить у моих родителей…"
    
    show lilly basic_oops at twoleft
    with charachange

    li "Не рановато ли представлять её родителям?"
    
    show misha hips_smile at tworight
    with charachange

    mi "Или уже немного поздновато, если вы понимаете, о чём я…"

    hi "Я не понимаю, о чём ты?"
    
    show misha sign_confused at tworight
    with charachange
    #Misha, confused

    mi "Хм… О том, что никакого секса до свадьбы…"

    hi "И при чём тут это?"
    
    show misha perky_confused at tworight
    with charachange

    mi "Понятия не имею, это ведь ты собрался её с родителями знакомить."
    
    show misha perky_smile at tworight
    show lilly basic_smile at twoleft
    with charachange

    li "И как ты им это объяснишь?"

    hi "Я спросил их после первой недели экзаменов."
    
    show lilly basic_pout at twoleft
    with charachange

    li "А, ты имеешь в виду после той субботней ночи?"

    hi "Ну… да."

    hi "Так ты знала?"
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Хисао, боюсь, что об этом знало всё общежитие…"

    hi "Чёрт, а мы пытались не шуметь."
    
    show lilly basic_emb at twoleft
    with charachange
    #Lilly Embarrassed

    li "Но что-то пошло не так…"

    hi "Что?"
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Понятия не имею."
    
    show lilly basic_smile at twoleft
    with charachange

    li "Разве не интересно, что всё это была идея Ханако?"

    "Никогда бы не подумал, что Лилли может вот так внезапно сменить тему, поэтому спрашиваю:"

    hi "Что ты имеешь в виду?"
    
    show lilly basic_planned at twoleft
    with charachange

    li "Эту нашу подготовку к экзаменам."

    li "Мне никогда и в голову не пришло бы пригласить так много людей."
    
    stop music fadeout 5.0
    
    show misha perky_confused at tworight
    with charachange

    mi "Может быть, она просто не хотела быть одна?"
    
    show lilly basic_concerned at twoleft
    with charachange

    #I'm not sure about the next bit. Maybe too much "baseball"-ness.
    #There will definitely be mention of the abuse in the "real" path.
    #But this might explain it better… maybe

    hi "Почему ты так думаешь?"
    
    show misha perky_sad at tworight
    with charachange

    mi "Ну, она никогда ни с кем не пыталась заговорить, поэтому мы думали, что она стесняется."

    mi "Может, она просто боялась?"
    
    show lilly basic_surprised at twoleft
    with charachange

    li "Боялась чего?"

    mi "Нас?"

    hi "В этом нет никакого смысла…"
    
    show lilly basic_listen at twoleft
    with charachange

    li "Отнюдь, возможно есть…"

    hi "Что ты имеешь в виду?"
    
    show lilly basic_oops at twoleft
    with charachange

    li "Что, если она хотела иметь друзей, но у неё их просто никогда не было?"
    
    show misha perky_confused at tworight
    with charachange

    "На лбу Миши появляются морщины: Миша думает."

    "Это странно. Я совершенно не могу сосредоточится, тогда как Миша, выпив примерно столько же, думает лучше, чем когда бы то ни было."
    
    show misha sign_confused at tworight
    with charachange

    mi "Нет, не то. Если у тебя никогда не было друзей, то ты пытаешься их завести."

    mi "Это как ботаники вечно крутятся вокруг крутых детей, надеясь привлечь к себе внимание."
    
    show lilly basic_concerned at twoleft
    with charachange

    li "Тогда что ты думаешь?"
    
    play music music_rain fadein 4.0
    
    show misha perky_sad at tworight
    with charachange

    mi "Что, если над ней надругались?"

    hi "Что ты имеешь в виду под «надругались»?"

    mi "Как… ну… знаешь…"

    mi "В том самом смысле надругались…"

    hi "Что? Нет…"
    
    show lilly basic_oops at twoleft
    with charachange

    li "Если бы над ней надругались, она должна была бы ненавидеть мужчин, разве не так?"
    
    show misha cross_frown at tworight
    with charachange

    "Миша качает головой."

    mi "Не только приёмные отцы могут домогаться своих дочерей."
    
    show lilly basic_surprised at twoleft
    with charachange

    $ doublespeak(hi, li, u"Что?", u"Что?")
    
    show misha sign_sad at tworight
    with charachange

    mi "Я к тому, что это могла быть и её мачеха."

    "Я открываю рот, чтобы что-нибудь ей ответить, но мне нечего возразить Мише."
    
    show lilly basic_concerned at twoleft
    with charachange

    li "Видимо, потребуется много времени, чтобы она воспринимала меня как подругу…"

    hi "Что? Нет, этого не может быть! Она бы мне сказала…"
    
    show misha perky_sad at tworight
    with charachange

    mi "Серьёзно? Вы знакомы только два месяца, этого очевидно недостаточно, чтобы всё тебе рассказать."

    #Actually, I kinda do like this way.
    #Stay tuned for the end of the path, wherein Hisao forces Hanako to go to her old house.

    "Эмоции и алкоголь ввергают мой мозг в водоворот мыслей."

    "Что-то из сказанного Мишей определённо имеет смысл, но это просто невероятно."

    "Ханако действительно крайне настороженно относится к людям."

    "Но казалось, что она сразу же мне открылась; даже Лилли сказала об этом при нашей первой встрече."

    "Но сколько я ни думаю об этом, целой картины не складывается, словно не хватает одного кусочка пазла."
    
    stop music fadeout 3.0

    "Огонь, теперь ещё это предполагаемое изнасилование… Всё это в голове не помещается."
    
    play sound sfx_impact2
    with vpunch

    "Раздавшийся за спиной грохот отвлекает меня от этих тяжких дум."

    emi "Простите, я думала, что иду прямо…"

    mi "Эй, с тобой всё в порядке?"
    
    show emi invis at leftsit
    with None
    
    show bg school_council_ni at bgright
    show lilly invis at center
    show misha perky_confused at center
    show emi sad_shy at leftsit
    with dissolvecharamovefast
    
    show emi sad_shy at left
    with charamove

    "Миша подбегает к Эми и помогает ей сесть на ближайший стул."
    
    show emi basic_closedsweat at left
    with charachange

    emi "Хе-хе, спасибо."
    
    show misha hips_smile at center
    with charachange

    mi "Всё нормально. Так, давай-ка я тебе это подам…"
    
    show misha perky_smile at tworight
    with dissolvecharamove
    
    show emi basic_grin at twoleft
    with dissolvecharamove
    
    play music music_emi fadein 6.0

    "Миша поднимает протез Эми с пола и начинает крепить его к её ноге."

    hi "Хех, похоже, что тебе доводилось уже делать это ранее."
    
    show emi sad_shyblush at twoleft
    with charachange
    #emi embarrassed.
    #Also, Apologies to Hive and Atwo.

    emi "Ну, только однажды."

    hi "Что только однажды?"
    
    show misha cross_grin at tworight
    with charachange

    mi "А, ничего. Просто я однажды помогала Эми. Ничего такого."
    
    show emi basic_hes at twoleft
    with charachange

    emi "Кстати, о той… истории, что ты рассказала мне в кабинете кружка рисования…"

    extend " Не могла бы ты… сказать, чем она закончилась?"
    
    show misha perky_confused at tworight
    with charachange

    mi "История?"
    
    show emi sad_annoyed at twoleft
    with charachange
    #Emi irritating
    
    emi "Ну, знаешь… та история…"
    
    emi "С тех пор…"
    
    show misha hips_grin at tworight
    with charachange
    #Misha surprised/realisation

    mi "А!"
    
    show misha sign_smile at tworight
    with charachange

    mi "Нормально… полагаю."
    
    show emi sad_grin at twoleft
    with charachange

    emi "Я уже сходила и проверила кабинет рисования, дверь не закрыта…"
    
    show misha perky_confused at tworight
    with charachange

    mi "Как насчёт… ох…"

    "Миша смотрит поверх плеча Эми, я следую за её взглядом."

    "Под столом, свернувшись калачиком, спит Рин."

    mi "Что ж, ты уверена?"

    show emi basic_hes at twoleft
    with charachange
    #Emi hesitant

    emi "Мне кажется… сейчас самое время учиться."
    
    show misha perky_smile at tworight
    with charachange

    mi "Ладно, пойдём проверим?"

    hi "Эй, куда вы собрались?"
    
    show emi basic_closedgrin at twoleft
    show misha cross_grin at tworight
    with charachange

    mi "Это секрет."

    "Миша подмигивает мне, ещё больше меня смущая."
    
    show misha cross_smile at tworight
    with charachange

    mi "Придёт день, когда я и тебя научу, Хисао."
    
    stop music fadeout 4.0
    
    hide misha
    hide emi
    with charaexit

    "Миша с Эми растворяются в темноте коридора, их шаги затихают вдали."
    
    show lilly invis at tworight
    with None
    
    show bg school_council_ni at center
    show lilly basic_weaksmile at center
    with dissolvecharamove

    li "И их осталось двое…"

    hi "Да уж, надо бы закругляться."

    hi "Начну-ка я тут прибираться."

    "Я засучиваю рукава и начинаю собирать разбросанные по комнате пустые банки и пакеты из-под еды."
    
    show lilly basic_listen
    with charachange

    li "О том… о чём мы говорили раньше…"

    hi "А?"
    
    show lilly basic_concerned
    with charachange

    li "Неужели ты думаешь, что… с Ханако и правда так обращались?"

    hi "Честно говоря, я не знаю."
    
    show lilly basic_sad
    with charachange
    #Lilly sad
    
    play music music_moonlight fadein 4.0

    li "Я знаю её с самого её появления здесь…"

    li "Я старалась за ней ухаживать, помочь ей завести друзей…"
    
    show lilly basic_oops
    with charachange

    li "Я делала что-то не так?"

    li "Но стоило мне прекратить вмешиваться в её жизнь, как вы начали встречаться."

    hi "Вмешиваться?"
    
    show lilly basic_displeased
    with charachange

    "Лилли в расстройстве заламывает себе руки."

    "Печально видеть её такой несчастной."
    
    show lilly behind_displeased
    with charachange

    li "Я…"

    extend " хотела свести вас вместе."

    li "Это было глупо с моей стороны, я знаю. Но то, что она счастлива, делает и меня чуточку счастливее."
    
    show lilly basic_reminisce
    with charachange

    li "Поэтому, как только она заговорила с тобой, я решила сделать всё возможное, чтобы вы были вместе."

    li "Но у меня ничего не получалось… И снова… И снова…"

    show lilly basic_oops
    with charachange
    #It would be so easy to chuck a pityfuck here
    #but I won't

    li "А потом я заболела, и вы начали встречаться."

    li "Неужели я не нужна?"

    li "Неужели я всё это время была только в тягость?"

    "По щекам Лилли бегут слёзы, по мере того как она всё больше и больше занимается самобичеванием."

    "Распитие спиртного – не самая лучшая прелюдия для такого рода беседы."
    
    show lilly basic_concerned_close
    with charachange

    "Я обнимаю её, и она продолжает плакать, уткнувшись мне в грудь."

    hi "Всё совсем не так."

    hi "Ты – лучшая подруга Ханако, это любой тебе скажет."

    hi "Порой мне кажется, что она любит тебя больше, чем меня."

    hi "То, что сказала сегодня Миша, – это просто теория."

    hi "И, кроме того, даже если это правда, ты не её мачеха."

    hi "Ты никогда не делала ничего, что могло бы принести ей боль, верно?"
    
    show lilly basic_pout_close
    with charachange

    li "Верно."

    hi "Тогда и волноваться не о чем, верно?"
    
    show lilly basic_reminisce_close
    with charachange

    li "Верно."

    hi "Что ж, давай наведём тут порядок."

    hi "Завтра утром мы с Ханако поедем ко мне домой, и я не хочу оставлять после себя такой беспорядок."
    
    show lilly basic_listen_close
    with charachange

    li "Хорошо…"
    
    stop music fadeout 6.0
    
    show lilly basic_sad
    with charachange

    "Лилли отстраняется от меня и начинает нащупывать ближайший стол, чтобы прибраться на нём."

    hi "С тобой всё будет в порядке?"
    
    show lilly basic_weaksmile
    with charachange
    li "Ну, я могу сортировать пустые блюда от не пустых…"

    hi "Я имею в виду во время нашего отъезда, без нас?"
    
    show lilly basic_smile
    with charachange
    #Lilly smile

    li "Конечно, у меня уже есть некоторые планы."

    li "Моя старшая сестра сейчас в Японии, так что мы собираемся съездить в летний домик в Хоккайдо."

    #Something just occurred to me. Wouldn't a home in Hokkaido be a *winter* house?
    #Oosaka, Fukuoka or Okinawa are more summer destinations, right?

    hi "Звучит здорово."
    
    show lilly basic_planned
    with charachange

    li "Так и есть. Я хочу как-нибудь пригласить вас туда."

    hi "Я был бы рад. Может, на следующих каникулах?"
    
    show lilly basic_smile
    with charachange

    li "Может."

    "Так, слово за слово, мы наводим в комнате порядок."
    
    play music music_daily fadein 6.0

    "И, точно по мановению волшебной палочки, три спящие красавицы просыпаются."
    
    show hanako emb_timid at closeright
    show rin basic_absent at closeleft2
    with charaenter

    ha "Что… случилось?"

    hi "Ты вырубилась. Снова."
    
    show hanako emb_downtimid at closeright
    with charachange

    ha "Ох… Прости."

    hi "Да всё нормально."
    
    show hanako basic_worry at closeright
    with charachange

    ha "А кто тут такой порядок навёл?"

    hi "Мы с Лилли."
    
    show rin basic_deadpanamused at closeleft2
    with charachange

    rin "А я руководила."
    
    show hanako basic_normal at closeright
    show lilly basic_pout
    with charachange

    hi "Разве ты не спала только что?"
    
    show rin basic_deadpansurprised at closeleft2
    with charachange

    rin "Да, просто у вас так хорошо получалось, что я решила не мешаться под ногами."
    
    show rin relaxed_doubt at closeleft2
    with charachange

    rin "А где Эми?"

    hi "А, Миша хотела ей что-то показать… или типа того."
    
    show rin basic_awayabsent at closeleft2
    with charachange

    rin "Ну ладно. А я так хотела те руки…"
    
    show hanako cover_worry at closeright
    with charachange

    ha "Те руки?"
    
    show rin basic_absent at closeleft2
    with charachange

    rin "Волшебные механические ноги Эми."

    rin "Нам почти удалось их приладить."
    
    show hanako emb_timid at closeright
    with charachange
    #Hanako puzzled.

    ha "Понятия не имею, о чём она говорит."

    hi "Это долгая история, я расскажу тебе завтра в поезде."
    
    show hanako cover_distant at closeright
    with charachange

    ha "Ах, точно, поезд…"
    
    show shizu invis at offscreenright
    with None
    
    show bg school_council_ni at bgleft
    show rin basic_absent at left
    show lilly basic_pout at twoleft
    show hanako cover_distant at center
    show shizu behind_blank at right
    with dissolvecharamove

    shi "…"

    "Вот блин. Всё это время за нашим разговором следила %(name_shizune)s."

    "Но без Миши нет никакой возможности наладить с ней общение."

    "А вечеринка уничтожила всё, что позволило бы ей изложить свои мысли на бумаге."
    
    show shizu basic_normal at right
    with charachange
    
    with Pause(0.2)
    
    show shizu behind_smile at right
    with charachange
    
    show shizu invis at offscreenright
    with dissolvecharamove

    "После ряда безрезультатных попыток что-то донести до нас жестами (я уверен, что она была уверена, что понять их довольно просто), %(name_shizune)s улыбается, кланяется и уходит."

    hide shizu
    with None
    
    show bg school_council_ni at center
    show rin basic_absent at closeleft2
    show lilly basic_smile at center
    show hanako cover_distant at closeright
    with dissolvecharamove
    
    hi "Я думаю, она сказала «спасибо»."
    
    show rin basic_deadpanamused at closeleft2
    with charachange

    rin "Должно быть, она бросила нам вызов."
    
    show lilly basic_oops
    show hanako emb_timid at closeright
    with charachange

    hi "Что?"
    
    show rin basic_awayabsent at closeleft2
    with charachange

    rin "Ты никогда не узнаешь."
    
    show rin relaxed_sleepy at closeleft2
    with charachange

    rin "Я хочу спать. Спокойной ночи."
    
    show rin invis at offscreenleft
    with dissolvecharamove

    "Рин разворачивается на каблуках, наклоняется вперёд и направляется к выходу из кабинета Совета."
    
    hide rin
    with None
    
    show bg school_council_ni at bgleft
    show lilly basic_smile at twoleft
    show hanako emb_downtimid at tworight
    with dissolvecharamove

    hi "Что ж, нам тоже стоит поспать."
    
    show hanako emb_smile at tworight
    with charachange

    ha "Хм…"

    ha "Знаешь, я ведь просто уснула, так что…"
    
    show hanako emb_smile_close at twocenteroff3
    with charachange

    "Ханако подходит ко мне и хватает за рубашку."
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Может, мне оставить вас наедине?"

    hi "Т… тебе точно не нужна помощь, чтобы вернуться в свою комнату?"
    
    show lilly behind_cheerful at twoleft
    with charachange

    li "У меня есть трость, так что я вполне в состоянии найти дорогу обратно."
    
    show hanako basic_smile_close at twocenteroff3
    with charachange

    ha "Я уже отнесла свои сумки в твою комнату, Хисао."

    hi "Да? Когда?"

    ha "Перед экзаменами."

    hi "Ну, хорошо…"
    
    show hanako basic_bashful_close at twocenteroff3
    with charachange

    ha "Так чего же мы ждём?"
    
    show lilly basic_smile at twoleft
    with charachange

    li "Не буду вас задерживать…"

    hi "М… ладно…"

    hi "Спасибо за пунш, Лилли."
    
    show lilly basic_ara at twoleft
    with charachange

    li "Не за что."
    
    stop music fadeout 3.0

    "Ханако практически всю дорогу до моей комнаты тянет меня за рубашку."
    
    scene black
    with dissolve

    return

label ru_HT17:

    #This may end up being the last scene in the True arc.
    #Can't say for sure, depends on how wordy I get in the train.
    #Also, if the "chat" at Hanako's old house is going to be conclusive enough.
    #Anyway, a conclusion is what I am aiming for.
    #Also, the "Playlist" name for this sence would be "I'm Here".
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    
    play ambient sfx_trainint fadein 2.0
    
    scene bg city_trainscenery
    show train_scenery 
    show train_scenery_fg
    show evfg hisao_trainride at Motion(trainwave, 4.0, repeat=True, bounce=True)
    with locationchange
    #BG Train window.
    
    "Поезд размеренно покачивается. Ханако положила голову мне на плечо."

    "После вчерашней вечеринки мы оба чувствуем себя не лучшим образом."

    "Во рту сухо и мерзко, а каждый гудок локомотива отдаётся болью в висках."

    "Я лезу в карман за ещё одной таблеткой обезболивающего и запиваю её глотком холодного чая."
    
    play sound sfx_trainchime

    "Поезд начинает останавливаться, и из громкоговорителей доносится голос:"

    #I'm not sure about the direct reference here, but I guess that all of the "Tokyo"s can be
    #removed easily.

    "Диктор" "Поезд пребывает на конечную станцию – Токио."

    "Диктор" "Убедительно просим вас не забывать свои вещи."

    "Я слегка толкаю Ханако, чтобы разбудить её."

    #Show Hanako tired

    hi "Эй, Ханако, мы уже приехали."

    ha "Ну ещё пять минуточек…"

    hi "Не думаю, что это возможно."

    "Ханако протирает глаза и оглядывается по сторонам, вспоминая, где она и что тут делает."

    ha "Мы уже на месте?"

    hi "Ты проспала примерно два часа…"

    ha "Ой… Прости."

    hi "Как ты себя чувствуешь?"

    ha "Лучше. Голова прошла, разве что я немного устала."

    "Не важно, насколько вам кто-то нравится, но даже небольшая головная боль может заставить вас его возненавидеть."
    
    stop ambient fadeout 3.0

    hi "Ну и хорошо. Давай я помогу тебе с сумками."
        
    #"The train slows to a stop and the doors slide open."
    
    show city_tokyostation at bgright
    show crowd
    with shorttimeskip
    
    hide train_scenery
    hide train_scenery_fg
    hide evfg hisao_trainride
    hide city_tokyostation
    show bg city_tokyostation at bgright
    with None
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    play ambient sfx_crowd_outdoors fadein 0.5

    "Перед нами раскинулся сложный лабиринт платформ и эскалаторов станции Токио."

    "Стада людей передвигаются туда-обратно по заранее установленным маршрутам."
    
    show hanako emb_timid_cas
    with charaenter
    #Hanako concerned

    hi "С тобой здесь всё будет нормально?"
    
    ha "Да… я в порядке."

    "Ханако крепко сжимает обеими руками ручки сумки, костяшки её пальцев аж побелели от напряжения."

    hi "Позволь мне взять это."
    
    show hanako def_worry_cas
    with charachange

    ha "А?"

    "Я протягиваю руку, пытаясь взять у неё сумку."

    ha "Всё нормально, я понесу…"
    
    ha "Она не очень тяжёлая."

    hi "Как скажешь. Позволь мне хотя бы за одну ручку взяться."
    
    show hanako emb_smile_cas
    with charachange
    #Hanako embarrassed

    "После краткого раздумья Ханако берётся за левую ручку, протягивая мне правую."

    "Я беру её, и мы направляемся к другой платформе."
    
    $ renpy.music.set_volume(0.3, 1.0, channel='ambient')
    
    scene bg city_subway
    show crowd at centersit
    with locationskip

    ha "Сколько нам ещё ехать?"

    hi "Ну, на электричке примерно час, а потом ещё немного на автобусе…"

    hi "Чуть более часа."

    ha "Эх… Ну ладно."
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')

    scene bg city_trainstation
    show crowd
    with locationskip

    "Мы входим в другое помещение станции, и нас тут же сметает человеческий поток."

    "Ханако крепко вцепляется в мою руку, и мы проталкиваемся через скопление народу к нашей платформе."

    #BG platform-city

    #"The line to my parent's house isn't as busy as the inner-city lines, and Hanako relaxes a little."

    hi "Ты как, держишься?"
    
    show hanako emb_timid_cas
    with charachange
    #Hanako not embarrassed but not happy.

    ha "Да… Ещё держусь."

    ha "Никто не обращает на нас внимания."

    hi "Это потому, что кругом люди, люди."

    hi "И никто никого не замечает. Я говорил тебе, что всё будет в порядке."
    
    stop ambient fadeout 3.0

    ha "О, это наш поезд?"
    
    hi "Да, это он. Давай попробуем занять места получше."
    
    #scene bg city_trainscenerycity
    play ambient sfx_trainint fadein 5.0
    
    scene black
    show train_scenery2
    show train_scenery_fg
    show evfg hisao_trainride2 at Motion(trainwave, 4.0, repeat=True, bounce=True)
    with locationskip

    #Bg train window 2

    "Застроенная центральная часть города остаётся позади, и наш поезд въезжает в пригород."

    "Ханако снова начинает дремать, оставив меня один на один с моей головной болью."
    
    stop ambient fadeout 3.0

    "Слава богу, она начинает проходить. Впрочем, возможно, благодарить за это стоит уже четвёртую за сегодня таблетку от головы."
    
    show city_houseext
    show hanako emb_timid_cas at tworight
    with shorttimeskip
    
    hide train_scenery2
    hide train_scenery_fg
    hide evfg hisao_trainride2
    hide city_houseext
    show hanako emb_timid_cas
    show bg city_houseext behind hanako
    with None
    
    $ renpy.music.set_volume(0.1, 0.0, channel='ambient')    
    play ambient sfx_traffic fadein 2.0
    play music music_daily fadein 2.0

    "Мы без каких-либо проблем добрались до автобуса и теперь стоим перед домом моих родителей."

    #BG houseX outside

    hi "Вот мы и дома."
    
    show hanako basic_smile_cas
    with charachange

    ha "Выглядит… миленько."

    hi "Отнюдь, зато функциональненько."

    hi "Дом был достаточно просторным для нас и относительно недалеко от города."
    
    show hanako emb_timid_cas
    with charachange

    ha "Я не это имела в виду."
    
    show hanako emb_downtimid_cas
    with charachange

    ha "Это прекрасно, когда есть куда возвращаться."

    hi "Ой, прости… Я не хотел…"
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "Всё в порядке."

    hi "Ну что, пойдём, что ли."

    "Я извлекаю из недр кармана старый ключ и отпираю дверь."
    
    stop ambient fadeout 1.0
    
    play sound sfx_dooropen
    
    scene bg city_houseint
    with locationchange

    #BG random house interior.

    hi "Я дома…"

    "В ответ тишина."

    "В доме никого."

    "Мы входим внутрь и сваливаем наши сумки в гостиной."

    "На кофейном столике я замечаю записку."

    #Sorry delta, I forgot how to declare notes

    $ written_note(u"Привет, Хисао. Спасибо, что приехал.\nПрости, но мы не можем вернуться домой раньше обеда.\nУвидимся.\n\nЦелуем.\nМама и папа.")

    #RAGE

    hi "Хех, похоже, что у нас есть время привести себя в порядок."
    
    show hanako basic_worry_cas
    with charachange

    ha "Ох."

    "Мы обмениваемся неловкими взглядами."

    hi "Знаешь, мы могли бы…"
    
    show hanako emb_blushtimid_cas
    with charachange
    #Hanako Embarrassed

    ha "Не здесь!"

    ha "Я ещё даже не познакомилась с твоими родителями!"

    ha "К тому же…"
    
    show hanako emb_blushing_cas
    with charachange

    ha "Я до сих пор неважно себя чувствую."

    hi "Эх."

    hi "Зато честно."

    "Если честно, я не уверен, что моя голова выдержит один раунд с Ханако."

    "За сплошной стеной обезболивающих я чувствую пульсирующее биение похмелья."

    hi "Итак, куда пойдём?"

    hi "Может, в город вернёмся?"
    
    show hanako cover_smile_cas
    with charachange

    ha "Да, хорошо."

    hi "Я знаю там одно местечко, оно должно тебе понравиться."
    
    show hanako basic_bashful_cas
    with charachange

    ha "Отлично. Веди…"
    
    #stop music fadeout 5.0

    #I dunno, maybe this next bit should be NVL?
    
    #I'll take up your offer, crud. Saves me some serious headaches with yet another train interior shot- Alphabro
    
    "Я беру Ханако за руку, и мы идём на автобусную остановку."
    
    scene bg city_busstat
    with shorttimeskip
    
    window hide

    nvl show dissolve

    n "После того как мы сменили автобус на поезд, нам, кажется, достаточно просто держаться за руки."

    n "\n«Хисао, я думала, что поезд в город идёт в другом направлении.»"

    n "«А мы и не направляемся в центр города, мы едем… кое-куда ещё.»"

    #Hanako curious

    n "«Серьёзно? Куда же?»"

    n "«Это секрет.»"

    n "«Ну скажи!»"

    n "«Нет. Ты всё сама увидишь, когда мы туда доберёмся.»"

    n "«Отлично! Я тогда тоже не буду с тобой разговаривать.»"

    n "\n\nВерная своему слову, Ханако в поезде так и не проронила больше ни слова."

    n "Она не нарушает свой обет всю дорогу, что мы идём к небольшой пригородной станции примерно в часе ходьбы от города."
    
    nvl hide dissolve

    nvl clear
        
    window show

    #BG suburb station
    
    stop music fadeout 5.0
    
    show hanako def_worry_cas
    with charachange

    ha "Это же…"

    hi "Да."
    
    show hanako basic_worry_cas
    with charachange

    ha "Как ты узнал?"

    hi "Лилли разыскала это для меня."

    ha "Как она?.."

    hi "Мы искали в газетах. Знаешь ли ты, что у газет есть электронные версии в интернете?"

    hi "Подобное случается довольно редко, ты знаешь?"
    
    show hanako emb_downtimid_cas
    with charachange

    #Hanako sad
    
    play music music_drama

    ha "Даже знать не хочу."

    hi "Почему?"
    
    show hanako emb_sad_cas
    with charachange

    ha "Я сказала, что не хочу. Пойдём обратно."

    hi "Нет."

    hi "Ты ведь ни разу сюда не возвращалась, да?"

    hi "Я знаю дорогу только досюда, а дальше уже ты меня поведёшь."
    
    show hanako emb_downsad_cas
    with charachange
    #Hanako Crying

    ha "Я не хочу!"

    hi "Ну, я не собираюсь принуждать тебя, однако думаю, что нам стоит хотя бы войти туда."

    hi "Ты не можешь избегать этого вечно…"
    
    show hanako emb_downtimid_cas
    with charachange

    ha "Почему бы и нет?"

    hi "Потому что ты прячешься."

    hi "Ты старательно делаешь вид, будто ничего не произошло, но это не так."

    hi "Ты надеешься всегда прятаться от того, что здесь произошло?"
    
    show hanako cover_worry_cas
    with charachange

    ha "Но…"

    hi "Что «но»?"

    hi "Случившегося уже не изменить."

    hi "Но, если ты и дальше будешь игнорировать это, оно так и будет съедать тебя изнутри."

    hi "Ты действительно этого хочешь?"
    
    show hanako emb_downtimid_cas
    with charachange

    #At this stage, I'm not sure if this is going as well as I had planned.

    "Ханако не отвечает, просто молча качает головой."

    #"I check my frustration, and try to take on a milder tone." -c'mon, that just makes Hisao seem more like a dick. I had to comment it out.

    hi "Подумай, я ведь здесь исключительно ради тебя. Если захочешь, мы сядем на следующий же поезд, вернёмся домой и забудем об этом."

    hi "Но мы проделали весь этот длинный путь… Так почему бы не сделать этот последний шаг?"
    
    show hanako emb_timid_cas
    with charachange

    "Я протягиваю руку в заливающейся слезами Ханако, она растерянно на меня смотрит."

    "На мгновение меня посещает мысль, что, возможно, это была не самая лучшая идея."
    
    show hanako cover_worry_cas
    with charachange

    "Но в тот момент, когда я уже собираюсь пойти обратно на перрон, Ханако берёт меня за руку."

    ha "Ты обещаешь, что пойдёшь со мной?"

    hi "Конечно."

    ha "Несмотря ни на что?"

    hi "Даже если ты попытаешься сбежать от меня."
    
    show hanako basic_worry_cas
    with charachange

    ha "Хо…"

    extend " хорошо."

    ha "Нам сюда… Наверное…"

    "Ханако нерешительно направляется к выходу из здания вокзала на главную улицу."
    
    scene bg city_street4
    with locationskip

    "Провинциальный городок, кажется, целиком состоит из невысоких домов, каждый – с небольшим двориком."

    "Местные жители – интеллигенция, променявшая некоторое увеличение времени на дорогу на некоторое увеличение жизненного пространства."

    "Но и тут чувствуется влияние урбанизации."

    "По мере того как мы удаляемся от станции, всё чаще начинают встречаться многоквартирные дома."
    
    scene bg city_alley
    with locationchange

    "Мы сворачиваем на главную улицу, и отдельностоящие дома становятся редкостью."

    "Вскоре мы оказываемся в окружении одних только многоквартирных домов."
    
    scene bg city_apartment
    with locationchange
    
    stop music fadeout 8.0

    "Спустя некоторое время Ханако останавливается перед одним помнящим лучшие времена домом."

    "Он выглядит более старым, чем остальные окружающие его строения."
    
    show hanako cover_worry_cas_close at right
    with charaenter

    ha "Это… Это здесь…"

    ha "Здесь я и жила…"

    "Так может выглядеть любой другой дом в мире."

    "Перед ним – небольшой дворик, посреди которого находится несколько почтовых ящиков, а вокруг них валяются брошенные игрушки."
    
    show hanako emb_downtimid_cas at right
    with charachange
    
    show bg city_apartment at bgleft
    show hanako emb_downtimid_cas at tworightsit
    with dissolvecharamove
    
    #show hanako emb_downtimid_cas at tworightsit
    #with charamove
    
    play music music_innocence fadein 4.0

    "Ханако проходит в калитку и опускается на колени."

    ha "Он был здесь."

    ha "Входная дверь была прямо здесь."
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    "Она смотрит так, будто перед её глазами стоит призрак старого дома."

    ha "Я думаю, что здесь они меня и нашли."
    
    show hanako emb_timid_cas at tworight
    with charamove
    show hanako emb_timid_cas at center
    with charamove

    "Она поднимается и делает насколько шагов по воображаемому дому."

    ha "А здесь… здесь умер мой отец."

    hi "Это невероятно…"

    hi "Подумать только, он был так близко…"
    
    show hanako emb_downsad_cas
    with charachange

    ha "Они сказали мне, что мать осталась внутри; у неё не было ни малейшего шанса."

    ha "А отец подхватил меня… и убедился, что я снаружи."

    ha "Так близко…"
    
    play sound sfx_whiteout
    
    scene ev hanako_park_alone 
    with whiteout

    "Ханако падает на колени и начинает плакать."
    
    show ev hanako_park_away 
    with charachange

    "Я становлюсь на колени рядом и обнимаю её за плечи."

    "И снова я поражаюсь – казалось бы, какие-то два шага всего…"

    "Здесь умер её отец, а там, в метре от меня, Ханако выжила."

    "Мы преодолели это расстояние меньше чем за секунду."

    #"I bend down next to Hanako, and she throws her arms around me."
    
    show ev hanako_park_closed
    with charachange

    "Она что-то беззвучно шепчет мне на ухо, и я крепко её обнимаю."

    hi "Прости, мне не стоило заставлять тебя приходить сюда сегодня."
    
    show ev hanako_park_look 
    with charachange

    ha "Нет… Перестань."

    ha "Мне жаль, что я не пришла сюда раньше."

    "Ханако отстраняется и вытирает опухшие от слёз глаза."

    hi "Правда? Почему?"
    
    show ev hanako_park_closed
    with charachange

    ha "У меня никогда не было возможности поблагодарить своего отца."

    ha "Он мог спастись сам, но вместо этого он выбросил на улицу меня."
    
    ha "Все эти годы…"
    
    show ev hanako_park_away 
    with charachange

    ha "Я винила его."

    ha "За то, что я попала в приёмную семью, за мою приёмную мать, за то, что я прошла через всё это…"
    
    ha "Я думала: «Почему ты просто не дал мне умереть?»"
    
    show ev hanako_park_look
    with charachange

    ha "Но… это не то, чего он хотел."

    ha "Он хотел, чтобы я жила."

    ha "Он знал, что выживу либо я, либо он. И он выбрал меня."

    #Hanako resolute
    
    play sound sfx_whiteout
    
    scene ev hanako_resolute #white
    with charachange #dissolve

    "Ханако встаёт, и я встаю вместе с ней."

    "Она внезапно откидывает голову назад и кричит."

    ha "Спасибо!"

    #Hanako smile

    "Я никогда ранее не слышал, чтобы она так громко говорила; она широко улыбается."
    
    scene bg city_apartment at bgleft
    show hanako basic_bashful_cas
    with locationchange

    "Она медленно поворачивает голову в мою сторону, всё ещё улыбаясь."
    
    ha "Спасибо, Хисао."

    #Geh, this feels far to quick and "lol end of story nao" for me.

    ha "Думаю, без тебя я застряла бы здесь навсегда."

    hi "Не благодари, я же заставил тебя приехать сюда…"
    
    show hanako emb_timid_cas
    with charachange

    ha "Я не это имела в виду."
    
    show hanako emb_downtimid_cas
    with charachange

    ha "Я рассматривала это как предлог, позволявший мне не двигаться дальше."
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "Но я не могла делать это вечно."
    
    show hanako emb_timid_cas
    with locationchange

    ha "Я никогда не забуду то, что здесь произошло, но я не хочу, чтобы это и дальше тянуло меня назад."

    ha "Но… Я не могу сделать это в одиночку."

    #So tempted to quote Retake here…
    
    show hanako basic_worry_cas
    with charachange

    ha "Хисао… ты поможешь мне?"

    ha "Пообещаешь, что всегда будешь со мной?"

    hi "Да… Я обеща…"
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    "Ханако прерывает меня посреди фразы долгим и страстным поцелуем."
    
    scene bg city_apartment at bgleft
    show hanako basic_bashful_cas_close
    with locationchange

    ha "Вот, теперь обещание скреплено поцелуем."

    "Житель" "Эй, вы двое, что вы там делаете?"

    "Незнакомый человек стоит рядом с почтовым ящиком, глядя на нас с подозрением."
    
    show hanako emb_smile_cas
    with charachange

    hi "Ну, мы… э…"

    ha "Я жила здесь раньше и хотела показать это место своему парню."

    "Житель" "О чём ты говоришь?"

    "Житель" "Я переехал сюда, ещё когда это здание только построили, и не помню, чтобы вообще вас тут видел."
    
    show hanako cover_bashful_cas
    with charachange

    ha "А, что ж, наверное, я ошиблась."

    hi "Мы пойдём, извините за беспокойство."
    
    stop music fadeout 4.0

    "Житель" "Ага, если я ещё раз вас здесь увижу – вызову полицию."
    
    show hanako basic_smile_cas
    with charachange

    ha "Не волнуйтесь, мы уже сделали то, зачем приходили."
    
    "Житель" "Идите уже отсюда…"
    
    show bg city_busstat
    show hanako emb_downsmile_cas_close at tworight
    with shorttimeskip

    #BG Train station
    play music music_twinkle

    "Мы с Ханако ожидаем поезда на пустынной станции, положив головы друг на друга."

    hi "Ты точно в порядке?"
    
    show hanako emb_timid_cas_close at tworight
    with charachange

    ha "Да, спасибо, всё хорошо."
    
    hi "Ну, что теперь?"

    ha "Я думаю…"

    extend " я хочу познакомиться с твоими родителями."

    #hi "Really?"

    #ha "Really."

    #ha "I have some news that they might want to hear."

    #hi "Oh, and what would that be?"

    #ha "I'm late."

    #Lol baby end.
    #Game over.

    #Well, maybe. This is a bit of a Lol ending 'cause I want to ask advice from y'all.

    return

label ru_end_hanakogood:
    # Hanako good end, after HT17
    scene black with dissolve
    centered "~ ханако, хорошая концовка ~" with dissolve
    return