init -2 python:
    ### ITALIAN
    
    init_language("it")

    displayDict["it"].timeformat = "%d/%m, %H:%M"
    
    displayDict["it"].activeLanguage = "Italiano"
    displayDict["it"].allLanguages = {}
    displayDict["it"].allLanguages["en"] = "Inglese"
    displayDict["it"].allLanguages["de"] = "Tedesco"
    displayDict["it"].allLanguages["it"] = displayDict["it"].activeLanguage
    displayDict["it"].allLanguages["jp"] = "Giapponese"
    displayDict["it"].allLanguages["ru"] = "Russo"
    
    displayDict["it"].act_term = u"Atto"
    displayDict["it"].window_name = u"Katawa Shoujo"
    
    displayDict["it"].main_menu_start = u"Inizia"
    displayDict["it"].main_menu_load = u"Carica"
    displayDict["it"].main_menu_extra = u"Extra"
    displayDict["it"].main_menu_config = u"Preferenze"
    displayDict["it"].main_menu_quit = u"Esci"

    displayDict["it"].game_menu_return = u"Indietro"
    displayDict["it"].game_menu_show = u"Mostra immagine"
    displayDict["it"].game_menu_history = u"Archivio testo"
    displayDict["it"].game_menu_skip = u"Modalità rapida"
    displayDict["it"].game_menu_auto = u"Autolettura"
    displayDict["it"].game_menu_config = u"Preferenze"
    displayDict["it"].game_menu_save = u"Salva"
    displayDict["it"].game_menu_load = u"Carica"
    displayDict["it"].game_menu_main = u"Menù iniziale"
    displayDict["it"].game_menu_quit = u"Esci"
    displayDict["it"].game_menu_current_scene = u"Scena corrente"
    displayDict["it"].game_menu_replay_indicator = u"Replay"

    displayDict["it"].return_button_text = u"Indietro"

    displayDict["it"].hdisabled_label = u"Disabilita contenuto adulto"
    displayDict["it"].config_page_caption = u"Preferenze"
    displayDict["it"].config_fullscreen_label = u'Modalità schermo intero'
    displayDict["it"].config_transitions_label = u'Disabilita transizioni'
    displayDict["it"].config_skip_unseen_label = u'Salta testo non letto'
    displayDict["it"].config_skip_after_choice_label = u'Continua a saltare testo dopo scelte'
    displayDict["it"].config_textspeed_label = u'Velocità testo'
    displayDict["it"].config_afmspeed_label = u'Intervallo autolettura'
    displayDict["it"].config_musicvol_label = u"Volume musica"
    displayDict["it"].config_musicvol_jukebox_label = u"Vol."
    displayDict["it"].config_sfxvol_label = u"Volume SFX"
    displayDict["it"].config_sfxtest_label = u"Prova"
    displayDict["it"].config_gamepad_label = u"Mappatura tasti gamepad…"

    displayDict["it"].config_language_sel = u"Selezione linguaggio…"
    displayDict["it"].config_language_caption = u"Preferenze > Selezione linguaggio"
    displayDict["it"].config_language_restart_note = u"Nota: Cambiare il linguaggio nel corso del gioco farà ripartire la corrente scena da un punto nodale."

    displayDict["it"].gamepad_caption = u"Preferenze > Mappatura tasti gamepad"
    displayDict["it"].gamepad_key_na = u"Non assegnato"
    displayDict["it"].gamepad_request_key = u"Premi il pulsante a cui vuoi assegnare “%s”.\nClicca il mouse o premi il pulsante SELECT per cancellare l' assegnazione."

    displayDict["it"].yesno_yes = u"Sì"
    displayDict["it"].yesno_no = u"No"
    displayDict["it"].yesno_okay = u"Continua"
    displayDict["it"].yesno_savesuccess = u"Gioco salvato con successo\ncome numero %s."
    displayDict["it"].yesno_quit = u"Vuoi davvero\nuscire da Katawa Shoujo?"
    displayDict["it"].yesno_return_to_main = u"Vuoi davvero tornare\nal menù principale?"
    displayDict["it"].save_page_caption = u"Salva"
    displayDict["it"].new_save_button = u"Crea nuovo salvataggio"
    displayDict["it"].load_page_caption = u"Carica"
    displayDict["it"].yesno_load_in_game = u"Vuoi davvero scartare\ni tuoi progressi?"
    displayDict["it"].yesno_save_overwrite = u"Vuoi davvero sovrascrivere\nil tuo salvataggio?"
    displayDict["it"].yesno_delete_savegame = u"Vuoi davvero cancellare\nil salvataggio numero %s?"
    displayDict["it"].play_time_label = u"Tempo di gioco"
    displayDict["it"].show_manual_saves = u"Manuale"
    displayDict["it"].show_auto_saves = u"Automatico"

    displayDict["it"].text_history_caption = u"Archivio testo"

    displayDict["it"].extra_menu_caption = "Extra"
    displayDict["it"].extra_music_button_label = "Jukebox"
    displayDict["it"].extra_gallery_button_label = "Galleria"
    displayDict["it"].extra_scene_button_label = "Biblioteca"
    displayDict["it"].extra_omake_button_label = "Omake"
    displayDict["it"].extra_opening_button_label = "Cinema"
    displayDict["it"].commentary_label = "Abilita commenti"

    displayDict["it"].music_page_caption = "Extra > Jukebox"
    displayDict["it"].music_stop_button_text = "Stop"
    displayDict["it"].music_now_playing = "In riproduzione"

    displayDict["it"].gallery_page_caption = "Extra > Galleria"
    displayDict["it"].gallery_onelocked = "Ancora un' immagine non sbloccata."
    displayDict["it"].gallery_manylocked = "Ancora %d altre immagini non sbloccate."
    displayDict["it"].gallery_singlelocked = "Immagine %d di %d non sbloccata."
    displayDict["it"].gallery_num_page_prefix = "Pagina "
    displayDict["it"].gallery_num_page_error = "Nessuna immagine da mostrare"

    displayDict["it"].scene_page_caption = "Extra > Biblioteca"
    displayDict["it"].scene_completion_label = "Completato: %s%%"
    displayDict["it"].scene_playthrough_label = "Torna indietro dopo la fine della scena (consigliato)"

    displayDict["it"].joy_left = "Sinistra"
    displayDict["it"].joy_right = "Destra"
    displayDict["it"].joy_up = "Alto"
    displayDict["it"].joy_down = "Basso"
    displayDict["it"].joy_dismiss = "Seleziona/Avanza"
    displayDict["it"].joy_rollback = "Archivio testo"
    displayDict["it"].joy_holdskip = "Tieni premuto per saltare"
    displayDict["it"].joy_toggleskip = u"Modalità rapida"
    displayDict["it"].joy_hide = "Mostra immagine"
    displayDict["it"].joy_menu = u"Mostra menù"

    ##Names

    displayDict["it"].name_ha_ = 'Ragazza dai capelli viola'
    displayDict["it"].name_emi_ = 'Ragazza coi codini'
    displayDict["it"].name_rin_ = 'Strana ragazza'
    displayDict["it"].name_li_ = 'Ragazza bionda'
    displayDict["it"].name_mi_ = 'Ragazza che ride'
    displayDict["it"].name_ke_ = 'Vicino occhialuto'
    displayDict["it"].name_mu_ = 'Uomo alto'
    displayDict["it"].name_yu_ = 'Bibliotecaria'
    displayDict["it"].name_no_ = 'Uomo dai capelli argentei'
    displayDict["it"].name_sa_ = 'Gallerista'
    displayDict["it"].name_aki_ = 'Persona ben vestita'
    displayDict["it"].name_nk_ = 'Uomo sorridente'
    displayDict["it"].name_hx_ = "Padre di Shizune"
    displayDict["it"].name_hh_ = "Ragazza magra"
    displayDict["it"].name_emm_ = "Madre di Emi"

    # Scenes available in the extras -> scene select menu. Name, label, description, path (path may also be a tuple).
    # Now also doubles as a lookup list for the actual scene names. Display in the extras can be suppressed
    # by setting the third value in the tuple to False. Suppression doesn't work in DQN mode.
    # Note that Ren'Py doesn't like non-ASCII characters in scene titles if the titles are not unicode strings
    displayDict["it"].s_scenes = (("Congelato", "NOP1", "Durante un giorno freddo e nevoso, i sogni di Hisao stavano per essere realizzati, solo per essere stroncati da un improvviso attacco di cuore.", "Act 1"), # NEW ACT 1
                                    ("Fascio di Hisao", "NOP2", "Hisao viene a sapere dell' Accademia Yamaku, dove probabilmente passerà il resto dei suoi giorni di scuola superiore.", "Act 1"),
                                    (u"Cominciare è Facile", "A1", "Hisao entra all' Accademia Yamaku per la prima volta, e incontra il suo insegnante di riferimento, Mutou.", "Act 1"),
                                    ("Entrata, Sinistra Palco", "A2", "Presentazioni alla classe, e incontro con la capoclasse e la sua interprete.", "Act 1"),
                                    ("Nella Nursery", "A3", "Misha e Shizune mostrano la mensa a Hisao, dopodichè lui va a incontrare l' infermiere.", "Act 1"),
                                    ("Stanza di Nessuno", "A4", "Hisao si trasferisce nella sua nuova stanza, incontrando il suo vicino Kenji nel processo.", "Act 1"),
                                    ("Chiacchiere", "A5", "Shizune e Misha parlano a Hisao del prossimo festival e lo invitano a pranzo.", "Act 1"),
                                    ("Chi Non Risika Non Rosica", "A6", "Shizune e Hisao si combattono per il mondo in una partita di Risiko.", "Act 1"),
                                    ("Pseudocopriteiera", "A7", "In cerca della biblioteca, Hisao si perde e trova Lilly in un' aula in disuso.", "Act 1"),
                                    ("Biblioteca Condivisa", "A8", "Trovando finalmente la biblioteca, Hisao incontra e spaventa Hanako.", "Act 1"),
                                    ("Bizzarro e Surreale", "A9", "Kenji rivela gli oscuri segreti di Yamaku.", "Act 1"),
                                    ("Teoria d' Evoluzione del Pranzo", "A10", "Shizune e Misha insistono perchè Hisao si unisca al Consiglio Studentesco prima di discutere il pranzo.", "Act 1"),
                                    ("Impatto Improvviso", "A11_1", "Andando a pranzo con Misha e Shizune, Hisao collide con Emi nel corridoio.", "Act 1"),
                                    ("Adorabile Scontro", "A11_2", "Hisao collide con una irruenta Emi mentre sta andando a pranzo con Hanako e Lilly.", "Act 1"),
                                    ("Deviazione", "A12", "Shizune e Misha portano Hisao alla loro sala da tè preferita, lo Shangai.", "Act 1"),
                                    ("Assaggio (parte 1)", "A13", "Hisao pranza tranquillamente con Lilly e Hanako.", "Act 1"), # there is no A14
                                    ("Costruisce Carattere", "A15", "Mutou cerca di avere una discussione seria con Hisao, ma Misha li interrompe e mette Hisao al lavoro.", "Act 1"),
                                    ("Un Pranzo Privato", "A16", "Cercando dei materiali, Hisao incontra per caso una strana ragazza nell' aula di belle arti.", "Act 1"),
                                    ("Imboscata", "A17", "Mentre aiuta Rin a trasportare della vernice, Hisao viene interrogato dall' infermiere.", "Act 1"),
                                    ("L' Altro Verde", "A18", "Hisao guarda Rin dipingere il suo murale.", "Act 1"),
                                    ("La Ragazza che Correva", "A19", "Mentre tenta di fare un po' di esercizio mattutino, Hisao incontra Emi alla pista di atletica.", "Act 1"),
                                    ("Sapone", "A20", "Kenji tende un' imboscata a Hisao nelle docce in un tentativo di procurarsi dei soldi.", "Act 1"), 
                                    ("Guerra Fredda", "A21", "Shizune e Lilly si scontrano su delle richieste di finanziamento.", "Act 1"),
                                    ("Prova di Competenza", "A22", "Shizune e Misha assaltano Hisao in un tentativo di farlo unire al Consiglio Studentesco.", "Act 1"),
                                    ("Orizzonte Degli Eventi", "A22_2", "Shizune e Misha assaltano Hisao in un tentativo di farlo unire al Consiglio Studentesco.", "Act 1"),
                                    ("Oltre il Proprio Dovere", "A23_1", "Hisao si sorbisce una lezione sui nobili doveri di un Consiglio Studentesco.", "Act 1"),
                                    ("Cose che Puoi Fare", "A23_2", "Dopo essere sfuggito alle grinfie di Shizune e Misha, Hisao aiuta nuovamente Rin.", "Act 1"),
                                    ("Colorare Negli Spazi", "A24", "Hanako e Hisao danno una mano alla classe di Lilly offrendosi di aiutare a costruire il loro chiosco.", "Act 1"),
                                    ("Esercizio", "A25", "Un' altra mattina presto vede Hisao correre alla pista con Emi.", "Act 1"),
                                    ("Cappello Invisibile", "A26", "Kenji dà a Hisao alcuni consigli su come socializzare.", "Act 1"),
                                    ("Vantaggio Degli Ospiti", "A26_1", "Shizune e Misha intercettano Hisao mentre lascia la sua stanza per andare a lezione.", "Act 1"),
                                    ("Lento Recupero", "A27_1", "Recuperando dal suo attacco, Hisao finalmente riesce ad arrivare in aula.", "Act 1"),
                                    ("Nessun Recupero", "A27_2", "Hisao lotta per andare in classe dopo essere stato intercettato dal Consiglio Studentesco.", "Act 1"),
                                    (u"Niente è Gratuito", "A28", "Hisao viene scortato nell' ufficio del Consiglio Studentesco per la sua prima giornata ufficiale di lavoro.", "Act 1"),
                                    ("Fatto coi Piedi", "A29", "Emi trascina Hisao fino al tetto per pranzare insieme a lei e Rin.", "Act 1"),
                                    ("Attento a Dove Vai", "A30", "Hisao e Lilly vanno a far compere, incontrando una Rin molto confusa sulla via del ritorno.", "Act 1"),
                                    ("Sostegno", "A31", "Hisao riceve la sua prima lezione di sabato, completa di una ramazina da Mutou.", "Act 1"),
                                    ("In Estetica", "A32", "Emi trova Hisao a far niente dopo le lezioni e lo recluta ancora una volta per aiutare Rin.", "Act 1"),
                                    ("Dolori Creativi", "A33", "Hisao incontra l' insegnante di belle arti, Nomiya, mentre Rin dipinge il suo murale.", "Act 1"),
                                    ("Esercizio Salutare", "A34", "Emi e Hisao discutono l' importanza di essere in forma.", "Act 1"),
                                    ("Assaggio (parte 2)", "A35", "In un tentativo di passare il tempo, Hisao fa una camminata per la scuola.", "Act 1"),
                                    ("Shangaiato", "A36", "Tè, dolci e competizioni con Shizune e Misha allo Shangai.", "Act 1"),
                                    ("Quiete", "A37", "Hanako e Hisao leggono libri per il festival.", "Act 1"),
                                    ("Niente Panico", "A38", "Dopo essersi svegliato durante il giorno del festival, Hisao viene salutato da un blaterante Kenji.", "Act 1"),
                                    ("Carnevale!", "A39", "Emi scopre Hisao a mangiare del cibo fritto, e lo obbliga a scortarla per punizione.", ("Act 1", "Emi")),
                                    ("Nuvole nella Mia Testa", "A40", "Hisao fa compagnia a Rin e al suo ormai terminato murale.", ("Act 1", "Rin")),
                                    ("Promessa di Tempo", "A41", "Dopo una dura giornata al suo chiosco, Hisao assiste Lilly a trovare Hanako.", ("Act 1", "Lilly")),
                                    ("Nc5xb3", "A42", "Incapace di aiutare Lilly al suo chiosco, Hisao cerca Hanako durante il festival.", ("Act 1", "Hanako")),
                                    ("Altamente Conclusivo", "A43", "Kenji e Hisao condividono un virile picnic sul tetto invece di andare al festival.", "Act 1"),
                                    ("Tirando Palle", "A44", "Mantenendo la sua parola, Hisao passa la giornata con Shizune e Misha.", ("Act 1", "Shizune")),
                                    )

    # TITLE CARDS
    # Definition. This maps an id tuple to a tuple of displayed text, filename modifier, and the position of said text.
    # the display function is tcard() in ui_code.rpy
    displayDict["it"].act_names = {(1, "all"): ("Durata della Vita", "act1", 190, 117), #lulz
                                    }
    # credits

    displayDict["it"].creditstring  = """{b}Scrittore Capo{/b}
Aura

{b}Scrittori{/b}
Anonymous22
cpl_crud
Suriko
TheHivemind

{b}Editori{/b}
Kagami
Losstarot
Silentcook

{b}Musica{/b}
Blue123
Nicol Armarfi

{b}Artisti{/b}
Ambi07
gebyy-terar
Kamifish
moekki
Raide
raemz

{b}Artisti addizionali{/b}
climatic
Doomfest
yujovi

{b}Programmatore{/b}
delta

{b}Traduttore{/b}
Silentcook

{b}Produttori{/b}
cpl_crud
Suriko



{b}Ringraziamenti{/b}
Anonymous
Celiest
chendo
climatic
Dark_Mercury
DeuceTrick
frumplstlskn
Ismuth
Kagami
kekekeke
konflikti
lulz
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
TcDohl
thalidomidegirl

{b}Ringraziamenti Speciali{/b}
PyTom
RAITA
KSG Threads on /vg/


{b}Prealpha Repair{/b}
smspf
Alphabro
Kelper
Buttface
Aki <3
muffinduck01
Gift of Gab
Stan Riders

                                     
{b}Also Helped{/b}
Parity
BWildness
Twoface
Sapiens
cometodaddycome"""

