label it_A25:

play sound sfx_alarmclock

scene bg school_dormhisao
with openeye

"La mia sveglia scatta, e io mi agito inutilmente per un po' finchè non mi ricordo di aver deciso di concedere una seconda possibilità al correre di mattina."

"Non so se sia una delle mie migliori idee, ma sono deciso a insistere."

"Questo riguarda la mia salute, dopotutto."

"Certo, le cose non sono andate al meglio di recente, ma quello non ha reso la mia esistenza così intollerabile da non volermi fare tentare tutto quel che posso per restare sano."

"E poi, pende tutto sull' asserire un poco di controllo su questa cosa, giusto?"

"Se riesco a farlo, bene, posso fare qualunque cosa."

"O almeno è quello che continuo a ripetermi."

scene bg school_track
with locationskip

play music music_emi fadein 0.3

play ambient sfx_emirunning fadein 0.3

"Ancora una volta, sembra che non sia solo a correre."

"Emi apparentemente è già arrivata da un po' di tempo."

"Sembra che si sia già riscaldata a dovere."

"A che cavolo di ora scende in pista, comunque?"

stop ambient fadeout 1.0

show emi basic_grin_gym
with charaenter

emi "Oh, sei tu!"

show emi basic_closedgrin_gym
with charaenter

emi "Sono sorpresa di rivederti!"

hi "E perchè?"

show emi basic_grin_gym
with charaenter

emi "Bè, non molti riescono veramente a tornare per un secondo tentativo."

show emi basic_annoyed_gym
with charaenter

"Fa una smorfia, apparentemente infastidita da un pensiero di passaggio."

emi "Come il resto della squadra di atletica, per esempio."

emi "Però, si supponeva che fosse su una base volontaria, così non è poi un grosso shock."

emi "E suppongo che sia piuttosto presto di mattina…"

"Scrolla le spalle, e improvvisamente sembra che abbia dimenticato di cosa stava parlando."

show emi basic_happy_gym
with charaenter

"La smorfia sparisce interamente, e sembra tornare improvvisamente al suo precedente filo di pensieri."

emi "E così! Muoviti, dunque!"

hi "Cosa?"

show emi excited_proud_gym
with charaenter

emi "Sei qui per correre di nuovo, giusto?"

hi "Beh, sì."

show emi basic_closedhappy_gym
with charaenter

emi "Allora muoviti!"

scene bg school_track_on
with locationchange

"Mi ritrovo a essere improvvisamente afferrato e tirato sulla pista."

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange

"Le cose sembrano duplicare la corsa di ieri."

"Cioè, io sembro lottare, mentre Emi si muove con una spontaneità che trovo invidiabile."

"E' incredibilmente seccante, diventare esausto così facilmente."
    
"So che dovrei essere paziente, procedere gradualmente, ma…"

"E' difficile rimanere positivi."
    
"Passiamo la curva e iniziamo il nostro secondo giro."

play ambient sfx_emirunning

"Emi sembra essersi spazientita di tenere il mio passo, e comincia ad accelerare."

"E' qui che ho ceduto ieri."



label it_choiceA25:
menu:
    with menueffect

    "Riuscirò a fare di più?"

    "Facciamo uno sforzo.":
        return m1

    "Prendiamocela comoda.":
        return m2

label it_A25a:
    
# if C72

"Lascio che Emi vada al suo passo, e lei non mostra pietà, guadagnando mezzo giro di vantaggio in un istante."

"Non posso biasimarla."

"Voglio dire, non è come se stessi davvero provvedendo una qualche sorta di vera competizione, no?"

"Invece, sto solo correndo a un passo regolare, che è quello che dovrei stare facendo, giusto?"

"Non c'è bisogno di provare a oltrepassare i miei limiti a questo stadio delle cose."

"Dio, ma ne vale poi la pena?"

scene bg school_track_on
with locationchange

"Quando finiamo il secondo giro, mi stacco di nuovo."

"Emi continua a correre, e quasi mi sembra che sia delusa."

"Beh, è stupido."

"Non ho niente da provarle — ora che ci penso, non ho niente da provare neanche a me stesso."

"Vado bene così come sono."

"E un corridore è quello che non sono."

"Probabilmente questa è stata una cattiva idea."

"Forse c'è qualcos' altro che posso fare invece di questo."

"Alzarsi presto è una rottura, comunque. Ci deve essere un' altra maniera di stare in salute."

"Camminare, forse. Belle passeggiate pomeridiane."

"Già, suona bene. All' inferno questa stupidaggine del correre."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene bg school_track
with locationchange

"Saluto Emi e torno nella mia stanza."
    
"Penserò a qualcos' altro più tardi."


    
#if C71

label it_A25b:

"Cosa sto facendo qui?"

"Voglio veramente cedere e lasciare che Emi mi sorpassi?"

scene bg school_track_running
with locationchange

"Accelero."

"Il secondo giro termina in fretta, e senza nemmeno considerarlo continuo ad andare avanti."

"Emi mi guarda da sopra la sua spalla e sogghigna."

show emi excited_proud_gym at twoleft
with charaenter

emi "Ce la fai?"

hi "Non *pant* vorrei che *pant* pensassi che sono fuori forma *pant*"

show emi excited_laugh_gym at twoleft
with charachange

hide emi
with charamoveoutleft

play ambient sfx_emipacing

"Emi ride — senza perdere il ritmo, tra l' altro — e accelera ancora di più."

"Bene, se è così che vogliamo giocare…"

"Anche io accelero il mio passo."
    
"Posso sentire i miei polmoni che bruciano, e le mie gambe stanno iniziando a chiedere cosa cavolo credo di stare facendo."
    
"L' acido lattico urla nei miei muscoli, ma faccio il sordo."

"Non posso permettermi di restare indietro, perchè quello significherebbe perdere."

"La voce razionale nel mio cervello chiede tranquillamente quando esattamente abbiamo iniziato la partita a questo gioco."

"Gli risponderei, ma sto avendo un sacco di problemi a pensare in questo momento."

"Lei è talmente {b}veloce{/b}."

"Come diavolo fa a mantenere—{w=.5}{nw}"

stop music fadeout 0.2

#Heart attack thuds start here
play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"E' come un filo che tira il mio torace, una sensazione soffocante di strettezza e dolore."

"Prima che possa pensare qualunque cosa eccetto “Oh merda”, la pista sparisce da sotto i miei piedi."

scene bg school_track_on at RotoZoom(0,-6,0.1,1.0,1.2,0.1, xalign=0.5, yalign=0.52)
with vpunch

"Inciampo, una mano che scatta per stringermi il petto, l' altra che colpisce la pista per impedirmi di cadere di faccia."

stop ambient fadeout 0.2

"Emi si gira di scatto e i suoi occhi si spalancano."

emi "Hisao!"

play ambient sfx_emisprinting

"Mi urla contro, sprintando dall' altro capo della pista."

show emi basic_shock_gym at RotoZoom(-6,-6,0,1.2,1.2,0, xalign=0.5, yalign=0.7)
with charamoveinright

stop ambient fadeout 0.1

emi "Cosa c'è che non va?"

hi "Nngh—Nulla, solo…"

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Respira ritmicamente."

"Calmati. Niente panico."

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Niente panico."

show emi basic_shock_gym at RotoZoom(-6,-12,0.2,1.2,1.5,0.2, xalign=0.5, yalign=0.7)
with None

show emi basic_hes_gym at RotoZoom(-6,-12,0.2,1.2,1.5,0.2, xalign=0.5, yalign=0.7)
with charachange

emi "Devo andare a chiamare l' infermiere?"

show black
with shuteyefast

scene black
with None

"Chiudo gli occhi, escludendo il mondo esterno."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.3)

with Pause(1.0)

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)

"Il mio cuore lotta per riguadagnare il ritmo."

"Lentamente, il dolore nel mio petto comincia a diminuire."

"Presto è sparito come se non ci fosse mai stato."

play music music_rain fadein 0.3

"Non è stato… nulla? No, qualcosa è successo."

scene bg school_track_on
show emi basic_hes_gym_close
with openeye

"Apro di nuovo i miei occhi e vedo una Emi molto preoccupata."

hi "Credo di stare bene."

"La mia voce sembra strana anche a me, bizzarramente tranquilla e normale. Fa sì che Emi si rabbui."

show emi sad_annoyed_gym_close
with charachange

emi "Io non credo."

"Sembra giungere a una decisione, e china la testa in assenso con se stessa."

show emi basic_annoyed_gym_close
with charachange

emi "Va bene. Tu ora vieni con me."

emi "Devi vedere l' infermiere."

with vpunch

"Emi mi prende per un braccio e mi tira su. Mi sento un po' traballante, ma rifiuto la spalla che Emi mi offre come appoggio."

"Onestamente, mi vergogno un po' della mia debolezza."

"Preferirei davvero che Emi non si preoccupasse per me anche se sembra che sia troppo tardi."

"Che diavolo, preferirei davvero che nessuno si preoccupasse per le mie condizioni, anche se a questo punto, pure quello sembra essere troppo tardi."

"Mi piacerebbe essere in grado di trattare l' intero affare da solo, senza essere un problema per nessuno."

"E già che sto desiderando cose, preferirei in primo luogo non avere questo problema di salute."

scene bg school_nurseoffice at bgleft
with locationskip

show emi basic_shock_gym at tworight
with easeinright

emi "Infermiere!"

"Emi irrompe nel suo ufficio senza bussare, ma questo non allarma minimamente l' infermiere."

show nurse grin at twoleft
with charaenter

nk "Buongiorno, bellezza. Che c'è?"

"Bellezza? Comunque, sorseggia tranquillamente dalla sua tazza di caffè ma la appoggia dopo aver seguito lo sguardo di Emi fino alla mia figura profilata nella porta."

show nurse fabulous at twoleft
with charachange

nk "Hisao? Cosa ti porta qui?"

show emi excited_sad_gym at tworight
with charachange

emi "Stavamo correndo ed è inciampato e ha cominciato a stringersi il petto e ho pensato di venire a prenderti e farlo aspettare lì ma ha detto che stava bene però dopo ho pensato che avresti dovuto vederlo comunque e—{w=1.5}{nw}"

show nurse concern at twoleft
with charachange

nk "Piano, Emi. Calmati."

show nurse neutral at twoleft
with charachange

nk "Hisao, cosa è successo?"

hi "Non lo so. Stavamo correndo, e il mio torace ha iniziato a farmi male come quella volta, ma dopo pochi secondi è sparito tutto."

hi "E' stato solo un pò' di batticuore o qualcosa del genere."

show nurse concern at twoleft
with charachange

"L' infermiere fa una smorfia, come per dire che “solo un po' di batticuore” è una specie di ossimoro."

nk "Non intendevo proprio questo quando ti ho suggerito di fare un po' di esercizio. Devi stare più attento, Hisao."

hi "Ero attento, stavo solo…"

"Ora che ci penso, “stavo solo facendo a gara con un membro della squadra di atletica” non sembra un ragionamento valido quanto credevo prima."

nk "Stavi solo cosa?"

hi "Ehh… cioè…"

hi "Stavo gareggiando con Emi."

nk "Emi, è la verità?"

show emi basic_hes_gym at tworight
with charachange

"Emi giocherella con le sue mani, apparendo adorabilmente contrita."

emi "Um, bè…"

show emi basic_closedsweat_gym at tworight
with charachange

"Alla fine non sembra essere capace di dirlo forte, e fa solo segno di sì."

"L' infermiere sospira e si strofina stancamente la fronte con una mano."

nk "Emi, devi essere più sensibile ai limiti degli altri!"

nk "Non so se te l' ha detto, ma Hisao ha dei problemi di cuore, e farlo gareggiare con te è stato incredibilmente irresponsabile."

hi "Ehh, a dire il vero sono io che ho cominciato."

stop music fadeout 0.5

"L' infermiere rimane sbalordito dalla mia affermazione."

nk "Tu COSA?"

hi "Stavamo solo correndo, ed Emi ha cominciato a lasciarmi indietro, e così io uh, ho accelerato per raggiungerla."

"L' infermiere guarda verso il soffitto, mormora una preghiera per la pazienza a un qualche dio, e riabbassa lo sguardo su di noi."

nk "Così siete {b}entrambi{/b} stupidi."

nk "E' un conforto, immagino."

nk "Ora seguimi, Hisao. Devo assicurarmi che il tuo cuore non stia per esplodere o qualcosa del genere."

show bg school_nurseoffice at left
show nurse concern
show emi basic_closedsweat_gym at offscreenright
with charamove

"Obbediente seguo l' infermiere nella stanza adiacente dove accertiamo che in effetti, non sto per cadere a terra morto."

nk "Così cosa ti senti?"

hi "Non lo so. Niente di speciale. Stanco, ma potrebbe essere solo l' esercizio fisico."
    
nk "Dovresti rimanere qui per qualche ora a riposare, e vedremo come ti senti dopo di quello."

"Non ho intenzione di obiettare, così mi corico sul letto dell' infermeria."

scene bg school_nurseoffice at left
with shorttimeskip

"Una Emi assolutamente miserabile entra dopo aver ricevuto una ramanzina dall' infermiere nell' altra stanza."

"Non ho capito cosa ha detto attraverso la porta chiusa, ma sono sicuro che non siano stati dei complimenti."

show emi sad_depressed_gym
with charaenter

play music music_dreamy fadein 0.3

emi "Ascolta, mi dispiace davvero, davvero tanto."

emi "Avrei dovuto stare più attenta."

hi "Ehi, non lo sapevi. Non è colpa tua."

"Sembra terribilmente giù e spiacente, e le mie rassicurazioni non fanno granchè per rallegrarla."

emi "Voglio farmi perdonare."

"Di nuovo quel cenno deciso."

show emi sad_shy_gym
with charachange

emi "Così devi venire a pranzo con me."

emi "Te lo porterò io, okay? Qualcosa di davvero davvero buono!"

"Comincio a dire “Non c'è bisogno che…” ma poi chiudo il becco e le faccio solo cenno di sì quando vedo il suo viso."

show emi excited_proud_gym
with charachange

emi "Bene!"

show emi basic_grin_gym
with charachange

emi "Ci incontriamo tutti sul tetto."

hi "Tutti?"

show emi basic_closedgrin_gym
with charachange

emi "Yep! Adesso il tempo è bello, così il tetto è un ottimo posto per pranzare, sai."

hi "Capisco."

show emi sad_shy_gym
with charachange

emi "Verrai, vero?"

emi "Non mi rifiuteresti mai la possibilità di farmi perdonare, vero?"

hi "Certo che no."

show emi excited_joy_gym
with charachange

emi "Grande! Ci vediamo lì!"

