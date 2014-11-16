label it_A31:

scene black
with None

play music music_daily fadein 2.0

scene bg school_scienceroom
with Dissolve(2.0)

"Gli studenti entrano in classe per la sessione di sabato mattina, e assolutamente ognuno di loro sfoggia gli occhi stanchi di chi ha lavorato per tutta la notte."

"Con solo un giorno rimasto per prepararsi suppongo che non sia sorprendente. Grazie al cielo dobbiamo soffrire per le lezioni solo fino all' ora di pranzo, e poi il nostro tempo è libero."

show muto irritated
with charaenter

"Mutou barcolla in classe con stanca baldanza. Immagino che gli studenti non siano i soli qui a godersi le ore piccole di venerdì."

"Senza dire una parola, scribacchia i numeri di una pagina e di alcuni problemi sulla lavagna e si accascia sulla cattedra."

"E' un comportamento completamente atipico per lui, ma sembra che nessuno in classe abbia intenzione di farglielo presente."

hide muto
with charaexit

play sound sfx_paper

"Senza una parola gli studenti arrangiano i loro libri di testo in posizione e si mettono al lavoro. Non volendo andare contro tendenza, faccio lo stesso."

"La stanchezza ha reso antisociale la classe; non si sente volare una mosca in mezzo allo sfogliare carte."

"Quello può essere parzialmente attribuito ai due posti vuoti accanto a me. Per qualche motivo Misha e Shizune non sono presenti; probabilmente stanno facendo del lavoro per il consiglio e il festival."

"E' molto silenzioso quando Misha non c'è."

"Mi chiedo se Misha è nata rumorosa come è, o se sta “compensando” per la carenza di voce di Shizune."

show muto normal
with charaenter

mu "Nakai, posso parlarti un momento?"

"Sono tanto dedito a pensare a Misha che non mi accorgo nemmeno di Mutou che si avvicina al mio banco."

hi "Sì… riguardo a cosa?"

mu "Probabilmente è meglio se parliamo fuori dall' aula…"

hide muto
with charaexit

"Qualcosa riguardo a questo intero affare non mi suona troppo bene, ma mi alzo e lo seguo nel corridoio."

stop music fadeout 2.0


label it_A31b:

scene bg school_hallway3
show muto normal
with locationchange

#conditional section; seen if you have a heart attack

"Mutou aspetta nel corridoio, grattandosi il capo mentre decide cosa sta cercando di dire. Non sapendo cosa sta succedendo, aspetto in silenzio."

mu "Ho sentito dal capoinfermiere scolastico che hai avuto un incidente l' altro giorno."

"Ah. Così riguarda quello."

hi "Beh, qualcosa del genere, ma non è nulla di cui preoccuparsi."

show muto irritated
with charachange

mu "Sì, sì lo è. Qualunque cosa possa mettere in pericolo la tua salute è qualcosa di cui preoccuparsi."

mu "Qui facciamo del nostro meglio per prepararvi alla vita. Parte di quello comprende conoscere i propri limiti, e come aggirarli."

mu "Sarebbe negligente da parte mia se non parlassi di questo."

hi "Va bene, ho capito. Mi dispiace."
    
"Mutou chiude gli occhi in frustrazione, e capisco che questa probabilmente non era la cosa migliore da dire."

mu "Qualcosa mi dice che non ti dispiace. Fingi quanto vuoi, ma questa non è una scuola normale."

mu "Molte persone hanno speso molto tempo, fatica e denaro per assicurarsi che tu, e ogni altro studente qui, possa avere lo stesso livello di educazione dei vostri pari."

mu "Che tu abusi di questo ignorando dei consigli, specialmente dei consigli medici, è semplicemente egoista."

"Non sono completamente sicuro se questo è davvero quello che pensa, o se è una specie di recita che ha provato molte volte per far sentire in colpa gli studenti e fargli fare la cosa “giusta”. Qualunque sia il caso, sta funzionando."

hi "Capisco. Tutto questo mi è nuovo, e mi scuso. Adesso conosco i miei limiti, e starò attento a seguirli."

show muto smile
with charachange

"Mutou sembra rilassarsi un poco, soddisfatto che il suo messaggio sia stato ricevuto."



label it_A31c:

scene bg school_hallway3
show muto normal
with locationchange

#Conditional section, if you didn't have a heart attack

"Mutou aspetta nel corridoio, grattandosi il capo mentre decide cosa sta cercando di dire. Non sapendo cosa sta succedendo, aspetto in silenzio."

mu "Così, dimmi, come vanno le cose?"

hi "Le cose?"

"Mi aspettavo che Mutou sarebbe stato un po' vago, ma questo è esagerare."

show muto irritated
with charachange

mu "Lo sai. Le cose. Ormai hai avuto una settimana per adattarti ormai, così come vanno le cose?"

hi "Uhh, direi bene."

show muto normal
with charachange

mu "Vedo. E come va la tua… condizione?"

"La pausa prima di “condizione” sembrava un po' eccessiva."

hi "Non ho avuto problemi finora."

show muto smile
with charachange

"Un breve lampo di sollievo passa sulla faccia di Mutou."

mu "Bene, molto bene. L' infermiere scolastico era un poco preoccupato che potessi stare sforzandoti un po' troppo."

mu "Mi ha chiesto di tenerti d' occhio quando lui non poteva."

hi "Bè, ha senso…"

show muto normal
with charachange

mu "Ti chiederei di non prenderci così alla leggera. Per quanto possiamo cercare di darti il livello di educazione che riceveresti in una scuola normale, devi capire che hai dei limiti."

mu "Il nostro scopo è di assicurarci che tu conosca dove sono quei limiti, e come massimizzare il tuo potenziale entro di essi. Mi segui?"

hi "Credo di sì. Voglio dire, non ho intenzione di fare niente di stupido."

show muto smile
with charachange

mu "Bene, suppongo che quello sia un inizio."

#conditionals end.



label it_A31d:

play music music_daily fadein 0.3

show muto normal
with charachange

mu "Così, passiamo alla mia prossima domanda; come stai trovando i tuoi studi? Mi è stato detto che sei stato costretto a letto per un certo tempo. Non siamo troppo avanti, vero?"

hi "Credo veramente di no. Ho cercato di stare al passo coi miei studi quando ero in ospedale, così non è stata troppo dura."

show muto irritated
with charachange

"Mutou si accarezza il mento e inarca un sopracciglio mentre assorbe questa informazione."

mu "Davvero… suppongo che ancora esistano degli studenti che capiscono l' importanza della cultura…"

"Non arriverei fino a tanto, stavo solo cercando di mantenermi occupato nella mia piccola prigione salvavita."

hi "Bè, sì. Bisogna tenersi al passo con queste cose, giusto?"

show muto smile
with charachange

mu "E' esattamente così. Una mossa falsa in questo mondo e rimani indietro, giusto?"

hi "Uh, giusto. Non vorrei che mi capitasse."

show muto normal
with charachange

mu "No, no non lo vorresti. Ogni settimana c'è una nuova scoperta scientifica. La maggior parte non significano nulla per i profani, ma una qualunque di esse potrebbe essere la chiave per la prossima Cosa Importante."

hi "Lo terrò in mente…"

"E' ovvio che il Discorso Serio di Mutou è finito, e che è tornato al suo solito, leggermente distratto approccio alla vita."

"Penso, col senno di poi, di preferirlo così. E' leggermente più prevedibile nella sua imprevedibilità."

show muto smile
with charachange

mu "Allora bene, penso che quello fosse tutto quello che avevo da dire. Torniamo dentro, eh?"

"Il mio sollievo a quel suggerimento è insormontabile."

hi "Certo. E' lei il capo, giusto?"

show muto normal
with charachange

"Mutou si ferma un momento."

mu "Non credo che nessuno dei miei studenti me lo abbia mai detto prima d' ora."

"Per un istante considero di rispondere, ma qualcosa di profondo dentro di me mi dice di chiudere il becco e rientrare in aula."

scene bg school_scienceroom
with locationchange

"Alcuni degli studenti sobbalzano al suono della porta, tentando rapidamente di fingere di stare lavorando sui problemi alla lavagna."

"Alcuni non si danno nemmeno pena, le loro teste chine sul banco mentre dormicchiano. Fortunatamente, pare che Mutou non li noti nemmeno."

"Ritorna alla sua cattedra e recupera una rivista scientifica da uno dei cassetti. Immagino di averlo colpito."

"La classe ritorna al quasi-silenzio in cui Mutou e io l' abbiamo lasciata prima della nostra chiacchierata."

"Sentimenti misti di stanchezza e anticipazione ronzano per la sala. Tutti qui sono o in attesa della possibilità di riposare o di quella di mettere in moto le loro preparazioni dell' ultimo minuto."

play sound sfx_normalbell

"L' orologio sul muro lentamente ticchetta via il tempo rimanente della lezione, finchè finalmente le campane cantano, terminando il tormento."

show muto normal
with charaenter

mu "Prima che ve ne andiate, aspetto le risposte a quei problemi per lunedì."

hide muto
with charaexit

"La classe sospira in unisono, istantaneamente pentendosi di aver poltrito, ma ancora acutamente conscia delle questioni più urgenti al momento."

#The below section is supposed to be on the HL side of things; I'm not sure what we're doing for the ER paths

"L' aula si svuota in un batter d' occhio quando tutti corrono verso le loro preparazioni dell' ultimo minuto per il festival."

stop music fadeout 2.0

"Io resto indietro e cerco di finire i problemi in fretta così da non dovermene preoccupare durante il resto del weekend, col festival e tutto il resto in arrivo domani."

show bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with charamoveinright

"A parte me, Hanako è l' unica che rimane, ovviamente in attesa di Lilly."

"E' strano che Lilly venga fino allla nostra aula a prenderla. Per lei è un viaggio inutile, e credo che andare in giro sia almeno nominalmente più difficile per lei di quanto lo sia per Hanako."

"Ma non sono affari miei, e naturalmente non faccio domande ad Hanako."

"A dispetto della relativa vicinanza dei nostri posti, nessuno cerca di aprire una conversazione riguardo a quello o a qualunque altra cosa, così un silenzio opprimente cade sull' aula."

"Il tempo passa in silenzio. E' probabilmente solo circa un quarto d' ora ma sembra di più. Io giro pagine del mio quaderno. Hanako gira pagine del romanzo che sta leggendo."

"La mina del mio portamine si spezza contro la carta proprio quando stavo per terminare un paragrafo."

"Il sospiro irritato e il mio rovistare in cerca di un rimpiazzo sembrano stare spezzando l' atmosfera nell' aula."

"Hanako mantiene il suo sguardo fermamente distolto dalla mia direzione."

"In breve tempo, l' alta figura di Lilly appare alla porta."

show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom
show hanako emb_downtimid at offscreenright
show lilly basic_smileclosed at left
with charamove

li "Hanako?"

show lilly basic_smileclosed at twoleft
show bg school_scienceroom at bgright
show hanako emb_downsmile
with charamove

"Il suo nome è tutto quel che serve perchè Hanako balzi dal suo banco e corra da Lilly."

hide lilly
with charaexit

show hanako emb_downsad
with charachange

show hanako emb_downsad at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_out_time_warp)
with None

hide hanako
with charaexit

"Parlano sottovoce per un momento, ma non ci vuole molto prima che Lilly se ne vada per il corridoio e Hanako torni in aula, sedendosi di nuovo al suo posto."    

show hanako emb_downsad at offscreenright
with None

show bg school_scienceroom at bgleft
show hanako emb_downsad at right
with charamove

"Osservo Hanako con la coda dell' occhio per pura curiosità all' idea che le due siano separate."

"Per un paio di minuti, non fa nulla eccetto sedere con il mento nella mano, fissando il banco con aria demoralizzata."

show hanako emb_downtimid at right
with charachange

"La noia evidentemente diventa troppo per lei però, e la sua forma snella cerca nella sua borsa ed estrae un piccolo libro."

"Ora che ci penso, quello non è il libro che le ho visto leggere in biblioteca. Deve essere una lettrice davvero veloce per divorarli a questa velocità."


label it_31e:

"Dopo circa dieci minuti di agitarsi nervosamente al suo posto e cercare di leggere, Hanako chiude il suo libro e se ne va a sua volta."

"Come dovrei fare io, dato che ho praticamente finito con i compiti e non c'è nient' altro da fare in aula."

scene bg school_dormhisao
with locationskip

"Non sentendomi davvero energico, vado dritto alla mia stanza e leggo per il resto della giornata."

scene black
with Dissolve(3.0)


#******************'
    
label it_A32:

scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None

hide hanako
with charaexit

"Dopo circa dieci minuti di agitarsi nervosamente al suo posto e cercare di leggere, Hanako chiude il suo libro e se ne va a sua volta."

"Come dovrei fare io, dato che ho praticamente finito con i compiti e non c'è nient' altro da fare in aula."

"Non che abbia qualcosa da fare da qualche altra parte."

scene bg school_hallway3
show crowd
with locationchange

play music music_dreamy fadein 0.3

play ambient sfx_crowd_indoors fadein 0.3

"La scuola è un alveare di attività ma nessuno fa caso a me."

"Passeggio di fronte ad aule piene di studenti freneticamente impegnati a fare questo e quello, ronzanti tutto intorno come piccole api operaie."

"Non si direbbe che la scuola sia finita per oggi."

scene bg school_courtyard
show crowd
with locationskip

play ambient sfx_crowd_outdoors fadein 0.2

"All' esterno è un po' più tranquillo, ma non di molto."

"Persone schizzano via da destra e manca, affrettandosi quanto più possono; occupate ed energiche."

"Io sento l' esatto contrario. Il sole di mezzogiorno sembra stare risucchiando tutto lo spirito dal mio corpo, facendolo sentire completamente floscio."

"Aria calda e soffice scorre dentro la mia camicia, dandomi l' impressione di un cuscino."

"Sbadiglio pigramente, pensando a cosa fare."

"Per prima cosa lascerò i miei libri ai dormitori, e poi… farò qualcosa che non ho ancora deciso."

"Forse Kenji è nella sua stanza."

stop ambient fadeout 1.0
stop music fadeout 1.0

scene bg school_dormext_half
with locationchange

"Lungo la strada per i dormitori, vedo Emi che sta venendo nella mia direzione, correndo anche se non indossa quelle strane protesi da corsa. La saluto agitando la mano e lei frena bruscamente."

show emi basic_closedgrin
with charamoveinright

emi "Ehi Hisao!"

"Macchie di pittura bianca e verde decorano rispettivamente il suo naso e il suo mento, ma il suo sorriso è ampio, come sembra sempre essere."

show emi excited_happy_close
with characlose

"Si china più vicino a me, amplificando la sensazione che mi stia esaminando."

emi "Chestaifacendo?"

hi "Niente, a dire il vero. Non ho nulla da fare per il festival e tutti gli altri sembrano stare facendo qualcosa di importante."

show emi excited_laugh_close
with characlose

emi "Perfetto! Allora puoi aiutare me e Rin!"

hi "Con le preparazioni per il festival? Eeeh, non sono sicuro che sarei di molto aiuto."

show emi excited_proud_close
with characlose

emi "Nessun problema! Neanche io sono di molto aiuto!"

"Emi afferra il mio polso e inizia a tirarmi di nuovo dentro la scuola con forza."

scene bg school_lobby
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.3

"Perfino il suo passo mentre cammina è più simile a un trotto, facendomi inciampare sui miei piedi mentre tento semplicemente di seguirla."

scene bg school_staircase2
with locationchange

"Le scale rallentano Emi un tantino. Forse è difficile salirle con le sue gambe, o forse ha finalmente perso il fiato."

scene bg school_hallway3
show crowd
with locationchange

"Torniamo indietro fino al terzo piano e al corridoio delle terze classi, finendo al posto da dove me ne sono andato cinque minuti fa. Avrei potuto rimanere lì ad aspettare Emi, se lo avessi saputo."

hi "Così stai… Rin sta ancora lavorando a quel murale?"

show emi basic_closedgrin
with charaenter

emi "Esatto! Ha bisogno di un sacco di pitture e pennelli e roba, così glie li porto dall' aula d' arte."

hi "E hai bisogno di me per aiutarti."

show emi basic_grin
with charaenter

emi "Bè… Rin ha detto che la hai già aiutata prima così ho pensato che non ti sarebbe dispiaciuto."

hi "Vedo."

stop ambient fadeout 2.0

scene bg school_classroomart at bgright
with locationchange

"Così a dispetto della logica sgangherata di Emi, eccomi di nuovo qui, a raccogliere roba dall' aula d' arte per conto di altri. "

play music music_dreamy fadein 0.3

"La stanza è vuota eccetto per noi e i solitari granelli di polvere che fluttuano nell' aria. Emi saltella dritta verso il retro, estraendo un minuscolo, sgualcito pezzo di carta dalla sua tasca."

"Mentre lei cerca di decifrare la scrittura scarabocchiata, io osservo più da vicino i materiali sparsi qui in giro."

"Dozzine di latte e bottiglie di pittura sono disposte sugli scaffali in un modo estremamente disorganizzato."

"Alcune sembrano essere rimaste qui per diverse decadi; reliquie di generazioni precedenti del club d' arte."

"Accanto alle pesanti cataste di carta da disegno ordinatamente impilata si trovano delle scatole piene di pennelli di diverse dimensioni e pastelli alla rinfusa."

