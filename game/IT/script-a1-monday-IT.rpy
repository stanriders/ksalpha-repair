#### MONDAY

#**************************************
label it_NOP1:
window hide None

scene black
with None

scene bg op_snowywoods
show snow
with Dissolve(2.0)

window show

play music music_serene fadein 0.2

"Una lieve brezza fa risuonare i nudi rami degli alberi come un carillon di legno."

"Questo è un posto popolare per le coppiette durante l' estate. Gli alberi decidui forniscono una splendida cupola di verde, lontano dalla vista degli insegnanti e degli altri studenti."

"Ma adesso, a inverno inoltrato, mi sento come se stessi sotto una pila di legname."

"Alito nelle mie mani raccolte a coppa e le strofino vigorosamente per evitare che si intirizziscano in questo freddo."

hi "Quanto dovrò aspettare qua fuori, poi? Sono sicuro che il biglietto diceva 4 del pomeriggio."

"Ah già… il biglietto… fatto scivolare di soppiatto tra le pagine del mio testo di matematica senza che me ne accorgessi."

"Finchè si parla di cliché, sono più un fan della lettera-nell'-armadietto, ma almeno questo modo dimostra una certa iniziativa."

"Mentre pondero il significato del biglietto, la nevicata gradualmente si infittisce."

"I fiocchi di neve che cadono silenziosamente dal cielo candido sono l' unico segno del tempo che passa in questo mondo stagnante."

"La loro lenta discesa sulla foresta ghiacciata fa sembrare che il tempo sia rallentato all' estremo."

play sound sfx_rustling

"Il fruscio di neve fresca sotto i piedi mi sorprende, interrompendo l' atmosfera tranquilla. Qualcuno si sta avvicinando a me da dietro."

mystery "Hi… Hisao? Sei venuto?"

"Una domanda esitante, a malapena udibile."

"Però, riconosco istantaneamente la proprietaria di quella voce argentina."

"Sento il mio cuore mancare un battito."

"E' una voce che ho ascoltato centinaia di volte, ma mai come più che un ficcanaso in una conversazione."

"Mi giro verso questa voce, la voce dei miei sogni, e il mio cuore inizia a correre…"

window hide

scene white
with dissolve
scene ev other_iwanako_start
show snow
with Dissolve(5.0)

window show

hi "Iwanako? Ho ricevuto un biglietto che mi chiedeva di aspettare qui… era il tuo?"

"Dannazione. Ho passato tutto il pomeriggio cercando di trovare un buon esordio, e quello è il risultato."

"Patetico."

"Iwanako" "Ahmm… sì. Ho chiesto a un' amica di darti quel biglietto… sono così felice che tu l' abbia ricevuto."

"Un timido, gioioso sorriso che mi rende tanto teso da non poter muovere un muscolo anche se ci provassi."

stop music fadeout 10.0

window hide

scene white
with dissolve
scene bg op_snowywoods
show snow
with Dissolve(2.0)

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Il mio cuore sta martellando adesso, come se stesse cercando di fuggire dal mio torace per reclamare questa ragazza come sua."

window hide

scene white
with dissolve
scene ev other_iwanako
show snow
with Dissolve(3.0)

window show

hi "Così… ah… eccoci qui. Fuori al freddo…"

"Di nuovo, il vento scuote i rami. Il rumore una volta cacofonico è ora dolce musica per le mie orecchie."

"Iwanako si ritrae appena appena dal soffio di vento."

"Una volta passato, si raddrizza, come sorretta da una nuova sicurezza."

"I suoi occhi si fissano sui miei e pigramente gira i suoi lunghi, scuri capelli intorno a un dito."

"Per tutto il tempo, l' incessante battito del mio cuore diventa più rumoroso."

window hide

scene white
with dissolve
scene bg op_snowywoods
show snow
with Dissolve(2.0)

window show

"la mia gola è secca; dubito che potrei spiccicare parola anche se provassi."

"Iwanako" "Vedi…"

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show

"Iwanako" "…volevo sapere…"

stop music fadeout 0.5

window hide

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Iwanako" "…se ti andrebbe di uscire con me…"

"Resto lì in piedi, immobile, tranne per il mio cuore martellante."

"Voglio dire qualcosa in risposta, ma le mie corde vocali sembrano essere state stirate oltre il punto di rottura."

play music music_tragic fadein 0.5

"Iwanako" "… Hisao?"

"Cerco di massaggiare la mia gola, ma questo manda soltanto fitte di dolore accecante lungo le mie braccia."

"Iwanako" "Hisao?!"

window hide

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"Il mio corpo si paralizza, eccetto i miei occhi, che si spalancano terrorizzati."

window hide

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha 
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha 
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)

window show

stop music fadeout 1.0

"Iwanako" "HISAO!"

"Il battito nel mio petto improvvisamente cessa, e mi cedono le gambe."

window hide

show passoutOP1
with None

nvl show Dissolve(0.2)

n "Il mondo intorno a me; la cupola di rami spogli, il cielo grigio di inverno, Iwanako che corre spaventata verso di me; tutto svanisce in nero."

n "Le ultime cose che ricordo prima di perdere conoscenza sono i suoni di Iwanako che urla aiuto e l'incessante fracasso dei rami…"

nvl hide Dissolve(3.0)

nvl clear

with Pause (1.0)

scene black
with None

#**************************************
label it_NOP2:

window hide None

scene black
with None

centered "Sono passati quattro mesi dal mio attacco di cuore." with dissolve

scene bg hosp_room
show sakura
show hospitalmask
with Dissolve (1.5)

play music music_rain fadein 4.0

nvl show dissolve

n "In tutto quel tempo, posso probabilmente contare le volte in cui ho lasciato questa stanza di ospedale senza supervisione sulle dita di una mano."

n "Quattro mesi sono tanti quando si viene lasciati soli con i propri pensieri. Così, ho avuto abbondanza di tempo per venire a patti con la mia situazione."

n "Aritmia."

n "Una parola strana. Estranea, aliena. Una parola che non vuoi nella stessa stanza con te."

n "Una condizione rara. Fa sì che il cuore si comporti erraticamente e occasionalmente batta troppo in fretta. Può essere fatale."

n "Apparentemente, ne soffro da molto tempo. Dicono che è stato un miracolo che sia riuscito ad andare avanti così a lungo senza che sia accaduto nulla prima d'ora."

n "E' davvero un miracolo? Immagino che fosse inteso per farmi sentire meglio; per farmi apprezzare di più la mia vita."

n "Non ha veramente fatto nulla per rallegrarmi."

nvl clear

n "I miei genitori, credo, sono stati colpiti da questa notizia più duramente di me. Gli è praticamente venuto un colpo ciascuno."

n "Allora io avevo già avuto un giorno intero per digerire il tutto. Per loro, era tutto nuovo. Erano preparati anche a vendere la nostra casa per pagare una cura."

n "Ovviamente non esiste una cura."

nvl clear

n "A causa della tarda scoperta di questa… condizione, sono dovuto rimanere in ospedale per un pezzo, per recuperare dai trattamenti."

n "Quando sono stato ricoverato in ospedale, sembrava che la mia mancanza fosse sentita…"

n "Per circa una settimana, la mia stanza nel reparto è stata piena di fiori, palloncini e cartoline."

n "Ma, i visitatori presto diminuirono e tutti i doni di buon augurio iniziarono a ridursi a nulla piuttosto in fretta."

n "Capii che l' unico motivo per cui avevo ricevuto tanti biglietti e fiori era perchè dimostrarmi la loro solidarietà era stato trasformato in un progetto per la classe."

n "Forse qualcuno era veramente preoccupato, ma ne dubito. Anche all' inizio, a malapena ricevevo dei visitatori. Entro la fine del primo mese, solo i miei genitori mi venivano a trovare regolarmente."

n "Iwanako fu l' ultima a smettere di visitarmi."

