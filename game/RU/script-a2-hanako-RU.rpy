label ru_H2:
    
    scene bg school_miyagi 
    show hanako emb_downsmile_close 
    with dissolve#None

    play sound sfx_doorknock2

    show hanako emb_timid_close 
    with charachange
    
    "Только мы расставляем фигуры, как вдруг до нас доносится стук в дверь."
    
    play sound sfx_dooropen

    show bg school_miyagi at bgright 
    show hanako emb_timid_close at tworight 
    with charamove

    show lilly basic_smileclosed at twoleft 
    with charaenter

    li "Ага, как я и ожидала, вы оба здесь."

    play music music_lilly fadein 4.0

    show hanako emb_emb_close at tworight 
    with charachange

    ha "Лилли…"

    hi "О… С возвращением, Лилли. Ты уже закончила?"
    
    show lilly basic_smile at twoleft 
    with charachange

    li "Учитель попросил помочь других ребят, так что мне наконец-то удалось освободиться. Вы тут с тех пор, как ты ушёл, Хисао?"

    hi "Большую часть времени. Мы немножко поиграли в шахматы."
    
    show hanako emb_smile_close at tworight
    with charachange

    ha "Н-не хочешь выпить чашечку чая?"
    
    show lilly basic_weaksmile at twoleft 
    with charachange
    
    li "Если честно, у меня появилась, как мне кажется, довольно неплохая идея: прогуляться за пределы школы…"

    show hanako def_worry_close at tworight
    with charachange

    "Ханако мгновенно падает духом, что сразу же отражается на её лице, хоть она ничего и не говорит."

    "Я почему-то чувствую себя обязанным озвучить отражённые на лице Ханако мысли."

    hi "Мне… мне кажется, что нам стоит остаться здесь…"
    
    show lilly basic_surprised at twoleft 
    with charachange

    li "В самом деле? Сейчас в школе слишком людно, и поэтому я подумала, что мы могли бы сходить в расположенный неподалёку чайный дом."
    
    show hanako emb_blushtimid_close at tworight
    with charachange

    ha "Ты имеешь в виду «Ш-Шанхай»?"

    show lilly basic_smileclosed at twoleft
    with charachange

    li "Именно. Пока все на фестивале, там должно быть практически пусто."

    hi "Чайный дом?"
    
    show lilly basic_weaksmile at twoleft
    with charachange
    
    li "Ах да, кажется, мы тебе о нём ещё не рассказывали."
    #Odds are fairly good he does instead; damn Shangai Amnesia will be a fucking headache to check for in final release. Note to self: check. -SC
    
    show lilly basic_smile at twoleft
    with charachange

    li "Этот чайный дом находится совсем неподалёку отсюда, и мы посещаем его время от времени."

    li "Возможно, «чайный дом» – не совсем подходящее название, но так уж это заведение себя позиционирует."

    li "По моему мнению, ему бы больше подошло «кафе»."
    
    "Разъяснения Лилли только озадачили меня. Какое-то кафе, которое называет себя чайным домом…"
    
    "Разве это не одно и то же вообще?"

    hi "Я… не совсем уловил мысль, но в любом случае пойду с вами."

    hi "Ханако, что насчёт тебя?"
    
    show hanako defarms_shock_close at tworight
    with Dissolve(0.2)

    show hanako def_worry_close at tworight
    with charachange

    "Вовлечённая в разговор против своей воли, Ханако слегка вздрагивает, но зато сосредотачивается."
    
    show hanako cover_bashful_close at tworight
    with charachange

    ha "Ес… если в «Шанхай», то ладно."
    
    show lilly basic_planned at twoleft
    with charachange

    li "В таком случае решено. Пойдёмте."
    
    show hanako basic_bashful at tworight
    with charadistant

    "Мы с Ханако встаём из-за стола, прерывая шахматную партию."

    "Не успеваю я и глазом моргнуть, как Ханако собирает фигурки в маленький ящичек и убирает доску."

    hi "Похоже, теперь мы готовы. Пожалуйста, ведите."
    
    stop music fadeout 8.0

    scene bg school_hallway3 
    with locationchange

    show hanako emb_smile at Position(xanchor=0.5, xpos=0.58) 
    show lilly basic_smileclosed at Position(xanchor=0.5, xpos=0.42) 
    with charaenter

    "Ханако встаёт рядом с Лилли, и мы выходим в коридор."
    
    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')

    play ambient sfx_crowd_outdoors fadein 1.0

    scene bg school_gate_ss 
    with locationskip

    "Девушки проводят меня через несколько незнакомых дверей, и мы выходим на улицу с противоположной от места проведения фестиваля стороны."

    "Приглушённый толстыми каменными стенами здания шум, исходящий от столпотворения людей, затухает до невнятного шёпота."

    #"Even around the gate there is only a limited amount of human traffic heading into the grounds."
    #I don't think that would be in sight from this angle. Need2check comparative geography. -SC

    hi "Странно, я думал, к этому моменту народ уже начнёт расходиться…"
    
    show hanako emb_downtimid_ss at Position(xanchor=0.5, xpos=0.58) 
    show lilly basic_smile_ss at Position(xanchor=0.5, xpos=0.42) 
    with charaenter

    li "Они, наверное, всё ещё здесь из-за фейерверка."

    hi "Фейерверка?"
    
    show lilly basic_weaksmile_ss at Position(xanchor=0.5, xpos=0.42)
    with charachange

    li "Да. Похоже, школа приготовила настоящее представление."

    li "Множество горожан прибыло именно ради того, чтобы на него посмотреть."

    "Теперь мне становится понятным решение Лилли покинуть территорию школы. Сложно представить, как Ханако справилась бы с тем, что население всего города свалилось на школу как снег на голову."

    "Они каждый год вот так уходят, чтобы избежать толп народа?"

    stop ambient fadeout 7.0
    play music music_tranquil fadein 3.0

    scene bg school_road_ss 
    with locationchange
    
    "С момента моего перевода сюда мы с Лилли уже во второй раз спускаемся по этой дороге."
    #Again need2check flow, but this seems likely to be true. -SC
    
    "Лишь теперь, когда я едва могу слышать оставшийся позади непрекращающийся гул фестиваля, становится понятно, насколько же он был оглушительным. В тишине вечернего воздуха я замечаю незначительный звон в ушах, восстанавливающихся от оказанного на них днём давления."

    show hanako emb_emb_ss at Position(xanchor=0.5, xpos=0.58) 
    show lilly basic_smileclosed_ss at Position(xanchor=0.5, xpos=0.42) 
    with charaenter

    "Ханако, пусть и вцепившись в Лилли, всё-таки умудряется вести её по дороге. Поэтому, а также из-за любопытных взглядов случайных прохожих она вновь полностью замыкается."
    
    "Она редко отрывает взгляд от дороги перед собой, и от неё не слышно ни слова."

    "Лилли сейчас тоже не чувствует себя столь уверенно, как в «Ямаку». Здесь она постукивает перед собой тростью куда чаще, чем в школе."
    
    "Стоит только покинуть наш изолированный мирок, этого уже не изменить."

    "В «Ямаку» каждый – «особенный», что сводит на нет всю эту «особенность»."

    "Однако, стоит лишь выйти за пределы школьных ворот, мы вновь ощущаем себя «изгоями»."

    "Особенно если мы идём в своей школьной форме. Будто вешаем себе на шею объявление, побуждающее людей заинтересоваться, что же с нами не так."

    "Я удивляюсь тому, что большинство учеников выходит за пределы школы, не снимая её. Правда, многие из них передвигаются с помощью трости или инвалидной коляски, поэтому она лишь поясняет то, что и так очевидно."
    
    "А может, только я отношусь к ней как к клейму? Возможно, к ней спустя какое-то время привыкаешь, как и к любой школьной форме."

    scene bg suburb_shanghaiext_ss
    with locationskip
    
    "Снаружи чайный дом выглядит довольно обыкновенно: кафе с типичной вывеской над входом."
    #Writing from here on might need major refurbishing, as above. -SC

    "Оно похоже на одно из тех мест, мимо которого вы пройдёте не задумываясь, не обратив внимания на очередное заурядное кафе средь морской пучины тысяч подобных заведений."
    
    "Если бы Ханако не направила Лилли ко входу, я бы продолжил идти по дороге, так и не узнав о его существовании."
    
    play sound sfx_storebell

    scene bg suburb_shanghaiint at Fullpan(5.0, dir='right') 
    with locationchange

    stop music fadeout 6.0
    
    "Интерьер выполнен в традиционном стиле. Всё выглядит так, словно выпилено из одного бруска дерева, начиная с прилавка и скамеек и заканчивая креслами с высокими спинками вдоль стен."
    
    "Но самой поразительной особенностью этого помещения является его безлюдность. На кухне за стеной вроде бы что-то кипит, но помимо этого стоит тишина."

    "Не услышав какого-либо приветствия, мы просто стоим рядом со входом, вежливо повинуясь надписи «Пожалуйста, подождите, вас проводят»."

    hi "Э-э, тут что, сегодня закрыто?"
    
    stop music
    play sound sfx_impact2

    show yuukoshang panic_up at Transform(xalign=0.5, yanchor=1.0, ypos=1.5, alpha=0.0)
    with None
    
    show yuukoshang panic_up at Transform(xalign=0.5, yanchor=1.0, ypos=1.0, alpha=1.0)
    show bg suburb_shanghaiint at right 
    with Dissolvemove(0.3)

    with vpunch

    "Звук упавшего стула эхом разносится по помещению, и из-за стойки тут же появляется голова."

    play music music_comedy fadein 0.5

    show yuukoshang neurotic_up
    with charachange

    yu "Я не спала, и добро пожаловать в «Шанхай»!"

    "Юко, одетая в пастельный передник и держащая в руках меню, бросается нам навстречу. Съехавшие очки и растрёпанные волосы заставляют усомниться в её предыдущем утверждении."

    "Но спала она или нет – отнюдь не первый вопрос, что возникает у меня в голове."
    
    hi "Ты теперь здесь работаешь? А как же библиотека?"
    
    show yuukoshang smile_down 
    with charachange

    yu "А? Лилли? Хисао?"
    
    show yuukoshang neurotic_up 
    with charachange

    yu "Добро пожаловать в «Шанхай»!"
    
    show yuukoshang noglasses_up at Position(ypos=1.25) 
    with Dissolvemove(0.2)

    play sound sfx_dropglasses

    with Pause(0.3)

    show yuukoshang noglasses_up at center 
    with charamove
    
    "Ещё просыпающаяся Юко в неистовом поклоне сбивает с себя очки."

    yu "А?! Мои очки…"

    "Пока я поднимаю их с пола, Лилли всё объясняет."
    
    show yuukoshang noglasses_up at tworight 
    show bg suburb_shanghaiint at center 
    with charamove

    show lilly basic_weaksmile at twoleft 
    with charaenter

    li "Юко работает здесь на полставки, когда заканчивает дела в библиотеке. И это одна из причин, по которой мы любим проводить здесь время."
    
    show yuukoshang neurotic_up at tworight
    with charachange
    
    "Юко забирает у меня очки и дрожащими руками возвращает их на место."

    yu "Да… это так… спасибо…"
    
    show yuukoshang neutral_down at tworight
    with charachange

    yu "Могу я проводить вас к столику?"
    
    show yuukoshang worried_up at tworight
    with charachange

    yu "Других посетителей нет, так что вы можете садиться куда хотите и заказывать что душе угодно. Но всё же вам придётся немного подождать, потому что готовить буду я сама…"

    show lilly basic_smile at twoleft 
    with charaenter

    li "Ничего, Юко, можешь успокоиться. Нам чайничек чёрного чая и тарелку бутербродов, пожалуйста…"
    
    show yuukoshang happy_down at tworight
    with charachange

    yu "Хорошо! Я сейчас же займусь!"
    
    hide yuukoshang 
    with charaexit

    show lilly basic_smile at center 
    show bg suburb_shanghaiint at bgright 
    with charamove

    "Юко устремляется во внутреннюю часть кафе, оставив нас стоять у входа."

    "Она раздвигает дверки-половинки, когда вспоминает, что так и не усадила нас."

    yu "Извините! Извините! Пожалуйста, усаживайтесь там, где понравится! Я скоро вернусь!"
    
    stop music fadeout 3.0

    hide lilly 
    with charaexit

    show bg suburb_shanghaiint at bgleft 
    with charamove

    "Последовав её совету, я подвожу Лилли к ближайшей кабинке. Ханако шагает следом."
    
    show lilly invis at twoleft
    show hanako invis at tworight
    with None
    
    show lilly basic_smileclosed at twoleftsit
    show hanako basic_normal at tworightsit
    with dissolvecharamove

    "Присаживаясь рядом с Лилли, я понимаю, насколько это место подходит Ханако."

    "Высокие стенки кабинки полностью отделяют нас от остального помещения, и не похоже, что здесь бывает много посетителей."
    
    "Все предметы обстановки, от подушек на скамейках до подставок для приправ, выглядят старыми, но не изношенными."

    "Интересно, осознанно ли Лилли выбирает подобные места для провождения времени с Ханако?"

    "Создаётся впечатление, что она готова пойти куда угодно, лишь бы её подруга не испытывала дискомфорта."
    
    play music music_another fadein 4.0

    show lilly basic_weaksmile at twoleftsit
    with charachange

    li "Итак, Хисао, я и не знала, что ты играешь в шахматы…"

    hi "Не сказать, что я мастер, но правила знаю."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "Ну же, не томи… кто выиграл?"

    "Невинная улыбка Лилли ставит меня в тупик. Я совершенно не желаю кичиться своей победой над Ханако."
    
    show hanako cover_bashful at tworightsit
    with charachange
    
    ha "Х-Хисао."
    
    hi "Да… но с небольшим преимуществом…"
    
    "Проклятие. Теперь я чувствую себя так, словно совершил что-то ужасное."
    
    show lilly basic_giggle at twoleftsit
    with charachange

    li "Что же, прими мои поздравления. Молодец, Хисао."

    hi "Э-э, спасибо. Но я давным-давно не играл. Было здорово сыграть вновь."
    
    show hanako basic_smile at tworightsit
    with charachange
    
    ha "Д… да, было здорово."
    
    "Ханако в волнении поправляет волосы и отводит взгляд, но лёгкая улыбка всё же появляется на её лице."

    "Реакция несколько более яркая, чем я ожидал, но по-своему милая."
    
    show hanako defarms_shock at Position(xpos=0.8, ypos=1.15) 
    show lilly basic_surprised at Position(xpos=0.2, ypos=1.15) 
    with Dissolvemove(0.5)

    show yuukoshang worried_up
    with charaenter

    "Она застигает меня врасплох. И лишь подобное стихийному бедствию появление Юко возвращает мне дар речи."

    hi "Ты в порядке, Юко? Может, тебе помочь?"
    
    show yuukoshang neurotic_up 
    show hanako def_worry at Position(xpos=0.8, ypos=1.15) 
    with charachange

    yu "Всё в порядке, всё в порядке, всё в порядке. Я всё сделаю, это моя работа."
    
    show yuukoshang worried_up 
    with charachange

    "С крайне сосредоточенным лицом Юко устремляет взгляд на поднос, который несёт, словно просто лишь глядя на него она способна удержать его содержимое на месте."
    
    show yuukoshang neurotic_down # tremble # what is that supposed to be? replaced with 'neurotic_down' for now [str]
    with charachange

    "К сожалению, это не производит никакого эффекта: чашки и блюдца медленно начинают танцевать по кругу, позвякивая при каждом столкновении друг с другом."

    show yuukoshang worried_up at Position(ypos=1.1) 
    with ease

    show yuukoshang worried_up at center 
    with ease

    "С большой осторожностью Юко ставит поднос на стол. В итоге посуда на нём лишь слегка дзинькает."

    show yuukoshang happy_down 
    with charachange

    yu "Вот видите!"

    hi "Э-эм, молодец."
    
    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Как всегда, премного благодарны тебе, Юко."
    
    show yuukoshang neutral_down at Position(ypos=1.2) 
    with Dissolvemove(0.2)
    
    with Pause(0.2)

    show yuukoshang neutral_down 
    with ease

    "Прежде чем ответить, Юко склоняет голову в фирменном поклоне."
    
    show yuukoshang closedhappy_down 
    with charachange

    yu "Всегда пожалуйста."
    
    show lilly basic_smile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Может, присоединишься к нам? Я хотела бы обсудить с тобой те книги, о которых мы тогда говорили…"

    "А ведь и правда, когда я впервые встретился с Ханако, Лилли и Юко обсуждали какие-то книги."
    
    "Какую-то литературу для Лилли на Брайле…"
    
    show yuukoshang neurotic_up 
    with charachange

    yu "Ах… да. У нас так и не было возможности перебрать их, так ведь?"
    
    show yuukoshang neurotic_up at centersit
    with charamove

    "Юко спешно садится рядом с Ханако."

    "Очевидно, преданность Юко работе не сильнее сосредоточенности; стоит ей лишь немного пошатнуться, и она тут же забывает про неё."
    
    show yuukoshang smile_down at centersit
    with charachange

    yu "Я буду в библиотеке завтра днём, если захочешь попробовать ещё раз…"
    
    show lilly basic_cheerful at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Замечательно, тогда я встречусь там с тобой после уроков."

    show hanako emb_timid at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "М-м… Л-Лилли…"

    show lilly basic_oops at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Боже мой, точно. Завтра понедельник, как я могла забыть?"

    "Не совсем понимаю, о чём они толкуют. Что и неудивительно: я здесь всего неделю, так что с распорядком каждого ученика едва ли могу быть знаком."

    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    with charachange
    
    li "В таком случае нам стоит заново договориться."
    
    show lilly basic_smile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Юко, а ты будешь в библиотеке в другие дни недели?"

    show yuukoshang worried_up at centersit
    with charachange

    yu "Хм-м, может быть, но будет слишком поздно…"
    
    show hanako emb_downsad at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "А у м-меня продукты закончились…"
    
    show lilly basic_listen at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Да уж, дилемма."

    "Лилли на секунду задумывается, но затем отвечает."

    show lilly basic_planned at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Хисао! Хисао сможет!"

    hi "М-м, смогу что? Я как-то потерял нить разговора…"
    
    "Не люблю, когда меня в добровольно-принудительном порядке заставляют заниматься чем-то, о чём я не имею ни малейшего понятия."
    
    "А я-то думал, что мне удалось вырваться из объятий Школьного совета и их неоднократных попыток меня завербовать."
    
    show lilly basic_smileclosed at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "О, конечно. Как-то на днях я помогала Юко сортировать новые книги на Брайле, поступившие в библиотеку."
    
    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Но по понедельникам мы с Ханако обычно ходим по магазинам: меньше народа, чем в выходные."
    
    li "На прошлой неделе мы не смогли пойти, потому что я была занята подготовкой к фестивалю. И хотя мне удалось вырваться в конце недели, но тогда уже не смогла Ханако."
    #Again, need2check if this is flow-conditional or not. -SC
    
    hi "И, так как я всё равно не понимаю шрифт Брайля, полагаю, ты хотела бы, чтобы я сходил с Ханако по магазинам?"
    
    show lilly basic_smile at Position(xpos=0.2, ypos=1.15) 
    show hanako emb_timid at Position(xpos=0.8, ypos=1.15) 
    with charachange

    li "Правильно. Ты бы очень мне этим помог."

    hi "Думаю, мне это по плечу. Ханако, что скажешь?"

    show hanako basic_smile at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "Е-если ты не против…"

    hi "Конечно же нет. Я всё ещё не знаком с магазинами в округе, так что, думаю, это неплохая идея."
    
    show hanako basic_bashful at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "Х-хорошо."
    
    show lilly basic_smileclosed at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Теперь, когда мы всё решили, может быть чаю?"

    li "Он давно уже стынет…"

    show yuukoshang panic_up at centersit
    with charachange

    yu "Это моя вина! Позволь налить тебе другой…"

    "Юко протягивает дрожащие руки, но я останавливаю её."

    "Не похоже, что она в состоянии управиться с кипятком."

    hi "Всё в порядке, оставь. Кроме того, ты уже сделала чай и бутерброды, так что выполнила свои обязанности, верно?"

    show yuukoshang neurotic_up at centersit
    with charachange
    
    yu "П… полагаю, что да."
    
    "Юко немного успокаивается, но всё ещё напряжённо наблюдает, как я делю бутерброды."
    
    stop music fadeout 1.0
    play ambient sfx_fireworks

    show white 
    with Dissolve(0.1)

    hide white 
    show fireshine 
    show hanako defarms_shock at Position(xpos=0.8, ypos=1.15) 
    show yuukoshang panic_up at centersit
    show lilly basic_surprised at Position(xpos=0.2, ypos=1.15) 
    with charachange

    "Я собираюсь откусить кусок бутерброда, но тут снаружи раздаётся громкий низкий грохот одновременно со вспышкой света."
    
    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    show yuukoshang smile_down at centersit
    show hanako emb_timid at Position(xpos=0.8, ypos=1.15) 
    with charachange

    li "А, полагаю, фейерверк начался."
    
    hide fireshine 
    show bg misc_sky_ni as front 
    show fireworks 
    with locationchange

    "Взглянув в окно, только сейчас я понимаю, что на смену сумеркам на город опустилась ночь."

    "Искры взрывающихся снарядов образуют фонтаны фейерверков, напоминающие огромные цветы."

    hide fireworks 
    hide front 
    show fireshine 
    show yuukoshang happy_down at centersit
    with locationchange

    yu "Пойдёмте посмотрим!"
    
    show yuukoshang panic_up at centersit
    with charachange

    yu "Ой… извини, Лилли…"
    
    show lilly basic_ara at Position(xpos=0.2, ypos=1.15)
    with charachange
    
    #show hanako_shanghaifw behind bg
    show hanako_fireshine behind bg
    #at Zoom((800,600),(40, 30, 720, 540),(0, 0, 800, 600),22.0, time_warp=_ease_time_warp, xalign=0.5, yalign=0.5)
    show ev hanako_shanghaiwindow behind hanako_fireshine
    with None

    li "Обо мне, пожалуйста, не беспокойтесь."

    li "Я слышала, что из этого кафе на салют открывается довольно неплохой вид…"
    
    play music music_serene fadein 4.0

    hide fireshine 
    hide bg 
    hide hanako 
    hide lilly 
    hide yuukoshang 
    with locationskip

    "Мы все, за исключением Лилли, несёмся к окну небольшой чайной, чтобы посмотреть фейерверк."

    "Вспышки цветных огней играют на лицах Ханако и улыбающейся Юко, и я даже на секунду забываю о том, что собирался смотреть на происходящее за окном."

    "Даже в этом совершенно новом мире есть несколько вещей, что остаются неизменными."

    "Наверное, потому школа и создала такой ажиотаж вокруг этого фестиваля, что он даёт шанс показать сходство между всеми людьми."
    
    stop ambient fadeout 3.0
    
    hide hanako_fireshine
    #hide hanako_shanghaifw 
    with Dissolve(1.0)

    "Представление заканчивается слишком быстро; фейерверки дорогие и бьют по карману даже хорошо финансируемым школам."
    
    scene bg suburb_shanghaiint at bgright 
    with locationchange

    "Прежде чем вернуться к чаю с бутербродами, Ханако поворачивается ко мне."

    show hanako emb_downsmile_close 
    with charaenter

    ha "М-м, с-спасибо за сегодняшний день…"
    
    show hanako emb_smile_close 
    with charachange

    ha "…и за завтрашний."

    hi "Всё хорошо. Не думаю, что я и сам любитель потолкаться в толпе народа."

    hi "Такой день, как этот, намного приятнее проводить где-нибудь далеко ото всех, правда же?"
    
    show hanako basic_normal_close 
    with charachange

    ha "А-ага."

    hi "Однако наше чаепитие слишком затянулось, поэтому давай вернёмся к столу."
    
    show hanako basic_bashful_close 
    with charachange

    ha "Т-точно."
    
    stop music fadeout 6.0

    hide hanako 
    with charaexit

    show bg suburb_shanghaiint at bgleft 
    with charamove

    show lilly basic_smileclosed at leftsit
    show yuukoshang neutral_down at centersit
    with locationchange

    show hanako invis at right
    with None
    
    show hanako basic_smile at rightsit
    with dissolvecharamove

    "Мы возвращаемся в нашу кабинку, к бутербродам."
    
    show lilly basic_smile at leftsit
    with charachange

    li "Звучало впечатляюще. По меньшей мере громче, чем в прошлом году…"
    
    show yuukoshang happy_down at centersit
    with charachange

    yu "Ага, было здорово! Ни разу не видела, чтобы они организовывали такое представление."

    yu "С каждым годом оно становится всё лучше."
    
    show lilly basic_weaksmile at leftsit
    with charachange

    li "Всё же боюсь, что за это время чай остыл."

    show yuukoshang panic_up at center 
    with Dissolvemove(0.2)
    
    play music music_ease fadein 0.5

    yu "О нет! Позволь мне налить новый! Это моя вина!"

    hi "Успокойся, Юко, в этом никто не виноват."

    "Я делаю глоток из своей чашки, просто чтобы подтвердить её слова."

    hi "Остыв, этот чай не стал плохим. Лишь стал похож на чай со льдом."

    show yuukoshang worried_up 
    with charachange

    yu "Правда?"

    hi "Да, правда. А если ты добавишь немного сахара, то станет просто отличным."
    
    show yuukoshang neurotic_up 
    with charachange

    yu "Ты уверен?"

    hi "Абсолютно. Давай ты присядешь и попьёшь его с нами?"

    show yuukoshang smile_down 
    with charachange

    yu "Х-хорошо."

    show yuukoshang smile_down at centersit 
    with charamove

    "Не похоже, что я убедил Юко, но она всё же садится."

    "Она аккуратно насыпает пять чайных ложечек сахара себе в чашку."

    hi "Э-э, я сказал «немного» сахара…"
    
    show yuukoshang neutral_down at centersit
    with charachange

    yu "Знаю, но мне нравится, когда чай сладкий."

    "Я с любопытством заглядываю в её чашку. Как я и предполагал, такое количество сахара отказывается растворяться в остывшей жидкости."

    "Дважды помешав ложечкой, она поднимает чашку и одним глотком выпивает всё содержимое."

    show yuukoshang happy_down at centersit
    with charachange

    yu "Ты прав, он не так уж и плох!"

    hi "Э-э, хорошо…"

    "Я поворачиваюсь к Лилли и Ханако. Пока я наблюдал за Юко, они уже закончили есть."

    "Не желая всех задерживать, я следую примеру Юко и допиваю остатки своего чая одним глотком."

    hi "Кажется, теперь мы закончили."
    
    show lilly basic_smile at leftsit
    with charachange

    li "Возвращаемся, или кто-то хочет повторить?"

    show yuukoshang neurotic_up at centersit
    with charachange

    "На лице Юко ясно отражается, что это плохая идея."

    hi "Думаю, лучше бы нам уже возвращаться в школу."

    hi "В конце концов, мы должны вернуться до отбоя."
    
    show lilly basic_smileclosed at leftsit
    with charachange

    li "Ох, в этом определённо есть смысл."
    
    show lilly basic_smile at leftsit
    with charachange

    li "Увидимся завтра, Юко."
    
    show yuukoshang neutral_down at centersit
    with charachange

    yu "Хорошо, удачно вам всем добраться обратно. Спасибо, что заглянули."

    stop music fadeout 9.0

    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_cicadas fadein 0.5

    scene bg suburb_shanghaiext_ni 
    with locationchange

    "Мы выходим из маленькой чайной, погружаясь в ночную темноту."
    
    $ renpy.music.set_volume(0.40000000000000002, 1.0, channel='ambient')
    scene bg suburb_roadcenter_ni 
    with locationchange

    "Ханако вновь цепляется за Лилли. Сейчас, под покровом темноты, она кажется не такой напряжённой, как по пути сюда."

    "Навстречу нам начинают попадаться группы людей, покидающих территорию школы. Чтобы избежать встречи с ними, Ханако ведёт нас в обход."

    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')

    scene bg school_dormext_full_ni 
    with locationskip

    "Дойдя до общежитий, мы замечаем, что школа кажется необычайно тихой в сравнении с гулом фестивального дня."

    hi "Спасибо за сегодня. Думаю, я узнал много нового."
    
    show hanako emb_timid_ni at Position(xanchor=0.5, xpos=0.59) 
    show lilly basic_weaksmile_ni at Position(xanchor=0.5, xpos=0.41) 
    with charaenter

    li "Всегда пожалуйста. А теперь, боюсь, мне пора откланяться."

    li "Я сегодня притомилась."

    "И правда, Лилли весь день провела на ногах; представляю, как должна была утомить её прогулка за пределы школы."
    
    "Я ощущаю укол вины, вспомнив, что я, наверное, единственный в школе, кто встал сегодня около десяти."

    hi "Без проблем."

    hi "Что ж, увидимся с вами завтра. Спокойной ночи."
    
    show lilly basic_cheerful_ni at Position(xanchor=0.5, xpos=0.41) 
    with charachange

    li "Спокойной ночи, Хисао."
    
    show hanako basic_smile_ni at Position(xanchor=0.5, xpos=0.59) 
    with charachange

    ha "С… спокойной."
    
    hide hanako 
    hide lilly 
    with charaexit
    
    stop ambient fadeout 4.0

    "Мы с девушками расходимся по общежитиям."

    "Только сейчас я понимаю, насколько сильно меня вымотал сегодняшний день."

    #Fade through black to the next scene.
    #I also know that this is a late request, but I think that this is a good place to put the Act 2 Card.
    return

    #---------------------------------------------------------