"Gli odori di pittura, trementina e carta nuova fluttuano nell' aria stagnante, mischiandosi nelle mie narici per formare quell' inconfondibile odore d' arte."

show emi basic_closedgrin at offscreenright
with None

scene bg school_classroomart at bgleft
show emi basic_closedgrin at right
with charamove

"Emi studia i suoi appunti e li compara con i marchi su varie latte di vernice, passandomele quando trova quelle giuste."

show emi basic_grin at right
with charachange

"Si mette in punta di piedi per guardare sullo scaffale più alto, ma non è proprio sufficiente."

show emi basic_annoyed at right
with charachange

"Non importa cosa faccia il livello del suo sguardo rimane al di sotto dello scaffale. Emi desiste e si limita a guardare in alto con desiderio, come un bambino in un negozio di giocattoli, sbuffando in irritazione."

show emi annoyedbounce
with None

"Dopo un momento di crescente rabbia, inizia a saltare su e giù, apparentemente cercando di leggere le etichette durante la frazione di secondo in cui le può vedere, e di prendere quel che può."

show emi basic_closedsweat at right
with charachange

"Non è una sorpresa che fallisca miseramente, e quasi riesca a far crollare l' intero scaffale."

"Adesso vedo perchè il mio darle una mano potrebbe essere utile."

hi "Su, lascia che lo faccia io. Non puoi saltare abbastanza in alto e non voglio che tu ti faccia male provandoci."

hi "E poi, sono tipo due volte più alto di te."

show emi sad_angry at right
with charachange

emi "Non è vero!"

"Si gira, infiammata di disprezzo, guance rosse e tutto quanto."

hi "Scherzo, sto scherzando. Comunque, guarderò io quassù, okay?"

show emi basic_annoyed at right
with charachange

"Mi dà un' altra occhiataccia ma non può trovare una replica. Con un riluttante “hmpf,” mi volta la schiena."

hide emi
with charaexit

"Così inizio a setacciare lo scaffale più alto in cerca di vernici, mentre Emi si china per recuperare quello che può dagli armadi."

"Scuoto un po' la testa, dopo essermi doppiamente assicurato che non mi possa vedere farlo."

"E' una sorpresa che Emi abbia un complesso riguardo la sua statura; non l' avrei presa in giro altrimenti."

"Sembra tranquilla ma immagino che tutti abbiano i loro punti deboli."

show emi basic_grin
with shorttimeskip

"Solo dopo che abbiamo raccolto e sparso su un banco quasi tutti gli oggetti come il bottino di cacciatori di tesori, capisco che non era necessariamente la battuta sull' altezza quella che la ha fatta irritare."

"Potrebbe non piacerle sentirsi dire che non può fare qualcosa. Come saltare."

"Ma Emi stessa sembra avere già dimenticato tutto. Pronta ad arrabbiarsi, pronta a perdonare… è quel tipo di persona?"

"Almeno non sembra essersela presa, dato che chiacchiera allegramente mentre raccogliamo il resto degli oggetti e torniamo indietro portandoli con noi."


stop music fadeout 2.0

scene bg school_courtyard
show crowd
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 0.2

"Cavallererescamente trasporto la maggior parte di essi mentre ci facciamo strada verso i dormitori."
    
show emi basic_annoyed
with charaenter

emi "Rin è veramente stressata dal dover finire il suo dipinto. E' colpa sua però; avrebbe dovuto cominciare prima."

hi "Riuscirà a farcela?"

show emi basic_closedgrin
with charaenter

emi "Non ho idea. A me sembra bello ma con Rin, non sai mai che sta succedendo."

show emi basic_annoyed
with charaenter

emi "L' ho trovata stamattina a terra davanti al dormitorio in posizione fetale. Non aveva dormito tutta notte. Non posso credere che le infermiere notturne non l' abbiano trovata."

show emi basic_grin
with charaenter

emi "E adesso sta dipingendo di nuovo come una matta."

hi "Già, ho… notato che sembra un po'… suonata. Per così dire."

show emi basic_closedhappy
with charaenter

"Emi fa una risatina a quello, e al mio probabilmente troppo ovvio imbarazzo."

show emi basic_happy
with charaenter

emi "Non ci faccio caso. E' solo un po' strana qualche volta."

"Su quello posso essere d' accordo con lei. A differenza di me, Emi sembra non essere snervata da… qualunque cosa sia che fa sembrare Rin così fuori fase."

"Comunque, non sembrano affiatate come Misha e Shizune. Con loro che qualche volta operano come una singola entità, è difficile dire dove una finisce e comincia l' altra."

"Anche se sono così diverse, proprio come lo sono Emi e Rin."

"E Rin è la più diversa di tutte, diversa da chiunque altro io abbia incontrato."

hi "Già, immagino che lei sia una persona molto… unica."

"Ritorno a quella parola, come se comprendesse da sola la personalità di Rin, ma a dire il vero è solo un sostituto per una lunga descrizione delle sue bizzarrie."

show emi basic_closedhappy
with charaenter

"Emi ride al mio cercare una parola propriamente qualificante."

show emi basic_grin
with charaenter

emi "Lei è solo strana."

show emi excited_proud
with charaenter

emi "Sai, prima ha passato mezz' ora seduta sulla sua scatola."

emi "Fissando le dita dei suoi piedi."

show emi basic_closedhappy
with charaenter

"Ridacchia di nuovo in un modo che mi fa pensare che non sappia cosa c'è di divertente, ma che lo sia e basta."

show emi basic_grin
with charaenter

emi "Per tutto quel tempo."


stop ambient fadeout 2.0

scene bg school_dormext_half
with locationskip

play music music_rin fadein 2.0

"L' area di lavoro è un disastro, ma il murale vero e proprio ha invaso ancora più il muro dall' ultima volta che l' ho visto."

"Le figure umane sfigurate sono state colorate per la maggior parte in toni di rosso e rosa e arancione; strane, immaginarie… cose popolano gli spazi tra di loro."

"Sembra… bello. Non posso pensare a nessuna parola che descriverebbe l' opera concisamente e complessivamente così mi decido per un generico “bello”."

"Ma onestamente, sembra che l' area intorno al muro diventi più disordinata allo stesso ritmo con cui progredisce il murale."

"Il terreno è cosparso con dozzine di latte di pittura, vari materiali per arte e bottiglie di bibite vuote."

show rin negative_spaciness
with charaenter

"Rin è al centro di questo caos, sembrando molto comoda lì in piedi come se fosse una parte naturale della scena."

"Le gambe dei suoi pantaloni sono state arrotolate fino alle ginocchia, esponendo le sue gambe magre che mostrano uno spettro di pitture di guerra in essiccazione, simili a quelle sulla faccia di Emi."

show emi basic_grin at offscreenleft
with None

show rin negative_spaciness at tworight
show bg school_dormext_half at bgright
show emi basic_grin at twoleft
with charamove

"Emi sprinta fino a Rin prima di me e le salta gioiosamente di fronte."

show emi basic_closedhappy at twoleft
with charachange

emi "Sono tornata!"

show rin basic_awayabsent at tworight
with charachange

rin "Sei stata veloce. Hai di nuovo corso nei corridoi?"

show emi excited_proud at twoleft
with charachange

emi "Hisao mi ha aiutato."

show emi basic_grin at twoleft
with charachange

"Emi mi indica vittoriosamente."

show rin basic_absent at tworight
with charachange

"Rin si gira seguendo il dito di Emi coi suoi occhi, guardando nella mia direzione generale."

show rin basic_deadpannormal at tworight
with charachange

"China la testa verso di me con aria assente. Sembra che non abbia dormito la notte scorsa: sguardo vuoto e vitreo che è leggermente fuori fuoco rispetto alla mia posizione, e movimenti che sembrano provenire da un film al rallentatore."

rin "Salve, Hisao. Grazie per l' aiuto."

hi "Non c'è bisogno che mi ringrazi."

show rin basic_deadpan at tworight
with charachange

rin "Lo ho appena fatto."

hi "Non importa."

hi "Sembra che tu abbia fatto dei progressi. Sembra andar bene, per quanto ne capisco."

show rin basic_deadpannormal at tworight
with charachange

rin "Ma adesso hai ancora più sfortuna."

hi "Lo so, ma sono disposto a correre il rischio."

show rin basic_deadpandelight at tworight
with charachange

rin "Quella è una cosa molto carina da dire. Per me, ovviamente. Non per te."

show rin basic_awayabsent at tworight
with charachange

rin "E' per questo che gli artisti sono sempre sfortunati. Devono costantemente guardare i loro dipinti incompleti."

rin "Così gli artisti non possono trovare l' amore, o i loro programmi TV vengono cancellati e muoiono giovani a causa di malattie imprecisate. E' una profonda e misteriosa legge dell' universo."

show rin basic_lucid at tworight
with charachange

rin "A meno che non siano ciechi."

"Considera questo per un po', mentre sembra stare per crollare addormentata."

show rin basic_absent at tworight
with charachange

rin "C'è un ragazzo."

show rin basic_deadpannormal at tworight
with charachange

rin "Nel club d' arte, vedi. Ragazzo cieco. Così non può. Vedere."

hi "Me lo hai già detto."

show emi basic_hes at twoleft
with charachange

"Dò un' occhiata di sbieco a Emi e lei la restituisce in un modo che dice che anche lei ha già sentito questa storia."

"Nessuno dice niente a Rin però, così lei continua il suo monotono soliloquio come un comico che non fa ridere."

show rin basic_awayabsent at tworight
with charachange

rin "Dovrebbe diventare un artista. Niente sfortuna, garantito."

rin "Non credi che sarebbe una buona idea?"

show rin basic_lucid at tworight
with charachange

hi "Che solo i ciechi dovrebbero diventare artisti? No, non proprio."

"…"

show rin basic_deadpan at tworight
with charachange

rin "Potresti avere ragione."

show rin negative_spaciness at tworight
with charachange

"Abbandonando questo treno di pensieri, si gira di nuovo per contemplare il suo lavoro e comincia a mormorare un motivo che credo di riconoscere ma di cui non riesco a ricordare il nome."

show emi basic_closedgrin at twoleft
with charachange

"Emi aggiusta i materiali che abbiamo portato e muove alcune latte di pittura, cercando di portare un po' di organizzazione nella scena."

show rin basic_awayabsent at tworight
with charachange

rin "Emi, ho bisogno deIla pittura blu di Prussia."

show emi basic_confused at twoleft
with charachange

emi "Quale è il blu di Prussia…"

"Sta fissando confusa sette o otto latte, ciascuna contenente una diversa tonalità di blu."

show rin basic_deadpan at tworight
with charachange

rin "E' quella che contiene la pittura color blu di Prussia."

show emi basic_annoyed at twoleft
with charachange

emi "Oooh, Rin! Non sei affatto di aiuto!"

"Dò un' occhiata anche io, anche se nemmeno io so come sembri il blu di Prussia. Mi chiedo cosa il blu abbia a che vedere con la Prussia."

"…O addirittura cosa sia la Prussia. Il nome suona vagamente familiare, ma non riesco a ricordare."

"Mentre nessuno dei blu sembra più Prussiano degli altri, i caratteri in piccolo sulle etichette sono abbastanza leggibili per determinare che nessuna dice nulla riguardo la Prussianità dei contenuti."

hi "Non c'è del blu di Prussia qui."

stop music fadeout 2.0
#if on Emi's path jump there, Emi drags hisao off (she says "we have to go back" instead) and there is no choice, otherwise carry on



#********************

label it_A33:

scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None

"Emi tira un sospirone."

show emi basic_closedsweat at twoleft
with charachange

emi "Immagino di dover tornare indietro a prenderne."

show emi basic_grin at twoleft
with charachange

emi "Ho promesso di aiutare col progetto della nostra classe, però, così sarò di ritorno un po' più tardi. Puoi arrangiarti senza per alcune ore?"

show rin basic_deadpannormal at tworight
with charachange

"Rin annuisce, e così Emi se ne va."

hide emi
with charaexit

show rin basic_deadpannormal
show bg school_dormext_half
with charamove

"Io resto perchè mi piace guardare Rin dipingere e perchè non ho niente di meglio da fare."

play music music_dreamy fadein 1.0

"Mi siedo su una scatola e prendo il libro di oggi dalla mia borsa. E' una storia che parla di tre tizi che bevono birra per due settimane intere e fanno poco altro."

hide rin
with charaexit

"Rin si sposta dal punto che aveva bisogno del blu e comincia lentamente a lavorare su di un altro."

"Il suo piede muove con sicurezza il pennello lungo il muro intonacato. Strati di pittura su strati di pittura. Il murale lentamente guadagna più forma."

"Giro le pagine a un passo comodo. In questo capitolo stanno bevendo birra a casa dell' amico del protagonista. In quelli precedenti era l' appartamento del protagonista stesso."

"Non è il tipo di libro che ti fa girare pagina dopo pagina, una fetta della vita immaginaria di qualcuno che mi fa chiedere perchè ha dovuto essere scritta."

"Perchè, davvero. La ragione per fare qualcosa di creativo… è qualcosa di incomprensibile."

"Come il perchè Rin fa dei dipinti. Sembra che lei e Emi siano uguali, andando decisamente contro i loro fati come fosse per dispetto."

"Rin ha perfino detto qualcosa di simile. “Fare qualcosa che non puoi fare solo perchè puoi farlo”."

"E' questo che intendeva? E' la sua ragione? Per Emi potrebbe essere, lei dà l' impressione di essere una persona molto testarda."

"Rin non dà quell' impressione. Ripensandoci, lei non dà nessuna impressione, o una diversa ogni volta che parlo con lei."

"Perchè ha detto quello che ha detto? Perchè lei, o chiunque, dipinge, o disegna, o scolpisce, o scrive?"

"Non ho mai avuto un grosso impulso creativo così non penso di poterlo davvero capire."

"Mi fa sentire vuoto dentro."

"Che pensiero amaro. Non posso davvero decidere se sia vero o falso, tra l' altro."

"Sono contento di essere così? Non posso negare di sentirmi un pochino invidioso di Rin, ma non posso davvero considerarlo un difetto di nessun tipo."

"Io sono io e lei è lei."

"Però, ho bisogno di trovare qualcosa, qualcosa che potrebbe… farmi sentire un poco meno perso dentro me stesso, invece di annegarmi soltanto in questi libri come ho fatto in ospedale."

"Non posso fare a meno di sentirmi disorientato; la nuova scuola, vita e persone intorno a me contribuiscono pesantemente a questa sensazione."

"Sto facendo del mio meglio per adattarmi ai circoli sociali esistenti, e la maggior parte delle persone che ho incontrato sono state davvero gentili."

"Sembra comunque che sia un intruso, però; come se non fossi al mio posto."

stop music fadeout 5.0

"Mi riscuoto dalla sensazione, accorgendomi di stare sognando a occhi aperti. Non ho girato una sola pagina del libro, nè fatto nulla per Rin."

"Lei sta cercando di versare della pittura da una grossa latta usando solo i suoi piedi, senza preoccuparsi di chiedermi aiuto. O forse lo ha fatto e io non l' ho sentita."

"In ogni caso, sembra molto instabile."

scene bg mural_part
show rin basic_awayabsent_close at tworight
with locationchange

"Scatto rapidamente per aiutarla, dato che sembra stia per versare gli interi contenuti della latta sul lastricato."

"Prendo la latta dai suoi piedi e ne verso un po' nella ciotola."

show rin basic_absent_close at tworight
with charachange

"Lei non dice niente nè lo faccio io. Ho una breve visione dei suoi occhi, che mi guardano silenziosamente da sotto la sua frangia arruffata."

"E' un' espressione illeggibile, una perfetta faccia da poker, mista a un accenno di qualcosa che potrebbe essere leggera sorpresa."

"Mi chiedo cosa stia pensando. Forse si sta chiedendo che cosa io stia pensando. Forse nulla."

play music music_normal fadein 0.3

hi "Un soldino per i tuoi pensieri."

show rin basic_deadpan_close at tworight
with charachange

rin "Hai dei soldini con te?"

hi "Non credo di averne."

show rin basic_deadpancontemplation_close at tworight
with charachange

rin "Allora io non credo che te li dirò. Non sto pensando a nulla comunque, così sei fortunato. Eccetto che ora lo ho appena fatto."

"Fa una smorfia, sembrando molto insoddisfatta."

rin "E' difficile non pensare a nulla. Ma è importante."

"Sto per chiedere perchè è importante quando un tizio anziano si avvicina a noi, con l' aria di avere degli affari da sbrigare con Rin."

scene bg school_dormext_half at bgright
show nomiya smile
with locationchange

no_ "Buon pomeriggio. Come sta andando?"

show nomiya smile at twoleft
show bg school_dormext_half
with charamove

show rin basic_awayabsent at tworight
with charaenter

rin "Posso farcela."

"Rin non stacca gli occhi dal muro e risponde così naturalmente che posso solo assumere che si conoscano."

"Non ho mai visto quest' uomo prima così naturalmente mi chiedo chi possa essere. Forse un insegnante?"

"I suoi capelli sono sbiaditi in un grigio argenteo, a tal punto che sembra che siano stati tinti artificialmente. Spero che non sia così."

"Piccoli occhiali tondi pendono dalla cima del suo naso, ma sembra che stia costantemente guardando al di sopra di essi, invece che attraverso le lenti."

"Sta studiando intentamente il murale da sopra i suddetti occhiali."

show nomiya talk at twoleft
with charachange

no_ "Bene, bene."