stop music fadeout 3.0

hide emi
with charaexit

#edit end of A25 for Hisao to stay at NK's office to rest for an hour or two -done
scene bg school_nurseoffice at left
with shorttimeskip

"Fluttuo in uno stato a metà tra addormentato e sveglio, sentendomi completamente privo di energie."

"Non solo il mio corpo, ma tutto di me è molle e paralizzato, a parte i miei sensi."

"Inghiotto con difficoltà e poi cerco di rimanere quanto più fermo posso, che in questo stato non è una cosa molto difficile."

"L' infermiere sta trafficando dall' altro lato delle tende che ha tirato per darmi un po' di privacy. Posso vedere la sua ombra spostarsi nella luce del sole."

"Ha aperto la finestra del suo ufficio. C'è vento fuori."

"Le tende bianche e pulite ondeggiano nella brezza con un moto pigro e pesante, come onde. La luce filtra attraverso di loro lentamente, mezza assorbita dalla stoffa."

scene darkgrey
with shuteye

"Chiudo gli occhi. La brezza sulla mia faccia è come la soffice stoffa delle tende."

"Ascolto il battito del mio cuore per un momento, cercando di isolarmi dal suono dell' infermiere che traffica al suo computer, e dal mio respiro pesante."

"E' regolare."

"Dannazione, neanche una settimana e finisco di nuovo così. Stavolta ho proprio combinato un casino. Avrei dovuto pensarci prima di giocare allo sportivo dilettante di fronte a una professionista."

"E perchè ho provato di fare il coraggioso, come se quel battito al cuore non fosse niente di che, anche quando era ovvio che lo era?"

"E' stato solo un riflesso, per spingerlo via, per tenerlo dentro."

"Non volevo che succedesse."

"Non volevo che Emi lo vedesse."

"Aaah…"

"Stupidostupidostupido."

"Devo stare più attento, o finirò di nuovo in ospedale, o peggio."

"…"

"Quello è il mio ultimo pensiero prima di cedere alla stanchezza."

scene black
with Dissolve(1.0)

window hide Dissolve(2.0)

with Pause(2.0)

scene bg school_nurseoffice at left
with openeye

window show

"Mi sono addormentato. Per quanto tempo? Che ore sono?"

"Mi sento un poco stordito e continuo a sbattere le palpebre compulsivamente."

show bg school_nurseoffice
with charamove

"Spingendo da parte la tenda, strizzo gli occhi contro la nuda luce che mi inonda dalla finestra. La trama della stoffa non assomiglia affatto a come era il vento prima."

play music music_normal fadein 0.3

"L' infermiere alza gli occhi dal suo lavoro, seduto esattamente dove era prima."

show nurse fabulous
with charaenter

nk "Come ti senti?"

"Non saprei proprio dire, così non rispondo nulla. Mi sento un po' insonnolito per essermi addormentato a un orario così strambo, spero di non sembrare troppo strano."

hi "Che ore sono?"

"Io che gracchio la domanda per orientarmi. L' infermiere che guarda il suo orologio prima di rispondere."

"Le cose sembrano accadere al rallentatore."

show nurse neutral
with charachange

nk "Dieci e un quarto."

"Provo per un momento a pensare cosa quello voglia dire ma non sono proprio sicuro."

show nurse concern
with charachange

nk "Non hai risposto alla mia domanda, Hisao."

hi "Oh. Bene."

show nurse neutral
with charachange

nk "Scendi da quel letto allora, e vediamo come te la cavi. Non…"

show bg school_nurseoffice as dizzy_bg behind nurse at RotoZoom(0,6,0.4,1.0,1.05,0.4), Alpha(0.0,0.5,0.4, xalign=0.5, yalign=0.5)
show nurse neutral as dizzy_fg at RotoZoom(0,-4,0.4,1.0,1.05,0.4), Alpha(0.0,0.5,0.4, xalign=0.5, yalign=0.5)
with Pause(0.4)
show bg school_nurseoffice as dizzy_bg behind nurse at RotoZoom(6,0,0.8,1.05,1.0,1.0), Alpha(0.5,0.0,1.0, xalign=0.5, yalign=0.5)
show nurse neutral as dizzy_fg at RotoZoom(-4,0,1.0,1.05,1.0,1.0), Alpha(0.5,0.0,1.0, xalign=0.5, yalign=0.5)

"Provo a fare esattamente quello, solo per ondeggiare in preda alle vertigini quando mi muovo troppo velocemente. L' infermiere si muove per sorreggermi da un braccio e sospira."
 
show nurse concern
with charachange

nk "…alzarti troppo in fretta, era quello che stavo per dire. Siediti lì, ti controllerò la pressione per essere sicuri."
 
"Le mie buone intenzioni sono certo durate a lungo. Mi zittisco, imbarazzato da me stesso, mentre l' infermiere si dà da fare con un aggeggio dall' aria antica e il mio braccio."

"Dopo un paio di minuti, lo mette via, non sembrando soddisfatto nè scontento."

show nurse neutral
with charachange

nk "Sei a posto. La testa ha smesso di girare?"

hi "Già."

nk "Bene. E i contenuti come vanno?"

show nurse concern
with charachange

nk "Non hai dimostrato un gran giudizio là fuori, Hisao."

"Ingoio la replica che stavo per dare. E' quello che stavo pensando anche io, ma sentirlo dire da qualcun altro mi fa voler protestare."

"Quello che sta dicendo non è piacevole. Non vuol dire che ha meno ragione."

hi "Nossignore."

show nurse neutral
with charachange

"Annuisce, sempre con l' aria neutra che aveva prima."

"Sarebbe facile arrabbiarsi con lui se dicesse “Te l' avevo detto” o qualcosa del genere, ma non lo fa."

nk "Io posso provare ad aiutarti a rimanere in salute, ma alla fine l' ultima decisione è tua. Speriamo che questo piccolo episodio sia qualcosa che te lo ricordi."

show nurse fabulous
with charachange

nk "Prendi, una nota per il tuo insegnante. Per evitare un interrogatorio."

"Prendo il foglietto di carta che mi sta offrendo e poi me ne vado perchè non riesco a pensare a nient' altro da dire, nè davvero voglio farlo."

show nurse neutral
with charachange

nk "Stai fuori dai guai, capito? Non penso che fosse niente eccetto uno spavento, ma la prossima volta potrebbe essere diverso."

"Capito."

scene bg school_nursehall
with locationchange

"C'è un qualche modo di arrivare all' edificio scolastico direttamente dall' edificio ausiliario, ma non ho voglia di scoprire come e probabilmente perdermi, così esco dall' uscita che conosco."

scene bg school_courtyard
with locationchange

"Mi fermo ai piedi delle scale dell' edificio ausiliario, indeciso per un momento tra andare ai dormitori per prendere i miei libri e la mia roba ed andare dritto in classe."

"Il sole mi fa bruciare gli occhi, così vado a sinistra, verso l' edificio principale."

stop music fadeout 2.0

    
#******************************
    
label it_A26:

scene bg school_dormhisao
with openeye

scene bg school_dormbathroom
with locationskip

"Mi sveglio e faccio una doccia calda."

label it_A26a:

scene bg school_dormhisao
with locationskip

play music music_sadness fadein 0.3

#this segment has some real problems and I can't figure out what has been changed. It is shown only if Hisao doesn't get heart attack on track, but it obviously referenced getting one. Wtf
#I'm changing it to refer Hisao's first heart attack with Iwanako, but this does require some observing. edit: seems it was a issue already.
#changing it again, it really came out of nowhere

"Tornato nella mia stanza, la prima cosa che vedo è la familiare fila di boccette di medicinali allineata sul mio comodino, che mi deprime, come al solito."

"E' seccante. Credevo di stare bene. Pensavo di avere fatto la mia pace con questa cosa, passato oltre."

"Ma cosa ho fatto davvero… mi sono permesso di dimenticare che ho un problema. Essere qui mi ricorda davvero la realtà, e cercare di combatterla mi fa solo del male."
   
"Rifletterci sopra serve solo fino a un certo punto. Lo ho già fatto prima d' ora, per dei mesi. Sembra che sia ora di passare oltre."

"Se mi permetto di dimenticare che la mia vita decisamente non sarà lunga quanto quella degli altri, non arriverò da nessuna parte."

"La mia vita può essere diversa dalle altre. Ma è una vita in progresso."
    
"Lo razionalizzerò così."

"Inghiotto la solita manciata di pillole, cercando di togliermi l' improvviso pensiero tetro dalla testa. Poi mi preparo ad andare in classe in anticipo, come al solito."

stop music fadeout 1.0

scene bg school_dormhallway
with locationchange

"Quando entro nel corridoio, noto Kenji che sta girando l' angolo, dirigendosi cautamente verso la sua stanza con una grossa borsa. Mentre mi passa accanto senza fare un suono come un ninja che si nasconde in piena vista, lo chiamo."

hi "Ehi."

play music music_kenji fadein 0.3

show kenji neutral
with charaenter

"Salta al suono della mia voce."

ke "Oh, ehi, amico. Non ti avevo notato. Sono davvero stanco."

"Credo sia più che proprio non mi avesse visto, ma non è quella la questione."

hi "Dove sei andato così presto? A far compere?"

show kenji tsun
with charachange

ke "Nah non stavo facendo compere. Qualche volta devo visitare… l' insegnante di matematica. Già, ho pensato che sarebbe stata una buona idea sapere quando ci sarà il prossimo test, dato che te lo dice in anticipo se vuoi."

hi "E allora, che c'è nella borsa?"

show kenji neutral
with charachange

ke "Ho pensato di andare a far compere già che ero fuori. Ho bisogno di rifornimenti per continuare il combattimento contro la vasta cospirazione femminista."

hi "Uh, okay."

hi "Credevo che tu non uscissi."

show kenji happy
with charachange

ke "Ora indosso un cappello."

"Decido di non fargli presente che non sta indossando nessun cappello."

"Un silenzio imbarazzante si forma tra di noi e poi Kenji lo rompe aprendo lentamente la sua porta, rilasciando un suono scricchiolante nell' aria che fa solo sembrare il momento ancora più imbarazzante."

"Poggia la borsa nella sua stanza e poi chiude la porta."

hi "Sono sorpreso che ti sia dato pensiero di scoprire la data di un test. Cercare di prendere vantaggio di un' opportunità per studiare è piuttosto diligente."

show kenji tsun
with charachange

ke "Io non studio mai."

hi "Oh…"

show kenji neutral
with charachange

ke "Volevo solo sapere qual era il giorno del prossimo test. Lo darò comunque, duh. Devo saperlo così so in che giorno non posso permettermi di marinare."

ke "Di solito spedisce degli aggiornamenti su quella robaccia per telefono, così ho dovuto uscire e controllare."

hi "E perchè devi uscire, quando puoi riceverli sul tuo telefono?"

show kenji tsun
with charachange

ke "Io non porto un telefono."

hi "Cosa vuol dire, non porti un telefono? Vuoi dire che lo lasci a casa?"

show kenji neutral
with charachange

ke "Nah, non uso telefoni. Non ho un telefono. Telefoni. Non ho nessun telefono."

hi "Perchè non hai un telefono? Come fai a non avere un telefono? Proprio nessuno? Nessun telefono?"

show kenji tsun
with charachange

ke "Non mi piacciono i telefoni. A dire il vero, mi spaventano un po'. Non so perchè. Credo che sia una specie di trauma represso."

ke "Ma, basilarmente, quando sento un telefono, divento nervoso. E' il mio più oscuro segreto."

show kenji neutral
with charachange

ke "Ho due teorie al riguardo: o ho una qualche paura di ricevere qualche indefinita, sinistra, fatale chiamata che cambia la mia vita, o sono stato picchiato con un telefono in passato. Picchiato così forte che non riesco a ricordarmelo."

hi "Picchiato in testa."

show kenji tsun
with charachange

ke "Bè, dove altro potrei venire picchiato con un telefono che mi renderebbe incapace di ricordarlo? Sul culo?"

"Inaspettatamente logico. Mi sento molto depresso ora. Percependo che questa conversazione è più o meno terminata, Kenji apre di nuovo la sua porta e si prepara a entrarvi."

show kenji neutral
with charachange

ke "Già, me ne vado a dormire, tizio. Divertiti."

hi "Le lezioni iniziano tipo tra venti minuti."

show kenji tsun
with charachange

ke "Ho già fatto qualcosa oggi. Troppo stanco per andare a scuola."

show kenji happy_close
with characlose

ke "Ehi, hai bisogno di un po' di lucidalabbra? Accidentalmente ne ho comprati due perchè credevo che il negozio avesse iniziato a vendere batterie stilo sfuse."

hi "Grazie ma no, grazie."



label it_A26b:

scene bg school_dormhallway
show kenji happy_close
with None

stop music fadeout 2.0

play sound sfx_impact2

show kenji tsun_close
with vpunch

"La porta del corridoio principale si apre con un botto quando gira dopo essere stata spinta troppo forte e batte contro il muro. Il suono viene seguito da un fragore di briose risate, e istantaneamente so chi è stato."

show misha perky_smile behind kenji
show shizu basic_normal2 behind kenji
with zoomin

show misha perky_smile at twoleft
show shizu basic_normal2 at tworight
with charamove_decel

hide kenji
with easeoutright

play sound sfx_impact2

"Al rumore, Kenji sparisce nella sua stanza come un ninja, sbattendo la porta proprio quando Shizune e Misha entrano in vista, la prima facendo piccoli, efficienti passi verso di me mentre la seconda più o meno rimbalza contro i muri."

show misha hips_smile_close at twoleft
with characlose

"Cerco di imitare Kenji, ma è troppo tardi. Misha mette il suo piede in mezzo alla mia porta per impedirmi di chiuderla, così non ho altra scelta che lasciarle entrare."

play music music_comedy fadein 0.3

scene bg school_dormhisao
with locationskip

show shizu behind_smile
with charaenter

shi "…"

show shizu behind_smile at tworight
with charamove

show misha hips_grin at twoleft
with charaenter
    
mi "Ciao, Hicchan~! Ciao~ ciao~!"

hi "Ciao."

hi "Cosa state facendo qui voi due?"

"Mi chiedo se la pausa tra quelle due frasi era sufficientemente lunga da essere cortese."

show shizu basic_normal at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange
   
mi "Hicchan, sei scortese~! Siamo venute a prenderti!"

show misha hips_smile at twoleft
with charachange

mi "Credevi che avremmo pensato che avresti tentato di scappare e che saremmo venute per assicurarci che tu non lo faccia? Certamente no, Hicchan~!"

hi "Ehi, non ho detto che è per quello che siete qui."

"Ma ora so che è esattamente quello per cui sono qui."