n "Dopo sei settimane, non si è più fatta viva. Non abbiamo mai avuto molto di cui parlare anche quando mi visitava, comunque."

n "Non abbiamo mai più toccato l' argomento che era tra di noi durante quel giorno nevoso."

nvl clear

n "L' ospedale?"

n "Non è davvero un posto dove mi piacerebbe vivere."

n "I medici e le infermiere sembrano così impersonali e anonimi."

n "Immagino che sia perchè vanno di fretta e hanno un milione di altri pazienti che li stanno aspettando, ma mi fa sentire a disagio."

n "Per circa il primo mese, ogni volta che lo vedevo chiedevo al primario di cardiologia di darmi una vaga idea di quando avrei potuto andarmene."

n "Non mi rispondeva mai in maniera diretta, ma mi diceva di aspettare e vedere se la terapia e le operazioni chirurgiche funzionavano."

n "Così, osservavo oziosamente la cicatrice che quelle operazioni avevano lasciato sul mio petto cambiare lentamente aspetto col tempo, considerandolo una sorta di presagio."

n "Chiedo ancora al primario di cardiologia quando potrò andarmene, ma le mie aspettative adesso sono abbastanza basse da non essere più deluso quando non ottengo una risposta. Il modo in cui gira intorno all' argomento mostra che almeno c'è qualche speranza."
    
nvl clear

n "A un certo punto ho smesso di guardare la TV. Non so perchè, ho smesso e basta."

n "Forse era il tipo sbagliato di evasione dalla realtà per la mia situazione."

n "Ho invece iniziato a leggere. C'è una piccola “biblioteca” nell' ospedale, anche se era più come un magazzino per libri. Ho cominciato a leggerla metodicamente, una piccola pila di libri per volta. Dopo averli divorati, tornavo a prenderne altri."

n "Ho scoperto che leggere mi piace e penso di essere persino diventato un po' bibliofilo. Ho cominciato a sentirmi nudo senza un libro in mano."

n "Ma adoravo le storie."

nvl clear

n "Questa era la mia vita."

n "I giorni diventarono sempre più difficili da  distinguere fra loro, diversi solo per il libro che stavo leggendo e il tempo fuori. Sembrava che il tempo si confondesse in una sorta di massa collosa in cui ero intrappolato, invece di muovermi in esso."

n "Poteva passare una settimana senza che io me ne accorgessi davvero."

n "Qualche volta, mi fermavo realizzando di non sapere che giorno della settimana fosse."

n "Ma altre volte, tutte le cose che mi circondavano si schiantavano dolorosamente sulla mia coscienza, attraverso la barriera di nonchalance che mi ero costruito." 

n "Le pagine del mio libro iniziavano a sembrare taglienti e brucianti e la pesantezza nel mio petto diventava talmente difficile da sopportare che dovevo mettere il libro da parte e solo sdraiarmi per un po', guardando il soffitto come se stessi per piangere." 

n "Ma quello accadeva solo raramente."

n "E non riuscivo nemmeno a piangere."

nvl hide dissolve

nvl clear

window show

"Oggi, il medico entra e mi sorride. Sembra eccitato, ma non troppo. E' come se stesse cercando di fare uno sforzo per essere felice per mio conto."

"I miei genitori sono qui. Sono passati alcuni giorni dall' ultima volta che li ho visti. Si sono perfino più o meno agghindati entrambi. Dovrebbe essere una specie di occasione particolare? Non è una festa."

"C'è questo rituale che il primario di cardiologia segue. Fa con calma, aggiustando le sue carte, poi mettendole da parte come per  puntualizzare l' inutilità di quel che ha appena fatto."

"Poi si siede disinvoltamente sul bordo del letto accanto al mio. Mi fissa negli occhi per un momento."

"Medico" "Ciao, Hisao. Come stai oggi?"

"Non gli rispondo ma gli sorrido, un poco."

"Medico" "Credo che tu possa andare a casa; il tuo cuore è più forte adesso, e con alcune precauzioni, dovresti essere a posto."

"Medico" "Abbiamo sistemato tutta la tua medicazione. Darò la ricetta a tuo padre." 

"Il dottore passa un foglio di carta a papà, la cui espressione si irrigidisce mentre lo legge rapidamente."

"Papà" "Così tanti…"

"Lo prendo dalla sua mano e dò un' occhiata a mia volta, sentendomi stordito. Come dovrei reagire a una cosa del genere?"

scene white
with Dissolve(2.0)

#$ renpy.show("wallodrugsbg", what=drugsDisp(), at_list=[Zoom((800, 600), (100, 75, 600, 450), (0, 0, 800, 600), 22.0, time_warp=_ease_in_time_warp)])
$ renpy.show("wallodrugsbg", what=drugsDisp(1600,800), at_list=[Pan((0.0,0.0),(1.0,0.0),25.0, time_warp=_ease_in_time_warp)])

"L' assurdamente lunga lista di medicinali che mi fissa dal foglio sembra insormontabile. Si fondono tutti insieme in un mare di lettere."

"Questa è follia."

"Effetti secondari, effetti indesiderati, controindicazioni e dosaggi sono listati riga dopo riga con gelida precisione."

"Cerco di leggerli, ma è talmente futile."

"Non posso capirci niente. Provarci mi fa solo sentire peggio."

"Tutto questo… per il resto della mia vita, ogni giorno?"

scene bg hosp_room
show sakura
show hospitalmask
with fade

"Medico" "Temo che sia il meglio che possiamo fare per ora."

"Medico" "Comunque, nuovi farmaci vengono sviluppati di continuo, quindi non sarei sorpreso se quella lista si riducesse col passare degli anni."

"Anni… Che razza di incoraggiamento è quello? Mi sarei sentito meglio se non avesse detto nulla…"

"Medico" "Inoltre, ho parlato coi tuoi genitori, e crediamo che sarebbe meglio se tu non ritornassi alla tua vecchia scuola."

hi "Cosa!?"

"Papà" "Per favore, calmati, Hisao. Ascolta quello che ha da dire il dottore…"

"Calmarmi? Il modo in cui lo dice mi fa capire che sapeva bene che non mi sarebbe andato a genio. Dovrò essere educato a casa?"

"Quel che è visibile della mia preoccupazione viene ignorato."

"Medico" "Capiamo tutti che la tua educazione è fondamentale; ma comunque non penso sia saggio per te essere privo di supervisione."

"Medico" "Almeno finchè non saremo certi che la tua terapia sia appropriata."

"Medico" "Così, ho parlato con i tuoi genitori riguardo a un trasferimento."

"Medico" "E' una scuola chiamata Accademia Yamaku che si specializza nel trattare con studenti disabili."

"Disabili? Cosa? Sono…"

"Medico" "Ha uno staff di infermieri presenti 24 ore su 24, ed è solo a pochi minuti da un ospedale policlinico altamente raccomandato. La maggioranza degli studenti abitano sul posto."

"Medico" "Considerala come una sorta di collegio privato. E' progettata per dare agli studenti un certo grado di indipendenza, mantenendo assistenza vicino."

"Indipendenza? E' una scuola per ragazzi disabili. Non cercare di camuffare questo fatto."

"Se fosse davvero così “libera,” non ci sarebbe uno staff di infermieri presenti 24 ore su 24, e non menzioneresti la vicinanza di un ospedale come un punto a favore."

"Papà" "Certo, è solo se vuoi andare. Ma… tua madre e io non siamo veramente in grado di insegnarti a casa."

"Papà" "Siamo andati là a dare un' occhiata un paio di settimane fa; penso che ti piacerebbe."

"Sembra che davvero non abbia scelta."

"Medico" "Le persone sofferenti della tua stessa condizione tendono generalmente a vivere a lungo, comparate a chi ha altri problemi cardiaci. Ti servirà un lavoro un giorno e questa è una buona opportunità per continuare la tua educazione."

