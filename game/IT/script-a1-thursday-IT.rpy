label it_A19:

play sound sfx_alarmclock

show bg school_dormhisao
with openeye

play music music_dreamy fadein 0.3

"Il suono di una sveglia mi trascina da un sonno disturbato nello spiacevole stato di veglia."

"Indugio sotto la coperta per alcuni minuti, raccogliendo le energie per alzarmi mentre invento scuse per non averlo già fatto."

"Davvero, non mi dispiacerebbe stare qui tutto il giorno. La scuola è sorprendentemente estenuante dopo una lunga pausa, e lo shock culturale non è ancora svanito, credo."

"Comunque, nonostante abbia l' impressione che saltare le lezioni qui sia facile, non credo che me la lascerebbero passare così liscia."

"E anche l' infermiere finirebbe sicuramente per starmi sul collo riguardo fare esercizio."
      
"Così alla fine mi alzo, inghiotto i medicinali della mattina e indosso i miei vecchi vestiti da calcio." 
   
"A causa delle mie condizioni, sono stato esonerato dal prendere parte alle lezioni di educazione fisica a Yamaku, e così non sono stato fornito di una tuta da ginnastica."

"Ne ordinerei una per coprire una simile contingenza, ma indossare la mia vecchia tenuta da calcio è piacevolmente nostalgico."

"Non posso più usarla per quello scopo, così forse in questo modo può trovare una nuova vita. Un po' come me."

label it_A19a:

#if C61

"Dopo tutto, se devo iniziare a prendermi cura di me stesso, non posso permettermi di fare lo scansafatiche. Comincerò dalle basi."

"Basi che includono tenere il resto del mio corpo in forma assieme a quel poco che posso fare per rinforzare il mio cuore."

"Forse allora potrò tornare a qualcosa che si approssima a una vita normale; o almeno qualcosa dove è meno probabile che cada morto in qualunque momento."



label it_A19b:
#if C62

"Mi sembra un po' stupido, davvero."

"Ma immagino che così posso almeno dire onestamente all' infermiere che sto facendo qualcosa per la mia salute."

"Non che io sia mai stato un gran corridore in primo luogo."

"Tentar non nuoce, suppongo."



label it_A19c:    
#End of split

show bg school_track
with locationskip

play ambient sfx_emijogging fadein 0.1

"Sono sorpreso dallo scoprire che non sono l' unico presente alla pista di atletica."

"Non solo, ma è una faccia che ho già visto prima."
  
"La ragazza dalle gambe prostetiche che mi ha abbattuto nel corridoio ieri sta agilmente correndo sulla pista, come una gazzella semi-meccanica."

"Qual era il suo nome? Era corto, ma non riesco a ricordarmelo."

"Sembra star correndo intorno a un passo discretamente rilassato, le sue gambe prostetiche ticchettanti ritmicamente sulla dura superficie della pista."

"Mi chiedo che ragione abbia per correre così presto di mattina. Forse è simile alla mia, e l' infermiere sta perseguitando la povera ragazza perchè corra proprio come sta perseguitando me."

"Io certamente non sarei qui se non fosse per la mia salute e per il suo incitamento."

"E anche considerando lo stato delle cose, è solo perchè volevo togliermi la scocciatura di mezzo presto."

"Il fatto che sarebbe stato meno probabile incontrare qualcuno che sarebbe stato testimone dei miei pietosi tentativi di tornare in forma era semplicemente un fortunato incidente."

"Me ne andrei, ma sembra che la mia precedente assalitrice mi abbia notato durante il suo ultimo giro."

"Mi saluta agitando allegramente la mano e corre fino a me."

stop music fadeout 2.0
stop ambient

show emi basic_grin_gym
with charaenter

emi_ "Buon giorno! Ti chiami Hisao, giusto?"

play music music_emi fadein 0.3

"Sorride ampiamente, apparentemente compiaciuta dall' essersi ricordata il mio nome."

show emi basic_closedgrin_gym
with charachange

emi_ "Potresti non ricordarti di me."

show emi basic_grin_gym
with charachange

emi_ "Emi? Ti ho fatto cadere nel corridoio ieri."



label it_A19i:

show emi excited_circle_gym
with charachange

emi "“Signorina Ibarazaki?”"

"Imita Misha che “imita” Shizune, non riuscendo a ottenere lo stesso tipo di sommessa cadenza nella sua voce acuta."



label it_A19j:

hi "Come potrei scordarmi una presentazione così ehmm, diretta?"
    
show emi sad_shy_gym
with charachange

"Emi ha la decenza di sembrare vagamente spiacente per un momento prima di ridacchiare."

show emi sad_grin_gym
with charachange

emi "Già, scusa per quello. Di nuovo."

hi "Hmm, bene, fintanto che non ne fai un' abitudine, immagino che sia tutto a posto."

show emi basic_happy_gym
with charachange

emi "Grande!"

"Non sono sicuro che abbia capito che stavo scherzando."

hi "Così la “spia-consultante” di cui stava parlando l' infermiere… in realtà sei tu?"

show emi basic_closedgrin_gym
with charachange

emi "Esatto!"

hi "Oh."

#blahblah, add more description around this huge dialogue-block here.

hi "Mi stavo aspettando qualcuno dallo staff di infermieri, per essere onesto."

show emi basic_confused_gym
with charachange

emi "Cosa, stai dicendo che io non sembro poter essere una spia?"

hi "No, questo è più un sollievo. Temevo che avesse qualcuno che spiava ogni mia mossa."

hi "A meno che tu non sia qui per fare proprio quello."

show emi excited_laugh_gym
with charachange

emi "No, sono qui per le mie ragioni, l' infermiere mi ha solo chiesto se avevo visto “uno studente trasferito dai capelli arruffati che sembra un tantino perso” nelle vicinanze della pista."

hi "Così perchè sei qui?"

"Emi assume una posa drammatica."

show emi basic_happy_gym
with charachange

emi "Allenamento!"

hi "Per cosa?"

show emi basic_closedhappy_gym
with charachange

emi "Atletica!"

hi "Ah, vedo. Sei nellla squadra di atletica, quindi?"

"Emi annuisce entusiasticamente."

show emi excited_proud_gym
with charachange

emi "Yep! E sono anche una dei migliori corridori!"

"E pure modesta, vedo."

show emi basic_grin_gym
with charachange

emi "Ehi, dovresti iscriverti!"

emi "E' un ottimo esercizio, sai."

"Penso che un tal grado di attività sia probabilmente fuori questione per me."

hi "Nah, non sono nemmeno sicuro che correre mi piaccia poi così tanto."

hi "E in più proprio non sono un fan degli sport organizzati, sai?"

"E' vero. Non sono mai stato nemmeno troppo serio riguardo al calcio."

"Voglio dire, correvo in giro con i miei amici e tutto il resto, ma quella era davvero l' unica ragione per cui abbia mai giocato."

"Non era per la gloria da guadagnare sul campo, questo è certo."

"Emi sembra capire quel che intendo."

show emi basic_confused_gym
with charachange

emi "Vedo, vedo. Non tanto interessato all' organizzazione e tutto il resto."
    
show emi excited_proud_gym
with charachange

emi "Ma adesso che sei qui, suppongo che correremo insieme, eh?"

hi "Cosa? Uh, certo, immagino."

"Emi sembra compiaciuta."

show emi excited_joy_gym
with charachange

emi "Non fai esercizi di riscaldamento?"

hi "Gli uomini veri non si riscaldano."

show emi basic_annoyed_gym
with charachange

emi "Oh no, dovresti sempre riscaldarti! Cattivo Hisao!"

show emi excited_proud_gym_close
with characlose

"Mi rimprovera con entusiasmo ma poi sorride e si china verso di me."

emi "Anch' io odio riscaldarmi."

show emi excited_laugh_gym_close
with charachange

"Improvvisamente ride."

emi "Cavolo, e non devo nemeno stirare le mie gambe!"

play sound sfx_gymbounce

show emi gymbounce
with charadistant

"Come per confermare la sua affermazione rimbalza su e giù un paio di volte, dando un' impressione momentanea di essere su una coppia di molle. Le sue protesi da corsa sembrano essere molto elastiche."

emi "Andiamo!"

stop music fadeout 1.0

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange

"Così partiamo entrambi lungo la pista, e immediatamente posso vedere che non stava mentendo riguardo a essere brava a correre."

"Emi si muove fluidamente, lanciandosi nella corsa con una specie di selvaggio abbandono."

"Io mi trovo più a concentrarmi sul correre decentemente."

#if C61


label it_A19d:

"Mani aperte, giusto?"

"E qualcosa riguardo al toccare con le punte dei piedi, invece che con i talloni…"

"Cerco di adeguare il mio passo a quello di Emi, ma è piuttosto difficile."

"A quanto pare non sono molto bravo."

"Forse Emi potrebbe aiutarmi una volta o l' altra."



label it_A19e:

#if C62

"Francamente, non ricordo se ci sia una forma particolare per correre, ma non posso fare a meno di sentirmi come se stessi sbagliando, in qualche modo."

"Mi sento goffo comparato ad Emi, che non sembra mai perdere il passo."

"…"

"Non credo più di voler continuare."



label it_A19f:

"Oggi davvero non mi sento in grado di percorrere più di un paio di giri, e piuttosto presto rallento fino a camminare."

scene bg school_track_on
with Dissolve(4.0)

"Emi continua a correre, e non sembra notare che mi sono fermato finchè non mi oltrepassa per la seconda volta."

stop ambient

"Slitta in una rapida frenata, respirando normalmente in contrasto con il mio comportamento piuttosto ansimante."

play music music_emi fadein 0.3

show emi basic_confused_gym
with charamoveinleft

emi "Già finito?"

"Chino la testa con aria afflitta."

hi "Heh, già."

hi "Ora non sono davvero in buona forma."

show emi basic_grin_gym
with charachange

"Emi annuisce, e poi di nuovo mi fa un gran sorriso."

"Sembra che sorrida molto spesso."

emi "Bè, la cosa importante è che tu abbia cominciato, giusto?"

show emi excited_amused_gym
with charachange

emi "La prossima volta, devi solo cercare di resistere più a lungo, e poi più a lungo, e più a lungo, e alla fine sarai bravissimo!"

hi "Lo terrò a mente."

hi "Ma adesso penso che andrò a prepararmi per le lezioni."

hi "Non dovresti farlo anche tu?"

"Emi scrolla le spalle senza sembrare preoccupata."

show emi basic_grin_gym
with charachange

emi "Nah, ho tempo in abbondanza."

"Noto che non porta un orologio."

hi "Sei sicura?"

"Un' altra noncurante scollata di spalle."

emi "Non proprio… ma devo terminare la mia routine!"

show emi basic_closedgrin_gym
with charachange

emi "Arrivederci, Hisao!"

hi "Uh, già. Ci vediamo."

stop music fadeout 2.0

hide emi
with easeoutleft


label it_A19g:

#if C61
"Non sono certo se l' esperimento di stamattina sia stato un successo o un fallimento, ma ammetterò di sentirmi leggermente soddisfatto di essere uscito questa mattina."

"E come ha detto Emi, devo solo insistere per migliorare, giusto?"

"La pratica rende perfetti, o qualcosa del genere."

"E' bello almeno sentirmi come se avessi preso una qualche parvenza di controllo sulla mia salute."

"Dovrò cercare di insistere."



label it_A19h:
#if C62

"A parte sentirmi più stanco di prima, non credo di avere ottenuto niente oggi."

"Sono talmente fuori forma che è imbarazzante."

"L' intera faccenda potrebbe essere stata una perdita di tempo. Troverò un' alternativa."
    


#**********************************

label it_A20:

scene bg school_dormext_half
with locationskip

"Torno ai dormitori per lavarmi e cambiarmi nella mia uniforme, cercando di resistere alla tentazione di fare una doccia veramente lunga e calda."

"Sono stanco per tutto il correre, così voglio solo rilassarmi, ma non voglio rompere la mia abitudine in lenta formazione di arrivare a scuola prima del trambusto mattutino."

scene bg school_dormbathroom
show steam
show steam2
with shorttimeskip

"Dopo una doccia comunque lunga, mi asciugo ed esco dal box per vestirmi."

show kenji silhouette_naked behind steam
with charaenter

"Senza preavviso, un' ombra appare tra il vapore, profilandosi minacciosa e irradiando intento maligno. Irrompe attraverso la nebbia."

play music music_kenji fadein 0.3

hide steam
hide steam2
show kenji neutral_naked
show steam as newsteam behind kenji
show steam2 as newsteam2 behind kenji
with charachange

ke "Come va?"

hi "Che stai facendo qui? Che diavolo, mi hai spaventato! Qual è il tuo problema?"

show kenji tsun_naked
with charachange

ke "Dovrei chiedertelo io. Ti ho cercato dappertutto, amico."

hi "Che vuoi dire con “dappertutto?”"

"Voglio chiedergli se mi ha cercato in giro così com'è, nudo come un verme, ma trattengo la lingua."

"Finalmente mi accorgo di essere ancora nudo anche io e rapidamente sollevo la mia camicia di fronte a me, ma Kenji non sembra accorgersi di niente."

"I suoi occhiali sono annebbiati. Ma allora, perchè non li pulisce? La sua vista è talmente cattiva che è come se stesse perpetuamente guardando attraverso una nebbia?"

ke "Lo sai, la tua stanza, e… Già, e basta. Ehi, voglio dire, mi sono comunque dovuto alzare, però. Vabbè. Non è importante. Puoi prestarmi un po' di soldi?"

show kenji neutral_naked
with charachange

"Fa una faccia innocente e distoglie lo sguardo, cercando molto intentamente di sembrare molto disinvolto. Non funziona; è trasparente quanto i suoi occhiali grandi come finestre."

"Parlare di cose normali in questo modo, senza avere nulla addosso, è imbarazzante."

"A dire il vero, in qualche modo è anche più imbarazzante essere nudo di fronte a qualcuno che non può vedere che sono nudo. Per non dir nulla del fatto che anche lui è nudo."

"Cerco di liberarmi della sensazione, con scarso successo."

hi "Soldi? Certo."

show kenji happy_naked
hide newsteam #lessening the processor load a little
with charachange

ke "Fantastico."

hi "Aspetta, perchè ne hai bisogno?"

show kenji tsun_naked
with charachange

ke "Ehhhh…"

show kenji neutral_naked
with charachange

ke "Non puoi solo darmeli perchè ho avuto la buona grazia di non frugare nelle tue tasche mentre eri nella doccia? Avrei potuto farlo, ma ho esercitato ritegno. E alla fine, non è il pensiero che conta? Dai, sii un amico."

"Questo non ha senso. Se è il pensiero che conta, dovrei trattenere il pagamento, dato she i suoi pensieri erano così chiaramente impuri e le sue intenzioni sono probabilmente ancora più sinistre dato che non può dirmi quali sono. E così gli dico."

show kenji tsun_naked
with charachange

ke "Sono offeso amico, ma se quello è il tuo gioco, allora bene, immagino di non aver scelta. Voglio ordinare una pizza, e ho già la maggior parte del suo costo. Ho bisogno del tuo aiuto per il resto."

hi "E anch' io ricevo una fetta di quella pizza, giusto?"

ke "No."

hi "Ma dici sul serio?"

show kenji neutral_naked
with charachange

ke "Già. Te ne darei un po', ma tu devi andare a lezione, non hai tempo per mangiare una pizza."

hi "E che mi dici di te?!"

ke "Io non vado a lezione, devo aspettare che arrivi la pizza e pagare il tizio. E poi mangiarla. Non è facile. Bisogna ottenere la pizza di nascosto. Se non ci si riesce, tutti ti vedono. E vedono la pizza. E ti chiedono una fetta."

show kenji tsun_naked
with charachange

ke "E' un mondo duro là fuori. Tutti vogliono una fetta. Poi tu rimani senza pizza in un mondo impietoso. E' già successo prima, è così che lo so."

ke "Ogni giorno, pianifico la mia vendetta, così quando le persone che mi hanno fatto torto ordinano una pizza, sarò lì. Sempre vigile!"

"Kenji assume una posa drammatica, completamente senza ironia."

show kenji neutral_naked
with charachange

ke "Comunque sì, mi servono solo tipo 400 yen. Per favore! Sei la mia unica speranza! Non posso uscire e comprarmi la mia pizza, è troppo lontano!"

ke "Cerco di non uscire a meno che non sia assolutamente necessario. Lascia che ti racconti cos'è successo l' ultima volta che sono uscito senza pianificare in anticipo."