label ru_H3:
    
    window hide None

    scene black 
    with dissolve

    $ renpy.music.set_volume(0.0, 0.0, channel='ambient')
    play sound sfx_alarmclock

    with Pause(1.2)

    play sound sfx_impact2

    window show
    
    "Звон будильника бьёт по ушам какой-то разудалой попсовой мелодией, но тут же замолкает от стремительного удара кулаком."
    
    scene bg school_dormhisao 
    with openeye

    "Моё тело включает автоматический режим; подсознательно поднявшись с кровати, я натягиваю школьную форму."
    
    scene bg school_scienceroom at bgright 
    with locationskip
        
    "Не успев осознать этого, я уже открываю дверь в класс 3-3. Не без удовольствия отмечаю, что я не единственный, кто после фестивальной недели выглядит будто с похмелья."

    "Лица одноклассников кажутся мрачными. Словно с окончанием фестиваля все их мечты, к сожалению, осуществились."

    "И, так как в этой жизни больше не к чему стремиться, ребята подчинились своим инстинктам, которые направили их прямиком в класс."

    "Или, возможно, я просто выдумываю."

    "Медленно пробираясь к своему месту, я только теперь замечаю, почему атмосфера в кабинете кажется столь мирной."
    
    "Места рядом с моей партой не заняты, и это великолепно. Самый громкий в мире переводчик для глухих ещё не прибыл."
    
    play sound sfx_doorslam
    play music music_running

    show misha invis at Position(xanchor=0.0, xpos=1.0)
    with None
    
    show misha hips_grin at right
    with Dissolvemove(0.3)
    with vpunch

    "И только я собираюсь занять своё место, как дверь распахивается, являя блистательную Мишу; её локоны подпрыгивают в такт энергичным движениям, а руки простираются к небу."

    show misha hips_laugh at right 
    with charachange
    
    mi "Я-хо-о-о-о~! Наконец-то всё закончилось!"

    "Оказывается, не все подверглись постфестивальной депрессии."

    "Сонный класс лениво поднимает на неё глаза, очевидно думая о том же, о чём и я."
    
    show misha sign_confused at right
    with charachange

    "Миша, застывшая в дверях с раскинутыми в воздухе руками, нервно оглядывает класс."

    "Она определённо чувствует всеобщую хандру, но не может решить точно, что ей делать дальше."
    
    show misha sign_confused
    with ease_decel

    "Внезапно её бросает вперёд."
    
    show misha perky_sad 
    with charachange

    mi "Эй!"
    
    show shizu invis behind misha at Position(xanchor=0.5, xpos=1.0)
    with None

    show misha perky_sad at twoleft 
    show bg school_scienceroom at center 
    show shizu adjust_happy at tworight 
    with dissolvecharamove

    "Миша вваливается в классную комнату, а за ней показывается толкнувшая её %(name_shizune)s, всё ещё держа перед собой вытянутую руку."
    
    show shizu basic_normal at tworight 
    with charachange

    shi "…"

    hi "Спасибо за представление, но, может, вы уже займёте свои места?"
    
    show shizu behind_frown at tworight 
    with charachange

    shi "…"

    "Всё ещё немного выбитая из колеи, Миша несколько секунд пребывает в замешательстве, прежде чем понять, что она должна перевести."
    
    show misha sign_smile at twoleft 
    with charachange

    mi "О! Да! %(name_shizuchan)s говорит, что она недовольна тем, что ты бросил нас на прошлой неделе."
    
    show misha cross_frown at twoleft 
    with charachange

    mi "Мы были очень заняты!"

    hi "Вот, значит, как? А как насчёт того, что я уже сделал для вас двоих?"
    
    show shizu cross_angry at tworight 
    with charachange

    shi "…"
    
    show misha hips_grin at twoleft 
    with charachange

    mi "Она говорит, что это имеет значение только для членов Совета. А так как ты отказался вступать, то она ничем тебе не обязана."
    
    show misha hips_grin_close at twoleft 
    with characlose

    "Миша наклоняется ближе и заговорщицки шепчет мне на ухо."

    mi "Я думаю, что она просто немного обиделась, так как ты не провёл этот день вместе с ней."
    
    show misha hips_smile_close at twoleft 
    with charachange

    mi "На самом деле %(name_sicchan)s очень благодарна за твою помощь на прошлой неделе."
    
    show shizu behind_frustrated at tworight 
    with charachange

    "Чувствуя, что говорят о ней, %(name_shizune)s постукивает пальцами по столу, пока Миша наконец не оборачивается."
    
    show misha sign_smile at twoleft 
    with charadistant

    show shizu basic_angry at tworight 
    with charachange

    show misha hips_grin at twoleft 
    with charachange

    show shizu adjust_blush at tworight 
    with charachange

    "Я не могу понять значения ни одного быстро меняющегося жеста, но по немного смущённому выражению %(name_shizune)s да плохо сдерживаемому смеху Миши вполне могу догадаться."

    stop music fadeout 8.0
    
    "В то время как происходит этот диалог, дверь снова открывается, но на сей раз в приемлемом темпе."
    
    show hanako invis at offscreenright 
    with None

    show bg school_scienceroom at bgleft 
    show shizu basic_normal at Position(xpos=0.42) 
    show misha hips_smile at Position(xpos=0.18) 
    show hanako emb_downtimid at right 
    with dissolvecharamove

    "Прикрывая за собой дверь, тихо входит Ханако."
    
    show hanako emb_timid at right
    with charachange

    "Выглядывая из-под волос, она быстро осматривает класс."

    "Когда наши взгляды встречаются, Ханако вдруг замирает. Она закрывает глаза, делает глубокий вдох, а затем подходит к моей парте."
    
    show hanako cover_distant at right
    with charachange

    ha "Д… доброе утро, Хисао."

    hi "Доброе, Ханако. Ты немного припозднилась."

    "Кстати, на моей памяти я впервые пришёл раньше неё."
    
    show hanako basic_normal at right
    with charachange

    ha "Я… я разговаривала с Лилли."
    
    show hanako basic_worry at right
    with charachange

    ha "Н-насчёт сегодняшнего дня."

    hi "А, значит, ты взяла у неё список? В таком случае мы можем отправляться сразу после занятий."
    
    show hanako emb_smile at right
    with charachange

    ha "К-конечно."

    hi "С нетерпением буду ждать."

    "Лицо Ханако на мгновение озаряется смущённой улыбкой, а затем она спешит к своему месту."
    
    scene bg school_scienceroom at bgright 
    with shorttimeskip

    play music music_normal fadein 3.0

    "Во время занятий становится ясно, что не только ученики чувствуют себя вялыми после фестиваля."

    "Муто, просто дав нам список упражнений из учебника, усаживается за стол."

    "Сегодняшний день настолько наполнен рутиной, что я на краткий миг забываю даже о большой перемене."
    
    play sound sfx_normalbell

    "Это настолько отупляет, что все кажутся удивлёнными, когда колокольный звон возвещает об окончании уроков."
    
    show shizu basic_normal at tworight 
    show misha perky_smile at twoleft 
    with charaenter

    "Пока я собираю портфель, меня окружают %(name_shizune)s и Миша."
    
    show misha hips_grin at twoleft 
    with charachange

    mi "Эй, %(name_hicchan)s, ещё не поздно к нам присоединиться. После фестиваля накопились пачки документов, которые нужно разобрать."

    hi "Э-э, извини, Миша, у меня… есть планы…"
    
    show hanako invis at offscreenright 
    with None

    show bg school_scienceroom at center 
    show shizu basic_normal at Position(xpos=0.42) 
    show misha hips_grin at Position(xpos=0.18) 
    show hanako cover_distant at right 
    with dissolvecharamove

    "Будто почувствовав неладное, Ханако появляется у меня за спиной, держа небольшую сумку и стараясь не встречаться ни с кем взглядом."
    
    show misha cross_laugh at Position(xpos=0.18) 
    with charachange

    "У Миши расширяются глаза, и она разражается смехом."

    mi "БВА-ХА-ХА! А ты не теряешь время, %(name_hicchan)s~? Что ж, не будем мешать твоим сегодняшним планам! А-ха-ха-ха!"
    
    show shizu behind_blank at Position(xpos=0.42)
    with charachange

    "Позади хохочущей Миши я вижу %(name_shizune)s, абсолютно не интересующуюся развернувшейся сценой. Быть может, конечно, я ошибаюсь, но думаю, что она сознательно меня игнорирует."

    show hanako emb_downtimid_close at right
    with characlose
    
    "Я чувствую, что кто-то аккуратно тянет меня за рубашку. Обернувшись, я вижу уставившуюся в пол Ханако."
    
    show hanako emb_timid_close at right
    with charachange

    ha "П… пойдём…"

    hi "Ладно. %(name_shizune)s, Миша, до скорого."

    hi "И я по-прежнему не заинтересован во вступлении в Совет."
    
    show misha cross_grin at Position(xpos=0.18) 
    with charachange

    mi "Зануда."
    
    stop music fadeout 2.0

    hide misha 
    hide shizu 
    with charaexit

    show bg school_scienceroom at bgleft 
    show hanako emb_timid_close at center 
    with charamove

    "Оживлённо друг другу жестикулируя, Миша и %(name_shizune)s выходят в коридор."

    hi "Все вещи взяла? Тогда не будем задерживаться."

    play music music_soothing fadein 4.0

    scene bg school_gate 
    with locationskip

    "Ученики волнами покидают школьные ворота и устремляются по дороге в город."

    "Я заметил странную вещь. Снаружи «Ямаку» выглядит абсолютно так же, как и любая другая старшая школа, но эта иллюзия исчезает, как только на глаза попадается кто-нибудь в инвалидной коляске или с отсутствующей конечностью."

    "А ещё я замечаю, что никто тут не ходит в одиночку."
    
    scene bg school_road 
    with locationchange

    show hanako emb_downsad_close at center 
    with charaenter

    "Как только мы с Ханако проходим через ворота, я обращаю внимание на то, что она сокращает дистанцию между нами."

    "Это ещё не «рядом», но уже и не то слегка отстранённое расстояние, которое она обычно выдерживает."

    "Полагаю, мы ещё недостаточно знакомы, чтобы идти настолько же близко ко мне, насколько она ходит с Лилли."

    "Однако, хоть физически она и сокращает расстояние между нами, мысленно она будто где-то далеко."

    "Её руки так сильно стискивают кожаные ремешки портфеля, что видно, как белеют костяшки пальцев. Она идёт опустив вниз голову и плотно сжав губы."

    "У неё такой вид, будто её вызвали в кабинет директора."

    "Я пытаюсь подавить смешок при этой мысли, но безуспешно."
    
    show hanako emb_timid_close 
    with charachange

    ha "Ч-что случилось?.."

    "Думаю, нет смысла это скрывать…"

    hi "Извини. Ты выглядишь так, будто попала в неприятности."

    show hanako defarms_strain_close 
    with charachange

    ha "Ч-ч-что ты имеешь в виду?"

    hi "Мне кажется, тебе стоит немного успокоиться. Мы же не уходим слишком далеко, да и вокруг только ученики, верно?"
    
    show hanako def_worry_close 
    with charachange

    ha "В-верно."

    "Не нравится мне, когда Ханако так взвинчена."
    
    hi "Тем более ты ведь это каждую неделю делаешь?"
    
    show hanako basic_worry_close 
    with charachange
    
    ha "Д-да. С Лилли."
    
    "Конечно. «С Лилли». Интересно, она когда-нибудь покидала школу без неё?"
    
    "Казалось бы, ничего особенного в этом нет, но зависимость Ханако от Лилли до абсурдного сильна."
    
    "Если она не может даже отлучиться без неё из школы, как бы она выжила, если бы они не встретились?"
    
    "Хотя, возможно, я преувеличиваю."
    
    hi "Ну, я с тобой. Кроме того, далеко мы не пойдём и вернёмся не успеешь и глазом моргнуть."

    show hanako emb_downsmile_close 
    with charachange

    "Ханако перестаёт так сильно стискивать ремешки. Её попытки скрыть робкую улыбку приводят к прекращению нашей беседы."
    
    "Мы бок о бок идём по петляющей дороге в город. По мере приближения к нашему месту назначения толпа студентов становится всё реже."
    
    "Некоторые учащиеся мчатся вперёд, а менее мобильные отстают, из-за чего толпа постепенно редеет."
    
    scene bg suburb_konbiniext 
    with locationskip
    
    "До магазина мы добираемся практически в одиночестве."

    scene bg suburb_konbiniint
    with locationchange

    "Используя меня как щит между собой и работниками магазина, Ханако движется по узким проходам, складывая товары согласно списку в свою корзину."

    "Хлеб, молоко, чай… тимьян?"

    "Что это за магазин такой, в котором продаются даже сушёные травы?"

    "С другой стороны, ничто в этом городе не кажется нормальным. В общем-то, это не так уж плохо."

    "Всё настолько необычно и непривычно, что закрывать глаза на это не очень получается."
    #..."confronting"? Wtf did you mean by this, crud... -SC

    "От города мои мысли невольно перескакивают на Ханако."

    "Не смотреть на её шрамы не получается; стоит мне только взглянуть на них, как я перестаю думать обо всём остальном."

    "Пусть и не хочется себе в этом признаваться, кажется я силой заставляю себя отводить от них взгляд."
    
    "Но, так или иначе, её шрамы напоминают мне о том, что мы все здесь не без причины."

    "…"

    "Ханако бросает последний предмет из списка в корзину и смущённо протягивает мне деньги."

    show hanako emb_downtimid_close
    with charaenter

    ha "Не м-м-мог бы ты, п-пожалуйста…"

    "Мне даже не сразу удаётся понять, чего она хочет."

    hi "А, ты хочешь, чтобы я оплатил покупки?"
    
    show hanako emb_downsad_close 
    with charachange

    "Она кивает, не поднимая глаз."

    "Полагаю, эту задачу обычно выполняет Лилли."

    hi "Конечно. Только позволь мне ещё кое-что взять…"

    "Я торопливо хватаю несколько необходимых мне продуктов и направляюсь к кассам с Ханако на буксире."

    "Продавец безразлично кивает мне, пробивая наши товары на кассе."

    "Способность не обращать внимания – залог спокойного соседства с «Ямаку». Ученики, должно быть, часто посещают этот магазин, так как он расположен ближе всех к школе."
    
    "Персонал, видимо, обучен тому, как правильно вести себя с такими, как мы. А может, и нет. И я единственный, кто постоянно думает об «уникальности» моих одноклассников."

    stop music fadeout 2.0

    scene bg suburb_konbiniext_ss 
    with locationchange
    
    "Наши покупки закончены, потому мы с Ханако выходим на улицу."

    scene bg school_road_ss 
    with locationskip

    play music music_tranquil fadein 10.0

    "Дорога довольно пустынна. Все покинувшие «Ямаку» ученики уже разошлись, и пока никто из них не начал возвращаться."

    "И на дороге, ведущей к школе, кажется, никого нет."
    
    show hanako def_worry_close_ss at center 
    with charaenter

    "Отсутствие людей сразу отражается на поведении Ханако: её руки опущены – в них она держит пакеты, – глаза смотрят прямо…"

    "Кажется, будто она наслаждается прогулкой."

    hi "Так к чему все эти странные покупки? Тимьян? Мне это слово и выговорить-то трудно, а уж в какие блюда его добавляют – и подавно не знаю…"
    
    show hanako basic_normal_close_ss 
    with charachange

    ha "Я… иногда… г-готовлю."

    hi "Ну, да. Я тоже, но… тимьян?"

    hi "Это ведь несколько более продвинутый уровень, да?"

    show hanako emb_blushing_close_ss 
    with charachange

    ha "Н-не совсем."

    hi "Ну, я думаю, готовить – это классно. Научишь меня как-нибудь?"

    show hanako emb_smile_close_ss 
    with charachange

    ha "Н-никаких проблем."

    "Что-то сомневаюсь я, что она не видит в этом никаких проблем, но с моей стороны будет мудро не заострять на её фразе внимание."

    "По крайней мере, теперь она выглядит намного счастливее, чем по дороге сюда."

    "Одно это дарит мне радость."

    scene bg school_dormext_full_ss 
    with shorttimeskip

    show hanako basic_normal_close_ss 
    with charaenter

    "Около женского общежития мы с Ханако разбираем пакеты с нашими покупками."

    "Если сравнить, то мои продукты выглядят значительно проще."

    hi "Ты меня ставишь прямо-таки в неловкое положение, честное слово…"
    
    show hanako defarms_shock_close_ss 
    with charachange

    ha "Н-нет, я не… Я только…"

    hi "Я просто шучу."
    
    show hanako def_worry_close_ss 
    with charachange

    hi "У меня куча не сделанной с прошлой недели домашней работы, поэтому мне нужно идти."

    hi "Ты сможешь сама донести пакеты до своей комнаты?"
    
    show hanako cover_bashful_close_ss 
    with charachange

    ha "Д-да."

    hi "Уверена? Ну ладно. Тогда увидимся завтра."
    
    show hanako basic_smile_close_ss 
    with charachange

    ha "П-пока."
    
    hide hanako 
    with charaexit

    stop music fadeout 7.0

    "Мы расходимся, и я возвращаюсь в свою комнату."

    scene bg school_dormhisao_ss 
    with locationskip

    "На моём столе лежит куча бумаг, с которыми нужно разобраться. Прошлая неделя была такой суматошной, что я просто не успевал ничего сделать вовремя."

    "Пока лежал в больнице, я старался не отставать в учёбе, но часть этого материала я никогда раньше не видел, даже в прежней школе."

    "Совершенно неподготовленный, я открываю банку с напитком и сажусь за работу."
    
    scene black 
    with dissolve

    return

    #---------------------------------------------------------
      