no_ "Che composizione audace hai qui!"

"Si muove per ispezionare il murale più da vicino, parlandone tra sè e sè in una maniera che rende ovvio che vuole che anche noi lo sentiamo."

show nomiya veryhappy at twoleft
with charachange

no_ "Molto bene, davvero molto bene…"

"Non so davvero cosa pensare ma Rin non sembra preoccuparsene molto. Sta guardando intorno al suo spazio di lavoro, le varie ciotole di diversi toni sparse dappertutto."

show rin basic_deadpan at tworight
with charaenter

rin "Hisao."

hi "Hmm?"

show rin basic_deadpannormal at tworight
with charaenter

rin "Un altro po' di questo."

hi "Dammi un secondo."

"Verso una mistura 50-50 di due pitture nella ciotola per creare altro dello stesso tono rosa pallido che Rin stava usando per riempire la forma della faccia di un uomo."

"Rin mi guarda farlo, il che mi rende in qualche modo nervoso. Il suo viso è talmente neutrale che sembra stia solo aspettando che io faccia qualcosa di sbagliato."

"L' uomo si gira per guardarmi a sua volta, sembrando sorpreso come se avesse notato solo ora la mia presenza."

"…Forse è così."

show nomiya talk at twoleft
with charachange

no_ "Oh, salve. E tu chi potresti essere?"

hi "Ah, sono uno studente trasferito alla classe 3-3. Hisao Nakai. Piacere di conoscerla."

show nomiya smile at twoleft
with charachange

no_ "La classe di Mutou, eh? Bene, non te ne farò una colpa!"

play sound sfx_birdstakeoff

show nomiya veryhappy at twoleft
with vpunch

"Ride molto forte. Odiosamente forte. Alcuni piccoli uccelli prendono il volo da un albero vicino."

show nomiya talk at twoleft
with charachange

no_ "Sono Shinichi Nomiya, l' insegnante di belle arti."

"Così questo è l' insegnante d' arte. In retrospettiva, avrei dovuto immaginarlo. Perfino sembra esserlo, per quanto valgono le prime impressioni."

show nomiya smile at twoleft
with charachange

no "Come mai hai finito per aiutare la mia pupilla?"



label it_choiceA33:
menu:
    with menueffect

    "Vorrei saperlo anche io…"

    "Sono solo rimasto con lei, credo.":
        return m1

    "Mi interessa il club d' arte.":
        return m2

label it_A33a:

hi "Suppongo di essere un po' interessato al club d' arte."

"Me lo lascio sfuggire, in parte inavvertitamente."

show nomiya talk at twoleft
with charachange

no "Cosa vuoi dire?"

hi "Nulla di… specifico."

hi "Mi chiedo se potessi partecipare una volta o l' altra. Anche se è solo per osservare o qualcosa di simile."

hi "Stavo pensando che dovrei iscrivermi a un club o qualcosa del genere, così…."

"Non è in nessun modo una mossa premeditata, ma un vago senso di determinazione è davvero cresciuto in me per quest' ultima settimana."

"Voglio fare qualcosa. Voglio essere parte di qualcosa."

"Potrebbe anche essere il club d' arte, indipendentemente dai miei difetti."

"L' insegnante sembra compiaciuto."

show nomiya veryhappy at twoleft
with charachange

no "Oh? Vuoi iscriverti? Bene, nuovi membri sono sempre i benvenuti, certamente."

no "Gli incontri del club sono piuttosto normali. Studiamo vari aspetti delle belle arti e le proviamo anche con mano."

show nomiya smile at twoleft
with charachange

no "O piede."

"Tossisce imbarazzato ma Rin non sembra farci caso. Sono un minimo confortato dal fatto che non sono l' unico con difficoltà di vocabolario in questa scuola."

"Nomiya recupera dalla sua gaffe teatralmente controllando l' ora sul suo enorme, luccicante orologio da tasca, e si colpisce ancora più teatralmente sulla fronte."

show nomiya veryhappy at twoleft
with charachange

no "Ora devo veramente andare, ma sono sicuro che se hai delle domande, Tezuka può chiarirle."

"In qualche modo menzionare Rin e “chiarire” nella stessa frase non sembra sensato. Però, non lo dico all' insegnante, dato che pare andare di fretta."

show nomiya smile at twoleft
with charachange

no "Tezuka, mi fa piacere vedere che questo piccolo progetto sta andando così bene."

show nomiya talk at twoleft
with charachange

no "Mi sono solo fermato per ricordarti di non scappare via da sola domani. Ho invitato certe persone al festival per te, e sono sicuro che anche a loro piacerebbe incontrarti."

show nomiya smile at twoleft
with charachange

no "Inoltre, l' incontro del club di lunedì è disdetto, perchè devo andare fuori città. Immagino che voi ragazzi possiate fare qualcosa tra voi, se volete."

stop music fadeout 2.0

hide nomiya
with charaexit

show rin basic_deadpannormal
show bg school_dormext_half at bgleft
with charamove

"L' insegnante se ne va, e veniamo lasciati di nuovo soli. Rin sta ancora dipingendo come se non fosse accaduto niente di notevole. Dato che nulla infatti è successo, io rimango a chiedermi cosa diavolo c'è che non va in me."

"Io e l' arte non siamo andati d' accordo in passato, almeno a giudicare dai voti che ero solito ricevere alle medie inferiori."

"Forse un club sarebbe diverso da lezioni obbligatorie. Chi lo sa?"

"Cerco di trovare qualcosa di significativo da chiedere riguardo a esso, ma non mi viene in mente niente."

"Andrò solo a un incontro del club e vedrò come vanno le cose."

hi "Così ha invitato qualcuno domani solo perchè vedano il tuo dipinto?"

show rin basic_absent
with charachange

rin "Ha molti amici che trattano d' arte. Gli piace parlare d' arte."

show rin basic_awayabsent
with charachange

rin "Penso che voglia che io parli di arte con loro."

hi "In qualche modo ho l' impressione che tu non sia troppo eccitata all' idea."

"Rin scrolla le spalle senza sbilanciarsi, ma mi lascia comunque un' idea della sua generale insoddisfazione al pensiero di dovere discutere il suo dipinto, o qualunque dipinto, con altri."

show rin basic_deadpan
with charachange

rin "Non mi piace davvero parlare di arte. E' già un modo di parlare senza parlare, quindi perchè darsi la pena di parlarne?"

hi "Posso capirlo."

show rin basic_deadpannormal
with charachange

rin "E' come essere annoiati e parlare di essere annoiati perchè si è annoiati."

hi "Non ti seguo."

show rin negative_spaciness
with charachange

rin "Hai mai parlato di essere annoiato? E' senza senso e non molto eccitante. Tutto quello che puoi davvero dire è “sono così annoiato.” Una volta ho passato una settimana cercando di pensare a qualcosa di significativo da dire riguardo alla noia."

rin "E' stata la settimana più noiosa che abbia mai vissuto."

hi "Ma sembra piuttosto appropriato, non credi?"

show rin basic_deadpan
with charachange

"Rin mi lancia uno sguardo, del tipo laconico che sembra non significare nulla ma lo fa."

hi "Comunque… non so, immagino di trovare solo raramente qualcosa da dire sull' arte."

hi "Voglio dire, come questo che stai facendo ora. Non ho idea di cosa pensare su di esso, eccetto che sembra bello. Cosa significa questo dipinto?"

show rin basic_deadpannormal
with charachange

rin "Non significa proprio nulla."
 
"…"

show rin basic_deadpandelight
with charachange

rin "E' quello che mi piacerebbe dire. Così l' ho detto. "

show rin basic_deadpannormal
with charachange

rin "Ma quella era una piccola bugia. L' ho detta comunque perchè mi piacerebbe un po' che fosse vera."

rin "L' insegnante voleva che facessi questo, ma non avevo nessuna idea. Ho provato ad averne, ma non è successo nulla."

show rin negative_spaciness
with charachange

rin "Così adesso questo è un dipinto senza idee."

hi "Ma… allora cosa stai dipingendo?"

show rin basic_absent
with charachange

rin "Non ne ho idea."

show rin basic_delight
with charachange

rin "Ora che ci penso, credo che lo chiamerò “Non ne ho idea”."

show rin negative_worried
with charachange

rin "Ah, adesso ho ricominciato a pensare. Questo è male."

show rin basic_absent
with Dissolve(0.15)

show rin negative_worried
with Dissolve(0.1)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.1)

show rin basic_absent
with Dissolve(0.15)

show rin negative_worried
with Dissolve(0.5)

"Scuote vigorosamente la testa per un po', cercando di scuotere “pensare” via dalla sua testa. I capelli rosso-ambrati volano da tutte le parti."

show rin basic_deadpannormal
with charachange

rin "E' per questo che ho chiesto aiuto a Emi. Lei rende facile non pensare a nulla."

rin "Lo sai, come parla parla parla di nulla per ore intere. E' come se la sua testa fosse fatta di schiuma di gelatina da bagno al gusto di gomma da masticare."

show rin basic_deadpandelight
with charachange

rin "Tu sei un po' uguale, ma non proprio. Mi aiuta molto se resti qui."

"Non sono sicuro se quello è un complimento o no. Probabilmente non è nessuna delle due cose; essendo Rin la persona evidentemente neutra che è."

hi "Così c'è qualcosa di specifico che vorresti facessi per farti non pensare?"

show rin basic_deadpan
with charachange

rin "Basta che tu sia."

play music music_dreamy fadein 0.3

hide rin
with charaexit

"Quindi senza sapere cosa dovrei fare, mi siedo solo su una scatola vuota per guardarla continuare col dipinto, oziosamente sfogliando le pagine del libro sul bere birra."

scene bg mural_part
show rin negative_spaciness_close at tworight
with locationchange

"Rin ha un' espressione serena sul suo viso, i suoi occhi verdi scuri nascondono quello che potrebbe pensare dietro di essi. No aspetta, si suppone che non stia pensando nulla, giusto?"

"Mormora quietamente un motivo, interrompendosi di tanto in tanto per cortesemente richiedere altra pittura o un diverso tipo di pennello."

"La sua concentrazione è ammirevole, anche se sembra essere a corto di riposo e sotto pressione per finire il lavoro."

"Centimetro dopo centimetro il dipinto guadagna più forma, dettagli vengono aggiunti su dettagli, colori si intrecciano l' uno con l' altro, riempiendo gli spazi vuoti, crescendo gli uni sugli altri."

"Mi ritrovo di nuovo a pensare all' ispirazione e alla motivazione per creare dell' arte."

"Uno dove prende le idee? Non vengono dal nulla, e non penso che ci siano muse che magicamente iniettano dell' ispirazione nella tua testa."

"Le idee hanno un' origine e uno scopo."

"Più ci penso, più sono convinto che Rin stia mentendo sul suo murale, o almeno distorcendo la verità. Forse nemmeno lei si accorge di farlo."

"Non puoi fare nulla di creativo senza avere un' idea di quel che stai per creare. Quello andrebbe contro la definizione."

"Bisogna decidere che ogni linea venga tracciata. Anche se viene fatta a caso, allora anche quella è una decisione conscia."

"Così il suo dipingere, perfino questo, deve essere basato sull' avere qualche deliberato scopo o idea di cosa dipingere."

"Se l' idea di Rin è di non avere idee, come ha detto, quello conta come avere un' idea?"

"Un paradosso di logica? Quelli sembrano essere il modus operandi di Rin per la maggior parte delle normali interazioni, quindi non mi sorprenderebbe se non se ne fosse accorta nemmeno lei."

"Mi chiedo se dovrei menzionarlo, ma non sono sicuro di volermi ingaggiare in una discussione sulla logica con questa ragazza."

"Uno di noi finirebbe probabilmente per andare in cortocircuito in breve tempo, così abbandono l' idea."

show rin basic_awayabsent_close at tworight
with charachange

show rin negative_spaciness_close at tworight
with charachange

"Rin sta agitandosi e dimenandosi nervosamente."

show rin negative_annoyed_close at tworight
with charachange

show rin negative_spaciness_close at tworight
with charachange

"Persino il suo volto normalmente inespressivo occasionalmente assume espressioni dall' aria piuttosto complessa, del genere che uno non inventa accidentalmente."

show rin negative_annoyed_close at tworight
with charachange

hi "Va tutto bene?"

rin "Sì. No."

rin "La schiena mi fa di nuovo male."

rin "Questo dipinto è troppo grande, dopotutto, e è difficile da dipingere in questa posizione."
  
hi "Vuoi fare una pausa?"

show rin basic_deadpanupset_close at tworight
with charachange

rin "Dopo aver finito questa parte."

show rin negative_annoyed_close at tworight
with charachange

"Ma ovviamente, non fa una pausa, e io non menziono di nuovo l' argomento perchè sarebbe completamente e totalmente futile."

scene bg school_dormext_half_ss
with locationchange

"Rin continua il suo lavoro e io resto con lei: mi piace guardarla dipingere, e adesso diventerò un membro del suo stesso club."

scene bg school_dormext_full_ni
with Dissolve(3.0)

"Quando dichiara che il murale è finito, è già talmente buio che non ho idea su come faccia a saperlo."

"Non c'è celebrazione, nessun senso generale di un lavoro ben fatto, solo uno stanco e laconico “ho finito” e poi ce ne andiamo entrambi a dormire."

scene black
with Dissolve(3.0)


label it_A33b:

hi "Continuo a chiedermelo anche io. La mancanza di meglio da fare, probabilmente."

show nomiya veryhappy at twoleft
with charachange

"Emette una risata gioviale, poi controlla il suo orologio."

show nomiya smile at twoleft
with charachange

no "Ora devo veramente andare. Tezuka, mi fa piacere vedere che questo piccolo progetto sta andando così bene."

show nomiya talk at twoleft
with charachange

no "Mi sono solo fermato per ricordarti di non scappare via da sola domani. Ho invitato certe persone al festival per te, e sono sicuro che anche a loro piacerebbe incontrarti."

show nomiya smile at twoleft
with charachange

no "Inoltre, l' incontro del club di lunedì è disdetto, perchè devo andare fuori città. Immagino che voi ragazzi possiate fare qualcosa tra voi, se volete."

hide nomiya
with charaexit

show rin basic_deadpannormal
show bg school_dormext_half at bgleft
with charamove

"Se ne va, girandosi teatralmente, e camminando quanto più drammaticamente è possibile camminare."

"Che insegnante bizzarro."
  
hi "Me ne vado anche io. Ci vediamo in giro, Rin."

"Sollevando una mano, mi giro per salire le scale che vanno ai dormitori."

"Forse, se riesco a finire di leggere questi libri oggi, avrò tutto domani libero per il festival."

scene black
with Dissolve(3.0)

stop music fadeout 2.0



    #******************
 
label it_A34:

#Gotta go in and make some changes to E1 as a result of this scene, but it's pretty solid otherwise.

scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None

show emi basic_closedgrin at twoleft
with charachange

emi "Dobbiamo andare a prenderne dell' altra, allora."

"Apro bocca per dire che veramente non siamo entrambi richiesti per un compito così semplice come trovare un' altro barattolo di blu di Prussia, ma Emi ha già afferrato il mio braccio e ha cominciato a trascinarmi via."

hide emi
with charaexit

"Saluto Rin, che non sembra essersi nemmeno accorta che noi due ce ne stiamo andando."

play ambient sfx_crowd_outdoors fadein 0.5

scene bg school_courtyard
show crowd
with locationskip

"Bene, se ne accorgerà quando cercherà di nuovo il suo blu di Prussia e scoprirà che ancora non c'è."

stop ambient fadeout 0.2
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_lobby
show crowd
with locationskip

"Forse."

scene bg school_staircase2
with locationskip

"…"

scene bg school_hallway3
show crowd
with locationskip

"Probabilmente no, a dire il vero."

stop ambient fadeout 2.0

scene bg school_classroomart
with locationskip

"Mentre sono impegnato a pensare a quanto sia strana Rin, Emi mi sta trainando di nuovo verso l' aula d' arte."

"Comincio a sentirmi senza fiato."

hi "Perchè tutta questa premura?"

show emi basic_confused
with charaenter

emi "Eh?"

"Emi mi sta valutando con lo sguardo, come se stesse cercando di capire qualcosa."

hi "E' solo che sembri avere fretta."

hi "Non sono sicuro di poterti stare dietro."

"La comprensione appare sul suo viso."

play music music_normal fadein 0.3

show emi excited_proud
with charachange

emi "Non sarai senza fiato, vero?"

"C'è un divertimento quasi accusatorio nel suo tono."

"Sono tentato di negarlo, ma poi mi accorgo che sto ansimando da quando ci siamo fermati."

"Immagino che sia abbastanza ovvio."

hi "Un pò. Non tutti possono essere in forma, sai."

hi "A ognuno il suo, giusto?"

show emi basic_annoyed
with charachange

"Emi fa un cipiglio. Non è un cipiglio particolarmente buono."   

hi "Ehh, cioè…"

hi "Dovrei… tornare in forma?"

"Non che non avessi già deciso di provarci."

"Dopo quell' incidente sulla pista immagino che ci sia una vera necessità di cominciare a correre abitualmente in qualche modo."

"Dopo tutto, stavo sentendomi piuttosto bene prima di avere il mio falso allarme."

"Bè, veramente no. Ma era… divertente?"

"Nel frattempo, il mio commento sembra aver aiutato Emi a giungere a una sorta di decisione."