"Questa non è un' opportunità, non chiamarla un' opportunità. Non chiamarla una stramaledetta opportunità."

"Medico" "Bè, dovresti essere eccitato alla possibilità di tornare a scuola. Ricordo che volevi ritornare a scuola, e anche se non è la stessa…"

"Una scuola speciale. Questo è…"

"Un insulto. Questo è quel che voglio dire. E' un passo verso il fondo."

"Papà" "Non è come pensi. Tutti gli studenti lì sono piuttosto attivi, a modo loro."

"Papà" "E' organizzata per studenti che possono ancora muoversi e imparare, ma hanno bisogno di un po' di aiuto… in un modo o nell' altro."

"Medico" "Tuo padre ha ragione. E molti dei diplomati della scuola sono andati oltre con risultati incredibili. Una persona non deve necessariamente essere limitata dalla sua disabilità."

"Medico" "Uno dei miei colleghi in un altro ospedale si è diplomato lì."

"Non me ne importa. Una persona non deve necessariamente essere limitata dalla sua disabilità? Quello è ciò che è una disabilità."

"Odio davvero il fatto che qualcosa di così importante sia stato deciso per me. Ma cosa posso farci? Una vita “normale” adesso è fuori questione."

"E' buffo, ho sempre pensato che la mia vita fosse un tantino noiosa, ma adesso mi manca."

"Voglio protestare. Voglio dare la colpa di questa mancanza di reazione allo shock, o alla stanchezza. Potrei facilmente urlare qualcosa adesso; qualcosa su come posso tornare comunque a scuola. Ma, no."

"Non dico nulla. Il fatto è che ora so che è futile."

"Guardo intorno alla stanza, sentendomi molto stanco di tutto questo. L' ospedale, i medici, la mia malattia, tutto. Non vedo nulla che mi farebbe sentire diversamente."

"Non c'è davvero una scelta. Lo so, ma il pensiero di andare a una scuola per disabili… non ho nemmeno idea, come saranno? Per quanto tenti di guardare alle cose positivamente, è molto difficile."

"Ma fatemi provare."

"Una tabula rasa non è un male."

"E' l' unica cosa a cui riesco a pensare per farmi andare avanti. Almeno ho ancora qualcosa; anche se è una “scuola speciale,” è qualcosa. E' un nuovo inizio, e la mia vita non è finita. Sarebbe un errore rassegnarmi a pensare solo quello."

"Come minimo, proverò a vedere come sembra la mia nuova vita."

window hide
  
stop music fadeout 1.0



#**************************************
label it_A1:

window hide None

scene bg school_gate
with slowfade

play music music_happiness fadein 0.3

window show

"Il cancello sembrava decisamente troppo pomposo per quel che era."

"In effetti, i cancelli in generale sembrano esserlo, ma questo in modo particolare."

"Mattoni rossi, ferro battuto nero e stucco grigio, assemblati in un insieme che non sembrava affatto accogliente."

"Mi sono chiesto se somigliava a quello a cui il cancello di una scuola dovrebbe somigliare, ma non sono riuscito a decidere. Probabilmente no."

"Ovviamente non volevo rimanere bloccato a pensare al cancello per troppo tempo, così sono entrato attraverso di esso con un passo spedito che mi ha fatto sentire sorprendentemente bene."

"Andare avanti è piacevole."

scene bg school_courtyard
with locationchange

"Così cammino verso l' edificio principale dell' Accademia Yamaku con questo passo spedito. Sono solo, dato che i miei genitori stanno portando la mia roba ai dormitori, e si suppone che qualcuno mi stia aspettando."

"I terreni sono incredibilmente lussureggianti, pieni del colore verde."

"Non sembrano il tipo di terreni appartenenti a una scuola, ma più come un parco, con un sentiero pulito in mezzo agli alberi e l' odore d' erba tagliata di fresco e tutte le altre cose da parco."

"Parole come “pulito” e “igienico” mi saltano in mente. Mi fa rabbrividire."

"Me ne libero. Mantieni una mente aperta ora. E' la tua nuova vita. Devi prenderla come viene."

"E' quello che continuo a dirmi."

"Alcuni grossi edifici si profilano dietro le chiome ricche di fogliame, troppo grandi e troppo numerosi per una semplice scuola."

"Tutto sembra fuori luogo; è diverso da quello che pensavo di sapere riguardo alle scuole."

"E' familiare e allo stesso tempo incredibile. Anche se mi è stato detto che questa è la mia nuova scuola, nel fondo del mio cervello non la sento come tale."

"Mi chiedo se la sensazione è reale o causata dalle mie aspettative di una scuola per disabili."

"E parlando di quello, non vedo nessun altro oltre me. E' un po' inquietante."

"Mi fa desiderare che ci fosse qualcuno qui, così da potermi ancorare a qualcosa di tangibile invece di avere questa sensazione di essere entrato in un' altra dimensione."

"Gli alberi mormorano col vento e i toni di verde in movimento tutto intorno a me attraggono la mia attenzione."

"Mi fanno ripensare agli ospedali, a come si dice che le sale operatorie siano dipinte di verde perchè il verde è un colore rilassante."

"Così perchè mi sento così ansioso, a dispetto di tutta questa vegetazione?"

"…"

"Solo dopo che mi trovo in piedi davanti all' altezzoso edificio principale, mi sorprendo da solo capendo perchè il cancello mi turbava:"

"Era l' ultima possibilità che avevo di tornare sui miei passi, anche se non avevo una vita a cui ritornare."

"Ma comunque, dopo essere entrato, non c'era assolutamente nessun modo per me di tornare indietro."

"Con questa realizzazione fissa nella mia testa e sentendomi nervoso, apro la porta principale."

scene bg school_lobby
with locationchange

"Un uomo alto dal cattivo portamento mi nota quando entro. E' solo logico, dato che siamo le uniche persone nell' atrio."

show muto normal
with charaenter

mu_ "Tu devi essere… Ni… Na… Niki?"

hi "Nakai."

show muto smile
with charachange

mu_ "Sei proprio tu. Eccellente. Sono il tuo insegnante di riferimento e di scienze. Mi chiamo Mutou."

mu "Benvenuto."

"Scambiamo una stretta di mano che non è nè decisa nè fiacca, e lui guarda il suo orologio."

show muto irritated
with charachange

mu "Il capo infermiere ha chiesto di farti una breve visita di controllo, ma non c'è tempo per quello ora."

hi "Oh. Dovrei andare più tardi?"

show muto normal
with charachange

mu "Sì, nel pomeriggio probabilmente andrà bene. Dovremmo muoverci e presentarti al resto della classe. Stanno già aspettando."

"Aspettandomi? Non mi piace davvero essere al centro dell' attenzione, ma immagino che sia inevitabile in una situazione come questa."

"In qualche modo, non sapere cosa mi aspetta mi fa sentire veramente nervoso."

"Pensando a questo, quasi non mi accorgo di cosa sta dicendo l' insegnante."

label it_choiceA1:
menu:
    with menueffect

#choice:
    mu "Vuoi presentarti alla classe?"

    "Perchè?":
        return m1
        
    "Sì, certo.":
        return m2

label it_A1a:

hi "Perchè? Devo farlo?"

mu "Certo che no. E' per quello che ho chiesto."

hi "Giusto."

mu "Allora andiamo."



label it_A1b:

hi "Sì, certo. Voglio dire, non è normale?"

mu "Certamente. Ma non tutti gradiscono essere al centro dell' attenzione."

"Probabilmente sono una di quelle persone, ma suppongo di dover essere io a dare la prima impressione di me stesso."

hi "Giusto, ma non c'è problema."

mu "Allora andiamo."



label it_A1c:

scene bg school_staircase2
with locationchange

"Il mio cuore sta battendo nel mio petto e continua a farmi ripensare alla mia condizione mentre seguo l' insegnante su per le scale."