label ru_H4:
    
    scene black 
    with None

    play music music_daily fadein 6.0

    scene bg school_dormhisao 
    with openeye #locationchange

    "Дни становятся жарче."

    "Этим утром я просыпаюсь покрытый потом. Это немного расстраивает, если ты один."
    #What. -SC

    "К тому времени, как ученики покидают свои общежития, направляясь либо в столовую, либо разбираться со своими утренними обязанностями, солнце уже припекает вовсю. Как ни странно, это поднимает мне настроение."

    "Ещё даже нет восьми, но я уже чувствую, что этот день будет приятным, спокойным и тёплым."

    "Если бы я не учился в школе, в которой каждое отсутствие в классе расценивается как признак угрожающей жизни ситуации, то предпочёл бы провести этот день на холме подле беговой дорожки."

    "Да, сегодняшний день действительно переполнен ленью."
    
    "Начав потягиваться, я вдруг вспоминаю предупреждение фельдшера о необходимости выполнения физических упражнений. Может, мне всё же стоило начать бегать по утрам?"
    
    "Непросто было бы начать бегать с такой, как Эми, но если бы я это делал в своём собственном темпе…"
    
    "Да кого я обманываю? Не имея стимула, я вряд ли смогу заставить себя заниматься."
    
    "Это не значит, что я буду просто целыми днями просиживать стул. Ведь даже поход в магазин можно счесть упражнением, верно? Особенно учитывая подъём в гору…"
    
    "Конечно, это не серьёзные разминки. Но, по сравнению с проведёнными на больничной койке месяцами, я получаю достаточно физических нагрузок."

    scene bg school_scienceroom 
    with shorttimeskip

    "Похоже, не я один наслаждаюсь сегодняшним днём."

    "Практически все в классе нет-нет да бросают взгляд в окно на манящее ясное небо."

    "Даже всегда пребывающая в боевом настрое %(name_shizune)s сегодня выглядит не такой бодрой, какой обычно бывает во время уроков."

    "Миша же, как и всегда, без комплексов. Расстегнув верхние пуговицы своей рубашки, она обмахивает себя тетрадью."

    "Видимо, я пялюсь слишком открыто, поэтому она показывает мне язык."

    "Тем не менее, ничуть не стесняясь моего взора, она продолжает делать то же, что и раньше."
    
    play sound sfx_normalbell

    "Похоже, что сигнал к большой перемене застаёт всех врасплох, так что класс пустеет гораздо медленнее, чем обычно."

    "Видимо, жара забирает у всех остатки сил."
    
    stop music fadeout 8.0

    "Ну, или почти у всех."
    
    show hanako emb_emb 
    with charaenter

    ha "Х… Хисао?"

    hi "Привет, Ханако, чем займёмся сегодня?"

    "Ханако держит в руках коробочку с едой."

    "Не нужно быть гением, чтобы понять, на что она намекает."
    
    show hanako emb_smile 
    with charaenter

    ha "М-м… хочешь снова с нами перекусить?"
    
    show hanako basic_bashful 
    with charaenter

    ha "Я… я принесла достаточно – хватит на всех…"

    hi "Круто. Но тебе не стоит так уж сильно напрягаться из-за подобного."
    
    show hanako basic_normal 
    with charaenter

    ha "А… хорошо."

    hi "Полагаю, мы направляемся в чайную комнату?"
    
    show hanako cover_worry 
    with charaenter

    ha "П… пожалуй."
    
    show hanako basic_normal 
    with charaenter

    ha "Лилли сказала, что встретит нас уже там, так что нам стоит… стоит…"

    hi "Стоит?"
    
    show hanako emb_smile at center 
    with charaenter

    ha "…стоит пойти туда вместе…"

    hi "Я не против. К тому же я очень проголодался из-за этой жары."

    "Ханако с облегчением вздыхает, и я собираю свои вещи."

    scene bg school_miyagi 
    with locationskip

    play music music_happiness fadein 1.0

    "Атмосфера в чайной комнате, как обычно, освежающая. Чувствуется полная уединённость от всего мира."

    "С другой стороны, может быть, именно благодаря этой породившей всеобщую вялость духоте, давно ставшая обыденной школьная возня едва долетает до наших ушей."

    "Ханако, будто пытаясь отвлечься от своих мыслей, медленно и аккуратно раскладывает на столе еду."

    "Блюда довольно скромные, но Ханако, судя по тому, как бережно она накладывает, готовила всё с любовью."

    hi "Лилли, видимо, ещё не пришла. Начнём без неё?"
    
    show hanako emb_timid at centersit
    with charaenter

    ha "О-она скоро будет…"
    
    show hanako emb_downtimid at centersit
    with charachange
    
    "Ханако пытается совладать с крышкой от коробочки с рисом."
    
    hi "Давай я помогу…"
    
    "Взяв контейнер из рук Ханако, я пытаюсь снять крышку."
    
    "Я стараюсь как могу, но она закрыта слишком плотно."
    
    hi "Дай угадаю: ты закрывала коробочку, когда рис был ещё горячим?"
    
    show hanako emb_sad at centersit
    with charachange
    
    ha "Д-да. Я торопилась…"
    
    "Я опускаю контейнер на стол."
    
    hi "Я так и думал. Похоже, она присосалась. Нам понадобится немного горячей воды, чтобы её открыть."
    
    hi "Но тут этим заняться у нас не получится: устроим нехилый потоп."
    
    li "Тогда как насчёт того, что сегодня я вас угощу?"

    show lilly invis at left 
    with None

    show hanako emb_smile at tworightsit
    show bg school_miyagi at bgright 
    show lilly basic_cheerful at twoleft 
    with dissolvecharamove

    "В дверях стоит Лилли. Она держит пакет, наполненный всякими булочками и рогаликами."
    
    show lilly basic_smileclosed at twoleft
    with charachange

    li "Это подарок от Юко в благодарность за мою вчерашнюю помощь."

    li "Поскольку из-за меня у вас изменились планы, я решила разделить добычу с вами…"

    hi "Лилли, ты нас спасла. Давай помогу разложить…"
    
    show lilly basic_smileclosed at twoleftsit
    with charamove

    "Благодаря предусмотрительности Лилли, на тарелке Ханако, так и не увидевшей риса, появляется различная выпечка. Я торопливо завариваю чай, чтобы завершить картину."

    hi "Не терпится приступить: всё такое аппетитное."

    show hanako emb_downtimid at tworightsit
    with charachange

    "Делая первый укус, я замечаю, что Ханако пытается украдкой посмотреть на мою реакцию."

    "На вкус ничего особенного, но не мне жаловаться, ведь я предпочитаю готовить на скорую руку."

    hi "Недурно. Полагаю, приготовлено из тех продуктов, что мы вчера купили?"
    
    show hanako emb_blushtimid at tworightsit
    with charachange

    ha "Д-да."
    
    "Глаза Ханако будто ждут от меня ещё какой-нибудь реакции."

    hi "Тогда наш поход в магазин стоил того. Спасибо, Ханако."
    
    show hanako cover_bashful at tworightsit
    with charachange

    ha "Я… я хотела показать тебе это… после вчерашнего…"

    hi "Всё в порядке, просто я был немного удивлён набором продуктов."
    
    show lilly basic_weaksmile at twoleftsit
    with charachange
    
    li "Ханако никогда не упустит шанса поэкспериментировать, когда дело касается еды."

    li "Я думаю, что это хорошо… иногда… время от времени"

    "Хоть улыбка Лилли и не меняется, небольшая перемена в тоне её голоса говорит мне, что в прошлом результаты были не столь успешны."

    "И не похоже, что у Ханако есть много знакомых, которых можно угостить её стряпнёй…"
    
    stop music fadeout 7.0

    "Постойте… Лилли ждала, чтобы сначала попробовал я? Она не начинала есть, пока я не сказал, что еда Ханако съедобна…"

    "…Так, с этих пор лучше начать брать еду с собой."

    hi "Главное, что вкусно, правда?"
    
    show hanako basic_smile at tworightsit
    with charachange

    ha "П-правда."
    
    show lilly basic_smileclosed at twoleftsit
    with charachange

    "Лилли, довольная, что не первая опробовала творение Ханако, отточенными движениями приступает к еде."
    
    "Она осторожно ощупывает контейнеры, выхватывая из них еду своими длинными пальцами, словно манипулятором из автомата с плюшевыми игрушками."
    
    "Не желая отставать, я приступаю к еде."
    
    show hanako emb_downsmile at tworightsit
    with charachange
    
    "У Ханако другая тактика: дождавшись, когда мы с Лилли уберём свои руки от коробочки, она быстро берёт свою порцию."
    
    show hanako emb_smile at tworightsit
    with shorttimeskip

    play music music_dreamy fadein 4.0
    
    "Вскоре все коробочки с едой пустеют, за исключением всё ещё закрытого контейнера с рисом."
    
    show lilly basic_smile at twoleftsit
    with charachange
    
    li "Спасибо за сытный ланч, Ханако."
    
    show hanako basic_smile at tworightsit
    with charachange

    ha "Н-нет… спасибо за булочки…"

    hi "Да, если бы не они, то на всех бы не хватило."
    
    show lilly basic_planned at twoleftsit
    with charachange

    li "Всегда пожалуйста."
    
    show lilly basic_weaksmile at twoleftsit
    with charachange

    li "Но теперь мне нужно возвращаться. Здесь так хорошо, что немудрено и опоздать."

    hi "Да, понимаю. Мы немного приберёмся и тоже пойдём."
    
    show lilly basic_smileclosed at twoleft 
    with dissolvecharamove

    li "Что ж, хорошего вам дня."
    
    hide lilly 
    with charaexit
    
    show hanako basic_smile at centersit
    show bg school_miyagi at center 
    with charamove

    "Постукивая тростью, Лилли удаляется прочь по тихому коридору."

    "Мы с Ханако, быстро собрав свои вещи, садимся в ожидании звонка."
    
    $ renpy.music.set_volume(0.5, 1.0, channel='music')

    scene bg misc_sky at Fullpan(20.0) 
    with locationchange

    "Наши взгляды устремлены в окно, в бесконечную небесную лазурь."
    
    play sound sfx_warningbell
    
    "Если бы не колокольный перезвон, я бы поклялся, что время остановилось."

    "Хорошо поев, я совсем не хочу никуда идти."

    "Я бросаю взгляд на Ханако, которая тоже не проявляет желания уходить."

    ha "Ну… ещё чуть-чуть…"
    
    $ renpy.music.set_volume(1.0, 3.0, channel='music')

    scene bg school_miyagi 
    show hanako basic_smile at centersit
    with shorttimeskipsilent

    "Промежуток между предупредительным звонком и звонком, возвещающим окончание большой перемены, проходит в мгновение ока."

    hi "Нам пора… люди будут волноваться и начнут нас искать, если мы пропустим…"
    
    show hanako basic_distant at centersit
    with charachange

    "Ханако вздыхает."
    
    show hanako basic_normal at centersit
    with charachange

    ha "Ты прав."
    
    show hanako basic_normal 
    with charamove

    "Она медленно поднимается на ноги, и я следую её примеру."
    
    scene bg school_staircase2 
    with locationskip

    "Молча мы проходим старую лестницу на третий этаж и идём в нашу классную комнату."
    
    scene bg school_hallway3 
    with locationchange

    play sound sfx_dooropen

    "У входа в класс я беру инициативу в руки и открываю дверь перед Ханако, заранее склоняя свою голову в извинении."
    
    scene bg school_scienceroom at center 
    with locationchange

    stop music fadeout 5.0

    hi "Извините, учитель, мы опоздали."
    
    play sound sfx_doorclose

    "Меня приветствуют не строгими словами и не возмущённой командой сесть, а лишь тишиной, созданной приблизительно пятнадцатью учениками, пытающимися не рассмеяться."

    show misha hips_grin
    with charaenter
    
    mi "Пф… пфва…"

    "Точнее, четырнадцать учеников пытаются, а у одной не получается."
    
    play music music_comedy

    show misha cross_laugh 
    with charachange

    mi "Пф-фаxaxaxa! Влюблённые голубки вернулись~!"
    
    show misha hips_laugh 
    with charachange

    "Мне всё тут же становится ясно."

    "Муто тоже опаздывает – его ещё нет."

    "Однако тот факт, что мы с Ханако опоздали и вошли в класс вместе, интересует всех гораздо больше."

    mi "BAXAXAXA~!"

    hi "Да-да. Спасибо. А теперь успокойся."
    
    hide misha 
    show hanako invis at Position(xpos=1.0)
    with charaexit

    show bg school_scienceroom at bgleft 
    show hanako emb_downsad_close at Position(xpos=0.8)
    with dissolvecharamove

    "Шагнув в класс, я понимаю, что Ханако крепко прижимается к моей спине, стараясь спрятаться от взглядов одноклассников."
    
    show hanako invis at Position(xpos=0.7)
    with dissolvecharamove

    "Пока я усаживаюсь, она, прикрывая лицо ладонями, устремляется к своей парте на заднем ряду."
    
    scene bg school_scienceroom at bgright 
    with charamove

    "По-быстрому проверив, не идёт ли учитель, я подхожу к парте Ханако и шепчу ей на ухо:"

    hi "Не бери в голову сказанное Мишей: она всегда такая. Я замечательно провёл сегодняшний день. Не беспокойся, ладно?"

    "Ханако кивает головой, держа её на сложенных на парте руках, но так и не поднимает ко мне лицо."
    
    play sound sfx_dooropen

    show muto invis at tworight 
    with None

    show muto normal 
    show bg school_scienceroom at center 
    with dissolvecharamove

    "Мне хотелось бы остаться и успокоить её, но внезапно в класс входит Муто, уже бурча лекцию, словно бы начал читать её ещё в коридоре."

    show muto smile
    with charaenter
    
    mu "…что, разумеется, прямо пропорционально заряду и обратно пропорционально квадрату расстояния…"
    
    hide muto 
    with charaexit

    play sound sfx_doorclose

    "Он настолько поглощён своей речью, что даже не замечает меня, крадущегося к своему месту от парты Ханако."

    return