show emi basic_closedgrin
with charachange

emi "Bene, è deciso allora."

show emi basic_annoyed
with charachange

"Mi lancia uno sguardo serio."

emi "Ti unirai a me."

"…"

hi "Chiedo scusa?"

show emi basic_grin
with charachange

emi "Di mattina."

emi "Tu e io ora siamo compagni di corse."

show emi basic_closedhappy
with charachange

emi "Ho una routine già preparata. In effetti…"

stop music fadeout 1.0

play sound sfx_rustling

"Estrae un pezzo di carta stropicciato."

show emi excited_amused
with charachange

emi "L' ho proprio qui con me."

"Prendo il foglio di carta e gli dò un' occhiata."

"Tempi, date, e giri di pista, tutti scritti."

"Un lento incremento da solo alcuni giri al giorno fino a…"

"Mio Dio, si aspetta che io corra delle maratone?"

"E dove ha trovato il tempo per mettere insieme tutto questo?"

"E da quanto tempo lo sta preparando, poi?"

hi "Lo hai preparato tu questo?"

show emi sad_shy
with charachange

emi "Un po'."

show emi sad_grin
with charachange

emi "Ma è davvero un' idea dell' infermiere!"

show emi basic_closedgrin
with charachange

emi "Mi ha detto di tenerti d' occhio per assicurarsi che tu facessi esercizio come ti aveva detto!"



label it_A34a:

play music music_kenji fadein 0.3

"Una vasta cospirazione?"

"Forse Kenji ha indovinato qualcosa…"

hi "Questo sembra un po' molto solo per “tenermi d' occhio.”"

show emi sad_grin
with charachange

emi "Bè, per essere onesta sto cercando di trovare un compagno di corse per la mattina da un po' di tempo ormai."

"Mio Dio, Kenji! Se solo potessi vedere la macchinazione spiegarsi!"

hi "Per cosa hai bisogno di un compagno, poi?"

show emi basic_annoyed
with charachange

emi "E' più facile seguire un allenamento se non sei il solo che lo pratica."

emi "Non è ovvio?"

emi "E' meno probabile cedere se qualcun altro sta contando su di te perchè tu ci sia, giusto?"

hi "Vedo. E questo non solo ti motiverà a correre, ma assicurerà che anche io continui a correre."

hi "In modo che io obbedirò all' infermiere…"

show emi excited_proud
with charachange

emi "…e io ti terrò d' occhio proprio come lui mi ha chiesto!"

show emi basic_closedgrin
with charachange

emi "Hai capito in fretta, Hisao."

hi "E se mi rifiutassi?"

"Non ho intenzione di rifiutarmi, ovviamente."

"Ma devo dimostrare almeno una resistenza simbolica a un piano così magistralmente eseguito."

show emi basic_grin
with charachange

emi "Beh, se tu rifiutassi dovrei fare il broncio."

emi "E tu dovresti vivere col fatto di essere il tizio che ha fatto fare il broncio a Emi Ibarazaki."

show emi basic_closedgrin
with charachange

emi "Non vuoi una cosa del genere sulla tua coscienza, vero?"

show emi sad_depressed
with charachange

"Come per dimostrazione, Emi comincia a fare il broncio."

"E' la cosa più adorabile e strappacuore che abbia mai visto."

hi "Okay! Lo farò!"

hi "Solo… non fare così!"

hi "Mi sento come se avessi appena colpito un cagnolino!"

show emi basic_closedgrin
with charachange

emi "Così è deciso, giusto?"

emi "Sarai il mio compagno di corse?"

emi "Seguirai l' allenamento?"

emi "E la dieta?"

hi "Dieta?"

show emi basic_grin
with charachange

emi "Già, la dieta!"

show emi excited_proud
with charachange

emi "Devi mangiare sano se vuoi tornare in forma, sai!"

"Esamino attentamente la routine di allenamento."

hi "Non vedo nessuna dieta qui."

show emi basic_shock
with charachange

emi "Oh giusto! Ho dimenticato di dartela!"

play sound sfx_rustling

show emi excited_amused
with charachange

"Un altro foglio di carta sgualcito viene estratto e consegnato."

"E' leggermente meno dettagliato."

show emi excited_happy
with charachange

emi "Mi sono fatta aiutare dall' infermiere a comporla."

stop music fadeout 2.0

"La quantità di dedizione che l' infermiere dimostra nel tenermi in buona salute è piuttosto schiacciante."

"Non conosco molti infermieri scolastici che farebbero sì che uno dei loro studenti mi spii, men che meno aiuterebbero a creare una dieta."

"D' altra parte, immagino di non essere in una scuola normale."

"E forse quello non è poi così un male."

"D' altra parte, questa dieta sembra tagliare fuori praticamente tutto quello che sarà offerto al festival domani."

"Hmm."

hi "Così quando cominciamo a correre?"

show emi basic_grin
with charachange

emi "Dopo il festival."

hi "Subito dopo? E se avessi mangiato qualcosa lì? Potrebbe venirmi mal di stomaco, sai."

show emi basic_annoyed
with charachange

emi "Intendevo il giorno dopo il festival."

hi "Quello lo sapevo."

"Non dovevamo fare qualcosa?"

hi "Oh! Credo che dovremmo prendere quella pittura per Rin, eh?"

show emi basic_shock
with charachange

emi "Oh no! Mi è sfuggito di mente!"

scene bg school_dormext_half_ss
with shorttimeskip

"Una volta che abbiamo preso la pittura e siamo tornati al murale, Rin è già sparita."

"Oh bè."

"Emi e io decidiamo di separarci qui, lasciando la pittura a terra."

"Rin la troverà. Quando torna, se non altro."

scene bg school_dormhisao
with locationskip

"Il festival è domani. A dire il vero sono un po' ecccitato."

"Allo stesso tempo, la settimana mi ha lasciato piuttosto stanco, così leggo un po' e poi vado a letto."

scene black
with Dissolve(3.0)


label it_A34b:

# I'm not sound/music directing this scene now because I have no idea where this scene leads to… -yujovi
#this was written to allow an extra entry to bad end with a choice from this scene, but unused for now, possibly will never be used

"Dannazione, perchè tutta questa gente insiste nel farsi gli affari miei? Suppongo che all' infermiere sia concesso, persino richiesto ma…"

hi "Sai, non credo che sarebbe una buona idea."

hi "Questo è un problema mio, non voglio davvero coinvolgere nessun altro."

hi "Devo arrangiarmi da solo."

show emi sad_depressed
with charachange

emi "Sei arrabbiato per ieri?"

"Sta facendo il broncio, e assomiglia un poco a un cucciolo ferito. Non potrei essere arrabbiato ora, anche se volessi."

hi "No, non è quello. Al contrario, quella è stata colpa mia."

"Mi appoggio al muro, distogliendo lo sguardo da Emi."

hi "E' solo che… non so, sembra una cattiva idea."


    #********************

label it_A35:

scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None

"Ma perchè Lilly la lascerebbe da sola? Sembra essere molto al di fuori dell' ordinario, giudicando dalla reazione di Hanako."

"…"

"…Ah, giusto. Credo che Lilly abbia menzionato qualcosa riguardo ad andare in città oggi prima che Rin ci incontrasse."

"Il pensiero di quella passeggiata mi fa guardare fuori."

scene bg misc_sky at Fullpan(15.0)
with locationchange

"Il sole splendente e le occasionali persone che vagano intorno godendosi il pomeriggio mi fanno desiderare di uscire dalla scuola, o almeno fare qualcosa di diverso da sedere qui."

"Cedendo a uno dei miei peggiori vizi, la procrastinazione, decido che la storia è una materia meglio studiata di domenica. O di lunedì. O qualunque altro giorno eccetto questo."

"Grugnisco mentre mi sollevo dal mio posto, brevemente discutendo con me stesso sul passare o no del tempo con Kenji."

"Lui non mi sembra il tipo di persona da “godersi il bel tempo all' aperto con gli altri”, veramente. Suppongo che lo vedrò più tardi."

scene bg school_scienceroom at bgleft
with Dissolve(1.5)

"Cambiando rotta, considero brevemente l' idea di parlare con Hanako, ma quando guardo verso il suo posto, ormai è vuoto. Deve essersene andata in biblioteca."



label it_choiceA35:
menu:
    with menueffect

    "Ci deve essere qualcosa da fare per passare il tempo…"

    "Farò una passeggiata in città.":
        return m1

    "Andrò in biblioteca.":
        return m2

label it_A35a:

"Seguire Hanako fino in biblioteca sembra un po' intrusivo. C' era una ragione per cui ha lasciato l' aula, dopotutto."

"E a parte quello, voglio raggiungere Lilly. Almeno, mi piacerebbe ringraziarla per essersi presa cura di me a dispetto dei suoi altri, ovviamente gravosi, doveri."

"Credo che camminerò per la città. Con un po' di fortuna, dovrei riuscire a trovare Lilly. E inoltre, l' esercizio mi farà bene."

play music music_soothing fadein 0.3

scene bg school_courtyard
with locationskip

"Camminando attraverso il cortile scolastico fino al cancello, chino leggermente la testa verso un paio di compagni di classe di passaggio, e il gesto viene restituito."
    
"Anche da qui, si possono sentire le grida dei membri dei club di atletica. Giudicando dal puro volume del fracasso, la pista deve essere piena in questo momento."

"Mi ricordo che Lilly ieri aveva detto qualcosa riguardo essere stato buttato nel bel mezzo di un periodo impegnativo per la scuola."

"Mentre io sto cercando di orientarmi e recuperare gli studi persi, tutti gli altri stanno facendo normali attività scolastiche. La sensazione di essere uno straniero ancora non si è dissipata. Almeno, non del tutto."

"Beh, suppongo che non tutto vada male."

"Questa è una scuola privata, e lo si nota facilmente quando si cammina all' aperto. Non solo i terreni circostanti sono vastissimi, ma gli edifici stessi sono immacolati e davvero diversi dai blocchi di cemento a poco prezzo delle scuole pubbliche."

"C'è anche il fatto che c'è un senso di comunità molto più forte qui, o almeno un' atmosfera più amichevole. Alla mia vecchia scuola, era generalmente accettato che le persone sarebbero state nel proprio gruppetto e basta."

scene bg school_gate
with locationchange

"Alla fine raggiungo il cancello, e comincio la camminata giù per la strada e verso la città."

scene bg suburb_roadcenter
with shorttimeskip

"Bene, questo è stato discretamente produttivo."

"Avendo visto una buona porzione della città, incluse perfino le case arrampicate sulle colline intorno alla periferia, decido di fare una camminata nel parco prima di tornare indietro."

"Vivendo in città per tutta la mia vita, la totale mancanza di uomini d' affari benvestiti e ragazze vestite alla moda mi colpisce come incredibilmente inusuale."

"Tutto quel che c'è da vedere sono l' occasionale persona anziana che si trascina lungo il marciapiede e le coppie assortite di donne di mezza età impegnate a chiacchierare fuori dai piccoli negozi."

stop music fadeout 2.0

"Camminare lungo la strada per il parco presto mi distrae da loro, però, facendomi capire che forse mi sono spinto più lontano di quanto avrei dovuto per vedere quanto più potevo."

"Mentre il mio respiro inizia ad ansimare e il mio torace si stringe sempre di più, abbandono il prospetto di insistere."

scene bg suburb_park
with locationskip

"Dopo una rapida occhiata intorno al parco mentre entro, mi siedo su una vecchia panchina traballante che noto vicino a un paio di distributori automatici."

"Per diversi minuti mi siedo a capo chino, forzandomi a respirare profondamente. Mi sento più come un vecchio che come un adolescente che dovrebbe essere nel fiore della sua vita."

"Devo stare pagando per la permanenza in ospedale, le operazioni e i medicinali. Accidenti."

"Alla fine, la mia respirazione ritorna normale e i muscoli nel mio torace si rilassano, non senza una discreta quantità di sollievo. Immagino che questo indichi la fine del mio piccolo soggiorno però, in ogni caso."

scene bg suburb_shanghaiext
with locationchange

"C'è un caffè all' angolo più lontano, così mi fermerò lì per spegnere la mia sete prima di tornare indietro."

scene bg suburb_shanghaiint at bgright
with locationchange

play sound sfx_storebell

"Una campanella sopra la porta segnala il mio arrivo a un bancone vuoto."

"Per alcuni momenti resto lì ad aspettare, scorrendo i miei occhi di tanto in tanto da un capo all' altro del bancone alla ricerca di un campanello per chiamare il servizio."

show yuuko neutral_shang
with charaenter

"Finalmente una porta dietro il bancone si apre, e la persona che ne emerge mi prende completamente di sorpresa."

play music music_another fadein 0.3

hi "Yu… Yuuko?"

hi "Ciao, non avevo idea che lavorassi qui."

"Non ho davvero neanche idea di come chiamarla, dato che tecnicamente è staff scolastico oltre ad essere, apparentemente, una cameriera."

show yuuko neurotic_shang
with charaenter

yu "Ah, sì, um…"

"Cammina rapida fino al bancone, prima di scagliarsi col suo busto verso il basso in un inchino eccessivamente profondo."

show yuuko happy_shang
with charaenter

yu "Benvenuto allo Shanghai! Posso prendere il suo ordine?"

"Dritti agli affari, vedo."

hi "Non so… bè, un caffè, per favore?"

show yuuko neutral_shang
with charaenter

yu "Sì, certamente. Glie lo preparo subito e glie lo porterò appena pronto."

hi "Uh, grazie."

"La formalità di Yuuko mi prende in contropiede. Sembra prendere il suo lavoro molto seriamente."

hide yuuko
with charaexit

"Obbedendo alle sue istruzioni, mi giro e dò una rapida occhiata intorno in cerca di un tavolo libero. Considerando che il caffè sembra essere vuoto, questo è un compito facile da concludere."

show bg suburb_shanghaiint at bgleft
with charamove

"Mentre cammino verso un tavolo adiacente alla finestra, noto un lampo di giallo da intorno a uno dei divisori delle tavole."

show lilly basic_smileclosed at twoleft
show akira basic_lost at tworight
with charaenter

"E infatti, basta uno sguardo per accertarmi che una certa Satou è al tavolo. Questo detto, non riconosco la figura in giacca e cravatta seduta di fronte a lei."

"Biondo, dalla pelle chiara e solo un poco più basso, lui… lei? Lei, credo, deve essere una sua parente."

"Dato che i due sono praticamente silenziosi mentre la figura in giacca sta bevendo da una tazzina di caffè, decido di salutare Lilly. Parte del motivo per cui sono qui era cercare di incontrarla, dopotutto."

hi "Ciao, Lilly."

show lilly basic_smile at twoleft
with charachange

li "…Hisao?"

hi "Già. Piacere di rivederti."

show akira basic_smile at tworight
with charachange

"La ragazza in giacca alza lo sguardo, notando la mia uniforme con un sorriso rilassato."

aki_ "Vi conoscete?"

hi "Direi… di sì."

"E' la più valida approssimazione della nostra relazione a cui possa pensare."

show lilly basic_smileclosed at twoleft
with charachange

li "Hmm… vuoi accomodarti?"

"Lo dice all' aria vicino a me, ma il messaggio è chiaro quanto basta e mi metto a sedere accanto a lei."

show lilly basic_weaksmile at twoleft
with charachange

li "Immagino che alcune presentazioni siano necessarie."

show lilly basic_smile at twoleft
with charachange

li "Hisao, questa è Akira Satou, mia sorella maggiore. Akira, questo è Hisao Nakai, uno studente di Yamaku."

"Sembra che la mia supposizione fosse giusta. L' appena presentata Akira fa un cenno di saluto, che restituisco."

"Quello che non restituisco però, è lo sguardo quasi analitico con cui mi esamina."

show lilly basic_smile at left
show akira basic_smile at right
with charamove

show yuuko neutral_shang
with charaenter

"Mentre lei sta facendo questo, Yuuko arriva al tavolo e piazza attentamente il mio caffè su di esso prima di inchinarsi e ritirarsi."

hide yuuko
with charaexit

show lilly basic_smile at twoleft
show akira basic_smile at tworight
with charamove

"Portando cautamente la mia mano sul lato della tazzina, scopro che è già proprio alla temperatura giusta per berlo. Dopo aver bevuto un sorso, il sapore risulta essere tanto buono quanto la temperatura."

"Yuuko sembra essere molto più abile con questo che a fare la bibliotecaria."

"Bevo un ottimo, lungo sorso prima di rilassarmi a sedere."

"Ci vogliono pochi secondi perchè l' esame di Akira giunga a un termine. Apparentemente annoiandosi rapidamente dell' attività, si rivolge a sua sorella."

show akira basic_boo at tworight
with charachange

aki "Così, come va la scuola ultimamente?"

"Sembra che Akira non si preoccupi del fatto che qualcuno che non conosce affatto possa sentire tutto quello che si dicono."

"Non che io mi lamenti. Lasciandole chiacchierare, mi metto comodo e continuo a bere l' aromatico caffè."

show lilly basic_smileclosed at twoleft
show akira basic_smile at tworight
with shorttimeskip

aki "Sembra che tu sia piuttosto impegnata, allora."

show lilly basic_smile at twoleft
with charachange

li "Almeno non sto più cucinando da mangiare per te dopo la scuola."

"Mentre parlano, lentamente mi accorgo di essere completamente incapace di percepire le emozioni di Lilly attraverso i suoi occhi; come potrei con chiunque altro."