show misha sign_smile at twoleft
with charachange

mi "E' ora di lavorare per il consiglio studentesco, sì lo è~!"

show misha hips_grin at twoleft
with charachange
    
mi "Non sei contento, Hicchan, di potere aiutare l' intera~ scuola~! Sei tipo, un eroe~! Le generazioni future racconteranno storie su questo giorno!"

"Interessante. Non pensavo che unirmi al consiglio studentesco sarebbe stato un atto eroico degno di Ercole."

hi "Beh… suppongo di avere promesso quindi…"

show shizu adjust_happy at tworight
with charachange

"Ho trascurato Shizune, e solo ora mi accorgo di lei ai bordi della mia vista, mentre spia nella mia stanza da sopra la mia spalla, i suoi occhi analitici che passano da oggetto a oggetto…"

"Questo è piuttosto indiscreto, la sensazione di essere esposto formicola nei miei testicoli. Fortunatamente non ho della biancheria sporca sul pavimento o niente del genere."

show shizu behind_smile at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange
    
mi "Hm~? Cosa c'è, Shicchan?"

show misha hips_smile at twoleft
with charachange

mi "Già, questa è la stanza di Hicchan~! Non l' abbiamo mai vista prima, non me ne ero nemmeno accorta!"

show misha hips_grin at twoleft
with charachange

mi "E' piuttosto semplice, ma Hicchan non ha ancora avuto il tempo di decorarla, non è così~?"

stop music fadeout 2.0

show misha sign_smile at twoleft
with charachange

mi "Quelle cosa sono?"

"Punta alla mia collezione di medicinali sul comodino."



label it_choiceA26:
menu:
    with menueffect

    "Non voglio davvero parlarne con queste due."

    "Cercare di evitare l' argomento.":
        return m1

    "Sbatterle fuori dalla mia stanza.":
        return m2


label it_A26c:

hi "Non sono nulla."

show shizu basic_normal2 at tworight
with charachange

"Rapidamente mi piazzo davanti a loro, cercando di nascondere la roba dietro la mia schiena. Shizune fa un passo indietro e sembra sospettosa, ma è un' espressione non priva di preoccupazione."

"Spero che se evito di parlarne, lei capirà che non voglio che continui a insistere."

show shizu behind_blank at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "Davvero? Cosa stai nascondendo, Hicchan~?"
    
hi "Nulla."

show shizu basic_normal at tworight
with charachange

shi "…"

show misha sign_confused at twoleft
with charachange

mi "Davvero~?"
    
"Capisco che non posso veramente schivarla stavolta. Sono ficcanaso per natura e nasconderle finirà solo per stuzzicare di più il loro interesse."
    
hi "Sì va bene, è {b}qualcosa{/b}, ma non voglio davvero parlarne, okay? Non… ancora."

hi "Possiamo solo lasciar stare per ora?"

show misha perky_smile at twoleft
with charachange

"Mentre Misha traduce, Shizune mi guarda fisso, i suoi occhi concentrati e analitici come sempre mentre mi guardano curiosamente da sopra i bordi dei suoi occhiali."

"Preme pensosamente insieme le sue dita, come se stesse calcolando il valore di perseguire questo più a lungo del necessario contro l' insulto di non rispettare il mio desiderio."

"La sua espressione finalmente si scioglie in un leggero sorriso e segna qualcosa a Misha."

play music music_shizune fadein 0.3

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Okay~! Allora, aspetteremo, e diventeremo sempre più amici, e un giorno quando ti andrà, puoi parlarcene~!"

"Tutte e due mi fanno larghi sorrisi, e mi sento scioccato e un po' stupido per essere fatto così."

"Non sono stupide, e probabilmente possono almeno indovinare parte di cosa c'è che non va in me. E…"

"Delle parole così semplicemente gentili e comprensive. Mi sento sollevato che non pensino ancor peggio di me anche se mi comporto così. Anche se non sono come gli altri qui. Anche se non riesco a essere a mio agio."

"Sembra che dietro le azioni irritanti e maliziose, entrambe queste ragazze siano davvero persone buone e gentili. E' quel che penso."

hi "Grazie."

hi "Così, volete che vi aiuti oggi, giusto? Dato che sono uno di voi adesso?"

show misha hips_grin at twoleft
with charachange

mi "Yup~!"

hi "Dopo la scuola?"

show misha sign_smile at twoleft
with charachange

mi "No no no~! Ora!"
    
hi "Ora? E le lezioni? Avete intenzione di marinare di nuovo?"

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha cross_laugh at twoleft
with charachange
 
mi "Hahaha~! E' per il bene comune, così sacrifichiamo la nostra lezione di matematica, e forse anche gli studi sociali~!"

hi "Bè, suppongo che a me stia bene."

show shizu behind_smile at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Fantastico, Hicchan~! L' hai detto, okay? Ricorda: “mi sta bene di aiutarvi~,” è quello che hai detto, giusto~?"

hi "Già."

"Quel tono… improvvisamente mi pento di averlo detto."

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Okay~! Sei pronto ad andare allora? Possiamo camminare fino all' ufficio insieme~!"

hi "No. Probabilmente mi farete portare tutta la vostra roba o qualcosa del genere."

#shizune's expression should change to a smile

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Non essere sciocco, Hicchan."

show misha hips_smile at twoleft
with charachange

mi "Non abbiamo mai camminato fino a scuola insieme, Hicchan~."

"Quasi voglio chiedere perchè dovremmo, ma poi mi viene in mente. Mi considerano tutte e due come un amico, come Misha ha detto prima. E vogliono diventare ancora più mie amiche, perfino."

"E' strano, non ho mai davvero pensato a loro in quel modo. O a nessuna delle persone che ho incontrato finora questa settimana. E' davvero così facile?"

"Come per caso…"

hi "Okay, andiamo, allora."

show shizu behind_smile at tworight
with charachange

"Shizune sogghigna astutamente e mette le mani dietro la schiena."

show misha hips_grin at twoleft
with charachange

mi "Hahaha~! Ottimo, Hicchan~! Okay, okay, ma prima~! Hai avuto un' idea davvero ottima, a Shicchan è piaciuta molto… Così~! è tempo per un gioco!"

hi "Oh no."

show misha hips_smile at twoleft
with charachange

mi "Shicchan ha una banconota da 1000 yen in una mano, Hicchan~! Se indovini quale, è tua! Se no…"

show misha hips_grin at twoleft
with charachange

mi "Porterai tutti i nostri libri in classe~! Giusto, Shicchan~? Giusto~!"

"Shizune e lei scambiano segni di assenso."

show misha sign_smile at twoleft
with charachange

mi "Okay, Hicchan~! Preparati~!"

scene bg school_courtyard
with shorttimeskip

"Portando tre borse invece di una, penso al giorno che ho davanti. O che abbiamo davanti."

"Posso vedere degli studenti che camminano avanti e indietro per il cortile, probabilmente in preparazione dei loro progetti."

"Il festival è praticamente arrivato. Quello significa che ci sono solo due possibili ragioni per cui il mio aiuto è richiesto."

"O è rimasto solo poco lavoro da fare, e vogliono solo una mano per concludere i controlli finali che sono obbligate a fare."

"Oppure è rimasta una tonnellata di lavoro, e Shizune sta fingendo di essere calma mentre un torrente di lavoro procrastinato e accumulato minaccia di ucciderci tutti."

stop music fadeout 2.0


label it_A26d:

#bg school_dormhisao
#shizu behind_smile at tworight
#misha sign_smile at twoleft

"Comunque, stavolta hanno davvero passato il segno. Seccatrici ficcanaso."

hi "Non sono nulla."

show misha perky_smile at twoleft
with charachange

mi "Davvero~, Hicchan? A me non sembra che non sia nulla."

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Che lunga fila di boccette, giusto~? Giusto~! Cosa sono quelle, Hicchan?"
    
hi "Solo alcune cose."

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange
    
mi "Quello sembra molto più di “solo alcune cose”…"

"Non posso incolpare nessuna delle due per essere così. Misha sta solo parlando per Shizune, e Shizune è solo curiosa di natura. Però, vorrei che loro due smettessero di impicciarsi e cogliessero il messaggio. Ma Misha non lo capisce, e Shizune non può."

"Per quello, continuano a insistere."

hi "Non sono davvero affari vostri."

hi "Non dovreste andarvene? La stanza di un uomo è privata, sapete."

"Shizune sembra prenderlo come una sfida."

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange

mi "Cosa vuol dire, Hicchan? Quando qualcuno vede qualcosa di interessante, il loro primo istinto è di chiedere cosa sia, quello è ovvio. Cosa c'è di sbagliato in questo?"

hi "Perchè, come ho detto, non c'è niente da vedere."

show misha perky_confused at twoleft
with charachange

mi "Hicchan, penso che Shicchan sia solo preoccupata."

hi "Quello che ho nella mia stanza non sono affari vostri, tutto qui."

show misha sign_confused at twoleft
with charachange

mi "Ma…"

hi "Dannazione! Qualche volta, vorrei che voi due la piantaste di giocare così tanto. Non è sempre divertente. Lo sapete, vero?"

"Lo dico molto più forte di quanto volessi, quasi urlandolo dritto in faccia a Misha. Sussulta e si ferma a metà di un segno, e perfino Shizune reagisce anche se non mi ha sentito."

"Immagino che la rabbia sulla mia faccia abbia detto tutto quel che c'era bisogno di dirle."

play music music_sadness fadein 0.3

show misha perky_sad at twoleft
show shizu behind_blank at tworight
with charachange

"Dopo che Misha termina lentamente la traduzione, le ragazze si guardano a vicenda con rimpianto."

show shizu behind_sad at tworight
with charachange

shi "…"

mi "Okay, Hicchan, ti lasceremo in pace."

"E' la prima volta che ho sentito Misha parlare senza quella familiare cadenza sali-e-scendi nella sua voce. Sembra così strano a sentirsi, e voglio scusarmi, ma si sono già girate per andarsene."

"Mentre cala il silenzio, mi pento sempre di più di quello che ho detto."

hide shizu
hide misha
with charaexit

"Le ragazze se ne vanno silenziosamente, e dopo che sono restato in piedi nella mia stanza per un po', mi vesto e le seguo."



label it_A26e:

show kenji tsun_close
with charachange

ke "Vabbè, amico."

hide kenji
with charaexit

"Entra rapido nella sua tana, finalmente lasciandomi libero di andare a lezione."



#*************************

label it_A27:

scene bg school_hallway3
with locationskip

play sound sfx_doorknock2

"I corridoi sono silenziosi come lo era il cortile, naturalmente dato che tutti sono in classe. Busso leggermente alla porta della classe 3-3 e spingo per aprire la porta quando Mutou risponde dall' altra parte."

scene bg school_scienceroom
with locationchange

hi "Scusate il ritardo."

"Quindici paia di occhi si girano verso di me."

show muto irritated
with charaenter

mu "Buongiorno, Nakai."

"Mutou sembra essere piuttosto confuso dal mio arrivare in ritardo, come se avessi interrotto il filo del suo discorso o qualcosa del genere."

"Giudicando dalle spiegazioni sconnesse che le sue lezioni tendono a essere, quello potrebbe essere il caso."

"Gli passo la nota che mi ha dato l' infermiere. Mutou la prende con un cenno del capo e la legge rapidamente."

show muto normal
with charachange

"Inarca le sopracciglia e mi lancia uno sguardo un po' severo ma non dice nulla, solo annuendo di nuovo solennemente."

"Scrollo le spalle e lui mi indica di andare al posto così naturalmente lo faccio."


label it_A27a:

scene bg school_scienceroom
show muto normal
with None

#so if you have joined SC, you see this
hide muto
with charaexit

"Solo due paia di occhi continuano a seguirmi intensamente mentre cammino fino al mio posto."

"Non sono affatto sorpreso quando sento l' unghia di Misha che mi pizzica attraverso la camicia circa quindici secondi dopo che mi sono seduto."

play music music_another fadein 0.3

show misha perky_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha perky_smile_close at Position(xalign=-0.3)
with charamove

mi "Psst! Dove eri?"

hi "Non sono affari tuoi."

"So che questa è probabilmente la peggior risposta che posso dare perchè serve solo a stuzzicare la loro curiosità, ma non ho le energie per inventarmi delle elaborate coperture in questo momento."

show misha perky_confused_close at Position(xalign=-0.3)
with charachange

show bg school_scienceroom
show misha perky_confused_close at offscreenleft
with charamove

"Però, Misha non insiste. E' inaspettatamente rapida a cedere oggi."

"…"

"Dopo un minuto, torna a ficcarmi il suo dito tra le costole."

show misha hips_grin_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha hips_grin_close at Position(xalign=-0.3)
with charamove

mi "Dai, diccelo! Anche a Shicchan interessa molto!"

"Erano solo le mie speranze. Ne ha solo parlato con Shizune, probabilmente inventando modi di farmi parlare."

hi "No."

show misha perky_sad_close at Position(xalign=-0.3)
with charachange

show bg school_scienceroom
show misha perky_sad_close at offscreenleft
with charamove

"Si ritira a negoziare di nuovo."

show misha sign_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Position(xalign=-0.3)
with charamove

label it_choiceA27:
menu:
    with menueffect

    mi "Come membro del consiglio studentesco, è tuo dovere dirci perchè salti le lezioni! Specialmente se è qualcosa di di-ver-ten-te~!"

    "Già, mi stavo di-ver-ten-do proprio molto nell' ufficio dell' infermiere…":
    #to A27b
        return m1

    "Non voglio parlarne, okay?":
    #to A27c
        return m2

label it_A27b:

"Per la miseria. Proprio non sa quando smetterla."

hi "Sì certo. Come no. Ve lo dirò. Stavo divertendomi un sacco."

hi "Stamattina per prima cosa ho avuto un attacco di cuore, e poi ho passato il tempo assieme al capo infermiere per qualche ora tanto per spassarmela."

hi "La miglior mattinata della mia vita, ve lo dico."

"Sto cercando di imitare il suo ridicolo parlare cadenzato mentre tengo la mia voce così bassa che nessun altro mi può sentire. Sputo le parole dalla mia bocca."

stop music fadeout 6.0

show misha perky_confused_close at Position(xalign=-0.3)
with charachange

mi "Hicchan, hai avuto un cosa? Dici sul serio?"

hi "Piantala. Mi hai sentito benissimo."

show misha perky_sad_close at Position(xalign=-0.3)
with charachange

mi "Ma Hicchan, questo è importante!"

hi "No, davvero. Lasciami in pace. Siamo anche nel bel mezzo della lezione."

show misha sign_sad_close at Position(xalign=-0.3)
with charachange

mi "Ma Hicchan!"

