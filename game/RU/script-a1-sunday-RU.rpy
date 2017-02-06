label ru_A38:
#Dawn of the Final Day

scene black
with None

scene bg school_dormhisao
with openeye


"Моё сегодняшнее пробуждение сопровождается лёгким головокружением. Уже почти полдень."

play music music_daily fadein 1.0

"Сегодня можно спать допоздна: воскресенье, уроков нет."

"Хотя это не простое воскресенье, а ещё и день фестиваля."

"Из окна видно, как люди в киоске с жареной собой накладывают лапшу страждущим по низкосортной пище."

"Я закидываю в рот пригоршню утренних лекарств и принимаюсь раздумывать, как же провести день."

"На следующей неделе ожидается несколько экзаменов, но я, в отличие от остальных, не считаю их угрозой, потому и не беспокоюсь."

"За неимением горящих обязательств по учёбе, я могу провести день фестиваля так, как хочу."

scene bg school_dormhallway
with locationchange

"Закончив утренние процедуры, я выхожу в коридор, намереваясь найти чего-нибудь поесть."

"Проходя мимо двери %(name_kenji)s, я вдруг решаю поинтересоваться, чем собирается заняться он."
   
"Все сегодня чем-то заняты, и мне любопытно, есть ли у него какие-либо планы."

"Хотя, с другой стороны, он вполне мог сделать из комнаты звуконепроницаемое убежище."

"Или нечто вроде крепости с табличкой «Женщинам не входить»."

"…и слово «Женщинам» перечёркнуто, а над ним накорябано: «Никому»."

stop music fadeout 0.5

play sound sfx_doorknock2

"Постучав в дверь, на которой, к счастью, никакой таблички нет, я снова слышу щёлканье по меньшей мере десятка замков. Дверь со скрипом открывается."

show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)

ke "Кто там?"

hi "«Кто там» надо спрашивать перед тем, как открываешь дверь."

play music music_kenji fadein 1.0

show kenji neutral at center
show bg school_dormhallway at bgright
with charamove

ke "А, это ты. Блин, ещё же рано."

hi "На самом деле не так уж и рано."

show kenji happy
with charaenter

ke "В чём дело, чувак?"

hi "Ни в чём, просто хотел спросить, чем будешь сегодня заниматься."

hi "Половина школы уже собралась снаружи."

show kenji rage
with charaenter

ke "Где – «снаружи»? Почему?"
   
hi "Что?"

ke "Что – «что»? Сегодня особый день? Почему они там? И кто это – «они»?"

show kenji tsun
with charachange

ke "Я их слышу. Шумят… только не говори, что… Началось вторжение?"

"Он вдруг принимает тревожный вид."
   
show kenji neutral
with charachange

ke "Какой сегодня день, чувак?"
   
hi "Да, наверное ты не видишь деревянные киоски на улице и то, как люди продают еду…"

ke "О чём ты, чёрт возьми? Я держу занавески задёрнутыми, чтобы помешать снайперам."

hi "О-ох, да фестиваль сегодня! Тебе ведь о нём известно?"

show kenji tsun
with charachange

ke "Твою мать, что, уже сегодня? Ах, чёрт. Во-от… чёрт. Чёрт бы их побрал."

ke "Не могу поверить, что я забыл, я ведь ещё не закончил свою крепость! Это плохо."

ke "Сегодня будет ужасный день… Хорошо, что ты меня предупредил, чувак. Паршивый будет день."

hi "Почему?"

show kenji neutral
with charachange

ke "О-о, чувак, они же будут повсюду. Люди. За окном. Общаться!"

"%(name_kenji)s нервно трёт виски. Ему как будто стало плохо."

show kenji tsun
with charachange

ke "Будет шумно, как в аду. Чёрт, а я собирался сегодня выйти, теперь всё пропало. Всё пропало."

ke "Это кошмар. Отстой. Лажа!"

ke "Блин, действительно лажа. Я теперь не могу никуда пойти. Некуда бежать."

"%(name_kenji)s, похоже, нервничает. Можно сказать, капитально съезжает с катушек."

show kenji neutral
with charachange

ke "Не могу поверить. Так вот что сегодня за день!"

ke "Чёрт, я даже не смог подготовиться."

show kenji tsun
with charachange

ke "Я даже не смог собраться, а теперь оно здесь и я бессилен. Тебе следовало сказать мне раньше, чувак. То есть я хотя бы теперь знаю, но… Я должен был узнать раньше! Только представь, чего бы я смог достичь…"

hi "Прости. Я думал, ты знаешь."

hi "Значит, я так полагаю, ты сегодня не будешь ничем занят?"
 
hi "Даже погода хорошая. Вчера было ветрено, так что я думал, что сегодня будет холодно. Но раз нет, то и смысла сидеть дома тоже нет. Да, тебе надо сходить посмотреть на фестиваль."

"%(name_kenji)s закрывает лицо руками и стонет."

ke "А-а, нет, нет! Я не могу. Они съедят меня заживо, я знаю."
    
"Наверное, это шутка, но он произносит её с невозмутимым лицом. Относительно невозмутимым."
    
show kenji happy
with charachange

ke "А что ты собираешься делать? Давай ко мне, поможешь строить крепость. Если будем работать вместе, то, может, ещё успеем."



label ru_A38a:
#If on Shizune's route

hi "Я проиграл спор, так что теперь должен побыть со Школьным советом."

"Забавно. Я ожидал, что цена проигрыша %(name_shizune)s в её дурацкой игре будет куда более жестокой. Это просто предлог, чтобы провести с ней время. В общем, думаю, она просто хочет, чтобы я повеселился."

"У неё могут быть добрые намерения, даже если она не может подойти и сказать о них прямо, и, думаю, она мне начинает нравиться всё больше."

hi "Я мог бы не пойти, но многое бы потерял. И к тому же я хочу пойти. То есть, понимаешь, сегодня захватывающий день. В любом случае будет что-то интересное."
    
show kenji tsun
with charachange

stop music fadeout 1.0

ke "Школьный совет? Что? Он ещё существует?"

ke "Там разве не всего два чувака?"

hi "Две девушки."

play music music_tension

show kenji rage
with charachange

ke "Правда? Симпатичные? Чёрт, нет, постой… симпатичные?"

ke "Нет! Это не важно! Я слышал, что президент у них сумасшедшая… никогда не говорит, а только отдаёт приказы через своих лакеев."

show kenji tsun
with charachange

ke "Чёрт, в любой школе они одинаковые… Какие-то бессердечные стервы. Стервы повсюду."

ke "Если там две девушки, они в большинстве – двое на одного. Опасная ситуация, чувак. Кто знает, что может случиться."

ke "Чёрт, в Совете всего две девушки, но сколько у них в руках власти!"

ke "Их надо остановить."

ke "Я прямо вижу, как они ищут пути осуществления своих феминистских планов. Я не могу доверять такому руководству."

ke "Это не круто. Совсем!"

show kenji rage
with charachange

ke "Чёрт. Дерьмо! Чёрт!"



label ru_A38b:
#If on Lilly or Hanako's route

hi "Не знаю. Я голодный, так что подумывал раздобыть еды и сходить на аттракционы."

hi "У твоего класса вроде крутой проект, и я тоже помогал, так что хочу посмотреть хотя бы его, и ещё поболтать с Лилли, наверное."

hi "Кстати, у тебя разве нет обязательств, связанных с проектом?"

show kenji rage
with charachange

ke "Ты с ума сошёл?"

ke "От этой слепой бабы ничего хорошего ждать не следует, печёнкой чую, чувак. Её присутствие – словно мрачная тень на пути моего великого взора."

ke "Чего и можно ожидать от слепых."

hi "Чё?"

hi "Кроме того, я думал, что ты тоже…"

show kenji neutral
with charachange

"Он поднимает руку, прерывая меня."

ke "Нет, у меня просто проблемы со зрением."

ke "Метафорически же я вижу дальше, чем кто бы то ни было до меня."

"В подтверждение своих слов %(name_kenji)s устремляет взор в мнимую даль, выставив вперёд подбородок, чтобы выглядеть более мужественно. Вообще-то всего в паре метров находится стена коридора, но это не меняет сути."

show kenji tsun
with charachange

ke "Я вижу будущее человечества, которое будет мрачным, если не подавить угрозу женщин."

ke "Они повсюду."



label ru_A38c:
#If on Rin's route

hi "Ну, я вступил в кружок рисования, так что, думаю, я пойду с ними."

show kenji rage
with charachange

ke "Что ты сделал?"

hi "Вступил в кружок рисования."

show kenji tsun
with charachange

ke "Чувак, это был неверный ход. Совсем неверный. Ты не представляешь, что за девушки в кружке рисования. Грустные, застенчивые милашки, которые вырвут твоё сердце и проглотят его."

"Я уже знаю одну из кружка рисования и не могу представить, чтобы Рин вдруг стала убийцей-психопатом."

hi "Звучит неправдоподобно."

ke "Не говори так. Не обманывай себя. Ты и понятия не имеешь, с чем столкнулся, чувак. Такие хуже всех."

show kenji neutral
with charachange

ke "Они тебя втянут своими выкрутасами, а потом, когда меньше всего ждёшь, – БАМ!"

hi "Что – «бам»?"

"Мой скептицизм немного сбивает %(name_kenji)s с толку, но он выглядит всё таким же безумным."

show kenji tsun
with charachange

ke "Это не важно."

ke "Будь осторожен, чувак, будь осторожен."



label ru_A38d:
#If on Emi's route

hi "Сомневаюсь… Мне хочется есть, но я заключил сделку, что попытаюсь беречь себя. Ну, быть здоровее, понимаешь."

hi "Не знаю, стоит держаться подальше от такояки или же пойти прямиком к ним."

show kenji tsun
with charachange

ke "Сделку? Звучит зловеще. А что ты получишь взамен?"

hi "Полагаю, что ничего. Это не такого рода сделка."

hi "Ты знаешь Эми из параллельного класса? Мы вроде как договорились присматривать друг за другом, и…"

show kenji rage
with charachange

ke "Йа-и-и-и-и-и-и-и-и!"

"От пронзительного визга и гримасы ужаса на лице %(name_kenji)s у меня кровь стынет в жилах. Как будто я сообщил католическому священнику, что продал душу дьяволу."

ke "С ней! Ты продал душу дьяволу и не получил ничего взамен?"

ke "Чувак, да что с тобой вообще такое?"

ke "Ты в курсе, с кем имеешь дело?"

ke "Она – угроза здоровью общества. Знаешь, сколько народу она каждый месяц отправляет в больницу, когда влетает в них на полной скорости?"

show kenji tsun
with charachange

ke "Она – одна из них! Ключевой игрок в этом глобальном заговоре, преследующий цель полностью покорить всё мужественное."

ke "Ушам своим не верю. Чувак, я доверял твоему здравомыслию. Я думал, мы братья."

ke "Тебе нужно отменить сделку, пока не поздно."

ke "И отказаться от похода на фестиваль… это же одна из их ловушек."



label ru_A38e:

"Он начинает теребить пальцами шарф, всё быстрее и быстрее, будто пытается добыть огонь, затем постепенно успокаивается, пока не проходит приступ паники."

stop music fadeout 2.0

show kenji neutral
with charachange

ke "Мне придётся найти надёжное укрытие, чтобы спрятаться. А потом завалюсь спать, чтобы этот жуткий день обошёл меня стороной."

ke "У меня для этого есть отличное средство. Пора готовиться."

show kenji tsun
with charachange

ke "Не ходи на фестиваль."

hi "Ладно."

show kenji neutral
with charachange

ke "Увидимся, чувак."

hide kenji
with charaexit

"Дверь с низким скрипом закрывается, и я даже не знаю, что и думать о словах %(name_kenji)s."




label ru_A44:

show bg school_dormhallway at bgright
with None

"Я задумываюсь, чем же мне хочется заняться с %(name_shizune)s и Мишей. Решив, что лучше быть во всеоружии, я заглядываю обратно в комнату, чтобы наполнить бумажник."
 
scene bg school_dormhisao
with locationchange

"Интересно, там есть игра, где надо поймать золотую рыбку бумажным сачком?"

"Поймать её гораздо легче, чем вам пытаются внушить. Но, с другой стороны, если бы я поймал рыбку, мне бы незачем было держать её у себя."

"Что мне делать с рыбой в своей тесной комнатке? Зажарить?"

"Я бы мог её отдать %(name_shizune)s или Мише, но это, наверное, было бы слишком."

"Действительно, проблема. Они обе милые, но не думаю, что у меня с кем-то из них есть шанс. Но, невзирая на это, я продолжаю обдумывать такой вариант. Я представляю себе, как они могли бы отреагировать, если бы я им сегодня что-нибудь подарил, например рыбку или куклу."

"Миша бы, наверное, как всегда засмеялась. А %(name_shizune)s бы выбила её у меня из рук."

"Может, это не такая уж и хорошая идея."

scene bg school_dormhallway
show shizu behind_blank_close
with locationchange

"Выйдя обратно в коридор, я чуть не врезаюсь в %(name_shizune)s."

hi "Привет, %(name_shizune)s. А где Миша?"

show shizu behind_frustrated_close
with locationchange

"Я пытаюсь жестикулировать, но, по сути, просто размахиваю руками. Надо будет попросить Мишу, чтобы чуть-чуть меня научила."

mi "Здесь!"

play music music_comedy

show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None

show misha hips_grin behind shizu at Slide(0.5,0.5,0.3,0.5,1.0)
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)

"Миша выскакивает из-за %(name_shizune)s, широко ухмыляясь."

mi "Мы просто пришли убедиться, что ты идёшь с нами на фестиваль."

show shizu basic_angry_close at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Не нарушай своё обещание~!"

hi "Обещание? Не припомню, чтобы я что-нибудь обещал."

show shizu cross_angry_close at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange

mi "Хватит пытаться увильнуть!"

show misha perky_sad at twoleft
with charachange

mi "Ну давай, %(name_hicchan)s, будет весело! Тебе в любом случае это необходимо, иначе станешь никчёмным!"

show misha perky_smile at twoleft
with charachange

mi "Ты ведь не хочешь стать одним из людей, сидящих целыми днями напролёт в комнате наедине с паранойей?"

"Я невольно бросаю взгляд через её плечо на дверь в комнату %(name_kenji)s."

"Я надеюсь, что он не слышит её слов, но, видимо, Миша как раз этого и добивается."

hi "Нет, конечно не хочу. Я просто дурачился и всё равно уже собирался уходить. Вам было не обязательно за мной заходить."

show misha cross_laugh at twoleft
with charachange

mi "Правда? А-ха-ха-ха! %(name_sicchan)s волновалась, что ты попытаешься как-нибудь отмазаться!"

show misha hips_grin at twoleft
with charachange

mi "Ты нам нужен, %(name_hicchan)s~!"

hi "Чего?"

"Сердце, кажется, ёкнуло."

show misha perky_smile at twoleft
with charachange

mi "У меня плоховато с прицелом, чтобы сбивать кукол с подставок… а %(name_sicchan)s отказывается бросаться вещами."

hi "Вот оно что."

"%(name_shizune)s глядит на меня, мгновенно замечая моё разочарование. Она поправляет очки."

show shizu adjust_happy_close at tworight
with charachange

shi "…"

mi "О чём, по-твоему, мы говорили? Я вообще ничем не хочу бросаться."

show misha perky_confused at twoleft
with charachange

mi "Почему, %(name_sicchan)s? Как-то странно…"

show misha perky_smile at twoleft
with charachange

mi "Ну, как бы то ни было, %(name_hicchan)s, тебе ведь приходилось кидать мячи, правда~, правда~? Так что! Тебе придётся пойти с нами!"

"Меня поражает их логика. Непонятно, шутят они или нет."

hi "Хех, если б я не знал, что вы шутите, то обиделся бы."

hi "Вы ведь шутите, да?"

show shizu behind_frown_close at tworight
with charachange

shi "…"

mi "Так и есть, %(name_hicchan)s~! Всё так и есть, так и есть, так и есть!"

hi "Тогда я спокоен."

show shizu basic_normal2_close at tworight
with charachange

shi "…"

show misha hips_smile_close at closeleft
with characlose

mi "Давай, пойдём! За окнами уже группа глухих музыкантов настраивает инструменты."

"Миша хватает меня за руку и тянет из дверного проёма, но мне вполне очевидно, что она не особо старается."

hide shizu #stupid renpy
with None

show shizu basic_normal2_close behind misha at tworight
with None

show shizu adjust_blush_close behind misha at tworight
with charachange

"%(name_shizune)s смотрит на нас, немного покраснев и нетерпеливо теребя пальцами дужку очков."

"Я не привык к таким, казалось бы, обыденным прикосновениям, но ничего против не имею. Как я могу возражать?"

stop music fadeout 1.0

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

play music music_normal

"На улице ещё светло, но солнце уже собирается скрыться в кронах деревьев."

"Похоже, что здесь собралась половина школы, я даже замечаю в стороне нескольких преподавателей, попивающих пунш."

"К ужасу работающих в киоске девушек, они уже почти опустошили целый чан."

"Предсказатели судьбы стоят и болтают с друзьями, в то время как остальные уже начали метать гороскопами в каждого из прохожих."

"Такая тактика кажется мне чересчур агрессивной, но она хотя бы показывает, что они вжились в роль. Необычно такое наблюдать, и я не знаю, смогу ли привыкнуть."

show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

show misha sign_smile at twoleft

mi "Надо бы чего-нибудь поесть. Ты голодный, %(name_hicchan)s?"

"Кстати сказать, я не ел целый день."

hi "Жареной лапши мне не очень хочется."

show misha hips_grin at twoleft
with charachange

mi "Ничего страшного, тут много чего другого жареного!"

hi "А какая-нибудь нежареная пища есть?"

show shizu adjust_smug at tworight
with charachange

shi "…"

mi "Конфеты. Вредная пища – самое главное в празднике!"

show misha cross_laugh at twoleft
with charachange

mi "Ва-ха-ха-ха-ха!"

show shizu behind_smile at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Давай я – то есть %(name_sicchan)s – угощу тебя чем-нибудь одним~!"

mi "Одним?"

show shizu adjust_smug at tworight
with charachange

shi "…!"

show misha sign_smile at twoleft
with charachange

mi "Только одним~! Чтобы ты набрался сил для метания!"

show misha perky_smile at twoleft
with charachange

mi "Только похоже, что ещё не все киоски открылись, так что тебе может не достаться желаемого."

"Я оглядываюсь, поражённый количеством киосков. Невероятно, фестиваль в «Ямаку» шире по своему размаху, чем в иных городах."

"Несмотря на сказанное Мишей, половина школы уже празднует."

"Воздух наполнен возбуждённой болтовнёй по меньшей мере половины всех учеников интерната."

"От аромата готовящейся еды мой голод с каждой секундой только усиливается."

show shizu behind_frustrated at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "Ну же, %(name_hicchan)s, еду скоро всю расхватают! Если хочешь такояки, надо идти прямо сейчас!"

show misha hips_grin at twoleft
with charachange

mi "Я бы поела такояки~! Давайте поедим!"

hi "Хорошо, я бы не отказался – сто лет их не ел."

hide shizu
with charaexit

hide misha
with charaexit

"%(name_shizune)s срывается с места прежде, чем Миша успевает ей перевести, и энергично направляется к лавке с такояки, а Миша пытается угнаться за ней."

scene bg school_stalls1
with locationchange

"Миша смеётся, подскочив к %(name_shizune)s, которая заказывает три порции такояки, показывая три пальца."

"Я раньше не обращал внимания, но теперь кажется странным, что %(name_shizune)s, будучи человеком, одержимым чаем высшего сорта, любит также и фастфуд."

"Я принимаю от неё тарелку с такояки, раздумывая, стоит ли начинать есть. Блюдо выглядит очень горячим."