"Diventa leggermente inquietante mentre subconsciamente mi concentro su questo fatto."

show akira basic_lost at tworight
with charachange

aki "Woah, quanto sei fredda. Non stavi solo cucinando per te comunque? Io mangiavo solo gli avanzi."

show lilly basic_displeased at twoleft
with charachange

li "Non è quello il punto… stai almeno riuscendo a nutrirti?"

show akira basic_resigned at tworight
with charachange

aki "Posso cucinare senza farmi esplodere, sai."

show akira basic_annoyed at tworight
with charachange

aki "Di solito."

show lilly basic_listen at twoleft
with charachange

li "Quello è…"

show akira basic_laugh at tworight
with charachange

aki "Hahaha! Va bene, va bene. Dovevo comunque imparare prima o poi."

show lilly basic_listen at left
show akira basic_laugh at right
with charamove

show yuuko neurotic_shang
with charaenter

yu "Ah, Lilly?"

show lilly basic_smile at left
show akira basic_boo at right
with charachange

"Tutti i presenti vengono temporaneamente distratti da Yuuko che piazza sul tavolo una tazza di tè per Lilly."

hide yuuko
with charaexit

show lilly basic_smile at twoleft
show akira basic_boo at tworight
with charamove

"Cogliendo l' occasione per guardare il suo orologio, Akira si solleva dal suo posto e china brevemente la testa verso di me."

show akira basic_smile at tworight
with charachange

aki "Bene, farò meglio ad andare. E' stato bello parlare con te, Lilly."

show lilly basic_oops at twoleft
with charachange

li "Akira, devi proprio…"

"Lilly sembra veramente intristita dall' improvvisa partenza di sua sorella. Sembra che possa avere ricevuto l' impressione sbagliata."

show akira basic_resigned at tworight
with charachange

aki "Scusa, devo tornare al lavoro. Mi staranno di nuovo addosso se non mi sbrigo a tornare."

"Così informale… la sua apparenza ben vestita e ordinata davvero darebbe a chiunque l' impressione sbagliata su di lei."

show lilly basic_concerned at twoleft
with charachange

li "Ciao, Akira…"

show akira basic_smile at tworight
with charachange

aki "Dai, non sembrare così giù. Sarò in giro di nuovo presto. Ci vediamo."

hide akira
with charaexit

"Con quello, se ne va dallo Shanghai tenendo alta una mano."

stop music fadeout 2.0

"Lilly sembra ancora piuttosto depressa, così provo a fare conversazione in un tentativo di distrarla."

show lilly basic_concerned
show bg suburb_shanghaiint
with charamove

hi "Sembra una brava persona."

show lilly basic_displeased
with charachange

li "Una volta vivevamo insieme, ma adesso che vivo a scuola quasi non ci vediamo più."

"Anche se Lilly è sempre stata molto affabile, non so ancora davvero molto di lei. In retrospetto, è sorprendente quante informazioni sia riuscita a strapparmi, davvero."

hi "Vivevate insieme? Da qualche parte qui vicino?"

li "Era piuttosto distante a sud, così il viaggio fino a Yamaku era abbastanza lungo."

show lilly basic_reminisce
with charachange

li "Con lei che lavorava sempre più ore e Yamaku così distante, alla fine non c'è stata molta altra scelta se non trasferirmi nei dormitori."

"Bene, quello spiega le chiacchiere sul cucinare. Evidentemente riguadagnando la padronanza di sè, Lilly ridiventa vivace… almeno un poco."

show lilly basic_weaksmile
with charachange

li "Immagino che ora tu sia più riposato?"

hi "Scusa?"

show lilly basic_smileclosed
with charachange

li "Suoni meno esausto di quanto eri quando sei entrato."

"Essere capace di sentire il mio respiro in quel modo… deve avere delle ottime orecchie."

hi "Già. Ho finito per camminare per tutta la città dopo aver pensato di fare una piccola passeggiata."

"Ricordandomi della mia sete dopo la camminata, mi chino in avanti e bevo un sorsetto dalla tazza."

"Senza altro indugio, Lilly comincia la sua profumata tazza di tè."

"Immagino che sia meglio che torni a Yamaku. Posso rimandare lo studio solo fino a un certo punto, e voglio avere una buona notte di sonno prima del festival."

"Alzandomi dal mio posto, prendo la tazza macchiata di caffè dal tavolo."

show lilly basic_surprised
with charachange

li "Te ne stai andando?"

hi "Già. Anche tu stai tornando indietro? Sta facendosi un po' tardi."

"Per un momento fa una pausa, prima di alzare di nuovo la testa dalla sua tazza come se mi stesse guardando."

play music music_dreamy fadein 0.3

show lilly basic_smile
with charachange

li "Yuuko, potremmo avere un altro caffè, per favore?"

yu "Okay, lo porto subito!"

hi "Quello… non è stato subdolo."

show lilly basic_giggle
with charachange

"Si lascia sfuggire un breve risatina alla mia franca valutazione della sua manovra. E' sorprendentemente infantile e spensierata, data la sua apparenza altrimenti composta."

"Alla fine, però, ho poca ragione di rifiutare. Per essere onesto mi è difficile dire di no, tutto considerato."

"Con un finto sospiro di esasperazione, mi siedo di fronte a lei."

hi "Vuoi un po' di compagnia, allora?"

show lilly basic_cheerful
with charachange

li "Hmm… direi più che mi stavo chiedendo…"

"Vedo che è nuovamente in modalità inquisitoria. Sembra essere stranamente interessata, o almeno curiosa, riguardo a me."

show lilly basic_smile
with charachange

li "Hai dei fratelli o sorelle?"

"Non una tangente inaspettata."

hi "No, sono figlio unico. Per essere onesto, l' idea di essere così vicino a qualcuno mi rende un poco invidioso."

show lilly basic_smileclosed
with charachange

li "Interessante…"

"Inarco un sopracciglio, ma ovviamente non vengo notato. Il breve silenzio comunica a dovere la domanda."

show lilly basic_smile
with charachange

li "E' solo che altri mi hanno detto la stessa cosa."

li "E' un argomento su cui mi è difficile pensare e parlare obiettivamente, dato che ho sempre avuto qualcuno come lei."

"Credo di poter capire quello che intende Lilly, dato che sarebbe difficile rimuoversi da una situazione in cui si è stati per tutta la propria vita."

"Lei e sua sorella devono avere avuto un legame piuttosto stretto."

"Facendo sforzi per interromperci quanto meno possibile, Yuuko viene da noi e scrupolosamente piazza due tazzine sul tavolo."

"Lilly la ringrazia mentre io mi rilasso, osservando questa esasperante ragazza di fronte a me."

"A dispetto di sembrare sempre in guardia e in controllo di sè stessa quando parla con gli altri, ha una curiosità quasi infantile riguardo le persone."

"Questo detto, i rari momenti in cui sembra abbassare leggermente la guardia sono quelli che concedono più comprensione di come pensa."

"Prendendo la mia bevanda, capisco qualcosa che probabilmente avrei dovuto notare prima."

"…Credo di cominciare a essere un po' incuriosito a mia volta da lei."

stop music fadeout 2.0

scene bg school_gate_ni
with shorttimeskip

play ambient sfx_cicadas fadein 0.3

"Nonostante aver tenuto un buon passo, è già il tramonto quando raggiungo il grande cancello di ferro di fronte alla scuola."

"Mentre è bello avere molto tempo a disposizione per vagare in giro in virtù del vivere accanto alla scuola, non posso fare a meno di avere la sensazione che ben pochi studenti sfruttino davvero l' opportunità."

scene bg school_courtyard_ni
with locationchange

"Paragonato al numero di studenti che vedo girare qua e là per il campus durante il tempo libero, è sorprendentemente raro vedere qualcuno in città."

"Immagino, dato il gran numero di servizi offerti dalla scuola, che molti semplicemente non possano vedere alcun motivo per avventurarsi fuori, per non parlare di persone quali Hanako e Kenji."

"Fa sì che mi domandi se persone come Shizune, Misha e Lilly sono l' eccezione per questa scuola, piuttosto che la regola."

stop ambient fadeout 1.0
scene bg school_dormhallway
with locationskip

"Mentre torno verso la mia stanza, continuo a paragonare la mia vecchia scuola con Yamaku. Mentre lo faccio, comincio a sorprendermi di essere riuscito ad abituarmi anche solo fino a questo punto a tutto quel che mi è successo."

scene black
with Dissolve(3.0)


#***********
    
label it_A36:

play sound sfx_doorknock

scene bg school_dormhisao
with openeye

"Alle otto e cinque minuti, un martellare incredibilmente rumoroso mi sveglia di soprassalto. Sta venendo da fuori della mia porta."

scene bg school_dormhallway
show shizu behind_blank at tworight
show misha hips_smile at twoleft
with locationchange

play music music_comedy fadein 0.3

"Rapidamente, apro la porta per trovare Shizune e Misha fianco a fianco di fronte a me. Entrambe sembrano un po' stanche, anche se è più evidente su Misha."

hi "Chi di voi due ha bussato?"

"Lo chiedo, echeggiando la domanda che deve essere nella mente di tutti nell' intero edificio."

show misha hips_grin at twoleft
with charachange

mi "Ahahaha, quello non importa, Hicchan!"

"Ignora la domanda immediatamente senza neanche batter ciglio."

show misha hips_smile at twoleft
with charachange

mi "Oh? Sei ancora in pigiama, Hicchan? Così non ti svegli alle otto?"

"Noto che i suoi capelli sono umidi. I suoi boccoli stanno a malapena tenendo la loro forma."

hi "No, pensavo di dormire un po' di più dato che è il weekend e così via, e che ho perso una gran quantità di sonno questa settimana."

"Mi chiedo se si è accorta del veleno nelle mie parole."

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Allora è un' ottima cosa che siamo venute a svegliarti!"

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Comunque, Hicchan, immagino che vorresti sapere perchè siamo qui, non è vero?"

"Non è difficile da indovinare, ma vorrei che non dicesse le parole che sta per dire."

show misha perky_smile at twoleft
with charachange

mi "Ti andrebbe di marinare le lezioni e andare da qualche parte di bello con noi?"

hi "Puoi ripetere?"

show misha hips_smile at twoleft
with charachange

mi "Ti va di marinare le lezioni per fare qualcosa di divertente?"

"Ero certo che mi avrebbero forzato ad aiutarle di nuovo con qualche lavoro da schiavo."

hi "Sul serio?"

show misha hips_grin at twoleft
with charachange

"Misha sogghigna e annuisce con entusiasmo."

"Mi piace questo nuovo approccio che stanno prendendo anche se sono un poco sorpreso che suggeriscano di marinare le lezioni, pur considerando che abbiamo solo mezza giornata dato che è sabato." 

hi "Voi due non siete preoccupate di perdervi costantemente le lezioni?"

show shizu behind_smile at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Bè, non sembra essere un problema! Hicchan, questa scuola praticamente si ferma ogni volta che arriva questo periodo dell' anno."

show misha hips_smile at twoleft
with charachange

mi "Tra l' altro, è sabato~. Non ti va di fare qualcosa di divertente?"

"Sono stupito da quanto sembra gli importi poco."

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Non che vogliamo fare pressione perchè tu ci conceda la tua compagnia, ma pensavamo che ti sarebbe piaciuto stare un po' insieme a noi!"

show shizu behind_blank at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Così… ti piacerebbe unirti a noi? Dai, ti divertirai molto di più che standotene seduto lì con la testa sulla tua scrivania~!"

"Suppongo che non mi perderò niente di importante, nè che mancherò a qualcuno."

hi "Va bene, allora, non penso che mi perderò molto. Cosa avete in mente?"

"I miei occhi si stringono in sospetto quando un pensiero attraversa la mia mente."

hi "Un momento… questo non è solo un qualche trucco per farmi fare dell' altra roba per il consiglio studentesco, vero?"

show shizu basic_angry at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "No, certo che no!"

show misha hips_frown at twoleft
with charachange

mi "E supporre a quel modo una cosa del genere è veramente cattivo, Hicchan."

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "…E comunque, sei nel consiglio studentesco adesso, ricordi?"

show misha hips_grin at twoleft
with charachange

mi "Se volessimo farti fare qualcosa per noi, non avremmo bisogno di ingannarti~!" 

show misha hips_laugh at twoleft
with charachange

mi "Hahaha!"

show misha hips_smile at twoleft
with charachange

"Questo tipo di coercizione mi è nuovo. Solo due belle ragazze sarebbero in grado di riuscire a usarlo."

"Mi permetto di rilassarmi un poco. Forse sono troppo paranoico, sembra che davvero possano solo volere passare un po' di tempo insieme."

"Ciononostante…"

stop music fadeout 1.0

hi "Niente trucchi?"

play music music_shizune fadein 0.5

show shizu basic_angry at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Niente trucchi! Smettila di essere così paranoico!"

hi "Bè, se lo dite voi."

"Improvvisamente, ricordo di essere ancora in pigiama."

hi "Mi chiedo se lascereste che mi vestissi prima?"

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Eh? Perchè, Hicchan? Stai benissimo così!"

hi "Preferirei comunque indossare qualcos' altro."

scene bg school_dormhisao
with locationchange

"Chiudo la porta prima che abbia una possibilità di rispondere e mi infilo in fretta la mia uniforme."

scene bg school_dormhallway
show misha perky_smile at twoleft
show shizu basic_normal at tworight
with locationchange

"Ritornando al corridoio, vedo che Shizune e Misha sono impegnate in una animata discussione."

"Mi chiedo se alle persone che discutono in segni capiti mai di ficcarsi accidentalmente le dita negli occhi l' un con l' altro."

show shizu behind_frown_close at tworight
with characlose

"Mentre sto considerando questo, Shizune mi dà impazientemente un colpetto sulla spalla."

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Così, abbiamo in programma di sparire in città! Ricordi quella sala da tè dove ci siamo incontrati mercoledì?"

hi "Sala da tè?" 

show shizu behind_frustrated_close at tworight
with characlose

shi "…"

show misha perky_confused at twoleft
with charachange

mi "Non ti ricordi?"

hi "Oh, quel caffé."

show misha hips_smile at twoleft
with charachange

mi "Sala da tè! Si chiama Shanghai. La Cina è il luogo di nascita del tè, sai. Forza, Hicchan! Offrirò persino io oggi!"

show misha hips_grin at twoleft
with charachange

mi "Ah… non io, non io, voglio dire Shicchan! Ahaha~!"

hi "Non so…"

show misha sign_smile at twoleft
with charachange

mi "E' carino, è veramente rilassante! E' come… metà caffé, metà ristorante, metà sofisticato, metà… biblioteca…"

"Cosa?"

hi "Quelle sono un sacco di metà."

"Ma Misha non sembra accorgersi del mio commento." 

show misha hips_smile at twoleft
with charachange

mi "Così~! Dai, non capita spesso che abbiamo così tanto tempo libero!"

show shizu adjust_smug_close at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Se sei occupato, però, non sei obbligato! Non è che la tua presenza sia assolutamente, assolutamente richiesta!"

show misha cross_laugh at twoleft
with charachange

mi "Hahahaha!"

show misha cross_grin at twoleft
with charachange

"Non ho mai visto in vita mia un tentativo di psicologia inversa peggio mascherato. Mi sento un po' stanco oggi, e i miei insegnanti in classe potrebbero voler scoprire dove sono finito. Forse."

"D' altra parte, non sono veramente stato in città da quando sono arrivato qui, così questa è una buona ragione per dirigersi lì."

"E poi, qualcosa da mangiare mi andrebbe a genio. Se offre Shizune, meglio ancora; sono completamente al verde."

hi "Va bene, andiamo. Fate strada."

show misha hips_smile at twoleft
show shizu behind_smile_close at tworight
with charachange

mi "Grande~!"

stop music fadeout 2.0

scene bg suburb_shanghaiint
with shorttimeskip

play music music_tranquil fadein 0.3

"Arriviamo alla sala da tè dopo una mezz' ora di camminata. Sembra che siamo gli unici clienti al momento."

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

hi "E' sempre così tranquillo di mattina?"

"Con quello, voglio dire se è sempre così vuoto."
    
show shizu basic_normal at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "No, è piuttosto strano. Ehi, non è un male però, giusto?"

hi "Hai ragione."

scene ev shizu_shanghai
with locationchange

"Ci sediamo a una grande tavola rotonda di marmo, e mi accorgo di non sapere che cosa servono qui. L' ultima volta ho solo seguito la raccomandazione di Yuuko."

hi "Ehi, c'è un menù o qualcosa del genere?"

scene ev shizu_shanghai_normallaugh
with charachange

mi "No!"

"Quella risposta era stranamente piena di soddisfazione."

scene ev shizu_shanghai_smirklaugh
with charachange

shi "…"

scene ev shizu_shanghai_smirknormal
with charachange

mi "Così, Hicchan, hai deciso cosa vuoi ordinare?"

scene bg suburb_shanghaiint at Fullpan(8.0)
with locationchange

"Guardo in giro per il negozio e non riesco a vedere nulla che assomigli a un menù."

"Non capisco, come sarebbe a dire? Cos' è questo posto?"

"E' una qualche specie di negozio segreto? Normalmente ci si può entrare solo con una stretta di mano segreta? Una qualche sorta di segnale?"

"Bisogna che qualcuno ti presenti? Giurare un patto di sague? Dannazione, non era affatto così l' altra volta."