"Misha suona preoccupata, o forse in preda al panico. Mi chiedo se capisce che non era la migliore delle idee essere così dannatamente invadente."

"…"

"La lascio cuocere nel suo brodo per un pò prima di rispondere. Non sarà traducibile per Shizune ma non mi importa."

hi "Non rompere, Misha."

hi "E dì anche a Shizune lo stesso."

"Quando le parole lasciano la mia bocca, immediatamente mi pento di averle dette, ma non è come se le potessi più ritirare."

show misha perky_sad_close at Position(xalign=-0.3)
with charachange

show bg school_scienceroom
show misha perky_sad_close at offscreenleft
with charamove

"Con mia parziale sorpresa, Misha tace davvero anche se non mi preoccupo di controllare che passi il messaggio a Shizune. In ogni caso, non importa."

"Mutou termina la sua lezione con un discorso generico riguardo al festival che si terrà tra due giorni."

#to A29, needs a conditional about Emi making Hisao feel better



label it_A27c:

hi "Lascia perdere. Non ho intenzione di dirtelo."

show misha hips_grin_close at Position(xalign=-0.3)
with charachange

mi "Davvero~?"

hi "Già."

show misha perky_confused_close at Position(xalign=-0.3)
with charachange

"Ci pensa su per un momento."

show misha hips_frown_close at Position(xalign=-0.3)
with charachange

mi "Sei tirchio, Hicchan~!"

"Posso sentire il broncio nella sua voce, delusa e abbattuta."

show bg school_scienceroom
show misha hips_frown_close at offscreenleft
with charamove

"Si ritira di nuovo un momento per negoziare col cervello del duo dinamico, prima di ritornare."

show misha hips_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha hips_smile_close at Position(xalign=-0.3)
with charamove

mi "Penso che dovremmo pranzare insieme e discuterne più a lungo… dice Shicchan."

show misha hips_grin_close at Position(xalign=-0.3)
with charachange

mi "Offriamo noi."

show misha sign_smile_close at Position(xalign=-0.3)
with charachange

mi "E comunque, devi ripagarci per non esserci stato stamattina e abbiamo bisogno di aiuto col lavoro~!"
    
"Gli altri studenti intorno a noi stanno cominciando a guardarci, probabilmente perchè Misha si sta chinando a tal punto sul suo banco che quasi sta cozzando con la testa contro la mia. I suoi ricci sfiorano il mio collo."

"Odorano di shampoo e molto di quello che usa per farli restare così come sono."

"Credo che la ragazza di fronte a me stia cercando di ascoltare. Spero che a nessuno stia venendo l' idea sbagliata, anche se non sono davvero sicuro come sarebbe possibile farsene venire un altro tipo."

"Fortunatamente Mutou rimane ignaro, o ignora deliberatamente Misha. Per ora."

"Proprio non posso spuntarla, non è vero?"



label it_choice2A27:
menu:
    with menueffect

    "Ho anche promesso di mangiare con Emi, ma non posso essere in due posti allo stesso tempo."

    "Andrò al pranzo con Emi e i suoi amici.":
        return m1

    "Andrò con Shizune, ora sono nel consiglio studentesco dopo tutto.":
        return m2


label it_A27h:
#lol label order

hi "Spiacente, non posso. Ho già promesso di andare a pranzo con qualcun altro."

show misha perky_confused_close at Position(xalign=-0.3)
with charachange

mi "Eeeh? Chi? é una ragazza~?"

hi "Già…"

show misha hips_grin_close at Position(xalign=-0.3)
with charachange

"La sua risatina mi convince a rapidamente aggungere qualcosa così che non le venga l' idea sbagliata."

hi "Non è niente del genere! E'… un po' complicato."

show misha perky_smile_close at Position(xalign=-0.3)
with charachange

"Complicato… già, la mia vita è così, a dispetto di essermi già adattato a una routine giornaliera di vita scolastica."
   
"Ogni cosa deve essere messa in un nuovo tipo di prospettiva in questa seconda vita, riconsiderata dal punto di vista di questo nuovo me."

"Il me con un cuore difettoso."

hi "Inoltre, non so se posso venire al consiglio dopotutto."

hi "O almeno per adesso. Ho qualcos' altro su cui mi devo concentrare prima."

"E' vero. Devo ripensare alle mie priorità. Questo è qualcosa che mi sta girando in testa da quando l' infermiere mi ha fatto quel discorso. Davvero non posso permettermi di fingere di non avere questo problema."

"Sono sorpreso di poter pensare così analiticamente, ma per adesso seguirò l' onda."
    
hi "Prometto che mi spiegherò per bene più tardi, ma non ora, okay? Per favore dì a Shizune che mi dispiace di deluderla."

show misha perky_confused_close at Position(xalign=-0.3)
with charachange

mi "Se lo dici tu, Hicchan."

"Suona sorpresa, e seria, che è qualcosa che non credo di avere mai sentito in Misha prima d' ora."

show bg school_scienceroom
show misha perky_confused_close at offscreenleft
with charamove

"Misha fortunatamente capisce che parlo sul serio, è un colpo di fortuna che abbia potuto dire quello che volevo tanto chiaramente che perfino lei ha capito. Si ritira per tradurre la nostra discussione per Shizune."

"Nessuna delle due mi parla dopo di ciò."



label it_A27i:

hi "E va bene, verrò con voi, ma lasciatemi in pace per il resto della lezione, okay?"

show misha hips_grin_close at Position(xalign=-0.3)
with charachange

mi "Affare fatto, Hicchan~!"

stop music fadeout 2.0

show bg school_scienceroom
show misha hips_grin_close at offscreenleft
with charamove

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

# this pause is necessary because there is no text here.
# if you can add some before he leaves the room, remove the pause
with Pause(7.0)

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationchange

"Lungo la strada per la stanza del consiglio studentesco, posso vedere degli studenti che camminano avanti e indietro per i corridoi, probabilmente in preparazione dei loro progetti."

"Il festival è praticamente arrivato. Quello significa che ci sono solo due possibili ragioni per cui il mio aiuto è richiesto."

"O è rimasto solo poco lavoro da fare, e vogliono solo una mano per concludere i controlli finali che sono obbligate a fare."
    
"Oppure è rimasta una tonnellata di lavoro, e Shizune sta fingendo di essere calma mentre un torrente di lavoro procrastinato e accumulato minaccia di ucciderci tutti."

stop ambient fadeout 1.0


label it_A27d:

#if you are not SC member and did not get a heartattack OR if you blew Shizune and Misha off in A26, you come straight to this, the day begins with it in some cases.

scene bg school_scienceroom
with locationskip

stop music fadeout 2.0

"Per una volta tanto, non sono tra i primi a entrare in aula la mattina."

"Invece, quasi tutti gli altri sembrano già essere arrivati. Ormai riconosco la maggior parte dei miei compagni classe di vista, anche se i nomi mi sfuggono ancora."



label it_A27e:

#If you have not joined SC, you see this instead of A27a, this is also a followup on A27e

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 0.3

"La lezione procede pigramente. Credo di stare iniziando a entrare nel ritmo della scuola."

"Ho perfino smesso di preoccuparmi di prendere appunti e di dimostrarmi costantemente attento. I primi giorni, ero piuttosto nervoso in classe."

"Mutou termina presto la sua lezione sull' elettricità, ma continua senza pausa a parlare del festival."

show muto normal
with charaenter

mu "Così, come sapete, il festival è dopodomani. Spero che i progetti di tutti siano un successo quest' anno."

show muto smile
with charachange

mu "Divertitevi, ma questa domenica, per favore tenete in mente il significato di questo festival…"
    
mi "Giochi e cibo fritto!"

"Tutti scoppiano a ridere, me incluso."

show muto irritated
with charachange

mu "Sì, grazie Mikado."

show muto normal
with charachange

mu "Ma intendevo più il-{w=.5}{nw}"

play sound sfx_normalbell

"Il resto della sua frase viene sepolto dal suono della campana della pausa pranzo, e tutti iniziano a raccogliere le loro cose."
    
"Mutou pondera per un momento, ma dato che quasi nessuno sembra più prestargli attenzione, lascia perdere e si siede."

stop music fadeout 2.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"Il corridoio è affollato… o tanto affollato quanto lo possono essere i corridoi in questa scuola. La maggior parte degli studenti sembra stare scendendo in mensa."


#to A29



label it_A27f:

scene bg school_scienceroom
with shorttimeskip

stop music fadeout 2.0

"Misha, e per delega Shizune, non mi infastidisce per l' intera mattinata."

play sound sfx_normalbell

"Quando suona la campana, non le guardo nemmeno mentre esco dalla classe."

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"Il corridoio è affollato… o tanto affollato quanto lo possono essere i corridoi in questa scuola. La maggior parte degli studenti sembra stare scendendo in mensa."


    
#***************

label it_A28:

scene bg school_council
with locationchange

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter

"Una volta dentro all' ufficio, mi guardo intorno e vedo che è deserto."

hi "Immagino voglia dire che non è rimasto troppo lavoro da fare, eh? Dato che non c'è nessuno qui…"

play music music_happiness fadein 0.3

show misha sign_smile at twoleft
with charachange

mi "E' sempre così, Hicchan~!"

"Questo conferma quello che ho sempre pensato ma che non sono mai stato in grado di dire definitivamente che sapevo con certezza: Shizune e Misha sono il consiglio studentesco. L' intero consiglio studentesco."

hi "Dannazione. Così è vero. Il consiglio studentesco siete veramente solo voi due."

show misha hips_grin at twoleft
show shizu cross_wut at tworight
with charachange

"Shizune sembra essere bloccata nel mezzo di decidere se vergognarsi o esplodere di rabbia, e Misha è ugualmente divisa tra ridere e cercare di fermarla."

show shizu behind_frustrated at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Bene, allora, Hicchan, sarai felice di sapere che dato che siamo solo noi tre, abbiamo un sacco da fare! Un sacco~! Un sacco~ sacco~ sacco~…"

hi "Quello non mi rende felice."

show shizu adjust_happy at tworight
with charachange

"Ma sembra rendere Shizune molto felice."

show misha cross_laugh at twoleft
with charachange

mi "Wahaha~!"

show misha hips_grin at twoleft
with charachange

mi "Sto scherzando!"



label it_A28a:
#you see this if you have been spending the morning in the infirmary

scene bg school_council
with shorttimeskip

"Il lavoro risulta essere ordinare e ricontrollare la considerevole quantità di carte necessarie perchè un evento come il festival scolastico possa avvenire."

"La burocrazia è una cosa incredibile."

play sound sfx_normalbell

"Ma riusciamo a finirlo proprio quando la campana suona la pausa per il pranzo."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter

mi "Okay~, adesso che abbiamo finito, possiamo rilassarci un po'! Ma non troppo, abbiamo ancora un sacco da fare per il pomeriggio~!"



label it_A28b:

show shizu behind_smile at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Davvero non è così tanto lavoro, Hicchan~. Così~, possiamo permetterci di goderci un po' il pranzo prima."

show misha cross_laugh at twoleft
with charachange

mi "Hahaha~!"

"Le due producono un piccolo schieramento di contenitori di plastica, apparentemente dal nulla."

show misha hips_grin at twoleft
with charachange

mi "Hm~ hm~… Sono cotolette di pollo con pomodori e germogli di soia~! Non sembra delizioso, Hicchan?"

mi "E' stato preparato giusto stamattina, ed è ancora caldo, così mangia mangia mangia~!"

"Prendo uno dei contenitori e lo apro. Sembra buono, e certamente ha un buon odore. Il fatto che sono davvero affamato aggiunge all' effetto."

hi "Wow, sembra ottimo. Dove l' avete preso?"

show shizu basic_normal at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Quello non importa, Hicchan!"

show misha sign_smile at twoleft
with charachange

mi "Ci doveva essere un chiosco che vendeva pranzi confezionati, ma la ragazza che doveva gestirlo improvvisamente ha detto che non poteva. Shicchan ha detto, “Che spreco, è stata una gran fatica ingannare Hicchan perchè lo costruisse~”—"

hi "Ehi, che diavolo…"

show misha hips_grin at twoleft
with charachange

mi "…Così~! Shicchan ha voluto vedere se poteva farlo lei, ma poi ha deciso di no, giusto, Shicchan~?"

show shizu basic_angry at tworight
with charachange

"Shizune fa il broncio arrabbiata, lanciando a Misha uno sguardo scontento. Non credo che si supponeva io sentissi quella storia."

hi "Questo è il tuo cibo di prova?"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Lo mangerò anche io, Hicchan~!"

show misha hips_grin at twoleft
with charachange

mi "E anche Shicchan~!"

"Quello non risponde alla domanda!"

"Ciononostante, divido un paio di bastoncini che mi vengono offerti da Shizune, raccolgo un pezzo di cotoletta, e me lo ficco in bocca."

hi "E' sorprendentemente buono. Non mi aspettavo che Shizune fosse una così brava cuoca."

show shizu basic_frown at tworight
with charachange

"Shizune mette giù i suoi bastoncini per segnare bruscamente verso Misha, che inghiotte la sua cotoletta con notevole difficoltà per parlare per lei."

show misha sign_smile at twoleft
with charachange

mi "Hicchan~! Non parlare a bocca piena~!"

hi "Non è che mi piaccia farlo. Comunque, quanto è materno mostrare quel tipo di preoccupazione…"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Non sai nemmeno mangiare come si deve, Hicchan~! Quello è tutto~!"

"E' uno stallo. Non posso mangiare se voglio parlare a Shizune, che non può mangiare se vuole rimproverarmi per il mio mangiare in modo sbagliato."

"Misha, presa in mezzo, è nella stessa situazione, e sembra essere la più scoraggiata da come stanno andando le cose."

"In ogni caso, il nostro cibo sta diventando più freddo a ogni secondo che passa, e non era bollente fin dall' inizio. Dovunque stesse dirigendosi la discussione, cessa piuttosto in fretta appena tutti lo capiamo, e mangiamo."

"Dopo un po' suona la campana, ma Misha non tenta di dirlo a Shizune, così sono sicuro che hanno in mente di saltare le lezioni e passare il resto della giornata di nuovo qui dentro."

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Hicchan, hai qualche progetto per il festival?"

hi "No, non proprio. Dopotutto, sono qui solo da una settimana, cosa avrei potuto organizzare in quel tempo?"

show misha cross_laugh at twoleft
with charachange

mi "Wahaha~! Hicchan, ci hai aiutato così tanto, non sottovalutarti!"

hi "Okay."

show shizu basic_angry at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange

mi "Diciamo sul serio~!"

hi "Okay!"