#-----------------------------

label ru_H5:
    
    $ renpy.music.play(music_comedy, fadein=0.5, if_changed=True)
    
    scene bg school_scienceroom
    with None
    
    "В то время как Муто продолжает бубнить, Миша наклоняется ко мне."

    show misha invis at offscreenleft 
    with None

    show misha perky_smile_close at Position(xanchor=0.5, xpos=0.16)
    with dissolvecharamove

    mi "Если учитель и не заметил твоего опоздания, то я заметила."

    "Это-то ясно, ты ведь такую шумиху устроила."
    
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "Мне сказали, чтобы я от тебя отстала на сегодня, но только при одном условии."

    hi "Вот как? И каково условие?"

    show misha sign_smile_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "Сегодня вечером ты должен помочь нам~!"

    "Я вытягиваю шею, чтобы заглянуть Мише за плечо."

    "%(name_shizune)s старается не встречаться со мной взглядом."

    "Она, небось, ещё и начала бы насвистывать какую-нибудь беспечную мелодию, если б могла."
    
    hi "Ясно. Но только сегодня."
        
    hi "Я же тебе говорил уже, что не вступаю в Школьный совет, помнишь?"
    
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.16)
    with charachange
        
    mi "Конечно! Подобная вербовка членов может быть сочтена… э-э, сочтена…"
    
    show misha perky_confused_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    "Она заглядывает в свой блокнот, очевидно в поисках соответствующей формулировки."
    
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "…за принуждение и, следовательно, будет идти вразрез с правилами."

    hi "Как-то очень странно от тебя слышать, что ты придерживаешься каких-то правил."
    
    show misha sign_smile_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "Всё нужно делать по инструкции!"
    
    show misha perky_smile_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "Просто правила написаны ещё не для всех ситуаций, поэтому некоторые моменты могут быть проигнорированы."

    hi "И после этого вы удивляетесь, почему никто не хочет вступать в Школьный совет…"

    #maybe a Misha sprite with her sticking out her tongue cold be useful
    
    stop music fadeout 3.0

    show misha hips_frown_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    with Pause(0.3)

    show misha invis at offscreenleft 
    with dissolvecharamove

    hide misha 
    with None
    
    #how'd that request work out for you, crud?

    "Миша показывает мне язык и возвращается к своему учебнику. Мы продолжаем грызть гранит науки в течение оставшейся половины учебного дня."

    #SFX bells
    
    with shorttimeskip

    play sound sfx_normalbell

    show shizu invis at offscreenright 
    show misha invis at offscreenleft 
    with None

    show misha hips_smile_close at twoleft 
    show shizu behind_blank_close at tworight 
    with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

    "Не успеваю я встать, как %(name_shizune)s и Миша кладут руки мне на плечи."

    hi "Эй, я же сказал, что помогу, чёрт…"
    
    play music music_shizune fadein 1.0

    show misha hips_grin_close at twoleft
    with charachange

    mi "Это просто страховка, Хисао, страховка~!"
    
    show hanako invis at offscreenright behind shizu 
    with None

    show misha hips_smile_close at Position(xpos=0.17) 
    show shizu behind_blank_close at Position(xpos=0.5) 
    show bg school_scienceroom at bgleft 
    show hanako emb_timid at Position(xanchor=0.5, xpos=0.9)
    with dissolvecharamove

    ha "Х-Хисао?"

    "Ханако, пытаясь покинуть комнату, начинает робко обходить нас, и я вдруг понимаю, что она может стать моим единственным шансом сбежать."

    hi "О, Ханако. Что случилось?"
    
    show shizu basic_angry_close at Position(xpos=0.5) 
    with charachange

    shi "…"
    
    show misha hips_frown_close at Position(xpos=0.17) 
    with charachange

    mi "Эй, с чего ты взял, что у тебя есть время на болтовню?"

    hi "Да успокойся ты, это не займёт много времени… Извини, Ханако, что ты сказала?"
    
    show hanako emb_downtimid at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "Я… я собиралась пойти в библиотеку, и… и я подумала…"

    "Ханако перебирает большими пальцами, а её глаза порхают по комнате, глядя куда угодно, только не на нас."
    
    show misha sign_smile_close at Position(xpos=0.17) 
    with charachange
    
    mi "Извини, Ханако, но Хисао должен идти с нами. Для него есть работа."
    
    show shizu behind_smile_close at Position(xpos=0.5) 
    with charachange

    shi "…"
    
    show misha hips_grin_close at Position(xpos=0.17) 
    with charachange

    mi "О-о! Но, если захочешь, ты тоже можешь нам помочь."
    
    show hanako cover_worry at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "Э-э…"
    
label ru_choiceH5:
menu:
    with menueffect

    mi "А ты как считаешь, Хисао?"

    "{font=playtime_cyr2.ttf}Что скажешь, Ханако?{/font}":
        return m1

    "{font=playtime_cyr2.ttf}Я уже достаточно сделал для Совета.{/font}":
        return m2