"От него поднимается пар, а на поверхности шкворчит масло."

show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"%(name_shizune)s с Мишей смотрят на меня так, будто ждут, что я начну есть первым."

"Я не могу уступить, поэтому насаживаю один кусочек на пластиковую вилочку, небрежно торчащую из угла тарелки."

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange

"Однако не успеваю я отправить его в рот, как %(name_shizune)s с Мишей страстно набрасываются на еду. %(name_shizune)s кусает такояки быстро, но аккуратно, а Миша, словно ребёнок, подолгу смакует каждый кусочек."

"Думаю, что они, как и все прочие здешние ученики, в конце концов просто обычные дети."

"Это здорово. Давненько я не гулял с кем-то вот так запросто, наслаждаясь компанией."

"Даже до того, как я попал сюда, у меня был очень занятой год. Настолько занятой, что я до сих пор даже не осознавал, чего лишался."

stop music fadeout 3.0

"А здесь я чувствую себя безмятежно."

"Очень умиротворяющая атмосфера. Я и не думал, что подобные фестивали до сих пор проводятся."

show misha perky_confused at twoleft
with charachange

play music music_comedy

mi "А? %(name_hicchan)s, ты что, не будешь есть?"

hi "Буду, буду."

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Надеюсь, тебя не отпугнуло то, что они горячие?"

hi "Нет, не в этом дело."

"Мне уже начинают нравиться их поддразнивания."

scene bg school_stalls1_ss
with shorttimeskip

"Я поспешно принимаюсь есть, пока еда не остыла, размышляя о том, какое великолепное зрелище создают тускло подсвеченные бумажные фонарики, сияющие тёплым светом на фоне заката."

show shizu behind_smile_close_ss
with charaenter

"Не успеваю я доесть свои такояки, как %(name_shizune)s встаёт передо мной, выпрямившись и строго сложив руки за спиной."

"Заметно, что она пытается быть как можно серьёзнее, но с такой улыбкой на лице даже ей не спрятать своё хорошее настроение."

$ renpy.music.set_volume(0.6,2.0, "ambient")

show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove

show misha cross_laugh_ss at twoleft
with charaenter

mi "А-ха-ха-ха~! Пойдём, %(name_hicchan)s, поиграем в какие-нибудь игры!"

hi "Разве у них всё уже готово?"

show shizu adjust_happy_close_ss at tworight
with charachange

shi "…"

show misha cross_grin_ss at twoleft
with charachange

mi "Нет, но не важно, не важно~! Пойдём, %(name_hicchan)s, пока толпа не собралась!"

show misha hips_grin_close_ss at closeleft
with characlose

"Миша кладёт руку мне на плечо и заливается смехом."

show misha perky_smile_close_ss at closeleft
with characlose

mi "Пойдём! Пойдём! В этом году призы просто здоровские, правда-правда~! Тебе разве не хочется выиграть призы для таких красоток, как мы?"

"Миша напускает на себя «милый» вид, и, надо сказать, получается эффектно. Я смотрю на %(name_shizune)s, ожидая, что она сделает то же самое, но она только глядит на меня как на сумасшедшего."

show shizu cross_wut_close_ss at closeright
with charachange

shi "…"

show misha hips_grin_close_ss at closeleft
with characlose

mi "Миша, прекрати!"

show misha perky_confused_close_ss at closeleft
with charachange

mi "Стоп… Миша – это же я…"

show shizu basic_normal2_close_ss at closeright
with charachange

shi "…"

show misha sign_smile_close_ss at closeleft
with charachange

mi "%(name_hicchan)s, торопись, ты уже тысячу лет держишь этот несчастный кусочек такояки!"

show misha cross_laugh_close_ss at closeleft
with charachange

mi "Ха-ха-ха-ха-ха!"

show misha cross_smile_close_ss at closeleft
with charachange

hi "Я люблю смаковать всё, что ем. Даже такое."

show shizu basic_sparkle_close_ss at closeright
with charachange

show shizu adjust_smug_close_ss at closeright
with charachange

"Внезапно %(name_shizune)s выхватывает у меня из руки вилку и с улыбкой отправляет такояки себе в рот."

"Всё происходит так быстро, что я оказываюсь не в состоянии этому помешать."

show misha cross_laugh_close_ss at closeleft
show shizu behind_smile_close_ss at closeright
with charachange

"Не успеваю я осознать, что же произошло, как Миша взрывается хохотом, а %(name_shizune)s так улыбается, что кажется, будто вот-вот к ней присоединится."

show shizu adjust_happy_close_ss at closeright
with charachange

shi "…!"

mi "Вот дело и решено~! Ва-ха-ха! Ха-ха-ха-ха!"

"%(name_shizune)s хватает меня за правую руку, а Миша – за левую."

show shizu behind_smile_close_ss at closeright
with charachange

shi "…"

show misha hips_grin_close_ss at closeleft
with charachange

mi "Ты идёшь с нами! Сегодня нас ждёт много интересного, веселись!"

show misha cross_laugh_close_ss at closeleft
with charachange

mi "Ха-ха-ха-ха~!"

stop music fadeout 5.0

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip

"Пробираясь сквозь уже довольно внушительную толпу, мы играем во все игры подряд: «Брось кольцо», «Замочи крота» и в такие, о которых я даже не слышал."

"Выигрываем мы редко, но нам всё равно весело."

hi "Эй, а тут есть «Поймай золотую рыбку»?"

play music music_dreamy fadein 0.3

show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter

shi "…"

mi "Конечно! Я не знала, что тебе нравится эта игра, %(name_hicchan)s!"

hi "Просто я всегда хотел попробовать. Она вроде не сложная."

show misha hips_grin_ss at twoleft
with charachange

mi "Ты в этом уверен, %(name_hicchan)s~?"

show misha cross_laugh_ss at twoleft
with charachange

mi "Ва-ха-ха-ха~! Ладно, ладно! Посмотрим! Их киоск где-то тут!"

show shizu basic_normal_ss at tworight
with charachange

shi "…"

show misha perky_smile_ss at twoleft
with charachange

mi "Только где ты собираешься держать рыбку? У тебя есть аквариум?"

hi "Ну… нет."

show misha hips_grin_ss at twoleft
with charachange

mi "Может, он её съест?!"

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

show misha cross_laugh_ss at twoleft
with charachange

mi "Ха-ха-ха-ха-ха-ха! А-ха-ха-ха-ха-ха-ха!"

show misha cross_grin_ss at twoleft
with charachange

mi "Ладно, %(name_hicchan)s, если нам удастся поймать рыбку, мы отдадим её тебе!"

hi "Что, правда? Снова посостязаемся? Ну что ж…"

show shizu basic_happy_ss at tworight
with charachange

"%(name_shizune)s, пытаясь скрыть горящий в глазах энтузиазм, оживлённо подталкивает меня к киоску."

scene bg school_stalls2_ss at bgright
with locationchange

"К счастью, им не удаётся поймать ни одной рыбки, но и мне везёт не больше."

stop music fadeout 5.0

$ renpy.music.set_volume(0.6,2.0, "ambient")

show bg school_stalls2_ss at bgleft
with charamove

"У меня не получается сдержать смех, когда они сразу после этого начинают тащить меня к особенно крупному цветастому киоску, в строительстве которого я принимал активное участие."

"Я его помню: с ним было особенно много возни."

"Продавец, парень ничем не примечательной наружности с выкрашенными в каштановый цвет волосами, выпрямляется, увидев, что мы подходим. Я замечаю две вещи:"

"Во-первых, это киоск с игрой по сбиванию кеглей, выстроенных пирамидой."

"Четыре шарика за пятьдесят иен, весьма неплохо."

"Во-вторых, тут есть инструкция к игре, напечатанная шрифтом Брайля. Мне хочется что-нибудь сказать по этому поводу, и я поворачиваюсь к %(name_shizune)s с Мишей."

"Но они либо не замечают её, либо для них она не кажется странной."

"Продавец" "Привет! Здорово, что ты пришла, %(name_hakamichi)s! Спасибо большое за помощь с этим киоском. Веселитесь?"

"%(name_shizune)s бросает взгляд на Мишу, которая молниеносно всё ей переводит, и лучезарно улыбается продавцу."

play music music_comedy

show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "Ха-ха~! Это ерунда, сущие пустяки~! Да, всё здорово~! Думаю, это лучший фестиваль из тех, что мы проводили!"

show misha perky_smile_ss at twoleft
with charachange

mi "%(name_shiraki)s, мы хотели бы поиграть, ведь можно?"

show misha hips_grin_ss at twoleft
with charachange

mi "Разумеется~, было бы чудесно, если бы ты просто отдал приз милым трудолюбивым работницам Школьного совета за все часы, которыми они пожертвовали, чтобы устроить весь этот праздник!"

name_shiraki "Ха-ха-ха, ха-ха… Нет."

"А %(name_shiraki)s крут."

hi "Эй, я пролил немало пота, строя этот киоск, и потратил два часа своей жизни. Думаю, я заслуживаю хотя бы один бесплатный раунд."

show misha hips_frown_ss at twoleft
with charachange

mi "И я!"

show shizu basic_angry_ss at tworight
with charachange

shi "…"

mi "Я тоже!"

show misha perky_confused_ss at twoleft
with charachange

mi "Ой…"

"Немного поколебавшись, он всё-таки сдаётся и, пожав плечами, вручает нам всем по четыре шарика."

show misha hips_grin_ss at twoleft
show shizu behind_blank_ss at tworight
with charachange

"Не проходит и секунды, как %(name_shizune)s и Миша отдают свои шарики мне."

hi "Чего это вы?"

hi "Только не говорите, что, наделав столько шума, вы даже играть не собираетесь!"

hi "И это после того, как мы все вместе накинулись на %(name_shiraki)s!"

name_shiraki "Вот именно…"

show shizu basic_frown_ss at tworight
with charachange

shi "…"

show misha sign_smile_ss at twoleft
with charachange

mi "А ты, пожалуйста, не вмешивайся~!"

show shizu adjust_happy_ss at tworight
with charachange

"%(name_shizune)s поворачивается ко мне и пренебрежительно машет рукой. Миша разрывается между переводом и утешением продавца."

show shizu adjust_smug_ss at tworight
with charachange

shi "…!"

show misha hips_grin_ss at twoleft
with charachange

mi "А-ха-ха-ха! %(name_hicchan)s, где твоё рыцарство? Кроме того, я – то есть %(name_sicchan)s – придерживаюсь политики небросания шаров!"

show misha hips_smile_ss at twoleft
with charachange

mi "Ой, прости, %(name_hicchan)s. У меня тоже плохо с бросанием шариков в цель. Однако у тебя наверняка это хорошо получается, правда, правда? Для тебя это не проблема!"

stop music fadeout 3.0

"Выглядит довольно просто. Кегли не так уж далеко, единственное препятствие в том, что шарики полые, пластиковые, да ещё и с дырками."

"Я бросаю один в кеглю, и он бесцеремонно отскакивает."

show shizu behind_blank_ss at tworight
show misha perky_confused_ss at twoleft
with charachange

hi "Какого чёрта?"

name_shiraki "Да, это не так просто, как кажется. Кегли наполнены водой. Секрет фирмы."

show misha hips_frown_ss at twoleft
with charachange

mi "Это не очень-то честно!"

hi "Потому-то четыре шарика всего за пятьдесят иен. Как хитро!"

show shizu basic_angry_ss at tworight
with charachange

shi "…"

show misha hips_smile_ss at twoleft
with charachange

mi "Ну давай, %(name_hicchan)s, ты сможешь их сбить! У тебя ещё одиннадцать попыток, давай!"

hi "Может, сама попробуешь?"

hi "%(name_shizune)s? Хочешь попробовать?"

show shizu behind_blank_ss at tworight
with charachange

"%(name_shizune)s выразительно качает головой из стороны в сторону."

"Я смеюсь: это выглядит довольно забавно."

play music music_soothing

"Собравшись, я бросаю ещё один шарик в пирамиду кеглей и заставляю её немного покачнуться."

show shizu basic_normal_ss at tworight
show misha perky_smile_ss at twoleft
with charachange

"%(name_shizune)s с Мишей бросают жадные взгляды в сторону игрушечной кошки."

"В общем-то, не так уж они и отличаются друг от друга."

"Порой я задумываюсь, не был бы голос %(name_shizune)s похож на Мишин, если бы она могла говорить."

"Нет, ну не настолько они похожи."

"Я бросаю ещё один шарик, поняв, что на самом деле это довольно просто. Если я смогу одновременно сбить две нижние кегли, то легко выиграю."

"Уже начинает собираться небольшая толпа, и давление на меня усиливается. Ещё девять бросков."

play sound sfx_impact2

"Я замахиваюсь, словно бейсбольный питчер, швыряю шарик изо всех сил, и кегли сыпятся вниз."

show shizu behind_blank_ss at tworight
show misha cross_laugh_ss at twoleft
with charachange

"Я торжественно требую приз в виде плюшевой кошки, а Миша заливается хохотом, будто это она её выиграла."

"%(name_shizune)s смотрит на меня своим обычным безэмоциональным взглядом. Ясно, что она тоже хочет эту игрушку."

show shizu basic_normal2_ss at tworight
with charachange

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "%(name_hicchan)s, поздравляю~! Что ты собираешься делать с этой куклой?"

"Правильного ответа не существует. Я должен ступать осторожно."

hi "Я… не знаю."

mi "Ну-у-у-у-у-у~ Если тебе не нужна, я заберу…"

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

show misha cross_grin_ss at twoleft
with charachange

mi "Если ты только не хочешь оставить её себе, %(name_hicchan)s. Не знала, что тебе нравятся куклы. Тонко."

hi "Не хочу. Мне она ни к чему."

show misha cross_smile_ss at twoleft
with charachange

mi "Можно тогда мне?"

show shizu behind_blank_ss at tworight
with charachange

shi "…"

"Их глаза сверлят мою душу."

"Такое решение я принимать не хочу. Я поворачиваюсь к киоску."

hi "У вас есть ещё одна такая же?"

name_shiraki "Да, как раз одна."

hi "Хорошо, ставьте всё на место, попробую ещё раз."

"У меня всё ещё остаётся восемь шаров."

"Как только кегли снова устанавливают, я бросаю изо всех сил, но промахиваюсь."

show misha hips_grin_ss at twoleft
with charachange

mi "Ха-ха-ха! Пытаешься выиграть ещё одну? Хочешь выкрутиться по-лёгкому, %(name_hicchan)s?"

hi "Если это так легко, можешь сама попробовать."

mi "Нет, спасибочки~!"

show misha perky_smile_ss at twoleft
with charachange

mi "Скажи, %(name_hicchan)s, а ты можешь положить игрушку, хотя бы пока кидаешь шары?"

hi "Нет."

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

mi "Осталась всего одна, и лучше бы тебе попасть! Облажаешься – убью~!"

show shizu behind_smile_ss at tworight
with charachange

shi "…"

mi "Однако же какой хитрый способ, чтобы не отдавать мне игрушку! И говоря «я», я имею в виду себя~!"

show shizu adjust_happy_ss at tworight
with charachange

shi "…!"

show misha cross_laugh_ss at twoleft
with charachange

mi "А-ха-ха-ха-ха~! Шутка!"

"Понятно, что Миша никого не хотела обидеть, и %(name_shizune)s шутка вроде бы нравится, но затем ей становится немного грустно."

"Я решаю вручить игрушку ей, хотя бы на то время, пока пытаюсь выиграть ещё одну. Целиться с огромной кошкой в руках трудновато."

show shizu behind_smile_ss at tworight
show misha perky_smile_ss at twoleft
with charachange

shi "…"

mi "Спасибо, %(name_hicchan)s. %(name_sicchan)s, похоже, счастлива~! Но ты ведь выиграешь и для меня тоже?"

hi "А я разве не этим занимаюсь?"

stop music fadeout 5.0

show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None

hide shizu
hide misha
with Dissolve(1.0)

"Я снова делаю бросок, но в этот раз совсем мажу."

"В руке чувствуется тяжесть, как будто кровь туда не поступает."

"Я ругаю себя, думая, что устать от такой ерунды – просто жалкое зрелище."

"И тут я понимаю, что это, вероятно, из-за сердца. Если так, то я не знаю, что и думать."

"Удручающе осознавать, что такой малости для меня достаточно, чтобы осознать собственную смертность."

"Наверное, я никогда не смогу перестать об этом вспоминать."

"Даже сегодня, в день, который я надеялся провести с удовольствием, в этот чудесный вечер, я не могу отделаться от причины моего присутствия в этой школе."

"Это место не сравнится ни с одним другим, я нигде ещё не чувствовал себя так умиротворённо."

"Но теперь сложно не думать о том, о чём думать совсем не хочется:"

play music music_sadness fadein 0.3

"Возможно, меня просто отправили сюда умирать."

"Последние несколько дней были лучшими в моей жизни. Впервые после долгого времени я почувствовал себя по-настоящему живым."

"Но в конечном счёте каждый раз, когда я взбираюсь на чересчур длинную лестницу или слишком сильно швыряю шарик, мне приходится вспоминать о том, что я могу умереть в любой момент."

"И это всегда будет меня ограничивать."

"Я ощущаю тоску и злобу. Всё-таки мне дорога моя жизнь, и я наслаждаюсь ею, а теперь она как никогда бренна."

"Интересно, что же меня в конце концов добьёт? Если я настолько слаб и жалок, это может быть что угодно: неудачное падение, удар в грудь или шальной бейсбольный мяч."

"Несмотря на потерю воли, я продолжаю играть в эту игру."

play sound sfx_heartfast

show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"Внезапно я чувствую укол в груди. Боль сразу же улетучивается, но заставляет меня чуть пошатнуться."

show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)

"%(name_shizune)s в испуге отпрыгивает, а потом подходит поближе, не отрывая беспокойного взгляда. Миша кладёт руку мне на плечо."

mi "Эй, %(name_hicchan)s, ты в порядке?"

hi "Да, в порядке. Не очень хорошо себя чувствую, наверное заболел. Думаю, я не смогу продолжить."

show misha hips_frown_close_ss at twoleft
with charachange

"Миша хмурится."

mi "Не перенапрягайся. Если ты настолько болен, то так только заболеешь ещё больше."

show shizu basic_normal2_close_ss at tworight
with charachange

shi "…"

show misha hips_smile_close_ss at twoleft
with charachange

mi "Смотри, фестиваль только начался, а мы постоянно играли в игры. Если устал, то давай отдохнём."

show misha sign_smile_close_ss at twoleft
with charachange

mi "Хорошая идея, %(name_sicchan)s, я тоже немного устала! Все мы малость выбились из сил, бегая по школе, %(name_hicchan)s!"

stop music fadeout 10.0

"Я киваю. Они вроде бы не заметили ничего необычного. Вот и отлично."


$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip

"Мы пробираемся через море народа, а Миша указывает на лица каждого из своих знакомых. %(name_shizune)s держит в руках тряпичную кошку, рассеянно обнимая её. Похоже, им весело."

"И вдруг на меня нападают угрызения совести."

"Из-за моего слабого здоровья нам пришлось всё прекратить."

play music music_tranquil

show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter

shi "…"

mi "%(name_hicchan)s, мы немного голодны, а ты?"

hi "Не то чтобы сильно, но чего-нибудь съел бы."

show misha hips_smile_ni at twoleft
with charachange

mi "Этого вполне достаточно, %(name_hicchan)s~! Чего бы нам купить?"

hi "Мне не важно, что угодно."

show shizu adjust_happy_ni at tworight
with charachange

shi "…"

show misha hips_grin_ni at twoleft
with charachange

mi "А! Тогда как насчёт бутербродов? И ещё что-нибудь попить! Миша всё принесёт!"

show misha perky_confused_ni at twoleft
with charachange