"Loro due sembrano indignarsi per le cose più strane."

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Però ci andrai, vero, Hicchan? Dovresti almeno vedere cosa abbiamo rea-lizzato…? Tutti dovrebbero poter guardare quello che hanno fatto così da comprendere pienamente il loro lavoro, quello è ciò che credo~! Tu non fai eccezione!"

show misha perky_smile at twoleft
with charachange

mi "Hicchan, dovresti decisamente andarci~! Se non hai nessun piano, allora forse possiamo perfino andarci insieme~!"

show shizu adjust_blush at tworight
with charachange

hi "Avete bisogno di una mano? Se c'è qualcosa per cui avete bisogno di aiuto, mi sta bene di restare."

"Mi sento molto più tranquillo di prima; le mie precedenti preoccupazioni e paure se ne sono andate. Mi ero completamente dimenticato del guaio di stamattina finora, divertendomi a questo modo con Shizune."

"Divertirmi con Shizune… Sembra un concetto strano a cui pensare, ma, ripensandoci, mi sono veramente goduto i momenti che ho passato con Shizune e Misha in questi ultimi giorni, a dispetto di tutto."

"Se potremmo andare insieme, allora forse posso permettermi di restare un po' più a lungo. E suppongo che sia meglio delle lezioni."

show shizu behind_blank at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Davvero, Hicchan? Okay~! Possiamo considerare questo il tuo ripagarci per il nostro pranzo gratis~!"

show misha cross_laugh at twoleft
with charachange

mi "Grande, questo è grande, davvero~ davvero~ grande~! Shicchan stava sperando di parlarne comunque più tardi! Ahahaha~! Wahahahahaha~!"

"Quello non è affatto un pranzo gratis. Normalmente sarei arrabbiato, o almeno leggermente turbato, ma il mio umore è migliorato rispetto a prima, così lascerò passare."

"Aiutarle risulta consistere soprattutto di timbrare moduli e fare quelle che sembrano essere diecimila copie di ciascuno di cinquanta diversi resoconti di bilancio."

"Non è difficile, ma è molto noioso, e secondo Misha, è il più semplice dei compiti che trattano."

"Mi sento diventare sempre più stanco, e con quello, meno disposto a rientrare in classe. Questo è particolarmente male perchè più tempo passo fuori dall' aula, più sembra difficile alzarmi e tornarci."

"Queste due sono una pessima influenza. Pessimi modelli di comportamento. Non che mi preoccupi troppo, e sono sicuro che nessuno le ammiri, ma è una questione di principio…"

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Fatto~!"

hi "Ah, siete state veloci. Io penso che avrò finito prima che sia passata questa lezione."

show misha sign_smile at twoleft
with charachange

mi "No, no, Hicchan, è tutto fatto. Così, anche tu hai finito~!"

hi "Quello non ha senso, mi stai dicendo che questo è tutto arbitrario e mi avete fatto restare qui tanto per fare?"

show misha hips_grin at twoleft
with charachange

mi "No~…"

show shizu basic_normal at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Ma ti abbiamo trattenuto abbastanza~! Dovresti tornare in classe, Hicchan~! Puoi ancora farcela per la maggior parte di questa lezione!"

hi "E voi?"

show shizu behind_blank at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Certo che veniamo anche noi, certo; arriviamo subito!"

stop music fadeout 2.0

scene bg school_hallway3
with locationchange

"Rassicurato, comincio a tornare in classe, ma la lezione è passata quasi per metà, così a metà strada comincio a pensare che sarebbe inutile e passo il tempo restante tra questa lezione e la prossima bevendo succo di frutta nel corridoio."

"Tengo d' occhio la porta dell' ufficio del consiglio studentesco, ma non si apre. Che cosa le sta trattenendo?"

"Sono impegnate a terminare la mia parte del lavoro? Bè, non dovrebbe richiedere così tanto tempo, a meno che non ce ne sia altro, e che volessero solo che me ne andassi."

"Più ci penso, e più mi sembra probabile."

"Shizune è… beh, non stupida, ma chiaramente, è incapace di dire come le cose stanno veramente."

"Forse è perchè non può parlare, così è più difficile per lei. Ha Misha, ma tutto considerato, per quanto lo facciano sembrare facile, c'è ancora una differenza tra parlare informalmente e la lingua dei segni."

play sound sfx_normalbell

"Prendo in considerazione di rientrare per vedere come se la stanno cavando, ma suona la campana, e devo andare a lezione."

scene bg school_scienceroom
with locationchange

"Mi raggiungono pochi minuti più tardi, e i pensieri che avevo in mente prima sfuggono nella routine della vita scolastica."

with shorttimeskip

"Quando mi ricordo di nuovo, le lezioni sono terminate per oggi e sono troppo stanco per fare altro che non sia rientrare, lavorare ai miei compiti, e andare a dormire."

scene black
with Dissolve(3.0)


#***************

label it_A29:

scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors
play music music_emi fadein 0.3

show emi basic_happy
with charaenter

emi "Hisao!"

show emi excited_proud
with charachange

emi "Ti sto per fare un' offerta unica, super extra speciale per il pranzo!"

show emi excited_laugh
with charachange

emi "Pranzi fatti in casa di Emi, e il privilegio di goderseli in privato con due bellezze esplosive!"

"Il suo troppo civettuolo discorsetto da imbonitore echeggia nel corridoio, un' impresa rimarchevole dato che è pieno di gente."

show emi basic_closedgrin
with charachange

"Emi assume una posa dall' aria molto sicura di sè come se fosse un tentativo di battere quanto sia già stata ridicola, gonfiando il suo molto modesto petto e facendo il segno di V per vittoria con la mano."

hi "Sembra delizioso. A cosa devo questo onore di essere invitato?"

show emi excited_proud
with charachange

emi "Te ne stavi lì con aria davvero persa e triste così ho pensato che avresti gradito un po' di compagnia."

"Quella è probabilmente la ragione più deprimente immaginabile."

show emi basic_closedgrin
with charachange

emi "Così che ne dici? Probabilmente sei davvero solo e finiresti per mangiare quel tremendo cibo della mensa altrimenti, tutto solo."

hi "Eeeh…"

show emi excited_proud
with charachange

emi "Scherzo, scherzo!"

hi "Certo, accetterò la tua offerta. Con piacere."

show emi basic_happy
with charachange

emi "Andiamo sul tetto!"

hi "Il tetto?"

hi "Perchè il tetto?"

show emi basic_closedgrin
with charachange

emi "Perchè è lì che pranziamo!"

emi "E se non vado lassù, probabilmente lei se ne andrà in giro e allora sono sicura che resterà afffamanta perchè non prepara mai un pranzo per sè stessa!"

hi "Chi?"

show emi basic_closedhappy
with charachange

emi "Vieni con me!"
    
"Senza rispondere alla mia domanda o aspettare una risposta, mi afferra per un braccio e mi trascina attraverso i corridoi."

"Tento di fare conversazione lungo la strada."

hi "Perchè hai un pranzo in più?"

show emi sad_grin
with charachange

"Emi sorride colpevolmente."
 
emi "A dire la verità, è il pranzo di ieri."

emi "Ho fatto una corsa all' ora di pranzo e ho dimenticato di mangiarlo."

"Huh."
    
stop ambient fadeout 1.0

# The line above will go wherever the scene changes from out of the hallway, I guess.


label it_A29x:

"La sua espressione è così buffa che quasi rido forte."

"Emi ride, da sola o per un motivo o l' altro, o forse proprio per nessuna ragione. Mi piace il suono che fa."

"La natura solare ed energica di Emi allevia il senso di costrizione nella mia testa dopo la zuffa con Shizune e Misha."

"Lascio che quella questione scivoli via dalla mia mente, e sorrido per la prima volta oggi."



label it_A29a:

#and this is what happens if you had a heart flutter:
scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors

"Normalmente, mi unirei alle masse e andrei in cerca anche io di un pranzo, ma oggi è diverso."

"Oggi, sono stato invitato a pranzare sul tetto."

"Un posto strano, ma è dove mi è stato detto di andare."

"Fortunatamente, riesco a trovare scampo dalla tempesta nell' attracco provvisto dalla porta dell' aula."

stop ambient fadeout 1.0

hide crowd
with Dissolve(2.0)

"Alla fine il torrente cessa ed esco sperimentalmente fuori nel corridoio."

"Solo per essere incontrato da Emi, che sta avanzando baldanzosamente lungo il corridoio come una palla di cannone."

play music music_emi fadein 0.3

show emi basic_happy
with charaenter

emi "Ehi! Ciao Hisao! Ottimo tempismo!"

show emi excited_proud
with charachange

emi "Ho un super extra pranzo oggi, come promesso! Saliamo le scale!"
    

    
label it_A29b:
    
#Finally, this is where the two join up again

scene bg school_staircase1
with locationchange

"La scala per il tetto è un po' malridotta, ma è chiaramente stata usata di recente."

"In cima alle scale c'è una porta, completa di lucchetto mancante."

"Mi chiedo chi è stato l' individuo intrepido che ha rimosso il lucchetto?"

scene bg school_roof at bgright
show emi basic_closedgrin
with Fade(0.5,0.3,1.0,color="#FFF")

"Emi spinge aprendo la porta e cammina con un sorriso smagliante nella luce del sole."

stop music fadeout 1.0

show rin silhouette at offscreenright
with None

show bg school_roof
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease

show emi basic_shock at left
with vpunch

"Improvvisamente, un' alta ombra appare dal nulla, stagliandosi imponente di fronte a noi. Emi indietreggia, quasi cadendo giù dalle scale."

$ doublespeak (emi, rin, "Eeek!", "Salve.")

show emi basic_hes at left
with charachange

show emi basic_hes at twoleft
with charamove

emi "Aaah! Mi hai spaventato, Rin!"

"Aspetta, non è che…"

#Show Rin sprite now
show rin relaxed_surprised at tworight
with charachange

play music music_rin fadein 0.3

rin "Salve."

"Notando che Rin sta parlando con me, Emi mi guarda con aria curiosa."

show emi basic_confused at twoleft
with charachange

emi "Voi due vi conoscete?"

"Guardo Emi confuso."

hi "E' lei l' amica di cui parlavi?"

show rin relaxed_nonchalant at tworight
with charachange

"Rin ha diretto il suo sguardo verso le nuvole che stanno vagando al di sopra della scuola."

rin "Non sapevo che tu conoscessi questa persona, Emi."

stop music fadeout 2.0

"…"

"Il silenzio imbarazzante dura solo per pochi secondi finchè Emi si lascia sfuggire una piccola risatina, ignorando la coincidenza."

show emi basic_closedgrin at twoleft
with charachange

emi "Ho invitato Hisao a pranzo. Se lo conosci, tanto meglio."

show rin basic_deadpan at tworight
with charachange

rin "Oh. Questo vuol dire che io non avrò da mangiare? O lo hai invitato a pranzo senza il pranzo?"

show emi basic_grin at twoleft
with charachange

emi "Uhh, nessuno dei due, ho da mangiare per tre."

show rin basic_deadpanamused at tworight
with charachange

rin "Buona idea."

hide rin
hide emi
with charaexit

"Camminano fino all' altro capo del tetto mentre io rimango alla torre dell' orologio per un po', assorbendo l' atmosfera."

play music music_soothing fadein 0.3

"Non c'è nessuno qui oltre a noi. Suppongo che il tetto non sia popolare quanto lo è in altre scuole."

"Alcune panchine e tavole dall' aria malconcia sono sparse qua e là intorno al bordo, forse in un tentativo di rendere il tetto meno desolato."

"I ciottoli che coprono il tetto scricchiolano sotto i nostri piedi."

"Sbircio oltre il reticolato del recinto per dare un' occhiata ai terreni della scuola e oltre."

"Gli studenti stanno passeggiando in coppie e gruppi per il campus e alla mensa."

"Alcuni camion di trasporti stanno oltrepassando la scuola dirigendosi verso il minimarket vicino."

"Da qualche parte un cane da guardia abbaia a un passante."

"In qualche modo, quando guardo verso il centro cittadino la sensazione della piccola città mi colpisce molto fortemente, quasi palpabilmente."

"Lo stile di vita frenetico delle grandi metropoli sembra così distante ed estraneo qui; nessuno deve correre per prendere un autobus come se la loro vita dipendesse da quello o deve farsi sovraccaricare i sensi dalle luci al neon e gli ingorghi di traffico."

"Mi sento sorprendentemente ottimista riguardo a questa mia nuova vita, guardando la mia nuova città, anche se sarà mia solo per un breve anno."

"Scoprire la mia malattia e dover traslocare lontano da casa mi sono caduti addosso così improvvisamente che non ho avuto tempo per pensare su come mi sento."

"Quando cammino all' aperto fuori dall' ombra della torre dell' orologio sento del calore toccare la mia schiena."

"Il sole splende da un cielo ceruleo perfettamente terso."

"Una brezza fredda che spazza il tetto mi fa rabbrividire, ma solo per un momento."

"Il vento porta l' odore di alberi e fiori, non smog e scarichi d' auto come faceva solo poche settimane fa."

"Emi si accomoda su una panchina con Rin al traino ed estrae una scatola portapranzo grande e due piccole dalla sua borsa."

show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter

emi "Muoviti, Hisao! Cosa stai aspettando?"

"Mi sta facendo segno di unirmi a loro, facendo spazio sulla già piccola panchina."

hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft

show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof
with charamoveinleft


"Mi siedo sull' angolo della panchina per occupare quanto meno spazio possibile. Si sta piuttosto stretti, ma in qualche modo tutti e tre riusciamo a starci sopra."

hi "Bel panorama."

show emi basic_closedhappy_close at closeleft
with charachange

"Emi reprime una risatina e piazza un portapranzo di fronte a Rin, e ne passa un altro a me."

show emi excited_proud_close at closeleft
with charachange

emi "Ecco a voi! Il pranzo, come promesso!"

"Fatto in casa, nientemeno. Sono impressionato."

hi "Wow. Sembra davvero ottimo."

show emi excited_amused_close at closeleft
with charachange

emi "Grazie! Li preparo io quando posso."

"La conversazione cessa mentre mi dedico all' attività di nutrirmi."

show rin basic_awayabsent_close at closeright
with charachange

"Masticando qualche morso, alzo lo sguardo e noto Rin che apre abilmente la sua scatola portapranzo e si ficca una forchettata di cibo in bocca usando solo i suoi piedi."

"Anche se l' ho già visto prima, non riesco a non essere impressionato dalla sua destrezza."

"Mi fa anche tornare in mente il tipo di luogo in cui mi trovo ora."

"Mi abituerò mai a vedere cose del genere?"

"Non riesco neanche a decidere se abituarmi a una cosa simile sarebbe un bene o un male."

