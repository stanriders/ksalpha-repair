init -2 python:
    ### RUSSIAN (gonna be a thing)
    
    init_language("ru")
        
    displayDict["ru"].styleoverrides = {"font": rufont, 
                                    "language": "western",
                                    "line_spacing": 0}
                                    
    
    displayDict["ru"].timeformat = '%d.%m.%y %H:%M'
    
    displayDict["ru"].activeLanguage = ruw(u"Русский")
    displayDict["ru"].allLanguages = {}
    displayDict["ru"].allLanguages["en"] = ruw(u"Английский")
    displayDict["ru"].allLanguages["de"] = ruw(u"Немецкий")
    displayDict["ru"].allLanguages["it"] = ruw(u"Итальянский")
    displayDict["ru"].allLanguages["jp"] = ruw(u"Японский")
    displayDict["ru"].allLanguages["ru"] = displayDict["ru"].activeLanguage
    
    displayDict['ru'].act_term = ruw(u"Акт")
    displayDict["en"].window_name = u"Katawa Shoujo"
    
    displayDict['ru'].main_menu_start = ruw(u"Начать игру")
    displayDict['ru'].main_menu_load = ruw(u"Загрузить")
    displayDict['ru'].main_menu_extra = ruw(u"Дополнительно")
    displayDict['ru'].main_menu_config = ruw(u"Настройки")
    displayDict['ru'].main_menu_quit = ruw(u"Выход")

    displayDict['ru'].game_menu_return = ruw(u"Назад")
    displayDict['ru'].game_menu_show = ruw(u"Показать фон")
    displayDict['ru'].game_menu_history = ruw(u"История")
    displayDict['ru'].game_menu_skip = ruw(u"Пропуск")
    displayDict['ru'].game_menu_auto = ruw(u"Авточтение")
    displayDict['ru'].game_menu_config = ruw(u"Настройки")
    displayDict['ru'].game_menu_save = ruw(u"Сохранить")
    displayDict['ru'].game_menu_load = ruw(u"Загрузить")
    displayDict['ru'].game_menu_main = ruw(u"Главное меню")
    displayDict['ru'].game_menu_quit = ruw(u"Выйти")
    
    displayDict["ru"].game_menu_jumper = ruw(u"Выбрать Акт")
        
    displayDict['ru'].game_menu_current_scene = ruw(u"Текущая сцена")
    displayDict['ru'].game_menu_current_music = ruw(u"Текущая композиция")
    displayDict['ru'].game_menu_replay_indicator = ruw(u"Переиграть")

    displayDict['ru'].return_button_text = ruw(u"Назад")

    displayDict['ru'].hdisabled_label = ruw(u"Отключить сцены для взрослых")
    displayDict['ru'].config_page_caption = ruw(u"Настройки")
    displayDict['ru'].config_fullscreen_label = ruw(u"Полноэкранный режим")
    displayDict['ru'].config_transitions_label = ruw(u"Отключить переходы")
    displayDict['ru'].config_skip_unseen_label = ruw(u"Пропускать непрочитанный текст")
    displayDict['ru'].config_skip_after_choice_label = ruw(u"Продолжать пропуск после выбора")
    displayDict['ru'].config_textspeed_label = ruw(u"Скорость текста")
    displayDict['ru'].config_afmspeed_label = ruw(u"Задержка авточтения")
    displayDict['ru'].config_musicvol_label = ruw(u"Музыка")
    displayDict['ru'].config_musicvol_jukebox_label = ruw(u"Гр.")
    displayDict['ru'].config_sfxvol_label = ruw(u"Звуки")
    displayDict['ru'].config_sfxtest_label = ruw(u"Проверка")
    displayDict['ru'].config_gamepad_label = ruw(u"Настройка геймпада…")

    displayDict['ru'].config_language_sel = ruw(u"Выбор языка…")
    displayDict['ru'].config_language_caption = ruw(u"Настройки » Выбор языка")
    displayDict['ru'].config_language_restart_note = ruw(u"Примечание: смена языка во время игры приведёт к возврату на начало последней сцены.")
    
    displayDict['ru'].config_language_naming = ruw(u"Варианты перевода имен") # Эта строка есть только в русском переводе [str]

    displayDict['ru'].gamepad_caption = ruw(u"Настройки » Настройка геймпада")
    displayDict['ru'].gamepad_key_na = ruw(u"Не назначено")
    displayDict['ru'].gamepad_request_key = ruw(u"Нажмите кнопку для привязки к “%s”.\nЩёлкните кнопкой мыши или нажмите select чтобы очистить привязку.")

    displayDict['ru'].yesno_yes = ruw(u"Да")
    displayDict['ru'].yesno_no = ruw(u"Нет")
    displayDict['ru'].yesno_okay = ruw(u"Продолжить")
    displayDict['ru'].yesno_savesuccess = ruw(u"Игра успешно сохранена под номером %s.")
    displayDict['ru'].yesno_quit = ruw(u"Вы уверены, что хотите выйти из\nKatawa Shoujo?")
    displayDict['ru'].yesno_return_to_main = ruw(u"Вы уверены что хотите \nвернуться в главное меню?")
    displayDict['ru'].save_page_caption = ruw(u"Сохранить")
    displayDict['ru'].new_save_button = ruw(u"Создать новое сохранение")
    displayDict['ru'].load_page_caption = ruw(u"Загрузить")
    displayDict['ru'].yesno_load_in_game = ruw(u"Вы уверены, что хотите\nпотерять весь пройденный путь?")
    displayDict['ru'].yesno_save_overwrite = ruw(u"Вы уверены, что хотите переписать\nсохранённую игру?")
    displayDict['ru'].yesno_delete_savegame = ruw(u"Вы уверены, что хотите\nудалить это сохранение?")
    displayDict['ru'].play_time_label = ruw(u"Время игры")
    displayDict['ru'].show_manual_saves = ruw(u"Ручные")
    displayDict['ru'].show_auto_saves = ruw(u"Авто")

    displayDict['ru'].text_history_caption = ruw(u"История")

    displayDict['ru'].extra_menu_caption = ruw(u"Дополнительно")
    displayDict['ru'].extra_music_button_label = ruw(u"Музыка")
    displayDict['ru'].extra_gallery_button_label = ruw(u"Галерея")
    displayDict['ru'].extra_scene_button_label = ruw(u"Библиотека")
    displayDict['ru'].extra_omake_button_label = ruw(u"Бонус")
    displayDict['ru'].extra_opening_button_label = ruw(u"Видео")
    displayDict['ru'].commentary_label = ruw(u"Включить комментарии")

    displayDict['ru'].music_page_caption = ruw(u"Дополнительно » Музыка")
    displayDict['ru'].music_stop_button_text = ruw(u"Стоп")
    displayDict['ru'].music_now_playing = ruw(u"Проигрывается")

    displayDict['ru'].gallery_page_caption = ruw(u"Дополнительно » Галерея")
    displayDict['ru'].gallery_onelocked = ruw(u"Следующее изображение не открыто.")
    displayDict['ru'].gallery_manylocked = ruw(u"%d следующих изображений не открыто.")
    displayDict['ru'].gallery_singlelocked = ruw(u"%d изображений из %d не открыто.")
    displayDict['ru'].gallery_num_page_prefix = ruw(u"Страница ")
    displayDict['ru'].gallery_num_page_error = ruw(u"Нет изображений")

    displayDict['ru'].scene_page_caption = ruw(u"Дополнительно » Библиотека")
    displayDict['ru'].scene_completion_label = ruw(u"Завершено: %s%%")
    displayDict['ru'].scene_playthrough_label = ruw(u"Использовать режим потока (рекомендуется)")
    
    displayDict['ru'].joy_left = ruw(u"Влево")
    displayDict['ru'].joy_right = ruw(u"Вправо")
    displayDict['ru'].joy_up = ruw(u"Вверх")
    displayDict['ru'].joy_down = ruw(u"Вниз")
    displayDict['ru'].joy_dismiss = ruw(u"Выбор\\u0434альше")
    displayDict['ru'].joy_rollback = ruw(u"История")
    displayDict['ru'].joy_holdskip = ruw(u"Удерживать для пропуска")
    displayDict['ru'].joy_toggleskip = ruw(u"Режим пропуска")
    displayDict['ru'].joy_hide = ruw(u"Показать изображение")
    displayDict['ru'].joy_menu = ruw(u"Показать меню")

    ##Names

    displayDict['ru'].name_hi = ruw(u"Хисао")
    displayDict["en"].name_all = ruw(u"Все")
    displayDict['ru'].name_ha = ruw(u"Ханако")
    displayDict['ru'].name_emi = ruw(u"Эми")
    displayDict['ru'].name_rin = ruw(u"Рин")
    displayDict['ru'].name_li = ruw(u"Лилли")
    displayDict["ru"].name_shi = name_shizune # hepb/poli switching
    displayDict['ru'].name_mi = ruw(u"Миша")
    
    displayDict["ru"].name_ke = name_kenji # hepb/poli switching
    displayDict['ru'].name_mu = ruw(u"Муто")
    displayDict['ru'].name_nk = ruw(u"Фельдшер")
    displayDict['ru'].name_no = ruw(u"Номия")
    displayDict['ru'].name_yu = ruw(u"Юко")
    displayDict["en"].name_sa = name_sae # hepb/poli switching
    displayDict['ru'].name_aki = ruw(u"Акира")
    displayDict['ru'].name_hh = ruw(u"Хидеаки")
    displayDict["en"].name_hx = name_jigoro # hepb/poli switching
    displayDict['ru'].name_emm = ruw(u"Мейко")
    
    displayDict['ru'].name_mk = ruw(u"Мики")
    
    displayDict["ru"].name_mystery = "???"

    displayDict['ru'].name_ha_ = u"Девушка с чёлкой"
    displayDict['ru'].name_emi_ = u"Девочка с хвостиками"
    displayDict['ru'].name_rin_ = u"Странная девушка"
    displayDict['ru'].name_li_ = u"Светловолосая девушка"
    displayDict['ru'].name_mi_ = u"Смеющаяся девушка"
    displayDict['ru'].name_ke_ = u"Сосед в очках"
    displayDict['ru'].name_mu_ = u"Высокий мужчина"
    displayDict['ru'].name_yu_ = u"Библиотекарь"
    displayDict['ru'].name_no_ = u"Седой мужчина"
    displayDict['ru'].name_sa_ = u"Владелица галереи"
    displayDict['ru'].name_aki_ = u"Хорошо одетый человек"
    displayDict['ru'].name_nk_ = u"Улыбчивый человек"
    displayDict["en"].name_hx_ = (u"Отец ") + (name_shizune) # hepb/poli switching
    displayDict['ru'].name_hh_ = u"Худая девушка"
    displayDict['ru'].name_emm_ = u"Мать Эми"
    
    # Scenes available in the extras -> scene select menu. Name, label, description, path (path may also be a tuple).
    # Now also doubles as a lookup list for the actual scene names. Display in the extras can be suppressed
    # by setting the third value in the tuple to False. Suppression doesn't work in DQN mode.
    # Note that Ren'Py doesn't like non-ASCII characters in scene titles if the titles are not unicode strings
    displayDict['ru'].s_scenes = (
                                    (ruw(u"На морозе"), 'NOP1', ruw(u"Холодным снежным днём мечты Хисао готовы осуществиться, но всё обрывается внезапным сердечным приступом."), 'Act 1'), # NEW ACT 1
                                    (ruw(u"Бремя Хисао"), 'NOP2', ruw(u"Хисао рассказывают о школе-интернате «Ямаку», где он, вероятно, проведёт остаток своих школьных дней."), 'Act 1'),
                                    (ruw(u"Воздействие ворот"), 'A1', ruw(u"Хисао впервые приходит в школу-интернат «Ямаку» и знакомится со своим классным руководителем Муто."), 'Act 1'),
                                    (ruw(u"Вход на сцену слева"), 'A2', ruw(u"Представление классу и встреча со старостой и её переводчицей."), 'Act 1'),
                                    (ruw(u"На приёме"), 'A3', (ruw((u"Миша и ")) + (name_shizune)) + (ruw(u" показывают Хисао столовую, после чего он идёт на прием к фельдшеру.")), 'Act 1'),
                                    (ruw(u"Ничья комната"), 'A4', (ruw((u"Хисао идёт в свою комнату, по пути встречая соседа по имени ")) + (name_kenji)) + ('.'), 'Act 1'),
                                    (ruw(u"Небольшой разговор"), 'A5', (name_shizune) + ruw((u" и Миша рассказывают Хисао о предстоящем фестивале и приглашают его на ланч.")), 'Act 1'),
                                    (ruw(u"Риск и награда"), 'A6', (name_shizune) + ruw((u" и Хисао борются за мировое господство.")), 'Act 1'),
                                    (ruw(u"Чаепитие вслепую"), 'A7', ruw(u"В поисках библиотеки Хисао теряется и в неиспользуемом кабинете обнаруживает Лилли."), 'Act 1'),
                                    (ruw(u"Общая библиотека"), 'A8', ruw(u"Наконец найдя путь в библиотеку, Хисао встречает и вспугивает Ханако"), 'Act 1'),
                                    ("Bizarre and Surreal", "A9", "Kenji reveals the dark secrets of Yamaku.", "Act 1"),
                                    ("Lunch Evolution Theory", "A10", "Shizune and Misha badger Hisao into joining the Student Council before discussing lunch.", "Act 1"),
                                    ("Short Sharp Shock", "A11_1", "On his way to lunch alongside Misha and Shizune, Hisao collides with Emi in the hallway.", "Act 1"),
                                    ("Meet Cute", "A11_2", "Hisao collides with a rampaging Emi on his way to lunch with Hanako and Lilly.", "Act 1"),
                                    ("Detour Ahead", "A12", "Shizune and Misha take Hisao to their favourite teahouse, the Shanghai.", "Act 1"),
                                    ("Sip (part 1)", "A13", "Hisao has a peaceful lunch with Lilly and Hanako.", "Act 1"), # there is no A14
                                    ("It Builds Character", "A15", "Mutou tries to have a D&M talk with Hisao, but Misha interrupts and puts Hisao to work.", "Act 1"),
                                    ("A Private Lunch", "A16", "Searching for supplies, Hisao happens across a strange girl in the art room.", "Act 1"),
                                    ("Waylay", "A17", "While helping Rin carry some paint, Hisao is quizzed by the nurse.", "Act 1"),
                                    ("The Other Green", "A18", "Hisao watches Rin paint her mural.", "Act 1"),
                                    ("The Running Girl", "A19", "When attempting to do some morning exercise, Hisao meets Emi at the running track.", "Act 1"),
                                    ("Soap", "A20", "Kenji ambushes Hisao in the shower in an attempt to get some cash.", "Act 1"),
                                    ("Cold War", "A21", "Shizune and Lilly face off over budget requests.", "Act 1"),
                                    ("Proof of Competency", "A22", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
                                    ("Event Horizon", "A22_2", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
                                    ("Above and Beyond", "A23_1", "Hisao gets a lecture about the noble duties of a Student Council.", "Act 1"),
                                    ("Things You Can Do", "A23_2", "After escaping from the clutches of Shizune and Misha, Hisao helps out Rin again.", "Act 1"),
                                    ("Paint by Numbers", "A24", "Hanako and Hisao lend a hand to Lilly's class by volunteering to help build their stall.", "Act 1"),
                                    ("Exercise", "A25", "Another early morning sees Hisao running at the track with Emi.", "Act 1"),
                                    ("Invisible Hat", "A26", "Kenji gives Hisao a few insider tips on how to socialize.", "Act 1"),
                                    ("Home Field Advantage", "A26_1", "Shizune and Misha hijack Hisao as he leaves his room for class.", "Act 1"),
                                    ("No Recovery", "A27", False, "Act 1"), #this is somewhat of a hack, and a special case
                                    ("Slow Recovery", "A27_1", "Recovering from his heart flutter, Hisao eventually makes it to class.", "Act 1"),
                                    ("No Recovery", "A27_2", "Hisao struggles to class after his hijacking by the Student Council.", "Act 1"),
                                    ("No Free Lunch", "A28", "Hisao is escorted to the Student Council office for his first official day there.", "Act 1"),
                                    ("Foot and Mouth", "A29", "Emi drags Hisao to the roof to have lunch with Rin.", "Act 1"),
                                    ("Mind Your Step", "A30", "Hisao and Lilly go shopping, meeting a very confused Rin on the way back.", "Act 1"),
                                    ("Support", "A31", "Hisao has his first Saturday lesson, complete with a talking to from Mutou.", "Act 1"),
                                    ("An Aesthetics", "A32", "Emi finds Hisao slacking around after class and recruits him to help Rin once again.", "Act 1"),
                                    ("Creative Pain", "A33", "Hisao meets the art teacher, Nomiya, as Rin paints her mural.", "Act 1"),
                                    ("Proper Exercise", "A34", "Emi and Hisao discuss the importance of being in shape.", "Act 1"),
                                    ("Sip (part 2)", "A35", "In an attempt to kill time, Hisao goes for a walk around the school.", "Act 1"),
                                    ("Shanghaied", "A36", "Tea, cake and competitions with Shizune and Misha at the Shanghai.", "Act 1"),
                                    ("Quiet", "A37", "Hanako and Hisao read books for the festival.", "Act 1"),
                                    ("Don't Panic", "A38", "After waking up on the day of the festival, Hisao is greeted by a ranting Kenji.", "Act 1"),
                                    ("Is Carnival!", "A39", "Emi catches Hisao eating fried food and makes him accompany her as punishment.", ("Act 1", "Emi")),
                                    ("Clouds in My Head", "A40", "Hisao keeps Rin and her now-finished mural company.", ("Act 1", "Rin")),
                                    ("Promise of Time", "A41", "After a trying morning at her stall, Hisao takes Lilly to find Hanako.", ("Act 1", "Lilly")),
                                    ("Nc5xb3", "A42", "Unable to help Lilly at her stall, Hisao searches for Hanako at the festival.", ("Act 1", "Hanako")),
                                    ("The Deep End", "A43", "Kenji and Hisao share a manly picnic on the roof instead of going to the festival.", "Act 1"),
                                    ("Throwing Balls", "A44", "True to his word, Hisao spends the day with Shizune and Misha.", ("Act 1", "Shizune")),
                                    ("Morning Run", "E3", "The first of Hisao's many morning runs with Emi.", "Emi"),
                                    ("Clouds, Time Travel, and Thou", "E4", "Another rooftop lunch with Emi and Rin. Hisao asks the two about the reasons for their friendship.", "Emi"),
                                    ("Questions That Need Answering!", "E5", "Idle chat between Emi and Hisao. Hisao asks Emi few more questions about her relationship with Rin.", "Emi"),
                                    ("Second Time's the Worst", "E6", "The second morning run. Hisao is almost dragged kicking and screaming around the track.", "Emi"),
                                    ("Let the Shipping Begin", "E7", "Hisao pays a visit to the nurse along with Emi, finding that the two have known each other for a while.", "Emi"),
                                    ("Track Meeting", "E8", "The day of the track meet. Another facet of Emi's personality is revealed.", "Emi"),
                                    ("Down that Medicine Now", "E9", "Hisao mentions a pain in his chest during a visit to the nurse and receives a lecture.", "Emi"),
                                    ("Piracy on the High Seas", "E10", "Hisao takes a nap on the rooftop, then discusses his future as a pirate with Emi.", "Emi"),
                                    ("Obligatory Dream Sequence", "E11", "And a very trippy dream sequence at that.", "Emi"),
                                    ("Famous Last Words", "E12", "Emi and Rin take Hisao along for a picnic, soon to be spoiled by rain.", "Emi"),
                                    ("Tracking Absences", "E13", "Hisao goes to the track as usual, but Emi is missing.", "Emi"),
                                    ("Dropping By", "E14", "A bedside visit for a sick Emi, which quickly changes to something else entirely.", "Emi"),
                                    ("The First Morning After", "E15", "Hisao reminisces about last morning, deciding to do something to help Emi.", "Emi"),
                                    ("The (Real) Beginning", "E16", "Another lunchtime on the rooftop, sans Rin.", "Emi"),
                                    (u"Eet Ees… Scienca!", "E17", "Mutou pulls Hisao into a short discussion about his future.", "Emi"),
                                    ("Definitions", "E18", "Emi and Hisao attempt another picnic, this time without any intervention from Mother Nature.", "Emi"),
                                    ("Science Sandwiches", "E19", "Back to the track in the morning, with business as usual, or so it seems.", "Emi"),
                                    ("Lunch and Science", "E20", "Hisao sees Mutou again about his future in the sciences.", "Emi"),
                                    ("Up, down, and up again", "E21", "Hisao helps further Kenji's causes using unusual methods.", "Emi"),
                                    ("Storage Space", "E22", "Emi pulls Hisao into the storage shed to talk with him, if you know what I mean.", "Emi"),
                                    ("After-School Plans", "E23", "Emi has Hisao make a few promises.", "Emi"),
                                    ("Putting the Fun in Funeral", "E24", "Hisao meets Emi's mom, as well as a graveside visit.", "Emi"),
                                    ("Clean Teeth", "E25", "Hisao wakes up, finding Emi sleeping next to him. Later, he finds Yuuko in his bathroom.", "Emi"),
                                    ("Hooray for Socks!", "E26", "Sex, drugs, but no rock and roll.", "Emi"),
                                    ("Debate Expresses Doubt", "E27", "Storytime with the nurse.", "Emi"),
                                    (u"Guess Who's Coming… Nevermind", "E28", True, "Emi"),
                                    ("Movement", "H2", "Lilly finishes her duties and treats Hanako and Hisao to tea", "Hanako"),
                                    ("Rosarium", "H3", "Hisao takes Hanako Shopping", "Hanako"),
                                    ("Chinese Tea", "H4", "Hanako invites Hisao to have lunch with her and Lilly.", "Hanako"),
                                    ("Dies Irae", "H5", "Hisao chooses between eating with Shizune or playing chess with Hanako", "Hanako"),
                                    ("Office Confessional", "H5_1", "Hisao and Misha discuss the plight of Hanako.", "Hanako"),
                                    ("Chess and Slides", "H5_2", "Hisao ditches the Student Council to read with Hanako", "Hanako"),
                                    ("On Waking Early", "H6", "Hisao wakes up early and has breakfast with Lilly.", "Hanako"),
                                    ("The First Tea Party", "HLT3", "The duet of trickery make Hisao their plaything in Lilly's private quarters.", ("Hanako", "Lilly")),
                                    ("Electric Angel", "HLT4", True, ("Hanako", "Lilly")),
                                    ("Kicks!", "HLT5", True, ("Hanako", "Lilly")),
                                    ("Droplets of Winter", "HLT6", True, ("Hanako", "Lilly")),
                                    ("Dining with the Mad Hatter", "H7", "Lilly invites Hisao to a tea party after hours.", "Hanako"), 
                                    ("Small Change", "H8", "Hisao forces Kenji to repay his loan.", "Hanako"),
                                    ("Through the Looking Glass", "H9", "Hisao and Lilly discuss Hanako's truancy.", "Hanako"),
                                    ("Dance Dance Dance!", "H10", "Hanako reveals her past to Hisao in return for learning about his heart.", "Hanako"),#End of Act 2 
                                    ("The Invitation", "H11", "Lilly finds Hisao cleaning up the Tea Room and tells him about Hanako's Birthday.", "Hanako"),
                                    ("Unexpected Alliance", "H12", "Shizune and Misha drag Hisao to dinner and Hisao finds out about Karaoke bars in town.", "Hanako"),#end of Final route similarities
                                    ("Kagerou", "H13", "Lilly and Hisao check out karaoke bars for Hanako's Party.", "Hanako"),
                                    #("Prompted Confession", "H14", "The trio get wasted during Lilly's party and Hisao half-heartedly admits his feelings to Hanako.", "Hanako"),
                                    ("Note From the Editor", "H14", "Choose your own adventure.", "Hanako"), # ending choice/personal notes
                                    ("Like Wildfire", "H15", True, "Hanako"),
                                    ("Fast and Thin", "H16", True, "Hanako"),
                                    ("Time Alone", "H17", True, "Hanako"),
                                    ("An Audience of Two", "H18", True, "Hanako"),
                                    ("Undue Concern", "H19", True, "Hanako"),
                                    ("Study Week", "H20", True, "Hanako"),
                                    ("Contemplation", "H21", True, "Hanako"),
                                    ("Tatters", "H22", True, "Hanako"),
                                    ("Waterfall", "H23", True, "Hanako"), # this scene exists online- Hisao's heartattack, leads to all bad ends
                                    ("Dawn", "H24", True, "Hanako"), # start of the returning script- scenes H14-H22/23 nonexistent
                                    ("Revelation", "H25", True, "Hanako"),
                                    ("In State", "H26", True, "Hanako"),
                                    ("Dulce Et Decorum Est", "H27", True, "Hanako"), # bad end 1
                                    ("Patience is a Virtue", "H28", True, "Hanako"),
                                    #("Future", "H29", True, "Hanako"), # want to also throw this between HT3 and HT4, if possible
                                    ("Triumphant Return", "H30", True, "Hanako"),
                                    ("Once more into the Breech", "H31", True, "Hanako"), # chance for bad end 2
                                    ("A Spoonful of Sugar", "H32", True, "Hanako"), # bad end 3, final destination
                                    ("Rhapsody in Blue", "L19", "Hisao visits Lilly in the hospital, where she makes a request of him.", "Hanako"),
                                    ("The Momentary Present", "L20", "After returning to the school, Hisao is met with a variety of surprises.", "Hanako"),
                                    ("A Pair of Steiffs", "HT1", "Hisao and Hanako visit the antique shop to find a present for Lilly.", "Hanako"), # Hanako True path
                                    ("Nothing's There", "HT2", "The duo deliver Lilly's presents to her in the hospital.", "Hanako"),
                                    ("Drizzly Night", "HT3", "Hisao attempts to give Hanako her bear and is met with a surprise.", "Hanako"),
                                    ("Painful History", "H29", "A life is forever changed.", "Hanako"), 
                                    ("Calling the Sunrise", "HT4", "Hisao returns to class after spending the night with Hanako in Lilly's room.", "Hanako"),
                                    ("Welcome Party", "HT5", "The group throws a party to celebrate Lilly's return and Hanako shows her growing confidence.", "Hanako"),
                                    ("Confession Vocal", "HT6", "Hisao consults Lilly about the previous night's events and Hanako gives Hisao a mysterious note.", "Hanako"),
                                    ("Girl Uppi", "HT7", "Hisao receives a pep talk from Lilly and meets Hanako behind the dorms.", "Hanako"),
                                    ("Four Right Feet", "HT8", "Hisao and Hanako's feelings for one another are finally realized.", "Hanako"),
                                    ("Lullaby for Strain", "HT9", "Hanako takes Hisao on a picnic date to a place that is special to her.", "Hanako"),
                                    ("Under Slave", "HT10", "The two share in their moment of embrace.", "Hanako"),
                                    ("Love is Psychadelic", "HT11", "After passing out the previous night, Hisao cleans up and makes a trip to the nurse's office.", "Hanako"),
                                    ("Eternal Dream", "HT12", "Hisao and Hanako visit Yuuko at the Shanghai, and Hisao tries to sneak a purchase past Hanako at the mart.", "Hanako"),
                                    ("Words I Cannot Say", "HT13", "The two share in another intimate moment, but are met by a surprise visitor.", "Hanako"),
                                    ("Re-Sublimity", "HT14", "Hanako invites Shizune and Misha to eat lunch on the rooftop, where they find Emi, Rin, and Lilly.", "Hanako"),
                                    ("Curves in Spacetime", "HT15", "Hisao gets roped into tutoring all six girls in science.", "Hanako"),
                                    ("Sucker Punch", "HT16", "After conquering finals, the group decides to celebrate in the Student Council room after-hours.", "Hanako"),
                                    ("I'm Here", "HT17", "Hanako faces the ghosts of her past.", "Hanako"),
                                    ("Mad Hatter", "L1", "Hisao shares the first of many lunchbreaks with Hanako and Lilly, resting from the day before.", "Lilly"),
                                    ("A One Rand Note", "L2", "Cornered by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.", "Lilly"),
                                    ("Presents and Presence", "L3", "While out in search of a present for Hanako, Lilly and Hisao meet Akira's fiancé.", "Lilly"),
                                    ("Unidentified Drinking Object", "L4", "The trio hold a birthday party for Hanako, interrupted by the surprise appearance of a certain sibling.", "Lilly"),
                                    ("The Day After", "L5", "Hisao and Lilly awaken, and try to recuperate from the previous evening's harried events.", "Lilly"),
                                    ("A Brief History of Thyme", "L6", "Hisao and Lilly go to get some groceries.", "Lilly"),
                                    ("The Two's Past", "L7", "Akira retells the childhood that she and Lilly have shared.", "Lilly"),
                                    ("Bon Voyage", "L8", "Lilly and Akira are seen off as they take a trip to their family in South Africa.", "Lilly"),
                                    ("Day by Day", "L9", "Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.", "Lilly"),
                                    ("Minor Discord", "L10", "Hisao talks with a quieter than usual Hanako, after Kenji gives him a little wanted promotion.", "Lilly"),
                                    ("Dissonance", "L11", "With Hanako withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.", "Lilly"),
                                    ("A World Away", "L12", "Hisao's reassured mind begins to wonder about the relationship between he and Lilly.", "Lilly"),
                                    ("Renewal", "L13", "Hisao, Lilly and Hideaki greet Akira and Lilly after their return from South Africa.", "Lilly"),
                                    ("Northern Sojourn", "L14", "The trio begin their holiday in Hokkaido.", "Lilly"),
                                    ("Prelude", "L15", "A morning walk begins a chain reaction of events.", "Lilly"),
                                    ("Crescendo", "L16", "Lilly's true feelings are told in the endless gold of the wheat fields." , "Lilly"),
                                    ("Diminuendo", "L17", "The two share their first night together.", "Lilly"),
                                    ("Grey Outlook", "L18", "Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.", "Lilly"),
                                    ("Rhapsody in Blue", "L19", "Hisao reflects on where he and Lilly are in life, before being joined by another.", "Lilly"),
                                    ("The Momentary Present", "L20", "Travelling back to Yamaku, Hisao and Lilly idly talk between themselves.", "Lilly"),
                                    ("Slow Steps 'fore a Waltz", "L21", "Back at school, the events of Hokkaido come to the fore.", "Lilly"),
                                    ("Joy and Conflict", "L22", "Settling back into daily life, Akira and Hideaki join the trio's teaparty.", "Lilly"),
                                    ("A Morning's Reverie", "L23", "Hisao and Lilly discuss their ambitions.", "Lilly"),
                                    ("Correct Procedure", "L24", "Hisao and Lilly arrange a date, before Hideaki and Akira join them.", "Lilly"),
                                    ("Out and About", "L25", "Hisao and Lilly go on their first date, finding out about each other's pasts.", "Lilly"),
                                    ("Steps of the Three", "L26", "Hisao, Hanako and Lilly muse on the upcoming holidays as they share tea together.", "Lilly"),
                                    ("Blackout", "L27", "An unexpected offer leads to an unexpected evening.", "Lilly"),
                                    ("A Faraway Future", "L28", "Lilly reveals her family's offer to join them in South Africa, With Hisao reluctantly accepting her wishes to go.", "Lilly"),
                                    ("Farewell", "L29", "Hisao and Hanako farewell Akira and Lilly the evening before they leave Japan.", "Lilly"),
                                    ("False Cadence", "L30", "Hisao rushes to confront Lilly, realising her conflict.", "Lilly"),
                                    ("Under a Maudlin Sky", "L31", "Waking in the hospital ward, Hisao struggles to come to terms with his life.", "Lilly"),
                                    ("Under a Bright Sky", "L32", "Lilly rejoins Hisao, the two beginning their life together anew.", "Lilly"),
                                    ("Forwards, with Gusto!", "L33", "Lilly and Hisao see off Akira.", "Lilly"),
                                    ("Cloud Lunch", "R2", "Hisao spends an afternoon of skipped class with Rin watching clouds on the rooftop.", "Rin"),
                                    ("Grayscale", "R3", "Hisao attends his first art club meeting and draws a portrait of Rin.", "Rin"),
                                    ("Black Mood", "R4", "After a particularly bad school day, Hisao ends up having a talk with Rin about an unexpected subject.", "Rin"),
                                    ("Dual Mono", "R5", "A lunch with Rin and Hanako. Rin philosophizes their reasons to be at Yamaku Academy.", "Rin"),
                                    ("Audience", "R7", True, "Rin"),
                                    ("Finding Places", "R8", True, "Rin"),
                                    ("Another Morning Ruined", "R9", True, "Rin"),
                                    ("The First Day of Summer", "R10", True, "Rin"),
                                    ("The Concept of Future", "R11", True, "Rin"),
                                    ("Umbrella Logic Cake", "R12", True, "Rin"),
                                    ("Six Meters Closer to Heaven", "R13", True, "Rin"),
                                    ("Understanding Words", "R14", True, "Rin"),
                                    ("Communication Problems", "R15", True, "Rin"),
                                    ("Signal/Noise Ratio", "R16", True, "Rin"),
                                    ("Contrast", "R17", True, "Rin"),
                                    ("The Secret Place", "R18", True, "Rin"),
                                    ("Teachers and Students", "R19", True, "Rin"),
                                    ("Left/Right", "R20", True, "Rin"),
                                    ("Twenty-Second", "R21", True, "Rin"),
                                    ("Seeking", "R22", True, "Rin"),
                                    ("The Scent of Light", "R23", True, "Rin"),
                                    ("Edge of the World", "R24", True, "Rin"),
                                    ("The Context of Rin", "R25", True, "Rin"),
                                    ("Haze", "R26", True, "Rin"),
                                    ("Escapism", "R27", True, "Rin"),
                                    ("Limbo", "R28", True, "Rin"),
                                    ("Delirium", "R29", True, "Rin"),
                                    ("The Physiology of Art", "R30", True, "Rin"),
                                    ("Door", "R31", True, "Rin"),
                                    ("Shards of Ire", "R32", True, "Rin"),
                                    ("Illusions for People", "R33", True, "Rin"),
                                    ("Desperate Glory", "R34", True, "Rin"),
                                    ("Wavelength", "R35", True, "Rin"),
                                    ("Blue Period", "R36", True, "Rin"),
                                    ("The World Only You Can See", "R37", True, "Rin"),
                                    ("Problems of Self-Referential Logic", "R38", True, "Rin"),
                                    ("Measuring Shadows", "R39", True, "Rin"),
                                    (u"Raison d'être", "R40", True, "Rin"),
                                    ("Cowgirls! Napalm! Happy Day!", "R41", True, "Rin"),
                                    ("Proof of Existence", "R42", True, "Rin"),
                                    ("Packet Sniffers", "S8", True, "Shizune"),
                                    ("Talk to the Hand", "S9", True, "Shizune"),
                                    ("Chinese Whispers", "S10", True, "Shizune"),
                                    ("Hypertension", "S11", True, "Shizune"),
                                    ("Chronic Fatigue", "S12", True, "Shizune"),
                                    ("Graduation", "S13", True, "Shizune"),
                                    ("Spring into Action", "S14", True, "Shizune"),
                                    ("Best Laid Plans", "S15", True, "Shizune"),
                                    ("The Box", "S16", True, "Shizune"),
                                    ("Force Feedback", "S17", True, "Shizune"),
                                    ("United Nations", "S18", True, "Shizune"),
                                    ("Use-Mention Distinction", "S19", True, "Shizune"),
                                    ("Happiness", "S20", True, "Shizune"),
                                    ("Laughing Matters", "S21", True, "Shizune"),
                                    ("Pangrammatic Window", "S22", True, "Shizune"),
                                    ("Headgames", "S23", True, "Shizune"),
                                    ("Confrontation", "S24", True, "Shizune"),
                                    ("Duality", "S25", True, "Shizune"),
                                    ("Acute Triangle", "S26", True, "Shizune"),
                                    ("Determinacy", "S27", True, "Shizune"),
                                    ("Tongue-Tied", "S28", True, "Shizune"),
                                    ("Lookahead", "S29", True, "Shizune"),
                                    ("Spiral", "S30", True, "Shizune"),
                                    ("Rock Bottom", "S31", True, "Shizune"),
                                    ("Connected", "S32", True, "Shizune"),
                                    ("Watershed", "S33", True, "Shizune"),
                                    ("Terminal", "S34", True, "Shizune"), #Shizune bad end
                                    ("On the Flipside", "S36", True, "Shizune"),
                                    #S37 doesnt exist.
                                    #It does now. -md01
                                    ("Below the Belt", "S37", True, "Shizune"),
                                    ("Infinity", "S38", True, "Shizune"),
                                    )

# TITLE CARDS
    # Definition. This maps an id tuple to a tuple of displayed text, filename modifier, and the position of said text.
    # the display function is tcard() in ui_code.rpy
    displayDict["ru"].act_names = {(1, "all"): (u"Продолжительность жизни", "act1", 190, 117), #lulz
                                 (2, "bad"): (u"Deep Six", "act2badend", 100, 250), #climatic
                                 (2, "emi"): (u"Acceleration", "act2emi", 120, 200), #NWS
                                 (3, "emi"): (u"2x400 Relay", "act3emi", 70, 350), #konflikti
                                 (4, "emi"): (u"Dicks", "act4emi", 200, 250), #konflikti
                                 (2, "hanalilly"): (u"Entanglement", "act2hanalilly", 380, 50), #animejet
                                 (3, "hanako"): (u"Party Line", "act3hanako", 100, 400), #somedude
                                 (4, "hanako"): (u"Mors Mortis", "act4hanako", 150, 250), #anonymouslurker
                                 (4, "hanatrue"): (u"Heterotic Strings", "act4hanatrue", 150, 250), #who the hell made this?
                                 (5, "hanatrue"): (u"Elucidation", "act5hanatrue", 350, 400), #same herepurpl
                                 (2, "lilly"): (u"Past", "act2lilly", 80, 170), #skim #Needs changing, maybe with Raide's child Lilly sketch
                                 (3, "lilly"): (u"Present", "act3lilly", 350, 400), #syureria
                                 (4, "lilly"): (u"Future", "act4lilly", 80, 170), #skim
                                 (2, "rin"): (u"Dream", "act2rin", 300, 220), #aura
                                 (3, "rin"): (u"Distance", "act3rin", 150, 230), #kekekeke
                                 (4, "rin"): (u"Difference", "act4rin", 200, 250), 
                                 (2, "shizune"): (u"Cat and Mouse", "act2shizune", 90, 90), #celiest
                                 (3, "shizune"): (u"Ellipsis", "act3shizune", 100, 400), #lild227
                                 (4, "shizune"): (u"Silent Voice", "act4shizune", 200, 250)
                                }
    # credits
    
    displayDict["ru"].creditstring = """{b}Сценарист{/b}
Aura
                                     
{b}Авторы{/b}
Anonymous22
cpl_crud
Suriko
TheHivemind

{b}Редакторы{/b}
Kagami
Losstarot
Silentcook

{b}Композиторы{/b}
Blue123
Nicol Armarfi

{b}Художники{/b}
Ambi07
gebyy-terar
Kamifish
moekki
Raide
raemz

{b}Дополнительные художники{/b}
climatic
Doomfest
yujovi

{b}Техническое обеспечение{/b}
delta

{b}Продюсеры{/b}
cpl_crud
Suriko

                                     
                                     

{b}Благодарность{/b}
Celiest
chendo
climatic
Dark_Mercury
DeuceTrick
frumplstlskn
Ismuth
Kagami
konflikti
Magaran
Moogy
OverCoat
Peorth
Petaru
skim
Solaris
silentkyon
stirfriedweasel
Syureria



{b}Отдельная благодарность{/b}
PyTom
KSG Threads on /vg/
RAITA




{b}Команда восстановления Преальфы{/b}
smspf
Alphabro
Kelper
Buttface
Aki <3
muffinduck01
Gift of Gab
Stan Riders


{b}Также помогли{/b}
Parity
BWildness
Twoface
Sapiens
cometodaddycome""" # <3 [str]

#smspf = shitty ms paint faggot 

    displayDict['ru'].drugs_wordlist = [ruw(u"Дизопирамид"),
                        ruw(u"Варфарин"),
                        ruw(u"Дилтиазем"),
                        ruw(u"Фелодипин"),
                        ruw(u"Пропранолол"),
                        ruw(u"Пенбутолол"),
                        ruw(u"Картеолол"),
                        ruw(u"Прокаинамид"),
                        ruw(u"Гепарин"),
                        ruw(u"Фенитоин"),
                        ruw(u"Верапамил"),
                        ruw(u"Хинидин"),
                        ruw(u"Флекаинид"),
                        ruw(u"5 мг/день"),
                        ruw(u"400 мг/день"),
                        ruw(u"15 мл/день"),
                        ruw(u"100 мг/день"),
                        ruw(u"10 мл/48 час"),
                        ruw(u"10 мл/день"),
                        ruw(u"200 мг/12 час"),
                        ruw(u"50 мг/12 час"),
                        ruw(u"500 мг/48 час"),
                        ruw(u"125 мг/12 час"),
                        ruw(u"25 мл/день"),
                        ruw(u"ночные кошмары"),
                        ruw(u"пониженное внимание"),
                        ruw(u"брадикардия"),
                        ruw(u"клиническая депрессия"),
                        ruw(u"бессонница"),
                        ruw(u"эректильная дисфункция"),
                        ruw(u"нарушение зрения"),
                        ruw(u"сердечное расстройство"),
                        ruw(u"тошнота"),
                        ruw(u"головокружение"),
                        ruw(u"галлюцинации"),
                        ruw(u"бронхоспазмы"),
                        ruw(u"одышка"),
                        ruw(u"утомляемость"),
                        ruw(u"гипотония"),
                        ruw(u"блокада сердца"),
                        ruw(u"озноб"),
                        ruw(u"диарея"),
                        ruw(u"остановка сердца"),
                        ruw(u"фибрилляция желудочков"),
                        ruw(u"атаксия"),
                        ruw(u"астма")]