mi "Что?.."

show shizu behind_smile_ni at tworight
with charachange

"%(name_shizune)s с улыбкой смотрит на меня. Я понимаю, что она пытается развеселить меня шуткой, и ей это удаётся – я смеюсь."

show shizu adjust_happy_ni at tworight
with charachange

shi "…"

show misha perky_smile_ni at twoleft
with charachange

mi "%(name_hicchan)s, народу уже слишком много, поэтому здесь мы поесть, пожалуй, не сможем. И шумно к тому же."

show misha sign_smile_ni at twoleft
with charachange

mi "Может, лучше подняться на крышу и поесть там?"

hi "Я согласен. Наверняка вид оттуда замечательный, да и ветерок, наверное."

show misha hips_grin_ni at twoleft
with charachange

mi "Значит, договорились! Думаю, мне теперь надо сходить за едой и напитками… Тогда до встречи~!"

stop music fadeout 4.0

hide misha
with charaexit

"Миша неловко машет рукой и убегает."

"Раньше я не замечал, как бумажные фонарики освещают ночь, но теперь могу оценить, насколько это завораживающее зрелище."

"Мягкое сияние пролетающих над головой светлячков походит на сверкание снежинок в ночном небе."

"В большом городе такого не увидишь."

show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None

show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)

"%(name_shizune)s нетерпеливо тянет меня за рукав и, нахмурившись, скрещивает руки на груди, выражая недовольство тем, что я отвлёкся."

play music music_shizune

show shizu basic_angry_close_ni at center
with charachange

shi "…"

hi "Ты ведь знаешь, что я не понимаю язык жестов."

show shizu behind_frown_close_ni
with charachange

shi "…"

"Кстати, а разве не глупо с моей стороны говорить? Она ведь не услышит."

show shizu behind_blank_close_ni
with charachange

"Я пожимаю плечами, показывая, что ничего не понимаю. %(name_shizune)s качает головой и отмахивается."

"Может, стоит попросить Мишу провести урок языка жестов?"

$ renpy.music.set_volume(0.4,2.0, "ambient")

scene bg school_roof_ni
with locationskip

"Поднявшись на крышу, я снова поражаюсь размерам школы. Территория настолько обширна, что непонятно, как я раньше не обращал на это внимания."

"Идя по крыше вслед за %(name_shizune)s, я не могу не поддаться очарованию сверкающих звёзд."

show shizu behind_smile_close_ni
with charaenter

"Мы с %(name_shizune)s усаживаемся на скамейку. Кажется, она пребывает в хорошем настроении и мягко улыбается, а ветер развевает её волосы."

"Собственно, большинство девушек одеты в юкаты. Интересно, почему %(name_shizune)s и Миша не надели их сегодня?"

"Мы смотрим на фестиваль внизу, который отсюда кажется морем янтарных фонарей и колышущихся бумажных вееров, переполненный людьми, часть которых нарядилась в праздничные юкаты."

"Юкаты хорошо бы на них смотрелись. Я мельком задумываюсь, какой тип юкаты каждая из них выбрала бы."

"%(name_shizune)s наверняка надела бы что-то традиционное, а вот насчёт Миши я не уверен."

"Прибегает Миша, тяжело дыша от быстрого бега и стараясь не уронить еду, которую несёт в руках."

"Разложив её на крыше, она позволяет себе расслабиться."

show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove

show misha hips_grin_ni behind shizu at twoleft
with charaenter

mi "А-ха-ха-ха! Это заняло немало времени! Вы не сказали, чего хотите, так что я взяла рисовый пунш, сэндвичей и сладостей! Всего понемножку!"

hi "Отлично. Давайте начнём."

"Миша откусывает кусочек от маленького треугольного сэндвича."

show misha hips_smile_ni at twoleft
with charachange

mi "Ну как, %(name_hicchan)s, что думаешь о фестивале? Он замечательный, правда?"

hi "Ага."

show shizu adjust_happy_close_ni at tworight
with charachange

shi "…"

mi "Красивые звёзды сегодня вечером. Трудно придумать более идеальный день."

scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange

"Звуки людской толпы, доносящиеся снизу, звучат как тихая музыка, смешиваясь с отдалённым стрекотом цикад."

"Я отпиваю пунш из банки и поднимаю взгляд на Мишу, которая, кажется, с комфортом спит, растянувшись на гравии с полупустой банкой яблочного сока на животе."

"%(name_shizune)s сидит с поджатыми ногами, медленно раскачиваясь взад и вперёд, словно нетерпеливый ребёнок, и смотрит на небо."

"Они обе такие красивые. Оглядевшись, я отмечаю, что многие ученики держат за руку свою девушку или парня."

"Не так далеко от нас на крыше расположилось несколько держащихся за руки парочек, созерцающих звёзды в вышине или огни фестиваля под нами."

"Часть меня хочет этого же."

"Глядя на %(name_shizune)s и Мишу, я размышляю о том, что, возможно, стоит пригласить одну из них на свидание. Может, рискнуть?"

"Золотые стрелки на изящных часиках %(name_shizune)s привлекают моё внимание, и я вижу, что уже довольно поздно. Но фестиваль ещё в самом разгаре."

"%(name_shizune)s всё так же держит за лапу плюшевую кошку, которую я выиграл. Она замечает, что я на неё смотрю."

shi "…?"

"И без раздумий протягивает её мне. Я улыбаюсь, желая спросить, что же мне с ней делать, – но она меня не поймёт."

"Я трясу головой и стараюсь объяснить, чтобы она оставила её себе. Надеюсь, она меня поняла."

stop music fadeout 8.0

"Посмотрев в сторону школы, я вижу перед собой множество людей, и все они веселы и счастливы."

"Я гляжу на них и чувствую умиротворение."

"Это было нечто. Сегодняшний день прошёл не зря."

"Но я всё ещё не могу стряхнуть с себя меланхолию и чувство вины. Они продолжают цепляться за меня, и я не могу от них избавиться."

"%(name_shizune)s что-то показывает мне жестами, а я не могу её понять. Что бы я ни сказал, она меня не услышит."

play music music_twinkle fadein 2.0 fadeout 2.0

hi "Я не понимаю тебя, %(name_shizune)s."

hi "Ладно, проехали. Интересно, мы оба считаем себя виноватыми в этом? В любом случае мне жаль, что я не могу тебя понять."

hi "Знаешь, я почти… почти рад, что ты чуть ли не силком меня сюда привела. Правда, если я попытаюсь встречаться с тобой, мне придётся крепко подумать над этой твоей стороной."

hi "Нет, в самом деле… Я рад. Сегодня было здорово."

hi "Ты бы была привлекательней, если бы чаще улыбалась. У тебя милая улыбка."

show shizu behind_frustrated_close_ni
show bg misc_sky_ni at right
with charaenter

"Разочарованная, она поднимается, сложив руки за спиной и выглядя уверенно и властно на фоне звёздного полотна."

show shizu out_serious_close_ni
with charachange

"Внезапно %(name_shizune)s вскидывает руки к открытому небу, словно удерживая его в своих руках."

"Словно она говорит мне: «Оглядись, посмотри на мир вокруг!»"

stop ambient fadeout 2.0

show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu

"Школа, купающаяся в свете фестиваля и раскрашенная цветастыми кимоно, крыша, освещённая светлячками, небо, настолько огромное, что вселяет благоговейный трепет."

"Чего она хочет? Понимание медленно снисходит на меня. Этот прекрасный вид – доказательство того, что в мире есть много вещей настолько прекрасных, что портить их плохим настроением непростительно."

"И я чувствую силу личности %(name_shizune)s, отстаивающей эту точку зрения."

hi "Спасибо, пожалуй."

hide shizu
show hill pairtouch
with charachange

"Я отворачиваюсь в сторону, но %(name_shizune)s хватает меня за плечо, при этом её часы скользят по моей щеке."

"Левой рукой она указывает на небо."
 
stop music fadeout 5.0
play ambient sfx_fireworks fadein 1.0

show fireworks behind hill
with None
show screen behind fireworks
with Dissolve(5.0)

"Со слабыми хлопками в небе начинают взрываться фейерверки, рассыпая дождь ярких красок, которые медленно исчезают во тьме."

"Я не могу вспомнить, когда в последний раз видел фейерверк, не говоря уже о таком большом. К тому же кажется, что его запускают откуда-то из школы, во что почти невозможно поверить."

"Огни в небе смешиваются со вторым залпом из города внизу, и создаётся впечатление, что совпадение не случайно, что они призваны дополнить друг друга, как две части дуэта."

"Это продолжается ещё, наверное, минут пятнадцать, а затем прекращается."

"%(name_shizune)s наконец понимает, что рука её так и лежит на моём плече, и аккуратно убирает её со стеснённым видом."

stop ambient fadeout 5.0
play music music_twinkle fadein 5.0
hide fireworks
hide screen
show hill pairnotouch
with Dissolve(5.0)

"Восстановив самообладание, она усмехается, уперев руки в боки и выпятив грудь вперёд."

"В такие моменты она выглядит словно обычная девочка-подросток. Энергичная, весёлая и беззаботная."

"Мы с %(name_shizune)s не торопясь едим, молча наблюдая, как толпа внизу постепенно редеет."

"Она сидит чуть наклонившись вперёд, удобно оперевшись подбородком на сложенные руки, и на лице её написано умиротворение с лёгким оттенком задумчивости."

"И она по-прежнему бережно держит за лапу плюшевую кошку."

"Я чувствую, что устал за день, говорю ей, что увижусь с ней и Мишей завтра, – даже и не подумав, что она меня не слышит, – и направляюсь назад к общежитию."

"Я ощущаю радость жизни и тепло в груди даже на прохладном ночном воздухе."

"Образ %(name_shizune)s, твёрдо стоящей перед самими звёздами и призывающей меня отбросить жалость к самому себе, никак не хочет покидать мой разум."

"Если… если для того, чтобы влюбиться, нужен лишь миг, то, думаю, я влюбился в неё."

"Самую чуточку."

window hide

stop music fadeout 4.0


        
#******************

#Emi Path
label ru_A39:

show bg school_dormhallway at bgright
with None

"Это как-то беспокоит, а теперь я и сам начинаю сомневаться."
  
"Стоит ли мне идти?"

"Я достаю книгу, которую собирался почитать."

"Что-то о подпольной почтовой системе, которая, может, существует, а может, и нет…"

"И эта книга короткая. Я могу прочитать её за день."

"Но хороший ли это способ провести время?"

"Ну, да. Определённо."

"Но, полагаю, пойти на улицу окажется идеей получше."

"Посмотреть фестиваль."

"Попробовать поучаствовать во всех сопутствующих развлечениях."

"В самом деле, я должен по крайней мере попробовать остаться тем дружелюбным человеком, которым был всю прошедшую неделю."

"Можно найти там что-нибудь перекусить, как предлагает мой живот."

"Почти время ланча… По крайней мере, я мог бы взять чего-нибудь с одного из тамошних лотков."

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

"Вскоре я оказываюсь снаружи, в окружении учеников и людей, которые могут приходиться кому-то из них родителями."

"Часто мне попадаются на глаза те, кто, очевидно, просто пришёл из города посмотреть на фестиваль."

"Их легко заметить."

"Они не могут перестать пялиться, и в их глазах читается: «Интересно, а что не так с {b}этим{/b} парнем?»"

"Хочется накричать на них."

"С другой стороны, не могу же я отрицать, что всю неделю тем же самым и занимался?"

"Меня накрывает волна чего-то похожего на отвращение, вины за мою собственную узколобость."

"…"

$ renpy.music.set_volume(0.6,2.0, "ambient")

scene bg school_stalls1
with locationchange

"Я отбрасываю мысли в сторону, сосредоточившись на приступах голода, которые полыхают в моём желудке, словно лесной пожар."

"Запах жареного приводит меня в край обетованный, где я могу поесть."

stop music fadeout 0.6

"Я ещё только получаю свой заказ, как меня прерывает громкий голос."

show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter

play music music_normal fadein 0.5

emi "Эй, какого чёрта ты делаешь?"

hi "Ем завтра… эм, ланч."

show emi sad_annoyed
with charachange

emi "Завтрак?"

show emi sad_angry
with charachange

emi "Ты хочешь сказать, что только что встал?"

hi "Эм-м…"

"Внезапно проспать всё утро стало чем-то вроде преступления."

hi "Нет, я имел в виду ланч… Честно."

"Она не покупается на это."

hi "Поздний завтрак?"

show emi basic_annoyed_close
with characlose

emi "Как бы то ни было, это определённо не здоровая пища."

"Она выхватывает еду из моих рук, воззрившись на меня."

"Какого чёрта она творит?"

hi "Эй, это мой завтрак!"

show emi sad_annoyed_close
with charachange

emi "Ты ведь сказал, что это ланч?"

hi "Это мой… Короче, это моя еда!"

"Эми упирает руки в боки и начинает читать мне нотацию."

show emi basic_annoyed_close
with charachange

emi "Ты и правда уже забыл свой режим питания?"

emi "Тебе надо серьёзнее относиться к своему здоровью, Хисао!"

show emi sad_angry_close
with charachange

emi "Как же твоё сердце?"

hi "С моим сердцем всё в порядке! Почти."

"В ответ она только закатывает глаза."

show emi basic_annoyed_close
with charachange

emi "Я в этом сомневаюсь."

show emi basic_closedgrin_close
with charachange

emi "Если бы это было так, тебя бы здесь не было, верно?"

"В её словах есть смысл, разумеется."

"Но я не собираюсь так просто сдаваться."

hi "Для сердца это не так уж и плохо!"

hi "Оно, безусловно, способно справиться с капелькой жира время от времени!"

"Ага, конечно. И небольшие пробежки – тоже не беда."
 
show emi basic_annoyed_close
with charachange

"Не похоже, что Эми убеждена."

"Неудивительно, мне и себя-то не удалось этим убедить."

emi "Может быть, но не тогда, когда ты дрыхнешь днями напролёт!"

"Её лицо принимает вкрадчивое выражение."

show emi basic_grin_close
with charachange

emi "Разумеется, если бы ты следовал расписанию с самого начала, то не оказался в этом положении…"

hi "Эй, у меня была весьма насыщенная неделя, знаешь ли!"

hi "Например, я едва не умер! И встретился с множеством людей, и ещё я был на крыше…"

show emi sad_annoyed_close
with charachange

emi "Это, чтоб ты знал, не является достаточным оправданием."

emi "Краткое свидание со смертью – не повод для пропуска базовых упражнений."

show emi basic_closedgrin_close
with charachange

emi "Таких как пробежка по утрам."

stop music fadeout 0.6

"Она кивает, словно приняла только что очень важное решение."

play music music_emi fadein 0.5

show emi basic_happy_close
with charachange

emi "Значит, решено!"

show emi excited_proud_close
with charachange

emi "Ты увидел, насколько ошибочен был твой путь, и готов следовать моему расписанию, правда?"

emi "Я увижу тебя завтра рано утром?"

show emi excited_happy_close
with charachange

emi "Мы будем партнёрами по бегу?"

hi "Знаешь, ты меня вчера уже убедила, что так будет лучше."

hi "Незачем убеждать меня заново."
    
"Хотя моя убеждённость как-то слабо отражается на поступках."
    
"Она права насчёт здоровой еды, в конце концов. А то, что я здесь заказал, ничуть не здоровое."
    
"Но вкусное!"
    
"Есть более важные вещи, чем вкусная еда, разве нет?"
    
"Например, оставаться живым?"
    
"Если бы Эми со своими угрозами за мои неверные решения здесь не было, я бы, наверное…"

"Эй, погоди секунду."
    
"У меня в мозгу внезапно возникает вопрос."

hi "Эй, а с какой радости тебя так волнует моё доброе здоровье?"

show emi basic_closedgrin_close
with charachange

"Эми пожимает плечами и ухмыляется."

show emi basic_grin_close
with charachange

emi "Ты ведь новичок."

emi "Я так понимаю, у тебя нет друзей, верно?"

show emi sad_grin_close
with charachange

emi "К тому же я доставляла тебе проблемы всю неделю, верно?"

emi "Я должна тебе за то, что ты не разозлился."

show emi basic_happy_close
with charachange

emi "Тем более я это фельдшеру обещала."

"А-га. Чокнутая маленькая девчушка-попрыгушка хочет вернуть моё здоровье."

"Наверное, бывает участь и похуже."

hi "Ладно, это звучит… Неплохо."

hi "Спасибо за участие."

hi "Значит, завтра утром?"

hide emi
with charaexit

"Подумав, что беседа завершена, я поворачиваюсь, чтобы уйти."

emi "Не так быстро!"

"Я чувствую, как меня хватают за воротник и тянут назад." with vpunch

hi "Эй, не так грубо!"

hi "Что тебе ещё нужно?"

show emi sad_shy_close
with charaenter

"Эми, кажется, вот-вот обидится на мой раздражённый вопрос."

emi "Думала, тебе захочется провести время в компании."

show emi basic_annoyed_close
with charachange

"Она глядит на меня с подозрением."

emi "Кроме того, ты ведь просто собирался украдкой прикупить ещё той жареной гадости, разве нет?"

"Я не собирался, но теперь, когда Эми об этом упомянула, идея кажется не такой уж и плохой."

hi "Ничего подобного!"

show emi sad_annoyed_close
with charachange

"Ещё один пристальный взгляд."

hi "Ладно, может быть, немножко…"
    
"Она всё глядит на меня в упор."
    
hi "Ладно, много."
    
"О боже, я опасен для себя и окружающих, да?"
    
"Сначала соглашаюсь, что надо выздоравливать, и тут же покупаюсь на соблазн первой попавшейся нездоровой привычки."

show emi basic_closedgrin_close
with charachange

emi "Я так и знала! Тебе нельзя доверять!"

show emi basic_grin_close
with charachange

emi "Теперь мне точно придётся пойти с тобой."

"Сама эта ситуация кажется глупой."

"Могу только представить, что думают прохожие, когда видят меня, выслушивающего наставления от девушки ростом вдвое ниже меня."

"Наверное, мне лучше пока сдаться."

hi "Отлично, делай что хочешь."

"Я вздыхаю."

"Попробую найти в этом положительную сторону."

hi "Чем тебе хочется заняться?"

show emi basic_confused_close
with charachange

"Эми ненадолго задумывается."

emi "Ну, я обещала Рин взглянуть на её фреску…"

show emi basic_grin_close
with charachange

emi "Так что давай отправимся к ней!"

"Признаюсь, мне самому слегка любопытно, что у неё в итоге получилось, и я снова отмечаю, что судьба моя могла быть куда менее приятной."

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"Я согласно киваю и вдруг обнаруживаю, что Эми практически волоком тащит меня сквозь толпу, устремляясь к нашей цели."

stop music fadeout 0.6

stop ambient fadeout 0.6

scene bg school_dormext_full at bgright
with locationchange

play music music_sadness fadein 1.0

"Ко времени прибытия к стенам общежития я чувствую, что моё сердце колотится очень сильно."

"Оно не должно так стучать после всего лишь маленькой пробежки."

"Я делаю несколько глубоких вдохов, заставляя себя расслабиться."

"По сравнению со многими учениками «Ямаку», я выгляжу вполне здоровым, но я всё равно должен находиться здесь."

"Иногда мне прямо хочется, чтобы я лишился руки или что-то в этом роде."

"По крайней мере, тогда будет очевидно, почему я тут."

"Но я, напротив, даже не кажусь больным."

"Даже сейчас, когда пытаюсь отдышаться, я просто похож на парня в плохой физической форме."

"Эми оглядывается и замечает моё бедственное положение."

show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

emi "Надеюсь, ты не собираешься умереть тут при мне?"

stop music fadeout 3.0

show emi basic_shock
with charachange

emi "Пожалуйста, не надо!"