scene bg school_hallway3
show muto normal
with locationchange

"La terza porta lungo il corridoio del terzo piano è marchiata come aula per la classe 3-3."

"Mutou apre la porta ed entra."

hide muto
with charaexit

mu "Buongiorno a tutti, scusate di nuovo il ritardo."

stop music fadeout 2.0

"Esito per un istante alla porta, congelandomi sul posto."



#**************************************
   
label it_A2:

scene bg school_hallway3
with None

"Ah, sveglia! Questo è un grosso passo, lo so… Ma è inutile preoccuparmi così tanto, o almeno non così presto."

scene ev hisao_class_start
with fade

play music music_normal fadein 0.3

"Seguo l' insegnante in aula e guardo intorno, parzialmente così da non dover incontrare gli sguardi curiosi dei miei nuovi compagni di classe."

scene ev hisao_class_move
with None

"E' piuttosto spaziosa; il soffitto è inusualmente alto e rimane un sacco di spazio tra i banchi e intorno ad essi."

"Un intero muro occupato da lavagne e le alte finestre in stile antico ad altezza della testa la fanno sembrare solo più grande."

"I banchi degli studenti sono solo banchi di legno standard con un ripiano al di sotto per conservarci i testi e sedie di legno con intelaiatura in metallo. Semplici ed efficienti."

"Smetto di camminare di fronte all' aula e guardo gli altri studenti. Sembrano tutti normali, come studenti in qualunque altra scuola. Ma allora, perchè sarebbero qui?"

"Probabilmente sono come me e hanno qualcosa che non va in loro, solo che non è immediatamente ovvio. Poi, mi accorgo che a una delle ragazze sembra mancare il pollice dalla mano destra. Il contrasto è un po' stridente."

"A dispetto della normale tendenza ad ascoltare quando qualcuno sta parlando di te, smetto di prestare attenzione al discorso dell' insegnante a metà mentre mi presenta alla classe."

"Noto dei capelli scuri in movimento e vedo che qualcuno mi sta guardando. Una ragazza dai capelli veramente lunghi e lisci, piuttosto attraenti."

"Quando vede che sto ricambiando il suo sguardo, si copre il viso con le mani come se quello la rendesse invisibile."

"C'è un bastone appoggiato contro la sedia di un ragazzo. E' bizzarro vedere qualcuno così giovane con un bastone."

"Un' altra ragazza sembra stare facendo dei movimenti curiosi con le mani. Lingua dei segni? Mi guarda da sopra i suoi occhiali, poi torna a quel che sta facendo."
#Il termine corretto è lingua, NON linguaggio dei segni. Consigliabile fare un search-and-replace per sicurezza prima o poi.

"E' piuttosto carina. E lo è anche la ragazza dall' aria allegra con i capelli rosa seduta vicino a lei. E' davvero difficile non notarla; non so come ho fatto a non accorgermi di lei appena sono entrato…"

mu "…per favore date il benvenuto al nostro nuovo compagno di classe."

"Applaude e così fanno tutti, eccetto per una ragazza in prima fila che ha una sola mano. Rabbrividisco un poco, ma lo nascondo inchinandomi in ringraziamento per questi applausi che non mi merito."


label it_A2a:

"Dopo l' applauso, c'è un breve silenzio e nessuno sembra voler essere responsabile per romperlo."

"L' insegnante capisce abbastanza presto che dovrebbe probabilmente dire qualcosa, così apre con un rumore incomprensibile, tace perdendo lo slancio, ed inizia a presentarmi."

"Nessuno sembra essere troppo interessato."

"Forse avrei dovuto dire di sì riguardo al presentarmi da solo."

"Probabilmente capendo che non sa niente di me, finisce solo per dire il mio nome sbagliandosi di nuovo, e mi chiede di scriverlo sulla lavagna."

"Lo faccio, e mi giro a fissare di nuovo la classe, sentendomi imbarazzato."


label it_A2b:

"Un silenzio collettivo mi dice che adesso dovrei aprir bocca."

hi "Così… sono Hisao Nakai."

"E poi?"

hi "I miei hobby sono la lettura e il calcio. Spero di andare d' accordo con tutti anche se sono un nuovo studente."

"E poi?"

"Sono talmente noioso. Questa è esattamente come qualunque presentazione mai fatta. Dovrei dire qualcosa di più. Qualcosa di più eccitante."

"Finisco per non dire nulla, e l' insegnante continua da lì."

"Tutti sembrano essere soddisfatti anche col poco che ho detto, però. Alcune ragazze stanno bisbigliando tra di loro, lanciandomi sguardi. Poteva andare peggio." 

"…"


label it_A2c:

scene ev hisao_class_end
with None

"Ascolto l' insegnante che borbotta qualcosa riguardo all' andare d' accordo mentre lascio che il mio sguardo percorra l' aula."

"Tutti sembrano starlo ascoltando attentamente e quando finisce applaudono di nuovo, che ho sempre pensato sia una cosa un po' strana da farsi."

"La ragazza della prima fila stavolta applaude, con la sua unica mano contro il suo altro polso che finisce in un moncherino bendato." 

"Mi fa sentire un po' a disagio."

mu "Svolgeremo del lavoro di gruppo oggi, così ti darà una possibilità di parlare con tutti. Ti può andare?"

hi "Sì, a me va bene."

stop music fadeout 5.0

mu "Ottimo, puoi lavorare con Hakamichi. E' la capoclasse."

mu "Può spiegarti tutto quel che potresti voler sapere. E chi altri potrebbe farlo meglio, giusto?"

"Come potrei saperlo?"

"L' insegnante distribuisce i compiti di oggi e annuncia che lavoreremo in gruppi da tre."

"Realizzo di non sapere chi sia Hakamichi. Tardo. L' insegnante sembra notare la mia espressione indifesa."

mu "Oh, già. Hakamichi è proprio lì, Shizune Hakamichi."

scene bg school_scienceroom at bgright
show misha perky_smile
with fade

"Mentre pronuncia il suo nome, la graziosa ragazza dall' aria briosa coi capelli rosa acceso e occhi color oro agita la sua mano in saluto. Mi siedo vicino a lei, accanto alla finestra."

hi "Ehi, immagino tu sia Hakamichi, giusto? Piacere di conoscerti."

show misha cross_laugh
with charachange

mi_shi "Hahaha~!"

"Cosa? Sono preso alla sprovvista dalle sue risa."

show misha hips_grin
with charachange

mi_shi "Piacere mio!{w=0.5} Ma~!"

mi_not_shi "Piacere mio! Ma~!{fast}, io non sono Hakamichi, sono Misha! Questa è Hakamichi. Shicchan~!"

play music music_shizune fadein 0.3

show misha hips_grin at twoleft
show bg school_scienceroom at center
with charamove

show shizu basic_normal at tworight
with charaenter

"Con una risatina allegra, Misha punta alla ragazza accanto a lei, quella che ho visto usare la lingua dei segni prima. Sembra che mi abbia fissato per tutto il tempo."

"Annuisce una volta con nonchalance per dimostrare che accetta la mia presenza… ma a malapena."

"Ha capelli corti, ma accuratamente e ordinatamente pettinati, occhiali di forma ovale bilanciati sulla cima di un nasino delicato, e occhi blu scuri che sembrano alternarsi ogni pochi secondi tra analitici e lievemente annoiati."

hi "Piacere di conoscerti."

show shizu behind_blank at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

show misha sign_smile at twoleft
with charachange

show misha perky_smile at twoleft
with charachange

"Guarda immediatamente Misha, che sorride e fa alcuni rapidi gesti con le mani."

show shizu adjust_happy at tworight
with charachange

show shizu behind_smile at tworight
with charachange

"Hakamichi annuisce e fa alcuni segni a sua volta."