label ru_H5_1:
    #-----------------------    
    
    show bg school_scienceroom at bgleft 
    show hanako cover_worry at Position(xanchor=0.5, xpos=0.9)
    show shizu behind_smile_close at Position(xanchor=0.5, xpos=0.5) 
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.17) 
    with None
    
    hi "Что скажешь, Ханако? Если взяться за работу вместе, то она не займёт много времени."
    
    show hanako emb_timid at Position(xanchor=0.5, xpos=0.9)
    with charachange

    "Волнение Ханако отвечает на мой вопрос прежде, чем она успевает сформулировать сам ответ."
    
    show hanako emb_downtimid at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "Мне… мне нужно идти…"

    "Что ж, этого следовало ожидать. Похоже, этим придётся снова заниматься мне и девочкам из Школьного совета."

    "Проще один раз подчиниться и освободить себя от дальнейших приставаний Совета."

    hi "Позже встретимся, хорошо?"
    
    show hanako emb_smile at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "Х-хорошо."
    
    stop music fadeout 3.0

    show misha hips_grin_close at twoleft 
    show shizu behind_smile_close at tworight 
    show hanako invis at offscreenright 
    show bg school_scienceroom at center 
    with dissolvecharamove

    show misha hips_smile_close at twoleft 
    hide hanako 
    with charachange

    mi "Ладно! Теперь, когда все прощания закончены, время для работы!"
    
    scene bg school_hallway3 
    with locationchange

    "Пока мы идём в комнату Школьного совета, Миша и %(name_shizune)s так и не отпускают моих плеч."

    "Я чувствую себя немного виноватым перед Ханако, но если это и есть цена того, чтобы к ней не приставала Миша, то я готов её заплатить."

    scene bg school_council
    with locationchange

    hi "Итак, чем займёмся сегодня?"
    
    show misha sign_smile
    with charaenter

    play music music_ease fadein 8.0

    mi "Аналитическое исследование!"

    hi "Да? А тебе не кажется, что этим обычно занимаются уже после чего-то?"
    
    show misha hips_grin 
    with charachange

    mi "Ага!"

    mi "Мы должны разобрать всю информацию о фестивале так, чтобы %(name_sicchan)s могла опросить учителей."
    
    show misha hips_grin at twoleft 
    show bg school_council at bgleft 
    with charamove

    show shizu adjust_happy at tworight 
    with charaenter

    "%(name_shizune)s, выложив передо мной на стол большую груду документов, сдержанно улыбается."
    
    show misha hips_smile at twoleft 
    with charachange

    mi "Ты должен отсортировать это в две стопки."
    
    show misha sign_smile at twoleft 
    with charachange

    mi "Одна по финансовым вопросам, например квитанции; одна по опросам; одна для позитивных откликов; ещё одна для того, с чем могут быть проблемы в следующем году; одна по вопросам, которые, вероятно, нельзя будет решить…"

    hi "Это несколько больше, чем две стопки…"

    show misha perky_confused at twoleft
    with charachange

    mi "А? И правда. Да, я думала, что будет только две стопки."

    mi "Виновата."

    hi "Ладно. Пока я буду сортировать, чем будете заниматься вы?"

    show misha hips_grin at twoleft
    show shizu adjust_smug at tworight
    with charachange

    mi "Мы пропустили ланч, потому что собирали все эти отчёты, поэтому мы собираемся пойти есть!"

    "Вы что, не могли отсортировать их сразу, пока собирали?.."

    "К счастью, во мне пробуждается чувство самосохранения, не позволяя мне открыть рот и тем самым ухудшить ситуацию."

    show misha perky_confused at twoleft
    with charachange

    mi "Э?!"

    show misha perky_sad at twoleft
    with charachange

    mi "Разве это справедливо?"
    
    show shizu behind_blank at tworight
    with charachange

    shi "…"

    "Я размышлял о несправедливом распределении работы и не заметил, что %(name_shizune)s продолжала жестикулировать."

    "Если бы не внезапное возмущение Миши, я, вероятно, не заметил бы этого вообще."
    
    show shizu adjust_smug at tworight
    with charachange

    show shizu basic_normal at tworight
    with charachange

    show shizu behind_blank at tworight
    with charachange

    "%(name_shizune)s выдаёт довольно длинную последовательность жестов, и ни один из них не выглядит приветливо."
    
    show misha sign_sad at twoleft
    with charachange

    show misha perky_sad at twoleft
    with charachange

    show misha perky_sad at twoleftsit
    with charamove

    "Придя к соглашению с подругой, Миша несколькими короткими жестами отвечает %(name_shizune)s, после чего садится рядом со мной за стол."
    
    show shizu adjust_happy at tworight
    with charachange

    hide shizu 
    with charaexit

    show misha perky_sad at centersit
    show bg school_council at center 
    with charamove

    "%(name_shizune)s машет нам рукой и исчезает за дверью."

    hi "И что всё это значит?"
    
    show misha perky_confused at centersit
    with charachange

    mi "%(name_sicchan)s боится, что ты напортачишь, если останешься без присмотра."
    
    show misha perky_sad at centersit
    with charachange

    mi "А поскольку она не сможет сказать тебе о местах, в которых ты ошибся, она заставила остаться меня."

    show misha cross_smile at centersit
    with charachange

    mi "Но она принесёт нам немного еды~!"
    
    show misha cross_grin at centersit
    with charachange

    mi "Как же это классно!"

    "Легкомысленность Миши просто непостижима. Из глубин уныния – на седьмое небо, и всего за жалкие несколько калорий."

    "Трудно представить, что кто-нибудь другой на её месте повёл бы себя подобным образом."

    hi "Ну, могло быть и хуже."

    hi "Так с чего начнём?"
    
    show misha sign_smile at centersit
    with charachange

    mi "С сортировки."

    hi "Это я уже понял."
    
    show misha hips_smile at centersit
    with charachange

    mi "В общем, начнём создавать стопки. А что с ними дальше делать, решим потом."

    hi "Понятно…"
    
    show misha perky_smile at centersit
    with charachange

    "Мы начинаем разделять заполненные бланки на всё большее и большее количество стопок."

    "В первую очередь просто по категориям: финансовые, отзывы, отчёты о происшествиях…"

    "Потом они раскладываются на хорошие и плохие отчёты и так далее, пока не создаётся впечатление, что мы только разбрасываем бумаги по всему столу."
    
    hi "Это безнадёжно."
    
    show misha perky_confused at centersit
    with charachange
        
    mi "А? Почему? Мы делаем то, что нам сказали, правильно?"

    hi "Да, но всё выглядит так, будто мы просто развели беспорядок."
    
    show misha hips_grin at centersit
    with charachange 

    mi "А, не волнуйся. Пусть %(name_shizune)s разбирается."
    
    show misha cross_grin at centersit
    with charachange 

    mi "Поэтому я думаю, что мы можем пока на этом остановиться."

    "Такое впечатление, будто здравый смысл Миши покинул комнату вместе с %(name_shizune)s."

    "Но спорить всё равно смысла нет."

    show misha perky_smile at centersit
    with charachange

    mi "Слушай…"
    
    show misha cross_smile at centersit
    with charachange

    mi "А что за дела у тебя с Ханако?"

    hi "Дела?"
    
    show misha hips_smile at centersit
    with charachange 

    mi "Ты же тусил сегодня с ней, не так ли~?"
    
    show misha hips_grin at centersit
    with charachange 

    mi "Между вами происходит что-то интересное? Может, есть какие-то слухи, что ты скрываешь от меня~?"

    hi "Если бы я рассказал вам о произошедшем с моей точки зрения, это уже не было бы слухом, не так ли?"

    show misha perky_confused at centersit
    with charachange

    mi "Нет, наверное…"

    hi "Полагаю, мы просто друзья."

    hi "Почему ты так интересуешься? Я думал, что она вам с %(name_shizune)s не нравится…"

    show misha cross_frown at centersit
    with charachange

    mi "Это не совсем так. Ты же знаешь, что %(name_sicchan)s и Лилли не ладят друг с другом."

    mi "Но, потому как Ханако почти всегда рядом с Лилли, у нас практически нет возможности пообщаться с ней."
    
    show misha sign_smile at centersit
    with charachange

    mi "Но это совсем не означает, что я не беспокоюсь о ней."

    hi "И о чём конкретно ты беспокоишься?"
    
    show misha perky_sad at centersit
    with charachange

    mi "Ну, она ни с кем не контактирует."

    "Если %(name_shizune)s и Лилли не нравятся друг другу из-за того, что не сошлись характерами, боюсь представить, как бы проходило общение между Мишей и Ханако…"

    show misha perky_confused at centersit
    with charachange
    
    mi "Я имею в виду, все мы здесь так или иначе в одной лодке, правильно~?"

    #But Misha's different...

    hi "Ну, предположим."
    
    show misha sign_smile at centersit
    with charachange

    mi "Однажды, когда она ушла из класса во время урока, %(name_sicchan)s подошла к учителю и спросила, как он собирается на это реагировать."

    show misha sign_confused at centersit
    with charachange
    
    mi "Он сказал, что в этой школе у каждого ученика есть свои особые потребности и что %(name_sicchan)s не должна волноваться по этому поводу."
    
    show misha perky_confused at centersit
    with charachange

    mi "Ханако никогда не делает задания в группах – она попросту сбегает."

    mi "Разве этих причин не достаточно, чтобы начать беспокоиться?"

    hi "Думаю, ты права. Она даже сейчас практически не отвечает, когда с ней пытаешься поговорить."
    
    show misha perky_sad at centersit
    with charachange

    mi "Ну, я ничего не могу с этим поделать. Мы с %(name_sicchan)s пытались с ней заговорить, когда она только начинала учиться, но она лишь испугалась и убежала."

    "Я подумываю сказать Мише, что абсолютно такая же ситуация произошла и со мной в начале знакомства с Ханако, но Миша кажется глубоко погруженной в мысли."

    "Слушать Мишу без влияния %(name_shizune)s… интересно."
    
    show misha cross_frown at centersit
    with charachange

    mi "Я думаю, она должна понять, что никого здесь не беспокоит то, как она выглядит, и что она вполне может довериться нам."
    
    show misha cross_smile at centersit
    with charachange

    mi "Если бы она смогла, то у меня бы груз с плеч свалился."

    "Я вдруг понимаю, что, когда %(name_shizune)s нет поблизости, Миша словно бы превращается в другого человека."

    "Пожалуй, я наблюдаю самый длительный диалог Миши без единого жеста."

    "Когда она рядом с %(name_shizune)s, её руки постоянно находятся в движении, переводя полученную информацию на язык жестов."

    "Что кажется непростым занятием даже для человека ясного ума."

    "А у Миши ум, честно говоря, не самый ясный."

    hi "Ну, раз ты так беспокоишься, то я присмотрю за ней."

    hi "Но тебе стоит извиниться перед ней за случай в классе. Не думаю, что Ханако оценила ту шутку по достоинству."

    show misha perky_confused at centersit
    with charachange

    mi "М-м? М-м~!"
    
    show misha perky_sad at centersit
    with charachange

    mi "Я даже внимания не обратила. Извини."

    hi "Скажи эти слова не мне, а ей."
    
    show misha perky_smile at centersit
    with charachange

    mi "Хорошо. Тогда завтра первым делом я с ней поговорю."
    
    hi "Вот и отлично."
    
    play sound sfx_doorslam
    with vpunch
        
    "Грохот со стороны двери возвещает о возвращении %(name_shizune)s."

    "Полагаю, она даже представить не может, сколько шума производит."

    show misha hips_grin at centersit
    with charachange

    mi "О, %(name_sicchan)s! Ты вернулась!"
    
    show shizu invis at Position(xanchor=0.5, xpos=1.0) 
    with None

    show misha hips_grin at twoleftsit
    show shizu behind_blank at tworight 
    show bg school_council at bgleft 
    with dissolvecharamove

    #So tempted to put in a "What took you so long thing to use the epic sprite, but will
    #refrain

    "%(name_shizune)s под завязку загружена товарами из минимаркета."
    
    show shizu basic_normal2 at tworight 
    with charachange

    shi "…"
    
    show misha sign_smile at twoleftsit
    with charachange

    mi "Это кое-какие излишки, оставшиеся после праздника. Поскольку по документам это относится к проведению фестиваля, мне удалось немного для нас урвать."
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "Хорошо сработано, %(name_sicchan)s. Десять очков."

    hi "Разве такое разрешено?"
    
    show shizu cross_angry at tworight 
    with charachange

    shi "…"
    
    show misha cross_frown at twoleftsit
    with charachange

    mi "Для человека, отказавшегося вступить в Школьный совет, ты, кажется, слишком интересуешься его политикой."
    
    show misha cross_grin at twoleftsit
    show shizu adjust_smug at tworight 
    with charachange

    mi "Видимо, мне стоит наказать тебя за сию дерзость и конфисковать часть твоей порции."

    hi "Хорошо, хорошо, я понял."
    
    show misha perky_smile at twoleftsit
    show shizu adjust_happy at tworightsit
    with dissolvecharamove

    "Миша смещает несколько стопок бумаги в сторону, чтобы освободить место под кучу принесённой %(name_shizune)s еды."

    "Увидев, что весь мой упорный труд пошёл насмарку, я понимаю, почему эти двое постоянно нуждаются в помощи."

    "Магазинная еда хоть и не шибко вкусная, но наесться ею вполне можно."
    
    show shizu behind_smile at tworightsit
    with charachange

    shi "…"
    
    show misha sign_smile at twoleftsit
    with charachange

    mi "Спасибо за помощь. Большую часть времени мы просто занимались заполнением отчётов за персонал."
    
    show misha perky_smile at twoleftsit
    with charachange

    mi "По крайней мере, в этом году мы смогли придумать заголовки для некоторых разделов, чтобы легче было проводить опрос."

    hi "Разве это не искажение фактов?"
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "Нисколько, нисколько. Мы следуем уставу. Ведь мы не виноваты в том, что правила не настолько чётко определены."

    hi "А я думал, что это как раз и означает искажение фактов…"
    
    show misha hips_smile at twoleftsit
    with charachange

    mi "Ты слишком много думаешь~!"

    hi "А знаешь что? Наверное, ты права."

    hi "В любом случае я должен откланяться…"

    hi "…то есть если мне это позволено."

    show shizu adjust_smug at tworightsit
    with charachange

    shi "…"
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "Твою работу можно считать выполненной. Можешь идти."

    hi "Ну спасибо."

    hi "И знаете, если бы вы делали акцент на возможности пользоваться привилегией бесплатных ланчей и не афишировали бесконечную загрузку работой, то, вероятно, уже обзавелись бы добровольцами."

    stop music fadeout 6.0

    show misha sign_smile at twoleftsit
    with charachange

    show shizu behind_blank at tworightsit
    with charachange

    mi "Может быть, ты и прав."

    hi "В таком случае подумайте об этом."

    hi "И над тем, о чём мы говорили… не переводи это %(name_shizune)s, если не хочешь."
    
    show misha perky_confused at twoleftsit
    with charachange

    mi "Что? Ах да. Я постараюсь увидеться с ней завтра."
    
    show misha perky_smile at twoleftsit
    with charachange

    mi "Спокойной ночи, %(name_hicchan)s."

    hi "Доброй ночи, Миша, %(name_shizune)s."
    
    scene black 
    with dissolve

    return
    
    #-------------
label ru_H5_2:
    
    show bg school_scienceroom at bgleft 
    show hanako cover_worry at Position (xanchor=0.5, xpos=0.9)
    show shizu behind_smile_close at Position(xanchor=0.5, xpos=0.5) 
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.17) 
    with None
    
    hi "Слушай, %(name_shizune)s. Знаю, что обещал помочь, но я забыл, что у меня уже есть планы на сегодня. Кроме того, я немало помогал вам на прошлой неделе, не так ли?"

    hi "Я обещаю, что помогу вам в другой раз."
    
    show misha sign_confused_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    show shizu basic_frown_close at Position(xanchor=0.5, xpos=0.5) 
    with charachange

    show misha perky_smile_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    show shizu behind_blank_close at Position(xanchor=0.5, xpos=0.5) 
    with charachange

    "Отпустив мои плечи, %(name_shizune)s и Миша долго и серьёзно беседуют."
    
    show misha sign_smile_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    mi "Ладно, как знаешь. Если честно, то мы просто хотели купить пирожных на остатки из выделенного на фестиваль бюджета и посидеть."
    
    show misha cross_laugh_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    mi "Так что, если ты не с нами, нам же лучше. Больше достанется. Ва-ха-ха-ха~!"
    
    stop music fadeout 6.0

    show shizu invis at offscreenleft 
    with dissolvecharamove

    show misha invis at offscreenleft 
    with dissolvecharamove

    hide shizu 
    hide misha 
    with None

    "%(name_shizune)s разворачивается и выходит в коридор, Миша следует за ней."

    hi "В общем, это оказалось намного легче, чем я думал. На прошлой неделе они преследовали меня, словно ищейки. Или тюремные охранники."

    hi "Или, может, как тюремные охранники, произошедшие от ищеек…"

    "Я не могу поверить, что подобные мысли пришли мне в голову, не говоря уже о том, что я их озвучил. Думаю, мне срочно нужно переселяться подальше от %(name_kenji)s."
    
    hi "…Не важно. Ну что, пойдём в библиотеку?"
    
    show hanako basic_smile at Position (xanchor=0.5, xpos=0.9)
    with charachange
        
    ha "А-ага."
    
    play ambient sfx_crowd_indoors fadein 0.5

    scene bg school_hallway3 
    show crowd 
    with locationchange

    "Ханако, укрываясь за моей спиной, следует за мной по переполненным коридорам."

    stop ambient fadeout 0.5
    play music music_happiness fadein 2.0

    scene bg school_library 
    show hanako invis at offscreenright 
    show yuuko neutral_down
    with locationchange

    show hanako basic_worry at tworight 
    with dissolvecharamove

    "Едва мы входим в дверь, как Ханако подбегает к прилавку, за которым Юко складывает книги."
    
    show hanako emb_emb at tworight 
    with charachange

    "Прежде чем я успеваю подойти, Ханако что-то шепчет ей на ухо."

    show yuuko neurotic_up 
    with charachange

    yu "М-м, возможно, ты найдёшь её в секции научной литературы, но наверняка не скажу. Если хочешь, можем заглянуть…"
    
    show hanako emb_downsad at tworight 
    with charachange

    ha "Н-не бери в голову."

    hi "Юко, это вы о чём?"
    
    show yuuko neutral_down 
    with charachange

    yu "О, Хисао… Ханако просто спросила про книгу о…"
    
    show hanako emb_blushing at tworight 
    with charachange

    ha "Н-ни о чём…"

    hi "«Книга ни о чём»? В секции научной литературы?"

    show hanako def_strain at tworight 
    with charachange

    ha "Я… я просто…"
    
    show yuuko neurotic_up 
    with charachange

    "Я перевожу взгляд на Юко. У неё такой вид, будто она лопнет от натуги из-за попыток не выдать секрет Ханако."

    hi "Юко, так что за…"

    show yuuko happy_down 
    with charachange

    yu "Шахматы! Она хотела найти книгу по шахматам!"

    "Я беру себе на заметку никогда не доверять Юко никакой важной информации."
    
    show hanako defarms_shock at tworight 
    with charachange

    ha "Ю-Юко…"
    
    show yuuko panic_up 
    with charachange

    yu "Прости, Ханако… само вырвалось…"

    hi "В общем, теперь это не секрет. Давай я тебе помогу. Мне тоже нужно освежить свои навыки."
    
    show hanako def_worry at tworight 
    with charachange

    ha "Х… хорошо."

    hide yuuko 
    with charaexit

    show hanako def_worry
    show bg school_library at bgleft 
    with charamove

    "Пристыженная Юко исчезает за прилавком, в то время как мы с Ханако углубляемся в секцию научной литературы."

    "Если я не ошибаюсь, то должна быть система для классификации подобных книг, но не понимаю, как хоть кто-нибудь сможет в ней разобраться, не потратив на это половину своей жизни."

    "Наверное, именно поэтому все мои знакомые библиотекари – неврастеники."

    #Dewey Decimal for Chess is 794.1, between magic tricks and educational games.

    "В конце прохода, между книгами с карточными фокусами и с какими-то детскими играми, стоит одинокая книжка под названием «Шахматная тактика для чемпионов»."

    show hanako basic_bashful 
    with charachange
    
    "Не успеваю я и глазом моргнуть, как она оказывается в руках Ханако, прижатая к груди."

    hi "В таком случае, полагаю, теперь она твоя. Не одолжишь её мне после того, как сама прочитаешь?"

    show hanako cover_worry
    with charachange

    ha "К-конечно. Я… я просто никогда ни с кем раньше не играла, потому и подумала…"

    "Вот чёрт! Не то чтобы я собирался намеренно обыграть Ханако, но она, похоже, восприняла это близко к сердцу."

    "С другой стороны, она, судя по всему, хочет сыграть со мной снова. Это же плюс, верно?"

    hi "Хах, ну это же не значит, что я гроссмейстер или что-то вроде того. Я просто немного играл перед…"

    "Мне приходит в голову, что я ни разу не говорил Ханако о своём состоянии. На секунду впав в замешательство, я раздумываю над тем, как выкрутиться. Сегодня – не лучший день для такого разговора."

    hi "…перед переездом в «Ямаку»."

    "Не хочется рассказывать Ханако о том, что играл я только в больнице с другими ребятами из соседних палат."

    "С ними тоже не особенно интересно было играть; старшему едва ли было пятнадцать."

    stop music fadeout 6.0

    show hanako cover_distant 
    with charachange

    #To be replaced with "concern" if it gets made.

    ha "Ты… ты в порядке?"

    hi "Ага, я просто кое-что вспомнил…"

    "Немного об этом подумав, я понимаю, что не должен бояться рассказать Ханако о времени, проведённом в больнице. Судя по её шрамам, ей, наверное, тоже долго пришлось пролежать на больничной койке."

    "Но по некоторым причинам я пока не могу об этом говорить, по крайней мере не сегодня. Сначала нужно всё хорошенько продумать."

    "Решив сменить тему, я беру первую попавшуюся книгу с полки."

    #791.068 – Amusement parks

    "Это книга о самых быстрых американских горках в мире…"

    "…изданная в 1982 году. Ну, не совсем актуальная, но должна быть достаточно интересной."

    hi "Мы выбрали книжки, пойдём займём места?"

    show hanako cover_bashful
    with charachange

    "Похоже, Ханако всё-таки поверила моему притворству, и мы направляемся в укромный уголок для чтения в конце библиотеки."
    
    hide hanako 
    with charaexit

    "Не сказав ни слова, мы просто открываем книги и приступаем к чтению."

    "Я старательно пролистываю свою книгу. Оказывается, что в 1982 году американские горки не были столь большими, как те, что строились в последующие десятилетия."

    "Большинство из них были сделаны из дерева. Не думаю, что рискнул бы на таких прокатиться."

    "А если бы я и решился проехать на чём-то потенциально опасном, то предпочёл бы, чтобы оно было сделано из стали или таких сплавов космической эры, как титан и рутений."

    "Я быстро теряю интерес к книге, и мой взгляд скользит по читальному сектору, пока не останавливается на Ханако."
    
    show ev hana_library_read
    with locationskip

    "Похоже, она поглощена чтением. Перелистывая взад-вперёд страницы, она будто пытается закрепить только что прочитанное. Интересно, это эффективная методика или она слишком уж сильно погрузилась в зубрёжку?"

    "Периодически она неосознанно убирает волосы с лица, обнажая свои шрамы."

    "Я всё ещё не уверен, можно ли с ней о них поговорить. Правильно ли вообще спрашивать о её шрамах? Или о её прошлом? О том, как много времени она провела в больнице? Посещает ли до сих пор доктора?"

    "Эти вопросы похожи на те, что задаёшь новичку, только перешедшему в твою школу. Правда, переиначенные на местный лад."

    "Но до настоящего времени никто не задал мне ни одного подобного вопроса. Ну, за исключением Рин. Но вряд ли её можно считать образчиком надлежащего поведения в обществе."

    "В этот раз я буду держать рот на замке. Если кто-то и захочет что-либо тебе рассказать о себе, то он сделает это сам. Попытка вызвать Ханако на откровенный разговор может заставить её снова замкнуться в себе."

    scene bg school_library_ss 
    show yuuko worried_up_ss at center 
    with shorttimeskip

    yu "М-м… извините, что прерываю, но я должна закрывать библиотеку."
    
    play music music_tranquil fadein 3.0

    hi "Уже?"

    "Я смотрю на свои часы. Действительно, пока я пребывал в размышлениях, прошло почти два часа."
    
    show yuuko smile_down_ss 
    with charachange

    yu "Хотите забрать с собой эти книги? Я могу записать их на выходе…"
    
    show hanako invis at Position(xpos=0.9, xanchor=0.5, ypos=1.17, yanchor=1.0)
    with None

    show hanako basic_worry_ss at Position (xpos=0.7)
    show bg school_library_ss at bgleft 
    show yuuko smile_down_ss at twoleft 
    with dissolvecharamove

    ha "П-пожалуйста."

    hi "Я пас. Оставлю её на полке по пути к выходу. Она оказалась не столь интересна, как я думал."
    
    show hanako emb_timid_ss at tworight 
    with dissolvecharamove
        
    "Ханако отмечает листком бумаги место, где остановилась, и встаёт. Девушки направляются к регистрационной стойке, а я возвращаю книгу на место."

    show yuuko neurotic_up_ss at twoleft 
    with charachange
    
    "Отработанным движением Юко считывает штрих-код книжки Ханако, но всё равно получается у неё это не сразу."
    
    show yuuko neutral_down_ss at twoleft 
    with charachange

    yu "О… ну наконец-то. С третьего раза удалось. Поскольку эта книга не из раздела художественной литературы, я могу выдать её только на неделю."

    show hanako basic_smile_ss at tworight
    with charachange

    ha "Н-ничего страшного."
    
    scene bg school_hallway2 
    with locationchange

    "Юко, выключив библиотечный компьютер, провожает нас до двери."

    show yuuko panic_up at twoleft 
    show hanako def_worry at tworight 
    with charaenter

    yu "Ой! Я не думала, что уже так поздно!.."

    hi "Но ты же сама только что сказала, что тебе нужно закрываться…"
    
    show yuuko worried_up at twoleft
    with charachange

    yu "Я знаю, но это было до того, как я посмотрела на время!"
    
    show yuuko neurotic_up at twoleft
    with charachange

    yu "Увидимся."

    hide yuuko 
    with easeoutleft

    "Быстрой походкой Юко устремляется по коридору, неуклюже таща за собой сумочку."
    
    show hanako def_worry
    show bg school_hallway2 at bgleft 
    with dissolvecharamove

    hi "Подозреваю, все библиотекари немного рассеянные."
    
    show hanako emb_timid 
    with charachange

    ha "Что?"

    hi "А, неважно. Я просто подумал, что никогда не встречал библиотекаря, который может распланировать свой день. Независимо от того, насколько легко он обращается с книгами."

    show hanako basic_smile
    with charachange

    ha "О… хе-хе… Я п-понимаю, о чём ты…"

    #Geh I need to know how to verbalise a short laugh without using "heh"

    "Что это было? Ханако только что усмехнулась? Я не пытался пошутить, но, видимо, напомнил ей о каком-то другом библиотекаре… или о ком-то ещё…"
    
    show hanako cover_worry 
    with charachange

    ha "Мне… мне пора возвращаться."

    hi "Ага, мне тоже. Я и не заметил, что уже так поздно. Спасибо, что провела со мной время."
    
    show hanako basic_bashful 
    with charachange

    ha "Не за что."

    hi "Кстати, как ты смотришь на то, чтобы я проводил тебя до общежития? Нам всё равно по пути."

    show hanako emb_blushing
    with charachange

    ha "Х-хорошо."
    
    hide hanako 
    with charaexit

    "Ханако устремляется вперёд, и мне приходится чуть ли не бежать, чтобы поравняться с ней."

    scene bg school_dormext_full_ss 
    with locationchange

    show hanako def_worry_ss 
    with charaenter
    
    stop music fadeout 6.0

    "Мы проходим через сквер и наконец оказываемся перед зданиями общежитий."

    hi "Вот и пришли. Увидимся завтра в классе?"
    
    show hanako emb_smile_ss 
    with charachange

    ha "К-конечно."

    hide hanako 
    with charaexit

    "Ханако, прежде чем войти в двери общежития, на прощание коротко машет мне рукой."
    
    scene black 
    with dissolve

    return