show emi sad_depressed
with charachange

emi "Это будет моей ошибкой, и я совсем не хочу заполучить такое чувство вины."

emi "И вообще, мне хватило прошлого раза и я не думаю, что желаю снова это видеть, особенно если фельдшер скажет, что виновата во всём была я."

play music music_daily fadein 0.7

hi "Н… не, я в порядке."

hi "Пожалуй, мне всё же придётся начать бегать."

show emi basic_closedgrin
with charachange

emi "А ты ещё хотел продолжить есть то сочащееся жиром… что бы это ни было."

show emi excited_proud
with charachange

emi "Вот видишь? Хорошо, что я тебя нашла, правда?"

"Да, так и есть."

hi "Может быть."

show emi basic_grin
with charachange

"Конечно, я не скажу ей, что не оказался бы в таком виде, если бы она не проволокла меня через весь фестиваль."

"Дальнейшее общение прерывается внезапным появлением Рин."

show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)
with Dissolve(1.0)

rin "А, это вы."

show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full at center
with charamove

show rin basic_awayabsent at tworight
with charachange

rin "Привет, Эми."

show emi basic_closedhappy at twoleft
with charachange

emi "Здорово, Рин! Я взяла Хисао с собой, потому что он пытался вызвать у себя новый инфаркт!"

show rin basic_absent at tworight
with charachange

hi "Неправда!"

"Моё возражение проходит незамеченным."

show emi basic_grin at twoleft
with charachange

emi "Мы зашли поглядеть, что вышло из фрески!"

"Рин деловито кивает."

show rin basic_awayabsent at tworight
with charachange

rin "Что ж, она прямо тут."

show rin basic_deadpan at tworight
with charachange

rin "Её довольно неплохо отсюда видно."

"Мне любопытно, как долго Рин уже стоит перед своей фреской."

"Кто-нибудь вообще приходил на неё посмотреть?"

"Или мы первые?"

"Очевидно, что мы не первые её увидели."

"В смысле, она довольно-таки большая."

"Нужно постараться, чтобы её не заметить."

"И в то же время я не думаю, что кто-нибудь заговаривал о ней с Рин."

"Кроме нас, конечно."

"Я чувствую, что обязан что-то сказать."

hi "Выглядит здорово."

show rin negative_spaciness at tworight
with charachange

rin "Я всё равно не очень довольна тем, какой она получилась."

rin "Но, думаю, пойдёт."

"Она, похоже, чуть ли не убеждает себя."

"Я точно не уверен, какого результата она ждала, но, полагаю, она не вполне его добилась."

scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)

"Мы стоим перед фреской и разглядываем её от края до края."

"Я старательно сосредотачиваюсь на композиции картины."

"Она и в самом деле любопытная."

"Цвета переплетаются и смешиваются, вовлекая меня в свой хоровод."

"Картина настолько фантастическая, что я уже не вполне уверен, в том ли ещё мире я нахожусь."

"Я пытаюсь обнаружить следы красок, которые мы с Эми достали."

"Но, как ни стараюсь, нигде не вижу следов прусской лазури."

"Ну и ладно."

"Уверен, она где-то тут."

scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)

"У меня начинают ныть ноги, но Рин, похоже, не собирается двигаться с места."

"Эми решается заговорить."

show emi basic_confused at twoleft
with charachange

emi "Эй, Рин, а ты ела?"

show rin basic_deadpan at tworight
with charachange

rin "Конечно. Иначе не выживешь."

show emi basic_hes at twoleft
with charachange

emi "А как насчёт последних пяти часов?"

show rin relaxed_nonchalant at tworight
with charachange

rin "Может быть. Но я снова голодна, поэтому, возможно, я ошибаюсь."

show emi basic_closedgrin at twoleft
with charachange

"Эми улыбается и хлопает в ладоши."

show emi basic_grin at twoleft
with charachange

emi "Отлично! Пойдём с нами, перекусишь!"

"Рин молча кивает."

show rin basic_deadpannormal at tworight
with charachange

rin "Хорошо, но нам нужно спешить, пока они не заметили, что я ушла."

"Я почему-то думаю, что им всё равно."

"Кем бы «они» ни были."

stop music fadeout 2.0

scene bg school_stalls1 at Fullpan(8.0)
with locationskip

"Когда мы возвращаемся к прилавкам с едой, я жадным взглядом окидываю выставленную там жареную пищу."

"Нет, лучше не надо."

"Я совершенно уверен, что Эми всё равно мне не позволит."

scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange

"Мы находим отличное местечко на газоне и присаживаемся, чтобы расправиться со своими покупками."

"Ну, вернее, моими покупками. Как-то так вышло, что я заплатил за всю еду."

"Удивительно, но моя (нежареная) еда вполне вкусная."

"Тишина окутывает нашу компанию – мы с Эми едим, а Рин глядит на… куда-то глядит, в общем, время от времени откусывая кусочек-другой."

"Я первым доедаю свою порцию и ложусь на траву."

"Эми бросает на меня взгляд, не отрываясь от еды."

play music music_dreamy fadein 0.3

show emi basic_confused at twoleft
with charachange

emi "Устал, Хисао?"

hi "Наверное, немножко."

show emi basic_annoyed at twoleft
with charachange

emi "Ну, не проспи завтра, постарайся."

show emi excited_proud at twoleft
with charachange

emi "Мы утром начинаем бегать, помнишь?"

"Вообще-то, я как раз забыл."

"Я сейчас просто наслаждаюсь спокойным отдыхом."

"Гулять с ними по фестивалю оказалось весело."

hi "Да, я поставлю будильник."

show emi basic_annoyed at twoleft
with charachange

emi "Попробуй только не прийти!"

show emi basic_closedgrin at twoleft
with charachange

emi "Я рассержусь, если ты не придёшь!"

hi "Боже упаси."

show rin basic_lucid at tworight
with charachange

rin "Думаю, Бог тут ни при чём."

show rin basic_deadpan at tworight
with charachange

rin "Если только не случится что-нибудь невероятное и твой будильник закоротит."

show rin basic_deadpannormal at tworight
with charachange

rin "Тогда это может оказаться божественным провидением."

show emi basic_grin at twoleft
with charachange

emi "Значит, не надо навлекать на себя никаких провидений."

"В моей голове начинает формироваться план."

"План, на который моя совесть отзывается уколом вины, но я всё равно собираюсь привести его в исполнение."
    
"Чёрт побери, я заслужил немного жареной пищи."
    
"И вообще, я начинаю бегать только завтра, так?"
    
"Значит, расписание заработает тогда, а не сегодня."
    
"Следовательно диета тоже начинается завтра, следовательно сегодня мне можно позволить себе что-нибудь нездоровое."
    
"Своего рода последнее «прощай» всему тому, что я жадно ел до больницы."

hi "Кстати, думаю, мне стоит вернуться в свою комнату."

hi "Мне надо доделать домашку, а поскольку я завтра собираюсь бегать, то мне надо лечь пораньше…"

show emi basic_annoyed at twoleft
with charachange

"Снова эти прищуренные глаза."

show emi sad_annoyed at twoleft
with charachange

emi "Ты уверен, что не собираешься улизнуть и купить себе всякой жареной гадости?"

hi "Не, я слишком сытый для этого."

"В подтверждение своих слов я похлопываю себя по животу."

hi "И к тому же вы всё равно меня обчистили."

show emi basic_closedhappy at twoleft
with charachange

"Эми хихикает. Неожиданно приятный звук."

"Чувствую ещё один укол вины."
    
"Она же должна понимать, что я ей вру, разве нет?"
    
"Или она настолько мне верит?"
    
"Я чувствую себя чуть ли не чудовищем."

show emi excited_proud at twoleft
with charachange

emi "Всё часть моего генерального плана, Хисао."

show emi basic_closedgrin at twoleft
with charachange

emi "Ну, тогда, наверное, увидимся завтра утром."

show emi basic_grin at twoleft
with charachange

emi "Спасибо за угощение! И за компанию!"

"А я-то думал, это она оказывает мне услугу."

show rin relaxed_surprised at tworight
with charachange

"Рин утвердительно кивает и машет мне ногой."

rin "Я не скажу «увидимся завтра», потому что это словно предсказывать будущее, а я вполне уверена, что на такое не способна."

hi "…"

hi "Хорошо."

hi "Ладно, пока."

"Странно, но я рад, что решился выйти сегодня из комнаты."

"Не самый плохой способ начать вторую неделю пребывания здесь, это уж точно."

stop music fadeout 2.0

scene bg school_stalls1
with locationchange

"Убедившись, что скрылся с глаз Эми, я сразу же бегу к прилавкам с едой и покупаю пирожные."
    
"По крайней мере, они не жареные, верно?"
    
"Это чуть лучше, чем я изначально планировал."
    
"Правда, мне всё равно неловко, что я соврал Эми."
    
"Её ведь действительно беспокоит моё здоровье."
    
"Я должен как-нибудь ей отплатить."
    
"Вернусь-ка я лучше к себе."

"К тому же у меня {b}есть{/b} важное дело."

scene bg school_dormhisao
with locationskip

"Меня дожидается книга, и я плюхаюсь на постель, принимаясь читать её под вспышки фейерверков."

scene bg school_dormhisao_ni
with Dissolve(2.0)

"Наконец начинает сказываться вся эта сегодняшняя ходьба (или, точнее, беготня)."

"Я и правда не в форме."

"Наверное, всё-таки неплохо, что Эми принудила меня начать бегать с ней по утрам."

"Я буду ждать этих пробежек."

window hide



#######################
#Rin Path

label ru_A40:

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_dormext_full
show crowd
with locationskip

"Когда я заставляю себя выйти за парадную дверь, снаружи меня встречает радостный гомон толпы."

"Территория школы за один день и одно утро превратилась в площадку для праздника."

"Красочные плакаты выстроились вдоль главной дорожки от основного входа к зданию школы."

"Кто-то ещё перетаскивает снаряжение, но за большей частью прилавков уже стоят ученики, расслабленные и готовые к бою."

"Большинству сегодня пришлось встать пораньше, чтобы закончить приготовления."

"Чувство вины набрасывается на меня, но скоро уходит прочь."

"Я, в конце концов, перевёлся совсем недавно."

"Посетители уже прогуливаются между рядами."

"Я вижу несколько молодых семей, в которых озабоченные родители стараются утихомирить своих веселящихся чад…"

"…некоторое количество наших учеников в сопровождении родителей…"

"…и множество старого и малого люда, чью причину появления здесь я не могу даже представить."

play sound sfx_normalbell

"Из системы школьного вещания доносится звон колоколов, и директор объявляет скрипучим голосом об открытии праздника."

"Все вежливо аплодируют, пусть и без особого энтузиазма."

# Applause sound effect?

"Школьный фестиваль… В моей прежней школе они не проводились. Мне это кажется чем-то старомодным, особенно учитывая то, из какой школы я перевёлся, но всё же немного захватывающим."

"Выходной день кажется слаще после первой недели тяжёлой работы, хоть я и пролежал до того четыре месяца на больничной койке."

"Помнится, во время своего заточения в больнице я мечтал оказаться пусть даже на уроке математики, лишь бы не на койке."

"Не могу вспомнить программу фестиваля, несмотря на то что Муто как-то рассказывал о ней на уроке."

"Я начинаю спускаться по ступенькам общежития, собираясь обойти весь праздник и попробовать всё, что он может мне предложить, но добираюсь лишь до основания лестницы."

stop ambient fadeout 1.0

hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)

"Несколько человек изучают фреску Рин, а сама художница стоит, прислонившись к стене в нескольких шагах от неё, выглядя при этом так, будто тихо-мирно умирает со скуки."

hi "Доброе утро."

show rin relaxed_surprised at tworight
with charachange

rin "Привет."

hi "Как идут дела?"

show rin relaxed_nonchalant at tworight
with charachange

rin "Никак не идут."

rin "Я застряла."

hi "В смысле «застряла»?"

rin "Это значит, что я не могу ходить. Думаю, мои ноги после вчерашнего вышли из строя."

hi "Больно?"

show rin relaxed_sleepy at tworight
with charachange

rin "Сложно сказать. Наверное."

"Нагрузка во время работы над фреской была больше, чем она давала понять. Я думаю, она просто слегка перегрузила мышцы или что-то вроде того. Я хочу расспросить её подробней, но Рин плавно меняет тему."

show rin basic_awayabsent at tworight
with charachange

rin "Друзья учителя заходили."

show rin basic_absent at tworight
with charachange

rin "Потом они собрались в город на обед и пригласили меня. Хорошо, что мои ноги настолько устали."

hi "Но ты осталась сидеть тут? Это плохо."

show rin basic_lucid at tworight
with charachange

rin "Я просто жду, пока снова смогу ходить. По здравому рассуждению, это же должно рано или поздно произойти."

rin "Учитель был рад, что я закончила фреску."

hi "А как иначе?"

show rin basic_awayabsent at tworight
with charachange

rin "Но я не знаю, на самом ли деле она закончена."

hi "Вот как?"

show rin basic_deadpanupset at tworight
with charachange

rin "Вчера я думала, что сделала всё, но сейчас уже не уверена. Мне надо было нарисовать больше деталей. Может быть. Наверное. Очень трудно сказать наверняка."

"Законченная или нет, в ярком дневном свете фреска выглядит великолепно."

scene bg mural at Position(xalign=0.05)
with Dissolve(2.0)

"Основной её элемент – разные части человеческого тела, в большинстве своём искажённые, снова и снова повторяющиеся в причудливых вариациях."

"Они кажутся грубыми, будто их бессмысленно разбросали и коряво покрасили, но в каждую деталь вложено много мысли и труда."

show bg mural at Position(xalign=0.25)
with charamove

hi "А у этого из головы растёт лягушка?"

rin "Это золотая рыбка."

show bg mural at Position(xalign=0.45)
with charamove

hi "А что это?"

#he's pointing at a randomly chosen detail on the mural. you can like zoom on it or whatever. Do pick something that isn't obviously "something"

rin "Ничего."

show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None

"Ну и ладно…"

"Стена настолько широка, что мне приходится крутить шеей влево-вправо, чтобы разглядеть всю картину."

"Это сложно оценить как единую композицию. Кажется, что части не подходят друг к другу, но я полагаю, что они всё же объединяются в целое."

"Пусть я понятия не имею, что изображает эта абстракция, но выглядит она красиво. И мне этого достаточно."

"Я устраиваюсь рядом с Рин, прислонившись к стене так же, как и она."

"Весёлые звуки фестиваля становятся громче по мере прибытия всё новых и новых горожан."

"Общежития находятся далеко от основных аттракционов в главном здании и киосков, расположившихся в школьном дворе, так что большинство посетителей сюда ещё не добралось."

show rin negative_spaciness_close at offscreenright
with None

show rin negative_spaciness_close at tworight
show bg mural at Position(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))

"На лице Рин появляется какое-то утомлённо-скучающее выражение, из-за чего она кажется отстранённой от всего, что происходит вокруг."

"Она удивительно немногословна. Может, виной тому сильная боль?"

hi "Ну так что люди искусства сказали о твоей фреске?"

show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)

"Мой вопрос пробуждает Рин ото сна. Она лениво поворачивает ко мне лицо."

show rin basic_deadpan_close at tworight
with charachange

rin "Я не уверена."

show rin basic_awayabsent_close at tworight
with charachange

rin "Я думаю, она им понравилась? Наверное, так и есть."

hi "А ты сама? Ты довольна фреской? Раз я в некотором роде поучаствовал, то было бы ужасно, если бы ты осталась недовольна."

"Рин качает головой, прикусив нижнюю губу."

show rin negative_sad_close at tworight
with charachange

rin "Думаю, получилось сносно. Не плохо, но и не хорошо. Просто… получилось. У меня в голове нет никаких мыслей по этому поводу, ну и пусть."

hi "Можно ещё спросить? Что на самом деле изображено на картине? Я думал об этом вчера, когда ты сказала, что ничего."

hi "Но это же логическая ошибка, ведь так? Нельзя создать что-то из ничего, даже в искусстве."

show rin negative_annoyed_close at tworight
with charachange

"Рин хмурится и, повернув голову, глядит на облака."

rin "Я не знаю. У меня не очень-то получаются объяснения. Это просто фреска, в ней нет ничего особенного. Я говорила."

"Мои расспросы её, похоже, раздражают."

rin "Я не знала, что я буду рисовать, поэтому решила нарисовать просто фреску."

rin "На этой фреске изображена фреска."

show rin basic_deadpancontemplation_close at tworight
with charachange

rin "Нет, постой. Я сейчас подумала, что лучше сказать так: «Она изображает саму себя»."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Значит… её фресочность на максимуме, настолько, насколько у меня получилось; так что если ты думаешь, что в ней есть некий смысл, то он примерно вот такой."

"Это бессмыслица."

"Значение… Я чувствую, как уголки моего рта поднимаются вверх, складываясь в улыбку с лёгкой тенью озабоченности."

scene mural all
with flash

"Я никогда не понимал живопись в полном смысле слова."

"Мне знакомы основы – она является средством для обмена идеями и мыслями."

scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash

"Однако я не учился тому, как надо воспринимать предметы живописи, как прочувствовать то, что художник намеревался выразить посредством неё."

"Я знаю, что тут не нужно никакого специального умения, но мой мозг почему-то не может связать картину с чем-то иным, кроме воспринимаемого моими глазами. Всё, что я вижу, – лишь фреска."

"Я могу восхититься мастерством рисунка, в конце концов даже я знаю разницу между плохой живописью и средней, между средней и хорошей."

"Но я не способен ни на что большее, так что не спрашивай меня о её значении, Рин."

"После её ответа у меня пропадает желание расспрашивать её дальше."

stop music fadeout 0.8

hi "Так чем займёшься, когда встанешь на ноги?"

