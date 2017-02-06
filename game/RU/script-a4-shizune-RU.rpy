label ru_S31:

    window hide None
    
    scene black 
    with dissolve
    centered "~ Хисао ~"
    with dissolve
    
    play ambient sfx_businterior fadein 0.5
    
    #play music music_moon fadein 2.2
    scene black
    with Dissolve(3.0)
    
    scene bg city_busride_ss 
    with locationchange
    
    window show dissolve
    
    "Я узнал о случившемся из электронного письма %(name_shizune)s, пришедшего на мой мобильный телефон. Я даже не заметил его до без малого пяти часов вечера."

    "Есть у меня такая вредная привычка: я часто (иногда несколько дней подряд) забываю проверять и заряжать телефон."

    "Поэтому я узнал о несчастье только спустя почти шесть часов."
    
    stop ambient fadeout 1.5 

    scene bg hosp_ext_ss
    with shorttimeskipsilent
    
    $ renpy.music.set_volume(0.7, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.2

    "К тому времени, как я добрался до больницы, было уже слишком поздно."
    
    $ renpy.music.set_volume(0.2, 1.0, channel='ambient')
    scene bg hosp_hallway 
    with locationchange
        
    "«%(name_shiina)s Микадо», значит? Немного странно, что я до сих пор не знал твоего полного имени."

    "Я довольно паршивый друг."

    "Впоследствии меня попросили ответить на некоторые вопросы полиции о Мише. Они собирались классифицировать случившееся как самоубийство."

    "Но это невозможно. Когда я видел её в последний раз, она выглядела такой счастливой."

    "Если только и это не было ложью."

    "И всё же я отказывался в это поверить. Я сказал им, что я в это не верю. На самом деле это не отрицание. Просто я абсолютно уверен, что они ошиблись."

    "Несмотря на…"

    "Миша, я сумел хотя бы в этот раз защитить тебя. Надеюсь, я всё сделал правильно."

    "Прости."

    stop ambient fadeout 1.5
    "…"
    
    #stop ambient fadeout 1.0
    
    #scene bg city_funeral
    #Lets try how this looks like, shall we? - Kelper
    #Also, this one confuses me. Should we show him while still in the graveyard/funeral? He talks about it in past tense. - Kelper
    $ renpy.music.set_volume(0.8, 0.0, channel='ambient')
    play ambient sfx_park fadein 1.0
    scene bg city_graveyard
    with shorttimeskipsilent
    
    #$ renpy.music.set_volume(0.2, 0.0, channel='ambient') 
    
    #play ambient sfx_crowd_indoors fadein 0.2

    "На похоронах было удивительно мало народу."

    "В последующие дни мне удалось найти этому объяснение. Понемногу. Я должен был это сделать."

    "Сейчас ведь лето, как-никак. И, несмотря на общительность Миши, в действительности она мало кого подпускала к себе. Думаю, по-настоящему хорошо её знали лишь %(name_shizune)s, я и Юко."

    "И всё же это удручает."

    "Не уверен даже, были ли там её родители."
    
    stop ambient fadeout 1.0
    
    #Felt like the depressing music should stop here -md01
    #stop music fadeout 7.0
    
    scene bg school_dormhisao 
    with shorttimeskipsilent
    
    $ renpy.music.set_volume(0.2, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.5
    "И я не видел %(name_shizune)s с того дня."
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound') 
    play sound sfx_hammer
    
    $ renpy.pause(0.5)    
    
    #The next few lines were originally written like this. I changed them up so they flow better with some scene direction -md01
    #"A knock at the door takes me out of my reminescing. I'm grateful to whoever it is for that. Without thinking, I open the door. It's Hideaki. He has a bag on the floor next to him that he picks up when he sees me."
    
    "Стук в дверь прерывает мои воспоминания. Кто бы это ни был, я благодарен ему за это. Не раздумывая, я открываю дверь."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    scene bg school_dormhallway
    show hideaki normal 
    with Dissolve(1.0)
    play music music_night fadein 5.0
    $ renpy.music.set_volume(0.0, 6.0, channel='ambient')  
    show hideaki normal at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with charamove
    
    show hideaki normal at center
    with charamove
    
    "Это %(name_hideaki)s. Рядом с ним на полу стоит сумка, которую он подбирает, увидев меня."

    hh "Доброе утро."

    hi "Ага…"

    "Это его обычное приветствие, но тон изменился. Я довольно ясно чувствую, что это пустая формальность. Странно видеть его лишённым своей обычной энергичности."

    "Я благодарен ему. Именно он занимался организацией похорон."

    hh "Как ты держишься?"

    "Трудный вопрос. Что я должен сказать? Как мне следует ответить? Не думаю, что адекватный ответ вообще возможен."

    hi "Нормально."

    hh "Ясно."
    
    show hideaki serious
    with charachange

    hh "А как %(name_shizune)s?"

    hi "Мы не общались некоторое время."
    
    show hideaki normal
    with charachange

    hh "Ясно. Не желаешь сейчас её навестить? Я здесь именно за этим. Подумал, что, наверное, её не помешало бы подбодрить."
    
    show hideaki normal_up 
    with charachange

    hh "У меня… это не очень-то получается. Если ты мне поможешь, буду признателен. К тому же, я уверен, она будет рада тебя видеть."
    
    show hideaki serious_up
    with charachange

    hh "А ещё я немного боюсь идти к ней в одиночку. Если там будешь ты, это слегка снизит напряжение. И, очевидно, ты мне нужен в качестве переводчика."
    
    show hideaki serious
    with charachange

    hh "Мы можем отправиться, как только ты будешь готов."
    
    hi "Думаешь, %(name_shizune)s в состоянии сейчас принимать посетителей? В последний раз, когда я её видел, она выглядела довольно подавлено."

    "На самом деле это ещё мягко сказано."
    
    #Experimenting with this placement, now it's gonna play as soon as you open the door. - Kelper
    #play music music_night fadein 5.0
    
    show hideaki normal
    with charachange

    hi "Поэтому…"
    
    show hideaki sad 
    with charachange

    hh "Ты прав."
    
    hh "…"

    hh "Знаешь, почему именно я организовывал похороны Микадо?"
    
    show hideaki thinking
    with Dissolve(1.0)

    "Он делает паузу. Не знаю, ожидает ли он ответа или нет."
    
    show hideaki normal
    with Dissolve(1.0)

    hh "Было бы логичнее, если бы это сделала %(name_shizune)s. Очевидно."

    hh "Однако после всего случившегося кажется, что %(name_shizune)s решила прекратить всякую деятельность, даже мыслительную."

    hh "Это странно."

    "Думаю, %(name_hideaki)s никогда раньше не видел %(name_shizune)s такой."
    
    show hideaki serious_up 
    with charachange

    hh "Я хочу подбодрить её. А ты?"

    "Это довольно упрощённый взгляд на вещи. Всё не так просто. Хотя для него вполне логично говорить такое. В конце концов, он брат %(name_shizune)s."

    "А %(name_shizune)s всегда поступает так, будто любые препятствия, возникшие на пути, можно с лёгкостью смести, если как следует постараться. Если ты проявишь упорство, сможешь всё преодолеть. Думаю, в этом заключалась суть её мировоззрения."

    "Я всё ещё не могу полностью поверить в это. Однако в этот раз, как и всегда, я соглашусь. Просто потому, что я всегда хотел верить во что-то в таком роде."

    hi "Тогда пойдём прямо сейчас."
    
    #Trying this background - Kelper
    #scene bg school_dormext_full 
    scene bg misc_sky at Fullpan(20.0)
    with fade

    "Снаружи всё так, словно ничего не изменилось. Довольно ярко светит солнце. И я в любую минуту ожидаю, что Миша набросится на меня сзади и закроет ладонями мои глаза."
    
    scene black
    with shuteye
    
    scene bg school_dormext_full_fb
    show noiseoverlay
    with flashback_slow
    
    $ renpy.pause(1.0)
    
    #Not sure of the hands in/out are a good idea here. -md01
    scene black 
    #I modified the hand thing, it was just too fast. New definition on line 1369, in ui_settings - Kelper
    with hands_inslow
    
    mi "Сюрприз~! Угадай кто~!"

    "…"
    
    #scene bg school_dormext_full_fb
    #with hands_out
    
    scene bg school_dormext_full with Dissolve(1.0)
    #with flashback_slow

    "Эх, это случалось столько раз, что у меня вошло в привычку быть начеку. Полагаю, теперь можно расслабиться, так?"

    "Мои глаза начинает пощипывать."
    
    show hideaki serious
    with charaenter

    hh "Ты в порядке?"

    "Из-за меня нам приходится ненадолго остановиться."
    $ renpy.music.set_volume(0.5, 2.0, channel='ambient')
    stop music fadeout 3.6
    
    scene bg school_girlsdormhall 
    with locationskip
    
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound') 
    play sound sfx_hammer
    
    "%(name_hideaki)s рефлекторно стучит в дверь %(name_shizune)s, прежде чем попробовать повернуть ручку. Дверь не заперта."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    
    $ renpy.music.set_volume(0.3, 0.5, channel='ambient') 
     
    scene bg school_dormshizune at left
    with locationchange

    "Я впервые в комнате %(name_shizune)s. Обстановка довольно аскетичная и прагматичная, хотя то тут, то там я всё же замечаю черты, присущие её индивидуальности."

    "На своём столе она всё ещё хранит плюшевую кошку, что я тогда выиграл для неё."
    
    #show shizu behind_blank at tworight
    #show hideaki serious at twoleft 
    #with charaenter
    #show shizu behind_sad at Position(xpos=0.9, ypos=1.1) with charachange
    
    #I think this is a better cue for this music, it's weird to play a dramatic song over the room's description - Kelper
    
    stop ambient fadeout 3.0
    show shizu basic_normal2 #at tworight
    #with charachange
    with Dissolve(1.2)
    #with Pause(0.5)
    play music music_moon fadein 0.5
   
    "Когда я подхожу достаточно близко, %(name_shizune)s поднимает взгляд, а затем быстро отворачивается."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    "Она сидит на кровати спиной к стене. Рядом коробка с книгами, которую она прижимает к себе."

    "Её лицо лишено эмоций, но я замечаю красноватые следы вокруг глаз."

    "Видеть её такой – это и вправду зрелище не из приятных."
    
    scene bg school_dormshizune at center
    show shizu basic_normal2 at tworight
    with dissolvecharamove
    
    show hideaki serious at twoleft
    with charaenter
    
    hh "Хисао, пожалуйста, не мог бы ты переводить ей то, что я говорю?"
    
    

    "Мне не хватает духу сказать ему, что она даже не смотрит в мою сторону. Впрочем, я попытаюсь. Если потребуется, я снова и снова буду становиться прямо перед тобой, %(name_shizune)s."
    
    show hideaki happy at twoleft 
    with charachange

    hh "Привет, %(name_shizune)s."

    hh "У тебя всё в порядке?"

    shi "…"
    
    show shizu behind_blank at tworight
    with charachange

    "Взгляд %(name_shizune)s не фокусируется на нас, а устремлён куда-то вдаль. Она кивает, словно признавая наше присутствие, однако не поднимает рук, чтобы поприветствовать меня."

    hi "Привет, %(name_shizune)s."

    shi "…"

    "Она не двигается. На самом деле кажется, что чем ближе мы подходим, тем меньше она становится."
    
    show hideaki happy_up at twoleft
    with charachange

    hh "У меня для тебя подарок. Ноутбук. Я специально выбрал слегка устаревшую модель, поскольку знаю, что тебе нравятся старомодные вещи."

    hh "С его помощью мы можем поговорить."
    
    show shizu basic_normal2 at tworight
    with charachange

    shi "…"
    
    show hideaki sad at twoleft 
    with charachange

    hh "Ты не хочешь говорить со мной?"

    "Руки %(name_shizune)s всё так же безвольно свисают вдоль тела, даже когда %(name_hideaki)s ставит перед ней ноутбук."
    
    show hideaki serious at twoleft 
    with charachange

    hh "%(name_shizune)s, могу ли я хоть что-нибудь для тебя сделать?"

    shi "…"

    "Хотя я лишь перевожу слова %(name_hideaki)s, надеюсь, %(name_shizune)s понимает, что я говорю от имени нас обоих. К несчастью, похоже, она нарочно избегает смотреть на кого-либо из нас."
    
    show hideaki serious_up at twoleft
    with charachange

    hh "Я проделал такой путь, чтобы тебя увидеть. Пожалуйста… сделай что-нибудь. Можешь хотя бы взглянуть на меня?"
    
    show hideaki sad at twoleft 
    with charachange

    hh "Почему ты не отвечаешь? Мне… как бы не всё равно."
    
    show hideaki thinking at twoleft
    with charachange
    
    hh "…"
    
    show hideaki sad at twoleft
    with charachange

    hh "Ладно, если ты этого хочешь, я вполне понимаю. Зайду как-нибудь в другой раз."
    
    show hideaki invis at Position(xpos=0.2) with dissolvecharamove
    
    $ renpy.pause(0.7)
    
    play sound sfx_doorclose
    $ renpy.pause(0.6)
    hide hideaki
    scene bg school_dormshizune at center
    show shizu basic_normal2
    with dissolvecharamove

    "После ухода %(name_hideaki)s я сам пытаюсь добиться от неё ответа. Или хотя бы взгляда."
    
    "Примерно с тем же успехом."

    "Что я делаю? Прямо сейчас я не могу ничего сделать."

    hi "Я вернусь, когда тебе станет лучше, хорошо?"
    
    scene bg school_girlsdormhall with locationchange
    
    stop music fadeout 7.0

    "Как только я выхожу, начинаю сожалеть, что не смог сделать для неё хоть что-то. Совершенно не смог её подбодрить. На самом деле я не смог сделать вообще ничего."
    
    window hide dissolve    
    
    scene black 
    with Dissolve(1.5)
    
    return

label ru_S32:

    #After the scene after this scene, the path splits into good and bad ends

    # I will probably rewrite this scene.
    $ renpy.music.set_volume(0.3, 0.0, channel='ambient')  
    play ambient sfx_rooftop fadein 0.5
    scene bg school_dormhisao with dissolve
    
    window show dissolve

    "Сегодня я собираюсь вновь навестить %(name_shizune)s."

    "Последние несколько дней я только и делал, что хандрил. Меня ни на секунду не покидала мысль о том, как выглядела %(name_shizune)s в тот день."

    "Полагаю, кто-то пытается мне сказать, что нельзя просто оставить всё как есть. Я хотел сделать больше. Я мог сделать больше. Так или иначе, я должен был быть рядом с ней."

    "Я мог даже обнять её. Хотя, возможно, это было бы чересчур сентиментально. Я ведь не какой-то там герой."

    "Я не особо умею разрешать такие ситуации. И прямо сейчас мне правда не помешала бы твоя помощь, Миша. Конечно, это невозможно."

    "Обувшись, я снова направляюсь в комнату %(name_shizune)s."
    
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')  
    scene bg school_girlsdormhall with locationskip

    "Стоя перед дверью, я замираю. Мне немного страшно. Она может снова не посмотреть на меня, и в этом случае я не знаю, смогу ли хоть что-то сделать. А если посмотрит, то не уверен, что смогу выдержать её взгляд."

    "Её глаза всегда были такими тёмными, пронзающими насквозь, они отражали её сущность. Как они выглядят сейчас?"

    "По правде говоря, я был здесь уже трижды с тех пор, как мы приходили сюда с %(name_hideaki)s."

    "В первый раз она не отвечала, что бы я ни делал. Следующие два раза дверь была заперта."

    "Заперта ли она и сегодня?"

    "%(name_shizune)s, если ты собираешься так закрыться от меня, я себе этого не прощу."

    "Я поворачиваю дверную ручку, полный необъяснимого трепета. Дверь открывается."
    
    play sound sfx_dooropen
    
    $ renpy.pause(1.3)
    
    #I feel like there should be a CG for this scene. -md01
    $ renpy.music.set_volume(0.3, 0.5, channel='ambient') 
    scene bg school_dormshizune
    show shizu behind_blank
    with locationchange
    
    #This track was set before I started. Is this a fucking joke? -md01
    #play music music_cellosolo fadein 0.2

    hi "Привет, %(name_shizune)s."

    shi "…"

    hi "Тебе лучше?"

    "Мне хочется ударить себя за то, как ужасно это звучит. Что за идиотская фраза."

    "Твоя дверь снова открыта. Не ты ли говорила мне, что ничего не делаешь просто так? Говорила, и не раз. Оставила ли ты дверь открытой, потому что хотела поговорить?"

    "Если это так, ответь мне, хотя бы разок."

    hi "Пожалуйста, %(name_shizune)s. Я включу ноутбук. Ты сможешь напечатать то, что хочешь сказать, но, прошу тебя, скажи хоть что-нибудь."

    "Я знаю, что, наверное, половину жестов я переврал, но уверен, что она всё поняла."

    "Я нажимаю на кнопку питания компьютера и наблюдаю, как он тихо оживает перед ней."

    hi "Вот так. Это займёт всего пару секунд. Можем мы просто поговорить? Хоть немного?"

    hi "Я беспокоюсь о тебе. Поэтому я здесь. Так что, пожалуйста, поговори со мной."

    "Поначалу я уже почти готов сдаться. В конце концов, я общаюсь с ней уже достаточно долго и знаю, что её воля сильнее моих самых смелых догадок. А это значит, что если она не хочет говорить, то всё так и будет."

    "Впрочем, как и всегда."
    
    show shizu basic_normal2
    with charachange

    "Затем, как ни странно, она пододвигает ноутбук к себе и начинает печатать. Через несколько секунд она всё стирает и начинает жестикулировать."
    
    stop ambient fadeout 3.0    
    play music music_sadness fadein 3.0
    
    show shizu behind_sad
    with charachange

    ssh "Знаешь, что это?"
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient') 
    "%(name_shizune)s вытаскивает книгу из лежащей рядом коробки. В тот раз она тоже лежала здесь. Я беру книгу и изучаю её. Кажется, это обычный белый блокнот, хотя и довольно потрёпанный."

    "Я пролистываю его. Каждая страница заполнена надписями, сделанными крупным детским почерком, а также множеством рисунков."

    ssh "Это записи Миши."

    "Её дрожащие, почти безжизненные руки формируют слова."

    ssh "Прочти их."

    "Невежливо вот так читать личные дневники умерших, разве нет?"
    
    show shizu basic_angry
    with charachange

    ssh "Они собирались выбросить всё из её комнаты. И я нашла это."
    
    show shizu behind_sad
    with charachange

    ssh "Всё это время я ничего не знала. Но знаешь, отчего мне больнее всего?"

    "Она пролистывает одну из записей, а затем указывает на строку, нацарапанную внизу страницы."

    window hide dissolve
    play sound sfx_rustling
    $fixedwritten_note((u"Хотела бы я по-настоящему поговорить с ") + (name_sicchan) + (u"."))
    window show dissolve
    "Прежде чем я успеваю осознать это, она перелистывает чуть дальше и указывает на другую строку."
    window hide dissolve
    play sound sfx_rustling
    $fixedwritten_note((name_sicchan) + (u", я бы хотела разговаривать с тобой свободнее."))

    play sound sfx_rustling
    $fixedwritten_note(u"Хотела бы я лучше выразить ей свои чувства.")

    play sound sfx_rustling
    $fixedwritten_note(u"Они оба такие счастливые. Иногда мне трудно продолжать смеяться.")

    play sound sfx_rustling
    $fixedwritten_note((u"Интересно, любит ли меня ") + (name_sicchan) + (u"?"))

    window show dissolve
    "…"

    hi "О чём ты? У тебя не было никакой возможности узнать, что всё так серьёзно. И в любом случае ты бы не смогла ничего сделать…"
    
    show shizu basic_normal2 with charachange

    ssh "Перестань жестикулировать. Это необязательно."

    "Что это значит?"
    
    #I really wanted to pause the track and resume it below, but it appears that renpy can't do that, so here is this
    #stop music fadeout 0.5
    #$renpy.music.set_volume(0.0, delay=1.0, channel='music')
    #This doesn't work though, completely cuts the mood off. I'm not sure what you wanted to achieve here - Kelper
    
    ssh "Я лгала."

    #Again, is this a fucking joke? This doesn't fit AT ALL! -md01
    #When ever I hear this track I think of Kenji going on about feminists with a moon base.
    #play music music_tension fadein 0.2
    
    ssh "Есть поговорка, что многие отношения построены на лжи. В моём случае таковы все отношения."
    
    show shizu behind_sad with charachange

    shi "…"

    ssh "Миша могла говорить со мной как с нормальной девушкой."

    ssh "Я умею читать по губам."

    "Мои мысли обрываются, я не могу в это поверить."
    
    #stop music fadeout 0.2

    hi "Правда?"
    
    show shizu basic_normal
    with charachange

    "Я произношу это слово, и мне почему-то трудно поднять руки. %(name_shizune)s кивает головой."

    ssh "Ты единственный, кто знает об этом."

    "Я хочу сесть, но практически не чувствую ног. Упаду ли я, если хотя бы слегка пошевелюсь? И, если упаду, как она это истолкует? Ведь ничто не ускользает от взгляда этих глаз."
    
    #Music comes back in after dramtic pause
    #play music music_hanako fadein 2.0
    
    #$renpy.music.set_volume(1.0, delay=5.0, channel='music')
    
    ssh "Ты начал мне нравиться из-за тех вещей, что ты говорил мне."
    
    #I love how inexplicable this sprite choice is. Why is she angry? Works great even if it was unintended. I'll be sad if this goes to make place for a CG. - Kelper
    show shizu behind_frown with charachange

    ssh "Я глухая. Очень весело насмехаться над глухим, он ведь не может ничего услышать. Даже если стоит прямо перед тобой, он ничего не поймёт."
    
    show shizu adjust_frown
    with charachange

    ssh "Это ведь так увлекательно, правда?"

    "На мгновение она теряет бдительность. Даже в такое время, в таком состоянии, %(name_shizune)s никогда до конца не убирала стену вокруг себя, но прямо сейчас мне удалось увидеть её прошлое."

    "Я так мало о тебе знаю. Теперь я понимаю это."

    "Твои жесты полны горечи и печали."

    "Как у человека, ощутившего всё это на собственном опыте."
    
    show shizu basic_normal2
    with charachange

    ssh "Ты ни разу не сказал про меня ничего плохого, хотя и мог. Именно тогда ты начал мне нравиться."

    ssh "Ты говорил со мной, даже когда не должен был. И я полюбила тебя."

    ssh "А ещё я люблю тебя за то, что ты захотел выучить язык жестов ради меня. Здесь ты превзошёл мои ожидания, и я была удивлена."
    
    show shizu behind_smile with charachange

    "Вспомнив об этом, она слабо улыбается."
    
    show shizu behind_sad
    with charachange

    ssh "Мне следовало признаться тебе. Но, как ты знаешь, я всегда настороже. И я боялась. Долгое время я водила тебя за нос. Миша написала, что хотела мне помочь. И она помогла."

    ssh "Я коварная и лживая женщина."
    #Hahah - Kelper
    
    show shizu basic_angry
    with charachange

    ssh "А ещё эгоистка."
    
    #show shizu behind_frown
    #with charachange

    ssh "Я даже ревновала, так как думала, что она может нравиться тебе больше, чем я."
    
    #show shizu behind_blank
    #with charachange
    
    show shizu basic_normal2
    with charachange

    ssh "Миша так много для меня сделала. Иногда я задаюсь вопросом: принимала ли я всё это как должное? У меня не очень получается выражать эмоции."
    
    #show shizu basic_normal2
    #with charachange

    ssh "Мне всё ещё не очень хорошо удаётся читать эмоции людей, да? Иначе я предвидела бы всё это."

    ssh "Если бы она сейчас была здесь, я бы сказала, как сильно я люблю её как друга. Мне жаль."
    
    show shizu behind_sad with charachange

    ssh "Мне очень жаль."

    "В уголках её глаз появляются слёзы. Она изо всех сил пытается сдержать их, но я не уверен, что в этот раз ей хватит самообладания."

    "Голова %(name_shizune)s опущена, словно в ожидании какой-то божьей кары. Вероятно, именно таковы её ощущения."

    ssh "Ты меня ненавидишь?"
    
    stop music fadeout 8.0
    $renpy.music.set_volume(0.5, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 8.0
    "Сейчас я даже не могу осознать, что только что произошло. Я в оцепенении от шока. Я никак не мог знать об этом, но, оглядываясь назад, многое встаёт на свои места."

    "Ты была права: ты ничего не делаешь без причины. Теперь я понимаю. Именно таким образом тебе удаётся так энергично и бесстрашно взаимодействовать с окружающим миром. Но в то же время ты бываешь такой осторожной и терпеливой."


    "Меня всегда интересовало, как такая двойственность уживается в одном человеке."

    "А ещё меня слегка задело, что ты играла со мной таким образом."

    "Тем не менее я всё ещё люблю тебя."

    "Даже если я чувствую себя опустошённым, как сдувшийся шарик."

    "Но это просто от шока. Даже если сейчас мне словно нечем дышать, это пройдёт…"

    #Doesn't it sound better here? - Kelper
    stop ambient fadeout 1.0
    hi "Нет."
    play music music_friendship fadein 3.0
    show shizu behind_blank with charachange

    "Странно разговаривать с %(name_shizune)s голосом. Незнакомое ощущение."
    $renpy.music.set_volume(1.0, 0.0, channel='ambient')
    #WTF is with this track? Was it the "we need different music for this, so here's a placeholder" track? -md01
    #play music music_cellosolo fadein 0.2
    
    #play music music_friendship fadein 1.0

    ssh "Тебе безразлично, что я лгала?"

    "Не то чтобы безразлично, просто я пока не знаю, как реагировать. Мне понадобится время. Время, чтобы во всём разобраться. Время, которого сейчас у меня нет, так как она выжидающе смотрит на меня, пытаясь прочитать что-нибудь по лицу."

    "Неужели ты так сильно погрязла во лжи, что решила, что никогда не сможешь рассказать правду?"

    "Но теперь ты настолько опротивела самой себе, что смогла-таки мне всё рассказать?"

    "И ты хочешь, чтобы я ненавидел тебя?"

    "Терпеть не могу, когда приходится так пристально рассматривать каждое действие %(name_shizune)s. Я не телепат, но иногда мне кажется, что она хочет, чтобы я напряжённо пытался понять её мысли. Но так было всегда, правда? Просто временами больше обычного."

    "Но, по крайней мере, ты рассказала мне."

    hi "Эй, ты ведь впредь будешь честна со мной? Ты мне очень нравишься, даже несмотря на всё это. И поэтому мне неприятно видеть тебя такой."

    hi "Разве ты не собиралась стать полезным членом общества? Это твои слова, не так ли? А если так, тогда прекрати так себя вести. Уверен, она бы тоже не хотела, чтобы ты зациклилась на этом навечно."

    hi "Ты никоим образом не могла всего этого знать. Теперь уже слишком поздно, однако это не повод… так бичевать себя. В этом всё дело?"

    hi "Если ты так на это смотришь, тогда да. Мне всё равно, что ты лгала."

    hi "Итак, ты понимаешь меня, да? Это хорошо. Я могу разговаривать с тобой, как я всегда мечтал."

    hi "Ладно?"
    
    show shizu basic_normal2
    with charachange

    "Она не выглядит убеждённой."

    hi "Я выучил язык жестов, потому что хотел разговаривать с тобой. Теперь я могу это делать. Но это не было пустой тратой времени. Мне ведь всё равно нужно понимать твои ответы. К тому же это неплохо для дальнейшего поступления в колледж."

    "Я улыбаюсь в надежде на ответную улыбку."
    
    show shizu basic_angry with charachange

    "%(name_shizune)s смотрит вниз на свои руки, покручивая большими пальцами, а затем отвечает."
    
    ssh "Ты чересчур понимающий."

    hi "Это потому, что я люблю тебя."
    
    show shizu behind_frustrated
    with charachange

    ssh "Не будь идиотом. Прошу, уходи."

    hi "Нет."
    
    show shizu cross_angry_close with characlose

    "%(name_shizune)s поднимается на ноги и направляется ко мне. Она собирается вытолкнуть меня за дверь?"

    "Я стою на месте, а она всё приближается."
    
    
    show shizu behind_sad_close with charachange
    play sound sfx_pillow
    with vpunch

    "Она останавливается и прислоняется головой к моей груди, словно она слишком устала, чтобы снова поднять её. Секунду я опасаюсь, что она упадёт, но она прижимается ко мне, обняв меня за плечи. Её слёзы орошают мою рубашку."

    "Я обнимаю её в ответ."

    "Ты впервые зависишь от меня. Это значит, что теперь на моих плечах довольно большая ответственность, не так ли?"

    "Мне больно оттого, что ты лгала. Однако я не стану из-за этого делать глупости. Я… теперь твоя опора, верно?"

    "А ты так же поддерживаешь меня."

    "Меня это устраивает."

    stop music fadeout 5.0
    "В прошлом я соответствовал твоим ожиданиям, так? В этот раз я снова превзойду их."
    window hide dissolve
    #I don't dislike this fade to white but it's too long and makes it seem the game has ended (?), fade to white is used in very very very few instances, let alone one as long as this one - Kelper. 
    #scene white with Dissolve(5.0)
    scene black with Dissolve(1.5)
    
    #Great scene all in all, really - Kelper
    return

label ru_S33:

    #After this, path splits into good and bad ends
    
    #Lets try some stuff - Kelper
    #scene bg school_dormhisao with Dissolve(2.0)
    scene black with dissolve
    #window show dissolve

    #This wasn't originally part of the NVL. I'm gonna take Alphabro's advice and use NVL as a direction tool. - Kelper
    #"I have time now to think about yesterday."
    
    play music music_rain fadein 1.5
    
    #window hide dissolve
    
    nvl show dissolve

    n "Сейчас у меня есть время, чтобы обдумать вчерашние события."
    
    n "Перед %(name_shizune)s мне удалось сделать вид, что всё в порядке, и поддержать её. Но сейчас я один, и я не могу не думать о тех вещах, что она говорила."

    n "Несмотря на то что она обманула меня, я не могу заставить себя сердиться на неё."

    n "Ты действительно водила меня за нос, ожидая, когда я первым приглашу тебя на свидание."

    n "Даже если и так, думаю, я всегда ощущал, что всё так и было. На самом деле, когда Миша спросила меня, нравишься ли ты мне или нет, у меня было чувство, что это ты подговорила её. Но такое поведение не является чем-то уникальным."

    n "Может, всё было не совсем так, однако такая возможность постоянно маячила на краю моего сознания. Поэтому я не сильно удивлён."

    n "Что же касается другого…"

    nvl clear

    n "Интересно, как долго ты притворялась, что не умеешь читать по губам."

    n "Об этом я тоже несколько раз подозревал, когда замечал небольшие перемены выражения твоего лица в ответ на фразы, которые ты никак не могла слышать."

    n "Эй… Однажды ты даже сказала мне заткнуться. Я правда должен был догадаться."

    n "…"

    # 1) If you cheated on Shizune with Misha, this should appear

    if seen_scene("S25h"):

        n "Так или иначе, я изменил тебе. Учитывая это, интересно, хватит ли у меня когда-нибудь воли обижаться на тебя, считая, что твоя ложь была хуже моей."

    # end detour

    n "Даже сейчас я не могу избавиться от чувства тоски, поселившегося во мне после случившегося с Мишей несчастья. Стало только хуже, потому что я со вчерашнего дня читаю её дневник."

    n "Я довольно быстро читаю. Поэтому уже добрался до того периода в её жизни, где появляюсь я."
    
    nvl hide dissolve
    nvl clear
    
    #window hide

    play sound sfx_rustling
    $fixedwritten_note((u"Сегодня в нашей школе появился новый ученик. Его зовут Хисао Накай. Буду называть его ") + (name_hicchan) + (u"~! Когда у всех есть прозвища, жить веселее."))

    play sound sfx_rustling
    $fixedwritten_note((name_sicchan) + (u", я сделаю всё, чтобы вы с ") + (name_hicchan) + (u"ом смогли быть вместе. Меньшее было бы полным эгоизмом. Счастье ") + (name_hicchan) + (u"а и ") + (name_sicchan) + (u" важнее моего. Если мои друзья будут счастливы, я тоже буду."))

    play sound sfx_rustling
    $fixedwritten_note((u"Мне всё равно, если ") + (name_hicchan) + (u" заменит меня в сердце ") + (name_sicchan) + (u". Может быть, там вообще никогда не было места для меня."))
    
    nvl show dissolve

    n "Удалось ли %(name_shizune)s дочитать до этого места?"

    n "Вот ещё одна причина, почему следует уважать личные вещи усопших."

    n "В ответ на предположение, что несчастный случай мог быть... преднамеренным, я высказался довольно резко."

    n "Я не хотел допускать эту возможность. И сейчас не допускаю. Но чем дальше я читаю, тем больше начинаю сомневаться."

    n "Я был неправ?"

    n "Я скучаю по тебе, Миша. Я не знаю, что делать и даже что думать. К тому же %(name_shizune)s изменилась с тех пор, как ты ушла. Она винит себя. Она ненавидит себя. Значит, может быть, она думает, что это было самоубийство."

    n "Если это правда, почему я ничего не замечал? Она ведь была очень подавлена. Мне следовало об этом подумать."

    n "И всё же ты выглядела такой счастливой."

    n "В данный момент я ненавижу все мысли в своём сознании. Хотел бы я на время просто перестать думать. Хоть ненадолго. Но, как бы сильно я ни хотел этого, облегчение не наступает."

    n "Возможно, мне следует прогуляться, подышать свежим воздухом и прочистить голову."
    
    nvl hide Dissolve(1.5)
    
    #I think this looks better now. The black background gives the scene.. something. What do you think? - Kelper
    
    scene bg school_gardens3 with Dissolve(2.0)
    with Pause(1.0)
    #Originally written like this -md01
    #"I head outside and start walking around the school perimeter, with no real place to go in mind. Circling around once, I stop at the front gate. I could always go to town, but I feel apprehensive about the idea somehow."

    window show dissolve
    "Я выхожу наружу и, не придумав, куда бы можно было пойти, начинаю обходить школу вокруг."
    
    scene bg school_gate with locationchange
    
    "Сделав круг, я останавливаюсь перед главными воротами. Всегда можно пойти в город, но этот вариант почему-то вызывает тревогу."

    "Наверное, сегодня там слишком людно…"

    "А мне нужно тихое место, чтобы подумать."
    
    scene bg school_lobby with locationskip

    "Во время летних каникул самое безлюдное место на школьной территории – сама школа."

    "Я захожу внутрь и начинаю блуждать по пустым коридорам, однако быстро становится очевидно, что прийти сюда было ошибкой. Все двери заперты, включая дверь в комнату Школьного совета, которую я проверил первой."
    
    stop music fadeout 5.0
    
    #Lets see what the night filter does to make the library look dark, but with some sunlight -md01
    #Tested. Night filter looks like crap. I guess I'll stick with the normal library pics for now. -md01
    #Thank god for Sapiens. - Kelper
    
    $renpy.music.set_volume(0.2, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.5 
    scene bg school_librarynolights with shorttimeskipsilent
    #Clock sound annoyed me - Kelper
    
    "Открыта лишь библиотека."

    "Начав свой путь среди книжных полок, я пару раз спотыкаюсь о стопки книг, разбросанные то тут, то там. Сегодня тут необычный беспорядок."
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound') 
    play sound sfx_footsteps_hard
    with Pause(2.2)
    #If you do this, then the lower volume doesn't work - Kelper
    #$ renpy.music.set_volume(1.0, 0.0, channel='sound') 
    
    show yuuko smile_down_nl with charaenter
    
    #I'm never good with song choices. How does this sound to you?. I thought it needed something not too overly dramatic. Nocturne is always my to-go song. - Kelper
    play music music_night fadein 1.0
    stop ambient fadeout 3.5
    "Услышав сзади шаги, я оборачиваюсь и вижу, что на меня смотрит Юко."
    
    yu "Добро пожаловать!{w=0.2} …В—{w=0.3}{nw}"
    $ renpy.transition (charachange, layer='master')
    show yuuko panic_down_nl
    extend "—библиотеку?{w=0.2}{nw}"
    $ renpy.transition (charachange, layer='master')
    show yuuko panic_up_nl
    extend " Ох, это ты."
    #I like that little effect. Text tags are pretty useful - Kelper
        
    $ renpy.music.set_volume(1.0, 0.0, channel='sound') 
    
    yu "Мне жаль. Мне очень жаль. Привет, Хисао."

    "Она только что перепутала свои работы? Это даже немного меня развеселило."

    hi "Привет, Юко. Что ты здесь делаешь?"
    
    show yuuko worried_down_nl with charachange

    yu "Я ведь библиотекарь?"
    
    "Юко инстинктивно напрягается."

    show yuuko neurotic_up_nl with charachange
    yu "…Или я больше не библиотекарь? Я… Мне нужна эта работа."

    #Can i chalk up for the light in bg school_library as being natural sunlight? I don't think Hisao would have mentioned the lights if it wasn't dark in there.
    #Maybe I'll get an anon to photoshop a picture of the library with the lights off, but with the sun coming in? -md01
    #Meh. Changed the line because fuck the lights. They're not important. -md01
    hi "Я знаю, просто свет выключен и это место казалось безлюдным."
    
    #hi "I know, it's just that it's the middle of the summer, and the place seemed empty."
    
    show yuuko worried_up_nl with charachange
    
    #play music music_kenji fadein 1.0
    #Kenji music doesn't belong here. I know, I know. But still. - Kelper
    
    yu "Э, вообще-то всё… непросто. Кто-то крадёт отсюда много книг, и всё бы ничего, пока он крал книги, которые у нас более чем в трёх экземплярах, однако…"

    yu "Кто бы это ни был, в последнее время он стал наглеть и, ох, э… красть книги… которые у нас в единственном экземпляре. А я хотела прочесть некоторые из них… вот… Поэтому теперь это личное."

    hi "Понятно."

    yu "Я не уйду, пока не поймаю его."
    
    #This doesn't look good to me. - Kelper
    #show yuuko neurotic_down_nl with charachange

    "Высказав всё это, она краснеет, и мне приходится убедиться, что моё выражение лица нельзя истолковать превратно. Если она решит, что я насмехаюсь над ней, то может расстроиться."
    
    show yuuko neutral_down_nl with charachange

    yu "А что ты здесь делаешь, Хисао?"

    hi "Я просто хотел отвлечься от некоторых мыслей."
    
    show yuuko worried_down_nl with charachange
    
    #stop music fadeout 2.0

    yu "Ох."

    "Судя по выражению её лица, полагаю, что она знает, от каких именно."

    "Юко была одной из немногих, кто присутствовал на похоронах. В противном случае, думаю, мне было бы труднее так свободно говорить с ней сейчас. Немного странно быть связанным таким событием…"
    
    #No, wait. Too dramatic - Kelper
    #play music music_sadness fadein 1.0

    hi "Да. Хотя и не только о Мише. Я беспокоюсь о %(name_shizune)s."

    hi "В последнее время, похоже, ей нездоровится."
    
    show yuuko worried_up_nl
    with charachange

    yu "Из-за…"

    hi "Да, довольно очевидно, что из-за этого. Я не знаю, что она может сделать. В смысле, как она отреагирует на случившееся. Думаю, я и представить не мог, что %(name_shizune)s будет настолько подавленной."

    hi "Хотя я могу это понять. Это действительно нечто такое… Это непросто."

    #She is later said to be smiling. - Kelper
    show yuuko neutral_up_nl with charachange
    
    yu "Конечно."

    "Её голос настолько тих, что я едва слышу его. Разговаривать об этом весьма неловко. Избегать упоминания имени Миши, словно это лишь подчеркнёт тот факт, что её больше нет. Не за этим я сюда пришёл."

    "После вчерашнего разговора с %(name_shizune)s мне пришла в голову одна мысль, и я не желаю к ней возвращаться."

    "%(name_shizune)s."

    "Никогда в жизни я не чувствовал себя настолько потерянным."

    hi "Эй, Юко."
    
label ru_choiceS33a:
    menu:
        with menueffect
 
        hi "%(name_shizune)s…"
 
        "{font=playtime_cyr2.ttf}Рассказать Юко об умении %(name_shizune)s читать по губам.{/font}":
            return m1
           
        "{font=playtime_cyr2.ttf}Не рассказывать.{/font}":
            return m2

    #UNUSED TEXT FOR A CHOICE I DELETED
    #IT'S JUST BEEN REVOKED! -md01

    label ru_S33a:    
    
    "Полагаю, ей можно рассказать."

    hi "Я рад, что ты мой друг. Я рад это слышать. Но сейчас важнее то, что… Ты также и друг %(name_shizune)s, правда?"
    
    show yuuko worried_down_nl
    with charachange

    "Юко выглядит озадаченной."

    hi "Извини. Просто я очень старался убедить %(name_shizune)s, что не ненавижу её. Но не уверен, что у меня это получилось. Я не уверен, что она верит мне так, как мне бы хотелось. Я не лгал, но это не имеет значения, если она не поверит."

    hi "Итак, возможно, она всё же думает, что я её ненавижу. И я беспокоюсь о том, что она может сделать, если так думает."

    "А что она сделает? Всякое возможно."

    "В конце концов, это %(name_shizune)s."

    hi "Полагаю, я хотел бы узнать, не будешь ли ты обижаться на неё за то, о чём я расскажу?"

    "Дурацкий вопрос. Явно дурацкий вопрос. Она ведь даже не знает, что я собираюсь рассказать, и я не знаю, как она отреагирует. Это не такой уж и незначительный секрет."

    "Я смотрю на Юко внимательнее."

    "Она не отвечает, но, учитывая её характер, сомневаюсь, что она будет злиться на %(name_shizune)s. Может быть, она даже отнесётся ко всему с пониманием."

    hi "Похоже, %(name_shizune)s умеет читать по губам."

    "Я боюсь взглянуть на неё. Ха, я боюсь Юко – это немыслимо."

    yu "Правда?.."
    
    show yuuko worried_up_nl
    with charachange
    
    #This line here did not have a character code on it. I can only assume it's said by Yuuko. -md01
    yu "Э… И как давно она это умеет?"

    hi "Некоторое время."
    
    show yuuko worried_down_nl
    with charachange

    yu "Ой…"

    #I broke and changed up this line so it'll flow better with direction.
    #I'm also not happy with Yuuko's sprites for this. None of them have a "hysterical laughter" quality to them -md01
    #"I start feeling as though I've made a terrible mistake, until Yuuko breaks out into laughter."
    
    "Я начинаю думать, что совершил ужасную ошибку..."
    
    show yuuko closedhappy_up_nl
    with charachange
    
    "...пока Юко не разражается смехом."
    
    show yuuko happy_down_nl
    with charachange

    yu "Прости. Прости меня. Просто я вспомнила, что наговорила %(name_shizune)s кучу всякого, потому что мне было нужно… выговориться, и я подумала, что она не может – э, не могла – меня слышать и мне не будет стыдно."
    
    show yuuko neutral_down_nl
    with charachange

    yu "А теперь, узнав обо всём, я вспоминаю, что говорила, и это…"
    
    show yuuko neurotic_up_nl
    with charachange

    "Она краснеет, однако снова смеётся, на этот раз слегка нервно, но в то же время она кажется счастливой."
    
    "Сделав паузу, Юко добавляет..."
    
    show yuuko neutral_up_nl
    with charachange

    yu "Нам как-нибудь стоит всем вместе сходить куда-нибудь."

    #CHanged and moved this line to before the previous one. -md01
    #"She says, after a pause."

    hi "Ага…"
    
    show yuuko neutral_down_nl
    with charachange

    yu "Уверена, с %(name_shizune)s всё будет в порядке. Если мне позволено это сказать."

    yu "То, о чём ты рассказал, только подтверждает её доверие к тебе. Иначе ты ничего бы не узнал."

    "Правда? Она выглядела так, что вряд ли рассказала всё из доверия."

    label ru_S33b:
    #2) Don't tell her

    "Я чувствую, что было бы неправильно разглашать нечто, что %(name_shizune)s было настолько сложно мне рассказать."

    "И, если из-за меня Юко будет по-другому относиться к %(name_shizune)s, я себе этого не прощу."

    hi "Неважно."

    show yuuko worried_down_nl with charachange
    
    "Она неуверенно улыбается."
    
    yu "Ладно…."
    
    show yuuko neutral_up_nl
    with charachange
    
    "Юко смотрит вниз, собираясь с мыслями."

    yu "А… вы с %(name_shizune)s пара, так ведь?"

    hi "Ага…"
    
    show yuuko neutral_nl
    with charachange

    yu "Они всегда были вместе. Иногда казалось, будто они – две половинки одной личности, и я всегда думала…."

    yu "Вполне понятно, каково ей сейчас. Я понимаю."

    hi "Всё не так просто."

    hi "Она очень упрямая. Думаю, ты знаешь об этом не хуже меня. Мне это нравится, потому что иногда это очень мило. Но сейчас это только мешает. Это похоже на какую-то стену, я практически вижу её."

    hi "И…"
    
    label ru_S33c:
    #UNUSED SCENE SPLIT FROM DELETED CHOICE
    #lolnope - md01

    hi "Хочешь узнать, чего я опасаюсь?"
    
    show yuuko panic_down_nl with charachange

    "По проблеску страха в глазах Юко я понимаю, что она беспокоится о том же, а также что она не хочет вдаваться в детали. Я тоже не хочу."
    
    show yuuko worried_down_nl
    with charachange

    "В библиотеке тишина. Тревожная тишина. Через какое-то время я слышу вздох Юко, и он кажется настолько громким, что я едва не вздрагиваю."

    hi "Я не знаю, что ещё можно для неё сделать, помимо того, чтобы просто быть рядом."

    hi "Даже если и так, что это значит? Просто стоять там и говорить с ней? О чём? И какая от этого будет польза? Мне нужно сделать нечто большее. И %(name_shizune)s тоже это нужно."

    hi "Думаю, что… в этот раз моих сил может не хватить."
    
    show yuuko worried_up_nl
    with charachange

    yu "Ты ведь не собираешься сдаться, не так ли?"
    
    #stop music fadeout 2.0

    hi "Сдаться?"

    "Меня слегка раздражают эти слова."

    hi "Нет, конечно нет. Я не знаю, что делать, однако не собираюсь просто ждать. %(name_shizune)s бы так не поступила. У оставшихся в живых тоже есть обязанности. Есть долг."

    hi "То, что она сейчас делает, неправильно, и это меня бесит."

    hi "Миши больше нет."
    
    show yuuko panic_up_nl with charachange

    "Юко заметно вздрагивает от моих слов и выглядит так, словно сейчас разрыдается. В этот момент и я едва держусь."
    
    show yuuko worried_down_nl
    with charachange

    hi "Ей не следует из-за этого так себя вести. Я лишь боюсь, что, если скажу это ей, она огрызнётся, что я не подхожу для таких разговоров. И это правда. Не подхожу."

    hi "…Какое-то время я полагал, что было бы неплохо просто перестать о ней думать, потому что мне не хотелось с этим разбираться. Я довольно паршивый друг, не так ли? %(name_shizune)s была бы права: у такого человека нет никаких прав указывать ей, что чувствовать."

    "Я чувствую опустошение."

    "Не знаю, ненавидит ли меня теперь Юко, но если это так, она здорово это скрывает."
    
    show yuuko happy_down_nl with charachange

    yu "Думаю… определённые воспоминания важно сохранить."
    
    show yuuko neurotic_up_nl with charachange
    
    yu "И ещё, все мы совершаем ошибки. Важно то… э… чему мы можем на них научиться и как мы их исправим."
    
    "Она густо краснеет и закрывает лицо руками."

    hi "Это похоже на фразу из фильма."
    
    show yuuko worried_up_nl with charachange

    yu "Правда? Прости."

    hi "Хорошая фраза."
    
    show yuuko worried_down_nl with charachange

    yu "Я… на самом деле там её и слышала…"

    hi "Хе-хе."

    "Однако в этом есть смысл."
    
label ru_choiceS33b:
menu:
    with menueffect
    
    "Следует ли мне навестить %(name_shizune)s, или пусть отдыхает?"
    
    "{font=playtime_cyr2.ttf}Сейчас ей нужен отдых, не стоит её тревожить.{/font}":
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        window hide dissolve
        scene black with Dissolve(1.5)
        return m1
        
    "{font=playtime_cyr2.ttf}Мне нужно проведать её.{/font}":
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        window hide dissolve
        scene black with Dissolve(1.5)
        return m2
    
label ru_S34:
    #This scene is hella short. So short the whole thing might as well be in NVL mode.
    #Yeah that's right a scene with absolutely no sprites or anything
    
    scene bg school_dormhisao_blurred
    show phone mobile at center 
    with Dissolve(2.0)
    
    #So, this is a problem. Nocturne fits, but it fits in the other scene too, and I think better. Ill try daylight. - Kelper 
    play music music_pearly fadein 2.0
    
    window show dissolve

    "Около девяти часов утра мне звонит %(name_hideaki)s. Кажется, он вновь стал самим собой, спокойным и церемонным, как всегда. Наш разговор недолог."

    hi "Алло?"

    hh "Здравствуйте. Это Хисао Накай?"

    "Чересчур официально. Уверен, он знает об этом, и я испытываю желание построить из себя умника."

    hi "Да. Да, это я. В конце концов, это ведь мой личный мобильный телефон."

    hh "Я не слишком рано звоню?"

    hi "Не слишком."

    hh "Ясно. Это хорошо. Я загляну через пару часов. Ровно через два часа. Сможешь ли ты снова пойти со мной к %(name_shizune)s?"

    hh "Наш прошлый разговор и разговором-то не назовёшь. С тех пор я думал о том, что хотел бы ей сказать, но, конечно, мне вновь понадобится твоя помощь. Извини, что продолжаю тебе этим докучать. Это моя вина, что я не выучил язык жестов."

    "Точно, ведь даже %(name_hideaki)s не знает, что %(name_shizune)s умеет читать по губам… Серьёзность, с которой она подошла к сокрытию этого умения, впечатляет."

    "Возможно, я и впрямь единственный, кто посвящён в эту тайну."

    hi "Да, конечно. Не беспокойся."

    hh "Спасибо."

    hh "Как %(name_shizune)s?"

    "В голову приходит множество вариантов ответа."

    hi "…Она в порядке."

    hh "Ладно."

    "Он вешает трубку."
    
    show phone mobile_alpha at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamove
    with Pause (0.5)
    
    scene bg school_dormhisao with locationchange

    "Два часа? Вообще-то я и сам собирался сегодня проведать %(name_shizune)s, но можно и подождать."

    "Я всё ещё не могу привыкнуть, что приходится так беспокоиться о %(name_shizune)s. В конце концов, именно она из нас троих, казалось, действительно распланировала свою жизнь. Конечно, всегда может случиться нечто неожиданное."

    "Но она была таким человеком, который так или иначе учёл бы и это."

    "Я всё ещё не знаю, что буду делать со своей жизнью. Не знала и Миша. Думаю, я уважаю %(name_shizune)s за её уверенность в себе. Может быть, меня всегда притягивал её чёткий, аналитический взгляд на вещи."

    "Но, похоже, так же, как я хотел изменить себя, пыталась измениться и %(name_shizune)s."

    "И теперь, учитывая происходящее, мне интересно…"

    "Полагаю, вопрос вот в чём: насколько просто человеку измениться, когда для этого требуется поменять всё?"

    "И действительно ли я достигну чего-либо, сидя тут и размышляя об этом, когда есть столько всего, что мне следует сделать?"

    stop music fadeout 5.0
    
    "Особенно сейчас, в такое важное время."
    
    scene bg school_dormhisao with shorttimeskip

    "В задумчивости я теряю счёт времени, умудрившись забыть о равномерно тикающих часах на стене. Когда я вновь замечаю их, оказывается, что прошло уже два часа с небольшим."

    $ renpy.music.set_volume(0.1, 0.0, channel='sound') 
    play sound sfx_cellphone 
    with Pause(1.0)
    
    "Я взвешиваю решение перезвонить %(name_hideaki)s, когда телефон в моей руке сам начинает звонить."
    scene bg school_dormhisao_blurred with locationchange
    with Pause(0.5)
    show phone mobile_alpha at Position(ypos=1.1) with None
    show phone mobile at center with dissolvecharamove

    hi "Ты всё ещё здесь?"
    $ renpy.music.set_volume(1.0, 0.0, channel='sound') 
    
    hh "Вообще-то, нет."
    
    play music music_drama fadein 3.0
    "Его голос неестественно напряжён."
    
    hh "Я ходил навестить %(name_shizune)s. Она… очень больна. Я сейчас в больнице. Очень сожалею, что не сообщил тебе раньше. Я запаниковал."

    "%(name_hideaki)s очень хорошо удаётся сохранять спокойствие, однако меня эта новость поражает подобно удару булыжником в живот и я задаюсь вопросом, насколько же плохо было %(name_shizune)s, если потребовалась госпитализация."

    "Как её туда доставили? Если бы я хоть раз выглянул в окно, то, возможно, увидел бы её и смог что-то сделать. Сейчас я даже не хочу рассматривать такую возможность."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient') 
    scene bg school_road with locationchange
    play ambient sfx_running fadein 0.5

    "Уже на бегу я понимаю, что не знаю, где в этом городе больница. И сколько их здесь."
    
    scene bg suburb_roadcenter with locationchange

    #Next sentence originally said "walk around so much" rather than "run". Changed it because it served direction better. Yup. Eat that up, Silentcook. - Kelper

    stop ambient fadeout 6.5
    
    "Те немногие люди, которых удаётся найти, ничем не могут мне помочь, и довольно скоро от этой беготни мне начинает не хватать воздуха, а в груди в такт сердцебиению начинает пульсировать тупая жгучая боль."

    #stop ambient fadeout 6.5
    
    "Это последний знак, что мне нужно остановиться. Мобильного телефона у меня с собой нет, и, хоть я и вижу таксофон, денег с собой у меня нет тоже."

    "Я чувствую, что меня сейчас стошнит."

    "…"
        
    #I added "and find out where the hospital is", to fix a continuity issue. He says he is going back to school and next background you use is a hospital background. - Kelper
    
    "Мне остаётся лишь вернуться в школу и узнать, где находится больница."
    
    stop music fadeout 2.5

    #scene border removed
    
    scene bg newhosp_ext with shorttimeskipsilent

    #play ambient sfx_rooftop fadein 0.5
    
    "Больница, где находится %(name_shizune)s, практически идентична той, где лежал я менее года назад."

    "Разве что она кажется ещё более унылой. Полагаю, больницы, как правило, выглядят более удручающе, когда ты здоров и навещаешь больного, чем когда ты болен сам."
    
    scene bg hosp_room3 with locationchange

    $ renpy.music.set_volume(0.4, 0.5, channel='ambient') 
    
    "Палата %(name_shizune)s до боли пустая, стены украшает лишь одна чрезмерно красочная картина, выглядящая неуместно в такой стерильно-белой комнате."
    
    #Maybe have some anons photoshop some sprites that would match this description? IDK if it's worth it. -md01
    
    #play sound sfx_rustling 
    show shizu behind_blank_gown with Dissolve(1.0)
    
    #The sprites don't really match this description -md01
    #"Shizune looks pale, but still manages to sit up straight when I enter the room, drawing the shirt of her school uniform like a cloak around her slim shoulders barely covered by a hospital gown."
    
    "%(name_shizune)s выглядит бледной, однако ей всё же удаётся сесть прямо, когда я вхожу в комнату."

    shi "…"

    hi "Привет, %(name_shizune)s. Как ты себя чувствуешь?"

    "Мне становится не по себе, когда я произношу эти слова, и я рад, что она меня не слышит, потому что это звучит настолько неискренне, что на меня накатывает печаль."

    "Я смотрю, как капельки жидкости скатываются по прозрачной трубочке, исчезающей из виду где-то в районе сгиба не видимой отсюда второй руки %(name_shizune)s."
    
    shi "…"
    
    show shizu basic_normal_gown with charachange

    "Она поднимает руки лишь на пару дюймов от кровати, а потом, подумав, снова опускает их."

    hi "Что-то не так?"
    #play sound sfx_footsteps_hard
    #with Pause(2.6)
    #play sound sfx_sitting
    #with Pause(1.0)
    
    play music music_tragic fadein 2.0
    
    "Когда она не отвечает, я сажусь на имеющийся в палате небольшой стул."

    hi "Ты понимаешь, когда я просто говорю… это продолжает меня удивлять. Я всё ещё привыкаю к этому."

    hi "Не знаю, почему ты здесь, но, полагаю, дело серьёзное. Я знаю, что ты чувствуешь, что ощущала, когда умерла Миша. Тебе плохо из-за этого, не так ли?"

    show shizu behind_blank_gown with charachange
    
    hi "%(name_shizune)s, тебе нужно перестать зацикливаться на этом. Она была моим другом, и я очень скучаю по ней. Я всё время ожидаю, что она откуда-то неожиданно выскочит, как всегда. Поэтому, думаю, я погорячился, сказав, что знаю, что ты чувствуешь. Это невозможно."

    hi "…Однако… У тебя есть будущее. Ты всё ещё жива. Не ты ли всегда считала обязательным для себя показать мне, сколь многое можешь преодолеть? Такова вся твоя жизнь, потому что именно так ты разбираешься буквально со всем."

    show shizu basic_normal2_gown
    with charachange

    shi "…"

    hi "У оставшихся в живых тоже есть долг. Ты понимаешь?"
    
    show shizu behind_sad_gown
    with charachange

    shi "…"

    "Она всё не поднимает руки, чтобы ответить. Она не показала ни единого жеста с тех пор, как я здесь."

    hi "%(name_shizune)s, о чём ты думаешь?"

    "Её глаза тёмные и проницательные, как всегда, но такие печальные, словно потускневшие драгоценные камни."

    hi "Пожалуйста, скажи хоть что-нибудь."

    "Ощущение дежавю. Не отгораживайся от меня. Мне нужно большее. Мне нужно, чтобы ты сказала мне что-нибудь, тогда я смогу продолжать. Тогда я смогу понять, что мои слова хоть как-то действуют."

    "Если не хочешь говорить, запусти в меня чем-нибудь. Сделай хоть что-то, вместо того чтобы просто смотреть на меня."
    
    show shizu behind_frustrated_gown with charachange
    with Pause(0.4)
    
    "Я поднимаюсь, а %(name_shizune)s, кажется, неверно истолковывает это как знак того, что я собираюсь уйти. Она поднимает левую руку, протягивает её в мою сторону, и я останавливаюсь."

    hi "Что такое?"

    "Её рот приоткрывается, словно чтобы что-то сказать, но ничего не происходит."
    
    #play sound sfx_rustling
    show shizu behind_sad_gown at centersit with dissolvecharamove

    "Похоже, уже одно это истощает её силы, и %(name_shizune)s снова ложится, опустив голову на подушку."

    "О чём ты думаешь? И почему продолжаешь вот так тянуться ко мне, не давая уйти, если не собираешься ни отвечать на вопросы, ни что-либо рассказывать мне?"

    "Мне достаточно какого угодно отклика. Я лишь хочу, чтобы она хоть что-то сказала. Чем дольше она не отвечает, тем сильнее ощущение тщетности моего прихода сюда. Скажи же что-нибудь."


    "%(name_shizune)s упряма, даже сейчас. Возможно, даже ещё упрямее. Если я чего-то и достиг, то лишь ещё больше укрепил и так непоколебимую волю. %(name_shizune)s, ты хочешь, чтобы я жил с таким чувством вины?"

    hi "Могу я спросить, чего ты хочешь добиться? Что ты задумала?"
    
    show shizu basic_angry_gown at centersit with charachange

    "Она почти незаметно качает головой."

    hi "Я…"

    hi "Это действительно необходимо?"
    
    shi "…"

    hi "Эй."

    #stop ambient fadeout 2.5
    
    hi "Ты пытаешься последовать за Мишей?"
    
    shi "…"
            
    $ renpy.transition (Dissolve(0.8), layer='master')
    show shizu behind_blank_gown at centersit
    extend""
    
    hi "Ты действительно этого хочешь?"
    #play music music_moonlight fadein 6.5    
    hi "Это… первый случай, когда ты следуешь за кем-то. По крайней мере, на моей памяти."

    hi "Пожалуйста, не надо. Ты говорила с %(name_hideaki)s?"
    
    show shizu basic_angry_gown at centersit with charachange

    shi "…"

    hi "Он беспокоится о тебе. Ты же видишь, не так ли? И Юко тоже. И я. До сегодняшнего дня я даже не допускал мысли о том, что ты хочешь убить себя."

    show shizu behind_sad_gown at centersit with charachange

    "В ответ на мои слова %(name_shizune)s опускает взгляд."

    hi "Ты действительно собираешься…"

    "Если у кого-то и хватит воли сделать нечто подобное, так это у неё."

    hi "%(name_shizune)s, ты понимаешь, кем ты являешься?"

    hi "Ты же была мечтой Миши. Ты читала её записи. Она действительно любила тебя. В том числе за твою целеустремлённость и ум. И теперь ты собираешься всё это уничтожить?"

    hi "Она писала, что мир очень большой, и это пугало её, однако ей удавалось двигаться вперёд, потому что она знала, что мир этот населён удивительными людьми. И ты была одной из них. Она считала тебя удивительной."

    hi "Уверен, ты именно такая."

    hi "Поэтому всё это… удручает."

    shi "…"

    "Неужели ты не видишь: я лишь хочу, чтобы тебе стало лучше? Так что дай мне хоть какой-то знак, что мои слова доходят."

    "Пожалуйста."
    
    show shizu behind_smilelow_gown at centersit with Dissolve(1.0)

    "Она очень печально улыбается."

    hi "Я правда люблю тебя."

    "Я пытаюсь прочитать её чувства по выражению лица, но это невозможно. Она ведь смогла более десяти лет скрывать умение читать по губам. Вот с каким человеком я имею дело."

    "Я всегда думал, что временами могу разглядеть настоящие чувства %(name_shizune)s за этим спокойным, необычайно выразительным взглядом. Если у меня и была такая способность, сейчас она мне изменила."

    "Я умоляю её ещё какое-то время, но всё тщетно. Я пытаюсь вытереть глаза платком, лежащим рядом на столе."

    "Она продолжает печально улыбаться, и фальшивость этой улыбки ужасающе очевидна."

    hi "Я не хочу только говорить тебе что-то. Пожалуйста, просто ответь."
    
    show shizu basic_normal2_gown at centersit with charachange

    shi "…"

    "Полагаю, мне до неё не достучаться."

    hi "Я вернусь завтра."
    
    "Когда я направляюсь к двери, она слегка приподнимает дрожащую левую руку. И оттопыривает мизинец."

    "Обещание?"
    
    show shizu behind_sad_gown at centersit with Dissolve(0.8)
    with Pause(1.2)
    play sound sfx_pillow 

    "Она снова протягивает мне руку, а затем опускает её. Прощальный жест. Я тоже машу ей на прощанье."
    
    window hide dissolve
    
    stop music fadeout 10.0
    
    #I felt like NVL mode was most appropriate for this scene. It was originally written for a normal dialogue box though. -md01
    scene black with Dissolve(5.0)
    
    $ renpy.pause(0.5)
    
    $ renpy.transition(Dissolve(1.5))
    show walivetext ruw(u"Позже я узнаю, что она умерла всего через несколько часов после моего ухода.{fast}")
    $ renpy.pause(3)
    
    $ renpy.transition(Dissolve(1.5))
    hide walivetext
    $ renpy.pause(1.5)    
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    #play ambient sfx_park
    #with Pause(0.5)
    #scene bg city_graveyard with locationchange
    #with Pause(1.0)
    
    nvl show dissolve
    
    n "Впоследствии я услышу, что она, вероятно, не поднимала руки для общения со мной, поскольку была слишком ослаблена обезвоживанием."

    n "Но я знаю, что дело в другом."

    n "Она не поднимала руки, потому что иначе даже я заметил бы, что она вытащила иглу капельницы и приложила её к сгибу локтя."

    n "И, наверное, она не дала мне подойти ближе, так как иначе я заметил бы расползающееся пятно от жидкости на больничном матрасе."

    n "Как может житель страны первого мира умереть от обезвоживания? Для этого нужны целенаправленные усилия."

    n "Именно это она и сделала…"

    n "Я узнал об этом лишь спустя сутки, потому что мой мобильный телефон разрядился."

    n "Даже эту новость я получил с опозданием."

    n "…"
    
    nvl clear

    n "\n\n\n\n\n\nЯ отреагировал как любой другой."

    n "«Я вернусь завтра?»"

    n "«Я вернусь завтра?»"

    n "Такими были мои последние слова?"

    n "Я чувствую сильное отвращение к самому себе."
    
    nvl clear

    n "\n\n\nОна исчезла из моей жизни чересчур быстро, но… я был бессилен всё это время. И после я тоже был бессилен. Оглядываясь назад, я вижу, сколько всего я мог ещё сделать или сделать лучше."

    n "Так что же останавливало меня всё это время?"

    n "Мне даже не хватает воли, чтобы хоть что-то сделать, кроме как вспоминать последние несколько месяцев и сожалеть."

    n "Я знал их меньше года. Когда я оглядываюсь назад, мне кажется, что время, проведённое вместе, пролетело ещё быстрее."

    n "Поначалу я даже не хотел вступать в Школьный совет."

    n "И я принимал это как должное. Даже как будто ненавидел всё это; %(name_shizune)s, всегда такую самоуверенную, агрессивно-игривую, и громогласный смех Миши с её особой манерой речи."

    n "Их обеих больше нет."
    
    nvl clear

    n "\n\n\nМиши, всегда такой счастливой и улыбчивой. Она хотела стать учителем языка жестов."
    
    n "И %(name_shizune)s, всегда активно противостоящей вызовам этого мира и не желающей никому ни в чём уступать."

    n "Как-то сложились бы их судьбы?"

    n "Больше всего я ненавижу себя за то, что, когда видел %(name_shizune)s в последний раз, я лишь помахал ей на прощанье."

    n "Я никак не могу забыть её протянутую руку."

    n "%(name_shizune)s, что ты имела в виду? Просто помахала на прощанье в последний раз?"

    n "Чего ты хотела от меня?"

    n "Этого? Или… Ты ожидала, что я схвачу тебя за руку и вытащу из затянувшей тебя печали?"
    
    nvl clear

    n "\n\n\Вероятно, всё так и было. Я так демонстративно хотел спасти тебя, поскольку думал, что сумею. Я полагал, что смогу тронуть твоё сердце, как ты моё, и ты снова станешь прежней."

    n "Как будто это так легко сделать. Если уж ты сама не смогла, чего я надеялся достичь своими бестолковыми усилиями?"

    n "Ты полагалась на меня."

    n "Ты впервые по-настоящему положилась на меня."

    n "А я тебя подвёл."

    n "Так вот каково тебе было, когда это случилось с Мишей?"

    n "Некоторое время я проведу в раздумьях о том, как загладить свою вину."
    
    nvl hide Dissolve(2.0)
    nvl clear
    scene black
    with Dissolve(3.0)
        
    $ renpy.pause(0.5)
    
    $ renpy.transition(Dissolve(1.5))
    show walivetext ruw(u"Позже той ночью я засну и увижу сон. . .{fast}")
    $ renpy.pause(3)
    
    $ renpy.transition(Dissolve(1.5))
    hide walivetext
    $ renpy.pause(1.5)
       
    stop ambient fadeout 2.5
    with Pause(3.5)
    return

label ru_end_shizunebad:
    # Shizune bad end, after S34
    scene black with dissolve
    centered "~ %(name_shizune)s: плохая концовка ~" with dissolve
    
    return

label ru_S36:

    #These last 2 scenes here did not have any music or sound fx originally. -md01
    
    scene bg school_dormhisao_blurred
    show phone mobile at center 
    with Dissolve(3.0)
    
    play music music_pearly fadein 3.0
    
    window show dissolve

    "Около девяти часов утра мне звонит %(name_hideaki)s. Кажется, он вновь стал самим собой, спокойным и церемонным, как всегда. Наш разговор недолог."

    hi "Алло?"

    hh "Здравствуйте. Это Хисао Накай?"

    "Чересчур официально. Уверен, он знает об этом, и я испытываю желание построить из себя умника."

    hi "Да. Да, это я. В конце концов, это ведь мой личный мобильный телефон."

    hh "Я не слишком рано звоню?"

    hi "Не слишком."

    hh "Ясно. Это хорошо. Я загляну через пару часов. Ровно через два часа. Сможешь ли ты снова пойти со мной к %(name_shizune)s?"

    hh "Наш прошлый разговор и разговором-то не назовёшь. С тех пор я думал о том, что хотел бы ей сказать, но, конечно, мне вновь понадобится твоя помощь. Извини, что продолжаю тебе этим докучать. Это моя вина, что я не выучил язык жестов."

    "Точно, ведь даже %(name_hideaki)s не знает, что %(name_shizune)s умеет читать по губам… Серьёзность, с которой она подошла к сокрытию этого умения, впечатляет."

    "Возможно, я и впрямь единственный, кто посвящён в эту тайну."

    hi "Да, конечно. Не беспокойся."

    hh "Спасибо."

    hh "Как %(name_shizune)s?"

    "В голову приходит множество вариантов ответа."

    hi "…Она в порядке."

    hh "Ладно."
    
    show phone mobile_alpha at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamove
    with Pause (0.5)
    scene bg school_dormhisao with locationchange

    "Он вешает трубку."

    "Два часа? Вообще-то я и сам собирался сегодня проведать %(name_shizune)s, но можно и подождать."

    "Я всё ещё не могу привыкнуть, что приходится так беспокоиться о %(name_shizune)s. В конце концов, именно она из нас троих, казалось, действительно распланировала свою жизнь. Конечно, всегда может случиться нечто неожиданное."

    "Но она была таким человеком, который так или иначе учёл бы и это."

    "Я всё ещё не знаю, что буду делать со своей жизнью. Не знала и Миша. Думаю, я уважаю %(name_shizune)s за её уверенность в себе. Может быть, меня всегда притягивал её чёткий, аналитический взгляд на вещи."

    "Но, похоже, так же, как я хотел изменить себя, пыталась измениться и %(name_shizune)s."

    "И теперь, учитывая происходящее, мне интересно…"

    "Полагаю, вопрос вот в чём: насколько просто человеку измениться, когда для этого требуется поменять всё?"

    "И действительно ли я достигну чего-либо, сидя тут и размышляя об этом, когда есть столько всего, что мне следует сделать?"

    "Особенно сейчас, в такое важное время."

    "…"
    
    stop music fadeout 1.0
    
    scene bg school_dormhisao with shorttimeskip

    "Я смотрю на часы. Остаётся ещё час. Но зачем я медлю? Я могу просто пойти к %(name_shizune)s прямо сейчас и узнать, как она. Ведь так?"
    
    play music music_innocence fadein 2.0

    "Последние несколько дней я только и делал, что думал: «Что ещё я могу сделать?»"

    "И только теперь я осмелился спросить себя, что я на самом деле сделал. Ответ – ничего."

    "Итак, после всех обещаний самому себе, что я буду делать больше для %(name_shizune)s, в реальности я не сделал ничего. Я поддерживал её, но не сказал ничего, что могло бы унять её тревоги. Я присматривал за ней, но не сделал ничего, чтобы облегчить её состояние."

    "Хотя и допускал, что она может совершить нечто ужасное."

    "Я думал, что, возможно, она попытается убить себя. И, по-видимому, Юко думала так же."

    "Бессмысленно сидеть здесь в ожидании. Если я так беспокоюсь о ней, почему я вообще оставил её одну? Это была ошибка. Правда. Просто я привык к другой %(name_shizune)s. За которую никогда не приходилось беспокоиться."

    "Может, я просто хотел продолжать верить в ту %(name_shizune)s? Которая могла сделать что угодно и никому не позволяла встать у себя на пути? Я всё ещё помню, как она выглядела в свете фейерверков много недель назад."

    "Вероятно, именно тогда я начал влюбляться в неё."

    "Может, я просто думал, что эта черта её характера в конце концов возобладает и, хоть и не за одну ночь, она вновь станет прежней?"

    "Я всё ещё тоскую по Мише, и если всё действительно так, то я не знаю, что и думать. Это кажется совершенно неправильным. %(name_shizune)s и Мишу связывало нечто большее, чем меня с каждой из них."

    "Это означает, что рана %(name_shizune)s намного глубже моей. Несравнимо глубже. Почему же я понадеялся на такую смехотворно глупую идею?"

    "А потом я вспомнил, что когда-то давно сказала мне Миша."
    
    #I know there is a flashback filter in the final, but I can't be bothered to port it over for one line of text -md01
    #Nevermind, I ported it over anyway -md01
    
    scene bg shizu_guestbed_fb
    show misha sign_sad_cas_fb
    show noiseoverlay
    with flashback

    mi "Так что… Пожалуйста, будь мне хорошей заменой, %(name_hicchan)s."
    
    scene bg school_dormhisao
    with flashback

    "Странная штука память. Миша, до сих пор я справлялся из рук вон плохо."

    "Надев куртку, я направляюсь в комнату %(name_shizune)s."

    #some transition
    
    stop music fadeout 2.0
    
    scene bg school_girlsdormhall with locationskip
    
    #Changed this line so it'll flow better with the scene direction
    #"When I get to the door, I turn the knob to find it open again. It looks like I've caught Shizune just as she is getting out of bed. When she sees me, she tries to stand up, and then collapses."
    
    "Добравшись до места, я поворачиваю ручку; дверь снова не заперта."
    
    
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    
    scene bg school_dormshizune
    show shizu basic_normal
    with locationchange
    
    show shizu adjust_blush
    with Dissolve(0.2)
    
    show shizu adjust_blush at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.9) with ease_accel
    play sound sfx_impact
    with vpunch
    
    "Похоже, я застал %(name_shizune)s, когда она вставала с кровати. Завидев меня, она пробует подняться, но падает."
    
    show shizu basic_frown
    with charachange

    "Я подбегаю и пытаюсь помочь, но она одной рукой отталкивает меня и, опираясь другой рукой о кровать, взбирается на неё самостоятельно."
    
    show shizu basic_frown at center
    with charamove

    "Моё первое побуждение – спросить, что случилось. Как только я открываю рот, %(name_shizune)s закрывает глаза и решительно качает головой, заранее отрицая наличие каких-либо проблем."

    "Я всё равно спрашиваю. Может, это из-за того, что она так себя чувствует и практически обессилела, но она отвечает."
    
    show shizu basic_normal with charachange

    ssh "В последнее время я почти ничего не ела. Я устала."

    "Это…"

    "Чтобы вот так свалиться от истощения, недостаточно пропустить пару обедов за несколько дней."
    
    play music music_drama fadein 1.0

    "Теперь уже не осталось и тени сомнения. Смерть Миши – не несчастный случай. Я был неправ, и даже сейчас мне больно вспоминать об этом. А теперь, кажется, и %(name_shizune)s хочет убить себя."

    "Пусть лучше я исчезну из твоей жизни после выпуска, чем потеряю тебя вот так."
    
    #Has in this sentence was "as"
    "Даже несмотря на то, что мы провели вместе не так много времени, ты дорога мне."

    hi "Я слышал, что иногда такое случается. Кто-то совершает самоубийство, и это настолько печалит кого-то из знакомых, что он тоже убивает себя. И это может продолжаться и дальше."

    hi "Вот, значит, как?"

    "Она отказывается отвечать."
    
    show shizu basic_angry with charachange

    ssh "О чём ты?"

    hi "О том, что здесь нельзя случайно уморить себя голодом."

    show shizu behind_blank
    with charachange

    shi "…"

    "Я угадал, не так ли? Ты пытаешься умереть от голода? Для этого требуется потрясающая сила воли, которая как раз у неё в наличии."

    hi "%(name_shizune)s, посмотри на меня."
    
    show shizu behind_blank_close
    with characlose

    "Я хватаю её за плечи и с удивлением ощущаю, насколько она хрупкая."

    hi "Наши поступки влияют на всех вокруг."

    hi "Ты очень упрямая. Временами это бывает полезно, но в данном случае? Это не искупление!"
    
    show shizu basic_normal2_close
    with charachange

    "Чёрт возьми, перестань отворачиваться от меня!"

    "Если я прямо сейчас скажу, что нуждаюсь в тебе, это будет эгоистично?"

    hi "%(name_shizune)s, я наконец могу понять ход твоих мыслей."

    hi "Что бы я ни сказал, если этого будет недостаточно, чтобы заставить тебя что-то сделать, ты просто не станешь утруждать себя ответом. Это ведь ты говорила, что это единственное преимущество языка жестов: перед ответом ты можешь тщательно взвесить каждое своё слово."
    
    show shizu behind_smilelow_close
    with charachange

    shi "…"

    "Она мягко улыбается и кивает, колеблясь между радостью, оттого что я всё понял, и сожалением, оттого что всё зашло так далеко, прежде чем мы в конце концов смогли понять друг друга."

    hi "Ты действительно этого хочешь?"

    "%(name_shizune)s снова кивает."
    
    show shizu behind_sad_close with charachange

    ssh "Ты меня ненавидишь?"

    hi "Нет. Я тебя не ненавижу."

    ssh "А следовало бы."

    "Я знаю. Знаю, ты хочешь, чтобы я тебя ненавидел."

    hi "И этого ты тоже хочешь?"

    "Она снова кивает."

    hi "Что ж… я в это не верю."

    hi "Потому что на самом деле это не то, чего ты хочешь, не так ли? В противном случае ты заперла бы дверь… и нашла бы более быстрый способ. Просто ты такой человек. Ты осторожна и никогда ничего не делаешь без причины, так?"

    hi "Даже этого. Даже чего-то подобного."

    shi "…"

    hi "Я не собираюсь ненавидеть тебя, %(name_shizune)s. Впервые ты в чём-то положилась на меня. Как же я могу ненавидеть тебя, когда ты на меня рассчитываешь?"

    hi "Ты проживаешь жизнь без сожалений. Я восхищаюсь этим. Поэтому ты хочешь, чтобы я тебя ненавидел? Я – последнее, о чём ты сожалеешь?"
    
    show shizu basic_normal2_close
    with charachange

    ssh "Да. Ты прав… Насчёт всего. Возможно, ты прав насчёт всего…"
    
    show shizu behind_frown_close
    with charachange

    ssh "Мои поздравления."

    hi "Не говори так, это не игра, %(name_shizune)s. Это ведь даже не отражает твои настоящие чувства. Прекрати."

    ssh "Верно."
      
    show shizu behind_blank with charadistant

    "Она начинает медленно откидываться назад, пока не облокачивается об изголовье кровати."
    
    show shizu basic_normal2
    with charachange

    ssh "Что, по-твоему, я должна делать?"

    ssh "Что, по-твоему, я должна чувствовать?"

    hi "Я не знаю, но этот путь неправильный. Это ужасный способ искупления чего-либо, правда. Миша этого не хотела бы. Когда кто-то умирает, оставшиеся в живых обязаны продолжать жить дальше, возможно даже ещё старательнее."

    hi "Я думал, уж ты-то поймёшь это лучше других."
    
    show shizu behind_sad
    with charachange

    ssh "Во всём этом моя вина."

    hi "Нет!"

    "Я морщусь от своего чересчур неистового крика."

    hi "Не твоя. Ты читала Мишины записи. Не говори так. Это неправда."

    hi "И, даже если бы это было правдой, чего бы ты таким способом достигла? Это ведь не «сравняет» никакой счёт. Что сделано, то сделано."

    hi "Все мы совершаем ошибки. Важно то, как мы к ним относимся, чему мы можем на них научиться и как мы используем их для личностного роста."

    "Я улыбаюсь про себя. Спасибо, Юко."

    hi "С моей стороны было ошибкой оставлять тебя одну, ведь я предполагал, что ты могла задумать. Я беспокоился об этом, но ничего не сделал. Вот почему сегодня я здесь."

    hi "Потому что я действительно ненавижу себя."
    
    show shizu basic_angry with charachange

    ssh "Я тоже."

    shi "…"
    
    show shizu behind_sad with charachange

    ssh "Прости."

    "Возможно, я всего лишь принимаю желаемое за действительное, но чувствую, что, наверное, теперь всё будет хорошо. По крайней мере, процесс пошёл в нужном направлении."

    "Я могу поверить в это, поскольку знаю, что уж кому-кому, а %(name_shizune)s хватит силы воли, чтобы измениться."
    
    stop music fadeout 5.0
    
    show shizu behind_blank with charachange

    "Её ладонь касается моей, тонкие пальцы нежно скользят по костяшкам моих пальцев, постукивая и лаская их."
    
    hi "Я люблю тебя."

    # Removed split
    #STOP RIGHT THERE CRIMINAL SCUM! This split is going back in. -md01

    label ru_S36a:

    #1) If you had sex with Misha way back in S25 and.or said you liked her over Shizune in S14:
    #Silly delta, it's S25h and S14b. Get yo shit together - md01

    hi "Временами я думал, что мне больше нравится Миша. А на самом деле я всегда любил именно тебя. Твои слова, произносимые ею."
    
    show shizu behind_smile
    with charachange

    ssh "Вначале мне было любопытно, смогу ли я заставить твоё сердце дрогнуть."

    hi "Хе-хе, интересный подбор слов."

    "И это всё, чего ты хотела?"

    #END OF REMOVED TEXT (I HOPE)

    label ru_S36b:

    #2) If you did not:

    hi "С той самой ночи на фестивале."

    hi "Я думал: «Ты вправду удивительная, %(name_shizune)s». Даже здесь, в этом крошечном городишке, куда, как я думал, меня просто сослали, потому что у меня не было будущего, где ни у кого его не было, я нашёл тебя. И я смог поверить."

    hi "Миша писала, что мир больше, чем она предполагала. Это пугало её. Однако ей удавалось двигаться вперёд, потому что она знала, что мир этот населён удивительными людьми, такими, как ты."

    "%(name_shizune)s, теперь ты понимаешь?"

    hi "Поэтому… Пожалуйста, продолжай жить."
    
    label ru_S36c:

    #end split
    
    show shizu behind_blank_close with characlose
    
    play music music_comfort fadein 3.0

    "Она сильнее прижимается ко мне и долго не отпускает."

    "Только теперь я понимаю ценность всего этого. Всего, что я приобрёл за этот год, и всего, что потерял."

    "Я отстраняюсь, чтобы смотреть в её глаза при разговоре."

    hi "Я буду продолжать пытаться превосходить твои ожидания. Я люблю тебя. Даже если ты всегда играла со мной. Я буду играть с тобой. Всегда."

    hi "Потому что я люблю тебя."
    
    show shizu behind_smile_close with charachange

    "Наконец-то я сумел это сказать."
    
    ssh "Я тебя люблю."

    "У неё такие красивые глаза. %(name_shizune)s умиротворённо закрывает их и снова меня обнимает."
    
    show shizu behind_smile with charadistant
    hide shizu with charaexit

    "Всё же усталость берёт своё, и она отпускает меня, чтобы прилечь."

    "Со временем она засыпает. Я сижу рядом, пока не раздаётся стук в дверь, которая так и осталась открытой. Кажется, пришёл %(name_hideaki)s."

    "Думаю, за час многое может случиться."

    "%(name_shizune)s, когда ты поправишься, когда всё это закончится, хотел бы я знать, как будут складываться наши жизни. Пойдут ли они по одному пути?"

    "У меня всё ещё есть несколько месяцев, чтобы подумать о будущем."
    
    stop music fadeout 3.0
    
    #This feels like it should have been the end of a scene, but it's not apparently. Added in these transitions to make it feel more like that.
    
    window hide dissolve
    scene black with fade

label ru_S37:

    window show dissolve
    
    scene bg school_girlsdormhall
    with locationchange
    
    "Я продолжаю ежедневно навещать %(name_shizune)s и с каждым разом замечаю, как на её лице вновь появляется здоровый румянец и к ней возвращаются жизненные силы."
    
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    
    scene bg school_dormshizune
    show shizu behind_smile 
    with locationchange
    
    "Я открываю дверь в её комнату и в этот раз обнаруживаю её стоящей за порогом, как будто она ждала меня."

    play music music_another fadein 0.2
    
    ssh "Доброе утро."
    
    hi "Доброе. Ты рано встала."
    
    show shizu adjust_happy with charachange
    
    ssh "Неужели? Ты сегодня весь при параде, а это означает, что ты встал ещё раньше меня, чтобы принять душ, одеться и прийти сюда. И кто теперь встал рано?"
    
    hi "По-прежнему ты."
    
    "Я до сих пор не привык вполне нормально говорить с %(name_shizune)s и часть своих ответов показываю неосознанно. Вероятно, трудно от этого избавиться, когда оно вошло в привычку."
    
    "Вернулись её поддразнивающие манеры и задор, и я рад это видеть. По большей части рад."
    
    hi "Эй, а ты тоже приоделась."
    
    show shizu behind_smile with charachange
    
    ssh "Да. Я подумывала о прогулке."
    
    "Только сейчас до меня доходит, что %(name_shizune)s, вероятно, не покидала общежитие больше двух недель и теперь, когда она пошла на поправку, начинает беспокоиться по этому поводу до такой степени, что согласна даже на бесцельную прогулку."
    
    hi "Вот как? Тогда, раз уж я здесь, я пойду с тобой."
    
    show shizu adjust_smug with charachange
    
    ssh "Можем пуститься наперегонки, и я выиграю."
    
    hi "Кто знает. Возможно, я смогу тебя удивить."
    
    "Меня посещает странное чувство дежавю, будто я уже говорил это раньше."
    
    "Забавно, %(name_shizune)s, но всё это время, что я тебя знаю, я размышлял о том, чем я могу тебя удивить. И я хотел тебя удивить. Я не переставал изумляться почему, и не думаю, что до сегодняшнего дня мог ответить на этот вопрос."
    
    "И я всегда хотел соревноваться с тобой, но не думал, что смогу."
    
    "Удалось ли мне удивить тебя в итоге? Я сделаю это ещё не раз."
    
    show shizu adjust_smug
    with charachange
    
    show shizu basic_sparkle
    with charachange
    
    hide shizu
    with charaexit
    
    "%(name_shizune)s улыбается и начинает жестами показывать что-то, но затем прерывается и, опустив руки, пожимает плечами. Потом она обходит меня и, придерживая открытую дверь, манит меня свободной рукой, призывая следовать за ней."
    
    scene bg school_gardens with locationskip
    
    "Мы начинаем прогуливаться вокруг школы. Свежий и прохладный утренний воздух, несомненно, один из моих любимых атрибутов этой школы. Пока мы бесцельно блуждаем с места на место, я замечаю, что %(name_shizune)s раз за разом пристально смотрит в направлении главного здания."
    
    scene bg school_courtyard_ss with locationskip
    
    "В конечном итоге перед ним мы и оказываемся – это наш последний пункт назначения. %(name_shizune)s заходит внутрь и тотчас направляется в комнату Школьного совета, чего и следовало ожидать."

    stop music fadeout 7.0
    
    scene bg school_council_ss
    show shizu basic_normal2_ss
    with locationchange
    
    #show shizu basic_normal2_ss at Position(ypos=1.1) with charamove
    
    "Отперев дверь своим неправомерно добытым дубликатом ключей, она переступает порог и усаживается за ближайшую парту, с виду будто растворяясь в атмосфере комнаты, уставившись на оранжевые солнечные лучи, льющиеся через окно."
    
    ssh "Это место хранит множество воспоминаний."
    
    hi "Ага…"
    
    show shizu behind_smilelow_ss
    with charachange
    
    ssh "Мы провели здесь много времени втроём. Но, возможно, недостаточно."
    
    "Какое-то время она задумчиво чистит ногти."
    
    show shizu adjust_frown_ss with charachange
    
    ssh "Вначале здесь была только я, в одиночестве. Даже когда у нас были другие члены Совета, они продержались тут около двух дней, и всё из-за Миши."
    
    #Not sure what's going on here. The bit up there just ends and I have no idea what to do with it. It feels like she should go on a bit of a rant, but then Hisao just interupts her. -md01

    #Perhaps the rant would have had something to do with how deceitful she was/is? The bit about her not needing the glasses makes me think so.
    
    hi "…Думаю, ты тоже можешь выглядеть мило. К примеру, когда поправляешь очки."
    
    show shizu adjust_blush_ss with charachange
    
    shi "?"
    
    "В этот раз она поправляет их более тщательно, словно задумываясь над этим действием больше, чем обычно."
    
    show shizu basic_normal2_ss with charachange
    
    #I changed the commented out line here because the ending bracket spilled over into the next line and it drove my OCD nucking futs. -md01
    #ssh "Even this, I don't really have to do it. My vision isn't that bad. It's mostly because…"
    
    ssh "Даже это... На самом деле мне не обязательно их носить. У меня не настолько плохое зрение. Это в основном потому, что…"
    
    ssh "Это привлекает внимание. Вот и всё."
    
    "Всё, что ты делаешь… так тщательно продуманно."
    
    hi "Тогда я не удивлюсь, если без очков ты ещё прекрасней."
    
    show shizu adjust_blush_ss with charachange
    
    ssh "Правда?"
    
    #I felt these next 2 lines didn't need to be here. They felt awkward. -md01
    
    #hi "Maybe you would be cuter without your glasses."
    
    #shi "…"
    
    "Внезапно вокруг что-то изменилось. В царящей атмосфере, в настроении."
    
    show shizu adjust_noglasses_ss with charachange
    
    ssh "Ты думаешь, я симпатичнее без очков?"
    
    hi "Нет. Думаю, ты симпатичнее в них."
    
    show shizu adjust_frown_ss with charachange
    
    shi "…"
    
    #scene white with whiteout
    
    #There are nude Shizune sprites in the final that might be useful here. I'd have to change some dialoge, or get someone to photoshop some stuff, but it could work. -md01
    
    show shizu basic_normal_ss
    with charachange
    
    "Глубоко и медленно дыша, она расстёгивает пуговицы на блузке и выскальзывает из неё, легко сбрасывая, но позаботившись о том, чтобы повесить её на спинку ближайшего стула, дабы она не помялась."

    play music music_one fadein 5.0
    
    show shizu behind_blank_bra_ss
    with Dissolve(0.8)
    
    shi "…"
    
    ssh "…Я хорошо выгляжу?"
    
    hi "Ты выглядишь великолепно."
    
    shi "…"
    
    scene white with whiteout
    
    "Краснея, она начинает приближаться ко мне и берёт меня за руки. Без предупреждения она скручивает их у меня за спиной, и её правая рука начинает подкрадываться к моему паху, по пути слегка ослабляя пряжку моего ремня."
    
    "У меня перехватывает дыхание, когда я ощущаю, как её пальцы ласкают меня сквозь ткань штанов, и это вызывает у неё приглушённое хихиканье с придыханием, что звучит словно ветерок, колышущий высокую траву."
    
    "Рука %(name_shizune)s продолжает игриво стимулировать мою промежность, пока сама она подвигается всё ближе, становясь на носочки, таким образом мы выравниваемся по росту."
    
    "Её большая грудь упирается в меня, другой рукой она до сих пор удерживает мои руки сзади, скручивая их в рогалик всякий раз, когда я пытаюсь освободиться, и с каждой последующей попыткой я всё меньше сопротивляюсь."
    
    "Я начинаю чувствовать поднимающееся к основанию шеи тепло. Словно разжигая огонь, %(name_shizune)s трётся своей щекой о мою и тихо дышит мне в шею."
    
    "Опустившись с носочков, она начинает медленно тянуть мой галстук зубами, продолжая при этом отталкивать меня назад."
    
    "В итоге я чувствую, как жёсткий край стола ударяется о мои ноги сзади, и я стараюсь удержаться от падения; беглый взгляд на %(name_shizune)s говорит о том, что именно этого она и добивалась. Резким движением она заваливает меня на столешницу."
    
    "Это тот же просторный стол, за которым мы сидели месяцами, выполняя работу Школьного совета."
    
    "Мои руки до сих пор прижаты за спиной, %(name_shizune)s восседает на мне сверху."
    
    "Всё не как в прошлый раз. Если я заговорю, она поймёт меня, но сейчас я не могу подобрать слов. Для надёжности она целует меня, будто боится, что я скажу что-нибудь и разрушу волшебство момента, но я был бы безумцем, если б сделал это."
    
    "Она вдруг отстраняется, поправляя очки, стараясь казаться спокойной и выдержанной, насколько это возможно, учитывая её покрытое капельками пота румяное лицо. Это зрелище вызывает у меня улыбку."
    
    ssh "Что тут смешного?"
    
    "%(name_shizune)s тоже начинает улыбаться, но, кажется, она не может воздержатся от продолжения."
    
    ssh "Мне следует просто остановиться и заставить тебя томиться от желания."
    
label ru_S37h:
    
    "Передав это жестами, она расстёгивает лифчик и опускается обратно на меня, сила тяжести выталкивает её обнажённую грудь наружу, на мою грудь, где она расплывается по моей рубашке, отделённая от меня лишь тонким слоем одежды."
    
    "%(name_shizune)s расстёгивает мой ремень и начинает стягивать с меня штаны и нижнее бельё. Возглас удивления срывается с её губ, когда мой напряжённый член выскакивает и бьёт её по руке. Звук настолько неожиданный и несвойственный %(name_shizune)s, что ещё больше возбуждает меня."
    
    "Одним плавным движением она сбрасывает юбку и трусики, они соскальзывают с её ног в аккуратную горку на полу."
    
    "Медленно продвигаясь по столу до тех пор, пока её колени не касаются моих локтей, %(name_shizune)s начинает одной рукой стимулировать себя, другой же – изящно поглаживает мой член, неспешно прослеживая каждый изгиб и жилку, как будто она составляет карту его поверхности."
    
    "Чувствуя моё предвкушение, она медленно опускается на меня сверху, всё больше краснея по мере того, как я всё глубже погружаюсь в её горячее и влажное влагалище."
    
    "В конце концов она останавливается, как только мой член достигает преграды в виде девственной плевы, после чего резко опускается, одновременно ложась на меня, заглушая хрип боли трением своей головы о ямочку моей шеи."
    
    shi "!!!"
    
    #I cut up this line because it overflowed out of the textbox -md01
    #"I thrust my hips towards her at the sudden sensation of movement, and Shizune fights against me, trying to pin me back down when I manage to pull my arms out from under me in that moment, her hips thrusting back with even greater force in response."
    
    "Испытывая нарастающее желание, я приподнимаю бёдра ей навстречу, а %(name_shizune)s озорно пытается прижать мои руки к столу, когда мне удаётся высвободить их из-под собственного тела."
    
    "Из-за этой возни она ещё сильнее насаживается на меня."
    
    "Стол под нашим весом шатается и скрипит, что побуждает %(name_shizune)s двигаться быстрее. Её грудь плотно зажата между нашими телами, упругие соски трутся сквозь мою рубашку, в то время как её бёдра качаются вверх-вниз на моём пенисе."
    
    #Had to cut up this line too. -md01
    #"I feel like I'm about to blank out from the pleasure as Shizune's canal clamps down tighter and tighter on my rod with each passing second, seeming to undulate as she grinds her crotch against mine harder with each thrust, slowing down only to catch her breath before resuming with double the force."
    
    "Я едва не теряю сознание от удовольствия, когда влагалище %(name_shizune)s сжимается всё плотнее вокруг моего члена, волнообразно двигаясь, и с каждым толчком %(name_shizune)s всё сильнее трётся о меня своей промежностью."
    
    "Она замедляется только для того, чтобы отдышаться, прежде чем продолжить с удвоенной силой."
    
    "Её дыхание становится всё тяжелее, и я чувствую, как её язык слегка касается моей щеки; возможно, промахнувшийся поцелуй, но я боюсь целовать её в ответ, потому что из-за её безудержного напора мы можем столкнуться головами."
    
    hi "%(name_shizune)s…"
    
    shi "…нн…"
    
    "Едва слышимый стон пронзает по большей части густую тишину, и %(name_shizune)s начинает ускоряться, приближаясь к своему пределу и, кажется, желая довести до кульминации нас обоих."
    
    shi "…х-х-х… м-м…"
    
    "Она издаёт звуки, похожие на шёпот, и я не смог бы их расслышать, не находись она так близко к моему уху; её нежные губы и язык кружатся около него, покуда её бёдра движутся всё быстрее и быстрее."
    
    "Мои руки теперь свободны, тогда как своими руками она поддерживает себя, и я тянусь, чтобы схватить %(name_shizune)s."
    
    "Мотая головой, она грубо прижимает мои руки к столу, ухитряясь вставить звук неодобрения между тяжёлыми вздохами. Затем она прикасается своими ладонями к моим и смыкает наши пальцы."
    
    "Я уже на пределе, мои бёдра выгибаются, и %(name_shizune)s испускает стон, который тут же пытается подавить, когда достигает кульминации, сжимаясь вокруг моего члена, пока я бурно извергаюсь в неё."
    
    "Израсходовав все силы, %(name_shizune)s заваливается на меня, её грудь поднимается и опускается в такт её глубокому дыханию. У меня кружится голова, когда я выскальзываю из неё, и мне едва удаётся на секунду поднять голову, прежде чем уронить её обратно на стол."
    
    #This line too. -md01
    #"The sound of Shizune's contented breathing and the feel of her plentiful breasts moving back and forth across my chest with each sigh grow more arousing with time in the stillness of the student council room, and my erection comes back, slowly growing back to full size between Shizune's inner thighs."

    "Звук её удовлетворённого дыхания в тишине комнаты Совета и ощущение её пышной груди, с каждым вздохом вздымающейся и опадающей на моей груди, заводит меня всё больше."
    
    "Ко мне возвращается эрекция, и мой член снова медленно набухает между бёдер %(name_shizune)s."
    
    scene bg school_council_ss
    show shizu behind_blank_nak_ss
    with fade
    
    "%(name_shizune)s сползает с меня, освобождая мои руки."
    
    show shizu behind_smile_nak_ss
    with charachange
    
    ssh "Ты всё ещё возбуждён?"
    
    ssh "Хочешь повторить?"
    
    "Я приподнимаюсь, пока не оказываюсь сидящим на самом краю стола, чувствуя себя немного нелепо голышом."
    
    ssh "Только теперь твоя очередь."
    
    "Наши ладони вновь соединяются. Она просит меня взять инициативу в свои руки? Интересно, кроется ли за этим нечто большее, чем может показаться сначала. Это очередное испытание или нечто вроде того?"
    
    "То, как она опирается на меня, её пальцы, сцепленные с моими, – всё это создаёт впечатление, будто она передаёт мне эстафету в гонке. Её прикосновение тёплое и ласковое, когда она толкается и доверчиво тянет меня за руки, неохотно отпуская их."
    
    scene white with whiteout
    
    "Вставая, я обхожу %(name_shizune)s и направляю её туда, где только что был я, таким образом мы меняемся с ней местами. Я наклоняю её, и её груди ложатся на стол. Она пытается оглянутся, чтобы посмотреть на меня."
    
    #Yet again. God damn A22 try and contain yourself, you animal. -md01
    #"Tracing a finger around her soft lower folds and the bright pink nub of her clitoris, I plunge in, grabbing onto her hips as I start pumping in and out of her. Shizune's fingernails rake across the surface of the table, holding onto it like a mountain climber scaling a rock wall."
    
    "Проведя пальцем по мягким складкам её половых губ и по блестящему розовому бугорку клитора, я погружаюсь внутрь, хватая её за бёдра, когда начинаю ритмично двигаться в ней туда и обратно."
        
    "%(name_shizune)s скребёт ногтями по поверхности стола, цепляясь за него, словно скалолаз за отвесную стену утёса."
    
    "По сравнению с прошлым разом %(name_shizune)s кажется более чувствительной и немного смущённой тем, что сейчас она не контролирует ситуацию, но я понимаю, что она уже думает о том, как отыграться, так как пытается вернуть своё обычное самообладание."
    
    "Моя рука скользит по изгибу её бедра в чулке, и я нежно ласкаю её клитор, едва не потеряв равновесие, когда она бурно реагирует, непроизвольно дёрнувшись вверх, чуть не сбросив нас на пол."
    
    "Хоть я и не могу видеть её лицо, я уверен, что %(name_shizune)s заливается румянцем."
    
    "Я обхватываю её внушительную грудь и ласкаю её, как всегда того хотел. Мягкая и идеальной формы, по ощущениям она даже больше, чем кажется, и буквально переполняет мои ладони."
    
    "%(name_shizune)s выгибается подо мной, когда я пощипываю её соски, извивается от стимуляции клитора и подаётся назад при каждом прикосновении."
    
    shi "нна…"
    
    shi "…ххх."
    
    "Раскинув руки, она хватается за края стола и цепляется ногами за мои щиколотки, прижимая нас ближе друг к другу, соединяя нас ещё плотнее и удерживая меня в себе."
    
    "Внутренние стенки её лона невыносимо горячие и упругие, а благодаря её встречным движениям трение только увеличивается, посылая меня на вершину блаженства."
    
    shi "…нх!"
    
    "Кончив, я чуть не падаю назад и едва успеваю приземлиться на стул, на который %(name_shizune)s повесила свою блузку."

    stop music fadeout 3.0
    
label ru_S37x:

    scene bg school_council_ss
    show shizu behind_smilelow_nak_ss
    with locationskip
    
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.3)

    hide heartattack alpha
    with Dissolve (0.5)
    
    "Монотонная пульсирующая боль разливается по правой стороне груди, затухает и проходит. Это недостаточно серьёзный повод для беспокойства, но я всё равно волнуюсь."
    
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.3)

    hide heartattack alpha
    with Dissolve (0.5)
    
    "Полагаю, мне стоило быть более осмотрительным: всё-таки секс – тоже физическая нагрузка, да ещё какая."
    
    show shizu behind_blank_nak_ss
    with charachange
    
    #Changed this line so we wouldn't have to get a photoshop of another sprite -md01
    #"In front of me, Shizune picks up her skirt and puts it back on, but abandons the effort to fully dress herself there and leans back against the leg of the table pensively."
    
    "Стоя передо мной, %(name_shizune)s подбирает юбку и начинает надевать её, но, оставив попытку полностью одеться, она с задумчивым видом облокачивается о стол."
    
    "Она впивается в меня взглядом, и я понимаю, что она тоже размышляет о моём состоянии. Возможно, даже больше, чем я сам."
    
    "%(name_shizune)s, я хочу, чтобы у нас было будущее."
    
    "Даже если это нереально, это то, чего я хочу."
    
    "Я не верил, что у меня есть хоть какое-то будущее, пока не встретил тебя."
    
    "До выпускного ещё есть время. Я всё ещё могу очень постараться, чтобы попасть в хороший колледж, хоть я и не помышлял, что это будет мне по силам, когда впервые прибыл в «Ямаку». Хоть я и сомневался, что доживу до этого момента, когда лежал в больнице."
    
    "Я сделаю всё возможное, ибо ты стала моей целью."
    
    window hide dissolve
    scene black with Dissolve(5.0)
    
label ru_S38:

    play music music_daily fadein 4.0
    scene bg school_courtyard with Dissolve(2.0)
    window show dissolve
     
    "Сегодня мой последний день в «Ямаку»."
    
    "Когда я впервые попал сюда, казалось, что этот короткий учебный год никогда не закончится. Казалось, что меня сослали в богом забытое место, и поначалу я именно так и думал."
    
    "Я не предполагал, что здесь есть хоть что-то, к чему можно привязаться. Конечно, я был неправ."
    
    "А теперь мне кажется, что этого времени было недостаточно – так быстро пролетел учебный год."
    
    "Вчера формально был последний учебный день. С момента пробуждения и до самой выпускной церемонии у меня в животе не проходило ощущение пустоты, и сразу после церемонии я попытался найти %(name_shizune)s, но потерялся в толпе."
    
    "Наконец я снова встретился с родителями, впервые после приезда в «Ямаку», и, когда всё было сказано и сделано, я так и не сумел найти %(name_shizune)s, даже обыскав всю школу."
    
    "Вот почему сегодня такой важный день. Последний день, когда мы можем здесь увидеться."
    
    scene bg school_girlsdormhall with locationchange
    
    stop music fadeout 3.0
    
    "В общежитие сегодня пробраться трудно, поскольку люди постоянно входят и выходят, упаковывая последние пожитки и прощаясь с друзьями. После сегодняшнего дня им будет непросто встречаться."
    
    "Поступят ли они в разные университеты или просто со временем потеряют связь…"
    
    "Я решил не допускать этого, даже если мы с %(name_shizune)s будем учиться в разных местах."
    
    "Я захожу проверить её комнату, но кто-то говорит мне, что она не возвращалась сюда с выпуска, и моё сердце замирает при мысли, что она могла уехать домой пораньше, сразу после церемонии. Однако сдаваться ещё рано."
    
    "Если она не здесь, есть только одно место, где ещё она может быть."
    
    scene bg school_council
    show shizu behind_blank
    play sound sfx_dooropen
    with locationskip
    play music music_shizune fadein 0.2
    
    #$ renpy.pause(0.5)
    
    "Я открываю дверь в комнату Школьного совета и вижу %(name_shizune)s, которая стоит лицом к двери, опираясь на стол, как будто ждала меня всё это время. Это случалось уже столько раз, и временами я думаю, что это может быть правдой."
    
    "Хотя я уже привык к большей части её причуд."
    
    hi "Привет."
    
    ssh "Привет."
    
    show shizu adjust_happy with charachange
    
    "Она выпрямляется и угрюмо поправляет очки."
    
    hi "Я надеялся, что найду тебя здесь."
    
    show shizu behind_smile
    with charachange
    
    ssh "Я тоже надеялась, что ты найдёшь меня здесь."
    
    hi "Хе-хе."
    
    show shizu basic_normal2 with charachange
    
    ssh "Сожалею, что не могла встретиться с тобой после церемонии. Нужно было разобраться с последними делами."
    
    ssh "Мне предложили работу в компании отца."
    
    ssh "Придётся начинать карьеру с нуля, но начальная зарплата всё же очень неплохая."
    
    ssh "Однако я размышляла, может мне следует целиком и полностью сосредоточиться на учёбе."
    
    ssh "У меня достаточно средств, чтобы всё это время ни в чём себе не отказывать."
    
    ssh "Я пока ещё в раздумьях, что выбрать."
    
    hi "Непростой выбор, похоже."
    
    show shizu adjust_smug with charachange
    
    ssh "Так и есть. Однако я уже решила. Я собираюсь продолжить обучение. Знаю, я подхожу для этой работы, но не хочу, чтобы все думали, что у меня привилегированное положение или, если я продвинусь по службе, что это не только из-за моих способностей."
    
    ssh "В этот раз приходится выбирать между гордостью и честолюбием."
    
    hi "Я смотрю на это несколько иначе. Кроме того, ты бы перенапряглась, если бы попыталась успеть всё. Иногда ты слишком амбициозна."
    
    "Ну, чуть чаще, чем иногда."
    
    show shizu adjust_angry with charachange
    
    "%(name_shizune)s улавливает подтекст и толкает меня в бок."
    
    show shizu adjust_happy with charachange
    
    ssh "Ну что же, а что дальше намерен делать ты?"
    
    hi "Я?"
    
    hi "Я поступлю в институт и стану учителем. Физика даётся мне лучше всего. Во всяком случае, этот предмет наиболее мне интересен. Поэтому стану преподавателем физики. По-видимому, чтобы стать учителем, нужно сдать не слишком сложный экзамен, главное – сдать его вовремя."
    
    show shizu behind_blank with charachange
    
    ssh "Похоже, ты уже всё распланировал."
    
    hi "Я подыскивал институты, в которых выдавались бы гранты на обучение, и уже получил несколько предложений."
    
    show shizu behind_smile with charachange
    
    hi "Что за выражение лица? Впечатляет, правда?"
    
    "%(name_shizune)s беззвучно хихикает."
    
    show shizu adjust_smug with charachange
    
    ssh "Нет."
    
    ssh "Знаешь, запланировав что-то, ты обязан следовать плану."
    
    hi "Я в курсе."
    
    show shizu basic_normal
    with charachange
    
    ssh "Думаешь, что сможешь довести дело до конца?"
    
    hi "Да. Смогу."
    
    show shizu adjust_happy
    with charachange
    
    ssh "Уверен? Если скажешь «да», нормативы изменятся. И я буду настаивать на их выполнении."
    
    hi "Да."
    
    show shizu basic_normal2 with charachange
    
    ssh "С чего это вдруг такое трудолюбие? При нашей первой встрече ты был другим, всё время бил баклуши. Нам с Мишей приходилось силой затаскивать тебя, вопящего и брыкающегося, в комнату Школьного совета."
    
    hi "Эй! Я ни разу не брыкался и не вопил."
    
    hi "Как бы то ни было, теперь у меня есть цель. Ты собираешься преуспеть, так? Если ты будешь требовать от меня выполнения взятых обязательств, я точно так же буду требовать от тебя выполнения твоих. И, если ты собираешься отличиться в своём деле, разве это не означает, что я тоже должен?"
    
    ssh "Кто это сказал?"
    
    hi "Разве ты не в восторге от соревнований?"
    
    show shizu adjust_smug with charachange
    
    "%(name_shizune)s дерзко ухмыляется, подняв брови."
    
    ssh "Да? А это кто сказал?"
    
    "Уверен, она уже поняла, о чём я. В конце концов, для меня эти отношения начинались с попыток дотянуться до тебя. Теперь же я хочу быть равным тебе. А может быть, даже превзойти тебя."
    
    "Ты даёшь мне стимул развиваться и свободу выбирать направление этого развития. Рядом с тобой я чувствую себя живым."
    
    "Ладонь %(name_shizune)s накрывает мою."
    
    hi "Ты, разумеется."
    
    "Я всегда соревновался с тобой. Поначалу ты мне не особо и нравилась. Я не знал, что ты от меня хочешь, поэтому я хотел лишь маленькой собственной победы над тобой, чтобы ты прекратила снова и снова ставить меня в глупое положение."
    
    "Когда я начал влюбляться в тебя, то перестал так думать. Возможно, в тот момент я стал рассматривать твоё поведение как... флирт."
    
    show shizu adjust_blush with charachange
    
    "Я говорю ей всё это, а она со слабой улыбкой отводит взгляд, при этом лицо её принимает задумчивое выражение. Через некоторое время она спрашивает:"
    
    show shizu behind_smile with charachange
    
    ssh "Я настолько важна для тебя?"
    
    "Она жестикулирует довольно непринуждённо, но я вижу, что это заботит её гораздо сильнее, чем кажется."
    
    hi "Ага…"
    
    #I thought this line would be better with the second part in it's own textbox -md01
    #ssh "A person's value is determined by how many people it would take to replace them. To me, you are irreplaceable."
    
    show shizu basic_normal2 with charachange
    
    ssh "Ценность человека определяется тем, сколько людей нужно, чтобы заменить его."
    
    show shizu adjust_happy with charachange
    
    ssh "Для меня ты незаменим."
    
    hi "…"
    
    hi "А ты – для меня."
    
    "Миша говорила, что её пугает, что их с %(name_shizune)s пути могут разойтись после выпуска. Меня тоже посещала подобная мысль."
    
    "Она такая красивая. Особенно сегодня. Может быть, потому что прямо сейчас я уже начинаю думать о том, как буду скучать по ней."
    
    #The line above and the line at 2262 were originally right after each other. I didn't think it made much sense that Hisao would be able to hear the sound of a camera shutter from outside while in the council room.
    #It would make even less sense for him to run outside to get the camera, and have him bring it back in to the council room to take her picture.
    #I added in the lines between this and the next comment. Basically, they leave the student council room and make their way out to the school grounds. -md01
    
    show shizu basic_normal with charachange
    
    "…"
    
    "Между нами не осталось ничего недосказанного, и мы какое-то время просто сидим и наслаждаемся обществом друг друга."
    
    "Наконец %(name_shizune)s начинает что-то жестикулировать."
    
    show shizu behind_smile with charachange
    
    ssh "Нет смысла сидеть в этой душной комнате. Пойдём на улицу."
    
    hi "Хорошо."
    
    stop music fadeout 2.0
    
    #Don't forget to add the ambient crowd fx
    #Edited out the crowd. It didn't work with them only showing up for one line of text before shipping out. -md01
    scene bg school_courtyard
    #show crowd
    with locationskip
    
    #play ambient sfx_crowd_outdoors fadein 1.0
    
    "Мы просто сидим и смотрим на проходящих мимо учеников."
    
    #"There is little that needs to be said at this point. We both know our remaining time together is short."
    
    scene bg school_courtyard_ss with shorttimeskip
    
    play music music_soothing fadein 2.0
    
    #stop ambient
    
    #"We walk with each other around the courtyard for a few hours."
    
    "Солнце начинает садиться, и большинство учеников уже ушло. Некоторые отправились в общежития, но большая часть уехала с родителями."
    
    "Мои мысли возвращаются к %(name_shizune)s и тому ограниченному времени, которое нам осталось провести вместе. Завтра я поеду на железнодорожную станцию и отправлюсь в долгую дорогу домой, тогда как %(name_shizune)s вернётся к своей семье."
    
    #End me butchering the script -md01
    
    play sound sfx_camera
    
    "Звук затвора фотоаппарата возвращает меня к реальности, и мне хочется влепить себе затрещину за то, что не взял с собой нормальную камеру. Взял бы – смог бы сделать её фото."
    
    "Было глупостью с моей стороны не додуматься взять фотоаппарат на выпуск. Не только из-за %(name_shizune)s, но и чтобы запечатлеть все памятные моменты и всех остальных людей, что я встретил здесь."
    
    "К счастью, на полпути по территории школы я замечаю выпускника с громоздкой, дорого выглядящей камерой в руках. Это фотоаппарат для получения мгновенных снимков, который выдаёт снимки сразу после съёмки."
    
    "Какая удача. Я даже не предполагал, что такие камеры ещё производят, да и раньше они были редкостью. Я подбегаю к нему."
    
    hi "Привет, можно я одолжу её на секунду? Всего один снимок."
    
    "Он со стоном рассказывает, что я уже, наверное, сотый человек за сегодня, но всё равно передаёт её мне, я бегом возвращаюсь к %(name_shizune)s и поднимаю камеру."
    
    show shizu behind_frustrated_ss with charaenter
    
    hi "Улыбочку!"
    
    "%(name_shizune)s качает головой."
    
    hi "Не любишь, когда тебя фотографируют?"
    
    show shizu adjust_angry_ss with charachange
    
    "Сухо поправив очки, она энергично жестикулирует в ответ."
    
    ssh "Боюсь, заставить меня улыбнуться на камеру гораздо труднее."
    
    show shizu basic_sparkle_ss
    with charachange
    
    "Её глаза озорно блестят, в них золотом отражается солнечный свет, в этих двух глубоких тёмно-синих заводях, всегда таких любопытных и насмешливо игривых."
    
    "Ещё одна игра?"
    
    show shizu behind_blank_ss
    with charachange
    
    hi "Ой, ну давай же."
    
    "…"
    
    hi "Ну, да, полагаю, не то чтобы это фото что-либо значило."
    
    hi "Мы ведь ещё увидимся, не так ли?"
    
    show shizu adjust_happy_ss with charachange
    
    shi "…"
    
    "Она кивает."
    
    hi "Я сказал «да», значит нормативы изменились."
    
    show shizu basic_normal_ss
    with charachange
    
    ssh "Изменились мои ожидания."
    
    hi "Я буду учиться не так уж и далеко от тебя. Я…"
    
    "Я не буду пытаться что-то сделать, я сделаю это."
    
    "Я не позволю нескольким километрам разлучить нас. Неужели я допущу, чтобы такая мелочь подорвала мою решимость быть с ней? Ну уж нет."
    
    hi "Каждые выходные. Давай будем встречаться каждые выходные."
    
    show shizu adjust_smug_ss with charachange
    
    ssh "Если мы оба относимся к этому серьёзно, небольшое расстояние не помеха."
    
    hi "Точно. У нас всё получится, правда?"
    
    show shizu basic_happy_ss
    with charachange
    
    ssh "Ты так серьёзен. Думаю, тебе в конце концов удалось меня впечатлить."
    
    hi "Хе-хе. ...Что насчёт свадьбы?"
    
    show shizu adjust_smug_ss with charachange
    
    ssh "А что?"
    
    "Не стесняйся."
    
    show shizu behind_smile_close_ss with characlose
    show shizu adjust_smug_ss with charadistant
    
    "%(name_shizune)s опускает камеру вниз, и я чувствую, как её нежные губы касаются моих. Она быстро отскакивает, прежде чем я успеваю ответить на поцелуй."
    
    ssh "Теперь, когда ты это сказал, мои ожидания снова изменились."
    
    ssh "Однако, думаю, это возможно."
    
    hi "Дети?"
    
    show shizu adjust_happy_ss with charachange
    
    ssh "Также возможно."
    
    ssh "Если будет мальчик, назовём его..."
    
    hi "Как насчёт, скажем... Исаму?"
    
    ssh "Может быть."
    
    ssh "А если девочка?"
    
    hi "%(name_shiina)s."
    
    show shizu behind_blank_ss
    with charachange
    
    ssh "Хорошо."
    
    ssh "Значит, решение принято."
    
    show shizu behind_smile_ss with charachange
    
    ssh "...И я прослежу за его выполнением!"
    
    "Наконец ты решила показать мне свою улыбку."
    
    "Я снова поднимаю камеру и делаю снимок."
    
    window hide dissolve
    
    play sound sfx_camera
    scene white with whiteout
    
    stop music fadeout 5.0
    
    scene black with Dissolve(5.0)
    
    #end
    
    return

label ru_end_shizunegood:
    # Shizune good end, after S38
    scene black with dissolve
    centered "~ %(name_shizune)s: хорошая концовка ~" with dissolve
    return