"Inizio a chiedermi se l' insegnante mi stava prendendo in giro, dicendo cose come “potrai parlare con gli altri” e “chi altri potrebbe spiegarti le cose meglio.”"

show misha hips_smile at twoleft
with charachange

mi "Posso vedere che sei un po' confuso, giusto?, Giusto? Ma, capisco perchè hai pensato che io fossi Shicchan!"

mi "Shicchan è sorda, quindi io sono la persona che traduce le cose da e per lei."

show misha hips_grin at twoleft
with charachange

mi "Sono come un interprete~! Dice che anche per lei è un piacere!"

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Sei il nuovo studente, vero? Bene, Shicchan, certo che lo è! Se non lo fosse, sarebbe stato lì in piedi senza ragione, giusto? Giusto~!"



label it_A2d:

mi "Sembra una persona molto interessante, non è vero~!"



label it_A2e:

"Misha mi guarda con una strana espressione, poi continua."

mi "Non sappiamo molto di lui, ma forse scopriremo qualcosa più tardi."

"Forse avrei dovuto presentarmi dopotutto. Qualunque cosa avrebbe dato una prima impressione migliore dell' insegnante che borbotta e si confonde col mio nome."



label it_A2f:

mi "Sapevamo che sarebbe arrivato un nuovo studente, ma non sapevamo che saresti arrivato oggi. Così presto! Hicchan, giusto?"

"Hicchan…?"

show misha hips_grin at twoleft
with charachange

mi "Yup~! Ti si adatta, no?"

"L' ho detto forte? E' solo una sorpresa. Non mi è mai piaciuto quel nomignolo."

hi "Non vedo davvero come."

show misha cross_grin at twoleft
with charachange

mi "Ti calza bene~! Sembri proprio come ti immaginavo!"

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha cross_laugh at twoleft
show shizu adjust_happy at tworight
with charachange

mi "Hahahaha~! Già, sembri proprio un Hicchan!"

hi "Mi chiedo perchè tutti sembrano pensarla così…"

shi "…"

"Hakamichi tamburella con le dita sul banco per attrarre l' attenzione di Misha. Eccitate scambiano nuovamente gesti avanti e indietro, le loro mani si muovono veloci quasi come lampi."

show shizu adjust_happy at tworight
with charachange

show misha sign_smile at twoleft
with charachange

show shizu behind_smile at tworight
with charachange

show misha perky_confused at twoleft
with charachange

"Misha sembra un po' in difficoltà."

show misha hips_grin at twoleft
with charachange

mi "Ahaha~! Ehmm, scusa per prima!"

show misha hips_smile at twoleft
with charachange

mi "Shicchan vuole che tu sappia che è la capoclasse, quindi se c'è qualcosa che vuoi sapere, non hai che da chiedere."

show shizu behind_blank at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Ti piace la scuola finora? Possiamo farti un po' da guide se non hai avuto il tempo per camminare in giro e…{w=0.5} familiarizzarti?{w=0.5} col posto!"

"Misha inciampa un po' sulla parola difficile, facendola spiccare nella sua traduzione altrimenti fluida."

hi "Grazie, sarebbe davvero di aiuto. Già, sono più o meno venuto dritto in classe oggi."

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_laugh at twoleft
with charachange

mi "Hahaha~!"

show misha hips_smile at twoleft
with charachange

mi "Così non va! Dovresti sempre cercare di informarti quanto più possibile sui posti dove stai andando prima di andarci. Non solo a scuola, tra l' altro~!"

show misha hips_grin at twoleft
with charachange

mi "Sempre! Anche se è una passeggiata fino al minimarket! Davvero, Shicchan? Hahaha~!"

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charachange

"Informarmi sui posti dove sto andando? Suppongo di non essermi preoccupato di farlo, o semplicemente non mi importava abbastanza per farlo."

"Non ero desideroso di venire qui, anche se ho negligentemente dato il mio tacito accordo alla proposta. Ma comunque…"

"Non dico nulla, e Misha segna qualcosa che termina con una stretta di spalle. Che era quello? Sembra che mi riguardasse."

"Ho voglia di sprofondare nella mia sedia. Entrambe stanno sorridendo, ma quella stretta di spalle mi ha colpito inaspettatamente duro."

show misha perky_sad at twoleft
with charachange

mi "Sembri depresso, tutto okay?"

show shizu basic_normal at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Non prenderla male, per favore~! Odio quando le persone hanno paura di fare domande! E' così che si imparano le cose, chiedendo~!"

mi "Chiedere aiuto è perfettamente normale, tanto quanto lo è aver bisogno di aiuto! Smetti di sembrare come se avessi appena fallito un esame!"

show misha cross_laugh at twoleft
with charachange

mi "Wahahaha~!"

hi "Va bene."

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Ah, e un' altra cosa, non c'è bisogno che tu chiami Shicchan qualcosa di formale come “Hakamichi” o “capoclasse” tutto il tempo! Basta che la chiami Shicchan~!"

stop music fadeout 0.5

show shizu adjust_blush at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Ahaha~! Okay, forse quello è troppo familiare. Forse “Shizune” sarebbe più appropriato?"

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

play music music_shizune fadein 5.0

mi "Yup, yup~! “Shizune” va benissimo!"

hi "Heh. Okay, quello mi sarebbe molto più facile."

"Mi sento molto più a mio agio. Entrambe sembrano talmente amichevoli, che mi sento come un idiota per essere stato tanto apprensivo prima. Specialmente riguardo a Shizune, che supponevo sarebbe stata una di quelle persone tutte affari."

"Bè, sembra ancora così. Solo di meno, immagino."

show shizu behind_frown at tworight
with charachange

shi "…!"

show misha perky_confused at twoleft
with charachange

mi "Eh? Oh, giusto, non abbiamo neanche toccato il compito! Dovremmo iniziare a lavorare adesso, o Shicchan si arrabbierà."

hi "Il compito è pure piuttosto lungo, così dovremmo iniziare ora se vogliamo finirlo prima che la lezione termini."

show misha hips_laugh at twoleft
with charachange

mi "Wahaha~! Sì, anche per quello!"

show shizu basic_frown at tworight
with charachange

shi "…"

"Shizune ci fissa con aria impaziente. Non ho bisogno di conoscere la lingua dei segni per capire."

hi "Okay, okay, messaggio ricevuto."

show shizu basic_normal at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Dopo le lezioni, possiamo fare una passeggiata insieme intorno alla scuola. Oggi è una bella giornata! Okay~?"

"Il compito è in verità molto complesso da svolgere, combinando aspetti di essere sia difficile che inutilmente lungo."

stop music fadeout 6.0

scene bg school_scienceroom
with shorttimeskip

"Nonostante tutto, lo terminiamo alcuni minuti prima di chiunque altro in classe, a dispetto di avere iniziato più tardi. Shizune e Misha sono davvero abili."

"Sono molto diverse però. La capoclasse è calma e professionale quanto sembra, mentre Misha ha un carattere molto più femminile e giocoso. Per non dire che si distrae un po' più facilmente."

"Per essere onesti, loro due hanno fatto la maggior parte del lavoro. Mi sento in colpa."

play sound sfx_normalbell

"Le campane della torre dell' orologio suonano, segnalando la fine della lezione. Ora di pranzare."

scene bg school_hallway3
with locationchange

"Non sapendo che altro fare, seguo Misha che mi sta facendo segno lungo il corridoio e giù per le scale."


    
#**************************************
label it_A3:

scene bg school_staircase2
with locationchange

"Scendiamo perfino al di sotto dell' atrio dove mi sono incontrato con Mutou, fino al piano più basso."

play ambient sfx_crowd_indoors fadein 6.0
$ renpy.music.set_volume(0.5, .5, channel="ambient")
play music music_normal

scene bg school_cafeteria
with locationchange

"Come tutto in questa scuola, la mensa sembra troppo spaziosa e stranamente moderna in contrasto con gli esterni classici."