scene bg mural at Position(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash

rin "Ничем."

hi "Ничем? Но сейчас же фестиваль, разве тебе не хочется повеселиться?"

show rin basic_absent_close at tworight
with charachange

rin "Мне и так хорошо."

hi "Ты не очень-то общительна, да?"

"Думаю, сейчас я больше убеждаю её, чем себя. Хотя меня и самого фестиваль не особо волнует, мне слегка любопытно поглядеть, на что он похож, только и всего."

"Её ответ меня не удивляет."

show rin basic_awayabsent_close at tworight
with charachange

rin "Нет, не общительна."
   
hi "Да и я, в общем-то, тоже…"

show rin basic_deadpan_close at tworight
with charachange

rin "Если тебе хочется, то иди."

hi "Знаю, но я могу составить тебе компанию. Я ещё не привык ко всему этому, так что никуда торопиться не собираюсь."

hi "Но могу и уйти, если ты хочешь побыть одна."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Я была бы рада, если бы ты остался."

"Походив вокруг да около, мы наконец к чему-то приходим. Её ответ вызывает во мне чувство странной радости, поэтому я остаюсь."

"Мне нравится быть рядом с ней. Странная тёплая аура безмятежности, которую она излучает, делает молчание уютным. Я очень это ценю."

"Мы молча глядим на проходящих мимо людей, пока все остальные весело общаются друг с другом."

"Некоторые ученики ведут семьи к общежитиям, чтобы показать свои комнаты. Они проходят мимо нас и мимо фрески, взглянув, может, разок-другой."

"Я больше думаю не о них, а о своей напарнице, пытаясь пробиться сквозь загадочную, нечитаемую стену её лица."

show rin basic_awayabsent_close at tworight
with charachange

show rin basic_absent_close at tworight
with charachange

show rin basic_awayabsent_close at tworight
with charachange

"Глаза Рин безустанно перебегают от одного проходящего мимо человека к другому."

"Ждёт ли она, что кто-нибудь остановится перед фреской, надеется ли втайне, что её творчество вызовет отклик?"

"Я не думаю, что в ней могут признать художницу. В конце концов, мы просто сидим тут, как парочка неприкаянных, а у неё даже нет рук."

"Я вообще сомневаюсь, что Рин стала бы напрашиваться на комплименты. Она для этого кажется слишком нелюдимой."

play music music_rin fadein 0.3

"Мимо проходит всё больше людей, некоторые тычут пальцем во фреску, обмениваются словами, которые я не могу расслышать. Кто-то роняет себе на ботинок мороженое. Бедолага."

hi "Всем, похоже, нравится."

"Высказываю я предположение, вбросив тему в разделяющий нас спёртый летний воздух."

"Рин отвечает не сразу, но я уже почти привык к подобным паузам. Она будто с большой осторожностью подбирает слова, во что, если честно, трудно поверить, учитывая, какая мешанина срывается с её языка."

show rin basic_lucid_close at tworight
with charachange

rin "Я хотела создать её такой, чтобы на неё можно было просто глядеть не думая. А потом я поняла, что в этом нет смысла. Поэтому получилась смесь того и сего."

show rin negative_spaciness_close at tworight
with charachange

rin "Издалека кажется, будто кого-то стошнило стадом бабочек на стену. Именно то, чего не хотела та несносная президентша. Для этого есть слово?"

hi "Что за слово?"

show rin basic_deadpannormal_close at tworight
with charachange

rin "Такое. Каким словом называют скопище бабочек?"

hi "Бабочки?"

show rin basic_deadpanupset_close at tworight
with charachange

rin "Нет, как стадо, или косяк, или куча."

hi "А. Я не знаю. Может, стая?"

rin "Может, людям нравится блевотина из бабочек."

show rin negative_confused_close at tworight
with charachange

"Рин смотрит на фреску с удивительно недовольным выражением лица."

rin "Середина могла быть куда лучше."

show rin negative_annoyed_close at tworight
with charachange

rin "Обычно я люблю промежутки, но этот стал просто болью в заднице. Не буквально, конечно… но потом и она началась. Да, всё-таки, похоже, буквально."

hi "Не будь к себе чересчур требовательной."

show rin basic_deadpannormal_close at tworight
with charachange

"Она одаряет меня изумлённым взглядом, но закрывает рот."

stop music fadeout 3.0

scene bg school_dormext_full at bgright
with locationchange

"Я начинаю задумываться, не стоит ли мне уйти и потратить своё воскресенье на что-нибудь более полезное."

"Это просто апофеоз замкнутости. Целый свободный день, праздник прямо за моей дверью, а что делаю я?"

"Сижу тут с Рин; мы с ней словно два отщепенца, которым нечем заняться, кроме как думать, какая же это жалость – быть лишь наблюдателем."

"Даже осознав, насколько я жалок, я ничего не предпринимаю. Я не встаю и не иду отрываться в океане веселья."

play sound sfx_rustling

centered "*шорх-шорх*"

"…"

centered "*суетится*"

play sound sfx_rustling

centered "*шорх*"

"…"

scene bg mural at Position(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange

"Рин беспокойно вертится, постоянно перекладывая одну ногу на колено другой и обратно."

"На лице у неё страшно раздражённое выражение."

hi "Что-то не так?"

show rin basic_deadpanupset_close at tworight
with charachange

rin "Да. Нет. Да."

scene bg school_dormext_full at bgright
show rin basic_deadpanupset at Move((0.7,1.0,0.5,0.8),(0.7,1.0,0.5,1.0),0.5, time_warp=_ease_in_time_warp)
with locationchange

"Она внезапно вскакивает на ноги. Удивительно, я думал, она ещё обездвижена, но, выходит, нет."

show rin negative_confused at tworight
with charachange

rin "Мне надо пойти и разыскать Эми или кого другого, мне нужна кое-какая помощь."

hi "Я помогу."

show rin relaxed_nonchalant at tworight
with charachange

rin "Нет, спасибо. Один из нас должен остаться здесь на всякий случай."

hi "Не глупи. С тех пор как я сюда пришёл, не случилось абсолютно ничего интересного, не считая парня, который уронил мороженое на ботинок. Давай я тебе помогу, мне скучно."

hi "Так в чём дело?"

show rin negative_annoyed at tworight
with charachange

"Губы Рин плотно сжимаются, превращаясь в одну почти идеально горизонтальную линию."

show rin basic_lucid at tworight
with charachange

"Она закрывает глаза и глубоко вздыхает."

"Когда она раскрывает веки, в её тёмных глазах читается пугающе суровое выражение, от которого мне делается не по себе."

play music music_rin fadein 0.2

show rin negative_angry at tworight
with charachange

rin "Хисао, хочешь ты это услышать или нет, я не знаю, но в любом случае ты не оставляешь мне иного выбора."

rin "У меня критические дни и мне нужна помощь. Однако я не думаю, что наши отношения зашли так далеко, что я могу позволить тебе стянуть с меня нижнее бельё, находясь в женском туалете, даже если ты и предложишь."

rin "Вот почему ты должен остаться здесь, а я – пойти искать Эми."

"Кровь приливает к моим щекам, как набегающая волна, пока мозг безуспешно пытается найти ответ, но сейчас я могу думать только о том, что это самая разумная вещь, которую я услышал от Рин за четыре дня знакомства."

hi "Ага."

hide rin
with charaexit

"Не желая встречаться с Рин глазами, я отворачиваюсь в сторону, притворяясь, что гляжу на чьих-то родителей."

"Уголком глаза я замечаю, как Рин поворачивается на месте и без лишних раздумий отправляется прочь."

"Мне хочется провалиться на месте."

"Интересно, надолго ли ушла Рин… и вернётся ли она вообще?"

"…"

scene bg mural at Position(xalign=0.6)
with shorttimeskip

stop music fadeout 2.0

"Некоторое время спустя она всё же возвращается, появившись словно из ниоткуда и присев там же, где была, – рядом со мной."

show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

rin "Я вернулась."

"Произносит она ровным голосом, будто я ничего не сморозил. Я тоже предпочитаю обо всём забыть и молчу."

scene bg mural_ss at Position(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Move((0.7,1.0,0.5,.85),(0.8,1.0,0.5,.9),3.0, time_warp=_ease_in_time_warp)
with Dissolve(3.0)

"Время проходит в бездействии, солнечные лучи свысока падают на главное здание. Они бьют мне прямо в глаза, но я только щурюсь, вместо того чтобы подвинуться."
  
"Ещё немного, и становится больно даже чуть приоткрыть глаза, а виски начинает ломить."

hi "У меня голова разболелась. Не день, а головная боль, представляешь?"

show rin basic_deadpan_close_ss at tworight
with charachange

rin "Ты голоден?"

hi "И как это связано с головной болью?"

show rin basic_deadpansurprised_close_ss at tworight
with charachange

rin "Никак. Я спросила, потому что сама проголодалась."

"…"

"Её безразличная серьёзность смывает моё раздражение своей нелепостью, и я снова замечаю, как приподнимаются уголки моих губ."

hi "Знаешь что? Я тоже."

hi "Пойду куплю нам еды. Чего бы тебе хотелось? Я угощаю."

show rin basic_lucid_close_ss at tworight
with charachange

rin "Всё равно."

play music music_dreamy fadein 3.0

show rin basic_deadpannormal_close_ss at tworight
with shorttimeskip

"Вернувшись с едой, я отдаю одну порцию Рин, другую оставляю себе и, не говоря ни слова, мы принимаемся есть."

show rin negative_spaciness_close_ss at tworight
show rin_shadow negative at Position(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange

"Рин смотрит вверх со свисающей из уголка рта вилкой."

rin "Что такое облака? Я всегда думала, что это мысли неба или типа того. Потому что их нельзя коснуться."

hi "Ты так думала, когда была ребёнком?"

rin "Нет, на прошлой неделе."

rin "Может, потому что иногда мои мысли кажутся облаками. Пушистые, белые и неторопливые."

rin "Как будто небо оказалось у меня в голове. Как будто моя голова – небо."

hi "Небо твоего разума?"

rin "Закрой глаза и подумай о небе. Ты не сможешь думать ни о чём другом, пока не остановишься."

scene black
with shuteye

"Я пробую так сделать. Работает. Волшебство?"

scene bg mural_ss at Position(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Position(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with openeye

"Открыв глаза, я вижу, как Рин изучающе смотрит на меня. Мне от этого неловко, потому что она ничего не говорит. Я отворачиваюсь."

scene bg misc_sky_ss at Fullpan(20.0)
with locationchange

hi "Облака – это вода. Испарившаяся вода."

hi "Знаешь, говорят, что почти вся вода в мире часть своего существования проводит в виде облаков."

hi "Каждая твоя капля слёз, крови или пота когда-нибудь станет облаком. И вся вода в твоём теле тоже отправится наверх после твоей смерти. Хотя это может занять какое-то время."

rin "Твоё объяснение лучше любого из моих."

hi "Потому что это правда."

rin "Должно быть."

"Я возвращаюсь к еде, пока она не остыла."

"Стена начинает отбрасывать на нас вожделенную тень, поскольку солнце продолжает своё путешествие по небесному своду."

"Но день уже плавно переходит в вечер, так что наш обед – скорее ужин. Или какое там слово можно подобрать для такого приёма пищи."

"Но, как его ни назови, он определённо вовремя. Я сто лет уже не ел."

"…"

"Утолив голод, я издаю удовлетворённый вздох. Рин съела не всё, но тоже, видимо, закончила с едой."

"Я откидываюсь назад, наслаждаясь атмосферой. Толпа редеет, но звуки веселья пока не стихают. Все, похоже, с удовольствием проводят время."

"А почему бы и нет? Тепло, идеальный летний день, когда солнце греет жарко, но не слишком."
   
"Солнце скоро сядет. Время и правда летит быстро."

scene bg mural_ss at Position(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Position(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with locationchange

hi "Мы сидим здесь уже шесть часов."

show rin basic_deadpansurprised_close_ss at tworight
with charachange

rin "Да, верно."

show rin basic_deadpancontemplation_close_ss at tworight
with charachange

rin "Тебе хочется заняться чем-то другим?"

hi "Нет, не особо."

show rin basic_deadpannormal_close_ss at tworight
with charachange

rin "И мне тоже."

show rin basic_lucid_close_ss at tworight
with charachange

"Она меняет позу и прислоняется к стене, и я следую её примеру, давая расслабиться своему телу."

"Мы сидим ещё несколько минут не говоря ни слова."

"Я пытаюсь понять настроение Рин по её внешнему виду, по напряжению мышц лица, по слабым намёкам на какое-либо выражение, проплывающим по её лицу. Всё без толку. Она непроницаема, как всегда."

scene bg school_dormext_full_ss
show crowd_ss
with locationchange
$ renpy.music.set_volume(0.6, 0.2, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 0.2

"Толпа накатывает то туда, то сюда, люди счастливо болтают друг с другом. Очень мало кто всерьёз уделяет внимание фреске, и ещё меньше людей – нам."

"Я рассеянно кручу в руках пару камешков."

"Делать что-то просто ради того, чтобы что-то делать, – самая суть безделья."

"По миллиметру солнце клонится всё ниже к веткам деревьев, меняя цвет неба при своём приближении к горизонту с жёлто-золотого до оранжевого, а потом до красного, говоря нам, что закат уже рядом."

"После такой плотной трапезы мой желудок будто полон свинца, но кирпичная стена кажется удивительно приятной подушкой для спины."

"Я пытаюсь бороться с напавшей на меня дремотой, но безуспешно."

#Hisao falls asleep, so fade to black or whatever
scene black
with shuteye

stop music fadeout 4.0
$ renpy.music.stop(channel=6,fadeout=2.0)

with Pause(4)
$ renpy.music.set_volume(1.0, 0.2, "ambient")
play ambient sfx_fireworks fadein 1.0

scene bg misc_sky_ni
with openeye

"Вздрогнув, я просыпаюсь."

"Низкий грохот сотрясает школьную территорию. В моих глазах пляшут, как звёзды, шлейфы ярких искорок."

"Что-то взмывает к небесам со стороны стадиона."

"За ним тянется огненный хвост, а затем следует вспышка, освещающая небо высоко над школой красными и жёлтыми огнями с ещё одним громким хлопком."

show fireworks
with dissolve

"Фейерверки."

"Внезапная вспышка света на холсте ночного неба разбудила меня, заставив осознать, что уже давно стемнело."

"Долго я спал? Я едва могу пошевелиться и не чувствую правую руку."

"Пытаясь её согнуть, я понимаю почему."

play music music_twinkle fadein 0.3

show rin basic_lucid_close_ni at Move((1.0,1.1,0.5,1.0),(0.9,1.1,0.5,1.0),1.0, time_warp=_ease_in_time_warp)
with Dissolve(1.0)

"Рин всем весом облокотилась на моё плечо, почти что упав мне на колени."

"Она крепко спит, и даже фейерверки не тревожат её сон."

"Рот слегка приоткрыт, а глаза мирно сомкнуты. Невинное лицо спящего ребёнка."

"Я осторожно трясу Рин свободной рукой, стараясь её разбудить или, если не удастся, подвинуть так, чтобы высвободить вторую руку."

"Лицо Рин дёргается, и её веки сжимаются плотнее, как будто сопротивляясь пробуждению."

show rin basic_deadpanupset_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"Она постепенно открывает глаза, но оставляет их полуприкрытыми. Свет фейерверков проникает сквозь её ресницы, отражаясь яркими вспышками в зелёной радужке; затем она поднимает взгляд на меня и хмурит брови."

show rin basic_deadpan_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

rin "Ещё немного, ладно?"

"Голос Рин сонный и неторопливый, её почти неразборчивое бормотание лениво повисает в воздухе."

"Похоже, она не вполне осознаёт ситуацию."

show rin basic_lucid_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"Рин снова роняет голову мне на плечо, наваливаясь на меня всем своим весом."

"Она ворочается под боком, устраиваясь поудобней и одновременно лишая меня всякого удобства."

"Я отчётливо чувствую тепло Рин и то, как вздымается и опадает грудь девушки, касающаяся моей руки; вскоре её дыхание возвращается к размеренному ритму."

"Не могу не позавидовать её способности засыпать несмотря ни на что, а также её непосредственности, позволяющей использовать как подушку того, кого знаешь меньше недели."

"Ракеты по одной взмывают в небо, распускаясь красными, зелёными и золотыми цветами, – и всё это сопровождается охами и ахами зрителей."

"Я пытаюсь выкинуть сбивающую с мыслей близость Рин из головы, ибо что я могу поделать? Я только надеюсь, что её «ещё немного» таковым и окажется."

"Один за другим блистающие всполохи рождаются и умирают за краткий миг, раскрашивая тёмное ночное небо и превращая его в постоянно изменяющуюся абстрактную картину."

"Я слушаю низкое буханье взрывов и тихое дыхание Рин, понемногу прочищая голову от сонного дурмана."

"К счастью, Рин просыпается до окончания фейерверков."

show rin relaxed_sleepy_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

rin "Я заснула."

show rin basic_awayabsent_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

show rin basic_lucid_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

show rin basic_awayabsent_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"Наконец она полностью открывает глаза и несколько раз моргает."

hi "Ты заснула на мне. Дважды."

show rin basic_absent_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

rin "Тебе не понравилось?"

hi "Э-э… Ну-у…"

show rin basic_absent_close_ni at Move((0.9,1.1,0.5,1.0),(0.9,1.0,0.5,1.0),1.0, time_warp=_ease_time_warp)

"Не обращая внимания на мою запинку, Рин выпрямляется, отстраняясь от меня."

hi "Ты тяжёлая."

"Это неправда – она весит всего ничего, – но мне надо хоть чем-то её попрекнуть, пусть даже это удар ниже пояса. Моя насмешка не оказывает на Рин никакого воздействия, поскольку её внимание устремлено вверх, к вспышкам фейерверков."

show rin negative_spaciness_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

"Она кажется загипнотизированной игрой их красок."

"Лёгкое колющее ощущение пробегает по моей руке, когда кровь вновь начинает течь по венам. Оно неприятное, но позволяет мне избавиться от головокружения."

"Всё больше и больше ракет взмывает к небу, яркие цвета разрывов отражаются на облаках."

"Мы оба не отрываясь глядим на фейерверк сквозь полог деревьев, зачарованные представлением."

"У нас мог бы быть куда лучший вид на небо, сдвинься мы всего на несколько метров, но никто даже и не думает внести такое предложение."

show rin negative_worried_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

rin "Я очень люблю фейерверки, пусть мне от них и становится как-то грустно. Как будто им очень хочется, чтобы ты взглянул на них, какие они громкие и яркие, но только поглядишь – а их уже нет."

show rin negative_sad_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

rin "Как будто они даже не реальны."

"…"

hi "Они настоящие, я точно тебе говорю."

hi "Всё это… настоящее, понимаешь?"

hi "Если задуматься, то ничто на самом деле не длится долго. Даже что-то вроде моей жизни или твоей – это лишь миг в истории мира, как одна из тех ракет. Хлоп – и нас нет."

hi "Но мы живём, не так ли?"

"Да, это реальность. Рин, сидящая рядом со мной, громкие взрывы фейерверков, широкое, бескрайнее небо. Эти вещи определённо настоящие, даже если они не останутся надолго."

"Я чувствую тепло в груди и гадаю, вызвано ли оно близостью Рин или же я просто рад быть живым."

show rin negative_spaciness_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

rin "Не представляю, что на это ответить."

hi "Да ничего… наверное, я просто разговариваю сам с собой."

hi "Знаешь, фейерверки прекрасны… Но в конечном счёте разве не глупо тратить столько денег на горстку искорок, рассыпающихся в долю секунды?"

show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None

show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"Рин отрывает взор от всё ещё продолжающегося представления и отстраняется, глядя на меня с неприязненным выражением."

rin "Ух ты, никогда бы не подумала, что ты такой циник."

hi "Циник – довольно грубое слово. Предпочитаю называть себя реалистом."

show rin relaxed_surprised_close_ni at tworight
with charachange

rin "А разве «реалист» – не то слово, которым циники обычно себя называют?"

stop ambient fadeout 1.0
hide fireworks
with dissolve

"Последняя ракета взрывается серебряными и голубыми искрами, на мгновение накрывая школу зловещей тишиной, а затем толпа начинает двигаться к главному выходу, напоминая стадо."

"Клочки серого дыма плывут к общежитию со стадиона. Резкий серный запах пороха, который они несут с собой, кажется пропитывает мою одежду и волосы."

hi "Что, всё?"

stop music fadeout 3.0

show rin negative_spaciness_close_ni at tworight
with charachange

rin "Вроде бы да."

scene bg school_dormext_full_ni
with locationchange

"Я встаю и потягиваю свою пострадавшую спину. Спать, прислонившись к кирпичной стене, всё же не лучшая идея."

show rin negative_spaciness_ni at Move((0.7,1.0,0.5,0.8),(0.7,1.0,0.5,1.0),1.0, time_warp=_ease_in_time_warp)
with Dissolve(1.0)

show rin basic_absent_ni at tworight
with charachange

"Рин тоже встаёт и поворачивается ко мне. Она явно устала, её глаза выжидательно смотрят на меня."

"Несмотря на то что ей обычно с трудом удаётся сосредоточить взгляд, сейчас она глядит прямо на меня – такое за прошедшую неделю случалось нечасто."

hi "Так… значит…"

"Я вдруг понимаю, что это было почти что свидание, пусть и спонтанное. Пусть даже мы ничего не делали."

"Но это было и не совсем свидание… но почему же у меня тогда краснеют щёки и я запинаюсь?"

"Не знаю, что мне сказать Рин, явно ожидающей моих слов, но, к счастью, она решает этот вопрос за меня."

show rin basic_deadpannormal_ni at tworight
with charachange

rin "Спокойной ночи, Хисао."

hide rin
with charaexit

"Она одаряет меня продолжительным взглядом, оглядывая с головы до пяток, затем разворачивается на месте и удаляется, растворяясь в толпе."

"…"

hi "Да… Доброй ночи."

"Я остаюсь в одиночестве, давая ответ прохладному ночному воздуху."

"Эх."

"Ничего подобного я от фестиваля не ожидал."

"Мы с Рин провели целый день на одном месте, хоть никто из нас и не предлагал что-либо сделать."

"У меня просто не нашлось занятия получше, и, очевидно, у неё тоже."

"Тепло тела Рин ещё ненадолго задерживается в моём теле, прежде чем раствориться в наступающей ночи."

window hide

    
#******************
#Lilly/Hanako path start

label ru_A41b:
#lol label hackery. Yeah...

scene bg school_gardens
#with shorttimeskip
with locationchange

"Я покупаю пластиковую тарелку такояки в киоске соседнего с нашим класса, сажусь в школьном сквере и принимаюсь глядеть на прохожих, неуверенно ковыряя по кусочку довольно безвкусную еду."

"Полагаю, жаловаться не стоит. Всё же лучше, чем ничего, и стоит недорого."

"Я гляжу на школу – созерцание приходящих и уходящих людей оказывается удивительно неплохим способом скоротать время во время еды."

play music music_tranquil fadein 0.3

play ambient sfx_crowd_outdoors fadein 0.3

show bg school_courtyard
show crowd
with locationchange

"Маленькие дети в сопровождении родителей или бабушек-дедушек шумно носятся от одного развлечения к другому; одной рукой они цепляются за сопровождающего, а в другой держат красочную сладкую вату непомерной величины."

"Кажется, преобладают люди пожилого возраста. Это я заметил, ещё когда гулял по городу."
#If he's on Hanako's path, has he actually walked around town at that point?

"Должно быть, это один из тех городков, где остались только коренные жители, решительно отказывающиеся его покидать, а также те, кто хочет прожить остаток своих дней в одном из спокойных мест, которых остаётся всё меньше."

"Думаю, это заодно и объясняет, откуда взялась такая консервативность в обычаях школы «Ямаку»."

scene bg school_gardens at Fullpan(8.0)
with locationchange

"Я не против. Мне, в общем, нравится спокойствие «Ямаку» и окрестностей."

"А вот жара – совсем другое дело. Так долго просидев на солнцепёке, я теперь могу думать только обо всё усиливающемся зное."

"Мне лучше двигать отсюда, если я—{w=.5}{nw}"

play sound sfx_warningbell

"Гхе!"

"Колокольный звон застаёт меня врасплох, пока я поднимаюсь со скамьи, – то же случается и с несколькими проходящими мимо людьми."

"Вслед за окончанием перезвона с треском пробуждается к жизни система вещания. О её возрасте можно судить по едва разборчивому объявлению директора, который объявляет об открытии и без того идущего полным ходом праздника."

"Довольно примечателен контраст между довольными улыбками стариков и, напротив, скучающими и болезненными гримасами людей помоложе. Что же до учеников, то им попросту наплевать."

"Тем не менее, когда обращение заканчивается, все дружно, пусть и без особого энтузиазма, хлопают и возвращаются к своим делам."

"Сунув руки в карманы, чтобы смотреться как можно более расслабленным, я мимоходом оглядываюсь по сторонам."

"…Особо далеко не посмотришь: кругом люди."

"Я решаю положиться на проверенное правило: идти туда, куда идут все. Прямо сейчас народ направляется в сторону школьного двора и его окрестностей."

"Выбросив тарелку в бак для мусора, я иду к главному зданию."

scene bg school_courtyard
show crowd
with locationchange

"Я удивляюсь, увидев, сколько здесь расставлено киосков. Должно быть, немало классов скооперировалось, чтобы выставить их сразу по несколько штук."

"Решая, какой посетить первым, я замечаю знакомый плакат с синей узорчатой окантовкой и красным текстом."

"Вполне можно начать обход с киоска Лилли. Мне любопытно узнать, как у неё идут дела после всех потраченных на его устройство усилий."

$ renpy.music.set_volume(0.6,2.0, "ambient")
stop music fadeout 2.0

scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange

"Подойдя ближе, я начинаю понимать, почему её классу так долго пришлось возиться, чтобы всё обустроить."

"Он как минимум вдвое шире большинства других киосков, и повсюду вокруг него расставлено кухонное оборудование, так что он скорее ближе к ресторану на открытом воздухе, чем к фестивальному проекту."

"Ученик впереди меня берёт миску лапши и отходит, а я приближаюсь к прилавку."

"Девушка за ним кажется довольно сердитой и велит мне подождать, а затем исчезает под прилавком."

"Улучив момент, я быстренько оглядываюсь по сторонам."

"Пар поднимается как будто отовсюду: из медленно выкипающих кастрюль, из небольших котелков. Наиболее плохо видящие ученики под присмотром, вероятно, классного руководителя, распаковывают продукты."

"Вскоре я замечаю Лилли, которая разговаривает с учительницей, ловко пересчитывая пальцами коробки и пакеты."

"Судя по её выражению и тому, что она, равно как и учитель, находится в состоянии лёгкого замешательства, очевидно у них некие проблемы со снабжением."

"Из-под прилавка, закрывая мне обзор, возникает девушка и тут же оборачивается назад с вопросом, где запасная коробка со сдачей."

"Лилли на миг замирает, затем они с девушкой меняются местами за прилавком, а учительница быстро куда-то уходит."

show bg school_stalls2 at left
show lilly basic_smileclosed
with charaenter

li "Простите, у нас небольшие проблемы. Что вы хотели?"

"Мне требуется несколько секунд, чтобы вспомнить, зачем я здесь. Я поспешно перевожу взгляд на выставленное на прилавке меню."

hi "Хм, ну, я думаю, немного… мисо-супа?"

show lilly basic_surprised
with charachange

li "А, это ты, Хисао?"

play music music_normal fadein 0.3

hi "Ага. Похоже, вы неслабо заняты."

show lilly basic_weaksmile
with charachange

"Сбросив личину официантки, она всем своим видом выражает полнейшее согласие."

li "Где-то в цепочке доставки наш заказ оказался перепутан. Мы сейчас стараемся всё поправить, но похоже, что у нас есть лишь половина необходимого."

hi "Порции поменьше не решат вашу проблему?"

show lilly basic_sad
with charachange

li "Видимо, нам так и придётся поступить, хотя я предпочла бы этого избежать. В том, что добрая половина нашего класса куда-то запропастилась, хорошего тоже мало."

"Я заглядываю ей за спину, чтобы оценить, сколько людей работает в киоске."

"Их максимум восемь."

hi "Могу поспорить, учитель ушла именно поэтому?"

show lilly basic_weaksmile
with charachange

li "Да, верно. Она рассчитывает пойти и пригнать на помощь ещё несколько наших одноклассников."

"Заслышав позади себя звуки шагов, я украдкой бросаю взгляд назад, обнаруживая позади себя пожилую пару, занимающую место в очереди. Полагаю, мне стоит перестать мешкать и прекратить болтовню."

hi "Вот деньги за суп."

show lilly basic_smile
with charachange

li "Суп… А, да, минуточку."

"Лилли поворачивается и просит чашу мисо-супа, а я тем временем отдаю ей деньги."

show lilly basic_reminisce
with charachange

"Вложив монеты в её ладонь, я непроизвольно замечаю, как сноровисто она пересчитывает их своими длинными бледными пальчиками. Обрадовавшись тому, что я дал ей точную сумму без сдачи, она кладёт её в маленький металлический лоток."

show lilly basic_smileclosed
with charachange

"Спустя всего пару минут суп оказывается готов и бережно вложен в её руки, после чего она разворачивается и без промедления передаёт его мне."

hi "Спасибо. Я зайду снова и верну плошку."

show lilly basic_smile
with charachange

li "Спасибо тебе, Хисао. О, и ещё кое-что. Ты не видел Ханако?"

hi "Ханако… Нет, сегодня не видел. А что?"

show lilly basic_sad
with charachange

"Она вздыхает со смиренным разочарованием."

li "Да ничего. Мне просто было любопытно, пойдёт ли она на фестиваль."

show lilly basic_weaksmile
with charachange

li "Значит, ты потом зайдёшь, когда закончишь?"

hi "Конечно. И я посмотрю, не попадётся ли мне Ханако."

li "Спасибо, Хисао."

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"Я отхожу от киоска и присаживаюсь, бережно держа обеими руками исходящую паром деревянную плошку."

"По сравнению с такояки, которые я брал до этого, совсем неплохо. Холоднее, чем должен быть суп, но запах обалденный."

"Пока я ем, не могу избавиться от смутного чувства вины за то, что не принимаю такого активного участия в обустройстве фестиваля, как остальные ученики."

"Ничего не поделаешь, ведь меня занесло в эту школу всего лишь неделю назад, но всё равно мне как-то совестно."

"К тому же некоторые ученики явно проводят время на фестивале не настолько весело, как посетители."

"Так или иначе, я доедаю и отправляюсь к киоску, чтобы вернуть плошку."

"Приняв во внимание, что очереди почти нет, я возвращаюсь не спеша."

stop music fadeout 2.0

stop ambient fadeout 2.0

scene bg school_stalls2
with locationchange

"Видимо, миссия учителя завершилась успешно: я вижу более чем дюжину прилежно работающих учеников и большая часть распаковки уже выполнена."

"Несмотря на то что большинство спокойно делают свою работу, Лилли, кажется, чем-то расстроена."

# This is where K1 and L1 would split



label ru_A41a:
#Lilly Path Festival scene.

"…Точно. Я знаю, что мне делать. Пусть это лишь один человек, но я сделаю фестиваль более приятным для неё."

"Я кладу чашу на прилавок и зову Лилли."

show lilly basic_smile
with charaenter

li "А, Хисао. Возвращаешь её, да?"

hi "Да, вот."

hide lilly
with charaexit

"Я сую плошку ей в руки, и она передаёт её тем, кто, видимо, отвечает за мойку посуды. Прежде я их не видел, так что это, вероятно, наказанные за опоздание."

hi "Хм, Лилли?"

show lilly basic_smileclosed
with charaenter

"Снова услышав мой голос, она поднимает голову и возвращается к прилавку, осознав, что я ещё тут."

hi "Хочешь, пойдём получше посмотрим на фестиваль?"

play music music_dreamy fadein 0.3

show lilly basic_pout
with charachange

"Она неодобрительно надувает щёки. Выглядит довольно мило, как полная противоположность её обычной сдержанной натуре."

"Требуется несколько секунд, прежде чем до меня доходит, в чём дело. Опаньки."

hi "Ой… я имел в виду, не…"

show lilly basic_giggle
with charachange

"Лилли хихикает, показывая, что это был лишь розыгрыш."

li "Ты всё ещё не привык к школе, да?"

"Она меня подловила."

show lilly basic_reminisce
with charachange

li "Но всё же… Мне, пожалуй, надо остаться за прилавком. Нам только сейчас удалось наконец всё распаковать."

"Думаю, её нежелание не должно меня слишком удивлять, учитывая, сколько труда она в это вложила."

hi "Но сейчас-то всё уже в порядке. Да и к тому же к тебе пришла подмога."

show lilly basic_surprised
with charachange

"Парень, занятый приготовлением лапши соба, ухмыляясь, поворачивается к нам."

"Ученик" "Давай, Лиль, ты заслужила передышку. Мы пока удержим форт."

show lilly basic_displeased
with charachange

li "Раз ты так говоришь, то я думаю, что можно…"

show lilly basic_reminisce
with charachange

li "Но если будет нужна какая-либо помощь…"

"Ученик" "То мы тебя позовём. Иди, у нас всё схвачено."

hide lilly
with charaexit

"Он машет на Лилли своей лопаточкой, и она наконец прекращает сопротивляться. Нащупывая путь вокруг прилавка, она подбирает по дороге свою трость."

"Пожалуй, первым делом нам нужно поискать Ханако. Лилли, видно, волнуется за неё, да и я сомневаюсь, что в её характере в одиночку гулять среди толпы."

hi "Так, я думаю, мы должны поискать Ханако. Откуда начнём?"

show lilly cane_reminisce
with charaenter

li "Хм…"

"Мы оба на миг замолкаем, раздумывая."

hi "Может, в её комнате в общежитии?"

li "Вряд ли. У неё там мало вещей, так что ей нечего там делать."

show lilly cane_satisfied
with charachange

li "…А! Библиотека?"

"Не самое плохое место для поисков заядлой читательницы, я полагаю."

hi "Значит, библиотека. Проверим сначала там."

scene bg school_lobby
with locationskip

stop music fadeout 2.0

"За исключением приглушённых звуков толпы, просачивающихся снаружи, внутри школа кажется почти заброшенной."
#Contrasts with at least one of the other endings, but at this stage, I don't know if it's even worth it to bother. Alt-reality handwave. -SC

"Видимо, чтобы обеспечить всех достаточным простором, все мероприятия были устроены снаружи, на школьных угодьях. Они действительно очень велики по меркам любой другой школы."

show lilly cane_smileclosed
with charaenter

li "Здесь тихо и уютно, не правда ли?"

hi "Ага. Куда уютнее, чем тот шум и гам снаружи."

scene bg school_staircase2
with locationchange

"Мы не торопимся и медленно проходим по первому этажу школы, добираясь в итоге до лестницы на второй этаж."

scene bg school_hallway2
show lilly cane_smileclosed
with locationchange

"Я замечаю, что Лилли предчувствует каждую дверь и каждое препятствие, не шевеля тростью, но скользя рукой вдоль перил коридора."

hi "Ты в самом деле знаешь школу наизусть, да?"

show lilly cane_smile
with charaenter

"Она улыбается и сразу кивает."

li "Я здесь уже несколько лет, поэтому знаю, где что находится."

show lilly cane_sad
with charachange

li "Хотя общежития иногда сбивают меня с толку. Я не так часто там бываю, и планировка у них не такая продуманная, как в главном здании."

li "Если я правильно помню, они раньше были бесхозным строениями, прежде чем их подновили и открыли в них общежития."

"Это объясняет, почему мужские и женские корпуса выглядят по-разному и почему комнаты в них довольно необычной для своего назначения планировки."

"Я предполагал, что она жила в общежитии с тех пор, как начала ходить в школу, но сейчас припоминаю сказанное ей вчера."

"Она, должно быть, переехала не сразу после перевода сюда. Так что ничего удивительного в том, что местность ей не так уж хорошо знакома."

hi "Да, точно, ты уже упоминала об этом."

hi "Я полагал, что большинство учеников жили в общежитиях с самого момента их зачисления. Или что таких по крайней мере немало."

show lilly cane_reminisce
with charachange

"На лице Лилли появляется выражение, которое я не могу прочитать, – своим вопросом я, видимо, задел деликатную тему."

li "Хм… Как бы лучше выразиться…"

show lilly cane_weaksmile
with charachange

li "У всех… свои причины."

"Что-то мне подсказывает, что одной из таких, «имеющих свои причины», является Ханако, вот Лилли и осторожничает с ответом. Моё собственное положение служит ещё одним примером."

"Полагаю, это выбор, который каждый делает для себя… или же, как в моём случае, подобный выбор делают за них."

hi "Думаю, тут ничего не поделаешь. По крайней мере, «Ямаку» кажется вполне милым местом."

show lilly cane_smile
with charachange

li "Рада слышать это от тебя. Я боялась, ты возненавидишь «Ямаку»."

hi "А что насчёт тебя?"

show lilly cane_surprised
with charachange

"Мой вопрос, заданный в ответ на утверждение Лилли, застаёт её врасплох."

li "Я здесь уже давно, так что…"

hi "Я не об этом. Ты кажешься довольно расстроенной из-за Акиры."

show lilly cane_smileclosed
with charachange

li "Хм~"

hi "Это ещё что за выражение?"

show lilly cane_smile
with charachange

li "Акира занята. Извини, Хисао."

"Лилли не видит, как быстро я подношу ладонь к лицу от этого её обвинения."

hi "Эй, я беспокоился за тебя. Так не отвечают на заботу."

show lilly cane_cheerful
with charachange

"Она награждает меня усмешкой, в то время как мы проходим коридор и входим в библиотеку."

scene ev hana_library_read_std
with locationskip

play music music_another fadein 0.3

"Сделав это, мы без труда обнаруживаем Ханако, ведь больше в комнате никого нет."

scene bg school_library
with locationchange

"А раз никого из сотрудников поблизости тоже не наблюдается, то и нужды соблюдать обычные библиотечные правила нет."

hi "Эй, Ханако."

show lilly cane_surprised
with charaenter

li "Ханако тут?"

"Услышав наши голоса, Ханако поднимает голову из-за книги, вероятно той же самой, что она читала в пятницу."

show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter

ha "Хисао? Лилли?"

hi "Да вот, решили заглянуть. Лилли только что удалось сбежать из лапшичного киоска… с небольшой помощью."

show lilly cane_pout at twoleft
with charachange

li "Это был не совсем побег…"

show hanako emb_downsmile at tworight
show lilly cane_surprised at twoleft
with charachange

"Ханако хихикает, на мгновение удивляя нас обоих."

show hanako basic_bashful at tworight
with charachange

ha "Я как раз беспокоилась о том, что… Лилли сейчас может не веселиться на фестивале."

hi "Ну, теперь мы можем наслаждаться им вместе, да?"

show lilly cane_smileclosed at twoleft
with charachange

"Они обе радостно кивают, и мы выходим из библиотеки навстречу веселью."

scene bg school_stalls1_ni
with shorttimeskip

stop music fadeout 2.0

$ renpy.music.set_volume(0.2,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3

"Я передаю немного мелочи девушке за кассой и беру два пластиковых стаканчика с чаем. Я кланяюсь чуть ниже, чем следует, так как девушка явно глуха."

"Если подумать, мне, наверное, стоило попросить этих двоих помочь мне, а не оставлять их в сквере, а самому идти за напитками."

"Жонглировать двумя стаканами с горячим чаем (для них) и банкой кофе (из автомата, для меня) не очень-то просто."

"С помощью осторожных манёвров мне удаётся сохранить всё в стабильном и вертикальном положении к тому моменту, как я подхожу к скамейке, на которой сидят и болтают Лилли и Ханако."

show bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange

"Это довольно неплохое место. Освещённое лишь лунным светом, оно находится на некотором удалении от самой гущи событий."
#is there actually moonlight?

"По сравнению с тем, каким знойным оно было днём, сейчас тут довольно прохладно."

"Не то чтобы это что-то значило. Большинство посетителей ушли поближе к месту запуска фейерверков или поднялись на холм, чтобы получше увидеть запланированное представление."

show lilly basic_smile_ni at twoleft
with charachange

li "С возвращением, Хисао."

show hanako basic_normal_ni at tworight
with charachange

"У неё хороший слух. Я довольно далеко, и даже Ханако меня ещё не видит."

hi "Вот, держите. Извините, что растворимый, это всё, что у них осталось."
# "Instant" tea? Is this a holdover from the old Act 1?

"Ханако осторожно берёт стакан из моей правой руки, и я аккуратно вкладываю второй в протянутую руку Лилли."

show hanako basic_smile_ni at tworight
show lilly basic_smileclosed_ni at twoleft
with charachange

li "Понравился тебе фестиваль, Хисао?"

hi "Да, было довольно весело."

"Отвечаю я честно. Большая часть еды была не ахти, но зато под конец было и правда весело, особенно с Ханако и Лилли."

"На самом деле я думаю, эти двое повеселились даже больше моего. Из-за нашего с Лилли присутствия замкнутость Ханако, обычно проявляющаяся в окружении других людей, уменьшилась настолько, что она начала получать удовольствие от происходящего."

stop ambient fadeout 1.0

$ renpy.music.set_volume(1.0,0.0, "ambient")

play ambient sfx_fireworks
play music music_twinkle fadein 0.3

scene bg misc_sky_ni
show fireworks
with dissolve

"Пока мы сидим и пьём, раздаётся первый залп фейерверка, взрывающегося ярким дождём синих искр на фоне ночного неба, провозглашая начало конца фестиваля."

"Его приветствуют весёлые крики из групп отдыхающих, разбросанных тут и там по школьной территории."

"Мы с Ханако несколько минут наблюдаем за фейерверками в небе, а Лилли спокойно слушает их с закрытыми глазами."

"Красные, зелёные, жёлтые, в форме звёзд, кругов и узоров всех форм и расцветок, один за другим они наполняют воздух, танцуя по небу."

"Нигде рядом с моим прежним жильём не устраивалось такое щедрое представление. Фестивали, подобные этому, в больших городах канули в лету."

"Наблюдать подобное зрелище вместе с ними… Наверное, это лучшее, что со мной случалось за последнее время."

scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange

li "Ну, вот и всё. Фестиваль наконец закончился."

hi "Ага."

"Она грустно вздыхает."

show lilly basic_concerned_ni at twoleft
with charachange

li "Как бы я ни жаловалась на то, что на нас свалилось много хлопот, всё-таки жаль, что нам предстоит выпуститься до следующего фестиваля «Ямаку»."

show lilly basic_concerned_close_ni at twoleft
with characlose

"Я делаю несколько шагов вперёд, подходя к Лилли, и мягко кладу руку ей на плечо."

hi "Не волнуйся. Мы в этом году ещё успеем сходить на Танабату, верно?"

show lilly basic_smile_close_ni at twoleft
with charachange

li "Ты прав. Было бы здорово сходить на этот праздник вместе."

"Проходят минуты молчания, сопровождаемые лишь взрывами фейерверков."

"Глядя на них двоих, я вспоминаю совет, который Лилли дала мне, когда мы вместе ходили в город."

"«Тебе стоит ценить возможность завести новых друзей», а?"

hi "Эй, Лилли?"

show lilly basic_smileclosed_close_ni at twoleft
with charachange

"Она слегка поворачивает голову, показывая, что слушает. Ханако тем временем по-прежнему не отрывает взгляда от сочных цветов фейерверка над головой."

hi "Ты не против, если я и впредь буду пить с вами чай?"

"Улыбка на её лице служит мне наилучшим ответом."

show lilly behind_cheerful_close_ni at twoleft
with charachange

li "Буду рада, Хисао."

stop ambient fadeout 1.0
# ^ I dunno where the fireworks are going to be ending, so move around whereever, I guess. -yujovi

window hide

stop music fadeout 2.0



###################
#Hanako Path
label ru_A42:

#This is the "real" version of H1, edited to fit with the split marked in L1

# Hanako/Lilly festival
play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_stalls2
with None

show lilly basic_reminisce
with charaenter

"Лилли, похоже, не в лучшем настроении, и я не могу её винить."
# ..."impressed" doesn't seem like the right word.

"Помимо проблем с киоском ей, похоже, приходится волноваться за Ханако."

"С первым я не могу ей по-настоящему помочь, так что, думаю, единственный для меня способ оказать ей помощь – снять с неё заботу о нашем общем застенчивом друге."

"Поставив плошку на прилавок, я зову Лилли."

hi "Эй, Лилли, не волнуйся за Ханако. Я обязательно прогуляюсь с ней, когда отыщу, договорились?"

show lilly basic_weaksmile
with charachange

"Я вижу, как по лицу Лилли явственно расплывается облегчение."

li "Спасибо, Хисао. И, если заметишь кого-нибудь из моего класса, будь добр, скажи им зайти сюда."

hi "Обязательно. Желаю приятно провести время. И не забудь сделать перерыв, хорошо?"

show lilly basic_smile
with charachange

li "Если получится. Увидимся позже, Хисао."

scene bg school_courtyard
show crowd
with locationchange

"Я оставляю Лилли за прилавком и направляюсь на поиски Ханако."

"Я отчасти виню себя за то, что оставил её одну, но, пусть на её долю и выпала немалая нагрузка, мне всё же кажется, что она вполне довольна."

stop ambient fadeout 0.2
play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationskip

"Проходы забиты колышущейся толпой, слоняющейся туда-сюда по праздничным угодьям."

"Если я хоть что-то знаю о Ханако, она к такому даже не приблизится."

"И, учитывая, что некоторые ученики показывают друзьям и семье свои комнаты в общежитии, сомневаюсь, что она найдётся и там."

"Положившись на слепую интуицию, я неохотно погружаюсь в людскую массу."

"К счастью, толпа не такая шумная, как обычно бывает на праздниках, – я предполагаю, что это из предупредительности к физическим недостаткам учеников."

stop ambient fadeout 5.0

"Я пробиваюсь сквозь скопления людей, и вскоре они редеют, а позже и вовсе исчезают."

hide crowd
with Dissolve(2.0)

"Неудивительно, учитывая, что я стою перед библиотекой."

"Даже самые дотошные из учеников не станут никому показывать эту часть школы."

play music music_another fadein 0.3
scene bg school_library
with locationchange

"Когда я захожу внутрь, шум праздника тает позади, превращаясь в глухое гудение где-то на заднем плане, и вскоре я оказываюсь в отведённой для чтения дальней части помещения."

"Позади одного из огороженных столов я замечаю чью-то макушку с тёмными прямыми волосами, привлекающую моё внимание."

hi "Привет, Ханако. У меня было чувство, что я найду тебя здесь…"

show hanako def_shock at Move((0.5,1.0,0.5,0.9),(0.5,1.0,0.5,1.0),0.5,time_warp=_ease_in_time_warp)
with charaenter

"Она вздрагивает от изумления, прежде чем медленно показаться над перегородкой."

ha "Х-Хисао?"

hi "Ага. Лилли изрядно занята, так что послала меня найти тебя."

show hanako basic_normal
with charachange

ha "О-о. Хочешь присесть?"

hi "Вообще-то я слегка голоден. Не хочешь пойти перехватить чего-нибудь с лотков?"

show hanako defarms_worry
with charachange

ha "Ум… Я… Я взяла с собой еду, поэтому…"

"Что и неудивительно, но всё-таки попытаться стоило. Ожидать, что она выйдет сегодня наружу, – слишком смелое предположение."

hi "А как насчёт поесть в чайной комнате? Я прошёл мимо неё по пути сюда, и там никого не было."

hi "Там мы сможем заварить себе чай, и вообще так будет удобней. Что скажешь?"

show hanako cover_distant
with charachange

ha "К-конечно. Пойдём."

show hanako basic_distant
with charachange

"Ханако закрывает книгу и отработанным движением откладывает её в сторону."

hi "Готова к походу?"

show hanako basic_normal
with charachange

ha "А… ага."

stop music fadeout 2.0

scene bg school_hallway3
with locationchange

"Мы выходим из библиотеки в направлении чайной комнаты."

"Как и ожидалось, вокруг ни души."

"Если бы не доносящийся из-за стен гомон толпы, то и не скажешь, что снаружи сейчас большое празднество."

show hanako emb_downtimid at tworight
with charaenter

"Ханако несёт свой портфель обеими руками и глядит перед собой в пол."

show hanako emb_downsmile at tworight
with charaenter

show hanako emb_downtimid at tworight
with charaenter

"Время от времени она, кажется, делает короткие шажки вместо обычных."

"В первый раз я не обращаю внимания, но вскоре замечаю, что она делает так постоянно."

hi "С тобой всё в порядке?"

play music music_dreamy fadein 0.3

show hanako defarms_worry at tworight
with charachange

"Она резко замирает на полушаге."

ha "Ч-что?"

hi "Не знаю… Кажется, будто ты спотыкаешься или типа того…"

show hanako emb_blushing at tworight
with charachange

"Розовый румянец окрашивает её щёки, и взгляд её снова утыкается в пол."

show hanako emb_downtimid at tworight
with charachange

ha "Нет… всё в порядке."

hi "Знаешь, когда ты вот так говоришь «всё в порядке», то прямо подталкиваешь задать тебе ещё вопрос."

"Секунду мне кажется, что она не ответит."

"Приготовившись оставить эту тему, я собираюсь снова отправиться дальше, как…"

show hanako emb_emb at tworight
with charachange

ha "Это… игра."

hi "Игра?"

show hanako emb_downsmile at tworight
with charachange

ha "Ты… видел, какие тут полы?"

"Странный вопрос. Полы выглядят точно как любые другие полы, расчерченные ячейками из квадратов линолеума."

"Ничего примечательного."

hi "Ну, да. А что с ними?"

show hanako emb_downtimid at tworight
with charachange

ha "Иногда… когда никого нет рядом… я наступаю только на тёмные…"

"Голос Ханако становится всё тише и тише по ходу объяснения, до такой степени, что я едва могу её расслышать в звенящей тишине пустого коридора."

hi "Тёмные?"

"Шаркнув ногой, Ханако указывает носком своей туфли на кусочек, который выглядит чуть-чуть темнее прочих."

show hanako emb_downsmile at tworight
with charachange

ha "В-вот такие."

hi "А, понятно, значит вот эти не годятся?"

"Я показываю на соседний квадратик."

show hanako emb_emb at tworight
with charachange

ha "А-ага. Примерно… примерно так."

hi "Угу, ясно. Ты часто так играешь?"

show hanako emb_downsad at tworight
with charachange

"Ханако качает головой."

hi "Только когда в коридорах пусто?"

show hanako emb_emb at tworight
with charachange

"Она кивает."

hi "Что ж, не будем задерживаться, а то скоро я по-настоящему проголодаюсь."

show hanako emb_smile at tworight
with charachange

"Она снова кивает, на сей раз с большим воодушевлением."

hi "Ну, тогда пойдём."

hide hanako
with charaexit

"Мы продолжаем путь по коридору, но на этот раз я замечаю, что Ханако чуть реже глядит на пол."

"Интересно, насколько человек должен быть одинок, чтобы додуматься до игры вроде этой?"

"Не успев понять, что я делаю, я замечаю, что стараюсь выверять каждый шаг, чтобы наступать только на правильные квадратики."

scene bg school_miyagi
with locationchange

"В чайной комнате шум фестиваля слышен чуть сильнее, но ветерок, дующий из открытого окошка, того стоит."

"Я не раздумывая подхожу к подоконнику и делаю глубокий вдох. Иногда я забываю, насколько легко здесь дышится по сравнению с моим родным городом."

show hanako basic_bashful
with charaenter

ha "Ты… будешь чаю?"

hi "Было бы здорово, спасибо."

hide hanako
with charaexit

"Мне приходит в голову, что это первый раз, когда я остаюсь наедине с Ханако и при этом она не пытается куда-нибудь сбежать."

"Отвернувшись от окошка, я гляжу, как она заваривает чай в простом чайничке и выкладывает на тарелку несколько бутербродов."

"Я не раз видел, как она это делает, но сейчас она кажется чуть другой."
#A number of times? -SC

"Как будто она…{w} спокойна."

"Вскоре она опускает на стол маленький поднос и наливает две чашки чая."

"Аромат свежезаваренного чая смешивается с ветерком, и на миг мне представляется, будто я нахожусь с миром один на один."

hi "Пожалуй, теперь я понимаю, почему тебе нравится эта комната."

show hanako defarms_worry
with charaenter

ha "Ум… Я не знаю, о чём ты."

hi "Ну, там, подальше, немало народу, но здесь будто совершенно другой мир."

hi "Можно вообразить, что тут нет никого на километры вокруг."

show hanako emb_downtimid
with charachange

ha "И-и верно."

ha "Словно мир позабыл об этой комнате."

show hanako emb_emb
with charachange

ha "И п-поэтому можно забыть о том, что снаружи."

"В некоторых случаях это привлекательно."

"Насколько я могу судить, издевательства в своей классической форме в этой школе не практикуются."

"Но при всём при том я не видел ни единого человека, разговаривающего с Ханако, кроме Лилли."

"Если тебя игнорирует мир, то место, где ты можешь забыть о его существовании, будет обладать особой притягательностью."

hi "Верно, в этом её плюс. Эта комната словно дарит нам своего рода свободу."

show hanako emb_smile
with charachange

ha "Д-да."

show hanako basic_bashful
with charachange

ha "Скажи… А ты в шахматы играешь?"

hi "Шахматы? Думаю, немножко умею."

hi "Я так понимаю, ты раньше играла?"

show hanako basic_distant
with charachange

ha "Чуть-чуть…"

hide hanako
with charaexit

"Ханако, не проронив более ни слова, подходит к одному из буфетов и достаёт из него маленький шахматный набор."

ha "Ты… ты хочешь…"

hi "Конечно, почему бы нет?"

"Я прерываю её на полуслове, но она, очевидно, не в обиде."

scene bg school_miyagi
show hanako basic_normal_close
with shorttimeskip

"Мы расставляем фигуры и вскорости уже посылаем пешек навстречу их неизбежной судьбе."

"Я не тороплюсь и внимательно изучаю каждый ход и его последствия, и ностальгия по игре отходит на задний план."

"Поначалу игра представляет собой длительную войну на истощение, но тут я замечаю брешь в её построениях и прорываю линию обороны."

show hanako basic_worry_close
with charachange

"Спустя несколько ходов её король попадает в окружение моих фигур."

hi "Шах и мат."

hi "А ты неплохо играешь, да?"

"Честная оценка. Её техника довольно хороша, но несколько раз мне удалось использовать её слабость в предвидении."

"Я поднимаю фигурку к глазам и внимательно её рассматриваю. Она кажется относительно новой, но уже потрёпанной."

show hanako basic_smile_close
with charachange

ha "Я… я думаю, нет."

hi "А Лилли играет?"

show hanako def_worry_close
with charachange

"Пауза перед ответом Ханако заставляет меня задуматься над своим вопросом."

ha "Н-немножко…"

ha "Э-это первый раз, когда я играла с кем-то… кроме неё или…"

show hanako emb_downsad_close
with charachange

"Или?.."

"Она резко обрывает себя, а мой вопрос остаётся невысказанным. Видимо, она имела в виду человека, которого знала ещё до поступления в «Ямаку»."

hi "Что ж, я польщён, что мне довелось с тобой сыграть."

show hanako emb_smile_close
with charachange

ha "Ум-м… Мы можем сыграть ещё?"

"Она спрашивает так неуверенно, будто просит меня отрезать мои же собственные руки. У неё разыгрался азарт?"

hi "Конечно. Хотя на сей раз не жди от меня пощады…"

"Хотя не то чтобы я поддавался раньше. Боевой настрой ей, похоже, нравится."

show hanako emb_downsmile_close
with charachange

ha "И… и от меня тоже…"

window hide

stop music fadeout 2.0

#scene willl flow into K2 with Lilly finishing her time at the café and collecting the
#two to go to the Shanghai



#******************

label ru_A43:
#Kenji rou-- er, Deep-Six

scene bg school_dormhallway at bgright
show kenji happy
with None

stop music fadeout 1.0

play music music_tranquil fadein 0.8

"Чем мне заняться? У меня нет никаких планов. Как ни крути, это довольно глупо."

"Может, мне стоило пригласить девушку? Я в конечном счёте вряд ли смогу сделать что-то такое. Это ведь моя первая неделя."

"Неделя, которую я потратил впустую, неуклюже ведя себя со всеми, спотыкаясь на каждом шагу, пытаясь понять, как здесь всё устроено."

"Если подумать, чего я добился?"

"Кого я мог бы пригласить?"

"Чёрт, как ни крути, а выходит, что %(name_kenji)s – мой единственный шанс на свидание сегодня."

"Это самое грустное, что случалось со мной с тех пор, как я схлопотал инфаркт из-за девушки, признавшейся мне в любви."

"Ничего не поделаешь."

hi "Я не знаю, правда. Пожалуй, мне нечего предложить, но крепость – это, кажется, перебор."

hi "Ты уверен, что не хочешь пойти на улицу? Посетители обязательно заявятся сегодня в общежитие."

show kenji tsun
with charachange

"Эти слова его словно громом поражают."

ke "Чёрт, а ты прав. Это место сегодня небезопасно."

ke "Надо найти где спрятаться."

"На миг он задумывается."

show kenji neutral
with charachange

ke "Крыша."

hi "Что «крыша»?"

show kenji happy
with charachange

ke "Мы пойдём и схоронимся там до позднего вечера."

ke "Идеальное место, туда никто никогда не поднимается."

show kenji neutral
with charachange

ke "Жди меня там через час. Мне надо приготовиться."

show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None

hide kenji
with charaexit

play sound sfx_impact2
with vpunch

"Он захлопывает дверь и закрывает её на замок."

"Блин, да что, чёрт побери, не так с этим парнем?"

"И, подумать только, я сейчас готов смириться с его безумствами. Меня это и правда угнетает."

"Эх, ну я и облажался…"

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_courtyard
show crowd
with locationskip

"Я делаю шаг наружу, и меня приветствует оглушительный шум толпы."

"Вся школа кипит от бурной деятельности."

"Повсюду видны киоски, между которыми роятся внушительных размеров толпы."

"Я не ожидал, что фестиваль привлечёт столько гостей."

"Должен признать, что люди, отвечающие за украшение территории, знатно постарались, и это заметно."

stop music fadeout 1.0

"Народу, похоже, весело, и атмосфера яркая, красочная и счастливая."

play music music_tragic

"То есть была бы, если бы не моё паршивое настроение."

"Сейчас оно бесит меня больше, чем что-нибудь другое."

"Ну, деваться некуда. Я решаю придерживаться изначального плана и поесть, а потом придётся взглянуть, что затеял %(name_kenji)s на крыше."

"…"

scene bg school_stalls2 at Fullpan(8.0)
with locationchange

"Чтобы убить время, я неспешно прохаживаюсь взад-вперёд, поглядывая на киоски, но настроения играть в эти игры у меня нет никакого."

"Кричащие цвета режут глаз, и с каждой минутой мне становится всё хуже."

"Я даже не могу решить, что бы мне съесть, и большой выбор в сочетании с оживлёнными толпами празднующего народа задачу тоже не упрощает."

scene bg school_stalls1 at bgright
with locationchange

"Я просто направляюсь к ближайшему лотку, предлагающему что-то хотя бы наполовину съедобное, и встаю в очередь."

"Оказывается, это лапша."

"Также выясняется, что она не очень-то хорошо приготовлена."

"Ну, по крайней мере, питательная. А ничего другого мне сейчас и не требуется."

scene bg misc_sky at Fullpan(25.0)
with locationchange

"Помешивая свою сомнительного качества лапшу, я вяло задумываюсь, чем сейчас занимаются остальные."

"%(name_shizune)s и Миша определённо где-то что-то организовывают."

"Мне лучше держаться от них подальше. Думаю, они так быстро не простят, что я бросил их наедине со всей этой работой."

"Эми, мне представляется, шныряет туда-сюда по киоскам, будучи удручающе жизнерадостной."

"Нет ни малейшего шанса её найти, равно как и избежать случайной встречи, так что пофиг."

"Лилли, вероятно, помогает своему классу с праздничным мероприятием и определённо слишком занята, чтобы составить кому-то компанию."

"Ханако не станет ни с кем общаться. Она либо держится ото всех подальше, либо помогает Лилли."

"Рин, должно быть, на посту у своей фрески, пусть и вряд ли чем-нибудь может помочь интересующимся, если таковые найдутся."

"Пойти туда ради тишины и спокойствия кажется самым лучшим выбором из имеющихся, но я всё же не могу представить, каким образом заталкивание в мой мозг искусства сможет поднять мне настроение, так что воздержусь."

scene bg school_stalls1 at bgright
with locationchange

"Пока я размышляю, моя еда, вместе с голодом, куда-то исчезает."

"Видимо, я просто мысленно отгородился от вкуса еды, что, вообще-то, неплохо."

"Сытый, но не довольный, я разворачиваюсь и иду к главному школьному зданию. Час уже почти прошёл."

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_lobby
show crowd
with locationskip

"Толпа здесь даже плотнее, чем снаружи."

scene bg school_hallway3
show crowd
with locationchange

"В коридорах не протолкнуться, и я боюсь представить, что творится внутри классных комнат."

stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"Я поднимаюсь по лестнице, ведущей к моей цели."

"Крыше."

"К счастью, дверь наверх не заперта, но сейчас на ней висит написанная от руки табличка:"

$ written_note(u"{size=55}{b}ВХОД ВОСПРЕЩЁН{/b}{/size}")

"Ну, это не мне."

scene bg school_roof at bgright
with locationchange

"Шум праздника здесь практически не слышен, а крыша выглядит заброшенной, как и ожидалось."

"Рядом с местом, где повалено проволочное ограждение, лежит кипа одеял, странно выделяющаяся на общем фоне."

stop music fadeout 3.0

"Погодите."

play sound sfx_rustling

"Мне кажется, или куча шевелится?"

"Удивительно, учитывая полное безветрие."

"Я осторожно вытягиваю руку и тыкаю её."

show kenji rage_close at Alpha(0.0,1.0,0.2), Move((0.5,1.0,0.5,0.7),(0.5,1.0,0.5,1.0),0.2)
with vpunch

$ doublespeak(ke, hi, u"А-А-А-А-А-А-А-А-А!")

play music music_drama fadein 0.2

show kenji rage
with charadistant

"Испугавшись, я отпрыгиваю назад."

ke "Кто там?"

hi "Чёрт тебя побери, %(name_kenji)s. Это я."

show kenji tsun
with charachange

ke "Ох блин, чувак, ты меня напугал."

hi "Так что мы здесь делаем?"

show kenji neutral
with charachange

ke "Мы устроим пикник."

hi "Что?"

show kenji happy
with charachange

ke "То. У меня есть одеяла, крендельки и виски. Идеальный набор, чувак."

hi "Виски?"

hi "Ты разве не слишком молод для выпивки?"

show kenji tsun
with charachange

ke "Мне, знаешь ли, двадцать."

hi "…Вовсе нет."

show kenji neutral
with charachange

ke "И мне, и тебе."

hi "Чего? Что за бред?"

show kenji tsun
with charachange

ke "Эй, ТЫ-то, по крайней мере, кое-что с того получил, а мне досталась всего-навсего бутылка виски…"

"Он несёт какую-то несуразицу, но я решаю ему подыграть."

hi "Так откуда у тебя бутылка виски?"

show kenji happy
with charachange

ke "Моя мама не смогла приехать на фестиваль, поэтому взамен прислала мне дорогого односолодового вискаря."

hi "Звучит правдоподобно."

ke "Хочешь глотнуть?"

hi "…"

"А что мне, собственно, терять? Этот день хуже стать уже не может."

hi "…Почему бы и нет."

hide kenji
with charaexit

show bg school_roof
with charamove_accel

show kenji happy_close at offscreenleft
with None

show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel

"Мы располагаемся на куче одеял, которые %(name_kenji)s сюда притащил."

"Он достаёт почти полную бутылку виски и передаёт её мне."

hi "Ты даже не принёс стаканы?"

show kenji tsun_close at twoleft
with charachange

ke "Не, это ж не пикник какой-нибудь романтичной принцесски. Какого хрена, чувак?"

show kenji neutral_close at twoleft
with charachange

ke "Это настоящий мужской пикник."

ke "Никаких стаканов."

ke "Никаких салфеточек."

ke "Только виски. Выпивка настоящих мужчин."

hi "Как скажешь."

show kenji happy_close at twoleft
with charachange

ke "И крендельки."

"Я рассматриваю бутылку поближе."

"Односолодовый виски 12-летней выдержки, как он и сказал."

"Пожав плечами, я делаю глоток. Выпивка обжигает горло, словно кислота, но на вкус вполне неплохо."

"Я чувствую, что виски ударяет в голову, а его послевкусие, задержавшееся во рту, так и просит сделать ещё глоток."

stop music fadeout 3.0

show kenji neutral_close at twoleft
with charachange

ke "Мы должны обсудить здесь наших контрреволюционных и бахвалистых женщин, пока они нас не слышат."

show kenji tsun_close at twoleft
with charachange

ke "Чёрт, я забыл принести свои таблицы."

"Я решаю поиграть с собой в игру-напивашку. Каждый раз, как %(name_kenji)s вспоминает «заговор женщин», я делаю глоток."

$wdt_off(False)

scene black
with delayblinds

centered "Четыре или пять часов, а может, несколько дней спустя:\n{w}(я сбился со счёта)"

#...music for this scene would be good, too.

scene ev kenji_rooftop
with delayblinds

window show

ke "Не кисни, чувак! Расслабься нахрен! Не, ну правда!"

hi "Я расслаблен, мать твою!"

ke "Говорю, что вижу!"

scene ev kenji_rooftop_kenji
with flash

ke "Подумай об этом. Когда начали дорожать земля и дома? Когда женщины начали появляться в качестве рабочей силы, потому что это создало ядрёные двухдоходные семьи."

ke "Я, конечно, забыл свои таблицы, но, поверь мне на слово, женщины стоят за разложением всего общества."

show ev kenji_rooftop_large at Pan((288,376),(1024,260),1.0,time_warp=_ease_time_warp)

hi "Ну да. В это сложно поверить."

"Хоть я так и говорю, однако то, что говорит %(name_kenji)s, начинает потихоньку приобретать смысл."

"Всё начинает сходиться, но я не могу понять: то ли %(name_kenji)s объясняет лучше, когда пьяный, то ли я, выпив, мыслю яснее."

show ev kenji_rooftop_large at Pan((1024,260),(288,376),1.0,time_warp=_ease_time_warp)

ke "Нет, чувак, думай. Думай! Подумай о глубоких подоплёках!"

ke "Люди теперь могут сказать что-то типа: «А, ну раз в семье сейчас приносят деньги два человека против одного, то они точно могут позволить себе платить за собственность больше»."

show ev kenji_rooftop_large at Pan((288,376),(1024,260),1.0,time_warp=_ease_time_warp)

hi "Я понял, о чём ты. Но земля в Японии всегда была дорогой."

show ev kenji_rooftop_large at Pan((1024,260),(288,376),1.0,time_warp=_ease_time_warp)

ke "…И цена на землю идёт вверх в основном тогда, когда в стране начинается индустриализация. …Но нет! Это из-за женщин! Корреляция сама за себя говорит."

show ev kenji_rooftop_large at Pan((288,376),(1024,260),1.0,time_warp=_ease_time_warp)

hi "А мне-то казалось, что подобные рассуждения – логическая ошибка. Ну ладно, пофиг, может, ты и прав."

show ev kenji_rooftop_large at Pan((1024,260),(288,376),1.0,time_warp=_ease_time_warp)

ke "Я всегда прав. Да-а, могу поспорить, женщины придумали индустриализацию, чтобы прикрыть свои следы."

ke "Дьявольски умный план."

ke "Вот так, блин, все могут идти на хрен!"

scene bg school_roof_ni
show kenji rage_ni at Move((0.5,1.0,0.5,0.9),(0.5,1.0,0.5,1.0),0.5,time_warp=_ease_in_time_warp)
with locationchange

"Он встаёт, впечатляя меня, потому что я почти уверен, что не смог бы этого сделать, даже если бы и захотел. Его крик такой громкий, словно у %(name_kenji)s сорвало переключатель мощности. Я дёргаюсь, испытывая желание зажать уши."

ke "А-а-ах, как здорово было б оказаться сейчас там, внизу… Но нет. Видишь ли, такие мысли – это ловушка: тебе кажется, что ты что-то упускаешь, но в конце этого пути нет ничего, кроме отчаяния…"

show kenji tsun_ni
with charachange

play music music_sadness fadein 1.5

"%(name_kenji)s выхватывает у меня бутылку и запрокидывает голову, собираясь влить выпивку себе в рот, но в итоге лишь проливает её на себя."

show kenji rage_ni
with charachange

ke "Вот чёрт! Гляди, я сбил прицел! И, что самое поганое в выпивке, – он сбивается всё сильней, чем больше ты пьёшь."

show kenji tsun_ni
with charachange

ke "Сегодня день отчаяния."

"Его голос разом опускается до шёпота, но он начинает тараторить, слегка коверкая слова из-за выпитого."

"Толкая речь, он размахивает бутылкой, расплёскивая её содержимое там и сям."

ke "Да, знаешь, какое было самое ужасное событие в моей жизни?"

"Я смутно припоминаю, как он рассказывал мне о своём втором-самом-ужасном-событии-в-жизни, а именно – когда птичка нагадила ему на голову."

"Я не особо много жду от его ответа, но всё равно киваю, чтоб он продолжал."

show kenji neutral_ni
with charachange

ke "Не поверишь, но у меня когда-то была девушка, вроде бы в прошлом году."

ke "Эге, я сейчас сорвал тебе крышу, а? Понимаешь, я никому раньше этого не говорил."

"И правда, крышу у меня от этой мысли сносит серьёзно. Мне вдруг начинает хотеться выпить. Я отбираю у %(name_kenji)s бутылку и заливаю в себя столько виски, сколько могу."

show kenji tsun_ni
with charachange

ke "Я был тогда более невинен и думал, что она в своём уме, в отличие от большинства женщин. Но однажды мы… переспали."

ke "Вышло вполне себе здорово, но сразу после случилось такое, ты не поверишь, странное и пугающее одновременно."

show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove

"Он шарахается к забору, прислоняясь к нему и щуря глаза."

ke "Я почувствовал себя ужасно усталым и сонным! Это ненормально, чувак! Что за хрень?"

ke "В смысле, это же должен быть пиковый, адреналиновый момент жизни любого чела, но вся моя энергия словно сливалась в унитаз!"

ke "Тут было замешано что-то зловещее, я это чувствовал."

ke "И тогда я понял… Женщины опасны, они высасывают жизнь из всех мужчин средством, которое доступно практически им одним!"

ke "Омерзительно."

show kenji neutral_ni at tworight
with charachange

ke "Да, братан, с тобой куда приятнее…"

"%(name_kenji)s прав, сегодня и впрямь день отчаяния. Я опрокидываю ещё, чтобы избежать раздумий над только что сказанным им."

ke "Теперь я последний разумный человек в безумном мире… Когда другие это поймут, случится война, великая война между мужчинами и силами феминизма."

ke "Но подвох в том, что не все мужики будут сражаться на моей стороне… что хреново. Я могу выставить планку довольно низко, подойдёт любой мужик. Но только не те челы, которых воспитала мамочка или сестра, это точно."

show kenji tsun_ni at tworight
with charachange

ke "И никаких хентайных футанари."

hi "Эх… Это всё так на меня не похоже, как будто ничего такого не случалось, как будто… и вовсе не должно было случиться."

"Странно, выпивка должна была подействовать."

"Но мне всё равно горько находиться сейчас здесь."

"По правде говоря, я не ждал фестиваля с той же радостью и предвкушением, как остальные в школе, но тем не менее."

"Было бы здорово с кем-нибудь пойти на него. Глядя отсюда кажется, что все весело проводят время. Наверное, я многое упускаю."

"Просто так вышло, что мне оказалось не с кем пойти."

"Может, кто-то и был. Если вспомнить, то было столько возможностей, но я их все прохлопал."

ke "Чёрт, это и есть истинное отчаяние… Самое худшее, что я иногда чувствую, что мне не предоставлено никакого выбора в жизни, понимаешь?"

ke "Словно у меня и не было шанса принять решение, вся херня просто шла своим чередом."

ke "Как будто всё заранее запрограммировано. Похоже на судьбу… или что-то вроде того. Как будто у меня нет права голоса в определении своих поступков."

stop music fadeout 0.5

show kenji rage_ni at tworight
with vpunch

ke "Скорее, задай мне вопрос!"

hi "Хм…"

ke "Быстро!"

hi "Я что-то не совсем…"

show kenji tsun_ni at tworight
with charachange

ke "Видишь? Вот ещё один пример! Чёрт! Дерьмо! Чёрт! Видишь, да? Я сейчас пытаюсь пойти против судьбы и взять управление своей жизнью в свои руки, но у меня даже нет возможности."

ke "Блин, чувак, ты меня обломал. Обломал меня в последний раз. Пипец."

#This code was glitchy as fuck. Made Kenji float sideways. Replaced it with the code from the final -md01
#show kenji tsun_ni at Move((0.7,1.0,0.5,1.0),(0.7,.9,0.5,0.5),1.0,time_warp=_ease_time_warp)
#with Pause(1.0)

#show kenji tsun_ni at RotoZoom(0,90,.7,1.0,1.0,0.0,rot_time_warp=_ease_out_time_warp,xpos=0.7, xanchor=0.5, ypos=.9, yanchor=0.5), Move((0.7,.9,0.5,0.5),(0.7,1.0,0.5,0.3),.7,time_warp=_ease_out_time_warp)
#with Pause(.7)

show kenji tsun_ni :
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0
    easeout 0.7 ypos 0.9 yanchor 0.5
with Pause(0.8)

show kenji tsun_ni :
    rotate 0
    easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3

with Pause(.7)
play sound sfx_impact
with vpunch

hide kenji

"Он падает на колени, затем валится набок, растягиваясь на гравии крыши."

hi "Эй, ты в порядке?"

ke "Нет, я не в порядке, не видишь – я в отчаянии?"

"Отвечает он мне язвительно."

#show kenji neutral_ni at Move((.7,1.0,.5,0.0),(.7,1.0,.5,.7),1.0, time_warp=_ease_in_time_warp)
#with charachange

show kenji neutral_ni :
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
    easein 0.5 ypos 1.0 yanchor 0.7
with Pause(0.5)

"Внезапно %(name_kenji)s садится, неловко отряхивается и протягивает ко мне руку за бутылкой. Я передаю ему остатки."

show kenji tsun_ni at Position(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange

ke "Что за чёрт? Блин, ты прикончил почти целую бутылку. Видишь, это как моя жизнь – никаких альтернатив…"

ke "Так и будет теперь всё время?"

hi "Ну, я вполне уверен, что всё время так не будет."

"О чём бы он ни толковал. У меня кружится голова. Я встаю и прислоняюсь к ограде, надеясь, что это поможет мне немного собраться."

show kenji tsun_ni at center
show bg school_roof_ni at center
with charamove

play music music_kenji fadein 0.5

ke "Да-а, я знаю. Надо превозмогать, сражаться всем, что имеем. Так и живём."

show kenji neutral_ni
with charachange

ke "Ты правильный парень."

show kenji happy_ni
with charachange

ke "Наша братская связь – то, что поддерживает меня в эти тёмные времена."

show kenji neutral_ni
with charachange

ke "Айда троллить женщин."

hi "Тралить женщин? Чего?"

show kenji neutral_close_ni
with characlose

ke "Троллить женщин. Троллить за женщин. Но нам надо начинать сейчас, пока я не потерял пьяную храбрость."

"Он дико размахивает руками. Безумно даже."

show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant

"Я отступаю назад."

show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"Он шагает вперёд."

stop music fadeout 1.0

show kenji happy_close_ni
with charachange

ke "Что с тобой? Не в настроении для любви?"

hi "Если честно… нет."

show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant

"Я делаю ещё шаг назад."

show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"Он делает ещё шаг вперёд."

"Он чересчур близко наклоняется ко мне."

hi "Что за чёрт, перестань ко мне прижиматься, мне это не нравится."

ke "Как прижиматься? Эй, тебе не стоит так опираться на ограду, это небезопасно."

"Я стараюсь отодвинуться от %(name_kenji)s, но моё равновесие меня подводит."

play music music_tension fadein 0.1

"Пошатываясь от головокружения, я хватаюсь за столбик ограды, но он поддаётся, как только я наваливаюсь на него своим весом."

"…Нехорошо это. Хотя мой пропитанный алкоголем мозг не может дать ответ почему."

#show black behind bg
#with None

#show n_vignette at RotoZoom(0,0,0.0,4.0,1.2,0.2, xalign=0.5, yalign=0.5)
#with Pause(0.2)

#show n_vignette at RotoZoom(0,0,0.0,1.3,0.0,8.0, xalign=0.5, yalign=0.5)
#show kenji happy_close_ni at RotoZoom(0,0,0.0,1.0,0.0,8.0, xalign=0.5, yalign=0.5)
#show bg school_roof_ni_crop at RotoZoom(0,0,0.0,1.0,0.0,8.0, xalign=0.5, yalign=0.5)

show black behind bg 
with None

show n_vignette :
    xalign 0.5 yalign 0.5 zoom 4.0
    linear 0.2 zoom 1.2
with Pause(0.2)

show n_vignette :
    zoom 1.2
    linear 8.0 zoom 0.001
show kenji happy_close_ni :
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
show bg school_roof_ni_crop :
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001


"Хотя лицо %(name_kenji)s, кажется, становится меньше – хоть какое-то облегчение."

"Вообще-то намного меньше. И с такой скоростью."

"И, похоже, начинает дуть ветер. Из-за этого я почему-то кажусь себе почти невесомым."

"Я в ступоре, будто мой разум полностью опустел."

hi "Я… падаю?"

scene nightsky rotation
with locationchange

"Кружась в воздухе, я смотрю на ночное небо. Бутылка выпадает из моих пальцев и бесследно исчезает, пока я лечу."

"Я понимаю, что это подходящий конец для плохого, по-настоящему плохого дня."

window hide

stop music fadeout 0.1
play sound sfx_crunchydeath

return



label ru_A45:
window hide
$ renpy.pause(1.0)

image wrestlemania = "bgs/misc_wrestlemania.jpg"

image flash = Solid((255, 255, 255, 255))

$ renpy.music.set_volume(1.0, 0.0, "music")

play music "bgm/Painful.ogg"

$ renpy.music.set_volume(0.15, 0.0, "ambient")

play ambient "sfx/cheer.ogg" fadein 4.0



scene wrestlemania:
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    2.0
    'flash'
    0.05 #2.05
    'wrestlemania'
    1.5 #3.55
    'flash'
    0.05 #3.6
    'wrestlemania'
    0.27 #3.87
    'flash'
    0.05 #3.92
    'wrestlemania'
    0.29 #3.949
    'flash'
    0.05 #3.999
    'wrestlemania'
    0.27 #4.269
    'flash'
    0.05 #4.274
    'wrestlemania'
    2.0 #6.418
with Pause(6.418)

show flash:
    alpha 1.0
    linear 4.0 alpha 0.0
with Pause(5.724)

scene wrestlemania:
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    'flash'
    0.05 #2.05
    'wrestlemania'
    1.6 #3.55
    'flash'
    0.05 #3.6
    'wrestlemania'
    0.27 #3.87
    'flash'
    0.05 #3.92
    'wrestlemania'
    0.29 #3.949
    'flash'
    0.05 #3.999
    'wrestlemania'
    0.27 #4.269
    'flash'
    0.05 #4.274
    'wrestlemania'
    2.0 #6.418
with Pause(4.418)

show flash:
    alpha 1.0
    linear 4.0 alpha 0.0
with Pause(5.724)
    
show kenji tsun:
    xanchor 0.5 yanchor 0.5
    xpos 0.5 ypos 1.5
    linear 10.0 ypos 0.5
    
$ renpy.music.set_volume(0.3, 1.0, "ambient")
    
show flash behind kenji:
    linear 0.05 alpha 0.0
    linear 0.05 alpha 1.0
    repeat
    
window show

ke "Чуешь, что готовит %(name_kenji)s?"

return