scene ev shizu_shanghai
with locationchange

hi "Non saprei, l' altra volta credo di avere solo preso un caffè? Cosa servono qui?"

scene ev shizu_shanghai_smirknormal
with charachange

shi "…"

scene ev shizu_shanghai_smirklaugh
with charachange

mi "Tè!"

hi "Ah, bene, allora…"

hi "Non solo tè, giusto? Non esclusivamente tè? Ci sono anche altre cose, giusto?"

scene ev shizu_shanghai_normallaugh
with charachange

shi "…"

scene ev shizu_shanghai
with locationchange

mi "Chiaramente~!"

hi "Chiaramente? Tipo cosa? Non c'è nessun menù qui. Dove sono i menù?"

"Stanno giocandomi un altro scherzo. Non c'è modo di uscirne; tutto quel che posso fare è prepararmi per l' inevitabile figuraccia in arrivo."

"Quasi vorrei uscire dal negozio, ma mi sono già seduto."

"Sarebbe scorretto andarmene ora; le regole non scritte di educata condotta sociale bloccano la mia uscita come un muro di fiamme."

"Decido di stare sul sicuro. Ordinerò quello che ordinano loro, se è accettabile e sufficientemente maschile."

hi "Perchè non ordinate prima voi? Prima le signore."

scene ev shizu_shanghai_smirknormal
with charachange

shi "…"

mi "Bella mossa, Hicchan, ma~ abbiamo già ordinato!"

hi "Come è possibile? Quando? Come? Da chi?"

mi "Siamo clienti abituali, veniamo qui così spesso che non ce n'è più bisogno!"

scene ev shizu_shanghai
with charachange

shi "…"

mi "Bè, credo che tu ne abbia avuto abbastanza. Siamo sedute sui menù, ovviamente!"

scene ev shizu_shanghai_normallaugh
with charachange

mi "Hahaha!"

"Guardo gli altri tavoli intorno a me. Su nessuno c'è un menù. Questo vuol dire che devono tenerli in una grossa pila vicino alla porta o qualcosa di simile. Che razza di cosa su cui sedersi, e che velocità per afferrarli così in fretta."

hi "Bè, non importa. Posso averne uno, allora?"

scene ev shizu_shanghai_smirklaugh
with charachange

shi "…"

scene ev shizu_shanghai_smirknormal
with charachange

mi "Ne puoi prendere uno se vuoi, ma tu non sei il tipo di persona che farebbe qualcosa di così la—sci—vo?, non è vero?"

"Dico loro che prenderò solo un caffè e appoggio la testa sulla fresca superficie del tavolo."

scene ev shizu_shanghai_borednormal
with charachange

shi "…"

scene ev shizu_shanghai_boredlaugh
with charachange

mi "Caffè? Questo è un luogo di estremamente alta classe, e tu vuoi ordinare caffè?"

"E' chiaro che stanno di nuovo prendendomi in giro."

hi "In tal caso, prenderò quello che prendete voi."

scene ev shizu_shanghai_smirklaugh
with charachange

shi "…"

scene ev shizu_shanghai_smirknormal
with charachange

mi "Hicchan, Shicchan beve un tè speciale che viene coltivato solo in zone remote dell' India."

mi "Il tè viene ancora fatto a mano da una tribù di coltivatori di tè che hanno trasmesso i metodi in eredità nelle loro famiglie per generazioni."

mi "Devono guadare delle acque infestate da alligatori una volta all' anno per ottenere le foglie di tè. A ogni viaggio, alcuni non ritornano vivi."

"Non posso bere qualcosa del genere, mi sentirei troppo in colpa."

hi "Allora prenderò quello che prendi tu."

scene ev shizu_shanghai_smirklaugh
with charachange

mi "Io non so cosa sto per bere."

"Come?"

hi "E va bene, allora voglio il tè per cui sono morte delle persone."

hi "No, come non detto. Prenderò un caffè."

hi "Se questo è un luogo di estremamente alta classe, allora dovrebbero avere del caffè di estremamente alta classe, giusto? … Nessuno è morto per quello, giusto?"

scene ev shizu_shanghai
with charachange

"La risposta perfetta, non c'è modo per loro di controbatterla. Shizune si stringe nelle spalle, come per dire “bella mossa.”"

"Non hanno ancora risposto alla mia seconda domanda."

scene bg suburb_shanghaiint
with locationchange

show yuuko neutral_shang
with charaenter

"Misha chiama Yuuko, che ci porta le nostre bevande e un singolo incredibilmente minuscolo dolce giallo con una piccola forchetta di plastica nera infilzata in esso per ciascuno di noi."

hide yuuko
with charaexit

"Mangio il mio dolce in un boccone, stupito da come è probabilmente la cosa meno soddisfacente che io abbia mai mangiato."

show shizu behind_blank at Slide(0.2,0.5,0.3,0.5,1.0)
show misha perky_smile_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

mi "Hicchan, hai qualche piano per domani?"

"Misha inghiotte un sorso del suo tè, qualcosa che suona sospettosamente di alta classe anche se sembra comune tè."

"Lo beve con incredibile noncuranza considerando quanto è caldo. L' esatto opposto di Shizune o Lilly."

"Piani? Suona minaccioso."

hi "Piani? Sì."

hi "Sì, sono incredibilmente occupato domani. Infatti, ho talmente tanto da fare che non avrò affatto del tempo libero a disposizione."
#why is he still trying to escape the girls? I don't get it -aura

hi "Proprio così… non un minuto libero. E tutto quel che devo fare è estremamente importante. Molto, molto importante."

show misha hips_grin_close at tworight
with charachange

"Misha ridacchia, chiaramente non credendomi, e poi segna il tutto a Shizune, che annuisce lentamente e deliberatamente sembrando ben poco divertita."

show shizu basic_normal_close at twoleft
with characlose

"Improvvisamente, si china in avanti, fissando analiticamente la mia faccia come una macchina della verità umana, aspettando che il minimo indizio mi tradisca."

"Dopo almeno un minuto di questo, torna a sedersi e beve un sorso di tè."

show shizu behind_blank at twoleft
with charadistant

shi "…"

show misha perky_smile_close at tworight
with charachange

mi "Okay, Hicchan, se sei così occupato. Non abbiamo niente da fare domani, così pensavamo che forse ti sarebbe piaciuto farci compagnia al festival!"

show misha sign_smile_close at tworight
with charachange

mi "Tu sei nuovo qui, comunque, giusto? Giusto? Così~ avevamo pensato che ti avremmo fatto da guide e ci saremmo divertiti un po' insieme, ma se sei così impegnato, lo capiamo!"

show shizu adjust_happy at twoleft
with charachange

shi "…"

mi "Peccato, peccato!"

show misha cross_grin_close at tworight
show shizu basic_normal2 at twoleft
with charachange

"Entrambe si stringono nelle spalle in perfetta sincronia, come se avessero fatto delle prove prima."

show misha cross_laugh_close at tworight
with charachange

mi "Ahahahahaha~!"

show misha cross_grin_close at tworight
with charachange

mi "Hicchan, sei così paranoico."

show shizu adjust_smug at twoleft
with charachange

shi "…"

show misha cross_smile_close at tworight
with charachange

mi "…E comunque non mi batterai mai, quindi perchè ti dai la pena di agitarti così tanto?"

show misha cross_laugh_close at tworight
with charachange

mi "Haha! Wow, Shicchan~!"

hi "Batterti? Di che stai parlando?"

"Sta parlando della coercizione? Non mi ero mai accorto che fosse solo un gioco per lei. Pensavo di essere il solo che la vedeva come una competizione."

show shizu basic_happy at twoleft
with charachange

shi "…"

show misha hips_grin_close at tworight
with charachange

mi "Lo sai~! …Eh? Lo sai, Hicchan? Perchè io non capisco."

show shizu adjust_smug at twoleft
with charachange

shi "…"

show misha hips_smile_close at tworight
with charachange

mi "Non puoi battermi in ingegno! —Ah, cioè, Hicchan, non me…"

show shizu basic_sparkle at twoleft
with charachange

shi "…"

show misha perky_confused_close at tworight
with charachange

mi "Cosa? Di che stai parlando, Shicchan…"

"Posso vedere Shizune sorridere astutamente, sfidandomi a entrare in questa battaglia di intelligenza e forza di volontà con lei."

"Quando viene spinto fino ai bordi della disperazione, un uomo non ha altra scelta che affondare, o aggrapparsi agli sfuggenti fili della speranza, combattere con tutte le sue forze contro le inevitabilità del suo fato e lottare contro l' impossibile."

"Perchè anche se fallisce, almeno fallisce sapendo di aver grandemente osato…"

"…O qualcosa del genere."

hi "Bene, vedremo, non sottovalutarmi."

show shizu behind_blank at twoleft
with charachange

shi "…"

show misha perky_smile_close at tworight
with charachange

mi "Non devi dimostrarlo prima di potertene vantare, Hicchan?"

hi "Ah, beh, potrei avere fortuna, non lo puoi escludere."

show shizu adjust_smug at twoleft
with charachange

shi "…"

show misha cross_grin_close at tworight
with charachange

mi "Non ci riuscirai~."

hi "Ci riuscirò! Aspetta—"

show shizu basic_happy at twoleft
with charachange

shi "…"

show misha cross_smile_close at tworight
with charachange

mi "Facciamo una scommessa sul risultato, allora!"

hi "Non mi interessano le gare."

"Quella è una bugia sfacciata."

hi "Aspetta, che vuoi dire esattamente?"

show misha cross_laugh_close at tworight
with charachange

mi "Fa lo stesso se non lo sai, non lo so nemmeno io! Wahahaha!"

show shizu basic_normal2 at twoleft
with charachange

shi "…"

show misha perky_smile_close at tworight
with charachange

mi "Così è deciso, allora! Bene, bene!"

hi "Cosa? Non hai sentito quello che ho appena detto?"

show shizu adjust_happy at twoleft
with charachange

shi "…"

show misha sign_smile_close at tworight
with charachange

mi "Ora tutto quel che rimane è il piatto! Cosa vince il vincitore, o, ancora più interessante, cosa perde il perdente!"

hi "Ehi!"

"E' un gioco molto pericoloso questo che sto giocando. Shizune è una ragazza molto pericolosa, se sa solo pensare in termini di vincere e perdere."

"Se vede ogni volta che parlo con lei come una specie di scontro tra forze di volontà, non credo che potrei resistere."

"Quel genere di cose fa ammattire la gente. E' troppo machiavellica; prima di questo avevo presunto che fosse solo piuttosto stoica."

"Ma nonostante tutto, sono interessato. Ripensandoci, capisco che la ho appena sfidata a quello che è essenzialmente un duello senza alcuna regola che non terminerà finchè uno di noi… cosa?"

"Immagino che sia così. E' così vago. Quali sono le condizioni di vittoria o sconfitta? Il primo che si sente stupido perde?"

hi "Non saprei, non ho mai dovuto pensare a una cosa del genere prima."

show misha hips_smile_close at tworight
with charachange

mi "Mai?"

hi "Mai."

show misha perky_confused_close at tworight
with charachange

mi "Quindi non hai mai giocato d' azzardo, Hicchan?"

hi "Sono sorpreso che voi due lo abbiate fatto."

show shizu behind_blank at twoleft
with charachange

shi "…"

show misha hips_grin_close at tworight
with charachange

mi "Oh, suvvia… E' solo per divertirsi, comunque, tra amici~!"

show misha sign_smile_close at tworight
with charachange

mi "E' per causare umiliazione, sofferenza, ed assoluta disperazione! Non è quello il punto?"

"Shizune poggia pensosamente un dito sulla sua tempia."

show shizu adjust_happy at twoleft
with charachange

shi "…!"

show misha hips_smile_close at tworight
with charachange

mi "Hm… Ah, che ne dici di questo, Hicchan: Se perdi, devi andare a scuola senza calzoni per un giorno intero."

hi "Sei impazzita?"

"Anche se comparato a quel che temevo avrebbe detto, è piuttosto leggero."

hi "Non possiamo semplicemente scommettere dei soldi, come persone normali?"

show shizu basic_sparkle at twoleft
with charachange

shi "…"

show misha hips_grin_close at tworight
with charachange

mi "Non che tu saresti in grado di vedere la mia puntata se facessimo così~! Ora, è il tuo turno! …Ma niente di perverso! Capito?"

show misha hips_laugh_close at tworight
with charachange

mi "Hahaha!"

hi "Credo di aver bisogno di più tempo."

"Questo mi farà stare costantemente sulle spine per settimane."

show misha hips_grin_close at tworight
with charachange

mi "Okay~! Forza, dovreste sbrigarvi entrambi, le vostre bevande si stanno raffreddando!"

show shizu basic_happy at twoleft
with charachange

"Finisco frettolosamente il resto del mio caffè mentre Shizune fa lo stesso, fissandomi con un fiero sguardo pieno di competizione nei suoi occhi."

"Sembra uno spreco che lei inghiotta a gran sorsi una cosa per cui qualcuno potrebbe essere morto perchè lei ne possa godere."

show misha sign_smile_close at tworight
with charachange

mi "Hicchan, sei sicuro di non volerci fare compagnia domani? Un sacco di gente non vede l' ora che arrivi; davvero non te lo vuoi perdere."

"Le borbotto qualcosa di incomprensibile."

show misha perky_confused_close at tworight
with charachange

mi "Non ho capito bene…"

"E' ora di pensare. La tazza di Shizune è più piccola, ma io posso bere più in fretta."

"Se Shizune finisce di bere per prima, potrebbe non pagare il conto, lasciandomi nelle peste, anche se ha detto che avrebbe offerto lei da bere."

"Dato che non ho soldi con me, verrei umiliato, e quindi questa potrebbe essere considerata una sconfitta."

"Se finisco per primo, le regole della cavalleria mi farebbero sembrare una carogna se dovessi fuggire di corsa da questa sala da tè, lasciandole tutto da pagare. Anche quella potrebbe essere considerata una sconfitta. Lei sfrutterebbe la situazione."

"In caso di un pareggio, lei potrebbe tentare di fuggire dalla porta, e io probabilmente farò lo stesso. Questo potrebbe portare a una collisione alla porta, che sarebbe umiliante, ma non troppo. …E rimarrebbe solo Misha a pagare il conto."

"Questo è davvero infantile. Sono un poco deluso da Shizune, e da me stesso."

show misha perky_smile_close at tworight
with charachange

mi "Beh, Hicchan, sarebbe veramente carino se potessimo celebrare tutti insieme il modo in cui abbiamo organizzato tutto il festival per bene dando un' occhiata ai frutti del nostro lavoro…"

"Misha sembra ignara del fatto che un' epica battaglia di volontà sta venendo combattuta di fronte a lei. Annuisco lentamente e deglutisco l' ultimo residuo del mio caffè."

hi "Bene, ho finito di godermi il mio caffè. Credo che per me sia ora di andare. Quindi adesso sto per andarmene. Tranquillamente."

show shizu adjust_happy at twoleft
with charachange

shi "…"

show misha perky_confused_close at tworight
with charachange

mi "Anche tu, Shicchan?"

mi "Perchè voi due vi state comportando in modo così strano?"

scene bg suburb_shanghaiext
with locationchange

"Esco rapidamente dalla porta e Shizune mi segue. Misha dovrà pagare il conto."

scene bg suburb_roadcenter
with locationchange

"Scusa, Misha."
    
show shizu behind_smile
with charaenter

"Raggiungendomi, Shizune spinge velocemente su i suoi occhiali e preme un biglietto nella mia mano."

$ written_note("Se perdi, sei obbligato a farci compagnia domani.")

hi "Così credi di poter vincere oggi? Mi sembra un tantino arrogante, Shizune."

"Ho dimenticato per un attimo che non può sentirmi. Faccio segno di sì."

"Proprio ora, lei sembra molto più carina del solito, dolcemente sorridente con un pochino di sicurezza che traspare."

"Shizune sembra energica e spensierata, anche se potrebbe essere solo colpa della caffeina."

show shizu adjust_happy
with charaenter

"Mi strizza l' occhio, e stende la sua mano per una stretta. Mi chiedo se c'è un buzzer lì dentro e se ha intenzione di darmi una scossa, ma non sembra il tipo di cosa che farebbe, così accetto."

"Con la stretta, lascia un' altra nota nella mia mano. Per un attimo penso che sia il buzzer e mi chiedo se lo shock potrebbe uccidermi."

hide shizu
with charaexit

"Shizune sogghigna e corre via."

$ written_note("Probabilmente non sai come ritornare a scuola da qui.\n\nCi sarà del lavoro che ti aspetta quando ci riuscirai. A presto~")

"Schiaccio drammaticamente il biglietto nel mio pugno ma non c'è nessuno che mi veda farlo, e questo mi rende triste."

"Mi chiedo se è troppo tardi per tornare al negozio e chiedere delle indicazioni a Misha."

"Ma d' altra parte, l' ho presa in giro perchè non sapeva come arrivare qui, così non le posso permettere di segnare punti contro di me perchè non so come tornare indietro."

"E se glie lo chiedo, Shizune potrebbe vederla come una vittoria. No, non è necessario."

"La scuola è sulla cima di una dannata collina, quanto può essere difficile trovarla?"

"Posso non avere un buon senso della direzione, ma sono sicuro che anche io posso farcela."

stop music fadeout 1.5

scene bg school_courtyard
with shorttimeskip

play music music_normal fadein 0.5