"Le sue grandi finestre con arco danno verso il cortile, in direzione del cancello principale."

show misha hips_grin
with charachange

mi "E' la mensa~!"

"La sua entusiastica affermazione dell' ovvio fa sì che la gente intorno a noi ci fissi, ma Misha non sembra preoccuparsene così procediamo verso la fila."

hide misha
with charaexit

"C'è una lista di opzioni piuttosto lunga sul menù, il che sembra ottimo finchè non capisco che molte di esse esistono per accomodare gli studenti che necessitano di diete speciali."

"Che bello. Sembra quasi che sia tornato all' ospedale, a mangiare porzioni misurate con precisione scientifica per incontrare i bisogni dei pazienti."

"Scelgo qualcosa a caso e seguo Shizune fino a una tavola, sedendomi di fronte a lei."

show misha hips_frown at twoleft
show shizu basic_normal at tworight
with charaenter

"Mentre pilucco il cibo mediocre che preferirei non mangiare, Misha mi dà una gomitata per attrarre la mia attenzione e indica Shizune."

show misha perky_smile at twoleft
show shizu basic_frown at tworight
with charachange

shi "…"

"Non capisco la lingua dei segni, quindi mi sfugge il punto."

"Forse guardare la persona che ti sta “parlando” è corretto e cortese?"

show misha hips_smile at twoleft
show shizu behind_blank at tworight
with charachange

mi "Vuoi sapere qualcosa?"

hi "Cosa?"

show misha hips_grin at twoleft
with charachange

mi "Riguardo qualunque cosa! Siamo le tue guide quindi dovresti chiedere se vuoi sapere qualcosa~!"

label it_choiceA3:
menu:
    with menueffect
    
    hi "Hmm, mi chiedo se…"
    
    "Chiedere della biblioteca.":
        return m1
    
    "Chiedere della sordità di Shizune.":
        return m2
    
    "Credo di sapere tutto quello che devo sapere.":
        return m3        
    
label it_A3a:

hi "Oh, già. C'è una biblioteca nella scuola? Ultimamente sono diventato fanatico del leggere così mi piacerebbe dargli un' occhiata."

"Misha fa il tipo di smorfia che rende chiaro che non considera leggere come un hobby sano, ma poi recupera nuovamente il suo sorriso."

mi "C'è~! E' al secondo piano, possiamo fartela vedere una di queste volte!"

hi "Grazie."

"Ritorno al mio cibo mentre le ragazze parlano tra di loro."



label it_A3b:

"Shizune mi interessa, e ho un po' voglia di chiedere qualcosa di lei."

"Ma non posso proprio chiedere qualcosa di così personale, non è vero?"

"Hmm…"

"Non mi viene in mente niente altro da chiedere così mi limito a concentrarmi sul mio cibo mentre le ragazze parlano tra di loro."



label it_A3c:

hi "Non mi viene in mente niente, davvero."
 
mi "Ooh! Vuol dire che siamo state buone guide, vero, vero~?"
 
"…"
 
hi "Eeh… se lo dici tu."
 
"Misha diventa raggiante, e così fa Shizune dopo una rapida traduzione."
 
"Scuoto la testa al loro entusiasmo un po' troppo esagerato, e dirigo la mia attenzione al cibo."



label it_A3d:

"Misha e Shizune fanno segni avanti e indietro con grande animazione, lanciandomi occhiate di straforo, ma Misha evita di tradurre."

"Forse stanno parlando di cose segrete da ragazze o roba del genere."

"…"

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, .5, channel="ambient")
stop ambient fadeout 2.0

"Mi accorgo presto che una conversazione in segni non basta a riempire un silenzio."

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 0.5

"Arriviamo presto in aula, ma non siamo i primi."

show hanako emb_downtimid at Position(xanchor=0.8, xpos=1.0)
with charaenter

"Quella ragazza dai capelli scuri che ho notato prima è accasciata sul suo banco, nell' ultima fila."

show hanako defarms_shock at Position(xanchor=0.8, xpos=1.0)
with vpunch

show hanako defarms_shock at Position(xanchor=0.6, xpos=1.0)
with charamove

"Trasale un poco quando Misha irrompe nella stanza con l' eleganza di un rinoceronte."

"Si fa un po' più piccola nella sua sedia. Posso sentire la sua tensione fino da qui, come se si stesse lentamente trasformando in pietra solo a causa della nostra presenza."

"Misha e Shizune non se ne accorgono o non se ne preoccupano, poichè camminano direttamente oltre a lei verso i loro posti e iniziano a conversare."

show hanako defarms_shock at offscreenright
with charamove

hide hanako
with None

"Continuo a essere incuriosito da lei, anche quando l' aula lentamente si riempie con altri studenti e finalmente con l' insegnante."

"Entrare nel ritmo della scuola sembra strano; è come se il mio cervello ricordasse come si fa, ma il mio corpo no."

"Verso la fine della lezione inizio a sbadigliare e a contare i minuti rimasti."

"Non dovrei essere così stanco al mio primo giorno di scuola."

"Forse è tutto il tempo passato in ospedale che mi ha reso così. Mi sto perfino sentendo fisicamente debole e privo di vitalità."

stop music fadeout 2.0

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"Non molto dopo, suona l' ultima campana."

"Le lezioni sono finalmente terminate per oggi."

"Vicino a me, Misha a Shizune stanno avendo una breve conversazione. Dopo un po' di discussione, Misha si gira verso di me."

play music music_shizune fadein 0.3

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

mi "Sfortunatamente non possiamo rimanere e farti da guide oggi, Hicchan. Dobbiamo già sbrigarci, dato che c'è un sacco di lavoro da fare per noi."

show shizu basic_normal2 at tworight
with charachange

shi "…"

mi "Riuscirai a orientarti, ne sono sicura."

hi "Ah, aspetta! L' insegnante ha detto che avrei dovuto vedere l' infermiere. Dove devo andare?"

show shizu behind_smile at tworight
show misha hips_grin at twoleft
with charaenter

mi "Davvero? Possiamo almeno mostrarti quello~!"

mi "Vieni, gli infermieri hanno un edificio proprio quindi dobbiamo uscire."    

hide shizu
hide misha
with charaexit

scene bg school_hallway3
with locationchange

"Ci uniamo al flusso degli studenti che si stanno facendo strada giù per la tromba delle scale e fuori, mentre le ragazze indicano altre classi del terzo anno sul nostro stesso corridoio."

scene bg school_courtyard
with locationskip

"Quando usciamo, le ragazze si dirigono verso l' edificio più piccolo proprio adiacente alla scuola."

"E' costruito nello stesso stile così sembra essere parte dell' edificio principale."

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

mi "Questo qui è l' edificio ausiliario. Contiene un sacco di roba ufficiale e importante, come l' ufficio della Fondazione Yamaku e tutti gli uffici degli infermieri. Hanno persino una piscina!"

hi "E quella come è ufficiale?"

show shizu behind_frustrated at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Non essere sciocco, Hicchan! E' per la fisioterapia, ovviamente."

show misha sign_smile at twoleft
with charachange

mi "Comunque, anche tutte le attrezzature dello staff sono lì. L' ufficio del capoinfermiere è al primo piano."

show misha hips_smile at twoleft
show shizu behind_smile at tworight
with charachange

mi "Ce la farai da qui, giusto~? Allora noi andiamo! Ci vediamo domani!"

stop music fadeout 5.0

hide shizu
hide misha
with charaexit

"Un intero edificio per cose che non hanno niente a che fare con l' educazione vera e propria?"

"Suppongo che sia necessario per un posto come questo."

scene bg school_nursehall
with locationchange

"Entro, sperando che questa sia veramente solo una visita rapida come ha detto l' insegnante."

"Su una porta bianca alla sinistra c'è una croce verde con la scritta “Capoinfermiere” e una targhetta."