#smspf = shitty ms paint faggot 

    displayDict["it"].drugs_wordlist  =  ["Disopiramide",
                        "Warfarin",
                        "Diltiazem",
                        "Felodipina",
                        "Propanololo",
                        "Penbutololo",
                        "Carteololo",
                        "Procainamide",
                        "Eparina",
                        "Fenitoina",
                        "Verapamil",
                        "Quinidina",
                        "Flecainide",
                        "5mg/die",
                        "400mg/die",
                        "15ml/die",
                        "100mg/die",
                        "10ml/48ore",
                        "10ml/die",
                        "200mg/12ore",
                        "50mg/12ore",
                        "500mg/48ore",
                        "125mg/12ore",
                        "25ml/die",
                        "incubi",
                        "cali di concentrazione",
                        "bradicardia",
                        "depressione clinica",
                        "insonnia",
                        "disfunzione erettile",
                        "alterazioni del visus",
                        "arresto cardiaco",
                        "nausea",
                        "vertigini",
                        "allucinazioni",
                        "broncospasmo",
                        "dispnea",
                        "stanchezza",
                        "ipotensione",
                        "blocco cardiaco",
                        u"estremitá fredde",
                        "diarrea",
                        "arresto cardiaco",
                        "fibrillazione ventricolare",
                        "atassia",
                        "asma"]