"Circa un' ora e mezza più tardi, cammino per il lungo sentiero lastricato che va dai cancelli all' edificio principale."

scene bg school_lobby
show shizu behind_blank at tworight
show misha hips_grin at twoleft
with locationchange

mi "Hahaa! Giusto la persona che stavamo aspettando. Così finalmente ce l' hai fatta, Hicchan, bene! Ora è tempo di lavorare lavorare lavorare~!"

"Misha e Shizune avevano preparato un' imboscata per me nell' atrio principale al pianterreno e io ci sono cascato dritto dentro."

"Avrei solo dovuto girare intorno alla scuola come avevo pianificato in origine, ma ho pensato di stare esagerando e di essere sciocco."

"Misha sta agitando una spessa pila di stampe nella mia generale direzione, prendendomi in giro."

show misha perky_smile at twoleft
with charachange

mi "Abbiamo un po' bisogno del tuo aiuto~!"

hi "Un po'?"

show misha hips_grin at twoleft
with charachange

mi "Abbiamo bisogno del tuo aiuto~!"

show shizu cross_angry at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Tu ci aiuterai!"

"Misha parla nella sua solita maniera giocosa e spensierata, ma anche così riesco a sentire la snervante e dura severità di Shizune dietro le parole."

hi "Quello suona come un ordine."

mi "Davvero? Lo è?"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "Eh? Lo è?"

show misha hips_laugh at twoleft
with charachange

mi "Ah, mi dispiace, Hicchan, suppongo che lo sia! Hahahaha!"

"Suona come se non le dispiacesse affatto."

show misha hips_grin at twoleft
with charachange

mi "Avevo pensato che ormai avessimo già fatto quasi tutto, ma viene fuori che abbiamo tutti questi segnali da attaccare a dei cartelli."

show shizu adjust_angry at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Tante mani significano lavoro leggero!"

show misha hips_laugh at twoleft
with charachange

mi "E tutti vincono! Hahahahaha!"

show shizu basic_angry at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Questo è tuo dovere, dopo tutto, come un membro del consiglio studentesco. Di cui sei parte."

mi "Come un membro."

mi "Del consiglio studentesco."

show misha hips_laugh at twoleft
with charachange

mi "Ahahaha~!"

show shizu behind_blank at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "E' un compito semplice, così toglierlo di mezzo adesso sarebbe bene. Non è così tanto lavoro. Una sciocchezza, davvero!"

show shizu basic_normal2 at tworight
with charachange

shi "…"

mi "E apprezzeremmo davvero il tuo aiuto!"

mi "Lo apprezzeremmo davvero, davvero!"

show misha hips_grin at twoleft
with charachange

mi "E inoltre, è ora che ci ripaghi per averti trattato così bene!"

hi "Così la sala da tè era una trappola dopo tutto! Traditrici e mentitrici!" 

show shizu behind_blank at tworight
with charachange

shi "…"

show misha cross_smile at twoleft
with charachange

mi "Non dire così. Non aveva assolutamente niente a che fare con questo, volevamo celebrare il tuo unirti al consiglio!"

"Ma allora perchè la ha tirata fuori adesso?"

hi "Ma—{w=0.3}{nw}"

show shizu cross_rage at tworight
with charachange

shi "…!"

show misha hips_grin at twoleft
with characlose

mi "Niente ma! Tu vieni con noi!"

show misha hips_grin at offscreenleft
show shizu cross_rage at offscreenright
with ease

show misha cross_smile_close at closeleft
show shizu cross_angry_close at closeright
with ease

"Non riesco nemmeno a finire la mia frase prima che mi prendano per le braccia e tentino di trascinarmi verso il loro ufficio."

show misha cross_laugh_close at closeleft
with charachange

"Misha ride istericamente mentre lei e Shizune si scambiano sguardi astuti dietro la mia schiena."

show shizu basic_angry_close at tworight
with charachange

shi "…!"

mi "Ah, non credo che tu abbia una scelta, Hicchan! Hahahaha!"

show misha hips_grin at twoleft
show shizu basic_angry at tworight
with charadistant

mi "Noi siamo in due, quindi non provare nemmeno a scappare, ora! Non prenderci alla leggera!"

show shizu behind_frown at tworight
with charachange

shi "…!"

mi "Hicchan, è tuo dovere aiutarci, comunque! Come un membro del consiglio studentesco!"

hi "Va bene, va bene! Come potrei dimenticarlo?"

hi "Però, seriamente, non ci sono altre persone che possono aiutarvi?"

show misha perky_confused at twoleft
with charachange

mi "Tipo chi, Hicchan?"

mi "Ti stava bene aiutarci ieri…"

hi "Ieri non è oggi!"

hi "E chiunque non sia io!"

hi "Perchè non c'è nessun altro nel consiglio?"

stop music fadeout 1.0

show shizu cross_wut at tworight
with charachange

shi "…!"

show misha cross_laugh at twoleft
with charachange

play music music_shizune fadein 0.3

mi "E' quello che ci piacerebbe sapere! …Aha… Ahahahahaha!"

"Le risa di Misha esplodono attraverso il corridoio. Non si accorge affatto della smorfia sulla mia faccia. E' vero, sono solo loro due, no?"

hi "Oh, giusto. D' accordo, vi aiuterò."

show misha hips_grin at twoleft
with charachange

"Misha si passa la lingua sui denti, e sembra molto soddisfatta."

mi "Questo è il mio Hicchan! Sapevo che potevamo fidarci di te!"

show shizu behind_smile at tworight
with charachange

shi "…!"

mi "Così prevedibile~."

scene bg school_council
with locationskip

"Quando arriviamo alla stanza del consiglio studentesco, resto a bocca aperta. Il numero di segnali, cartelli, e pali è pazzesco."

"Sono impilati da tutte le parti come materiali di costruzione in un cantiere, una cosa di cui informo Shizune e Misha senza esitazione."

hi "Ci sono così tanti pali qui che usandoli probabilmente potrei costruire un secondo muro intorno alla scuola!"

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

mi "Hahaha~! Davvero? Beh, sono tanti, così forse…"

show shizu basic_angry at tworight
with charachange

shi "…!"

show misha perky_confused at twoleft
with charachange

mi "Eh? No?"

mi "Come fai a saperlo, Shicchan?"

show shizu behind_frown at tworight
with charachange

shi "…!"

mi "Davvero?"

hi "Non dirmi che lo ha davvero preso in considerazione?!"

show misha hips_grin at twoleft
show shizu adjust_smug at tworight
with charachange

"Shizune esita, poi spinge un poco su i suoi occhiali mentre Misha si lascia sfuggire una risata che suona molto nervosa."

"Così lo ha preso in considerazione."

show shizu basic_normal2 at tworight
with charachange

shi "…!"

mi "Ahaha! Quello è… irrilevante, Hicchan! Puoi muoverti e costruire i cartelli, per favore?"

hi "Va bene, va bene."

hi "Mi sembra che mi abbiate mentito, però. Credevo avessi detto che non sarebbe stato poi così tanto lavoro?"

show shizu behind_blank at tworight
with charachange

shi "…!"

show misha hips_smile at twoleft
with charachange

mi "Ah, bè, Shicchan voleva dire che non sarebbe così tanto lavoro per noi."

show shizu basic_normal at tworight
with charachange

shi "…!"

mi "Qualcuno deve supervisionarti mentre fai questo lavoro, sai, per assicurarsi che tu lo faccia bene. E quelle persone saremo noi."

hi "Così voi due cosa farete?"

show misha cross_laugh at twoleft
show shizu basic_happy at tworight
with charachange

mi "Guarderemo! Hahahaha~!"

show shizu adjust_happy at tworight
with charachange

shi "…!"

show misha perky_smile at twoleft
with charachange

mi "No, quello era solo uno scherzo, Hicchan. Anche noi ti aiuteremo, certo. Il consiglio studentesco dovrebbe davvero avere molto più personale."

show misha perky_sad at twoleft
with charachange

mi "Questo è solo un brutto anno. Meno persone del solito, anche se l' anno prima ne avevamo ancora di meno."

"Meno persone del solito? Meno di ora? Così quello significa che prima… una persona sola?"

mi "E poi c'è proprio anche un sacco di lavoro in più rispetto a prima."

show shizu behind_smile at tworight
with charachange

shi "…!"

show misha perky_smile at twoleft
with charachange

mi "E poi, a Shicchan piace lavorare con te. E anche a me!"

mi "Abbiamo fatto molto più di quello che normalmente potremmo, sai."

"Posso ben crederci. Recentemente, sembrano un po' stanche ogni volta che le vedo."

"Lavorare per il consiglio studentesco è apparentemente un contratto da 24 ore al giorno, e da quel che ho visto e sentito, ci sono solo loro due. Bè, immagino di essere io il terzo."

"Devono lavorare quasi ininterrottamente. Mi chiedo quanto tempo spendono lavorando in questa stanza, quando non le vedo."

"E ho perfino occasionalmente visto Misha fare dei sonnellini qualche volta senza Shizune al suo fianco. Da sola, Shizune deve lavorare settimane da 60 ore espletando i suoi doveri del consiglio studentesco, in addizione alle normali lezioni."

scene bg school_council_ss
with shorttimeskip

"Passano due ore, e cerco di prendere una puntina solo per scoprire che la scatola è vuota. Shizune la afferra ancora prima che io possa dire qualcosa."

show shizu adjust_happy_ss at tworight
show misha perky_smile_ss at twoleft
with charaenter

"Sorride, lanciandola espertamente in un cestino dei rifiuti assieme a un' altra scatola di puntine vuota che ha in mano."

show shizu behind_smile_ss at tworight
with charachange

shi "…!"

show misha hips_grin_ss at twoleft
with charachange

mi "Così le hai finite anche tu, Hicchan? Non preoccuparti, Shicchan dice che ne prenderà delle altre."

show misha hips_laugh_ss at twoleft
with charachange

mi "Hahahaha!"

show misha hips_grin_ss at twoleft
with charachange

mi "Anche noi abbiamo finito una scatola, ma io e Shicchan abbiamo deciso di aspettare finchè non avevi bisogno anche tu di una scatola piena prima di prenderne una nuova."

"Qualcosa di tutto questo mi sembra strano."

hi "Aspetta, abbiamo finito tutti le puntine proprio ora? Wow, che strana coincidenza, eh?"

show misha perky_smile_ss at twoleft
with charachange

mi "Ah, bè, a dire il vero, Hicchan, le abbiamo finite venti minuti fa, e c'era solo una scatola di riserva, quella che abbiamo dato a te."

mi "E stavi facendole fuori piuttosto in fretta, così~! abbiamo pensato che avremmo dovuto aspettare finchè tutti non avessimo finito le puntine!"

show misha sign_smile_ss at twoleft
with charachange

mi "Così, Shicchan avrebbe potuto andare a prendere nuove scatole di puntine per tutti allo stesso tempo. Sai, per maggiore efficienza~!"

show shizu basic_normal2_ss at tworight
with charachange

"Shizune annuisce, preparandosi a uscire dalla porta."

hi "Aspetta un attimo, così voi due cosa avete fatto per gli ultimi 20 minuti?"

show shizu adjust_happy_ss at tworight
with charachange

shi "…!"

show misha hips_grin_ss at twoleft
with charachange

mi "Ahaha~! Niente, ovviamente! Cosa potevamo fare? Eravamo senza puntine, Hicchan!"

show shizu behind_smile_ss at tworight
show misha cross_grin_ss at twoleft
with charachange

"Shizune e Misha si scambiano sguardi d' intesa prima di offrirmi una perfettamente sincronizzata ed incredibilmente esagerata simultanea scrollata di spalle."

hi "Vedo. Così avete deciso di fare una pausa. Astuto."

show shizu adjust_smug_ss at tworight
with charachange

shi "…!"

show misha hips_grin_ss at twoleft
with charachange

mi "Oh, sappiamo che era astuto."

hi "Di chi è stata l' idea?"

show misha hips_smile_ss at twoleft
show shizu adjust_happy_ss at tworight
with charachange

mi "Di entrambe, ovviamente, ovviamente!"

show misha cross_laugh_ss at twoleft
with charachange

mi "Ahahaha~! Bene, Hicchan, è stata tutta un' idea di Shicchan."

show shizu behind_smile_ss at tworight
with charachange

hide shizu
with charaexit

"Mi giro immediatamente verso Shizune, che mi fa un breve saluto e un sorriso sorprendentemente allegro prima di svanire rapidamente fuori dalla porta."

show misha cross_grin_ss at twoleft
with charachange

show misha cross_grin_ss
show bg school_council_ss at bgright
with charamove

"Bene, allora perchè non avete semplicemente detto che volevate fare una pausa!?"

"Prima pensavo che Shizune e Misha fossero poli opposti."

"Misha sembra sempre così energica e giocosa, come qualunque altra ragazza."

"Shizune, d' altra parte, sembrava sempre distante. Aggressivamente manipolatrice e vagamente spaventosa, ma distante."

"Ci sono stati momenti quando ho pensato che non avesse un senso dell' umorismo. Per quanto fosse graziosa, non la avevo quasi mai vista sorridere. Per non menzionare tutto il resto."

"Lo sguardo analitico, l' espressione permanentemente stoica, e perfino la sua calligrafia; così meccanicamente precisa che tutto quello che scrive sembra stampato."

"Ma Shizune e Misha non sono davvero tanto differenti quanto pensavo."

hi "Sono un poco sorpreso."

stop music fadeout 1.0

show misha perky_confused_ss
with charachange

play music music_happiness fadein 1.0

mi "Perchè?"

hi "Shizune. Non sapevo le piacesse scherzare in quel modo."

"Quel che voglio dire è, non sapevo che potesse comportarsi in modo così femminile. A dire il vero era piuttosto grazioso."

show misha perky_smile_ss
with charachange

mi "Resteresti sorpreso, Hicchan."

hi "Bè, non sapevo neanche che tu e lei foste così inseparabili, la prima volta che vi ho visto."

"Sono sempre stato curioso di sapere come queste due si sono incontrate."

hi "E' da molto che vi conoscete o qualcosa del genere?"

hi "Amiche di infanzia?"

hi "Vicine di casa?"

show misha perky_sad_ss
with charachange

mi "Haha… Mi spiace, Hicchan, non è niente del genere, anche se sarebbe più carino se fosse così."

show misha perky_smile_ss
with charachange

mi "Quando sono arrivata in questa scuola, mi hanno solo piazzato vicino a Shicchan, e lei sembrava una persona molto seria."

show misha sign_smile_ss
with charachange

mi "E ho pensato, “Passerò il resto dell' anno accanto a questa persona, forse!”"

mi "“Così sarebbe bello se potessimo essere amiche! Ma, mi chiedo se le piacerò.”"

show misha hips_grin_ss
with charachange

mi "E ho imparato che era sorda. Sai, Hicchan, la prima volta ho pensato che mi stesse solo ignorando~!"

show misha hips_smile_ss
with charachange

mi "Ma, fortunatamente, conoscevo un po' di lingua dei segni, e diventammo amiche."

"Voglio sapere dove è che Misha ha imparato la lingua dei segni, ma suppongo che sia qualcosa da chiedere un' altra volta."

show misha perky_smile_ss
with charachange

mi "Adesso, direi che stiamo sempre insieme. E' bello, io ho sempre voluto qualcuno che mi ascoltasse, e penso che a Shicchan piaccia avere qualcuno con cui parlare! Così, tutti guadagnano qualcosa."

hi "Heh. E' bello."

show misha hips_grin_ss
with charachange

stop music fadeout 1.5

mi "Tutto qui? Sembri deluso, Hicchan, cosa ti stavi aspettando?"

play music music_comedy fadein 0.5

show misha hips_laugh_ss
with charachange

mi "Ahahahahaha!"

show misha hips_grin_ss
with charachange

mi "Sai, Hicchan, non credo che io e Shicchan ti abbiamo ringraziato a dovere."

hi "Per cosa?"

show misha perky_smile_ss
with charachange

mi "Per esserti iscritto al consiglio studentesco. Ci sei stato di grande aiuto, Hicchan, adesso penso che riuscirò a dormire molto di più~!"

hi "Bene, sono felice di essere d' aiuto, se aiuta una giovane donna a dormire la notte."

show misha hips_smile_ss
with charachange

mi "Quella è una cosa interessante da dire, Hicchan."

mi "Anche Shicchan apprezza veramente che tu ci aiuti."

stop music fadeout 0.5

show misha hips_smile_ss at twoleft
show bg school_council_ss
with charamove

show shizu behind_frustrated_ss at tworight
with charaenter

"In quel momento, Shizune rientra nella stanza, con un' aria leggermente infastidita e bevendo rapidi sorsi da un piccolo cartone di succo."

play music music_shizune fadein 0.25

show shizu adjust_happy_ss at tworight
with charaenter

shi "…"

"Lancia sul pavimento due scatole di puntine con un sorriso storto."

show shizu basic_normal2_ss at tworight
with charachange

shi "…!"

show misha sign_smile_ss at twoleft
with charachange

mi "Ah, Shicchan."

play sound sfx_crunchydeath

show shizu behind_frown_ss at tworight
show misha sign_confused_ss at twoleft
with charachange

"Misha apre bocca per parlare, ma poi rapidamente la richiude quando Shizune improvvisamente accartoccia il suo cartone con un rumore simile al suono di ossa rotte."

show shizu basic_angry_ss at tworight
with charachange

shi "…!"

