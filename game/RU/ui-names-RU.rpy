init -3 python:
    ### hepb/poli switching
    ### некоторые строки используют ruw(...) из-за неправильного отображения в меню [str]
    
    if not persistent.runamings:
        persistent.runamings = "poli" # Поливанов включается по умолчанию. [str]
    
    if persistent.runamings == "poli":
        name_hicchan = u"Хиттян"
        name_sicchan = u"Ситтян"
        name_shizune = ruw(u"Сидзунэ")
        name_kenji = ruw(u"Кендзи")
        name_sae = ruw(u"Саэ")
        name_jigoro = ruw(u"Жигоро")
        name_tatibana = u"Татибана"
        name_ibarazaki = u"Ибарадзаки"
        name_ikezawa = u"Икэдзава"
        name_tezuka = u"Тэдзука"
        name_hakamichi = u"Хакамити"
        name_shiraki = u"Сираки"
        name_shinichi = u"Синити"
        name_saionji = u"Сайондзи"
        name_uchan = u"Ю-тян"
        
    if persistent.runamings == "hepb":
        name_hicchan = u"Хиччан"
        name_sicchan = u"Шиччан"
        name_shizune = ruw(u"Шизуне")
        name_kenji = ruw(u"Кенджи")
        name_sae = ruw(u"Сае")
        name_jigoro = ruw(u"Джигоро")
        name_tatibana = u"Тачибана"
        name_ibarazaki = u"Ибаразаки"
        name_ikezawa = u"Икезава"
        name_tezuka = u"Тезука"
        name_hakamichi = u"Хакамичи"
        name_shiraki = u"Шираки"
        name_shinichi = u"Шиничи"
        name_saionji = u"Сайонджи"
        name_uchan = u"Ю-чан"