#-------------------------------

label ru_H6:
    
    scene bg school_dormhisao 
    with openeye

    "Птицы щебечут."

    "Обычно в такие моменты хочется размышлять над красотой природы."

    "Но на часах только шесть утра."
    
    play sound sfx_pillow

    scene black 
    with Dissolve(0.2)

    "Накрыв голову подушкой, я утыкаюсь лицом в матрас, надеясь, что немедленно снова засну."

    "Как наивно."

    "Я ворочаюсь с боку на бок, но сон так и не возвращается."
    
    play music music_daily fadein 10.0

    scene bg school_dormhisao 
    with locationchange

    "Всё, природа, ты победила. Видишь? Я уже встаю…"

    "Недосып клонит голову вниз, и есть только одно средство от этого – хороший плотный завтрак."

    $ renpy.music.set_volume(0.29999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 0.5

    scene bg school_cafeteria 
    with locationchange

    "Было бы неплохо быть тут первым посетителем."

    "Первым, чтобы набрать свежеприготовленной, ещё горяченькой еды и усесться там, где душе угодно…"

    "Да, было бы здорово."

    "Но даже мой исключительно ранний подъём не помог мне быть первым среди самых прилежных учеников."

    "Полагаю, есть немало людей, которые по той или иной причине встают ни свет ни заря."

    "Группа учащихся в спортивной форме толпится вокруг одного из столов, нетерпеливо обсуждая планы на игру в перерывах между едой."

    "Также в зале попадаются школьники с заспанными глазами, поднятые в такую рань теми же птицами, что и я."

    "И, конечно, есть те, кто просто любит рано вставать. Такие тут обычно появляются с портфелями, набитыми учебниками и выполненной домашней работой."

    "Трудно не проникнуться ненавистью к таким людям, особенно когда чувствуешь себя таким невыспавшимся."

    "Обнаружив знакомое лицо в этом столпотворении, я направляюсь к ближайшему столику."

    "Сидя в одиночестве, Лилли аккуратно прощупывает вилкой маленькую тарелку с яичницей."

    "Прервать её движения, напоминающие своей точностью часовой механизм, – точно совершить преступление."

    "Вот, значит, как выглядят машинальные движения у незрячих? Они просто совершают закрепившиеся в мышечной памяти за годы движения, так же, как любой зрячий, почитывающий газету за завтраком."

    hi "Доброе утро, Лилли. Я не ожидал тебя встретить здесь в столь ранний час."

    show lilly basic_surprised at centersit
    with charaenter

    li "О, Хисао, ты напугал меня. Я и не знала, что ты так рано завтракаешь."

    hi "Не завтракаю. Сегодня – скорее исключение из правил. Я предпочёл бы опоздание в школу раннему подъёму на завтрак."

    show lilly basic_weaksmile at centersit
    with charachange

    li "Знаешь, как говорят: «Лучший отдых – смена деятельности»."

    hi "Да говорят вообще много всякого…"
    
    show lilly basic_ara at centersit
    with charachange

    li "И то верно."

    "Мне сейчас, честно говоря, не до бесед. Нужно чем-нибудь подкрепиться, иначе мыслительный процесс совсем остановится."

    "Активировать режим работы вилкой."
    
    show lilly basic_weaksmile at centersit
    with charachange

    "Лилли продолжает механически кушать завтрак."

    "Её движения словно лишены жизненной энергии. Полагаю, они сродни блуждающему взгляду во время выполнения повседневных рутинных дел."

    "Но после нескольких циклов поиска и последующего принятия пищи Лилли откладывает в сторону вилку и вытирает губы салфеткой."
    
    #maybe spelling things out a little too much here.
    #also might be a little too perceptive for dipshit Hisao
    # It's okay.

    stop music fadeout 6.0
    stop ambient fadeout 6.0

    show lilly basic_concerned at centersit
    with charachange

    li "Хисао, ты не против, если я задам тебе вопрос?"

    "Чёрт. Я был бы не против немного поесть и ещё часа четыре поспать. К тому же лёгкие вопросы не начинаются со слов: «Ты не против, если я задам тебе вопрос?»"

    hi "Конечно."
    
    show lilly basic_listen at centersit
    with charachange

    li "Считаешь ли ты Ханако своим другом?"

    "Хм, это похоже на наводящий вопрос."

    hi "Я… полагаю, да. Почему ты спрашиваешь?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Без особых причин."
    
    show lilly basic_displeased at centersit
    with charachange

    play music music_serene fadein 8.0

    li "Почему?"

    li "Почему ты думаешь о ней как о друге?"

    "Это уже выше моего понимания. Что она ожидает от меня услышать?"

    hi "Я правда не знаю. Может быть, потому что она немного по-другому воспринимает общение с людьми…"
    
    show lilly basic_reminisce at centersit
    with charachange

    li "Хм-м. С тех пор как я с ней познакомилась, она действительно ни с кем не дружила."
    
    show lilly basic_concerned at centersit
    with charachange

    li "По ней не скажешь, что она интересуется другими людьми, и я думаю, что люди немного боятся её внешности."

    hi "Действительно? Я думал, что такие вещи здесь никого не могут смутить. Ведь это уже дискриминация."

    show lilly basic_listen at centersit
    with charachange

    li "Хм-м, если выразиться одним словом…"

    "Нахмурившись, она задумывается. Меня беспокоит то, что у неё на уме."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Я сказала бы, что ты немного наивен."

    "Наивен? Я был бы оскорблён, если бы не лёгкая улыбка на её лице."

    hi "П… понимаю."
    
    show lilly basic_reminisce at centersit
    with charachange

    li "Даже невзирая на то, что в «Ямаку» более сплочённый коллектив по сравнению с другими школами, здесь тоже временами не удаётся избежать конфликтов."

    "На самом деле я это и сам заметил."

    "Некоторые ученики избегают друг друга в коридорах."
    
    "Глухие и слепые ведут себя так, словно состоят во враждующих кланах, ни словом не обмениваясь друг с другом."

    "Даже Лилли с %(name_shizune)s можно считать непримиримыми соперницами, и это при том, что они достаточно толерантны."

    "Ну, по крайней мере, Миша частично маскирует настрой %(name_shizune)s. Кто знает, каковы её истинные мысли?"
    
    hi "Думаю, ты права. Когда я впервые приехал сюда, был откровенно шокирован Я без конца совершал ошибки. Точнее, считал, что совершаю. Например, когда говорил тебе «увидимся позже»."

    hi "Я не знал, считается это грубостью или нет, поэтому пытался вообще не думать об этом, не относиться к окружающим как-то по-особенному."

    hi "Так я и поступил. Убеждая себя, что Ханако, ты и все остальные абсолютно нормальные, я старался игнорировать очевидное."
    
    hi "Я разговаривал с Ханако так, словно она обычный человек, и так мы стали друзьями."
    
    hi "По крайней мере, такова, на мой взгляд, причина."

    show lilly basic_smileclosed at centersit
    with charachange

    li "Хисао, пусть я и считаю тебя наивным, я также уверена, что ты добрый. Это, возможно, одна из лучших твоих черт."

    hi "Хм, спасибо."
    
    show lilly basic_smile at centersit
    with charachange

    li "Скажи мне, ты свободен сегодня вечером?"

    hi "Если не считать домашнюю работу, то свободен как ветер."
    
    show lilly basic_cheerful at centersit
    with charachange

    li "В таком случае ты не хотел бы присоединиться к нашему с Ханако чаепитию?"

    hi "Э-э, если честно, у меня почти не осталось денег, поэтому не уверен, что получится куда-либо выбраться…"
    
    show lilly basic_smile at centersit
    with charachange

    li "О, я не подразумевала прогулку по городу. Мы хотели собраться здесь."

    hi "Ты знаешь, как вечером попасть в классы?"

    show lilly basic_giggle at centersit
    with charachange

    li "Нет, это запрещено правилами. Для посиделок мы с Ханако часто используем мою комнату. Пожалуйста, заходи после заката, не стесняйся."

    hi "Конечно, без проблем."

    hi "Какой номер твоей комнаты?"
    
    show lilly basic_smileclosed at centersit
    with charachange
    
    li "214, на втором этаже."

    hi "Хорошо, запомнил."
    
    show lilly basic_cheerful at center 
    with dissolvecharamove

    li "Что ж, вынуждена тебя покинуть. На меня всё-таки возложены обязанности старосты класса. До вечера, Хисао."

    hi "Ага, до встречи."
    
    hide lilly 
    with charaexit

    stop music fadeout 8.0

    "Что это было?"

    "Я только что был приглашён в комнату девушки после отбоя?"

    "Разве это разрешено?"

    "Здесь есть комендантский час, но я никогда не слышал о каких-либо правилах для посетителей общежитий."

    "Этого оказывается достаточно, чтобы мой сонный мозг враз взбодрился."

    "Добавьте к этому не слишком тёплый завтрак, и получится адское тонизирующее средство."

    "Теперь остаётся только пережить дневную рутину и уроки…"
    
    return
    
#---------------------------------    

label ru_H7:
    
    scene bg school_girlsdormhall 
    play sound sfx_time
    with shorttimeskipsilent
    
    with Pause(0.3)

    play sound sfx_doorknock2

    "Я робко стучусь в дверь, на которой написано «214», ещё раз проверяя время на наручных часах."

    li "Это ты, Хисао? Я сейчас подойду."

    "Услышав через дверь мелодичный голос Лилли, я успокаиваюсь."

    "Впервые меня пригласили в комнату девушки после наступления темноты."

    "Хоть я и понимаю, что это приглашение не имеет никакого скрытого намёка, меня не покидают мысли о возможностях."

    "Один парень. Две девушки. В комнате общежития. С чайным сервизом."

    "Последний из перечисленных фактов никак не уменьшает щекотливости первых трёх."

    "Не успеваю я продолжить эту мысль, как щёлкает замок и дверь со скрипом открывается."

    li "Пожалуйста, заходи."

    play sound sfx_dooropen

    window hide

    scene white 
    with dissolve

    with Pause(0.1)

    play music music_one fadein 10.0

    scene ev lilly_bedroom at Zoom((800,600),(40, 30, 720, 540),(0, 0, 800, 600),15.0, time_warp=_ease_time_warp, xalign=0.5, yalign=0.5)
    with Dissolve(4.0)

    window show

    "Дверь полностью открывается, и впервые перед моим взором предстаёт комната Лилли."

    "Мебель в ней выглядит старинной, на стенах практически отсутствуют какие-либо украшения. В центре стоит низкий стол."

    "Кажется, что у каждого предмета в этой комнате есть своё место."

    "Я заканчиваю рассматривать комнату, и мой взгляд возвращается обратно к девушкам."
    
    scene ev lilly_bedroom_large at Move((-130,-400),(-130,-600), 3.0, time_warp=acdc_warp, subpixel=True)
    with flash

    "Прямо передо мной стоит Лилли, всё ещё держась за дверь. Она одета в тёмно-синюю пижаму."
    
    show ev lilly_bedroom_large at Move((-130,-600),(-830,-300), 1.0, time_warp=_ease_time_warp, subpixel=True)
    with None
    
    with Pause(1.0)
    
    show ev lilly_bedroom_large at Move((-830,-300),(-830,0), 10.0, time_warp=acdc_warp, subpixel=True)
    with None

    "Позади неё я вижу сидящую за столиком Ханако, облачённую в консервативную светло-розовую ночную рубашку."

    "Руки Ханако зажаты между колен, плечи выдаются вперёд, голова опущена, будто она пытается в ней спрятаться."

    "И ей было бы несложно это сделать: она выглядит размера на два больше, чем нужно."

    "Складки фланелевой ткани делают Ханако похожей на ребёнка, который, играя, примеряет гардероб своих родителей."

    "Она поднимает взгляд, чтобы удостовериться, что это я. На её лице проскальзывает чуть заметная улыбка."
    
    show ev lilly_bedroom_large at Move((-830,0),(-130,-400), 1.0, time_warp=_ease_time_warp, subpixel=True)
    with None

    li "Что же, мы дар речи потеряли?"

    "Полагаю, совсем не обязательно обладать зрением, чтобы понять, что кто-то стоит и пялится."

    hi "Да нет, я… вы обе здорово выглядите."

    "Ханако краснеет и отворачивается, по-прежнему улыбаясь."

    li "Нет никакого смысла стоять в дверях, Хисао. Прошу, присаживайся."
    
    scene bg school_dormlilly 
    show lilly basic_smile_paj at twoleftsit
    show hanagown distant at tworightsit
    with locationchange

    play sound sfx_doorclose
    stop music fadeout 10.0

    "Я делаю шаг в комнату и закрываю за собой дверь."

    "Разворачиваясь, она натыкается на меня и хватается за мою руку."

    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Ой, прошу прощения. Для троих эта комнатка тесновата. Не проводишь меня к моему месту?"

    "Я медленно подхожу к столу и стараюсь сесть так, чтобы ничего не задеть."

    "Ничего не могу с собой поделать и, когда сажусь, мимолётно заглядываю в вырез пижамы Лилли."

    "Сейчас я понимаю, что быть слепым – это ужасно."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    li "Надеюсь, не откажешься от чашечки чая? Ханако, не могла бы ты налить?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "К… конечно. Хи… сао… ты…"
    
    show hanagown distant_blush at tworightsit
    with charachange

    ha "…ты не…"

    show hanagown worry_blush at tworightsit
    with charachange

    ha "…ты не хотел бы…"

    hi "Я не отказался бы от чашечки чая. Тебе помочь?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Н… нет, я справлюсь…"
    
    show hanagown smile at tworightsit
    with charachange

    ha "Спасибо…"

    play music music_dreamy fadein 2.0

    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "Ты что-то разнервничалась, Ханако, это на тебя не похоже. Обычно в этой комнате ты не такая… или смущаешься перед гостем?"
    
    show hanagown distant at tworightsit
    with charachange

    ha "Н…нет. Просто… просто…"

    hi "Устала сегодня?"
    
    show hanagown smile at tworightsit
    with charachange

    ha "А…ага."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    "Я сажусь за столик спиной к двери."

    "Слева от меня сидит Лилли в тёмно-синем, справа – Ханако, одетая в розовое."
    
    show teaset alpha at Position(xalign=0.5, yanchor=0.5, ypos=0.6)
    with None
    
    show teaset at Position(xalign=0.5, yanchor=0.5, ypos=0.5)
    with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

    "Стоящий на столе алый чайный сервиз с цветочками выглядит настолько же практичным, насколько и милым."

    "Контрастируя с простой, но довольно изящной мебелью, он смотрится довольно странно, что наводит на мысль, что сервиз выбирала, скорее всего, Ханако."

    "Наливая чай из заварочного чайника, Ханако случайно задевает чашку и та издаёт тонкий звон."
    
    show hanagown worry at tworightsit
    show lilly basic_displeased_paj at twoleftsit
    with None
    
    show teaset alpha at Position(xalign=0.5, yanchor=0.5, ypos=0.6)
    with Dissolvemove(0.5, time_warp=_ease_out_time_warp)
    
    hide teaset
    with None

    "Она судорожно вздыхает. Должно быть, она действительно очень нервничает, хотя этот звон – не то, из-за чего стоило бы беспокоиться."

    show hanagown worry_blush at tworightsit
    with charachange
    
    "Ханако бросает в дрожь из-за этой оплошности."

    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Переживать совершенно не из-за чего…"

    show hanagown normal at tworightsit
    with charachange

    "Слова Лилли, кажется, ободряют Ханако, и та, успокоившись, ловко разливает чай в две оставшиеся чашки."
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Вот, Хисао… Лилли."

    "Ханако аккуратно ставит чашки на блюдца перед Лилли и передо мной."

    "К такому обслуживанию и привыкнуть недолго."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Спасибо, Ханако."

    hi "Ага, спасибо."
    
    show hanagown smile at tworightsit
    with charachange

    ha "П-пожалуйста."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    "Лилли ищет свою чашку и, обнаружив её, деликатно отпивает."

    "Я делаю то же самое. Этот чай на вкус лучше того, что мы обычно пьём в школе."

    hi "Очень вкусно, будто вовсе даже и не чай пьём…"
    
    show lilly basic_ara_paj at twoleftsit
    show hanagown normal_blush at tworightsit
    with charachange

    li "Похоже, что ты сделала правильный выбор, Ханако."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    li "Ты молодец, это был смелый шаг с твоей стороны."

    hi "Ага… он… потрясный. Ни разу ещё подобного чая не пробовал…"

    show hanagown smile at tworightsit
    with charachange

    "Счастливая улыбка возвращается на лицо Ханако."

    "Даже несмотря на покалеченное лицо, её застенчивую улыбку нельзя назвать иначе как очаровательной."
    
    show hanagown distant_blush at tworightsit
    with charachange

    ha "Я рада, что вам понравилось…"

    "Ханако, наконец успокоившись, отпивает из своей чашки."

#--------------------
label ru_H7a:
    
    "Я вспоминаю о недавнем разговоре с Мишей."

    "Стоит ли переживать из-за поведения Ханако, или она просто застенчива?"

    "А ещё слова Лилли этим утром…"

    "Похоже, что их беспокойство искреннее, да и понимание ситуации у них лучше, чем у меня."

    "Но, в самом деле, чем я могу помочь?"

    "Я не пластический хирург и не могу изменить её внешность. И я не психолог, способный помочь ей стать более общительной."

    "Так что, чёрт возьми, Лилли и Миша хотят, чтобы я сделал?"

    "Это раздражает. Мы с Ханако быстро становимся друзьями по нашему обоюдному желанию, поэтому они хотят, чтобы я решил все её проблемы."

    "И я понятия не имею, что мне делать."

    "Никто не может вылечить ни моё сердце, ни глаза Лилли, ни Мишины…"

    "…что бы там у неё ни было."

    "Но всё же я не вижу ничего плохого в том, что мы с Ханако становимся хорошими друзьями. Теперь, когда она стала относиться ко мне теплее, мне нравится проводить с ней время."

#------------------------    

label ru_H7b:
    
    "Я почему-то внезапно вспоминаю о вопросе Лилли во время завтрака."

    "Почему я подружился с Ханако?"

    "Похоже, что Лилли действительно беспокоится о ней, но это не значит, что я в силах ей помочь."

    "Насколько я могу судить, физически ей шрамы не мешают, да и каждый, кого я встретил в этой школе, похоже, в некоторой степени научился справляться со своей инвалидностью."

    "У меня нет никаких скрытых мотивов, чтобы общаться с Ханако, просто у нас схожие интересы."

    "Разве этого мало?"



#-----------------

label ru_H7c:
    
    show lilly basic_smile_paj at twoleftsit
    with charachange
    
    li "Хисао, значит тебе понравилось?"

    "Лилли снова возвращает меня из раздумий в реальность, и я секунду вспоминаю, где нахожусь."

    "Я в комнате с двумя девушками в ночном белье. Мне бы радоваться."

    hi "Ага, тут так спокойно. Словно я вовсе не в школе. Часто вы так собираетесь?"
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Да, но в самой школе мы пьём чай гораздо чаще."

    li "Если постоянно так собираться, то из особого случая это превратится в рутину."

    hi "Понимаю, к чему ты клонишь, но я бы вот так сразу к подобным чаепитиям не привык."

    "Разве что лет за сорок."

    "Вскоре я допиваю свой чай."

    hi "Было восхитительно. Спасибо, Ханако, Лилли."
    
    show hanagown smile at tworightsit
    with charachange

    ha "Пожалуйста."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Да, ты всегда у нас желанный гость, Хисао."

    li "Радостно, что к нам присоединился ещё один человек."

    hi "В таком случае всегда, когда вам нужно будет составить компанию, я к вашим услугам."

    hi "Всегда."

    "Надеюсь, убедительно получилось."

    stop music fadeout 8.0
    show lilly basic_sleepy_paj at twoleftsit
    with charachange

    "Лилли зевает, безуспешно пытаясь прикрыться рукой."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Извините, я, похоже, немного устала."
    
    show hanagown distant at tworightsit
    with charachange

    ha "Думаю, мы все немного устали…"
    
    show lilly basic_ara_paj at twoleftsit
    with charachange

    li "Боже, боже, как мы сегодня проницательны, Ханако."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Нам действительно пора отправляться спать; завтра нас ждёт школа."

    hi "Ага… и я должен идти."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange
    
    li "Спасибо за визит, Хисао."
    
    show hanagown normal at tworightsit
    with charachange
        
    ha "С… спасибо. Ты придёшь ещё?"
           
    hi "Даже целой армии меня не остановить."

    show lilly basic_cheerful_paj at twoleftsit
    with charachange

    li "Впечатлена твоей решимостью, Хисао."

    hi "Ну ты меня поняла. Но мне и правда пора; уже поздно."

    ha "Да, почти ночь."

    "Я встаю и направляюсь к двери."
    
    show hanagown normal at tworight 
    with dissolvecharamove

    "Ханако осторожно встаёт вслед за мной."

    "Я останавливаюсь и поворачиваюсь к ней."

    hi "Пойдёшь со мной?"
    
    play music music_comedy fadein 0.5

    show hanagown normal_blush at tworight
    with charachange

    "Ханако мгновенно заливается краской."
    
    show hanagown distant_blush at tworight
    with charachange

    ha "Не… я… нет… эта комната… она не…"

    hi "Да всё хорошо, я же просто пошутил."
    
    show hanagown smile at tworight
    with charachange

    ha "А… ясно… спокойной ночи…"
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    li "Спокойной ночи, Ханако. Спокойной ночи, Хисао."

    hi "Доброй ночи всем."

    "И на этом наша вечеринка заканчивается."

    scene bg school_girlsdormhall 
    with locationchange

    "Невзирая на то, что я не знаю наверняка, что могу сделать для Ханако, мне не хочется подводить Лилли."

    "Стоит двери за нами закрыться, я поворачиваюсь к Ханако."
    
    show hanagown distant_blush 
    with charaenter

    hi "Ханако, знаешь, тебе не стоит так уж нервничать из-за меня."

    hi "Я к тому, что мы же друзья, верно?"

    show hanagown normal_blush 
    with charachange

    ha "П-правильно. Мы… друзья."

    hi "Если ты вдруг захочешь, например, пойти гулять – только дай мне знать. К тому же нас всё ещё ждёт тот шахматный матч-реванш, помнишь?"
    
    show hanagown distant 
    with charachange

    ha "Т-точно."
    
    show hanagown normal 
    with charachange

    ha "H-но я не думаю, что ты победишь…"

    hi "Чем труднее одержать победу, тем интереснее игра."
    
    show hanagown smile 
    with charachange

    "Кажется, что Ханако издаёт приглушённый смешок, или, может быть, это был просто лёгкий выдох."

    ha "С-спокойной ночи, Хисао…"
    
    show hanagown invis at tworight 
    with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

    hide hanako 
    with None

    stop music fadeout 5.0

    "С этими словами Ханако возвращается в свою комнату, расположенную по соседству с комнатой Лилли."

    "Я направляюсь к своему общежитию, но похоже, что даже простая ходьба полностью лишает меня сил."
    
    scene bg school_dormhisao 
    with locationskip

    "Едва я добираюсь до своей комнаты, как меня с головой накрывает волна усталости."
    
    play sound sfx_switch

    scene bg school_dormhisao_ni 
    with Dissolve(0.2)

    "Скинув обувь, я валюсь на кровать и, как только моя голова касается подушки, моментально засыпаю."
    
    scene black 
    with dissolve

    return


#-----------------
label ru_H8:
    
    scene bg school_dormhallway 
    with locationchange

    "Я открываю дверь своей комнаты, собираясь идти на уроки."
    
    show kenji invis at twoleft 
    with None

    show kenji neutral_close at center 
    with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

    ke "Выспался?"

    play music music_kenji fadein 0.5

    "Внезапное появление %(name_kenji)s заставляет меня подскочить, и я еле-еле избегаю столкновения с ним лбами."

    "Да, я в курсе, что он плохо видит, но мы ведь с ним уже знакомы. Так зачем он подходит ко мне настолько близко?"
    
    show kenji neutral 
    with charadistant

    hi "Ох. Ага. Спал как ребёнок."

    show kenji tsun
    with charachange

    ke "Чёрт, почему люди так говорят? Ты когда-нибудь слышал, как ребёнок спит?"

    ke "Они кричат. Всю ночь. Каждую ночь. Дети всегда плохо спят."

    "Ну вот и конец утренней безмятежности. Надо запомнить, что нельзя применять речевые обороты в разговоре с %(name_kenji)s."

    hi "Ладно, понимаю. Я выразился образно."

    show kenji neutral
    with charachange

    ke "Ага, ясно. A где ты был вчера вечером? Я хотел кое-что у тебя попросить, а ты как сквозь землю провалился."

    "У меня мелькает мысль, а не рассказать ли %(name_kenji)s правду о том, что я проводил время с Ханако и Лилли?"

    "К счастью, я тут же отметаю эту мысль."

    hi "Я отсутствовал. Патрулировал, осматривал окрестности. Ну, ты понимаешь. Разведка."

    show kenji happy
    with charachange

    ke "Молодец, чувак, молодец. Я знал, что ты из того типа людей, что планируют свои действия наперёд…"

    hi "Так чего ты хотел?"
    
    show kenji neutral 
    with charachange

    ke "Я хотел было прикупить жратвы, но обнаружил, что нужна мелочь."

    hi "Подожди, что? Я же давал тебе деньги на прошлой неделе, и ты, кстати, всё ещё мне их не вернул!"

    show kenji tsun
    with charachange

    ke "Тс, а я уже начал думать, что ты крутой чувак."

    "%(name_kenji)s, порывшись в кармане, выуживает оттуда свой бумажник."

    "Пока он отсчитывает четыреста иен, что мне должен, я замечаю по меньшей мере пару десятитысячных купюр."

    hi "Эй, какого чёрта? Почему ты занимаешь деньги у меня, когда у тебя и своих предостаточно?"

    "%(name_kenji)s слегка присвистывает, поняв, что попался."

    ke "Отвали, чувак. Плохая примета – тратить купюру на что-либо, что составляет меньше половины её номинала. Правило магната."

    ke "Вчерашний ужин мог мне обойтись в семь лет неудачи. Семь лет!"
    
    show kenji happy 
    with charachange

    ke "Тебе не кажется, что это уже достаточная причина кого-либо выручить?"

    ke "Я бы меньше пострадал, даже если бы просто украл те продукты."

    "Мой здравый смысл призывает что-нибудь ему ответить, но я всё же сдерживаюсь."

    "Отстаивание своей точки зрения с таким, как %(name_kenji)s, только приведёт к ещё более сложным дискуссиям."

    hi "Ага, ты, прав, наверное. Может быть, тебе стоит получше готовиться к подобным ситуациям?"
    
    show kenji neutral
    with charachange

    ke "Да, чувак, знаю. Но у меня столько дел, что трудно везде успеть. А ещё тебя вечно нет поблизости, поэтому я остаюсь сам по себе."

    ke "Мы с тобой по идее должны быть братьями по братству, помнишь?"

    hi "Ага, ага, помню. Глобальный заговор и всё такое. Я буду держать ухо востро."
    
    show kenji neutral_close 
    with charachange

    "%(name_kenji)s так близко наклоняется ко мне, что мне в нос бьёт резкий запах чеснока."
    
    show kenji tsun_close 
    with charachange

    ke "Да уж постарайся, чувак. Ты уже проводишь здесь гораздо меньше времени. С этого-то всё и начинается."

    ke "Они попытаются расколоть нас. Разделяй и властвуй, как сказал Сунь-Цзы."

    hi "Так точно. А сейчас я должен идти. У меня занятия. Ты со мной?"
    
    show kenji neutral_close 
    with charachange

    ke "Не, я устал. Для того чтобы убедиться, что ничего не случится после размена той банкноты, я не ложился всю ночь."

    hi "Гляжу, ты рационален как никогда."
    
    show kenji tsun_close 
    with charachange

    ke "Как скажешь. Спокойной ночи."

    stop music fadeout 3.0

    show kenji invis at twoleft 
    with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

    "%(name_kenji)s скрывается в своей комнате. Выходя в прихожую, за спиной я слышу бряцанье замков его двери."
    
    return
    #--------------
    
label ru_H9:
    
    scene bg school_dormhallway 
    with None

    scene bg school_scienceroom 
    show muto smile at center 
    with shorttimeskip

    play music music_daily fadein 4.0

    mu "…именно поэтому некоторые люди не могут свернуть язык трубочкой, а у некоторых второй палец ноги длиннее, чем большой."

    "Муто криво улыбается, очевидно гордясь своим объяснением действия рецессивных генов."

    "Однако, независимо от того, насколько его самого впечатляет наука, определяющая то, кем мы являемся, его лекция всё равно вводит класс в ступор."

    "Почему плохое объяснение может даже самую интересную информацию превратить в ничего не стоящую?"

    show muto irritated 
    with charachange

    "Я вижу, что Муто и сам прекрасно понимает, что ничто из сказанного им в течение последнего получаса не было воспринято окружающими."
    
    $ renpy.music.set_volume(0.29999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 4.0

    "Разговоры шёпотом начинают нарушать молчание, и со скоростью лавины уровень шума в классе начинает нарастать."
    
    show muto normal 
    with charachange

    "Сдавшись, Муто раздаёт несколько вопросов из учебника и начинает вытирать доску."

    hide muto 
    with charaexit

    "Конечно же, как только ученики начинают разговаривать и смеяться между собой, Ханако собирает свои вещи и покидает класс."

    "Испытываемый поначалу шок от того, что кто-то столь откровенно прогуливает уроки, начинает исчезать, но я не перестаю об этом задумываться."

    "Она уходит, потому что не желает, чтобы с ней разговаривали? Или же одна лишь мысль об окружающих людях нарушает её покой?"
    
    play sound sfx_normalbell
    $ renpy.music.set_volume(1.0, 4.0, channel='ambient')

    "Мои размышления прерывает колокольный звон, возвещающий начало большой перемены. Может быть, она просто воспользовалась возможностью, чтобы уйти пораньше?"

    "Обыденная ученическая суета, предваряющая каждый ланч, эхом разносится по комнате, и, пока Миша отвлеклась, я хватаю еду и выскакиваю за дверь."

    stop ambient fadeout 1.0

    scene bg school_miyagi 
    show lilly basic_smileclosed at centersit
    with locationskip
    
    "Лилли, одиноко сидящая в чайной комнате, выкладывает свой ланч."

    hi "Значит, Ханако ещё не пришла?"
    
    show lilly basic_smile at centersit
    with charachange

    li "О, Хисао, как дела? Я не встречала её с самого утра."

    "Точно, Ханако и Лилли живут по соседству."

    "Их-то утренний диалог, небось, куда адекватнее, чем потоки бреда %(name_kenji)s."

    hi "Странно. Она рано покинула класс, и я решил, что она направилась сюда."

    show lilly basic_displeased at centersit
    with charachange

    li "О, так она по-прежнему так поступает? Уходит до конца урока?"

    hi "А? Да, я замечал это за ней несколько раз."
    
    show lilly basic_sad at centersit
    with charachange

    stop music fadeout 7.0

    "Лилли слегка опускает голову с видом человека, привыкшего слышать плохие новости."

    li "Я была уверена, что она прекратит это делать, раз вы становитесь друзьями."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Наверное, каждому человеку нужно время."

    hi "Ну, я как раз задавался этим вопросом. Всё-таки почему она уходит?"

    show lilly basic_reminisce at centersit
    with charachange

    li "Я и сама до конца не уверена. Думаю, она не хочет попасть в ситуацию, в которой ей придётся отвечать на вопросы."

    "У меня всплывают воспоминания о первой встрече с ней. Тогда я подумал, что она выглядит как загнанная зверушка. Может быть, я был не так уж и далёк от истины."

    hi "Но, кажется, она прекрасно общается с тобой и со мной… вроде как…"
    
    show lilly basic_displeased at centersit
    with charachange

    li "Всё немного сложнее, чем кажется. Готова поспорить, первое, чем большинство интересуется, – это её шрамы и то, как она их получила."

    li "Она редко разговаривает об этом со мной, но я уверена, что она не желает вспоминать о том происшествии."
    
    show lilly basic_reminisce at centersit
    with charachange

    li "Оставить класс и убежать от расспросов – её защитная реакция, если можно так выразиться."
    
    hi "Хм… в таком случае почему она разговаривает со мной?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Ты сам вчера во время завтрака ответил на свой вопрос: ты пытаешься игнорировать её недостатки. Как только Ханако увидела, что ты не собираешься её расспрашивать, она тебе открылась."

    li "Мне кажется, завести друзей ей хочется сильнее прочего, но страх перед прошлым ей сильно мешает."

    hi "Хм, наверное, ты права. Может быть. Я не знаю. Ты знаешь её лучше меня, так что поверю тебе на слово."
    
    play music music_normal fadein 3.0

    show lilly basic_giggle at centersit
    with charachange

    li "Я бы не беспокоилась на этот счёт. Уверена, что совсем скоро ты узнаешь её так же хорошо, как и я."
    
    show lilly basic_smileclosed at centersit
    with charachange

    li "Я знаю её достаточно долго, чтобы понять – она чрезвычайно взволнована перспективой завести новую дружбу. А если учесть, сколько у вас общих интересов…"

    hi "Ну, вряд ли походы в библиотеку можно считать командным видом спорта, хотя читать на пару с кем-то всё же неплохо."
    
    show lilly basic_smile at centersit
    with charachange

    li "И я так думаю. Ханако всё-таки обычный человек. Ей тоже порой нужна компания."

    hi "Ясно. Вроде бы. Но, честно говоря, я вас обеих ещё не до конца понимаю."
    
    show lilly basic_smileclosed at centersit
    with charachange

    li "Это естественно, Хисао. Мы совсем мало знаем друг друга. Было бы неправильно ждать от тебя понимания, ведь мы и сами не всегда в состоянии понять тебя."

    show lilly basic_weaksmile at centersit
    with charachange
    
    li "Но становиться друзьями, узнавая друг друга всё больше, – это ли не удовольствие?"

    hi "Да, да, конечно."

    show lilly basic_cheerful at centersit
    with charachange

    li "Хисао, надеюсь, ты не будешь против, если я приступлю к еде?"

    hi "Конечно, кушай. Я тоже, наверное, перекушу. Мне ещё до начала урока надо сдать несколько книг в библиотеку, поэтому стоит поторопиться."

    show lilly basic_smileclosed at centersit
    with charachange
    
    li "Ханако, скорее всего, там же. Если встретишь её, передай, чтобы она вечером зашла ко мне. Я хотела бы с ней поговорить."

    hi "А ты не пойдёшь?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "К сожалению, у нас собрание старост классов, поэтому я уйду, как только доем."

    hi "Ладно. Если не встречу её в библиотеке, передам ей твою просьбу в классе. Уверен, после ланча она вернётся."

    "Мы молча приступаем к еде, и я размышляю над нашей беседой."

    "Я всегда думал, что Ханако была застенчива просто из-за того, что стеснялась своих шрамов."

    "Но сей взгляд на неё очень поверхностен."

    "Казалось бы, стоило только туману вокруг Лилли и Ханако начать рассеиваться, как вдруг я запутываюсь ещё сильнее, чем в самом начале знакомства с ними."

    "Торопясь на предстоящую встречу, Лилли быстро заканчивает трапезу. Я её понимаю."

    "%(name_shizune)s, скорее всего, тоже пойдёт на собрание. Сомневаюсь, что Лилли хочет дать ей ещё один повод для ссоры."
    
    show lilly basic_smile at centersit
    with charachange

    li "Мне пора откланяться. Завтра в то же время?"

    hi "В то же время, в том же месте. Мне тоже надо поспешить, чтобы не опоздать."
    
    show lilly cane_smileclosed at centersit
    with charachange

    show lilly cane_smileclosed at center 
    with charamove

    stop music fadeout 4.0

    "Лилли мягко улыбается, берёт свою трость и выходит в холл."

    return

    #----------
    
label ru_H10:

    scene bg school_hallway2 
    with locationchange

    "Мы покидаем комнату и, повернувшись друг к другу спиной, расходимся в противоположных направлениях. Я по какой-то причине переживаю, не вступит ли она в очередную словесную перепалку с %(name_shizune)s."

    "Как бы мне ни нравилась Лилли, %(name_shizune)s с Мишей сильно помогли мне адаптироваться к этой школе, хотя половина наших бесед состояла из откровенных попыток завербовать меня в Школьный совет."

    "Кроме того, я мало знаю каждую из них. А вдруг ранее они были лидерами некоего тайного общества, но их любовь друг к другу развела их в разные стороны…"

    "Да уж, мне пора прекращать читать беллетристику. Она ест мой мозг. Либо стоит держаться подальше от %(name_kenji)s и его пагубного влияния."

    "Грустно, что теперь я эти две вещи приравниваю друг к другу."

    scene bg school_library at right 
    with locationskip

    play music music_happiness fadein 2.0

    "Возвращая книги, я подталкиваю их по скату, и они с приятным стуком врезаются в дно тележки."

    play sound sfx_impact2

    show yuuko panic_up 
    with vpunch
 
    "Юко, однако, это не впечатляет в той же мере, что и меня."

    yu "Х-Хисао! Ты напугал меня!"

    hi "Извини, я думал, что ты к такому уже привыкла. Или тут все такие безграмотные, что никто не читает книг?"

    show yuuko worried_up 
    with charachange

    yu "Что? Нет, думаю, тут каждый умеет читать…"

    hi "Ага… не бери в голову."

    "Есть бои, которые не выиграть. Попытка объяснить шутку – один из них. Так утверждал мой отец."

    hi "Скажи, Юко, ты видела Ханако? Она рано ушла из класса, но я не нашёл её на обычном месте."
    
    show yuuko closedhappy_down 
    with charachange

    yu "Вроде я видела, как она прокралась сюда перед ланчем…"

    show yuuko panic_up
    with charachange
         
    yu "А! Я никому не должна была об этом говорить!"

    hi "Я же упомянул, что заметил, как она уходит. Расслабься…"

    show yuuko smile_down
    with charachange

    yu "А… конечно. Она, наверное, в задней части библиотеки."

    hi "Спасибо. Какие-нибудь новые книги поступили?"
    
    show yuuko worried_up 
    with charachange

    yu "Прости, нет. Дам знать, когда что-нибудь появится."

    hi "Хорошо."

    "Если и есть вещь, которую я знаю о библиотекарях наверняка, так это то, что они очень ценят людей, проявляющих искренний интерес к их работе."

    hide yuuko 
    with charaexit

    show bg school_library at Fullpan(10.0, dir='left') 
    with None

    "Я прохожу знакомый путь к уголку, где любит сидеть за книгой Ханако, по пути рассматривая названия на корешках."

    "Порой мне бывает трудно обнаружить на полках книгу, способную меня заинтересовать. Имя автора и название книги теряются в море похожих слов."

    "Поэтому иногда я перечитываю прочитанные ранее книги. Лучше поставить на фаворита, нежели на нового скакуна."

    "Стоит мне заметить книгу знакомого автора, но с незнакомым названием, как я тут же снимаю её с полки."

    "Всяко лучше, чем перечитывать конспекты."

    scene ev hana_library_read_std 
    with locationskip

    "Как и ожидалось, Ханако сидит на всё том же пуфе, читая «Дэнс, дэнс, дэнс»."

    hi "Привет, Ханако. Как ты?"

    "Я сдерживаю желание спросить, почему она так рано оставила класс. Если Лилли права в своих догадках, то этот вопрос может вызвать негативный эффект."

    "Лучше пока оставить эту тему. Иногда самый верный способ получить ответ от кого-то – не спрашивать."
    
    show ev hana_library_smile_std 
    with charachange

    ha "Хисао. Я в порядке."

    hi "Рад слышать. Как книга? Говорят, от неё крышу сносит."

    ha "И-интересная… вроде."
    
    ha "Я п-просто только начала, так что пока н-не знаю."

    hi "Не страшно. Скажи, как прочитаешь, – я, может, тоже её возьму."

    ha "К-конечно."

    "Остаётся ещё пятнадцать минут до конца большой перемены. Недостаточно, чтобы начать читать новую книгу, но слишком много, чтобы просто стоять и ничего не делать."
    
    show ev hana_library_read_std 
    with charachange

    "Ханако уже вернулась к чтению, так что дальше беседа у нас, думаю, не сложится."

    "Что ж, мне лучше устроиться поудобнее."

    play sound sfx_pillow

    "Расположившись на пуфе, я открываю книгу."

    "С самой первой строчки узнаётся неповторимый стиль автора. Читая абзац за абзацем, я начинаю помаленьку расслабляться."
    
    stop music fadeout 8.0

    "Но, как я ни стараюсь, всё равно не могу погрузиться в атмосферу книги."

    "Отчасти это происходит из-за нехватки времени, но наиболее отвлекающим фактором является Ханако."
    
    show ev hana_library_std 
    with charachange

    show ev hana_library_read_std 
    with charachange

    "Примерно раз в десять секунд она поглядывает на меня поверх своей книги, но стоит только нашим глазам встретиться, как она тут же приподнимает её, чтобы скрыть свой взгляд."

    "Полагаю, она всё-таки хочет о чём-то поговорить."
    
    scene bg school_library 
    with locationskip

    hi "В чём дело? Ты похожа на настороженного суриката."

    show hanako emb_blushing at centersit
    with charaenter

    ha "Н-нет, ничего."

    hi "Я же уже говорил, что твоё «ничего» на самом деле обычно значит «что-то всё же есть»."

    show hanako cover_worry at centersit
    with charachange

    "Ханако немного ёрзает на пуфе, надеясь, что, изменив своё положение, она подберёт нужные слова."
    
    show hanako emb_downsad at centersit
    with charachange

    ha "Со… со мной произошёл несчастный случай."

    hi "Несчастный случай? Сегодня? С тобой всё хорошо?"
    
    show hanako emb_sad at centersit
    with charachange

    "Ханако качает головой. Её волосы, разметавшиеся по плечам, кажутся аметистовыми на фоне светлых и тёмных участков кожи."
    
    show hanako emb_downsad at centersit
    with charachange

    ha "Н-нет. Когда я была м-маленькой."
    
    play music music_hanako
    
    "Осознание смысла её слов поражает меня словно гром среди ясного неба."
    #I want to change this metaphor, but the minute I thought 'truck' I also added 'berzerker' in my head. Fuck. -SC

    hi "Всё в порядке, Ханако, если не хочешь, можешь ничего не рассказывать…"

    "Она снова качает головой."
    
    show hanako emb_sad at centersit
    with charachange

    ha "Н-нет. Я хочу… я должна сказать тебе."
    
    scene ev hanako_crayon1
    show hanako_crayon2 behind ev
    with locationskip

    ha "Когда я была маленькой… я пережила пожар."

    ha "М-мой дом сгорел дотла, и я чуть… не сгорела вместе с ним."

    hide ev hanako_crayon1
    with charaexit

    ha "После этого… я осталась одна…"
    
    scene bg school_library 
    show hanako emb_downsad_close at centersit
    with locationskip

    "Глаза Ханако блестят в тусклом освещении библиотеки, и я протягиваю руку, чтобы прикоснуться к ней."

    hi "Всё хорошо, Ханако. Ты можешь не продолжать."
    
    show hanako emb_sad_close at centersit
    with charachange

    ha "Н-но… я должна…"

    hi "Почему? С чего ты так решила?"

    show hanako cover_distant_close at centersit
    with charachange

    ha "П-прошлой ночью Лилли р-рассказала мне о твоём сердце…"
    #Continuity check needed. -SC
    #Lilly finds out about Hisao's heart in A03b; I'm 90$% sure you can't get the H path without seeing A30b, but worth a check 
    show hanako cover_worry_close at centersit
    with charachange

    ha "И-и я… я подумала, что это неч-честно."

    hi "Нечестно?"
    
    show hanako emb_blushing_close at centersit
    with charachange

    ha "Ч-что я знаю о тебе всё, а-а ты обо мне не знаешь ничего…"

    "Я мягко сжимаю руку Ханако."

    hi "Не говори глупостей. Но да, у меня аритмия."

    "Я наклоняюсь ближе к Ханако."
    
    hi "Но чего я не сказал Лилли, так это то, что первый приступ у меня случился после того, как мне призналась в любви девушка."

    "Я слабо улыбаюсь, чтобы разрядить напряжённость ситуации."

    show hanako cover_worry_close at centersit
    with charachange

    ha "П-правда?"

    hi "Правда. От неё давным-давно не было никаких вестей, поэтому, думаю, между нами всё кончено."

    hi "Ну вот, теперь мы узнали чуточку больше друг о друге. Но тебе не обязательно заставлять себя говорить о том, о чём не хочется."

    "Мне становится не по себе, даже когда я просто вспоминаю о том дне. Я так и чувствую тот обжигающий лёгкие запах больничного дезинфицирующего средства."

    "Я предполагаю, что сейчас Ханако испытывает схожие с моими чувства."

    "Во время реабилитации я лишь однажды видел ожоговую палату. Я тогда просто заскучал и решил прогуляться."

    "Проходя онкологию, я подумал, что, наверное, смогу выдержать, но когда я увидел ожоговую палату, развернулся и пошёл обратно к себе в кровать."

    "Подумать только. Ханако провела месяцы в таком месте, чувствуя только запах сгоревшей кожи, сильного дезинфицирующего средства и стерилизованного воздуха."

    "Те больные, у которых были действительно тяжёлые ожоги, находились в изолированных барокамерах, в которые не могли попасть никакие инородные предметы. А это значит, что и книги там читать было нельзя."

    "Я сошёл бы с ума, если бы в больнице проводил время без книг."

    "И она сказала, что была одна… Неужели её родители погибли? Мне нужно будет спросить об этом Лилли. Иначе вполне могу ненароком ляпнуть что-нибудь не то."

    show hanako emb_timid_close at centersit
    with charachange
    
    ha "С-спасибо, Хисао."
    
    show hanako emb_downtimid_close at centersit
    with charachange
    
    ha "Я… Я почти никому не рассказывала об этом."

    hi "Честно говоря, я тоже почти никому ещё не говорил… о том, как всё произошло."

    show hanako cover_smile_close at centersit
    with charachange

    ha "Т-тогда я тоже н-никому не скажу."

    hi "Договорились."
    
    play sound sfx_warningbell

    "Я пожимаю и отпускаю руку Ханако. Из открытого окна доносится звук колокола, возвещающего об окончании перемены."

    hi "Ну что, возвращаемся в класс?"
    
    show hanako basic_bashful_close at centersit
    with charachange

    ha "К-конечно."

    $ renpy.music.set_volume(1.0, 0.0, channel='music')

    window hide

    return

#-------------

    