ke "Ero fuori. Non ricordo cosa stavo facendo. Qualcosa. Ero in piedi? Forse stavo chiedendomi come ero arrivato lì."

show kenji tsun_naked
with charachange

ke "E poi, dal nulla, è capitato."

ke "Come un fulmine che spezza il cielo, come spezzi un tramezzino in due parti uguali per renderlo più maneggevole da tenere e mangiare, un uccello mi ha cagato in testa."

ke "E' stato il secondo momento più scioccante della mia vita."

hi "Qual è stato il primo?"

"Mi ignora e continua. Voglio prenderlo e scuoterlo. Sta solo cercando di mantenere l' iniziativa? Crederò a quello, anche se è più probabile che non mi abbia proprio sentito."

ke "E' stato come nelle sigle di certi anime, sai come c'è sempre una parte dove il tizio principale sta combattendo il suo rivale, e volano uno contro l' altro e incrociano le spade e ci sono tipo, grandi aure colorate e drammatiche e dello zoom?"

show kenji neutral_naked
with charachange

ke "E' stato così, ma con della popò."

hi "Okay."

show kenji happy_naked
with charachange

ke "Così insomma, ho bisogno di un po' di soldi. Per favore? Non lasciarmi nelle peste, amico. Mi bastano solo tipo 1000 yen."

hi "Credevo che fossero 400."

ke "Okay."

hi "Cosa?"

ke "Te li renderò, giuro."

hi "Sarà meglio, prendere a prestito significa quello."

show kenji neutral_naked
with charachange

ke "Non so quando sarò in grado di ripagarti."

hi "Hai una settimana."

show kenji tsun_naked
with charachange

ke "Aaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhggggggggggghhhhhhhh……"

"Kenji fa una smorfia di dolore e un rumore simile a una mucca morente, cosa particolarmente inquietante dato che la sua bacchetta sta dirigendo liberamente l' orchestra."

ke "Non dovresti essere così pignolo con i soldi tra fratelli in armi, amico. Gli uomini sono già messi male adesso. Lo sapevi che le pornostar uomini guadagnano solo circa la metà delle pornostar donne?"

hi "Quello non significa niente se non sei una pornostar."

ke "Così forse sono una pornostar, come attività secondaria, e cerco di far quadrare i conti mentre combatto contro l' agenda femminista, e tu non mi puoi nemmeno lasciare le tue briciole, bastardo. Nessuno capisce. Nessuno."

"Le femministe non sarebbero contro la pornografia in primo luogo?"

hi "Di nuovo questa roba sull' agenda femminista?"

ke "Questa roba è importante. Posso vedere che a te non frega niente, ma è un problema serio, qui. Le femministe… sono un nemico pericoloso, non c'è dubbio."

ke "Prendile alla leggera, e ti svegli la mattina con un coltello nella schiena, bam! Senza preavviso!"

hi "Come fai a svegliarti la mattina se qualcuno ti ha accoltellato nel sonno?"

show kenji happy_naked
with charachange

ke "Le donne sono pessime ad accoltellare."

hi "Credevo che avessi appena detto di non prenderle alla leggera."

show kenji neutral_naked
with charachange

ke "Bè, volevo dire di non prenderle alla leggera per le cose grosse."

ke "Individualmente non sono una minaccia, ma se ci fosse una specie di guerra, tipo una grossa guerra, con gli uomini da una parte, e le forze femministe dall' altra parte, sarebbe piuttosto brutta."

show kenji tsun_naked
with charachange

ke "E quel giorno verrà, quando le femministe usciranno dal loro quartier generale centrale top secret mondiale femminista, e diranno “Adesso è l' ora, figli di puttana!”"

hi "Sei ridicolo, non esiste un grande edificio quartier generale mondiale femminista, e dove lo nasconderebbero poi?"

hi "Voglio dire, dovrebbe essere enorme, non potresti nasconderlo sulla terra, qualcuno si accorgerebbe di una grande fortezza piena solo di donne."

show kenji happy_naked
with charachange

ke "Chi ha detto che era sulla terra?"

"Smetto di guardare Kenji e inizio a far pratica di smorfie di disapprovazione in uno specchio così da poter figurare quale tipo possa esprimere al meglio le mie emozioni. Da questa distanza non mi può comunque vedere."

"Il che, sfortunatamente, significa che continua solo a inveire senza alcun riguardo per buon senso o sensibilità."

show kenji tsun_naked
with charachange

ke "Già, c'è una guerra in corso. Una guerra di cui non molti sono al corrente, ma è una grande guerra che un giorno esploderà, e ingloberà tutto il mondo conosciuto."

ke "Allora dovremo scegliere da che parte stare. Dovremo farci valere. Infatti, sta avvenendo già adesso."

ke "Immagina, il campo di battaglia insanguinato. Un brutale conflitto senza fine."

ke "Quasi ho ceduto, quando ho pensato che questa causa fosse una sciocchezza… Quando mi sono stancato della desolazione della nostra battaglia…"

ke "Quando ho confuso quella volta che è andata via la luce per un raid femminista e ho pensato che la fine fosse vicina…"

ke "Ma poi ho capito che se avessi ceduto, sarebbe tutto finito, e ho pensato tipo, “wow” e ho capito che dovevo fare sul serio. Perchè sono l' ultimo uomo sano di mente in un mondo folle. E' una questione di dovere."

hi "Deve essere un movimento piuttosto misero se tutto pende su un tizio nudo che sproloquia in un bagno a un altro tizio nudo."

show kenji neutral_naked
with charachange

ke "Così posso avere i soldi?"

"E' tra me e l' uscita, sta diventando freddo perchè sono ancora nudo, e voglio andare a scuola, così accetto di prestargli i soldi."

show kenji happy_naked
with charachange

ke "Fantastico. Grazie, tizio. Dovremmo andare al bowling più tardi."

hi "Bowling?"

ke "Già, è lo sport finale. Inoltre quasi non ci sono donne che lo praticano, rendendolo anche lo sport più virile."

ke "Dici che dovrei indossare la mia camicia rosa da bowling con scarpe in tinta o quella verde pastello con decorazioni floreali?"

hi "Esistono vestiti da bowling?"

show kenji neutral_naked
with charachange

ke "Forse."

hi "Comunque, farai meglio a ripagarmi."

ke "Posso ripagarti in roba, giusto?"

"Non ho il tempo per chiedergli di elaborare su cosa quello voglia dire."

hi "Non lo so. Devo andare in classe, e tu sei un po' tra i piedi."

show kenji tsun_naked
with charachange

ke "Oh. Scusa. Già, non voglio farti perdere tempo, e ho qualcosa da fare anche io. L' ora è giunta."

hi "L' ora per cosa?"

show kenji happy_naked
with charachange

ke "Mi piace solo dirlo."

ke "Okay, adesso l' ora è davvero giunta."

hi "Per cosa?"

show kenji tsun_naked
with charachange

ke "Devo usare il bagno. Esci."

hi "Stavo per farlo! E che vuol dire quello? E' un bagno grande."

ke "E allora? Devo essere solo o non ce la faccio. La pressione…"

hi "Okay. E se entra qualcun altro?"

ke "…"

ke "Penserò a qualcosa."

"Dirigo contro di lui la smorfia su cui mi sono esercitato che sembra un po' sciocca riflessa nei suoi occhiali."

"Lui o non se ne accorge o non la vede, comunque, così mi vesto e torno di corsa nella mia stanza, sentendomi come se fosse passata un' eternità da quando mi sono svegliato."

stop music fadeout 2.0

scene bg school_dormhisao
with locationskip

"Questo è tempo perso per sempre. Glie la farò pagare in qualche modo."

"Ma adesso, devo andare in classe."



#*****************************************

label it_A21:    

scene bg school_scienceroom
with locationskip

play music music_dreamy fadein 0.3

"Sono il primo a entrare in classe oggi, anche se penso di essere un po' troppo in anticipo. D' altra parte, starmene seduto qui solo per venti minuti batte dover soffrire per gli stessi minuti con Kenji."

"La combinazione di fatica, frustrazione e noia comincia a farmi sentire molto stanco."

"Per un secondo cado vittima di un colpo di sonno, svegliandomi quando la mia testa picchia sul piano del mio banco."

"Strofinandomi la fronte, capisco che questa è una ragione buona quanto qualunque altra per restare sveglio per ora e smettere di venire il aula così presto da ora in poi."

"Alla fine, sento un rumore picchiettante fuori nel corridoio, e l' alta figura di Lilly compare alla porta. Lei non è in questa classe, così deve avere qualche altro motivo. Forse sta cercando Hanako."

"Lilly si ferma alla porta, con aria esitante come se fosse un vampiro che non può entrare se non viene invitata. Considero l' idea di farlo perchè sembra piuttosto sola lì in piedi."

"Entra di sua volontà però, dopo avere sistemato la sua gonna e il colletto dell' uniforme come se fosse importante sembrare perfetti mentre si entra nella nostra classe." 

show lilly cane_concerned at left
with charamoveinleft

li "Chiedo scusa."

"Fa un appello all' aula silenziosa con una voce inquisitiva e delicata. Capisco che il silenzio potrebbe snervarla a causa della sua cecità così lo spezzo."

hi "Buongiorno, Lilly."

show lilly cane_surprised at left
with charachange

show lilly cane_surprised
show bg school_scienceroom at bgright
with charamove

li "Hisao? Buongiorno. Non ti ho sentito entrare."

"Mi chiedo se pensa che sia sospetto che non le abbia detto nulla prima. E' probabile. Se ora dovessi dire una bugia troppo grossa, sarebbe la mia fine."

hi "Beh, ero già qui, solo addormentato fino a ora."

show lilly cane_listen
with charachange

li "Oh. Hai per caso visto Hanako oggi?"

hi "No, pare che lei arrivi solo appena prima che suoni la campana… o più tardi. Vuoi che le riferisca qualcosa da parte tua?"

show lilly cane_weaksmile
with charachange

li "No, non importa. E' strano, ma credo che siamo le uniche due persone in tutta la scuola in questo momento. Non ho sentito nessun altro mentre venivo qui."

hi "Non avrei dovuto alzarmi così presto oggi, immagino."

show lilly cane_smile
with charachange

li "Ti stai rimproverando per aver fatto qualcosa che anche gli altri dovrebbero fare? La puntualità è un' ottima cosa. O almeno, io la penso così."

show lilly cane_concerned
with charachange

li "Oggi sarà una mattina molto impegnativa. Il festival comincerà presto, e oggi è la scadenza per registrare i progetti di classe, dar resoconto del bilancio, e tutta l' altra burocrazia ufficiale."

show lilly cane_weaksmile
with charachange

li "Potrebbe darsi che tutti stiano cercando di completare i moduli necessari all' ultimo minuto. Forse è per quello che oggi è così tranquillo."

show lilly cane_surprised
with charachange

mi "Ciao~ ciao~!"

show shizu behind_blank at offscreenright
show misha hips_grin at offscreenright
with None

show lilly cane_surprised at left
show misha hips_grin
show shizu behind_blank at right
show bg school_scienceroom at bgleft
with charamove

hide misha
show misha hips_grin behind shizu
with None

"Misha appare nella stanza con Shizune come se avesse ricevuto un segnale, urlando a un volume che fa visibilmente sussultare Lilly."

show misha hips_smile
with charachange

mi "Ciao, Hicchan~!"

hi "Ciao."

show shizu behind_smile at right
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Oh guarda, è la rappresentante di classe~! Salve~!"

show lilly cane_smile at left
with charachange

"Lilly sorride, probabilmente divertita dall' uso di Misha - o Shizune - della parola “guarda.”"

show lilly cane_smile at left
with charachange

li "Buon giorno."

show shizu adjust_smug at right
with charachange

shi "…"

show misha cross_smile
with charachange

mi "Certamente, non è la rappresentante di questa classe, giusto, giusto~?"

show lilly cane_weaksmile at left
with charachange

li "Non lo sono."

"Lilly sembra un po' più guardinga nelle sue risposte a Shizune di quanto lo fosse con me l' altro giorno. Direi che davvero non vanno affatto d' accordo."

"Poi comprendo che Lilly potrebbe effettivamente non sapere che Shizune è presente e che sta cercando di capire se c'è o no, per sapere con chi sta parlando."

"Per quel che ne sa, sta parlando con Misha, ma sapendo che lei e Shizune sono praticamente inseparabili, potrebbe aspettarsi che sia Shizune quella che in realtà “parla”."

"Accidenti, se è complicato. Decido di aiutare Lilly, per la mia pace mentale più che per qualunque altra cosa."

hi "Sei in anticipo, Shizune."

show shizu basic_angry at right
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Tu eri ancora più in anticipo di noi!"

"Misha gonfia le guance, irritata. Perchè si sta arrabbiando? Sente anche emozioni per conto di Shizune?"

"Non è così strano, però, che Shizune non abbia gradito il mio piccolo commento. E' vero, ero qui prima di loro, così il mio dire qualcosa del genere potrebbe decisamente essere male interpretato in molti modi."

"Specialmente da Shizune, che non ha il vantaggio di sentire il tono di voce per valutare l' intento."

"Prima che possa iniziare a calcolare se dovrei scusarmi o no, Shizune è già passata oltre."

show shizu adjust_smug at right
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Capoclasse~! E' un bene che sia qui~! Dobbiamo parlare."

show shizu behind_frown at right
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Il festival cominicia tra tre giorni, giusto? Tutte le altre classi hanno già consegnato i resoconti di bilancio previsti per i loro progetti! Persino i primi anni! Eccetto lei~!"

show misha cross_laugh
with charachange

mi "Wahaha~!"

show lilly cane_surprised at left
with charachange

li "C'è ancora tempo per consegnarlo, non è vero?"

stop music fadeout 2.0

show shizu cross_angry at right
with charachange

shi "…"

show misha cross_frown
with charachange

mi "Oggi! La scadenza è oggi! Certamente si sta prendendo il suo tempo, no? Se fosse stato per me, avrei già avuto tutta la burocrazia necessaria pronta giorni fa, ma qualcuno~! ha dovuto dire “la scadenza, per favore estendetela~!”"

show lilly cane_displeased at left
with charachange

li "Sì, sono stata io. Pianificare qualcosa su questa scala non è un affare da poco, e una settimana è un periodo troppo breve per aspettarsi che un' intera classe elabori completamente una questione così complessa."

show shizu adjust_angry at right
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Vuole sapere cos'è più difficile di distribuire i fondi per il progetto di una classe? Trattare la stessa faccenda per tutte le classi della scuola e altro~! E quella che lo fa sono “io!”"

"Misha si mette le mani sulle anche e si raddrizza. Wow, sta veramente entrando nella parte. Lilly non sembra essere molto divertita, però."

hi "Ehi, Shizune, non sei un po' troppo severa con lei? Rimane ancora un intero giorno di tempo."

show lilly cane_weaksmile at left
with charachange

li "Per favore, Hisao. Va tutto bene."

"Lilly sembra felice che io stia prendendo le sue parti, ma un po' timorosa che io possa pensare che lei non sappia prendersi cura di se stessa."

show lilly cane_listen at left
with charachange

li "Se questo riguarda il bilancio, allora sono delusa che pensi che lo abbia dimenticato. Capisco quanto sia importante."

show shizu behind_frustrated at right
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Allora~! Posso averlo, per favore?"

hi "Shizune, potrebbe non averlo con lei in questo preciso momento."

#edit this segment for Lilly to be less defensive and show a bit of fangs? Though making her bitchy might weaken her character, as that would make Shizune a big weak spot for her, that could throw her off balance. also keep the incoming CG in mind, as in that they both have massive battle auras and whatnot 

# touchup for now - Suriko

show lilly cane_displeased at left
with charachange

li "Non è qui adesso. Ho chiesto a due studenti di prendersene cura per me. Studenti dalla mia classe."

"Con mia grande sorpresa, enfatizza l' ultima frase. Sa degli sforzi di Shizune e Misha per farmi entrare nel consiglio studentesco?"

"Immagino che la voce debba essersi sparsa, così ora mi sta usando come uno strumento contro Shizune. Oh, fantastico…"

show shizu cross_angry at right
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Era la sua responsabilità~! Un resoconto di bilancio non è qualcosa che si dovrebbe solo delegare; come capoclasse, è il suo lavoro essere aggiornata su tutto! Trascurare in questo modo le procedure è davvero terribile~!"

show lilly cane_listen at left
with charachange