"Abituarmi a questo posto significa che sto rinunciando a essere una persona normale?"

"O vuol solo dire che sto diventando più comprensivo nei confronti di chi mi circonda?"

"Vengo distratto dai miei pensieri dalla vista di Emi che sta massacrando il suo pranzo come se avesse insultato i suoi antenati."

show rin basic_absent_close at closeright
with charachange

hi "Sembri piuttosto affamata."

show emi basic_grin_close at closeleft
with charachange

"Emi alza lo sguardo, bocca mezza piena, e inghiotte prima di annuire."

emi "La mia corsa mattutina mi fa sempre venire un gran appetito."

show emi basic_closedhappy_close at closeleft
with charachange

emi "Il che è ottimo, perchè così brucio via il pranzo piuttosto in fretta."

show emi excited_proud_close at closeleft
with charachange

emi "Mi aiuta a conservare la mia figura femminile."

show rin basic_deadpan_close at closeright
with charachange

rin "Cosa succederebbe se la perdessi? Diventeresti un uomo?"

"Per un pelo non mi strozzo col mio pranzo cercando di non ridere."

show emi basic_annoyed_close at closeleft
with charachange

emi "E' un modo di dire."

show rin basic_deadpandelight_close at closeright
with charachange

rin "Anche la tua figura deve correre di mattina?"

hi "Voi due parlate sempre in questo modo?"

show rin relaxed_surprised_close at closeright
show emi basic_confused_close at closeleft
with charachange

$ doublespeak (emi, rin, "Parliamo in che modo?", "In che modo?")

"Credo che quello risponda alla mia domanda."

hi "Ehh, come non detto."
    
hi "Così, uh…"

"Lotto per pensare a un argomento di conversazione e mi decido per l' ovvia domanda."

hi "Come vi siete incontrate?"

show rin basic_awayabsent_close at closeright
with charachange

"Rin sembra soddisfatta di lasciare che Emi risponda a questa domanda."

show emi basic_grin_close at closeleft
with charachange

emi "Qualcuno all' assegnazione alloggi ha pensato che ci saremmo complementate bene, così ci hanno assegnato stanze adiacenti."

hi "Complementate?"

show rin basic_deadpannormal_close at closeright
with charachange

rin "Come scarpe e una giacca."

hi "Eh?"

show emi basic_closedgrin_close at closeleft
with charachange

"Emi ride alla mia confusione."

emi "Mettici insieme e abbiamo tutti i nostri arti, capisci?"

hi "Ah."

show emi basic_happy_close at closeleft
with charachange

emi "Così ho cominciato ad aiutare Rin a prepararsi di mattina, e questo è quanto!"

show emi basic_grin_close at closeleft
with charachange

emi "Voglio dire, non puoi aiutare qualcuno a vestirsi tutte le mattine e non andarci d' accordo."

hi "Capisco."

"Rin sceglie questo momento per interrompere."

show rin basic_deadpan_close at closeright
with charachange

rin "Ho dei problemi con le camicie."

hi "Giusto, quello sembra… piuttosto ovvio."

show rin basic_surprised_close at closeright
with charachange

rin "Davvero?"

hi "Abbastanza…?"

"Questo non aiuta, ma almeno Emi sembra trovare l' intero affare buffo."

"E quello, combinato col fatto che Rin è genuinamente curiosa, mi fa sentire lievemente meglio e allo stesso tempo mi confonde."

hi "Voglio dire, non hai le braccia."

hi "Così uh, indossare una camicia sembra essere una di quelle cose che sarebbero… difficili."

"Sapete che vi dico? Adesso smetto di parlare."

"Mi risparmierà un sacco di guai a lungo termine."

"Rin annuisce con quella che sospetto sia intesa essere un' aria saggia."

show rin basic_lucid_close at closeright
with charachange

rin "Capisco."

show rin basic_absent_close at closeright
with charachange

"La conversazione cessa quando rivolgo di nuovo la mia attenzione al mio pranzo."

"E' davvero molto buono."

"Emi finisce il suo pranzo per prima e fa un rumore soddisfatto."

show emi excited_laugh_close at closeleft
with charachange

emi "Ah, era ottimo."

"Mentre si dà da fare col riordinare la sua roba, Rin parla."

show rin basic_deadpan_close at closeright
with charachange

rin "Ho sete."

show emi basic_shock_close at closeleft
with charachange

emi "Oh! Quasi me ne ero scordata! Scusa!"

show emi basic_closedgrin_close at closeleft
with charachange

"Con un gesto da prestigiatrice, fruga nella sua borsa e preleva un trio di cartoni di succo."

"Me ne lancia uno che sembra essere succo di mirtilli, uno a Rin che sembra essere una sorta di latte alla fragola (completo di schema di colori rosa), e tiene un (ugualmente rosa) cartone di un qualche tipo di cocktail di frutta per sè."

show rin basic_awayabsent_close at closeright
with charachange

"Rin conficca destramente la sua cannuccia attraverso la cima del suo cartone e comincia a bere."

"Sono nuovamente impressionato da quanto sia flessibile, ma stavolta tengo il mio commento per me."

"Per qualche motivo non penso che nè Emi nè Rin siano il tipo di persona che pensa due volte alla maniera in cui aggirano le loro particolari disabilità."

"Particolarmente Rin."

"Infatti, lei dà l' impressione di essere completamente non a conoscenza del fatto che le mancano degli arti."

"Che quella sia o no una decisione conscia è un altro discorso."

"Davvero non ne sono sicuro."

show emi basic_grin_close at closeleft
with charachange

emi "Così Hisao, ti piace questo posto?"

show rin basic_absent_close at closeright
with charachange

hi "Hmm?"

hi "A dire il vero, è molto bello. Mi piacciono i posti alti, per il panorama."

hi "Grazie per avermi invitato."

hi "E anche per il pranzo."

show emi excited_amused_close at closeleft
with charachange

"Emi spara un sorriso da mille watt, immagino compiaciuta dalla mia risposta."

emi "Nessun problema!"

show emi excited_proud_close at closeleft
with charachange

emi "Sentiti libero di mangiare ancora insieme a noi, okay?"

emi "Non ti preparerò un pranzo, ma puoi portare il tuo quassù."

hi "Niente servizio pranzo? Non saprei…"

show emi basic_annoyed_close at closeleft
with charachange

"Emi finge di essere offesa."

emi "Stai cercando di approfittare del mio buon cuore?"

emi "Che faccia tosta!"

show emi basic_closedgrin_close at closeleft
with charachange

"Fa una risatina."

show emi sad_depressed_close at closeleft
with charachange

emi "Bene, se quella è la tua risposta, suppongo che io e Rin continueremo semplicemente a mangiare il pranzo tutte sole…"

"Vengo improvvisamente assaltato dal paio di occhi da cerbiatto più strappacuore che abbia mai visto quando Emi fa il broncio."

hi "Scherzavo! Stavo scherzando!"

hi "Adorerei pranzare di nuovo quassù."

hi "Buon posto, e anche la compagnia è okay."

show emi basic_grin_close at closeleft
with charachange

"Emi fa un po' la faccia scura alla mia dichiarazione di “okay” ma sembra abbastanza contenta che abbia accettato il suo invito."

"Immagino che questo ci renda amici ora."

"O almeno conoscenti."

play sound sfx_normalbell

"La campana del pranzo suona, segnalando un ritorno ai piani inferiori."

show emi basic_hes_close at closeleft
with charachange

emi "Rin, non hai finito di nuovo il tuo pranzo!"

show rin basic_deadpan_close at closeright
with charachange

rin "Non ero così affamata."

show emi basic_annoyed_close at closeleft
with charachange

emi "Se non mangi di più, finirai per svanire!"

show rin relaxed_boredom_close at closeright
with charachange

"Rin scrolla le spalle, come se questo fosse un rischio accettabile."

stop music fadeout 4.0

hi "Forza, faremo meglio ad andare."

scene bg school_staircase1
with locationchange

"Scendiamo tutti e tre per le scale insieme."

scene bg school_scienceroom
with shorttimeskip

"Le lezioni pomeridiane passano, e ancora una volta mi ritrovo senza un piano per il doposcuola così mi dirigo in biblioteca per restituire un paio di libri che ho finito di leggere."

scene bg school_library
with locationskip

play music music_happiness fadein 0.3

"Entrando, vedo che ci sono più o meno tanti studenti quanti ce ne erano martedì, il che è ancora più evidente grazie al quasi totale silenzio che avvolge la stanza."

play sound sfx_impact2

with vpunch

show yuuko panic
with easeinbottom

"Quando lascio cadere la pila di libri che avevo preso a prestito nella buca per le restituzioni del bancone, Yuuko compare improvvisamente da dietro di esso, presa di sorpresa dal botto che fanno quando arrivano in fondo al carrello accanto a lei."

hi "Ah, scusa Yuuko. Non volevo spaventarti."

show yuuko worried
with charachange

yu "No, no. Va tutto bene. Capita… spesso. Ormai ci sono abituata."

show yuuko neurotic
with charachange

yu "Um, posso esserti di aiuto?"

hi "Non importa, credo di sapere dove è tutto. Grazie comunque."

hide yuuko
with charaexit

"Suppongo che prenderò un altro libro o due già che sono qui. Non c'è molto altro da fare, e dopo avere letto così tanto durante la mia permanenza in ospedale, è diventata un' abitudine dura da perdere."

stop music fadeout 8.0

"Vago giù per la sezione narrativa verso il retro della biblioteca, controllando gli scaffali in cerca di qualcosa che attragga la mia attenzione."

"Mentre lo faccio, guardo verso l' angolo dove si trovava Hanako l' ultima volta che sono stato qui, non aspettandomi veramente nulla."

scene ev hana_library_read_std
with locationskip

"…sorprendentemente, però, lei è lì, completamente assorta in un libro piuttosto spesso. Decido di non disturbarla come l' ultima volta e torno a cercare materiale di lettura."

scene bg school_library_ss
with shorttimeskip

"Dopo un' indiscernibile quantità di tempo spesa a esaminare le corsie, finalmente mi decido per un paio di libri e li estraggo dallo scaffale."

"Senza nessun problema, cammino svelto fino al bancone, registro i miei libri in prestito e li ficco nella mia borsa mentre esco."

scene bg school_courtyard_ss
with locationskip

"Quando finalmente lascio l' edificio principale, il tramonto non è troppo lontano. Rimane una manciata di studenti, ma la maggioranza se ne sono andati; presumibilmente verso le loro case o i dormitori."



label it_A29c:

scene bg school_dormhisao_ss
with locationskip

"Sentendomi completamente esausto, mi dirigo verso la mia stanza per leggere i libri che ho preso a prestito. C'è già stata abbastanza azione ed eccitazione per un giorno solo."

play music music_night fadein 0.3

"Il primo è “Le avventure di Alice nel paese delle meraviglie”. Conosco la storia, ovviamente, ma non ho mai davvero letto il libro originale."

"E' tanto bizzarro quanto ricordo sia la storia, con i buffi personaggi e la trama priva di senso."

"Comincio a pensare anche a me stesso come a una specie di Alice, sventuratamente rotolante giù per la tana del coniglio in questo Paese degli storpi."
    
"…Okay, quella era un' espressione piuttosto forte. Però, la locazione isolata e la maniera in cui la scuola apertamente si adatta ad assolutamente qualunque cosa è inquietante. E' come un altro mondo."

"Mi chiedo perchè non posso liberarmi della sensazione di essere un estraneo come Alice, nonostante che praticamente tutti siano così ospitali e amichevoli con me."

"Girando un' altra pagina, la mia mente comincia ad andare alla deriva lontano dal libro. C'è silenzio, posso sentire il battito del mio cuore contro la stoffa della mia camicia."
    
"Per qualche ragione, mi fa sentire veramente male come sempre da quella volta nella foresta con Iwanako. Come se fossi chiuso in una gabbia con qualcosa di cattivo e spaventoso."

scene bg school_dormhisao_ni
with Dissolve(3.0)

"Metto giù il libro per un po' e fisso il soffitto, prendendomi il mio tempo per liberarmi della sensazione."

"200 pagine più tardi, cado addormentato."

stop music fadeout 2.0

scene black
with shuteye


#*********************
    
label it_A30:

scene bg school_courtyard_ss
with None

"Suppongo di dover comprare qualcosa da mangiare. Non posso vivere di cibo della mensa e mangiare fuori per tutta la mia permanenza qui."

scene bg school_gate_ss
with locationchange

"Mentre mi dirigo verso il cancello, mi stiracchio rumorosamente alcune volte per cercare di tenere a bada la stanchezza che si è accumulata durante la settimana."

scene bg school_road_ss
show lilly back_smileclosed_ss
with locationchange

"Dopo esserci passato attraverso e aver girato l' angolo, però, vedo una figura solitaria che sta camminando giù per la collina verso la città sotto di noi. Il colore dei suoi capelli e il battere del suo bastone sono inconfondibili."

show lilly cane_surprised_ss
with charachange

"Cammino rapidamente fino a raggiungerla, un' azione che sembra attrarre la sua attenzione senza bisogno di dire una parola."

hi "Ciao, Lilly."

show lilly cane_weaksmile_ss
with charachange

"Ci mette un momento per identificare la voce, aggiustando leggermente la posizione della sua testa per puntare un po' più verso la fonte della mia voce mentre lo fa."

play music music_lilly fadein 0.3

show lilly cane_smile_ss
with charachange

li "…Hisao?"

hi "Yep, sono io."

"Sembra avere una buona memoria per le voci. Il fatto che si sia ricordata è una piacevole sorpresa."

li "Buona sera. Cosa ti porta qui?"

show lilly cane_weaksmile_ss
with charachange

"Di nuovo, fa un piccolo cortese inchino. E, di nuovo, rispondo allo stesso modo prima di realizzare che non è necessario che lo faccia."

hi "Sto solo andando in città. E tu?"

show lilly cane_ara_ss
with charachange

li "Oh cielo, che coincidenza."

hi "Stai facendo lo stesso, eh?"

show lilly cane_smile_ss
with charachange

li "Mm. Di solito vado a fare compere di venerdì."

show lilly cane_surprised_ss
with charachange

"Fa una breve pausa, improvvisamente sembrando un po' persa."

li "Detto quello, Hanako di solito viene in città con me…"

"Ah. Non persa, ma preoccupata. Le due sembrano sorvegliarsi a vicenda piuttosto da vicino. E' abbastanza sorprendente che Hanako si dimentichi di Lilly in questo modo."

hi "L' ho vista che leggeva in biblioteca. Probabilmente è solo rimasta presa da un libro."

show lilly cane_weaksmile_ss
with charachange