"Una voce dall' interno risponde quasi immediatamente quando busso, ma non riesco esattamente a comprenderla."

"Suonava un poco come un invito ad aprire la porta, quindi così faccio e mi autoinvito dentro."

scene bg school_nurseoffice
with locationchange

"La stanza non è grande e ha uno strano odore, ma un uomo dall' aria amichevole si gira sulla sua sedia mobile per guardarmi quando entro."

"Il suo posto di lavoro è bene ordinato, ma il cestino sotto la tavola è stracolmo di materiali sanitari usati e c'è almeno una dozzina di cerchi causati da tazze di caffè sul piano della scrivania."

play music music_nurse fadein 0.2

show nurse neutral
with charaenter

nk_ "Salve. Posso esserti di aiuto?"

"Ha l' aria giovane e lineamenti un poco irregolari, ma le fossette nelle sue guance cancellano quell' impressione quando sorride."

hi "Ehm, è lei l' infermiere?"

show nurse grin
with charachange

"Sorride come una persona che ha sentito esattamente questa domanda centinaia di volte."

nk_ "Sì certo, lo sono. Dice così sulla porta, no?"

nk "Puoi chiamarmi col mio nome o solo “l' infermiere” come fanno tutti."

"Ma certo. Mi scuoto dalla mia confusione, realizzando che probabilmente dovrei stringere la mano profferta.{w} La sua stretta è piuttosto ferma e amichevole."

hi "Giusto… ehh, sono un nuovo studente e il mio insegnante di riferimento mi ha detto di venire a presentarmi. Il mio nome è Hisao Nakai."

"I suoi occhi si illuminano in comprensione e fa schioccare le dita."

show nurse fabulous
with charachange

nk "Oh tu sei QUEL Nakai. Stavo giusto leggendo la tua cartella stamattina."

nk "Una qualche forma di aritmia cronica con correlata deficienza del muscolo cardiaco, giusto?"

"Fa segno di sedermi nella poltrona vuota di fronte alla sua scrivania."

hi "Eh, sì."

show nurse neutral
with charachange

nk "Bene. Bè, sei probabilmente già stato sufficientemente introdotto alla scuola, quindi mi limiterò a riassumere rapidamente."

nk "Abbiamo vari generi di servizi disponibili, per la maggior parte fisioterapia e simili."

nk "C'è sempre qualcuno del mio staff a disposizione, anche di notte, quindi non esitare mai a chiamarci se c'è un problema."

"Il famoso staff infermieristico ventiquattr' ore su ventiquattro."

hi "Wow, questo posto è come un ospedale."

nk "Bè, non proprio. Per esempio, qui non pratichiamo neurochirurgia."

"La sua battuta sembra così fuori luogo che rimango a chiedermi perchè l' abbia addirittura detta."

hi "Già… solo che è veramente strano avere così tanto personale medico in una scuola."

nk "Ti ci abituerai."

"Io non ne sono così sicuro ma non lo faccio sapere all' infermiere."

nk "Adesso, lasciami solo ritrovare la tua cartella…"

"Mentre cerca qualcosa nel suo computer e rimescola pile di fogli, lascio vagare il mio sguardo per la stanza."

"E' l' epitome del generico, devo davvero dire."

"Muri e soffitto beige, pavimento di laminato grigio scuro e tutto l' equipaggiamento che ti aspetteresti da un' infermeria scolastica."

"Perfino i ridicoli poster educativi appesi su tutti e quattro i muri, che mi ricordano di mangiare bene — tre volte al giorno e da tutti i gruppi di cibi."

show nurse grin
with charachange

"Sorridendo, l' infermiere estrae una spessa cartella da una pila di similarmente spesse cartelle e la apre."

nk "Quindi, hai già medicinali per l' aritmia, ricorda solo di prendere le tue pillole tutte le mattine e sere o non serviranno a molto."

show nurse fabulous
with charachange

nk "A parte quello… pratichi qualche sport? Roba rischiosa come… non so, la boxe?"

"Sogghingna alla sua battuta ma io non lo imito."

hi "Eh, bè. Giocavo a calcio occasionalmente con alcuni compagni di classe."

nk "Va bene, temo di doverti raccomandare di evitarlo, almeno per il momento."

hi "Oh."

"La mia mancanza di reazione gli fa inarcare un sopracciglio, ma davvero non sono troppo preoccupato dal suo divieto di tirare calci al pallone."

"Immagino di non averlo mai fatto a causa di un' ardente passione per lo sport. Solo per aver qualcosa da fare."

nk "Qualunque tipo di impatto potrebbe essere molto pericoloso per il tuo cuore e rischiare un altro attacco non è una buona idea."

nk "Quello precedente è stato causato da un impatto improvviso al tuo torace? Non c'è menzione della causa nelle tue carte."

hi "Ehh… non esattamente."

show nurse concern
with charachange

"Evado la domanda in modo accettabile, e mi lancia uno sguardo al di sopra delle sue carte, con un' espressione più seria sul suo viso."

nk "Comunque, devi mantenere il tuo corpo in forma così un po' di esercizio ti farebbe bene."

nk "Come ho detto abbiamo fisioterapia e roba del genere a disposizione, ma non credo che ti servano davvero delle misure così pesanti."

nk "Pratica solo regolarmente un poco di esercizio leggero."

nk "Camminate a passo veloce o anche jogging leggero, salto della corda, quel genere di cose. Nuoto, forse? Abbiamo una piscina qui."

hi "Così mi è stato riferito."

show nurse neutral
with charachange

nk "Davvero? Molto bene."

nk "In ogni caso, e sono sicuro che ti è già stato detto, devi solo fare attenzione a non sforzarti troppo."

"Scuote un dito per enfatizzare il punto. Davvero non ce n'è bisogno, ho già sentito questa storia mille volte."

show nurse concern
with charachange

nk "Assolutamente nessun rischio inutile. Prenditi cura di te stesso."

hi "Okay."

"Scorre le mie carte un' altra volta e le appoggia sulla scrivania, chiaramente soddisfatto."

show nurse neutral
with charachange

nk "Bene. Questo è quanto, allora. Vienimi a trovare se mai ne senti il bisogno."

scene bg school_nursehall
with locationchange

"Vengo congedato prima ancora che me ne accorga. Davvero una visita rapida."

stop music fadeout 0.75



#***************************************

label it_A4:

scene bg school_courtyard
with locationchange

"Finisco per trovarmi di fronte all' edificio principale e all' edificio ausiliario, anche se ai miei occhi continuano a sembrare essere una e la stessa cosa."

play music music_pearly fadein 0.2

"E' la prima vera occasione che ho di guardare gli altri studenti, così guardo gente che esce dalla scuola, che va verso il cancello o i dormitori."

"Tutti sembrano sapere dove stanno andando."

"E io continuo a pensare che la maggior parte di loro non sembrano troppo speciali per essere studenti di una scuola speciale. D' altra parte, non lo sembro neanche io."

"Questo mi rende uno di loro?{w} Uno di noi?"

"…"

"Dovrei andare da qualche parte anche io, per evitare di perdermi."

"E' più o meno ora di cena, ma mi sento stanco invece che affamato."

"La stanchezza in me continua a crescere man mano che barcollo verso i dormitori, collocati a breve distanza dal complesso di edifici principale."

scene bg school_gardens2
with locationchange

"C'è una sorta di giardino tra la scuola e i dormitori; cespugli, fiori e quel soverchiante odore di erba tagliata di fresco che riempie l' atmosfera."

"Sovviene alla mia stanca mente che l' odore sembra nuovo perchè non sono stato affatto all' aperto per così tanto tempo."

scene bg school_dormext_start at bgleft #downplaying the mural here
with locationchange

"L' edificio del dormitorio è grosso e fatto di mattoni rossi. Come gli altri, sembra decisamente troppo pomposo per quel che è, così procedo ed entro."