show shizu adjust_angry_ss at tworight
with charachange

shi "…"

show shizu behind_frown_ss at tworight
with charachange

shi "…!"

"Posso dire che ogni duro, tremante gesto con le mani è molto probabilmente un epiteto."

hi "Cosa sta dicendo?"

show misha perky_confused_ss at twoleft
with charachange

mi "E' solo stato molto difficile ottenere queste…"

show shizu basic_angry_ss at tworight
with charachange

shi "…!"

show misha sign_confused_ss at twoleft
with charachange

mi "Immagino che sia un eufemismo, Shicchan…"

"Shizune si calma un po', aggiustandosi gli occhiali e pettinando leggermente indietro la sua frangia di capelli con un dito."

show shizu adjust_happy_ss at tworight
with charachange

shi "…"

show misha perky_smile_ss at twoleft
with charachange

mi "Ripensandoci, non è poi stato così un gran problema? Questo è previdente da parte tua!"

show misha hips_smile_ss at twoleft
with charachange

mi "Bene allora, immagino che noi due dovremmo tornare al lavoro, Hicchan!"

hi "Certo, perchè no."

scene bg school_council_ni
with shorttimeskip

"Quando abbiamo finito coi cartelli, sta già facendo buio fuori."

"Non mi aspettavo che qualcosa del genere prendesse così tanto tempo. Ma d' altra parte, se fosse stato così facile, dubito che Shizune e Misha avrebbero chiesto il mio aiuto."

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter

"Shizune cade in una sedia vicina, facendo crocchiare sistematicamente le sue nocche e lasciandosi sfuggire uno sbadiglio sommesso."

show shizu behind_blank at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "E' tutto per oggi, direi! E' un gran bene, Shicchan, anche io sono molto stanca."

hi "Questo ha preso più tempo del previsto."

show shizu behind_frustrated at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Sei d' accordo? Hahaha, nenche noi ci aspettavamo di metterci tanto! Non come previsto!"

show misha perky_sad at twoleft
with charachange

mi "Aww, ho tanta fame. Mi sono appena ricordata di non aver mangiato niente tutto oggi."

"Ora che ci penso, neanche io ho mangiato da quando mi sono svegliato stamattina, ma ora sono quasi troppo stanco per pensare al cibo."

hi "Credo che abbiano già smesso di servire la cena."

show misha perky_confused at twoleft
with charachange

mi "Non è possibile! Hicchan, puoi pensare a qualunque modo con cui potremmo… ottenere del cibo?"

hi "Ottenere del cibo?"

"Non mi piace il suo tono di voce."

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Perchè non ordinarne? Oh, giusto, immagino che potremmo."

hi "Ordinarne? Da dove?"

mi "Dalla città, ovviamente!"

hi "Non sapevo che consegnassero alla scuola. Bè, che cosa avete intenzione di prendere?"

show misha hips_smile at twoleft
with charachange

mi "Forse un po' di cucina cinese!"

hi "Dato che lo fate già voi, posso unirmi anche io? Anch' io mi sento piuttosto affamato."

show misha hips_laugh at twoleft
with charachange

mi "Ahahaha~! Hicchan, avresti dovuto semplicemente dirlo subito!"

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Che cosa? Offri tu? Grande! Grande!"

show shizu behind_blank at tworight
with charachange

shi "…"

show misha cross_laugh at twoleft
with charachange

mi "Wahaha, è vero, se non fosse per te, non saremmo qui così tardi, Shicchan!"

show misha cross_grin at twoleft
with charachange

"Misha afferra svelta un menù da un cassetto dietro di lei e inizia a comporre il numero lentamente e accuratamente, come se fosse abituata a sbagliarlo."

mi "Che cosa vuoi, Hicchan?"

hi "Beh, credo che prenderò solo dei ravioli."

show shizu behind_smile at tworight
with charachange

"Alzo la mano in un gesto di ringraziamento a Shizune, che risponde con un lievissimo sorriso, per una frazione di secondo."

show misha cross_laugh at twoleft
with charachange

mi "Ahahahahaha~!! Hicchan, Shicchan paga per tutti stasera, offre tutto lei, così ti puoi permettere di abbondare un po'!"

hi "Allora, anche del riso fritto con scampi."

show misha cross_grin at twoleft
with charachange

mi "Va bene, va bene! E tu, Shicchan?"

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Una frittata cinese? Okay, allora."

hi "Ehi, Misha, quello vuol dire veramente “frittata?” Puoi farmelo rivedere?"

show misha hips_grin at twoleft
with charachange

mi "Certo! Haha! Così, così…"

mi "E questo è per quello che hai ordinato: ravioli!"

mi "Riso fritto con scampi!"

mi "Io prenderò della zuppa e una frittura, lo si dice così…"

show misha cross_laugh at twoleft
with charachange

mi "Ed ecco quanto costa il tutto: 3685 yen! Wahahahaha~!"

hi "Beh, non so in quante situazioni avrò bisogno di ricordarmi quel preciso numero…"

mi "Ahahahaha! Okay~! Sto per ordinare, in caso che qualcuno voglia qualcos' altro. Nessuna obiezione? Bene bene, allora!"

scene bg school_council_ni
show shizu behind_frustrated at tworight
show misha hips_smile at twoleft
with shorttimeskip

"Shizune rigira impazientemente un paio di bastoncini tra le dita mentre aspettiamo che il cibo arrivi."

hi "Ehi, dove li hai presi quelli?"

show misha hips_grin at twoleft
with charachange

mi "Questa non è la prima volta che abbiamo ordinato da mangiare fuori, Hicchan, e ci danno sempre una tonnellata di bastoncini, per qualche motivo, anche quando gli diciamo che siamo solo in due."

hi "E voi due ne avete accumulati un mucchio dopo un mucchio di lunghe notti mangiando cibo da asporto nell' ufficio?"

show misha cross_laugh at twoleft
with charachange

mi "Esattamente! Hahahahahaha!"

show shizu basic_angry at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "Sto esagerando?"

show shizu behind_blank at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Haha! Giusto, Shicchan! Ehi, Hicchan, sapevi che una volta che avremo collezionato cento paia di bastoncini ordinando da mangiare, potremo governare l' universo?"

hi "Anche io una volta lo credevo, quando ero piccolo."

show misha perky_smile at twoleft
with charachange

mi "Hicchan, sei bravo a dividerli al centro? Io non riesco mai a farlo bene, così ho trovato la piccola pila di bastoncini che Shicchan aveva conservato e ho fatto pratica su almeno venti di quelli."

show misha hips_grin at twoleft
with charachange

mi "Si è davvero arrabbiata quella volta!"

show shizu adjust_blush at tworight
with charachange

shi "…!"

"Mi scappa da ridere quando Shizune diventa rossa come un peperone in indignazione. Non sapevo che avesse un lato così infantile."

scene bg school_council_ni
with shorttimeskip

"Quando il cibo arriva, lo divoro di gusto, bevendo una delle minuscole lattine di soda che Shizune ha comprato per noi da una delle macchine distributrici nel corridoio."

stop music fadeout 2.0

"Ringraziandole entrambe per la cena, torno ai dormitori, pronto a ritirarmi per la notte."

scene bg school_dormhallway
with locationskip

"I dormitori sono spettralmente silenziosi eccetto per i suoni di TV portatili e radio che mormorano incomprensibilmente dietro muri sottili."


play ambient sfx_cicadas fadein 4.0

scene bg school_dormhisao_ni
with locationchange

"Di notte qui è silenzioso, e molto pacifico. Posso sentire i grilli frinire fuori dalla mia finestra, e vedere delle vere stelle quando guardo in alto."

"Stanco, tento di addormentarmi quanto più in fretta posso, sentendomi solo un poco derubato del mio sabato."

stop ambient fadeout 1.0

scene black
with shuteye




#*********************

label it_A37:

#Taken from the Hanako split.
#based on the new ending for A31

# This now comes from the H branch in A35

scene bg school_scienceroom
with None

"La biblioteca pare essere un posto buono quanto qualunque altro. Hanako sembrava essere stata presa piuttosto di sorpresa da Lilly che se ne andava, così potrebbe volere qualcuno con cui parlare."

"Mettendo la mia borsa a tracolla, esco dall' aula."

scene bg school_hallway3
with locationchange
    
"Cammino lungo il corridoio per la biblioteca, oltre una moltitudine di porte chiuse."

"Attraverso ciascuna di esse si sentono i suoni di prove furiose. Della  musica rock esplode attraverso una porta, forte quasi come quella di un concerto."

"Immagino che questo sia uno dei vantaggi di una scuola privata; ci sono stanze a sufficienza per tutti in momenti come questo."

"E, ora che ci penso, i terreni e gli edifici della scuola sono mantenuti in condizioni decisamente buone. Quello non può costare poco."

"Ho sentito dire che questo posto ha alcuni benefattori piuttosto ricchi."

play music music_happiness fadein 0.3

scene bg school_library
with locationchange

"I muri della biblioteca isolano solo parzialmente il rumore delle preparazioni per il festival, ma sono gli unici suoni che si possano sentire."

"Qui non si vede anima viva, con tutti che apparentemente si stanno godendo il bel tempo fuori o stanno lavorando su eventi per il festival."

"Non c'è neanche Yuuko. Forse non lavora di sabato."

#Does he know about the Shanghai at this point? No time for fact checking just yet

"Cammino silenzioso per la biblioteca, ormai discretamente familiare con la sua struttura. Mi dirigo verso il retro, dove si trova l' angolino privato di Hanako."

"Faccio scorrere la mia mano lungo i dorsi dei libri mentre cammino, sentendo la superficie individuale di ciascuno mentre scorro i titoli."

"Ero abituato a fare sempre così alla biblioteca dell' ospedale. Certe cose non cambiano mai, suppongo."

"Come l' odore di una biblioteca. Non importa quanta cura ci si metta, la carta dei libri finirà sempre per degradarsi col tempo."

"Probabilmente, non importa in quale biblioteca si entri, dovunque al mondo, deve avere quell' identico odore, leggermente stantio."

"Trovo qualcosa che sembra abbastanza leggero da poter essere letto senza grossi sforzi di concentrazione e cerco Hanako nella zona di lettura."

scene ev hana_library_read_std
with locationchange

"Ancora una volta, è seduta su una poltrona-cuscino dando la schiena a uno scaffale. Leggendo lo stesso libro che aveva in aula, sta lentamente progredendo attraverso le pagine."

show ev hana_library_std
with locationchange

"A differenza dell' ultima volta che l' ho vista qui, mi siedo silenziosamente a mia volta. Il rumore basta ad attrarre la sua attenzione, ma non a spaventarla."

"Questa delicata routine che deve essere seguita ogni singola volta che cerco di parlare con lei mi fa quasi sentire come se stessi andando a caccia."

hi "E' lo stesso libro di prima?"

ha "S-sì… ho quasi finito…"

hi "Ottimo."

"Mi chiedo se dovrei…"

hi "Potrei prenderlo in prestito quando lo hai finito?"

"La mia bocca è più veloce del mio cervello, a quanto pare."

ha "C-certo… potrebbe n-non piacerti ma…"

hi "Sono sicuro che non sia così male. Dopotutto, tu non lo hai abbandonato, giusto?"

ha "S-suppongo di no."

scene bg school_library
with locationchange

"Mi sistemo nella mia poltrona e mi dedico a leggere il mio libro che avevo sepolto nella mia borsa."

"E' una light novel che parla di pirati. Per essere onesto sto a malapena scorrendo le parole, avendo scelto il libro solo perchè appartiene a un genere differente da quello che leggo di solito."

"Trovando difficile raccogliere abbastanza entusiasmo per finire il libro, e notando che inavvertitamente ho distratto molto Hanako, decido di provare a fare conversazione."

hi "Così, vedo che Lilly se ne è andata senza di te?"

show hanako emb_downtimid
with charaenter

show hanako basic_worry
with charachange

"Annuisce prima di distogliere gli occhi dal suo libro. Doveva essere veramente interessata dopotutto."

ha "Lilly ha detto che doveva andare a… incontrare qualcuno…"

hi "Oh?"

show hanako basic_normal
with charachange

ha "A-Akira. Sua sorella…"

hi "Sorella? Non l' ho mai sentita parlare della sua famiglia…"

show hanako cover_distant
with charachange

ha "Lei… lei e Akira vivevano insieme una volta."

hi "Credevo che tutti gli studenti vivessere nei dormitori?"

show hanako cover_worry
with charachange

ha "N-non sono… voglio dire, siamo… obbligati."

hi "Ma è più semplice, giusto? Voglio dire, qui si può mangiare e si è vicini alla scuola… Non credo di essere arrivato puntualmente in classe così spesso in tutta la mia vita."

show hanako cover_smile
with charachange

"Il suo sorriso malamente nascosto si dimostra ampiamente gratificante."

"In un angolo della mia mente so di avere un po' di compiti di cui prendermi cura, ma qui si sta molto comodi. E nessuno può trovarmi e obbligarmi a lavorare per il loro progetto personale."

"Anche se adesso che sto pensando al festival, sorge un' altra domanda…"

hi "Ehi, Hanako, che cosa fai per il festival?"

stop music fadeout 0.2

show hanako def_shock
with charachange

"Per un istante penso che Hanako stia per lanciare il suo libro in aria a causa dello shock."

ha "S-scusa…?"

hi "Stavo solo chiedendo cosa fai per il festival di domani. Hai dei piani?"

show hanako def_worry
with charachange

ha "Io… non lo so."

"Hanako risponde nel modo che le persone usano quando non vogliono che tu faccia altre domande. Immagino che grandi folle e musica rumorosa non siano davvero le sue cose preferite."

hi "Oh, okay."

"Cambia argomento, cambia argomento…"

play music music_happiness fadein 0.3

hi "Così, com'è la sorella di Lilly?"

show hanako basic_normal
with charachange

ha "E'… è simpatica. E' bella come Lilly, ma si veste… per affari…"

hi "Per affari?"

show hanako basic_distant
with charachange

ha "Lei… lei è sempre in giacca e cravatta…"

hi "Ah, vedo. E quello la rende meno bella in qualche modo?"

show hanako emb_emb
with charachange

"Hanako scuote la testa, imbarazzata."

ha "N-no… solo… diversa."

"Devo ammetterlo, questo mi incuriosisce. Sentire Hanako parlare di qualcuno che non è Lilly è una novità, e che ne parli anche in luce positiva…"

"Ma mentre cerco di figurarmi questa misteriosa sorella, tutto quello a cui riesco a pensare è Lilly in giacca e cravatta. E non riesco a immaginarmi che non sia attraente. Per nulla."

hi "Bene, un giorno o l' altro dovrai presentarmi."

show hanako basic_bashful
with charachange

ha "O-okay."

"La nostra breve conversazione cessa improvvisamente come è cominciata, ed entrambi torniamo ai nostri libri."

stop music fadeout 4.0

scene bg school_library_ss
with shorttimeskip

"Il passaggio del tempo viene marcato solo dal movimento graduale della chiazza di luce che traspare dalla finestra."

"Lentamente, i rumori delle varie prove nell' edificio si smorzano e cessano quando gli studenti cominciano a sentirsi affamati e stanchi."

"Solo pensarlo fa sì che il mio stomaco cominci ad annodarsi. Credo che sia ora di tornare."

hi "Pensi che Lilly possa essere ritornata? Credo che potrei tornare al mio dormitorio. Questa settimana mi ha piuttosto stancato."

"E non una sola parola è una bugia. Trasferirmi in una nuova scuola quando questa si sta preparando per un grosso evento è stato gravoso, per non dire di peggio."

"Posso sentire la mia testa diventare pesante mentre leggo il mio libro."

show hanako basic_smile_ss
with charaenter

ha "O-okay. Io… io credo che starò qui ancora per un po'."

"Guardando il libro di Hanako, vedo che le mancano solo poche pagine per finirlo."

"Per un momento considero l' idea di rimanere finchè non finisce, ma il mio stomaco si rigira di nuovo, emettendo un rumore gorgogliante."

hi "Certamente. Bene, me ne vado prima che si faccia buio. Ci vediamo in giro, okay?"

show hanako basic_bashful_ss
with charachange

ha "O-okay. Ci vediamo, Hisao."

hi "A dopo."

show hanako defarms_worry_ss
with charachange

ha "H-Hisao?"

hi "Hmm?"

show hanako emb_smile_ss
with charachange

ha "G-grazie. P-per aver passato del tempo con me."

play music music_dreamy fadein 0.3

"Posso vedere quanto sia stato difficile per lei pronunciare quella semplice frase. Mi lascia in sospeso per un momento."

"Così. C'è qualcuno in questa scuola che è ancora più solo di me. Forse solo è la parola sbagliata, non mi è mancata la compagnia questa prima settimana, ma sono comunque riuscito a sentirmi un po' solitario e distaccato."
    
"Forse sola è la parola sbagliata anche per Hanako, lei ha Lilly dopotutto, no?"

"Realizzo che sono rimasto lì per decisamente troppo tempo senza rispondere, e riesco a produre un sorriso perfetto, non troppo esagerato."

hi "Prego."

hi "Buonanotte, Hanako."

show hanako emb_downsmile_ss
with charachange

ha "N-notte."

scene bg school_hallway3
with locationchange

"La lascio a finire il suo libro e torno verso i dormitori e la promessa di cibo…"

stop music fadeout 3.0

scene black
with Dissolve(3.0)

return