"Rilascia un piccolo sospiro di sollievo."

li "Grazie. Ha l' abitudine di farlo."

hi "Avida lettrice?"

show lilly cane_smile_ss
with charachange

li "Giusto. Non le piace essere in mezzo a folle di gente, così leggere lontana da tutti la lascia rilassare un po'."

"Anche se probabilmente non intendeva farlo, non posso fare a meno di fare una smorfia mentre mi ricorda il mio primo incontro con lei."

show lilly cane_smileclosed_ss
with charachange

"Non volendo affatto menzionarlo, resto in silenzio mentre continuiamo a camminare tranquillamente lungo la strada silenziosa."

"Tac, tac. Tac, tac."

"Con la strada spoglia di auto e gli studenti di Yamaku sempre più distanti dietro di noi, il quieto stormire delle foglie e il misurato battito del bastone di Lilly contro il marciapiede sono tutto quel che si può sentire."

"E' abbastanza piacevole, specie paragonato al trambusto di dove abitavo una volta."

"Prima che me ne accorga, mi sono rilassato a tal punto che un sonoro sbadiglio mi sfugge prima che lo possa controllare."

show lilly cane_giggle_ss
with charachange

li "Stanco?"

hi "Già, mi hanno fatto correre come un dannato questi ultimi giorni."

"E' un eufemismo, direi. Trasferirsi in una scuola diversa sarebbe già abbastanza duro, ma non quanto questo…"

show lilly cane_smile_ss
with charachange

li "Bene, sperabilmente tutto dovrebbe sistemarsi per te. Il festival sta eccitando tutti ora come ora, e tu sei stato buttato nel bel mezzo delle cose."

"Per un momento esito, ma data la sua apparente tolleranza per la franchezza decido di dire tutto quel che penso."

hi "Suppongo di sì. Yamaku è abbastanza differente però. Voglio dire, la formalità che circonda tutto, l' isolamento intorno a essa… per non menzionare la differenza più ovvia."

hi "E' una specie di atteggiamento mentale completamente diverso. Immagino che mi ci abituerò però, col tempo."

show lilly cane_smileclosed_ss
with charachange

"Fa un cenno di assenso dall' aria molto pratica, apparentemente compiaciuta dalla mia risposta. Sembra quasi che mi abbia incluso nel gregge di studenti che sta guidando, insieme alla classe 3-3 ed Hanako."

"Bè, non che mi dispiaccia. E' bello poter parlare liberamente, in ogni caso."

show lilly cane_smile_ss
with charachange

li "Guardando al lato positivo, uno potrebbe vederla come una possibilità di cominciare di nuovo. Dovresti tener cara la possibilità di farti nuovi amici."

"E' ottimistico. Ciononostante, è un bene avere un atteggiamento positivo verso cose del genere, immagino."

hi "Suppongo che sia un buon punto di vista sulla cosa."

scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss
with shorttimeskip

"Mentre camminiamo lungo la strada, sembra diventare un po' turbata. Prima che possa chiederle a cosa sta pensando, sembra riprendersi e parla di altro."

show lilly cane_weaksmile_ss
with charachange

li "Così, dove stavi andando in città?"

"A dire il vero quella è una buona domanda. Sono venuto a comprare del cibo, ma la disposizione della città mi è ancora completamente estranea."

"Avevo solo intenzione di gironzolare un po' e vedere cosa riuscivo a trovare, ma col tramonto che si sta già avvicinando e la notte non troppo lontana, non sembra molto saggio farlo."

"Dovrò chiederle delle indicazioni. Di nuovo."

hi "Volevo solo prendere qualcosa da mangiare… ma ora che lo dici, non so davvero dove andare."

show lilly cane_planned_ss
with charachange

li "Bene allora, questo è un colpo di fortuna. Avevo proprio intenzione di andare al minimarket anche io."

hi "Sembra che mi farai nuovamente da guida, allora. Grazie."

"Insieme camminiamo fino al negozio, i miei passi attentamente rallentati per rimanerle al fianco. Paragonato al solito passo con cui cammino, il suo è alquanto più lento. Non che non ci sia una buona ragione."

scene bg suburb_konbiniext_ss
with shorttimeskip

"Dopo quel che non può essere più di diversi minuti, scorgo il nostro obiettivo. Questa città è davvero piuttosto piccola."

scene bg suburb_konbiniint
with locationchange

"Senza ulteriori indugi, entriamo ricevendo un saluto dal bancone."

stop music fadeout 2.0

show lilly cane_weaksmile
with charaenter

li "Ti dispiace se ti seguo? Di solito mi aiuterebbe Hanako, ma dato che non è qui…"

"Ci metto un momento prima di capire cosa vuol dire."

"Considerando che non potrebbe leggere nessuna delle etichette, far compere senza alcun aiuto sarebbe una grossa fatica per lei."

"Detto questo, non riesco a liberarmi della sensazione che avesse quest' idea fin da quando ho detto che stavo venendo qui."

play music music_soothing fadein 0.3

hi "Certamente. Sarebbe un piacere."

"Afferro due cestini rossi consunti dalla piccola pila accanto all' entrata, passandone uno a Lilly."

show lilly cane_weaksmile at Position(ypos=800)
with charamove

show lilly basic_smileclosed at Position(ypos=800)
with charachange

show lilly basic_smileclosed
with charamove


"Lei lo appoggia a terra, mettendoci dentro la sua borsa da scuola, retraendo il suo bastone e facendolo scivolare attraverso le maniglie del cestino prima di raccoglierlo nella destra."

"Aspetta, se non usa il suo bastone…"

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"Prima che possa completare il pensiero, si avvicina al mio fianco e prende il polsino destro della mia uniforme tra le sue dita snelle."

show lilly basic_concerned_close at twoleft
with characlose

li "Così può andare?"

hi "Ah, certo."

show lilly basic_smileclosed_close at twoleft
with characlose

"Non ho ragione per non accettare. Posso pensare a cose peggiori che fare compere con una bella ragazza che si tiene stretta a me, anche se è per necessità."

"Navighiamo attraverso il negozio, senza che uno degli occasionali clienti di passaggio sembri battere ciglio."

"Considerando quanto è vicina Yamaku, immagino che vedere degli studenti provenienti da lì deve essere completamente normale per i residenti locali."

"Quando raggiungiamo ogni corsia, controllo rapidamente con Lilly per sapere di cosa ha bisogno. Lo prendo assieme a quello che voglio io, e metto le nostre compere nei rispettivi cestini."

"Immagino che questa sia la stessa routine che lei e Hanako seguono ogni venerdì."

hi "A posto, rimane solo il pane e quello dovrebbe essere tutto per me. Ti serve qualcos' altro, Lilly?"

show lilly basic_smile_close at twoleft
with characlose

li "No, questo dovrebbe essere tutto."

hi "Andiamo, allora."

show lilly basic_smileclosed_close at twoleft
with characlose

"Dopo una rapida deviazione verso la sezione panetteria, ci dirigiamo verso la cassa."
    
"La coda, grazie al cielo, è quasi inesistente. In pochi minuti abbiamo entrambi pagato per il nostro cibo e siamo fuori dalla porta."

scene bg misc_sky_ni at Fullpan(15.0)
with locationchange

"Mentre Lilly recupera il suo bastone e lo estende completamente, io perdo un momento a guardare su verso il cielo notturno mentre tengo le nostre borse."

"Per un momento provo a fare nuvole col mio alito, ma il calore dell' estate non sembra cooperare."
    
"Alla fine lei si raddrizza, stirandosi un attimo prima di prendere la sua borsa lasciandomi le mie due."

scene bg suburb_konbiniext_ni
show lilly cane_listen_ni
with locationchange

hi "Sei stanca anche tu?"

show lilly cane_sleepy_ni
with charachange

li "Le preparazioni per il festival sono state un completo caos. E Shizune che mi alita sul collo non è stato esattamente un aiuto."

hi "Ehi, sta solo cercando di organizzare tutto. Meglio prima che poi, giusto?"

show lilly cane_weaksmile_ni
with charachange

li "Suppongo di sì. Apprezzerò il rilassarmi in città domani, questo è certo."

"Immagino che le preparazioni per il festival stiano costando fatica a entrambe."

stop music fadeout 4.0

scene bg suburb_roadcenter_ni at bgright
with locationchange

"Usciamo sulla strada silenziosa, parlando tra di noi mentre trasportiamo le nostre borse di cibo e altri acquisti dal negozio."

"…Un momento, cos'è quello?"

"Mi accorgo di una figura molto distintiva che procede verso di noi, messa in controluce dai lampioni."

"Per un secondo penso che sia un altro studente dalla mia classe, ma quando lui, o dovrei dire lei, si avvicina presto la riconosco."

show bg suburb_roadcenter_ni
show rin relaxed_nonchalant_ni at right
with charamoveinright

hi "Rin? Che stai facendo qua fuori così tardi?"

show lilly cane_surprised_ni
with charaenter

li "Rin?"

"Lilly solleva il capo, e sembra che stia cercando di concentrarsi sull' ascoltare più attentamente. Improvvisamente capisco che probabilmente dovrei interpretare la scena per lei."

hi "E' Rin… Tezuka credo fosse il suo cognome, dalla nostra scuola."

show lilly cane_weaksmile_ni
with charaenter

"Si irrigidisce sentendo il nome e assume un' espressione complicata, qualcosa come una fusione forzata di un sorriso composto e di una smorfia di dolore."

li "Ah. Capisco."

"Immagino che Lilly conosca anche Rin."

show rin basic_awayabsent_ni at right
with charachange

show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove

"Rin si gira per guardarci, sembrando terribilmente frastornata. Non sono completamente sicuro che ci riconosca, o almeno se lo fa, non lo dimostra."

"Sembra uno zombie. O una statua. Una statua di uno zombie."

"Ma lentamente, alcuni sintomi di comprensione sembrano illuminarsi nei suoi occhi scuri: questo è qualcosa a cui deve reagire."

show rin basic_lucid_ni at tworight
with charachange

show rin basic_awayabsent_ni at tworight
with charachange

"Rin sbatte le palpebre una volta. Molto scrupolosamente."

show rin basic_absent_ni at tworight
with charachange

rin "Salve."

"…"

"C'è una pausa imbarazzante, in cui tutti aspettano che qualcun altro dica qualcosa."

hi "Che stai facendo qua così tardi?"

"…"

rin "Io…"

play music music_rin fadein 0.3

show rin basic_deadpan_ni at tworight
with charachange

rin "Me lo stavo chiedendo anche io. Proprio ora."

show rin basic_deadpannormal_ni at tworight
with charachange

rin "Alcune persone me lo hanno chiesto poco prima. Assumo che stessero chiedendosi la stessa cosa."

rin "Non lo sapevo. Neanche loro lo sapevano. Ho chiesto. E' per quello che me lo sto chiedendo."

rin "Così questo è più o meno tutto. E' come l' assassinio misterioso in un giallo senza l' assassinio."

"…"

show rin negative_spaciness_ni at tworight
with charachange

rin "Stavano andando da quella parte."

show rin basic_absent_ni at tworight
with charachange

"Si gira a sinistra per dimostrare la direzione in cui le altre persone sono andate come se fosse importante, poi ruota indietro come un pupazzo meccanico in uno di quei marchingegni a orologeria eccessivamente complessi."

"Per una persona che dà l' impressione di essere il tipo silenzioso, Rin usa davvero un sacco di parole per dire cose che non hanno bisogno di molte parole per essere dette."

"Incerto se abbia finito o no non dico nulla. Nè lo fa Lilly, che sembra ugualmente derubata del dono della parola per il momento."

"Credo che stiamo in effetti entrambi solo temendo che una qualunque risposta potrebbe provocarla a continuare."

"La nostra stupefatta carenza di reazione non tocca affatto Rin. Lei continua a guardarci in attesa, un calmo inizio di espressione sul suo viso inespressivo."

"Sembra essere quel genere di persona. Sempre così rilassata."

"Come se una dose da elefante di sedativi stesse scorrendo nelle sue vene al posto del sangue."

show lilly cane_concerned_ni at twoleft
with charachange

li "Amnesia? Non ricordo che tu soffra di niente del genere, però…"

hi "No, non penso che sia quello."

hi "Gli altri passanti probabilmente erano solo preoccupati, però. Sembra davvero che ti sia persa, a giudicare dal modo in cui stai in mezzo alla strada."

show rin basic_deadpan_ni at tworight
with charachange

rin "Oh, capisco."

show rin relaxed_nonchalant_ni at tworight
with charachange

rin "Forse in quel caso avrei dovuto assumere un altro tipo di posa."
    
"Considero per un po' se perseguire ulteriormente questo discorso, o lasciar perdere per amor della mia sanità mentale."

"Decido per la seconda opzione."

"Sembra che la maggior parte delle volte, sia meglio non scavare troppo in profondità di quello che Rin sta bofonchiando."

"Parlare con Rin è come giocare a scacchi con un supercomputer che fa mosse apparentemente completamente casuali come per schernire tutto quello che sai degli scacchi. E' così, ma con l' interazione umana."

"E anche se vinco, mi sembra di avere perso."

"Dannazione, è proprio come aveva detto Kenji. Anche quando vinco, perdo. E' questo il potere delle ragazze di Yamaku?"

"…"

"Metto da parte il pensiero come troppo pericoloso da considerare ulteriormente. Probabilmente è solo la propaganda antifemminile di Kenji che mi ha preso in un momento di debolezza."

hi "Già, forse assumere un' altra posa avrebbe potuto funzionare."

hi "Ma comunque, non hai idea di cosa stai facendo qui?"

show rin negative_annoyed_ni at tworight
with charachange

"Si rabbuia, sembrando estremamente insoddisfatta dalla mia domanda, o dalle sue conseguenze, o dalla risposta che sta per dare."

rin "Ce l' ho. Parte di un' idea. Non posso davvero dire che tipo di idea."

show lilly cane_smile_ni at twoleft
with charachange

li "Quello sembra un progresso, almeno."

"Lilly suona come se avesse visto una possibilità per un qualche genere di conversazione discernibilmente normale. Non posso dire di condividere il suo ottimismo."

rin "Sì, ce n'è un po'. Decisamente. Il resto arriverà più tardi."

show rin basic_deadpanupset_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charachange

rin "Ne sono sicura. Ho sempre delle… ragioni."

"Il silenzio risultante uccide fin troppo visibilmente le speranze di Lilly. Non sono durate a lungo."

"A parte le sicurezze di Rin, per quanto posso capire prive di basi… che bisognerebbe fare?"

"Potremmo solo lasciarla ai suoi affari, qualsiasi essi siano… ma è tardi e non penso che riceveremmo dei ringraziamenti se Rin viene trovata qui in piedi nel bel mezzo della notte."