scene bg school_dormhallground
with locationchange

"Ci vuole più tempo del necessario per pescare la chiave che mi è stata data dalla mia tasca."

hi "Stanza uno-uno-nove…"

"A dispetto dell' esterno ornato, l' interno del dormitorio è piuttosto nuovo, funzionale, e noioso."

"Come per l' edificio principale, i corridoi e le porte sono larghi per accomodare sedie a rotelle."

"Faccio capolino intorno all' angolo formato dalla porta del soggiorno."

"Dentro, alcuni studenti stanno guardando la televisione."

"Uno fa un breve cenno di assenso a mò di “salve” prima di tornare a girarsi verso la TV."

"Sembra che da queste parti solo le ragazze siano socievoli. Credo che a me stia perfettamente bene."

"Mi arrampico su per le scale fino al piano superiore."

scene bg school_dormhallway
with locationchange

"Qui, piccoli corridoi si diramano da quello principale."

"Ciascuno di questi corridoi minori sembra avere un bagno e doccia, oltre a quattro stanze."

"Circa a metà del corridoio, vedo la stanza 119."

"I cartellini per i nomi delle stanze adiacenti alla mia sono vuoti. Credo che siamo solo in due qui."

"Della luce splende da sotto la porta della stanza 117, così busso piano."

stop music fadeout 1.0

hi "Salve, c'è nessuno?"

"Dall' interno sento alcuni movimenti, poi lo scattare di molti più lucchetti di quanto credessi queste porte avessero. Dopo un momento la porta si apre cigolando."

play music music_kenji fadein 0.5

show kenji tsun at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

"Un ragazzo occhialuto è in piedi sulla soglia. Mi sta guardando con aria molto intenta attraverso i suoi occhiali estremamente spessi."

ke_ "Chi è?"

"Cieco? No, almeno non del tutto, perchè avrebbe degli occhiali se lo fosse?"

show kenji tsun_close
with characlose

"Si china verso di me finchè quasi i nostri nasi si toccano. Il suo alito puzza d' aglio."

hi "Hisao Nakai… mi sto trasferendo nella stanza accanto. Pensavo che avrei dovuto presen…"

show kenji happy
with charadistant

"La sua faccia improvvisamente si illumina in comprensione, e si raddrizza di nuovo, estendendo la sua mano in un sorridente saluto, quasi dritta nel mio diaframma."

ke_ "Oh, come va amico? Il nome è Kenji."

hi "Ah, ciao."

"Prendo la mano sudata di Kenji e la stringo, ancora un po' scosso dall' improvviso cambio di attitudine e veemente benvenuto."

ke "C'erano delle persone dall' aria sospetta che entravano e uscivano dalla tua stanza prima."

hi "Probabilmente erano i miei genitori."

show kenji tsun
with charachange

ke "I tuoi genitori? Sei sicuro? Perchè potrebbe anche essere stato qualcun altro. Non puoi giudicare un libro dalla sua copertina."

"Il suo proverbio fuori posto rimane imbarazzante nell' aria tra di noi mentre cerco di pensare a un qualche modo di rispondere."

hi "Direi che le possibilità sono abbastanza alte."

show kenji happy
with charachange
 
"Rabbrividisce e fa alcuni gesti esagerati con le mani."

ke "Sei un uomo coraggioso, Hisao."

ke "Io non credo che potrei fidarmi delle possibilità."

show kenji neutral
with charachange

ke "L' unico di cui mi fido è me stesso."

hi "Vorrebbe dire che neanche io dovrei fare conoscenza con te?"

"Ci pensa sopra per un po'."

ke "Una saggia decisione."

show kenji happy
with charachange

ke "Dannazione, sei più sveglio di quanto sembri."

ke "Probabilmente."

ke "Come sembri? Spero non sveglio."

show kenji neutral_close
with characlose

"Strizza gli occhi e si china di nuovo verso di me, ma io mi ritiro per schivarlo."

show kenji tsun
with charadistant

ke "Lascia perdere, non importa."

hide kenji
with charaexit

"Con quello, si gira, annaspa per un momento in cerca della maniglia della porta, e la chiude dietro di sè."

stop music fadeout 0.5

"Inserisco la chiave nel lucchetto della porta marchiata 119."

scene bg school_dormhisao_ss
with locationchange

play music music_night fadein 0.5

"Nudi muri beige, lenzuola bianche, una scrivania fatta di legno scadente. Brutte tendine."

"E' la stanza di nessuno; impersonale, come lo era la mia stanza di ospedale."

"Le mie borse sono ai piedi del mio letto, e sembrano molto più vuote di quanto fossero stamattina."

"L' armadio è aperto, ed è pieno dei miei vestiti."

"Inoltre, sembra che ci sia anche un certo numero di uniformi scolastiche appese."

"Un biglietto è appuntato alla manica di una delle camicie."

$ written_note("Ciao Hicchan. Abbiamo disfatto le tue valigie, e fatto il letto.\nHanno detto che se queste non sono della taglia giusta dovresti andare all' ufficio domani.\nSe hai dei problemi, puoi sempre chiamarci.\n\nCon amore, Mamma e Papà.")

"Bene, almeno non devo preoccuparmi di disfare i miei bagagli."

"Stavo più o meno sperando di doverlo fare, così avrei avuto qualcosa di cui occuparmi."

"E' ancora troppo presto."

"Appoggio il biglietto sulla mia scrivania e mi corico sul letto, sentendomi svuotato."

"Stare sdraiato qui mi fa voler leggere qualcosa, ma non ho nulla con me."

"Mi chiedo se l' ospedale mi ha condizionato a voler leggere ogni volta che non ho niente da fare."    

"Il desiderio nervoso continua solo a crescere al punto che devo alzarmi."

"Forse è stress o qualcosa del genere."

"Ero piuttosto nervoso al riguardo prima di venire qui, e anche per tutta la giornata di oggi. Lo sono ancora, credo."

"Dannazione, mi devo distrarre in qualche modo, in modo da non essere così innaturale tutto il tempo."

"Domani, andrò a prendere in prestito qualche libro dalla biblioteca."

"Già, farò così."

"Ma per adesso…"

"Le bottigliette di medicinali ordinatamente sistemate sul mio comodino attirano la mia attenzione."

"Ne raccolgo una e la scuoto solo per sentire i contenuti tintinnare all' interno, e poi leggo l' etichetta incollatavi dalla farmacia."

$ written_note("Hisao Nakai\n\nDue compresse al giorno per restare vivo")

"Non dice veramente così, ma potrebbe anche farlo."

"E' piuttosto contorto, che la tua vita dipenda da delle sostanze chimiche in questo modo. Me ne risento un poco, ma che scelta ho?"

"Con un sospiro, comincio il mio nuovo rituale giornaliero di prendere il giusto numero di pillole da ogni bottiglia, controllando attentamente che i dosaggi siano giusti."

"…"

"Mi corico di nuovo, sentendomi vuoto e incerto, e dopo di quello continuo a fissare il soffitto vuoto ed estraneo per molto tempo."

scene bg school_dormhisao_ni
with Dissolve(3.0)

"Non inizia a sembrare più familiare, nemmeno dopo che cade l' oscurità e delle lunghe ombre si estendono lungo la mia stanza come dita."

"Le lenzuola sembrano leggermente più confortevoli, calde e simili a un nido contro il gelo che passa per temperatura ambiente da queste parti."

"Presto la sfumatura di oscurità più chiara che è il soffitto sembra come qualunque soffitto di notte, e diventa l' unica cosa che riesco ancora a riconoscere."

"La notte mi invita a dormire, e io sento il gelo della mancanza di familiarità e la paura che strisciano nuovamente su per la mia schiena."

"Continuo ad allontanarmi lentamente alla deriva dal mondo che conoscevo."    

stop music fadeout 2.0

scene black
with shuteye


return

