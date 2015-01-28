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
                                    )
                                    # removed until translated [str]

# TITLE CARDS
    # Definition. This maps an id tuple to a tuple of displayed text, filename modifier, and the position of said text.
    # the display function is tcard() in ui_code.rpy
    
    # dont forget ruw(u"...")
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
                                 (2, "lilly"): (ruw(u"Прошлое"), "act2lilly", 80, 170), #skim #Needs changing, maybe with Raide's child Lilly sketch
                                 (3, "lilly"): (ruw(u"Настоящее"), "act3lilly", 350, 400), #syureria
                                 (4, "lilly"): (ruw(u"Прошлое и Настоящее"), "act4lilly", 80, 170), #skim
                                 (5, "lilly"): (ruw(u"Будущее"), "act4lilly", 80, 170), # volvo giv art pls
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