"Il che probabilmente succederà, a meno che lei non riesca a ricordare cosa stava facendo qui in primo luogo."

"Per quanto riguarda il mio tentare di indovinare cosa potrebbe essere passato nella sua testa quando ha deciso di imbarcarsi in questa avventura, le possibilità a favore sembrano pari a quelle di vincere la lotteria."

"Diverse volte consecutivamente."

"Anche Lilly è stranamente silenziosa. Adesso apprezzerei un po' di aiuto dall' esterno, specialmente se lei è più familiare con Rin di me."

"Ma non posso farci niente. Sembra che la sua familiarità con Rin sia esattamente il perchè stia rimanendo in silenzio."

hi "Così, assumo che tu stessi andando da qualche parte, non tornando a scuola… qualche idea di dove?"

show rin relaxed_surprised_ni at tworight
show lilly cane_surprised_ni at twoleft
with charachange

"I suoi occhi si spalancano in shock e sobbalza indietro in un modo un po' artificiale, facendolo sembrare come se fosse stato un numero preparato per situazioni come questa."

rin "Sai leggere il pensiero? E' quella la tua disabilità? E' così unica!"

hi "No… Cosa? Perchè penseresti una cosa del genere?"

show rin relaxed_disgust_ni at tworight
show lilly cane_listen_ni at twoleft
with charachange

rin "Sapevi cosa stavo facendo."

show lilly cane_displeased_ni at twoleft
with charachange

hi "Eh, è stata solo una deduzione fortunata. Prima abbiamo camminato per questa stessa strada nella direzione opposta, per arrivare al negozio."

hi "Se tu stessi andando a scuola, ti avremmo incontrata lungo la strada."

show rin basic_deadpanupset_ni at tworight
with charachange

rin "Oh."

"Sembra un poco delusa."

"Come Kenji, Rin è certo rapida a saltare a conclusioni completamente irrazionali."

"Forse è qualcosa nell' acqua. Prendo mentalmente nota di rifornirmi di bibite."

hi "Sai, questa è la seconda volta questa settimana che qualcuno mi chiede se so leggere il pensiero."

hi "Dò davvero un' impressione del genere?"

show rin basic_deadpannormal_ni at tworight
with charachange

"Rin scrolla le spalle e quella è tutta la risposta che ricevo."

hi "Sai-{w=0.3}{nw}"

show lilly cane_smile_ni at twoleft
with charachange

li "Forse dovresti tornare con noi a scuola?"

"Lilly si intromette proprio quando stavo per sfatare ulteriormente le mie supposte capacità telepatiche. Suona piuttosto preoccupata, e il sorriso forzato sul suo viso nasconde malamente questo fatto."

"Forse è giunta alla stessa mia conclusione. Decido di lasciare cadere l' argomento lettura del pensiero per il bene comune, è comunque futile."

hi "Già, Lilly ha ragione. Se non riesci a ricordare, non c'è motivo per restare qui."

show rin basic_awayabsent_ni at tworight
with charachange

"Rin considera questa piuttosto semplice deduzione per un momento, poi annuisce."

show rin basic_absent_ni at tworight
with charachange

rin "Okay."

stop music fadeout 2.0

scene bg school_road_ni
with shorttimeskip

"Così ci dirigiamo nuovamente verso la scuola, avendo perso molto più tempo del necessario con questo episodio."

show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter

"Rin cammina lungo il bordo del marciapiede nel suo modo aritmico, sembrando come una mistura di una sonnambula e di un' acrobata, mentre Lilly tiene una mano sulla mia spalla, tastando il terreno col suo bastone."

"Tac passo passo passo tac tac passo passo passo."

"A parte quello e alcuni frammentari inizi di conversazione, c'è silenzio. Un silenzio assai distante da quello rilassante mentre entravamo in città, tra l' altro."

hi "Come sta andando il murale?"

show rin basic_deadpan_ni at tworight
with charachange

rin "Avremo della sfortuna. Mai parlare di progetti in corso."

show lilly cane_weaksmile_ni at twoleft
with charachange

li "Sono sicura che sarà splendido."

show rin basic_deadpannormal_ni at tworight
with charachange

rin "Sfortuna."

"Tac passo tac passo. Non ha voglia di parlarne. La cortesia di Lilly sembra fuori luogo, per la prima volta. Passo passo passo."

"La collina su cui si trova Yamaku è sorprendentemente ripida, in salita. Rallentiamo il passo, ma sento comunque accelerare il mio battito e il mio respiro diventa più pesante."

"Siamo quasi arrivati, posso già vedere il cancello."

"Più di quello, però, noto che la mano di Lilly si stringe leggermente sulla mia spalla. Interpretandolo come un segno che vuole chiedere qualcosa, apro bocca."

hi "Qualcosa non va, Lilly?"

"Resisto alla tentazione di dire “A parte la nostra compagna di viaggi?” Ma a malapena."

"Per un momento sembra chiedersi se addirittura dovrebbe parlarne, ma decide di farlo comunque."

show lilly cane_concerned_ni at twoleft
with charachange

li "Va tutto… bene?"

hi "Tutto bene? Cosa intendi?"

"Il fatto che non posso interpretare la sua domanda incredibilmente vaga la ferma, per un secondo."

li "E' solo che… sembri stranamente stanco, immagino."

"Adesso che lo fa notare, mi accorgo che il mio fiato è sorprendentemente corto. La camminata in salita mi ha davvero stancato."


label it_choiceA30:
menu:
    with menueffect
    
    "Anche se Rin è persa nel suo mondo, Lilly se ne è accorta fin troppo in fretta…"
    
    "Scusa, non sono davvero in ottime condizioni.":
        return m1

    "Sto bene.":
        return m2
        
label it_A30a:

hi "Sto bene, sto bene."

show lilly cane_sad_ni at twoleft
with charachange

li "Tu… non suoni come qualcuno che sta bene."

show rin basic_deadpansurprised_ni at tworight
with charachange

rin "A guardarlo, non sembra nemmeno che stia bene."

"La domanda di Lilly ha stimolato la curiosità di Rin. Splendido."

show lilly cane_concerned_ni at twoleft
with charachange

li "Non dovresti sforzarti se c'è qualcosa—{w=.5}{nw}"

hi "Ho detto che sto bene, okay?"

play music music_rain fadein 0.3

show lilly cane_displeased_ni at twoleft
show rin basic_deadpannormal_ni at tworight

with charachange

"Quasi lo urlo, inavvertitamente, ma non è come se importasse."

"Per un momento sembra che Lilly stia per protestare al mio tono, ma non lo fa."

"Rin è disinteressata come al solito, anche se c'è qualcosa nella sua espressione che tradisce la sua confusione."

"Per un periodo di tempo lungo in maniera imbarazzante, non scambiamo una parola. Voglio ritirare quello che ho fatto ma ormai non è più possibile."

hi "Scusate. Era… troppo."

hide lilly
hide rin
with charaexit

"Cambio strada, lasciando indietro le ragazze. Pentendomi istantaneamente della mossa, ma non posso evitarlo."

"Sto fuggendo, fuggendo dal confrontare me stesso. Perfino capendo che razza di codardo sono, non mi fermo."

stop music fadeout 3.0

scene black
with Dissolve(3.0)

label it_A30b:

hi "Va tutto bene, devo solo prendere fiato. Le mie condizioni non sono delle migliori ultimamente."

show lilly cane_oops_ni at twoleft
with charachange

li "Oh."

li "E' qualcosa che… è correlato al tuo trasferimento qui? Voglio dire…"

show lilly cane_concerned_ni at twoleft
with charachange

"Si interrompe piuttosto bruscamente, forse capendo che stava ficcanasando un po' troppo. Il suo istinto è acuto però, e mentre l' argomento non mi piace non è come se dovessi mentire."

"Se è Lilly, non penso che mi dispiaccia."

play music music_lilly fadein 0.3

hi "Sono solo un po' debole per il momento."

show lilly cane_oops_ni at twoleft
with charachange

li "Hanako ha detto che sembri abbastanza… in salute, così naturalmente ho pensato…"

show lilly cane_sad_ni at twoleft
with charachange

"Di nuovo, Lilly non finisce la sua frase, lasciandola svanire con una certa preoccupazione."

"Mentre aggrotta la fronte, la sua espressione di disagio mi spinge a dire almeno qualcosa per tranquillizzarla."

"E' sorprendente che sia così imbarazzata, considerando la sua attitudine diretta nei confronti della sua cecità. Deve sapere che non tutti condividono la sua tranquillità su certe cose."

hi "No, è okay."

hi "Ho un cuore… immagino che la maniera migliore di dirlo sarebbe… piuttosto malconcio. Aritmia."

hi "Mi ha causato un brutto attacco di cuore un po' di tempo fa, e ho passato la maggior parte della primavera in un ospedale. Sono finito a Yamaku per ordine del medico."

"Annuisce silenziosamente in comprensione."

"La mia risposta, però, sembra solo farle aggrottare ancora di più la fronte. Non sembra sapere bene come reagire, dato che non ci conosciamo poi così bene."

"Non posso davvero fargliene una colpa, dato che ho l' esatta stessa reazione."

label it_A30c:

"Con mia sorpresa, dopo un attimo il suo viso mostra che ha appena capito qualcosa."

show lilly cane_oops_ni at twoleft
with charachange

li "Aspetta… così quella volta quando tu ed Emi vi siete scontrati nel corridoio…?"

"Faccio una smorfia. La sua abilità di sommare due più due così in fretta è inaspettata."

hi "Già. Suppongo di essere un perfetto esempio del perchè quelle regole riguardanti il correre nei corridoi esistono."

show lilly cane_sad_ni at twoleft
with charachange

"Quello è uscito molto più asciutto di quanto volessi. Lilly si ritira visibilmente dal continuare il discorso."

label it_A30d: 

"Mentre la voglio tranquillizzare, non voglio davvero neanche restare sull' argomento."

hi "Non preoccuparti."

show lilly cane_weaksmile_ni at twoleft
with charachange

"Cerco di offrire un sorriso rassicurante ma poi capisco la futilità dell' idea. Senza poter sapere questo, Lilly mi sorride in modo rassicurante ma non dice più altro."

scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip

"Arrivando ai dormitori, Rin si ferma di fronte al suo murale come se il fulmine l' avesse colpita. E' stata così silenziosa per quasi tutta la camminata di ritorno che mi ero praticamente dimenticato della sua presenza."

stop music fadeout 1.0

show rin relaxed_disgust_ni at tworight
with charachange

rin "E' venerdì, vero?"

show lilly cane_smile_ni at twoleft
with charachange

li "Sì… venerdì, otto giugno."

play music music_rin fadein 0.3

show rin basic_upset_ni at tworight
with charachange

rin "Questo è male."

show lilly cane_surprised_ni at twoleft
with charachange

li "Male? Perchè?"

show rin negative_annoyed_ni at tworight
with charachange

rin "Credo di stare per mettermi in posizione fetale e vomitare. Probabilmente in ordine inverso."

show lilly cane_concerned_ni at twoleft
with charachange

li "Qualcosa non va?"

show rin negative_confused_ni at tworight
with charachange

rin "No. Non c'è nulla che non va. E' venerdì e ancora non c'è nulla che non va. Questo murale, bisogna che sia terminato prima di domenica. Quindi va tutto bene."

show rin negative_worried_ni at tworight
with charachange

rin "Avete per caso della droga? O una macchina del tempo?"

show rin negative_confused_ni at tworight
with charachange

rin "Questo non è bene. Non è bene."

"Così è rimasta indietro sulla sua tabella di marcia. Ricordando l' esasperazione di Shizune verso l' attitudine spensierata di Rin diversi giorni fa, non so cosa pensare."

"Si è lasciata aperta per un “te l' avevo detto” a meno che non riesca a fare quello che deve fare entro domenica mattina."

"Rin continua a fissare il suo murale sembrando mortificata quanto lo può sembrare."

show rin negative_annoyed_ni at tworight
with charachange

rin "Lasciatemi sola. Dovrò lavorare per un pò."

"Io lancio uno sguardo a Lilly, aspettandomi che lei condivida la mia aria incredula mentre alzo gli occhi al cielo, ma poi capisco che lei non è il tipo che fa quel genere di cose."

show rin negative_angry_ni at tworight
with charachange

rin "Lasciatemi sola."

stop music fadeout 2.0

hide rin
with charaexit

show lilly cane_concerned_ni
show bg school_dormext_half_ni at bgright
with charamove

"Ovviamente lo facciamo, non volendo esasperarla più di quanto già sia."

"C'è un pessimo presagio che si torce nel mio stomaco. Rin certo ha un dono per far sì che gli altri si preoccupino per lei."

"Sembra una persona che non dovrebbe mai essere lasciata sola."

hi "Forse dovremmo chiamare qualcuno? Suonava come se stesse andando in shock o qualcosa di simile."

show lilly cane_oops_ni
with charachange

li "Sono certa che starà benissimo. Lei è solo una… eeeh… come dire…"

"Lilly inclina un po' la testa, cercando di trovare una maniera educata di dare della matta a Rin senza darle della matta."

hi "Unica?"

show lilly cane_weaksmile_ni
with charachange

li "Sì, una persona davvero unica."

hi "Immagino che si potrebbe dire così."

show lilly cane_giggle_ni
with charachange

"Ride melodiosamente all' idea, annuendo in assenso."

show lilly cane_weaksmile_ni
with charachange

li "Mi dispiace di non averti aiutato mentre parlavi con lei. Io… non la capisco davvero, così tengo le distanze da lei."

"Così avevo indovinato. Lilly offre un lieve sorriso di scusa come se le dispiacesse che le sue carenze le abbiano impedito di diventare più vicina a Rin."

"Non le faccio una colpa. Affatto."

play music music_lilly fadein 0.3

"Lilly si lascia sfuggire un lungo respiro, probabilmente uno sbadiglio camuffato. Immagino che questo affare l' abbia stancata tanto quanto ha stancato me."

show lilly cane_cheerful_ni
with charachange

li "Farò meglio ad andarmene e a consegnare questi ad Hanako. Grazie per la compagnia, Hisao."

"Mi sorride molto dolcemente. Sembra diverso dal normale, a dispetto del fatto che lei sembra sorridere così spesso."

"Non posso identificare qual è la differenza. E' solo diverso."

"Rilassato, direi, ma quello è probabilmente solo sollievo per essersi liberati di Rin. Forse."

hi "Già… buonanotte. Salutami Hanako."

show lilly cane_smile_ni
with charachange

li "Lo farò. Buonanotte."

hide lilly

scene black
with Dissolve(3.0)

return