li "L' hanno completato, dato che erano in grado di farlo, ma gli studenti si sono ammalati recentemente, così non sono potuti venire a scuola a consegnarmelo. Se vuole, mi scuserò da parte loro per essere malati."

show misha hips_grin
with charachange

mi "Okay~!"

"Anche se Misha manca completamente la punzecchiatura di Lilly, non è così per Shizune, che sembra divisa tra essere offesa dall' audacia di Lilly e saltare di gioia al prospetto di una sfida."

show shizu behind_frown at right
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Lilly, non vivono qui a scuola? E' una passeggiata di cinque minuti, sai~."

mi "Cosa potrebbero concepibilmente avere che gli impedisce di prendersi cinque minuti dalle loro vite piene di impegni… per consegnare qualcosa che avrà un effetto sulla soddisfazione della loro intera classe?"

show shizu adjust_angry at right
with charachange

"Lilly apre bocca per dire qualcosa, ma Shizune chiude la distanza tra di loro e inizia a segnare furiosamente, agitando le mani come un direttore d' orchestra."

"Misha fa del suo meglio per trasmettere la stessa passione, ma non sembra riuscire a perdere il suo normale tono allegro. Il risultato è interessante e moderatamente surreale."

shi "…"

show misha cross_frown
with charachange

mi "E cos'è questa attitudine~? Ho detto che non è qualcosa che dovresti delegare; sei la rappresentante di classe o no?"

show misha hips_frown
with charachange

mi "Dimmi i nomi di quei due studenti, dovrebbero avere il tuo lavoro se tu non sai nemmeno trattare qualcosa di così semplice da sola."

show lilly cane_displeased at left
with charachange

li "Un modulo non copre l' entità di quel che normalmente devo trattare."

"Il tono di Lilly sta diventando leggermente impaziente, ma sta facendo un valido sforzo per non lasciar vedere a Shizune quanto si stia turbando. Sta giocando le sue carte difensivamente."

"Shizune, d' altra parte, stringe allegramente le dita intorno al bordo dei suoi occhiali, sapendo che Lilly non può nè sentire nè vedere quanto è eccitata."

show shizu adjust_smug at right
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Certamente, fai talmente tanto, capoclasse~! Deve essere talmente difficile essere te~!"

show lilly cane_listen at left
with charachange

"Lilly stringe le labbra alle parole di Misha, chiaramente capendo l' intento che c'è dietro anche se Misha le pronuncia senza la minima traccia del sarcasmo che era inteso in esse."

"Shizune e Lilly non si piacciono, quello è chiaro, ma questo sembra un po' eccessivo. Sembra che Lilly ne abbia avuto abbastanza e sia pronta a rispondere per le rime."

play music music_tension

$ wdt_off(False)

scene black
with Dissolve(0.2)

show showdown_lilly_slice at Position(xanchor=0.0, xpos=1.0, yalign=0.0)
show showdown_shizu_slice at Position(xanchor=1.0, xpos=0.0, yalign=1.0)
with None

play sound sfx_draw
show showdown_lilly_slice at Position(xalign=0.0, yalign=0.0)
with slice_in

with Pause(0.2)

play sound sfx_draw
show showdown_shizu_slice at Position(xalign=1.0, yalign=1.0)
with slice_in

with Pause(0.2)

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 3.0, color="#FFF")


play sound sfx_slide2
show ev showdown_large at Zoom((800,600),(0, 0, 2400, 1800),(280, 100, 800, 600),.2)
with None

window show

# No ellipses during this sequence; it kills the dynamics of the exchange

li "A dire il vero stavo discutendo il resoconto di bilancio giusto prima che tu arrivassi."

li "Devi essere ricca di talento per aver concluso tutti i tuoi doveri pertinenti al consiglio studentesco talmente presto da potermi venire a cercare per assicurarti che io non dimentichi i miei."

play sound sfx_slide
show ev showdown_large at Pan((280,100),(1400,160),0.2, time_warp=_ease_time_warp)
with None

mi "Mi stai accusando di essere una scansafatiche? Sembra che tu mi stia confondendo con te stessa~!"

play sound sfx_slide2
show ev showdown_large at Pan((1400,160),(280,100),0.2, time_warp=_ease_time_warp)
with None

li "Non credo. Quella sarebbe una cosa molto difficile per me; compararmi con te."


play sound sfx_slide2
show ev showdown_large at Pan((280,100),(1400,160),0.2, time_warp=_ease_time_warp)
with None

mi "Hai ragione, la differenza tra di noi è come il cielo e l' inferno."

play sound sfx_slide
show ev showdown_large at Pan((1400,160),(280,100),0.2, time_warp=_ease_time_warp)
with None

li "E non è difficile indovinare quale dei due tu possa rappresentare."

$ _window = False

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 1.5, color="#FFF")

window show

"L' aria tra loro si distorce per il calore della loro inimicizia. Beh, non veramente. Non possono più nasconderla, però. Pare che perfino Misha stia iniziando a capire la vera natura di questa conversazione."

stop music fadeout 5.0

scene bg school_scienceroom at bgleft
show lilly cane_listen at left
show misha perky_confused
show shizu basic_angry at right
with flash

shi "…"

show misha sign_confused
with charachange

mi "Hicchan~! Anche tu, non fare lo scansafatiche~!"

hi "Di che stai parlando?"

show shizu basic_frown at right
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Non stai prendendo parte al festival, Hicchan? Sì, non è vero? Quindi~! Spero che tu abbia intenzione di fare molto di più di questa persona per assicurarti che vada tutto liscio~!"

label it_choiceA21:
menu:
    with menueffect
    
    "Non capisco perchè improvvisamente Shizune si stia arrabbiando con me."
    
    "Non coinvolgermi! Ho fatto la mia parte!":
        return m1

    "Ehi, calma. Dà un po' di tregua a me e a Lilly…":
        return m2
        
label it_A21a:

hi "Perchè sto venendo coinvolto, poi? Ho fatto più che abbastanza, penso."

hi "Se sei arrabbiata con Lilly, quello non ha nulla a che vedere con me."

show lilly cane_reminisce at left
with charachange

li "Ora, aspetta un momento… stai implicando che il presidente ha più ragioni di rimproverare me di te?"

"Ah cavoli, penso che avrei potuto esprimermi meglio."

hi "No, su quello non saprei però… voglio dire…"

show shizu behind_frown at right
with charachange

shi "…"

show misha perky_confused
with charachange

mi "Cosa stai dicendo, Hicchan?"

hi "E' solo che non penso affatto che sia giusto che tu dica questo, visto che vi ho aiutato."

"L' umore è cambiato. Adesso è come la resa dei conti tra due pistoleri.  Bè, lo era anche prima, ma stavolta l' attenzione di Shizune è concentrata su di me."

"E lo stesso vale per quella di Lilly, anche se rimane in silenzio. Temo di averla inavvertitamente fatta infuriare."

show shizu cross_angry at right
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Stai dicendo che mi sbaglio?"

"Che situazione pericolosa."

hi "E' troppo presto per discutere con te. …Sì, penso che sia ingiusto che tu mi dia addosso."

show shizu behind_frustrated at right
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Hicchan, tu vuoi troppo~! Ma~! Hai le tue ragioni. Okay, okay okay~! Tu non sei pigro, Hicchan."

show misha hips_laugh
with charachange

mi "Hahaha~!"

"Shizune spinge su i suoi occhiali col pollice, quasi in approvazione."

show shizu adjust_happy at right
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Così va bene! Se non sei inutile, non dovresti lasciare che nessuno dica che lo sei~! Ma la prossima volta che lo dico, sarà davvero perchè mi stai deludendo come la signorina capoclasse, così non lasciare che questo ti dia alla testa!"

show lilly cane_displeased at left
with charachange

"Lilly riceve la critica in silenzio, un' espressione velenosa congelata sul suo viso."

show misha hips_smile
with charachange

mi "Capoclasse~! Shicchan dice: “Non si dimentichi di quel resoconto, per favore~!”"

li "Non lo farò."

show lilly cane_listen at left
with charachange

li "E' tutto?"

show misha hips_grin
with charachange

mi "Yup~!"

li "Allora, buon giorno a tutti voi."

"Se la sua voce fosse più tangibile, taglierebbe l' aria dell' aula in due."

hide lilly
with charaexit

"Lilly lascia la stanza, comprensibilmente di malumore ma comunque riuscendo a essere padrona di sè e calma come sempre."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with charamove

hi "Shizune, oggi hai davvero esagerato un po'."

show misha perky_smile at twoleft
with charachange

mi "E' vero, Shicchan, solo un pò~."

"Se mi aspettavo che Shizune ammettesse malvolentieri che ho ragione anche su questo, penso che mi stessi aspettando troppo. Lei non risponde."

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha cross_laugh at twoleft
with charachange

mi "Hahaha~! Shicchan pensa che dovresti farti gli affari tuoi."

show misha hips_smile at twoleft
with charachange

mi "Hicchan, abbiamo alcune cose dell' ultimo minuto di cui prenderci cura prima delle lezioni~! Potremmo fare tardi, così~! Puoi coprire per noi, per favore?"

hi "Sì."

show misha cross_grin at twoleft
with charachange

mi "Perfetto~! Yay~! Okay~! Grazie, Hicchan!"

hide misha
hide shizu
with charaexit

"Escono anche se mancano solo dieci minuti prima che la campana suoni, segnalando l' inizio delle lezioni."



label it_A21b:

hi "Ehi, sono quello nuovo, ricordi?"

hi "Non è che avrei potuto fare molto, anche se avessi voluto."

show lilly cane_displeased at left
with charachange

li "E' vero, non dovresti aspettarti che uno studente trasferito si butti a capofitto durante la sua prima settimana."
   
"E' stranamente confortante che Lilly prenda le mie parti così decido di sostenerla a mia volta."

hi "Già, non sei ragionevole con nessuno di noi due."

show shizu behind_frustrated at right
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Scuse, tutte scuse. La signorina capoclasse ha avuto abbondanza di tempo per occuparsi del suo resoconto."

mi "E ti abbiamo ripetutamente offerto una posizione per aiutare col lavoro del consiglio studentesco, ma ti sei rifiutato di prenderti l' impegno di rendere il festival un successo."

hi "Già, ma come ho detto allora, non sono sicuro di…"

"Non ho tempo da perdere ora; non importa quel che faccio, vorrà dire essere coinvolto in uno scontro con Shizune, e quello è ciò che lei vuole."

hi "Lasciamo perdere. Scordatevelo."


label it_A21c:

"Gli giro la schiena."

hide shizu
hide misha
with charaexit

show lilly cane_displeased
show bg school_scienceroom at bgright
with charamove

hi "Lilly, le lezioni stanno per cominciare, quindi possiamo parlare più tardi. Dirò ad Hanako che la stavi cercando."

"Riesco a percepire che Shizune si congela. Forse questa è la prima volta che è mai stata ignorata in modo così brusco."

show lilly cane_smile
with charachange

li "Grazie, Hisao. Adesso vado, allora."

"Mi concede il sorriso più dolce che ho visto in tutta la settimana, e gira sui tacchi per andarsene."

hide lilly
with charaexit

"Appena Lilly è uscita dalla porta, improvvisamente inizio a sentirmi riluttante riguardo a girarmi e confrontare Shizune."

"Posso sentire i suoi occhi bruciare sulla mia schiena, e non riesco a decidermi a guardarla. Deve essere furiosa. Continuo ad aspettarmi che Misha dica qualcosa per alleviare la tensione, ma è davvero sperare in troppo."

"Alla fine, torno al mio posto e ascolto il suono dei passi di Shizune quando marcia fuori dalla stanza. Non ritorna se non pochi minuti prima dell' inizio della lezione."



label it_A21d:

hide shizu
hide misha
hide lilly
with charaexit

"Gli giro la schiena."

"Torno al mio posto e fingo di non sentire il finale del litigio tra Lilly e Shizune."

"Alla fine, Lilly lascia la nostra aula e Shizune e Misha si siedono, senza parlarmi."

"Posso sentire gli occhi di Shizune bruciare sulla mia schiena. Probabilmente è arrabbiata, ma io lo sono altrettanto con lei."

"Non capisco perchè mi abbia dovuto coinvolgere nel litigio."



#*****************************

label it_A22:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_normal fadein 0.3

"Hanako non si presenta affatto alla lezione del mattino, lasciando il suo posto vuoto e solitario sul retro dell' aula."

"Devo dirle che Lilly la stava cercando se la vedo più tardi."

"Dopo gli eventi di stamattina, la lezione è piuttosto noiosa al confronto. Giro pigramente le pagine del mio libro di testo."

"Ultimamente abbiamo coperto la stessa quantità di pagine ogni giorno, quindi leggere avanti è più o meno come darmi un' anteprima su cosa tratterà la lezione di domani."

"L' orologio al fronte della stanza sembra incredibilmente rumoroso. L' insegnante non ha detto nulla per più di sette minuti, optando invece per coprire la lavagna in file e file di equazioni copiate direttamente dal libro."

"Il ritmico impatto del gesso sulla lavagna sembra sincronizzarsi perfettamente col ticchettio dell' orologio."

show misha cross_smile_close at offscreenleft
with None

show misha cross_smile_close at Position(xpos=0.1)
show bg school_scienceroom
with charamove

$ renpy.music.set_volume(0.4,1.0)

"Inizio a copiare le equazioni tanto per passare il tempo, senza accorgermi della testa di Misha che fa capolino al di sopra della mia spalla finchè quasi non mi è addosso."

hi "Che stai facendo?"

"Cerco di raggiungere un equilibrio tra parlare abbastanza piano da non attrarre attenzione ma abbastanza forte da attrarre la sua."

show misha cross_grin_close at Position(xpos=0.1)
with charachange

show misha cross_grin_close at twoleft
show bg school_scienceroom at bgright
with charamove

mi "Che stai facendo, Hicchan~?"

"Il panico mi assale quando Misha inizia a parlare al suo normale volume."

"Balbetto una risposta affrettata, continuando a tenere la mia voce bassa a dispetto del fatto che lei abbia appena cancellato qualunque speranza di essere discreto che avrei potuto avere."

hi "Sto copiando quella roba, che stai facendo? Perchè tanto rumore?"

show misha perky_confused_close at twoleft
with charachange

mi "Aw~, davvero? Ma è tutta nel libro… E' per quello che nessun altro la sta copiando~!"

hi "Lo so, perchè stai parlando così forte?"

show misha hips_grin_close at twoleft
with charachange

mi "Perchè stai parlando così piano, Hicchan? E' difficile sentirti."

"Guardo intorno per vedere se qualcuno si sta accorgendo della nostra conversazione ed è piuttosto ovvio che tutti lo hanno fatto, anche l' insegnante."

show shizu behind_smile at right
with charamoveinright

"Shizune sorride civettuola e inizio a chiedermi se Misha sta facendo così perchè glie lo ha detto lei."

"E' per via di quello che è successo prima tra lei e  Lilly?"

"E' questo quel che ottengo per aver provato ad essere ragionevole? Per provare a prendere la strada di mezzo? Shizune è decisamente troppo orgogliosa, anche se ormai dovrei aspettarmi questo tipo di comportamento da lei."

hi "Perchè stai facendo questo?"

show misha perky_confused_close at twoleft
with charachange

mi "Eh?"

"Misha è totalmente ignara dello sguardo imbarazzante che l' insegnante ci sta rivolgendo, mentre cerca di bilanciare il suo testo su un dito."

"Per un breve momento sembra che le cose possano andare male, ma l' insegnante si limita a distogliere lo sguardo, come se non ne valesse la pena."

"Immagino che questo sia un bene, e mi accascio nella mia sedia in sollievo."

scene bg school_scienceroom at bgright
with shorttimeskip

"Il resto della lezione passa tranquillamente, e stavolta sono in grado di apprezzare che sia così."

$ renpy.music.set_volume(1.0,1.0)

play sound sfx_normalbell

"Quando suona la campana, non ho fretta, così rimango per un po', ripassando quello che abbiamo coperto in classe oggi. Preferisco comunque andarmene per ultimo, così da non dover affrontare la folla nei corridoi."

"Noto che anche Shizune e Misha sono rimaste indietro, parlando con qualcuno da un' altra classe."

"Shizune sta segnando così in fretta che le sue mani fanno rumori come spade che tagliano l' aria."

"Misha sta disperatamente cercando di starle dietro, ma è chiaro che a malapena riesce anche solo a capirla."

