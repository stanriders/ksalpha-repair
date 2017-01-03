init -3 python:
    ### hepb/poli switching
    ### некоторые строки используют ruw(...) из-за неправильного отображения в меню [str]
    
    if not persistent.runamings:
        persistent.runamings = 'poli' # Поливанов включается по умолчанию. [str]
    
    def switch_runaming():
        # python is kinda strange [str]
        global displayStrings, name_hicchan, name_sicchan, name_shizune, name_kenji, name_sae, name_jigoro, name_tatibana, name_ibarazaki, name_ikezawa, name_tezuka, name_hakamichi, name_shiraki, name_shinichi, name_saionji, name_uchan, name_hanachan, name_shirakawa, name_shiina, name_shizukichi, name_shii, name_shii_sha, name_shi_chi_shii_sha, name_shichishiisha, name_shizu, name_shizuchan, name_takahashi, name_yamato_nadeshiko, name_hideaki, name_kojiro, name_mizuki, name_musashi, name_yoshida, name_kashiwagami, name_kenji_caps, name_shin, name_kuzuhara
        if persistent.runamings == 'poli':
            name_hicchan = u"Хиттян"
            name_sicchan = u"Ситтян"
            name_shizune = u"Сидзунэ"
            name_kenji = u"Кендзи"
            name_kenji_caps = u"КЕНДЗИ"
            name_hideaki = u"Хидэаки"
            name_sae = u"Саэ"
            name_jigoro = u"Дзигоро"
            name_ibarazaki = u"Ибарадзаки"
            name_ikezawa = u"Икэдзав"
            name_tezuka = u"Тэдзук"
            name_hakamichi = u"Хакамити"
            name_shiraki = u"Сираки"
            name_shinichi = u"Синити"
            name_saionji = u"Сайондзи"
            name_uchan = u"Ю-тян"
            name_hanachan = u"Хана-тян"
            name_shirakawa = u"Сиракава"
            name_shiina = u"Сиина"
            name_shizukichi = u"Сидзукити"
            name_shii_sha = u"Сии…са"
            name_shi_chi_shii_sha = u"Си…ти…сии…са"
            name_shichishiisha = u"Ситисииса"
            name_shizu = u"Сидзу"
            name_shizuchan = u"Сидзу-тян"
            name_takahashi = u"Такахаси"
            name_yamato_nadeshiko = u"ямато-надэсико"
            name_kashiwagami = u"Касивагами"
            name_yoshida = u"Ёсида"
            name_musashi = u"Мусаси"
            name_kojiro = u"Кодзиро"
            name_mizuki = u"Мидзуки"
            name_shin = u"Син"
            name_kuzuhara = u"Кудзухара"
        else:
            name_hicchan = u"Хиччан"
            name_sicchan = u"Шиччан"
            name_shizune = u"Шизуне"
            name_kenji = u"Кенджи"
            name_kenji_caps = u"КЕНДЖИ"
            name_hideaki = u"Хидеаки"
            name_sae = u"Сае"
            name_jigoro = u"Джигоро"
            name_ibarazaki = u"Ибаразаки"
            name_ikezawa = u"Икезав"
            name_tezuka = u"Тезук"
            name_hakamichi = u"Хакамичи"
            name_shiraki = u"Шираки"
            name_shinichi = u"Шиничи"
            name_saionji = u"Сайонджи"
            name_uchan = u"Ю-чан"
            name_hanachan = u"Хана-чан"
            name_shirakawa = u"Ширакава"
            name_shiina = u"Шиина"
            name_shizukichi = u"Шизукичи"
            name_shii_sha = u"Шии…ша"
            name_shi_chi_shii_sha = u"Ши…Чи…Шии…ша"
            name_shichishiisha = u"Шичишииша"
            name_shizu = u"Шизу"
            name_shizuchan = u"Шизу-чан"
            name_takahashi = u"Такахаши"
            name_yamato_nadeshiko = u"ямато-надешико"
            name_kashiwagami = u"Кашивагами"
            name_yoshida = u"Йошида"
            name_musashi = u"Мусаши"
            name_kojiro = u"Коджиро"
            name_mizuki = u"Мизуки"
            name_shin = u"Шин"
            name_kuzuhara = u"Кузухара"
        
        displayDict['ru'].name_shi = ruw(name_shizune) # hepb/poli switching
        displayDict['ru'].name_ke = ruw(name_kenji) # hepb/poli switching
        displayDict['ru'].name_sa = ruw(name_sae) # hepb/poli switching
        displayDict['ru'].name_hx = ruw(name_jigoro) # hepb/poli switching
        displayDict['ru'].name_hx_ = (u"Отец ") + (name_shizune) # hepb/poli switching
        displayDict['ru'].name_hh = ruw(name_hideaki) # hepb/poli switching

        
        return True;

    