"Chino la testa. Di qualunque cosa stiano discutendo, sembrano essere affari seri. Probabilmente incomprensibili per me. Non solo, ma Shizune sembra anche arrabbiata, anche se potrebbe essere solo la sua normale severità che la fa sembrare così."

"Shizune segna fino al punto di far scricchiolare i suoi polsi, e Misha si sforza di risputare il tutto in forma di parole."

"Qualche volta inciampa su se stessa come se stesse tentando degli scioglilingua. E poi in più, deve segnare indietro qualunque cosa dica l' altra ragazza."

"Sembra un lavoro duro."

"Misha pare stanca, quasi al punto di svenire."

"Fortunatamente per lei, i loro affari sono presto conclusi e le ragazze si siedono di nuovo ai loro posti."

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter

mi "Uwaaah! Sono così stanca!"

"Sta fiaccamente appoggiando la testa sul suo banco, con aria esausta."

hi "Le preparazioni per il festival devono essere dure per te."

"In effetti, le persone in questa scuola sembrano stare prendendo il festival molto seriamente. Ogni volta che vedo qualcuno indugiare prima e dopo le lezioni stanno sempre parlando dei loro piani per quello."

"E' veramente forte vedere tutti così entusiasti al riguardo."

"Sono probabilmente il solo che non ha qualcosa da fare."

show shizu basic_normal at tworight
show misha perky_confused at twoleft
with charachange

"Shizune inizia a farmi segni e Misha si scuote, guardando le sue mani con occhi leggermente sfocati."

show shizu behind_frown at tworight
with charachange

shi "…"

"Segna con mosse secche, pesanti, drammatiche."

"Misha traduce i suoi segni in parole per me."

"Lo fa così bene che è quasi come se Shizune stesse effettivamente parlando, trasmettendo i suoi pensieri direttamente attraverso Misha."

show misha cross_frown at twoleft
with charachange

mi "Bè, siamo nel consiglio studentesco, sai, quindi siamo piuttosto occupate."

hi "Sarcasmo?"

show misha perky_confused at twoleft
with charachange

mi "Eh?"

"Il tono delle azioni di Shizune mi fa pensare che stia “parlando” con sdegno, ma Misha la interpreta normalmente, rimpiazzando qualunque intento potesse esserci stato colla sua allegria. E' ancora disorientante, non credo che mi ci abituerò mai."

hi "Non importa."

hi "Come potrei dimenticarlo, con voi due che cercate di farmi iscrivere almeno due volte al giorno?"

show misha cross_laugh at twoleft
with charachange

mi "Hahaha~! Però, Hicchan, qualcuno potrebbe dire che c'è troppo lavoro."

show shizu basic_normal2 at tworight
with charachange

show misha perky_sad at twoleft
with charachange

mi "Sarebbe bello se gli studenti mostrassero un po' più di supporto per i loro leader, un po' di apprezzamento per chi sta lavorando così duramente per rendere tutto questo possibile."

show shizu behind_frown at tworight
with charachange

show misha perky_smile at twoleft
with charachange

mi "Forse, per esempio, un po' di aiuto. Quello è chiedere troppo, vero? Yep~! Dell' aiuto sarebbe apprezzato~! Da parte di studenti come te~!"

show shizu adjust_angry at tworight
with charachange

show misha hips_frown at twoleft
with charachange

mi "Se gli studenti mostrassero la loro dedizione e spirito di corpo, e offrissero un po' di aiuto, bene, non ne ho veramente bisogno…"

show shizu behind_smile at tworight
with charachange

show misha hips_smile at twoleft
with charachange

mi "Ma non necessariamente lo rifiuterei … Così~! sarebbe carino se qualcuno volesse…"

stop music fadeout 2.0

show shizu adjust_blush at tworight
show misha perky_confused at twoleft
with charachange

mi "Oh? Salve~!"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Position(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

play music music_hanako fadein 0.3

show hanako emb_timid at Position (xanchor=0.5, xpos=0.93)
with charamoveinright

"Guardo sopra la mia spalla e vedo Hanako timidamente fare capolino nella stanza, la maggior parte del suo corpo nascosto dietro la porta."

show misha perky_smile at Position(xanchor=0.5, xpos=0.15)
with charamove

mi "Ehilà! Di nuovo a giocare alla delinquente?"

show hanako emb_blushtimid at Position (xanchor=0.5, xpos=0.93)
with charachange

"Hanako diventa rossa come un peperone alla diretta punzecchiatura di Misha, anche se era solo uno scherzo."

show shizu basic_angry at Position(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad at Position (xanchor=0.5, xpos=0.93)
with charachange

show hanako emb_downsad at Position (xanchor=0.5, xpos=0.97)
with charamove

"Shizune la fissa indagatrice, facendo sì che Hanako chini la testa e inizi a ritirarsi al punto che solo le sue dita possono essere viste nervosamente aggrappate al bordo della porta."

"Forse sta mostrando la sua antipatia per Hanako per associazione alla sua antipatia per Lilly."

"Sembra essere così, e probabilmente anche Hanako lo sa."

"Sembrano essersi temporaneamente dimenticate di tentare di farmi rimanere per il resto della giornata."

hi "Cosa c'è, Hanako?"

show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
with charachange

ha "L… Lilly è passata di qui?"

mi "Spiacente, Satou non è qui. E', eh, passata stamattina però."

show hanako emb_downtimid at Position (xanchor=0.5, xpos=0.97)
with charachange

"Hanako continua a guardare con aria incerta verso Shizune, che la fissa a sua volta con la sua solita espressione analitica. Che sta cercando di fare?"

"Ovviamente Shizune non distoglierà lo sguardo, ed è già abbastanza intimidante così come è, quindi posso solo immaginare quanto sarebbe terrorizzata Hanako."

"E' un po' buffo però, guardare la reazione di Hanako al normale comportamento di Shizune. Questo è quel che succede quando due persone agli estremi opposti si incontrano, a quanto pare."

show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
with charachange

ha "Sapete… sapete dov'è?"

show shizu behind_frown at Position(xanchor=0.5, xpos=0.35)
with charachange

shi "…"

show misha hips_frown at Position(xanchor=0.5, xpos=0.15)
with charachange

mi "Se ha del buon senso in quella testa, è nella sua classe, a lavorare sul loro progetto per il festival. Ma chissà dove sta perdendo tempo quella donna."



label it_A22a:

show misha hips_grin at Position(xanchor=0.5, xpos=0.15)
with charachange

mi "Potrebbe stare bighellonando da qualche parte, proprio come Hicchan~! Wahaha~!"

"Dannazione, perchè Shizune sente il bisogno di fare notare cose del genere?"



label it_A22b:

scene bg school_scienceroom at bgleft
show shizu behind_frown at Position(xanchor=0.5, xpos=0.35)
show misha hips_frown at Position(xanchor=0.5, xpos=0.15)
show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
with None


mi "Potrebbe stare bighellonando da qualche parte~! Che donna inutile~!"

show hanako emb_downtimid at Position (xanchor=0.5, xpos=0.97)
with charachange

hide hanako
with easeoutright

"Hanako annuisce in fretta e si ritira di corsa, ovviamente per evitare qualunque ulteriore contatto con Shizune. Sfortunatamente, questo focalizza la loro attenzione di nuovo pienamente su di me."

stop music fadeout 2.0

show shizu behind_frown at tworight
show misha hips_frown at twoleft
show bg school_scienceroom at bgright
with charamove

show misha hips_grin at twoleft
show shizu behind_smile at tworight
with charachange

mi "Ma Hicchan non è inutile, giusto? Giusto? L' ha detto lui stesso~! Wahaha~!"

"Vedo che direzione sta prendendo il discorso, e non ne voglio sapere, non dopo quell' esperienza di ieri."

play music music_tension fadein 0.3

hi "Bè, buona fortuna colle vostre preparazioni…"

"Inizio a rifare la mia borsa, pronto a fuggire verso l' uscita."

"Sfortunatamente sono al capo esattamente opposto della stanza."

"La breve distanza fino alla porta ora mi sembra una terra di nessuno impossibilmente vasta."

show misha perky_smile at twoleft
show shizu behind_blank at tworight
with charachange

show bg school_scienceroom at bgleft
show shizu behind_blank
show misha perky_smile at Position(xalign=-0.15)
with charamove

show bg school_scienceroom
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charamove

"Shizune e Misha iniziano entrambe a manovrare lentamente di fronte a me, tagliando la mia via di fuga in un modo inquietantemente cauto che mi fa pensare a un abbordaggio navale."

stop music fadeout 2.0

show misha hips_grin at twoleft
with charachange

play music music_comedy fadein 0.3

mi "Credo che Shicchan stia dicendo che dovresti aiutarci, Hicchan~!"

hi "Ooh, non saprei, è talmente indiretta."

show misha perky_confused at twoleft
with charachange

mi "Ma~! quello è l' intento, quindi, per favore? Non posso farcela, dobbiamo addirittura costruire dei chioschi per il festival, quasi tutti da sole, riesci a crederci?"

show misha perky_sad at twoleft
with charachange

mi "Inchiodare insieme delle assi, ancora e ancora, per ore intere, è davvero dura!"

mi "Mi sono talmente abituata che stavo facendo dei movimenti di martellare in classe, e non me ne ero nemmeno accorta!"

"Picchia sul suo banco alcune volte, imitando dei colpi di martello."

mi "E' talmente ripetitivo, non lo sopporto! E ieri, ho addirittura inchiodato tutte le assi una sull' altra…"

mi "Era solo una pila di assi inchiodate, e allora ho dovuto dividerle e rifare di nuovo da capo, e mi hanno urlato e riso dietro~!"

hi "Uh…"

show misha perky_smile at twoleft
with charachange

mi "Così…"

show misha hips_grin_close at twoleft
with characlose

"Stringe la mia spalla con una mano e sorride, facendo scorrere rapidamente e maliziosamente la lingua sui suoi denti."

mi "Hai dei progetti per oggi, Hicchan?"

mi "Mi chiedo se ne hai~."

hi "Certo che ho dei progetti…"

show misha perky_confused_close at twoleft
with characlose

mi "Davvero~?"

mi "Ci aiuterai, vero?"

"Noto che le sue mani si muovono costantemente."

"Sta segnando tutto quello che diciamo in modo che Shizune possa capire."

"Shizune è piuttosto silenziosa oggi. E' ancora arrabbiata? Beh, probabilmente almeno un pochino. Posso vederlo nei suoi occhi. Ma questo potrebbe anche essere solo un altro modo di farmi sentire in colpa e far sì che la aiuti."

"Devo trovare una via di fuga."

hi "Ehi, dovrei andare ora, in biblioteca. Sai, i compiti…"

hi "Dovrei proprio andare, non è vero? Devo essere diligente perchè sono un nuovo studente, dopotutto, così devo fare una buona prima impressione, giusto? Già…"

hi "Allora, arrivederci!"

show misha perky_confused_close at offscreenleft
show shizu behind_blank at twoleft
show bg school_scienceroom at bgleft
with ease

hide misha
show misha perky_confused_close behind shizu at offscreenleft

show shizu basic_normal2 at offscreenright
show bg school_scienceroom
with ease_accel

show shizu cross_angry at tworight
show bg school_scienceroom at bgright
with ease_decel

"Mi giro per fuggire verso la porta, ma Shizune sta bloccando la mia strada, braccia incrociate sul suo petto e con un' espressione severa sul volto."

show shizu basic_angry at tworight
with charachange

"Agita un dito in scherno e inizia a segnare a Misha con l' aria di un caposquadra che dia istruzioni ai soldati suoi compagni."

show misha perky_smile at twoleft
with charamove

mi "Non sembrava che avessi alcuna fretta di correre in biblioteca, Hicchan~!"

show misha hips_grin at twoleft
with charachange

mi "E' vero, Shicchan~, sembra che probabilmente volesse prendersela comoda per il resto della giornata."

show misha hips_laugh at twoleft
with charachange

mi "Hahaha~! Wahaha~! Sei circondato~!"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Andiamo all' aula del consiglio studentesco~!"

"Si lascia sfuggire un risolino, e poi esplode in una risata."

show misha cross_laugh at twoleft
with charachange

mi "Mi dispiace, Hicchan, mi sento in colpa, ma così beneficiano tutti, no?"

show shizu basic_normal2 at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "E' vero, Shicchan! Sì~, anche quello è un punto valido."

show shizu behind_blank at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Sì, questo è di beneficio a tutti, risolve tutti i nostri problemi."

show shizu basic_frown at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange

mi "Già già~!, anche io pensavo che avrebbe apprezzato di più i nostri sforzi."

show misha hips_frown_close at twoleft
show shizu basic_frown_close at tworight
with characlose

"Si stringono più vicine, come se stessero per balzarmi addosso."

hi "Ehi, ragazze, due contro uno non è molto leale, no?"

show shizu behind_blank_close at tworight
with charachange

shi "…"

"Continua a guardare avanti, impassibile, poi sorride sinistramente."

show shizu basic_sparkle_close at tworight
show misha hips_grin_close at twoleft
with characlose

mi "Forza, abbiamo un sacco di lavoro da fare! Andiamo alla stanza del consiglio studentesco~!"

hi "Uuh, non saprei…"

show misha cross_laugh_close at twoleft
with characlose

"Misha ride."

show misha hips_grin_close at twoleft
with characlose

mi "Deja vu~?"

"Misha prima tenta di soffocare, poi lascia esplodere un' altra risata."

show misha cross_laugh_close at twoleft
with characlose

mi "Hahaha, sai, il mio oroscopo diceva che oggi sarebbe stata una buona giornata per me."

show misha perky_smile_close at twoleft
with characlose

mi "E ora che ci aiuterai—{w=.5}{nw}"

show shizu adjust_smug_close at tworight
with charachange

"Shizune rapidamente le segna qualcosa."

show misha hips_grin_close at twoleft
with charachange

mi "Giusto~!, volevo dire, ora che hai deciso di aiutarci, completamente di tua volontà,"

mi "Potrò prendermela comoda! Che fortuna~, eh?"

"Apro bocca per dire qualcosa ma poi capisco che è inutile."

"Cambio obiettivo cercando di pensare a una via di uscita. No, le loro azioni sono chiaramente deliberate, non ha senso tentare di ragionare con loro."

"Non si può ragionare coi pazzi. Faccio una smorfia, e loro non si accorgono nemmeno della mia insoddisfazione, provando ulteriormente i miei sospetti."

"Adesso sembrano piuttosto rilassate, credo che pensino di aver già vinto così stanno allentando la loro guardia."

stop music fadeout 2.5

"Quello è un tantino arrogante."

"Mi oltrepassano mentre si muovono attraverso la porta,"

hide shizu
hide misha
with charaexit

"E io furtivamente cammino all' indietro nell' aula mentre loro entrano nel corridoio, girando verso il pozzo delle scale."

"Lascio sfuggire un sospiro di sollievo e rapidamente recupero il resto della mia roba così da potermi mettere in fuga."

"La porta dell' aula sbatte chiudendosi."

play sound sfx_impact2

play music music_comedy fadein 0.5

show shizu cross_angry at offscreenright with None
show misha cross_frown at offscreenleft with None
show shizu cross_angry at tworight
show misha cross_frown at twoleft
with ease

shi "…"

mi "Quello non è stato molto carino, davvero. Hahaha, ci hai veramente fregato per benino, però. Non è vero, Shicchan?"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Giusto, giusto… …Hahaha!"

show misha cross_frown at twoleft
with charachange

mi "Che idea era quella? Pensavo che avessi detto che ci avresti aiutato!"

mi "E poi ci hai completamente mollato! E credevi anche di poter farcela sotto il naso, non è vero?"

show misha cross_laugh at twoleft
with charachange

"L' espressione indignata sparisce e inizia a ridere istericamente, calmandosi solo dopo uno sguardo seccato da Shizune."

show misha cross_grin at twoleft
with charachange

mi "Oh, ah… Già~, credevi anche di poter farcela sotto il naso. Ma, un criminale ritorna sempre sulla scena del crimine!"

"In primo luogo, non sono nemmeno riuscito a lasciare l' aula. No, aspetta, in primo luogo non ho nemmeno acconsentito ad aiutarle."

show misha perky_smile at twoleft
with charachange

mi "Non molto sveglio, vero, criminale? Pensare di poter schivare i tuoi doveri in quel modo… Davvero infame, Hicchan~!"

hi "Sono un criminale? Che cosa ho fatto? Qual è l' accusa? Di che sono colpevole?"

show misha hips_grin at twoleft
with charachange

mi "Quello è il tribunale che lo deciderà, criminale! Non credo che dobbiamo essere noi a dirtelo!"

show misha perky_smile at twoleft
with charachange

mi "Inoltre, tu sei il criminale, tu sai che cosa hai fatto!"

hi "Hai mai letto “Il Processo,” di Kafka?"

show misha hips_grin at twoleft
with charachange

mi "No, cos'è, Hicchan~? Cosa ha a che vedere con questo?"

hi "L' ho letto alcuni mesi fa. Parla di queste persone che indicono un processo inventato contro un tizio che vuole solo vivere la sua vita. Si rifiutano di lasciarlo in pace, e lui non può combattere il sistema."

show shizu basic_frown at tworight
with charachange

shi "…"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Hicchan, quello cosa ha a che vedere con qualunque cosa?"

show misha sign_confused at twoleft
with charachange

mi "Ehi~!, che vuol dire?"

stop music fadeout 1.5

"Si torna a girare verso di me dopo la conclusione di uno scambio di segni avanti e indietro per un discreto periodo di tempo."

play music music_shizune fadein 1.5

show misha hips_frown at twoleft
with charachange

mi "Sai, siamo entrambe un poco deluse da te. Ci hai lasciato nelle peste, Hisao."

show shizu basic_frown at tworight
with charachange

shi "…"

mi "Scaricato il barile."

show shizu behind_frown at tworight
with charachange

shi "…"

mi "Abbandonate al nostro fato. E mollate ad arrangiarci~."

show shizu cross_angry at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Ti pare il modo di trattare le persone? Fuggire dalle tue responsabilità, abbandonare i tuoi camerati?"

show misha hips_frown at twoleft
with charachange

mi "Pensiamo che ci sia dovuto che tu onori il tuo impegno."

hi "Cosa? Ma non mi sono impegnato a fare nulla~!"

"Il fiato mi si blocca in gola e per un momento mi soffoco."

show shizu basic_frown at tworight
with charachange

shi "…"

show misha cross_smile at twoleft
with charachange

mi "Quello non è vero, Hicchan! Hai detto che non sei inutile, lo hai decisamente detto, sì, decisamente, decisamente decisamente~!"

show misha hips_grin at twoleft
with charachange

mi "Adesso vogliamo che tu provi quelle parole~! Farai meglio a prepararti a dimostrare che non sei un tizio inutile!"

mi "Il tuo onore sarà eternamente macchiato se provi a svignartela~!"

mi "Così per il resto della giornata, dovremo passare il tempo insieme, solo noi tre, e lavorare duro!"

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Non puoi prenderci in giro!"

mi "Dovresti essere contento, stai facendo un gran servizio alla tua scuola. Non chiedere cosa la tua scuola possa fare per te…"

mi "Ma cosa tu puoi fare per la tua scuola!"

show misha cross_laugh at twoleft
with charachange

mi "Hahaha!"

mi "Hahahahahahaha!"

"Deprimente."

show misha cross_grin at twoleft
with charachange

mi "Allegro, allegro, Hicchan!"

"Mi molla una pacca sulla schiena con abbastanza forza da farmi uscire l' aria dai polmoni. Annaspo per respirare."

mi "E poi, non sei contento di passare la giornata con due belle ragazze?"

show misha hips_laugh at twoleft
with charachange

mi "Hahahaha!"

"Suppongo che abbiano ragione. Mi sono lasciato sfuggire quelle parole."

"Accettando il mio fato, le seguo fino all' aula del consiglio studentesco…"

scene bg school_council_ss
with shorttimeskip

stop music fadeout 2.0

play sound sfx_hammer

"…E martello l' ultimo chiodo nel chiosco. C'è voluto tutto il pomeriggio, e tra poco sarà passata l' ora di cena. Ma adesso è finita."

play music music_another fadein 0.5

show shizu basic_normal_ss
with charaenter

"Shizune estrae un metro a nastro e una piccola livella, e lo ispeziona attentamente."

show shizu behind_smile_ss
with charachange

"Sorride con aria soddisfatta, poi fa segno a Misha di avvicinarsi."

show shizu adjust_happy_ss
with charachange

shi "…"

show shizu adjust_happy_ss at tworight
show bg school_council_ss at bgright
with charamove

show misha perky_smile_ss at twoleft behind shizu
with charaenter

mi "Dice che hai fatto un ottimo lavoro. In effetti, potresti addirittura essere dotato per queste cose."

show misha hips_smile_ss at twoleft
with charaenter

mi "Wow, anche io sono impressionata. E sei stato svelto, hai già fatto questo genere di cose prima?"

hi "No. Mai."

hi "Mai prima d' ora."

hi "E non lo farò mai più."

show shizu behind_smile_ss at tworight
with charachange

shi "…"

mi "Bene, la nostra quota per la giornata è di sei chioschi. Tra pochi minuti io e Shicchan dovremmo finire questo."

show misha hips_grin_ss at twoleft
with charachange

mi "Il che significa~… ancora quattro!"

show misha sign_smile_ss at twoleft
with charachange

mi "Stiamo andando a un buon passo, dice~!"

show misha hips_grin_ss at twoleft
with charachange

mi "Non è divertente?"

hi "Cosa?"

"Potrei pensare a un milione di cose che preferirei fare, ma immagino che tutti debbano fare la loro parte per il festival, perfino io."

hi "Siete entrambe fortunate che vi stia aiutando, se davvero non avessi voluto, avrei potuto districarmi facilmente."

show shizu basic_normal2_ss at tworight
with charachange

shi "…"

show misha perky_smile_ss at twoleft
with charachange

mi "Davvero, Hicchan?"

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

show misha cross_laugh_ss at twoleft
with charachange

mi "Wahaha~! Shicchan pensa che tu stia solo facendo il gradasso! I giapponesi non possiedono la risposta “combatti o fuggi”, Hicchan~!"

"Shizune unisce i suoi polpastrelli con aria subdola."

show shizu basic_happy_ss at tworight
with charachange

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "Decisamente~! Decisamente, decisamente~! Se davvero avessi voluto scappare, avresti preso azione immediata~! E' così che capisci se qualcuno è serio; quando non hanno dubbi, nè rimpianti!"

show shizu basic_normal_ss at tworight
with charachange

shi "…"

show misha sign_smile_ss at twoleft
with charachange

mi "Forse è stata una cattiva idea dirtelo, dato che ora Hicchan sa cosa fare la prossima volta~."

"Però, solo il fatto che le stia bene di avermi detto questo mi mostra che dubita che sarei capace di agire."

"Quello mi fa solo desiderare di più di farlo, e quasi voglio che l' opportunità di farlo compaia di nuovo. Ma se capita, lei potrebbe fregarmi di nuovo in qualche modo."

stop music fadeout 2.0

show shizu behind_smile_ss at tworight
with charachange

shi "…"

show misha perky_smile_ss at twoleft
with charachange

mi "Shicchan dice che è contenta adesso."

scene bg school_council_ni
with shorttimeskip

play music music_dreamy fadein 0.3

"Molto, molto più tardi la stessa sera, stiamo guardando sei chioschi completati."

"Coll' orgoglio di un lavoro ben fatto, ci riposiamo e ammiriamo i frutti del nostro lavoro, senza scambiare una parola. Solo ammirandoli."

"Mi accorgo di sentirmi molto assetato."

hi "Ehi, non c'è una macchina distributrice fuori nel corridoio? Sono accese più o meno tutto il giorno, giusto?"

show misha hips_smile
with charaenter

mi "Già, e le bevande costano davvero poco. Di solito prendiamo qualcosa da lì durante giorni come questo."

"Scavo nelle mie tasche, e trovo una singola moneta da cento yen."

hi "Bastano questi? Mi sento un po' assetato."

show misha hips_grin
with charachange

mi "Cento yen? Puoi comprare qualunque bevanda venduta dalla macchina con quelli."

hi "Bene, molto bene, allora."

show misha hips_grin at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Ah, aspetta un secondo."

show misha hips_grin at twoleft
with charachange

mi "Hm? Che c'è, Shicchan? Vuoi che compri una bevanda anche per te? Hahaha!"

show shizu behind_smile at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Hicchan, ci hai veramente aiutato, così oggi ti— voglio dire Shicchan, ti offrirà da bere."

show misha perky_confused at twoleft
with charachange

mi "Ehi, e io?"

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Cosa vorresti da bere? Ho sete anche io?"

show misha perky_confused at twoleft
with charachange

mi "Anche io!"

hi "Hm, non so. Qualunque cosa va bene. Forse la soda al melone."
#Oh Gesù ho controllato ed esiste. E pure la melonsoda, anche se non con questo nome.

show shizu behind_smile at tworight
with charachange

shi "…"

show misha perky_sad at twoleft
with charachange

mi "Ehi, aspetta, Shicchan! Anche io voglio qualcosa da bere!"

hide shizu
with charaexit

show misha perky_sad
show bg school_council_ni
with charamove

mi "Aw…!"

show misha perky_confused
with charachange

mi "Sai, è in momenti come questo che penso che mi stia solo stuzzicando."

hi "Probabilmente è così. Sono sicuro che prenderà qualcosa per te, giusto?"

mi "Già, di solito lo fa. Però… non si sa mai…"

hi "Heh."

show misha perky_confused at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu basic_normal2 at tworight behind misha
with charaenter

"Shizune ritorna con due sode al melone e una lattina di succo di frutta."

"Passa a me una delle sode, e l' altra a Misha."

show misha hips_grin at twoleft
with charachange

mi "Grazie, Shicchan~! Avevo completa fiducia che me ne avresti comprata una, sapevo di poter contare su di te! Wahahaha!"

show misha perky_confused at twoleft
with charachange

mi "Ma come hai fatto a sapere che questo era quel che volevo? Di solito prendo qualcos' altro."

show shizu behind_smile at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Come? Sapevi che avrei voluto provarla? E che mi piacciono questo tipo di cose da bambini? Hahahaha!"

show misha hips_laugh at twoleft
with charachange

mi "Hahahaha!"

"Mimo i miei ringraziamenti a Shizune, che sorride e annuisce."

stop music fadeout 2.0

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Senti, Hicchan…"

hi "Sì?"

show shizu behind_smile at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Abbiamo passato un sacco di tempo insieme. Già, in così poco tempo, abbiamo fatto così tanto."

mi "Dovremmo smettere entrambi di far finta di niente. Quello che sto cercando di dire è,"

"Sembra proprio che stia per chiedermi di uscire insieme, ma non è possibile. Ciononostante, il mio cuore sta battendo come un martello pneumatico. Dannazione, questo mi ricorda un' altra scena simile capitatami quest' anno."

"Provo a dire qualcosa, ma il mio cervello non riesce a decidere se fermarla o dirle di continuare."

"Mi sento arrossire fino alla cima delle orecchie."

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha hips_smile at twoleft
with charachange

mi "Quel che sto cercando di dire è…"

play music music_comedy fadein 0.2

show misha hips_grin at twoleft
with charachange

mi "Vorresti unirti al consiglio studentesco?"

hi "Ah, che delusione."

show misha cross_laugh at twoleft
show shizu adjust_blush at tworight
with charachange

mi "Hahaha! Hahahaha! Hahahahaha! Wahaha! Hahahaha!"

mi "Pensavi che volesse chiederti di uscire con lei, Hicchan?"

mi "Hahahaha! Hahaha! Hahaha! Hahahaha!"

mi "Hahahahahahahaha!"

"Adesso mi sento molto imbarazzato, posso sentirmi diventare ancora più rosso in faccia."

"Anche Shizune tenta di nascondere il suo arrossire dopo che Misha traduce, e poi mette alcuni fogli di carta di fronte a me."

show shizu behind_frustrated at tworight
with charachange

shi "…"

show misha cross_grin at twoleft
with charachange

mi "Così, che ne dici? Tutte le carte sono pronte."

show misha cross_smile at twoleft
with charachange

mi "E comunque, sei già seduto. Sembri molto a casa tua qui. Bevande e tutto~!"

stop music fadeout 2.0

show shizu basic_normal at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Che cosa rispondi?"

"Si calma un poco e chiede di nuovo, un po' più solennemente."

show misha cross_smile at twoleft
with charachange

mi "Hicchan, che cosa rispondi?"

show misha sign_smile at twoleft
with charachange

mi "Non è che detesti questo lavoro, giusto?"

play music music_dreamy fadein 1.5

"Sono più che un poco sorpreso da questo improvviso cambio di tono. Non so davvero come reagire."

"Per cominciare, non sta urlando tumultuosamente senza riguardo per il tatto."

"Tutte le altre volte, sono sicuro che sapeva già che avrei risposto di no."

"Questa volta, sembra davvero seria."

show misha perky_smile at twoleft
with charachange

mi "Penso che forse dovresti diventare un membro. Non solo perchè ci farebbe comodo il tuo aiuto, ma, bè, passi comunque il tempo con noi."

mi "Penso anche che a Shicchan farebbe piacere se ti unissi a noi. Non ci odi o niente del genere, giusto?"

show misha perky_sad at twoleft
with charachange

mi "Non sarebbe un male se ti iscrivessi. E lo apprezzerei se tu lo facessi."

"Sembra avere dei problemi a pronunciare le sue parole, che è strano per una persona loquace come Misha."

"Per qualche motivo, sono quasi preoccupato da questo."

show shizu behind_blank at tworight
with charachange

"I miei occhi deviano nella direzione di Shizune, che mi fissa incertamente in risposta, distrattamente pulendosi le unghie."

show misha perky_smile at twoleft
with charachange

mi "Se non vuoi aggregarti a noi, prometto che non te lo chiederemo di nuovo, ma se volessi, saremmo veramente felici."

"Sia Shizune che Misha sembrano incapaci di guardarmi negli occhi."

"Non posso mentire, il pensiero di essere vicino a due ragazze così carine è qualcosa che non posso assolutamente rifiutare."

"Non sono eccitato dalla prospettiva di questo genere di lavoro tutti i giorni, ma ce ne dovrebbe essere meno dopo il festival."

"Almeno, spero."

hi "Va bene. Credo che non possa essere un male, quindi, perchè no?"

show shizu adjust_happy at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Meraviglioso. Meraviglioso! Ahahaha~!"

"Shizune si tocca le punte delle dita in segno di soddisfazione."

show shizu basic_happy at tworight
with charachange

shi "…"

show misha perky_smile at twoleft
with charachange

mi "Lei compilerà tutto il necessario, Hicchan. Congratulazioni, adesso sei ufficialmente un membro del consiglio studentesco!"

hi "Grande. Non sono eccitato dall' idea di tanto lavoro."

hi "Per essere onesto, non ho mai partecipato a nessuna attività di consiglio studentesco prima."

hi "Ma forse sarà un' esperienza positiva?"

"Misha inizia ad applaudire, ridendo esuberante mentre lo fa."

show misha hips_laugh at twoleft
with charachange

mi "Congratulazioni, Hicchan!"

show shizu adjust_smug at tworight
with charachange

shi "…"

mi "Congratulazioni!"

show shizu behind_smile at tworight
with charachange

shi "…"

mi "Congratulazioni!"

show shizu adjust_happy at tworight
with charachange

shi "…"

mi "Congratulazioni!"

hi "Ho colto il messaggio."

"Non posso fare a meno di sorridere, trovando questa infantile dimostrazione graziosa."

show misha hips_grin at twoleft
with charachange

mi "Il consiglio studentesco è sempre impegnato, sai! Ma per oggi, abbiamo finito. Arrivederci a domani, Hicchan!"
    
show misha hips_smile at twoleft
with charachange

mi "Ci è rimasto ancora del lavoro da fare, così conteremo su di te!"

stop music fadeout 2.0

scene bg school_hallway3
with locationchange

"Lascio la stanza, sentendomi completamente distrutto. Il campus è totalmente deserto, e la scuola sembra piuttosto minacciosa a questa tarda ora. La sola finestra ancora illuminata è quella dell' ufficio del consiglio studentesco."

"E' così che sarà il consiglio studentesco? Il mio corpo potrebbe non resistere."



#*****************************

label it_A23:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_normal fadein 0.3

"Hanako non si presenta affatto alla lezione del mattino, lasciando il suo posto vuoto e solitario sul retro dell' aula."

"Devo dirle che Lilly la stava cercando se la vedo più tardi."

"Dopo gli eventi di stamattina, la lezione è piuttosto noiosa al confronto. Giro pigramente le pagine del mio libro di testo."

"Devo recuperare un po', a dispetto di aver tentato di tenere il passo coi miei studi in ospedale, ma non mi sento troppo entusiasta al riguardo."

"L' orologio al fronte della stanza sembra incredibilmente rumoroso. L' insegnante non ha detto nulla per più di sette minuti, optando invece per coprire la lavagna in file e file di equazioni copiate direttamente dal libro."

"Il ritmico impatto del gesso sulla lavagna sembra sincronizzarsi perfettamente col ticchettio dell' orologio."

"Inizio a copiare le equazioni tanto per passare il tempo, anche se sono già nel libro di testo."

scene bg school_scienceroom at bgright
with shorttimeskip

play sound sfx_normalbell

"Quando suona la campana, non ho fretta perchè non ho nulla da fare, così rimango per un po', ripassando quello che abbiamo coperto in classe oggi. Preferisco comunque andarmene per ultimo, così da non dover affrontare la folla nei corridoi."

"Noto che anche Shizune e Misha sono rimaste indietro, parlando con qualcuno da un' altra classe."

"Shizune sta segnando così in fretta che le sue mani fanno rumori come spade che tagliano l' aria."

"Forse c'è della rabbia contenuta lì."

"Misha sta disperatamente cercando di starle dietro, ma è chiaro che a malapena riesce anche solo a capirla."

"Chino la testa. Di qualunque cosa stiano discutendo, sembrano essere affari seri."

"Shizune segna fino al punto di far scricchiolare i suoi polsi, e Misha si sforza di risputare il tutto in forma di parole."

"Qualche volta inciampa su se stessa come se stesse tentando degli scioglilingua. E poi in più, deve segnare indietro qualunque cosa dica l' altra ragazza."

"Sembra un lavoro duro."

"Misha pare stanca, quasi al punto di svenire."

"Fortunatamente per lei, i loro affari sono presto conclusi e le ragazze si siedono di nuovo ai loro posti."

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter

mi "Uwaaah! Sono così stanca!"

"Sta fiaccamente appoggiando la testa sul suo banco, con aria esausta."

"Sfrutterò l' opportunità per riconciliarmi un poco con Shizune, senza farmi accalappiare di nuovo nella questione del consiglio studentesco, anche se sospetto che quella porta ora per me sia chiusa."

hi "Le preparazioni per il festival devono essere dure per te."

"In effetti, le persone in questa scuola sembrano stare prendendo il festival molto seriamente. Ogni volta che vedo qualcuno indugiare prima e dopo le lezioni stanno sempre parlando dei loro piani per quello."

"E' veramente forte vedere tutti così entusiasti al riguardo."

"Sono probabilmente il solo che non ha qualcosa da fare."

show shizu basic_angry at tworight
with charachange

"Shizune prima mi squadra, come se stesse cercando di decidere se ignorarmi o ridere di me, ma alla fine inizia a segnare senza fare nessuna delle due cose."

show misha perky_confused at twoleft
with charachange

"Misha si scuote, guardando le sue mani con occhi leggermente sfocati."

show shizu behind_frown at tworight
with charachange

shi "…"

"Segna con mosse secche, pesanti, drammatiche."

"Misha traduce i suoi segni in parole per me."

"Lo fa così bene che è quasi come se Shizune stesse effettivamente parlando, trasmettendo i suoi pensieri direttamente attraverso Misha."

"Deve essersi esercitata vigorosamente."

show misha cross_frown at twoleft
with charachange

mi "Ovviamente, siamo nel consiglio studentesco, sai, quindi siamo piuttosto occupate."

show shizu basic_frown at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "E' un nostro importante dovere, assicurarci del successo del festival con tutte le nostre forze."

show shizu behind_frown at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange

mi "Ci disonoreremmo di fronte alle passate generazioni del consiglio studentesco se il festival dovesse fallire."

show shizu adjust_angry at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "E' per questo che non ci devono essere difetti, no… uhhh credo che quello fosse “impedimenti”, niente di niente che possa rendere il festival meno che perfetto."

"L' appassionato discorso di Shizune e l' interpretazione di Misha sono davvero stranamente adatti a loro."

stop music fadeout 2.0

show shizu adjust_blush at tworight
show misha perky_confused at twoleft
with charachange

mi "Oh? Salve~!"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Position(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

play music music_hanako fadein 0.3

show hanako emb_timid at Position (xanchor=0.5, xpos=0.93)
with charamoveinright

"Guardo sopra la mia spalla e vedo Hanako timidamente fare capolino nella stanza, la maggior parte del suo corpo nascosto dietro la porta."

show misha perky_smile at Position(xanchor=0.5, xpos=0.15)
with charamove

mi "Ehilà! Di nuovo a giocare alla delinquente?"

show hanako emb_blushtimid at Position (xanchor=0.5, xpos=0.93)
with charachange

"Hanako arrossisce come un peperone alla diretta punzecchiatura di Misha, anche se era solo uno scherzo."

show shizu basic_angry at Position(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad at Position (xanchor=0.5, xpos=0.93)
with charachange

show hanako emb_downsad at Position (xanchor=0.5, xpos=0.97)
with charamove

"Shizune la fissa indagatrice, facendo sì che Hanako chini la testa e inizi a ritirarsi al punto che solo le sue dita possono essere viste nervosamente aggrappate al bordo della porta."

"Forse sta mostrando la sua antipatia per Hanako per associazione alla sua antipatia per Lilly."

"Sembra essere così, e probabilmente anche Hanako lo sa."

hi "Cosa c'è, Hanako?"

show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
with charachange

ha "L… Lilly è passata di qui?"

mi "Spiacente, Satou non è qui. E', eh, passata stamattina però."

show hanako emb_downtimid at Position (xanchor=0.5, xpos=0.97)
with charachange

"Hanako continua a guardare con aria incerta verso Shizune, che la fissa a sua volta con la sua solita espressione analitica. Che sta cercando di fare?"

"Ovviamente Shizune non distoglierà lo sguardo, ed è già abbastanza intimidante così come è, quindi posso solo immaginare quanto sarebbe terrorizzata Hanako."

"Guardare la reazione di Hanako al normale comportamento di Shizune mette un po' a disagio. Questo è quel che succede quando due persone agli estremi opposti si incontrano, a quanto pare."

show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
with charachange

ha "Sapete… sapete dov'è?"

show shizu behind_frown at Position(xanchor=0.5, xpos=0.35)
with charachange

shi "…"

show misha hips_frown at Position(xanchor=0.5, xpos=0.15)
with charachange

mi "Se ha un po' di buon senso in quella testa, è nella sua classe, a lavorare sul loro progetto per il festival. Ma chissà dove sta perdendo tempo quella donna."



label it_A23a:

scene bg school_scienceroom at bgleft
show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Position(xanchor=0.5, xpos=0.35)
show misha hips_frown at Position(xanchor=0.5, xpos=0.15)
with None

hide hanako
with charamoveoutright

"Hanako annuisce in fretta e si ritira di corsa."

stop music fadeout 2.0

show misha hips_grin at Position(xanchor=0.5, xpos=0.15)
with charachange

mi "Di cosa stavamo parlando? Oh già, stiamo davvero lavorando duro per la buona riuscita del festival."

"E facendo impazzire altre persone nel processo."

hi "Bè, buona fortuna."

"Mi alzo per andarmene, uscendo prima che una di loro riesca a rimproverarmi di nuovo dandomi del perditempo."

scene bg school_hallway3
with locationchange

"I corridoi sono abbastanza silenziosi, come mi aspettavo. Tutti devono essere agli incontri dei club o alle preparazioni del festival. O entrambe le cose."

"Le accuse di Shizune riguardo il mio essere un fannullone mi echeggiano nella testa."

"Mi sento un po' in colpa per non stare contribuendo, ma pare che mi manchi la decisione necessaria per fare qualcosa di concreto al riguardo."

"Per il festival, è già troppo tardi a meno che io non conti di aiutare Shizune e Misha, cosa che naturalmente non faccio. E per i club… non so."

"Forse non sono un tipo da club."

scene bg school_dormext_half
with locationskip

"A metà strada tra l' edificio scolastico e i dormitori noto una figura di fronte agli ultimi."

"E' Rin."

"Sembra che stia lavorando sul suo murale anche oggi."

"Cammino fino a lei, che non sembra accorgersi che mi sto avvicinando."

scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with locationchange

"E' seduta su una cassa rovesciata, contemplando intentamente il muro che sta dipingendo con un pennello tenuto tra le dita di un piede."

"Il murale ha fatto considerevoli progressi da ieri ma è ancora solo completo a metà per quanto posso capire."

"Sono apparsi altri colori e anche le figure umane distorte si sono sparse e moltiplicate."

"Devo dirlo, lo stile in cui è dipinto attira molto l' occhio ed è davvero unico. Non che io sia un conoscitore d' arte su nessuna scala misurabile, ma è comunque molto bello."

"Mi schiarisco la gola per attrarre la sua attenzione, ma non distrarla al punto che la sua concentrazione vada persa."

rin "Aspetta."

"Non si gira nemmeno per vedere chi è."

"Aspetterò."

"…"
    
"…"
    
"…"
    
"…"
    
scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with shorttimeskip

"…"

"Quindici minuti più tardi decido che la sua concentrazione non è infatti andata persa e che ho anche aspettato abbastanza così le dò un colpetto sulla spalla per ricordarle la mia presenza."

"Rin gira meccanicamente la testa nella mia direzione, finendo per guardare all' altezza del mio inguine."

play music music_rin fadein 0.3

show rin basic_deadpan_close at tworight
with charachange

rin "Oh, Hisao."

"Come fa a capirlo? Mi sentirei molto meno a disagio se mi guardasse in faccia."

hi "Osservazione astuta. Impengnata a lavorare, vedo."

"La conversazione comincia come se non fossi qui già da un quarto d' ora, ma non è un problema. Almeno comincia."

hi "Ha un bell' aspetto."

"E' così, gli strati di pittura che nascondono altri strati di pittura, mischiandosi e formando le figure umane, creano davvero un aspetto di grande effetto. Ma Rin sembra seccata."

show rin basic_deadpanupset_close at tworight
with charachange

rin "Non dovresti commentare su un lavoro in corso. Sette anni di sfortuna."

hi "Sembra terribile. Credo che ritirerò il commento allora."

"Però, ha un bell' aspetto. Mi chiedo se mi toccheranno quattordici anni di sfortuna per averlo pensato."

show rin basic_awayabsent_close at tworight
with charachange

"Rin torna a guardare il suo dipinto e lo tocca con un alluce."

show rin relaxed_nonchalant_close at tworight
with charachange

rin "Potresti mischiare un po' di questo colore? Lo sto finendo."

"Guarda in basso verso una ciotola mezza vuota contenente i resti della stessa vernice rosata."

"Non avevo davvero intenzione di fermarmi ad aiutarla con questo progetto però… non avevo davvero intenzione di fare nulla in particolare, suppongo."

show rin basic_absent_close at tworight
with charachange

"Guardo Rin, che mi guarda con aria vacua."

hi "Solo per questa volta."

show rin basic_awayabsent_close at tworight
with charachange

"Rin raccoglie un altro pennello e lo immerge in un altro tono di rosso pallido. Ci sono dozzine di ciotole simili tutto intorno alla sua area di lavoro. Da come sembra la scena potrebbe essere seduta qui da ore."

"Mi chiedo se è così. Però vorrebbe dire che ha saltato le lezioni, cosa che ovviamente non considererei improbabile per un personaggio quale è Rin."

"Verso un pochino di bianco e rosso nella ciotola, cercando di ottenere lo stesso colore che è già sul muro."

"Pare che mi sia impossibile riuscirci."

"E' davvero inconveniente che lei non ne abbia mischiato a sufficienza in primo luogo. Ottenere esattamente la stessa tonalità sarà impossibile, ma almeno posso provare di avvicinarmici per quanto riesco."

hi "Parlando di duro lavoro, anche quello non è un impegno enorme per te? E' un dipinto così grande e così via."

show rin basic_deadpan_close at tworight
with charachange

rin "Oh, non sono ancora vecchia e amareggiata a sufficienza da pensare così."

hi "Suppongo di no."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Hai supposto giusto."

show rin basic_deadpancontemplation_close at tworight
with charachange

rin "Le gambe mi fanno male però. Sono pesanti come piombo. Piombo fatto di mattoni."

hi "Per via della posizione?"

rin "Già, mi piace di più farlo in posizione orizzontale, se capisci di cosa sto parlando."

rin "Ma niente da fare. Non posso chiedere al muro di stendersi."

show rin negative_spaciness_close at tworight
with charachange

"Dicendo quello, si stiracchia un po', piegando le gambe e la schiena molto più di quanto un essere umano dovrebbe potere flettersi. La facilità con cui manovra il suo corpo è stupefacente."

show rin negative_annoyed_close at tworight
with charachange

show rin negative_spaciness_close at tworight
with charachange

"C'è un piccolo tic nella sua altrimenti vuota espressione - un attimo di dolore forse - mentre si stira i polpacci."

"Rin deve avere resistenza e destrezza molto superiori a quelle di una persona normale per essere in grado di vivere come vive, ma sta sfinendosi lavorando a questa cosa."

hi "Perchè ti spingi fino a un tal punto? Fai almeno una pausa o qualcosa del genere. Continua domani se va così male."

show rin basic_deadpannormal_close at tworight
with charachange

"Questo le fa fare una pausa."

"E una lunga, che sembra uno sbadiglio mentale."

"…"

show rin basic_deadpan_close at tworight
with charachange

rin "Non credo, Hisao."

rin "Non mi sto spingenndo, Hisao."

hi "Sembra proprio di sì."

show rin basic_deadpannormal_close at tworight
with charachange

rin "No. Questo non ha niente a che vedere collo spingere o tirare o niente di correlato a quel genere di cose."

show rin basic_awayabsent_close at tworight
with charachange

rin "C'è questo ragazzo."

hi "Un ragazzo?"

show rin basic_absent_close at tworight
with charachange

rin "Sì."

hi "Dove?"

show rin basic_deadpannormal_close at tworight
with charachange

rin "Al club d' arte."

hi "Ehmm… quindi?"

show rin basic_deadpan_close at tworight
with charachange

rin "E' cieco."

hi "Oh. Come si fa a dipingere se si è ciechi?"

show rin basic_awayabsent_close at tworight
with charachange

rin "Non ne ho idea."

hi "Così perchè è lì?"

show rin basic_absent_close at tworight
with charachange

rin "Quello è il punto. Lui è lì."

"Dovrebbe veramente dire più di una parola alla volta per far sembrare questa più una discussione e meno un interrogatorio."

show rin basic_awayabsent_close at tworight
with charachange

rin "Non può veramente fare nulla che chiameresti arte, giusto? Ma viene comunque. E dipinge."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Perchè?"

hi "Non lo so. Perchè?"

show rin basic_deadpan_close at tworight
with charachange

rin "Non lo so. E' per quello che ho chiesto."

hi "Quindi?"

show rin basic_deadpannormal_close at tworight
with charachange

rin "Non dipinge spesso ma penso che i suoi dipinti siano molto interessanti."

hi "Sono sicuro che lo siano."

show rin basic_lucid_close at tworight
with charachange

rin "Una volta ci ho provato. A dipingere a occhi chiusi."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Non  è stato troppo interessante. E per ripulire il pavimento c'è voluta una vita. Non ci ho riprovato."

show rin basic_deadpandelight_close at tworight
with charachange

rin "Ma sta diventando più bravo a scolpire."

hi "Vedo."

"Forse stava cercando di arrivare a un punto. Forse si è scordata di averne uno."

hi "Sembra che il club d' arte sia pieno di persone interessanti."

show rin basic_deadpan_close at tworight
with charachange

rin "Non proprio."

"Risposta piuttosto brutale, e non si è affatto accorta del sarcasmo."

hi "No?"

show rin basic_awayabsent_close at tworight
with charachange

rin "Proprio come ho detto. Non sono molto interessanti. Di solito non mi interesso molto a persone che non sono interessanti."

show rin basic_absent_close at tworight
with charachange

rin "Forse tu sì."

hi "Forse."

"…"

show rin basic_awayabsent_close at tworight
with charachange

rin "Ma quel ragazzo è interessante."

show rin basic_lucid_close at tworight
with charachange

rin "Forse sono come quel ragazzo, o forse tu lo sei. Forse tutti lo siamo."

rin "Facciamo cose che non possiamo fare, solo perchè possiamo."

"Quello era piuttosto profondo, penso, e glie lo dico."

hi "Sei una persona profonda."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Nah. Sono una persona veramente superficiale e sconsiderata. Me lo dicono sempre."

show rin basic_deadpanamused_close at tworight
with charachange

rin "Sapevi che posso pensare a solo quattro cose contemporaneamente?"

hi "No, ma ora lo so."

show rin basic_lucid_close at tworight
with charachange

rin "Ora sto pensando alla toilette delle ragazze al secondo piano, gelato al gusto di gelato, il mio dito centrale e un taglio di capelli."

show rin basic_awayabsent_close at tworight
with charachange

rin "Ho bisogno di un taglio di capelli."

show rin negative_spaciness_close at tworight
with Dissolve(0.1)

show rin basic_delight_close at tworight
with Dissolve(0.1)

show rin negative_spaciness_close at tworight
with Dissolve(0.05)

show rin basic_delight_close at tworight
with Dissolve(0.05)

show rin negative_spaciness_close at tworight
with Dissolve(0.05)

show rin basic_delight_close at tworight
with Dissolve(0.05)

show rin negative_spaciness_close at tworight
with Dissolve(0.1)

show rin basic_delight_close at tworight
with Dissolve(0.2)

"Scuote la testa vigorosamente, lasciando che i suoi corti e arruffati capelli volino in tutte le direzioni. Posso vedere che è una cosa che le piace fare."

show rin basic_awayabsent_close at tworight
with charachange

"Diventiamo silenziosi quando Rin fa distrattamente alcuni passi, muovendo qua e là qualche pennello. Il pensiero riguardante il club d' arte mi ronza in testa un po' più a lungo."

"Mi sento come se stessi camminando su terreni molto inesplorati per quanto riguarda l' arte. Da come vanno questi incontri con Rin, è come se stessi cominciando a fumare o roba del genere. Probabilmente dovrei smettere di parlare con lei."

"Non è che lei non mi piaccia, a dispetto della confusione che il suo essere se stessa causa, e non è che non mi piaccia neanche l' arte. Ho perfino disegnato per divertirmi qualche volta. Solo che non ho una vera spinta creativa o abilità tecnica."

"Così di solito, se devo disegnare qualcosa, mi viene la sindrome da carta bianca e mi congelo completamente."

"Quello, o riesco a disegnare qualcosa di deforme e prontamente resto frustrato dalla mia incapacità a mettere la figura nella mia testa su carta e abbandono senza nemmeno davvero tentare di fare uno sforzo."

"A differenza di questa ragazza. Anche lei mi frustra. Stare con lei è come guardare in uno specchio che non riflette nulla."

"Fa dubitare della sanità dell' atto."

show rin basic_absent_close at tworight
with charachange

"Rin siede sulla sua scatola, ondeggiando da un lato all' altro, apparentemente a suo agio nello scomodo silenzio."

"Mi sta fissando di nuovo, o forse sta fissando un punto sopra alla mia spalla. Non riesco a capire veramente cosa i suoi occhi stiano mettendo a fuoco."

"Sto pensando di andarmene così che lei possa continuare a lavorare indisturbata e che io possa fare quello che voglio fare da solo. Non è come se avessi qualcosa che devo fare oggi…"

hi "Oh, cavoli."

show rin basic_deadpan_close at tworight
with charachange

rin "Dove?"

hi "Da nessuna parte, mi sono solo dimenticato di dire ad Hanako che Lilly la stava cercando."

hi "La conosci? Dalla mia classe?"

show rin basic_deadpanamused_close at tworight
with charachange

rin "Oh, lei. La Misteriosa Ragazza del Bagno."

show rin basic_amused_close at tworight
with charachange

rin "Quella persona è buffa. L' ho vista andare al bagno cinque volte durante un intervallo tre settimane fa. Sono sicura che sia il record mondiale."

show rin basic_deadpandelight_close at tworight
with charachange

rin "E' stato molto misterioso."

hi "E' per quello che la chiami Misteriosa Ragazza del Bagno?"

show rin basic_absent_close at tworight
with charachange

rin "Che altra ragione potrebbe mai esserci? Bè, se c'è è un mistero eterno. Non l' ho seguita fin là dentro."

"…"

show rin basic_awayabsent_close at tworight
with charachange

rin "Forse era la settimana prima di quella? E' possibile."

"…"

rin "Guardarla mi fa venire fame."

hi "Non dire così."

hi "Almeno, non quando Hanako sta ascoltando."

show rin basic_deadpannormal_close at tworight
with charachange

"Rin si gira per guardarmi senza espressione, come se non fosse sicura del perchè l' ho rimproverata."

"Ma lei non mostra di capire più di prima, così a questo punto lascio perdere."

hi "Così vuoi andare a cena allora?"

show rin basic_awayabsent_close at tworight
with charachange

rin "No. Non ancora."

"Rin ha rivolto il suo sguardo affamato verso il muro, e sembra leggermente più energica, o almeno leggermente meno letargica di prima."

"E' come se il muro fosse un opponente che deve sconfiggere, qualcosa che deve battere prima di potersi concedere la cena."

"Questa è la sensazione che ricevo. Un bizzarro senso di empatia mi sopraffà e mi fa sorridere un pochino tra me e me."

"Con tutta la sua stranezza, Rin è veramente tosta."

hi "Io me ne vado."

hi "Divertiti."

stop music fadeout 3.0

"Rin ha già preso un pennello e lo sta intingendo nella pittura, così ovviamente non può più sentirmi o non risponde nulla neanche se ci riesce."



#*******************************

label it_A24:

scene bg school_scienceroom at bgleft
show hanako emb_timid at Position (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Position(xanchor=0.5, xpos=0.35)
show misha hips_frown at Position(xanchor=0.5, xpos=0.15)
with None

show bg school_scienceroom at right #omg hax
show hanako emb_timid at right
show shizu behind_frown at offscreenleft
show misha hips_frown at offscreenleft
with charamove

hi "Devi trovarla? Ti stava cercando stamattina ma immagino che non vi siate incontrate."

"Aspetta per un po' senza rispondere alla semplice domanda, con aria terribilmente insicura di sapere se è giusto rispondere a una domanda del genere."

show hanako emb_blushtimid at right
with charachange

ha "G…già."

hi "Posso venire con te."

hi "Se è okay."

show hanako emb_downtimid at right
with charachange

show hanako emb_blushtimid at right
with charachange

"Hanako annuisce a malapena, ancora in guardia, spalle rigide come fossero di legno. Ho l' impressione che dopotutto potrebbe sentirsi più a suo agio da sola, ma è troppo tardi per cambiare idea adesso."

"Ha quest' espressione veramente preoccupata che sembra avere quasi costantemente, che fa stare me costantemente in guardia. Mi chiedo perchè."

"Più o meno capisco perchè sembra essere sempre così diffidente… o forse è meglio dire, perchè possa esserci una persona come lei."

"Ma continuo a non avere idea su come dovrei comportarmi vicino a una persona del genere."

hi "Presto sarà ora di cena. Avevi intenzione di mangiare con Lilly?"

show hanako emb_downtimid at right
with charachange

show hanako emb_blushtimid at right
with charachange

"Annuisce lievemente."

"Così deve avere provato a entrare nella mensa."

"Bè, c'è un po' di folla per la cena, così come la mensa è affollata durante il pranzo."

"Non è altrettanto fitta perchè la cena è più lunga dell' ora del pranzo, ma posso capire perchè Hanako sarebbe scoraggiata dall' entrare."

"Raccolgo la mia borsa e ce ne andiamo. Hanako corre un po' per seguire il mio passo iniziale, così rallento per adattarmi alla sua velocità."

stop music fadeout 2.0

scene bg school_hallway3
with locationchange

"Non ci vuole molto prima che camminiamo a un passo confortevole per il corridoio."

show hanako def_worry at right
with charaenter

"Sembra quasi che stiamo facendo una passeggiata insieme; qualcosa che non posso dire di avere mai fatto prima in compagnia di una ragazza."

"Hanako non sembra stare pensando la stessa cosa però. Anche se stiamo camminando allo stesso passo, non si avvicina mai tanto che io la possa toccare."

"Immagino che si senta ancora un po' a disagio in mia presenza. Considerato quanto è timida, non sembra esserci modo di evitarlo, almeno per ora."

play music music_dreamy fadein 0.3

scene bg school_cafeteria
with locationchange

"Una volta che siamo arrivati in mensa, non c'è più molto affollamento, ma Lilly non si vede da nessuna parte."

show hanako emb_downsad
with charaenter

"Il capo di Hanako si china ancora più in basso del solito."

hi "Hai già guardato da qualche altra parte?"

show hanako basic_worry
with charaenter

ha "S-solo in biblioteca… stavo leggendo…"

"Così passa in biblioteca le lezioni che salta."

hi "Ah, non proprio una ricerca approfondita allora. Bè, se dovessi indovinare, penso che sarebbe nella sua classe come ha detto Shizune, giusto?"

show hanako cover_worry
with charachange

ha "G-giusto."

show hanako basic_normal
with charachange

"Col più lieve di cenni di assenso, Hanako accetta il mio ragionamento."

"Dio, è talmente impacciata."

"E' come se avessi bisogno di guanti di seta a doppio strato imbottiti anche solo per iniziare a interagire con lei."

"Un po' di conversazione potrebbe aiutarla ad abituarsi di più a me. Non è difficile capire che il silenzio tra di noi sta pesando sui nostri pensieri."

hi "Così, tu e Lilly di solito passate il tempo insieme dopo le lezioni, giusto?"

show hanako emb_downtimid
with charachange

ha "S-sì."

"Non sono ben sicuro di cosa mi aspettassi dalla sua risposta, nè perchè ho posto la domanda. Era piuttosto ovvio, dopotutto."

"Lei non sembra neanche il tipo che coltiva un circolo sociale, quindi sospetto che Lilly possa in effetti essere la sua unica amica."

hi"Essere in classi diverse deve essere un fastidio, immagino."

"Annuisce seccamente, quasi di riflesso. Paragonando con le azioni e parole attentamente valutate di Lilly, Hanako si affretta a rendere le sue risposte quanto più rapide e brevi possibile."

show hanako emb_downsmile
with charachange

ha "Lilly… passa a trovarmi, però. Anche quando ha da fare…"

"Sorride lievemente mentre lo dice, evidentemente apprezzando il fatto che Lilly faccia uno sforzo per aiutarla."

"E' piuttosto grazioso, a dire il vero. Non c'è bisogno di dire altro, emtrambi contenti che la discussione abbia raggiunto un termine."

scene bg school_staircase2
with locationchange

"Mentre ascendiamo le scale verso l' atrio ci incontriamo con un gruppo di studenti che le stanno scendendo come un branco di pesci che si muove da una zona di pascolo a un' altra."

show hanako cover_worry_close at Position(xanchor=0.4, xpos=0.0)
with charaenter

"Sembrano stare facendosi gli affari propri, ma prima che possa accorgermi di quel che sta facendo, Hanako si è mossa dietro di me."

hi "Ehi, stai bene?"

show hanako basic_worry_close at Position(xanchor=0.4, xpos=0.0)
with charaenter

ha "C-continua a camminare…"

hide hanako
with charaexit

"Gli studenti ci incrociano senza degnarci di uno sguardo, e Hanako torna in posizione al mio fianco mentre entriamo nell' edificio, il suo temporaneo sollievo dall' ansietà praticamente scomparso."

scene bg school_lobby
show hanako basic_normal
with locationchange

"Anche mentre saliamo verso il secondo piano, lei non sembra rilassarsi."

"Non è come se non avessi mai conosciuto persone timide prima, o perfino ragazze timide, ma Hanako sembra essere ben oltre quello che chiamerei normale nella sua paura degli altri."

"Se non fosse stato per Lilly che ha agito da mediatrice, dubito che Hanako sarebbe mai perfino stata in grado di camminare al mio fianco così. Sembra andare completamente in cortocircuito in presenza di altri."

"Il resto della camminata fino alla classe di Lilly procede in un teso silenzio, mentre io mi rammarico della sua completa incapacità di socializzare."

scene bg school_hallway3
with locationskip

stop music fadeout 2.0

"Dopo aver salito le scale, il rumore proveniente dalla classe di Lilly è udibile fin da metà del corridoio. Non mi aspettavo affatto un tale fracasso."

hi "Bè, immagino che l' abbiamo trovata…"

"Non è stato difficile. Mi chiedo se Hanako sia venuta qui prima e poi mi sia venuta a cercare per avere supporto."

"Bene, se fosse vero, allora almeno sta cominciando a fidarsi un poco di me. Quello può solo essere un bene."

"Finalmente, raggiungiamo la porta della classe 3-2. Apro la porta, mentre Hanako si posiziona non proprio furtivamente dietro di me."

play music music_another fadein 0.3
play ambient sfx_crowd_indoors fadein 0.3

scene bg school_room32 at bgright
with locationchange

"Dentro c'è un alveare di attività, apparentemente ogni studente della classe sta parlando allo stesso tempo mentre tutti lavorano frettolosamente sui loro separati compiti."

"Giudicando dai barattoli di pittura, le decorazioni e gli striscioni che stanndo venendo costruiti, il tutto deve essere per il festival scolastico in arrivo."

"Suppongo che la mia priorità debba essere di trovare Lilly…"

"…{w} Eccola."

"Trovarla in mezzo alla confusione è sorprendentemente semplice, soprattutto grazie al suo aspetto."

"Con un paio di studenti riuniti attorno a lei mentre è in piedi di fronte alla classe, sembra che sia incaricata delle preparazioni, o almeno impegnata a organizzarle."

"Ci facciamo cautamente strada attraverso i vari studenti accoccolati sul pavimento per carenza di posti a sedere, e quando finalmente raggiungiamo Lilly alzo una mano esclusivamente per la forza dell' abitudine."

hi "Ciao, Lilly."

show lilly basic_surprised
with charaenter

"Solleva il capo interrompendosi dal parlare con una ragazza considerevolmente più piccola che deve essere una sua compagna, cercando di ascoltare quanto meglio può."

li "Scusa, chi…"

hi "Ah, scusa. Hisao. Ho anche Hanako con me."

show lilly basic_smile
with charachange

show lilly basic_smile at twoleft
show bg school_room32
with charamove

show hanako basic_normal at tworight
with charaenter

ha "C-ciao."

"E' piuttosto nervosa. Considerando il numero di persone tutto intorno, non è molto difficile capire il perchè."

"Lilly prende un attimo di pausa per valutare la situazione prima di rivolgersi nuovamente all' altra studentessa."

show lilly basic_smileclosed at twoleft
with charachange

li "Per il momento, chiedi consiglio a Moriya. Kenji è già occupato a dipingere uno di quegli striscioni."

"Un rapido cenno di assenso e scappa via, dita che scivolano attentamente lungo la superficie del muro per orientarsi."

$ renpy.music.set_volume(0.1,1.0)

"Aspetta… Kenji? Quel Kenji?"

"Mi giro in fretta, piegandomi di lato per vedere oltre Hanako."

"E infatti, in un angolo della stanza, Kenji è piegato su di una striscia di stoffa mentre la dipinge. I suoi occhi sono a pochi centimetri dal pennello, ricordandomi quanto doveva stare vicino per distinguere la mia faccia quando lo ho incontrato."

$ renpy.music.set_volume(1.0,1.0)

show lilly basic_smile at twoleft
with charachange

li "Scusatemi. La nostra classe non ha molti studenti che possono vedere anche solo parzialmente, quindi sono molto richiesti."

"E' vero, la classe 3-2 era specialmente per studenti con problemi di vista. Prepararsi per il festival deve essere piuttosto duro per loro."

li "E scusami, Hanako, per non essere riuscita a farcela in tempo. Ora siamo nel bel mezzo di una fase critica e quella diabolica presidentessa mi sta sul collo per puro divertimento, così sono in una posizione rischiosa."

ha "E' okay."

"Posso percepire la tensione irradiarsi dalla normalmente tanto composta e calma Lilly. Le piccole differenze nelle sue espressioni, il suo modo teso di parlare, come se avesse fretta di muoversi avanti quanto prima possibile… è sotto pressione."

"E ovviamente anche Lilly è ancora di cattivo umore dopo l' alterco di prima con Shizune."

hi "Serve una mano? Potrei darvi dell' aiuto se ne avete bisogno. Forse anche Hanako potrebbe farlo."

"La possibilità di concentrarsi su qualcosa le farebbe bene, ma dubito che abbia il coraggio di chiedere. Subito dopo lei annuisce in conferma, così sono fiducioso di aver fatto la mossa giusta."

"Piuttosto insolitamente, Lilly emette un percettibile sospiro di sollievo."

show lilly basic_weaksmile at twoleft
with charachange

li "Ah, questo è un sollievo. Potremmo veramente finire prima che tutti vadano a cena, ora."

show lilly basic_listen at twoleft
with charachange

li "Potresti aiutare la persona che sta dipingendo lo striscione grande? E' un grosso lavoro per lui, ma nessun altro lo può aiutare."

hi "Kenji? Certo."

show lilly basic_surprised at twoleft
with charachange

"Sembra sorpresa che lo conosca. Non posso davvero biasimarla."

li "Immagino che già vi conosciate?"

hi "Le nostre stanze sono adiacenti. Difficile non incontrarsi, davvero."

show lilly basic_ara at twoleft
with charachange

li "Bene, è bello vedere che ti stai facendo degli amici così presto."

"Amico… mi chiedo se quella è la parola giusta da usare per lui."

"Il silenzio di Hanako durante il dialogo mi ricorda la ragione per cui l' ho persuasa ad aiutare in primo luogo."

hi "Allora andremo ad aiutarlo. Sa lui che cosa bisogna fare, giusto?"

stop music fadeout 2.0

show lilly basic_smileclosed at twoleft
with charachange

li "Esatto. Chiedete se avete dei problemi."

hide lilly
hide hanako
with charaexit

"Con un coro di assenso, io e Hanako cominciamo un altro viaggio attraverso l' aula."

"Kenji siede curvo sul pavimento, il suo sguardo fisso sul cotone bianco di fronte a sè."

show kenji tsun at Position(yanchor=0.45, ypos=1.0)
with charaenter

hi "Ehi Kenji."

"…Nessuna risposta. Continua a trascinare il suo pennello intinto nella pittura lungo il grande kanji mezzo dipinto che è tracciato a matita sulla tela."

hi "Kenji?"

show kenji tsun
with charamove

ke "Eh? Cosa? Chi è?"

"Se questo è il modo in cui tratta i compagni di classe, c'è poco da stupirsi che stia lavorando su questo da solo."

hi "Sono io. Hisao. Dai-{w=.5}{nw}"

ke "Giusto, giusto, quello lo so amico. Cosa stai facendo qui, però?"

"La sua attitudine sprezzante mi secca."

"Deve essere il tipo che si concentra molto sul suo lavoro, e detesta essere disturbato da qualcuno finchè non ha finito, immagino."

show kenji tsun at twoleft
show bg school_room32 at bgleft
with charamove

show hanako cover_distant at tworight
with charaenter

"Mentre parliamo, il suono dei passi di Hanako che fa capolino da dietro di me mi ricorda che c'è anche lei."

hi "Sono solo qui per aiutare collo striscione. Io e Hanako, cioè."

show hanako cover_worry at tworight
with charachange

ha "S… Salve…"

show kenji happy at twoleft
with charachange

ke "Oh. Uh, ehilà. Suppongo sia okay."

"Appena Hanako entra nell' equazione, il suo comportamento cambia completamente. La sua improvvisa falsa ospitalità è leggermente inquietante."

"Oh, giusto. Donne. Ripensandoci, questa potrebbe non essere stata una grande idea dopotutto."

show bg school_room32 at bgleft
show kenji neutral_close at left
show hanako basic_distant_close at right
with locationskip

"Io e Hanako ci piazziamo malvolentieri dal lato opposto dello striscione di stoffa rispetto a Kenji, notando le numerose piccole lattine di pittura poggiate a terra tutto intorno."

"Classe 3-2… chiosco di spaghetti?"

hi "Voi ragazzi vendete spaghetti al festival di domenica?"

show kenji happy_close at left
with charachange

ke "Già, qualche chiosco fuori. O roba del genere."

"“O roba del genere?” La sua natura vaga accende una discreta quantità di sospetti in me. Il lavoro per prima cosa, però."

hi "Così come vuoi che ci dividiamo? Noi facciamo i bordi mentre tu fai il testo? O vuoi fare il contrario e fare i bordi?"

show kenji tsun_close at left
with charachange

ke "Il testo è mio. Voi fate i bordi."

"E' sorprendentemente deciso sull' argomento."

show hanako basic_distant_close at right
with charachange

"Mentre allungo la mano per prendere un pennello, noto che Hanako sta già chiedendosi quali colori usare."

show hanako basic_normal_close at right
with charachange
show hanako basic_distant_close at right
with charachange
show hanako basic_normal_close at right
with charachange

"Quando inizio a dar di pennello sulla stoffa, lei ha già cominciato un delicato motivo. Sembra che la mia idea di distrarla da tutti quelli che la circondano abbia funzionato."

"Con una pennellata di blu scuro, noi tre iniziamo silenziosamente a lavorare."

"Non prima che Kenji sfrutti il fatto che Hanako sta lavorando per chinarsi verso di me e bisbigliare con aria cospiratoria, però."

play music music_kenji fadein 0.3

show bg school_room32
show kenji tsun_close
show hanako basic_normal_close at offscreenright
with charamove

show kenji neutral_close
with charachange

ke "Okay amico, perchè sei qui?"

hi "Hanako voleva solo dell' aiuto per trovare Lilly, questo è tutto."

show kenji tsun_close
with charachange

"Apparentemente disapprova le mie motivazioni."

ke "Capisco. Sembra che ti abbia giudicato male."

show kenji happy_close
with charachange

ke "Stai infiltrandoti tra loro, non è vero? Andando sotto copertura?"

"Avrei dovuto immaginarlo. Lasciargli ignorare la verità sarebbe probabilmente meglio di mentirgli spudoratamente o infastidirlo, in tutti i casi."

hi "E' per quello che tu sei qui?"

ke "Ovviamente. E' uno schifo, ma non c'è maniera migliore per ottenere informazioni di provvedere da soli."

show kenji tsun_close
with charachange

ke "Dobbiamo essere uniti, amico. Questa è una scuola dura, un mondo duro."

hi "Sì, molto duro."

"Non capisce il vero intento di quel che dico mentre si raddrizza, convinto che sia solidale con la sua causa. Farò meglio a lavorare."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene bg school_room32
show kenji neutral_close at left
show hanako basic_normal_close at right
with shorttimeskip

ha "Finito."

hi "Sembra che anche io abbia finito. Bel lavoro."

"Noi due congiungiamo le linee dei nostri motivi, il mio una copia quanto più simile sono riuscito a fare del suo."

scene bg school_room32
with locationskip

"Con un grugnito, mi sollevo dal pavimento e guardo in giro."

"A parte me e Hanako, nell' aula sono rimasti solo Kenji che sta finendo un cartello oltre a Lilly e un paio di studenti che stanno parlando tra di loro."

"Guardando il mio orologio, non c'è da sorprendersi. Sta facendosi piuttosto tardi."

show hanako basic_normal at Position(yanchor=0.0, ypos=1.0)

hi "Serve una mano?"

play music music_normal fadein 0.3

show hanako basic_normal
with charamove

"Offro una mano a Hanako, che lei usa per tirarsi in piedi."

"Mentre lo fa, non posso evitare di guardare il suo polso; se le sue cicatrici si estendono fino a lì, quanto del suo corpo è rimasto bruciato?"

show hanako emb_downtimid
with charachange

"Però sento un senso di colpa dato che lei subito si copre il polso con l' altra mano."

hi "Ha un bell' aspetto, non è vero?"

show hanako emb_timid
with charachange

"Sembra sorpresa per un momento prima di accorgersi che sto parlando dello striscione."

show hanako basic_bashful
with charachange

ha "Suppongo… di sì."

"Il suo sorriso dimostra che prova un po' di orgoglio nel risultato, proprio come me."

hide hanako
with charaexit

"Ora che il pavimento è molto più ordinato dato che le decorazioni sono state piazzate su banchi e scaffali, è molto più facile arrivare fino a Lilly attraversando la stanza."

hi "Abbiamo finito collo striscione. Immagino che sia tutto quel che c'era da fare ?"

show hanako basic_smile at tworight
show lilly basic_smileclosed at twoleft
with charaenter

"Lilly china il capo in apprezzamento."

show lilly basic_smile at twoleft
with charachange

li "Grazie Hisao, Hanako. Se c'è qualche modo in cui vi posso ringraziare…?"

hi "Non importa. E' meglio che star seduto nella mia stanza a studiare, comunque."

show hanako basic_normal at tworight
with charachange

ha "Anche a me va bene."

"Annuisce, prima di ricordarsi improvvisamente di un' ultima persona."

show lilly basic_surprised at twoleft
with charachange

li "Oh, Kenji è ancora qui?"

"Mentre apro bocca, Kenji risponde dall' altro capo della stanza."

ke "Già, ho appena finito."

"Colloca attentamente il suo cartello su un pezzo di scaffale libero perchè si asciughi, prima di camminare frettolosamente oltre di noi e fuori dalla porta."

show hanako basic_normal
show lilly basic_surprised at left
show bg school_room32 at bgleft
with charamove

show kenji neutral at Position(xalign=1.15)
with charaenter

ke "Ci vediamo amico."

hi "Ciao."

hide kenji
with charaexit

show hanako basic_normal at tworight
show lilly basic_surprised at twoleft
show bg school_room32
with charamove

"I due studenti rimanenti salutano Lilly prima di andarsene a loro volta, lasciando noi tre soli."

hi "Bene, suppongo che con quello siano andati tutti."

show lilly basic_displeased at twoleft
with charachange

li "Spero che non dovremo più fare niente del genere."

hi "Lavorare dopo la scuola?"

show lilly basic_concerned at twoleft
with charachange

li "Esatto. I piani della classe quest' anno erano ambiziosi. Forse troppo ambiziosi."

show hanako emb_smile at tworight
with charachange

ha "I chioschi sembrano belli, però."

hi "Ha ragione, si vede che ci si è lavorato sopra un sacco."

show lilly basic_ara at twoleft
with charachange

li "Oh cielo, sono sicura che molti di noi sarebbero felici di sentirlo dire. Almeno ora non è rimasto molto lavoro da fare fino al festival vero e proprio."

show hanako basic_smile at tworight
with charachange

ha "Umm… Si sta facendo piuttosto tardi. Vogliamo andare?"

show lilly basic_smileclosed at twoleft
with charachange

li "Probabilmente è una buona idea. Anche tu stai tornando ai dormitori, Hisao?"

hi "Già, credo che vi seguirò."

stop music fadeout 2.0

scene bg school_gardens2_ni
with locationskip

$ renpy.music.set_volume(0.1,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3

"L' illuminazione notturna fa sembrare i giardini davvero diversi. Paragonate alla solita apparenza di verde lussureggiante, le cose sono molto più calme."

"Dato che è così tardi, l' assenza di studenti probabilmente aiuta. Se ne possono vedere uno o due che si affrettano verso e dai dormitori cercando di spremere fino all' ultimo il loro imminente coprifuoco, ma non di più."

"Tutto quel che si può sentire sono i nostri passi, in aggiunta al bastone di Lilly che regolarmente batte il terreno di fronte a lei."

"E' bello potersi finalmente rilassare un po' dopo la folle corsa durante la scuola."

"Senza neanche accorgermente, faccio un piccolo sbadiglio."

show lilly cane_smile_ni at twoleft
show hanako basic_normal_ni at tworight
with charaenter

li "Stanco?"

hi "Già. Mi sto ancora abituando al ritmo delle cose, suppongo."

hi "La… uh… cosa… con Shizune mi ha preso un po' alla sprovvista, però."

"Stringo un po' i denti alla candida menzione del loro piuttosto pubblico alterco. Detto quello, voglio scoprire cosa accidenti ci sia dietro."

show lilly cane_displeased_ni at twoleft
with charachange

li "Ah… riguardo a quello…"

li "Mi dispiace che sia stato così pubblico. Shizune e io… ci conosciamo da un certo tempo."


label it_A24c:
#lol label order

# If he pissed off Lilly

"La sua voce sembra leggermente irritata mentre ricorda Shizune, e ripensandoci, probabilmente la mia parte negli eventi."

show lilly cane_listen_ni at twoleft
with charachange

li "Se tu non la aiutassi, lo apprezzerei. L' ultima cosa di cui ha bisogno è di essere incoraggiata."

"Bene, questo conferma i miei sospetti a quel tempo. La ho fatta infuriare."

"Detto quello, mentre posso accidentalmente averla data in pasto ai lupi, non potevo sapere e qunindi non sono in una posizione dove dovrei scusarmi."

"Un paio di minuti di teso silenzio passano tra di noi, con gli occhi di Hanako che sfuggono a destra e a manca."

"Abbandonando il prospetto di ogni forma di scuse, Lilly desiste dalla lotta e cambia argomento."



label it_A24d:

# If he didn't

"La sua voce sembra leggermente irritata mentre ricorda Shizune, ovviamente maldisposta a parlarne più a lungo."

show hanako basic_distant_ni at tworight
with charaenter

"Lancio uno sguardo ad Hanako per capire il suo punto di vista, ma la sua espressione è, non stranamente, evasiva e difficile da leggere."

"In tutti i casi suppongo che il fatto che lei si sia scusata valga qualcosa, anche se la mia curiosità non è soddisfatta."



label it_A24e:

# End conditionals

stop ambient fadeout 2.0

play music music_lilly fadein 0.2

show lilly cane_weaksmile_ni at twoleft
with charachange

li "In ogni caso, sarò felice una volta che il festival sarà terminato."

"Il cambio di discorso è benvenuto, e pulisce velocemente via l' atmosfera pesante."

hi "Posso immaginarlo. I festival alla mia vecchia scuola erano molto più modesti di questo."

show lilly cane_smileclosed_ni at twoleft
with charachange

li "Yamaku insiste sull' idea di una comunità scolatica, così lo staff cerca di rendere i nostri festival e altre cose del genere delle occasioni speciali."

hi "Però sono gli studenti che fanno il lavoro. Che mondo ingiusto."

show lilly cane_giggle_ni at twoleft
show hanako emb_emb_ni at tworight
with charachange

"Hanako e Lilly ridacchiano entrambe in accordo, gustandosi il fatto che nessun membro dello staff è in grado di sentirci brontolare."

show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with charachange

li "Immagino che provenire da una severa scuola solo per ragazze mi abbia aiutato un po' con Yamaku. Al paragone, Yamaku è molto più rilassata."

"Quello spiegherebbe molto del suo modo di parlare e comportamento beneducati, in ogni caso."

scene bg school_dormext_half_ni
show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with locationskip

"Quando arriviamo ai dormitori, giunge finalmente il momento di dirigerci verso le nostre rispettive stanze."

hi "Arrivederci Lilly, Hanako."

"Entrambe annuiscono cortesemente prima di procedere verso i dormitori femminili, accanto a quelli maschili."

stop music fadeout 2.0

play ambient sfx_cicadas fadein 0.3

hide lilly
hide hanako
with charaexit

"Come ci si può aspettare da un simile arrangiamento, c'è un membro dello staff che disinvoltamente pattuglia all' esterno per impedire qualunque attività notturna."

"Oltrepassandolo, stiro rapidamente le mie braccia e mi strofino il collo, entrambi decisamente doloranti dopo aver lavorato sul pavimento così a lungo, prima di camminare fino alla mia stanza."

"E' bello avere una direzione da seguire, però. Dopo così tanto tempo in ospedale, i fatti quotidiani di studiare, compiti e insegnanti sembrano quasi una benedizione."

"Immagino che se le cose continuano così, il mio soggiorno a Yamaku potrebbe finire per essere decente."

stop ambient fadeout 2.0
$ renpy.music.set_volume(1.0,0.0, "ambient")


label it_A24a:

scene bg school_dormhisao_ni
with locationskip

"Attenendomi all' assillante vocina dell' infermiere che sento nella mia testa, regolo la mia sveglia in modo che mi faccia alzare abbastanza presto da andare di nuovo a fare jogging."

"Ho fatto una promessa e ho intenzione di mantenerla. E inoltre, Emi finirà per fare la spia se non mi faccio vedere."

"Ma non è poi così male."

scene black
with shuteye


label it_A24b:

scene bg school_dormhisao_ni
with locationskip

"Mi sento stanco così regolo la mia sveglia in modo che mi faccia alzare quanto più tardi posso, al contempo lasciandomi arrivare in tempo per l' inizio delle lezioni."

"La vocina dell' infermiere mi sta quasi assillando nella mia testa parlando di corse mattutine. Decido di recuperare andando a fare una camminata domani dopo la scuola."

"Scommetto che a Emi non importerà comunque."

scene black
with shuteye

return
