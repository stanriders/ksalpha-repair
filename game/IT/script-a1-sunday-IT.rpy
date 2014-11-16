label it_A38:
#Dawn of the Final Day
    
scene black
with None

scene bg school_dormhisao
with openeye


"Il giorno dopo, mi sveglio sentendomi un po' stordito. E' già quasi mezzogiorno."

play music music_daily fadein 1.0

"Dormire fino a tardi non è un problema, dato che è domenica e non ci sono lezioni."

"Non solo una domenica, però, ma anche il giorno del festival."

"Dalla mia finestra posso già vedere alcune persone del chiosco della soba che stanno lanciando spaghetti su piatti per avventori desiderosi di cibo di bassa qualità."

"Inghiotto una manciata delle mie medicine della mattina e considero come passare la giornata."

"Ci saranno alcuni esami durante la prossima settimana, ma non li considero minacciosi quanto altri, così non sono tanto preoccupato al riguardo quanto probabilmente dovrei essere."

"Senza nessuna urgente obbligazione riguardante la mia educazione, dovrei essere libero di passare la giornata al festival come mi pare."

scene bg school_dormhallway
with locationchange

"Terminando le mie abluzioni mattutine, esco nel corridoio, con l' intento di uscire e trovare qualcosa da mangiare."

"Passando di fronte alla sua porta, decido impulsivamente di chiedere a Kenji cosa farà oggi."
   
"Sono curioso di sapere se ha dei piani, dato che tutti stanno facendo qualcosa."

"D' altra parte, posso immaginarmelo ad aver costruito un rifugio a prova di suono nella sua stanza."

"O probabilmente qualcosa tipo un forte, completo con un cartello che dice “Ragazze Non Ammesse”."

"… e con “Ragazze” cancellato e “Persone” scarabocchiato a mano al di sotto."

stop music fadeout 0.5

play sound sfx_doorknock2

"Bussando alla porta della sua stanza che è fortunatamente priva di qualunque tipo di cartello, sento di nuovo l' inquietante scattare di almeno dieci lucchetti che vengono aperti. La porta si apre uno spiraglio."

show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)

ke "Chi è?"

hi "Dovresti chiederlo prima di aprire la porta."

play music music_kenji fadein 1.0

show kenji neutral
show bg school_dormhallway at bgright
with charamove

ke "Oh, sei tu. Diavolo, è presto."

hi "Non è proprio così presto."

show kenji happy
with charaenter

ke "Cosa c'è, amico?"

hi "Nulla, volevo solo chiedere cosa farai oggi."

hi "Metà della scuola è già là fuori."

show kenji rage
with charaenter

ke "Fuori dove? Perchè?"
   
hi "Cosa?"

ke "Cosa “cosa”? Oggi c'è qualcosa di speciale? Perchè sono lì? Chi sono?"

show kenji tsun
with charachange

ke "Li posso sentire. E' rumoroso… non dirmi… E' cominciata l' invasione?"

"Sembra improvvisamente più allarmato."
   
show kenji neutral
with charachange

ke "Che giorno è, amico?"
   
hi "Già, immagino che tu non possa vedere i grossi chioschi di legno là fuori, e la gente che vende roba…"

ke "Di che diavolo stai parlando? Tengo le mie tendine sempre chiuse per ostacolare i cecchini."

hi "Uhh, è il festival. Lo sai quello… vero?"

show kenji tsun
with charachange

ke "Oh merda, è oggi? Ah, dannnazione. Ah… dannazione. Maledizione."

ke "Non posso credere di essermi dimenticato, non ho ancora finito il mio forte. Questo è male."

ke "Oggi sarà una pessima giornata… Hai fatto bene a dirmelo, amico. Questa sarà una brutta giornata."

hi "Perchè?"

show kenji neutral
with charachange

ke "Oh diavolo, saranno dappertutto. Le persone. Fuori dalla mia finestra. Socializzando!"

"Kenji si sfrega nervosamente le tempie, e improvvisamente sembra stare molto male."

show kenji tsun
with charachange

ke "Sarà un rumore d' inferno. Dannazione, e volevo uscire oggi, ma adesso è rovinato, è tutto rovinato."

ke "Questo è terribile. Fa schifo. Fa schifo!"

ke "Che diavolo, questo fa veramente schifo. Adesso non posso andare da nessuna parte. Non c'è posto dove fuggire."

"Kenji sembra nervoso. Si potrebbe perfino dire che stia abbondantemente uscendo dai gangheri."

show kenji neutral
with charachange

ke "Non ci posso credere. Così ecco cos' era oggi."

ke "Dannnazione, e non mi sono nemmeno potuto preparare."

show kenji tsun
with charachange

ke "Non ho nemmeno potuto farmi forza e adesso è qui e non posso fare nulla. Avresti dovuto dirmelo prima, fratello. Voglio dire, almeno, lo so, ma… avrei potuto saperlo prima! Immagina cosa avrei potuto concludere…"

hi "Scusa. Pensavo che lo sapessi."

hi "Così immagino che non farai niente oggi?"
 
hi "Perfino il tempo è bello. Ieri era davvero ventoso, così pensavo che oggi sarebbe stato freddo. Non lo è, però, quindi non c'è davvero ragione per starsene al chiuso. Già, dovresti fare un giro al festival."

"Kenji geme e si copre la faccia colle mani."

ke "Agh, no, no! Non posso farlo. Mi mangeranno vivo là fuori, lo so."
    
"Quella doveva essere una battuta, ma la ha detta con una faccia talmente seria. Relativamente seria."
    
show kenji happy
with charachange

ke "Che hai intenzione di fare? Dovremmo stare insieme qui dentro, puoi aiutarmi a costruire il mio forte. Potremmo ancora farcela se lavoriamo insieme."



label it_A38a:
#If on Shizune's route

hi "Dovrò passare il tempo col consiglio studentesco, dato che ho perso una scommessa."

"E' buffo. Ero convinto che il prezzo da pagare per aver perso contro Shizune al suo stupido gioco sarebbe stato molto più alto. Questo è solo un pretesto per passare del tempo con lei. In tal caso, immagino che voglia solo che mi diverta."

"Anche se non riesce a essere diretta e a rendere le sue intenzioni chiare, possono essere buone intenzioni dopotutto, e penso che stia cominciando a piacermi di più."

hi "Potrei non andare, ma sarebbe uno spreco. E ho anche voglia di andare. Voglio dire, lo sai, oggi sembra un giorno abbastanza eccitante. Se non altro, sarà interessante."
    
show kenji tsun
with charachange

stop music fadeout 1.0

ke "Il consiglio studentesco? Cosa? Esiste ancora?"

ke "Non sono tipo, due tizi?"

hi "Sono entrambe ragazze."

play music music_tension

show kenji rage
with charachange

ke "Davvero? Sono carine? Dannazione, no, aspetta… sono carine?"

ke "No! Non ha importanza! Ho sentito che la presidentessa del consiglio studentesco è pazza… che chiunque sia non parla mai e dà solo ordini per mezzo di lacchè."

show kenji tsun
with charachange

ke "Merda, sono uguali in tutte le scuole… Sembra una stronza dal cuore di ghiaccio. Stronze dappertutto."

ke "Se sono due ragazze, ti battono in rapporto di forza due a uno. E' una situazione pericolosa, fratello. Chissà cosa può succedere."

ke "Dannazione, il consiglio studentesco sono solo due donne, ma hanno così tanto potere."

ke "Devono essere fermate."

ke "Posso vederle, mentre fanno piani per avanzare la loro agenda femminista. Non posso fidarmi di un' amministrazione del genere."

ke "Questo non va bene. Non va bene!"

show kenji rage
with charachange

ke "Dannazione. Merda! Dannazione!"



label it_A38b:
#If on Lilly or Hanako's route

hi "Non so. Sono piuttosto affamato così pensavo di prendere qualcosa da mangiare prima e poi vedere le attrazioni."

hi "Il progetto della tua classe sembrava abbastanza forte, e ho dato una mano a farlo, così voglio almeno vedere quello e chiaccherare con Lilly, direi."

hi "E parlando di quello, non hai nessuna obbligazione nei confronti del progetto?"

show kenji rage
with charachange

ke "Sei fuori di testa?"

ke "Quella pupa cieca non ha in mente niente di buono; posso sentirmelo nella milza amico. La sua presenza è come un' ombra oscura che ostacola la mia grande visione."

ke "Come ci si può aspettare dai ciechi."

hi "Cosa."

hi "E inoltre, credevo che anche tu lo fossi…"

show kenji neutral
with charachange

"Solleva la mano per interrompermi."

ke "Solo legalmente."

ke "Metaforicamente, posso vedere più lontano di qualunque uomo abbia mai visto prima di me."

"Kenji fissa stoicamente il metaforico orizzonte per enfatizzare la sua affermazione, sporgendo avanti il mento per sembrare più mascolino. A dire il vero è solo il muro del corridoio a due metri di distanza, ma non importa."

show kenji tsun
with charachange

ke "Posso vedere il futuro dell' uomo, ed è oscuro a meno che la minaccia delle donne non venga soffocata."

ke "Sono ovunque."



label it_A38c:
#If on Rin's route

hi "Bè, mi sono iscritto al club d' arte così immagino che andrò con loro."

show kenji rage
with charachange

ke "Tu hai fatto cosa?"

hi "Mi sono iscritto al club d' arte."

show kenji tsun
with charachange

ke "Amico, quella è stata una brutta mossa. Davvero brutta. Non sai che genere di ragazze ci sono nel club d' arte. Bamboline turbate e angosciate che ti strappano il cuore e lo mangiano crudo."

"Bene, conosco un membro del club d' arte, e non riesco davvero a immaginarmi Rin che diventa improvvisamente un' assassina psicotica."

hi "Sembra improbabile."

ke "Non dirlo. Non prenderti in giro. Non hai idea di quel con cui stai trattando qui, amico. Sono il peggior tipo."

show kenji neutral
with charachange

ke "Ti attirano con tutta questa merda pretenziosa e quando meno te lo aspetti, BAM!"

hi "Bam cosa?"

"Kenji sembra leggermente disturbato dal mio scetticismo, ma non meno matto."

show kenji tsun
with charachange

ke "Non importa."

ke "Bada a dove metti i piedi amico, bada a dove metti i piedi."    



label it_A38d:
#If on Emi's route

hi "Non saprei… sono un po' affamato, ma ho stretto questo accordo di provare a prendermi più cura di me stesso. Essere più sano, sai."

hi "Non so se dovrei girare al largo dai takoyaki o tuffarmici a capofitto."

show kenji tsun
with charachange

ke "Accordo? Suona sinistro. Così tu cosa ottieni in cambio?"

hi "Nulla, immagino? Non è quel tipo di accordo."

hi "Conosci Emi, del nostro anno? Ci siamo messi più o meno d' accordo di essere partner e…"

show kenji rage
with charachange

ke "Aieeeeeeee!"

"L' urlo penetrante e l' espressione di abietto terrore sulla faccia di Kenji mi gelano il sangue nelle vene. E' come se avessi detto a un prete cattolico che ho venduto la mia anima al diavolo."

ke "Lei! Hai venduto la tua anima al diavolo, e non hai ottenuto niente in cambio?"

ke "Che cavolo c'è che non va in te, amico?"

ke "Lo sai con chi stai trattando?"

ke "E' un pericolo per la salute pubblica. Sai quante persone manda all' ospedale ogni mese coi suoi placcaggi in volo attentamente piazzati?"

show kenji tsun
with charachange

ke "E' una di loro! Una partecipante fondamentale nella vasta cospirazione che mira alla completa sottomissione di tutto quello che è maschile."

ke "Non posso credere a quello che sto sentendo. Mi fidavo del tuo giudizio, amico. Pensavo che fossimo fratelli."

ke "Devi dire di no prima che sia troppo tardi."

ke "Anche questo festival, è solo uno dei loro trucchi."



label it_A38e:
    
"Trastulla nevosamente la sua sciarpa, sempre più in fretta come se stesse cercando di fargli prendere fuoco, poi lentamente inizia a calmarsi una volta che l' attacco di panico finisce di avere il suo corso."

stop music fadeout 2.0

show kenji neutral
with charachange

ke "Dovrò trovare qualche posto dove nascondermi, un rifugio sicuro. E poi mettermi KO così da non dovere sperimentare questo giorno orribile."

ke "Ho qualcosa di perfetto per quello. Ora devo prepararmi."

show kenji tsun
with charachange

ke "Non andare al festival."

hi "Okay."

show kenji neutral
with charachange

ke "A dopo, amico."

hide kenji
with charaexit

"La porta si chiude lentamente con un quieto cigolio e non so come sentirmi riguardo a quel che Kenji ha appena detto."




label it_A44:

show bg school_dormhallway at bgright
with None

"Considero quello che mi piacerebbe fare con Shizune e Misha. Decidendo che è meglio essere ben preparato, rientro nella mia stanza un momento per riempire il mio portafoglio."
 
scene bg school_dormhisao
with locationchange

"Mi chiedo se c'è quel gioco dove si prova a catturare pesci rossi su una retina di carta."

"Sembra molto più facile di quanto lo fanno sembrare. D' altra parte, se catturassi un pesce rosso, non avrei una vera ragione per tenerlo."

"Cosa potrei fare con un pesce nella mia minuscola stanza? Cucinarlo?"

"Potrei darlo a Shizune, o a Misha, ma quello potrebbe essere oltrepassare i miei limiti."

"E' un vero problema. Sono tutte e due carine, ma non penso di avere una possibilità con nessuna di loro. Ciononostante, rimugino sul pensiero di farlo. Immagino come potrebbero reagire se gli dessi un dono stanotte, come un pesce o una bambola."

"Misha probabilmente riderebbe come fa sempre. Shizune potrebbe colpirlo e farlo cadere dalla mia mano."

"Forse non è poi così una buona idea dopotutto."

scene bg school_dormhallway
show shizu behind_blank_close
with locationchange

"Appena esco fuori, quasi urto contro Shizune."

hi "Ciao, Shizune. Dov'è Misha?"

show shizu behind_frustrated_close
with locationchange

"Cerco di segnarlo quanto meglio posso, ma in realtà sto solo inventandomi gesti. Devo chiedere a Misha di insegnarmi qualcosa."

mi "Qui!"

play music music_comedy

show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None

show misha hips_grin behind shizu at Slide(0.5,0.5,0.3,0.5,1.0)
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)

"Misha spunta da dietro Shizune, sorridendo ampiamente."

mi "Siamo solo venute per assicurarci che tu venissi con noi al festival."

show shizu basic_angry_close at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Non tornare sulla tua promessa~!"

hi "Promessa? Non credo di aver promesso nulla."

show shizu cross_angry_close at tworight
with charachange

shi "…"

show misha hips_frown at twoleft
with charachange

mi "Smetti di cercare di uscirne!"

show misha perky_sad at twoleft
with charachange

mi "Daidai, Hicchan, sarà divertente! Ne hai bisogno, comunque, o diventerai un poco di buono!"

show misha perky_smile at twoleft
with charachange

mi "Non vuoi diventare una di quelle persone che restano soltanto nella loro stanza tutto il giorno, facendo i paranoici, non è vero?"

"Mi trovo a fissare da sopra alla sua spalla la porta della stanza di Kenji proprio di fronte alla mia."

"Spero che non abbia sentito, ma penso che Misha voglia il contrario."

hi "No, certo che no. Stavo solo scherzando un po', e comunque stavo per andare. Non c'era bisogno che voi due veniste qui."

show misha cross_laugh at twoleft
with charachange

mi "Davvero? Ahahaha! Shicchan temeva che tu avresti tentato di svicolare in qualche maniera!"

show misha hips_grin at twoleft
with charachange

mi "Abbiamo bisogno di te, Hicchan~!"

hi "Eh?"

"Credo che il mio cuore abbia appena saltato un battito."

show misha perky_smile at twoleft
with charachange

mi "Io non ho la mira che ci vuole per abbattere le bambole dai loro piedistalli in quel gioco… e Shicchan si rifiuta di tirare cose."

hi "Oh."

"Shizune mi fissa, immediatamente accorgendosi del mio disappunto. Disincrocia le braccia e si aggiusta gli occhiali."

show shizu adjust_happy_close at tworight
with charachange

shi "…"

mi "Cosa credevi intendessimo dire? Io mi rifiuto di lanciare alcunchè."

show misha perky_confused at twoleft
with charachange

mi "Perchè, Shicchan? E' strano…"

show misha perky_smile at twoleft
with charachange

mi "Bene, comunque, Hicchan, tu hai lanciato delle palle prima d' ora, giusto~, giusto~? Così! Devi venire con noi!"

"Sono stupito dalla loro logica. Non so se stanno scherzando o no."

hi "Heh, mi sentirei offeso se non sapessi che voi due stavate scherzando."

hi "State scherzando, vero?"

show shizu behind_frown_close at tworight
with charachange

shi "…"

mi "E' quello che è, Hicchan~! E' quello che è quello che è quello che è quello che è!"

hi "Beh quello è rassicurante."

show shizu basic_normal2_close at tworight
with charachange

shi "…"

show misha hips_smile_close at closeleft
with characlose

mi "Forza, andiamo! La banda dei sordi sta preparandosi fuori dalla tua finestra."

"Misha prende la mia mano e tenta di tirarmi fuori dalla porta, ma è chiaro che non ci sta affatto provando sul serio."

hide shizu #stupid renpy
with None

show shizu basic_normal2_close behind misha at tworight
with None

show shizu adjust_blush_close behind misha at tworight
with charachange

"Shizune ci guarda, arrossendo leggermente e giocherellando impazientemente coi suoi occhiali."

"Non sono abituato a questo genere di contatto familiare, ma non ho nulla contro di esso. Come potrei obiettare?"

stop music fadeout 1.0

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

play music music_normal

"Fuori c'è ancora luce, ma il sole sta preparandosi a tramontare dietro gli alberi."

"Sembra che metà della scuola sia qui fuori, e posso perfino vedere alcuni membri del corpo insegnante insieme da un lato, che stanno servendosi del punch."

"Stanno per svuotare l' intera coppa, con costernazione della ragazza che sta servendo al chiosco."

"Ci sono alcuni veggenti che stanno chiacchierando oziosamente con i loro amici, mentre altri hanno già iniziato a lanciare oroscopi a chiunque entri nel loro raggio d' azione."

"Penso che quella specie di tattica sia un po' troppo aggressiva, ma mostra che ci tengono. E' rinfrescante da vedere, ma non so se sarò in grado di abituarmici."

show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

show misha sign_smile at twoleft

mi "Bene, dovremmo prendere qualcosa da mangiare. Sei affamato, Hicchan?"

"Ora che ci penso, non ho mangiato niente tutto il giorno."

hi "Non ho veramente voglia di mangiare spaghetti fritti."

show misha hips_grin at twoleft
with charachange

mi "Tutto okay, ci sono altri cibi fritti!"

hi "Ci sono dei cibi che non sono fritti?"

show shizu adjust_smug at tworight
with charachange

shi "…"

mi "Dolciumi. Le porcherie sono l' essenza delle celebrazioni!"

show misha cross_laugh at twoleft
with charachange

mi "Wahahahaha!"

show shizu behind_smile at tworight
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Forza, io — voglio dire, Shicchan — ti offrirò una cosa!"

mi "Una?"

show shizu adjust_smug at tworight
with charachange

shi "…!"

show misha sign_smile at twoleft
with charachange

mi "Solo una~! Solo perchè tu possa caricare di energia il tuo braccio che lancia!"

show misha perky_smile at twoleft
with charachange

mi "Ah, ma non sembra che tutti i chioschi siano ancora pronti, così potresti non riuscire a trovare quello che vuoi."

"Dò un' occhiata in giro, sorpreso dal numero di bancarelle. E' incredibile, questo festival sembra più grande di quelli che si potrebbero vedere in una vera città."

"Nonostante quel che ha detto Misha, sembra che metà della scuola stia già celebrando."

"L' aria ronza per l' eccitato chiacchericcio di almeno metà del corpo studentesco."

"Sento odore di cibo che cuoce, e mi sta solo rendendo più affamanto con ogni secondo che passa."

show shizu behind_frustrated at tworight
with charachange

shi "…"

show misha perky_confused at twoleft
with charachange

mi "Forza, Hicchan, il cibo sta già sparendo in fretta! Se vuoi dei takoyaki, dobbiamo muoverci ora!"

show misha hips_grin at twoleft
with charachange

mi "A me andrebbero un po' di takoyaki~! Andiamo, mangiamo quelli!"

hi "Va bene, è una vita che non mangio takoyaki. Ci sto."

hide shizu
with charaexit

hide misha
with charaexit

"Shizune parte ancor prima che Misha possa segnarle la risposta, camminando di buon passo verso la bancarella dei takoyaki mentre io e Misha cerchiamo di raggiungerla."

scene bg school_stalls1
with locationchange

"Misha ride mentre saltella verso Shizune, che ordina tre porzioni di takoyaki mostrando tre dita alzate."

"Non l' avevo mai notato prima, ma per qualcuno così ossessionato dal tè di alta classe, è un po' strano che a Shizune piaccia anche tanto il fast food."

"Prendo il piatto di takoyaki che mi passa e mi chiedo se dovrei iniziare a mangiarli subito. Sembrano estremamente caldi."

"Posso vedere il fumo che si alza dal piatto e l' olio che ribolle sulla superficie."

show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"Shizune e Misha mi guardano, come se stessero aspettando che io mangi prima che possano cominciare."

"Non posso ritirarmi, così ne infilzo uno con la minuscola forchetta di plastica che sporge allegramente dall' angolo del piatto."

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange

"Però, prima ancora che possa metterlo in bocca, Shizune e Misha iniziano a mangiare di gusto, con Shizune che dà rapidi ma delicati morsi ai takoyaki mentre Misha mangia voracemente come una bambina."

"Immagino che dopo tutto, entrambe siano solo ragazze come qualunque altro studente qui."

"E' piacevole stare così. Non credo di avere avuto da molto tempo una possibilità come questa di godere della compagnia di altri e passare del tempo insieme."

"Ancor prima di venire qui, stavo passando un anno pieno di impegni. Così pieno che non mi ero accorto di cosa mi stessi perdendo fino ad ora."

stop music fadeout 3.0

"Qui, mi sento in pace."

"Questa è un' atmosfera tranquillizzante. Non sapevo che questo genere di festival esistesse ancora."

show misha perky_confused at twoleft
with charachange

play music music_comedy

mi "Eh? Hicchan, non vuoi mangiare il tuo cibo?"

hi "No, lo voglio mangiare."

show shizu adjust_smug at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "Spero che tu non ti stia tirando indietro perchè è troppo caldo."

hi "Non è per quello."

"Anche il loro stuzzicarmi sta iniziando a diventare accattivante."

scene bg school_stalls1_ss
with shorttimeskip

"Mangio rapidamente prima che il mio pasto si possa raffreddare, pensando che le lanterne di carta debolmente illuminate che ardono caldamente contro il tramonto sono una vista splendida."

show shizu behind_smile_close_ss
with charaenter

"Prima che io possa finire il mio ultimo morso di takoyaki, Shizune si piazza di fronte a me, perfettamente dritta in piedi con le sue braccia rigidamente tese dietro la schiena."

"Posso vedere che sta facendo del suo meglio per sembrare quanto più seria possibile, ma nemmeno lei può nascondere il suo buonumore dato che c'è un leggero sorriso sul suo volto."

$ renpy.music.set_volume(0.6,2.0, "ambient")

show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove

show misha cross_laugh_ss at twoleft
with charaenter

mi "Ahahaha~! Dai, Hicchan, andiamo a giocare a qualcosa!"

hi "Ma i chioschi dei giochi sono pronti?"

show shizu adjust_happy_close_ss at tworight
with charachange

shi "…"

show misha cross_grin_ss at twoleft
with charachange

mi "No, ma non importa, non importa~! Forza, Hicchan, prima che diventi troppo affollato!"

show misha hips_grin_close_ss at closeleft
with characlose

"Misha poggia la sua mano sulla mia spalla e ride molto sonoramente."

show misha perky_smile_close_ss at closeleft
with characlose

mi "Forza! Forza! I premi sembrano davvero belli quest' anno, davvero davvero~! Non ti piacerebbe vincere qualche premio per due ragazze carine come noi?"

"Misha mi scocca contro la sua migliore espressione “carina”, che è effettivamente piuttosto carina. Guardo Shizune, aspettandomi che faccia lo stesso, ma lei mi fissa soltanto come se fossi ammattito."

show shizu cross_wut_close_ss at closeright
with charachange

shi "…"

show misha hips_grin_close_ss at closeleft
with characlose

mi "Misha, piantala!"

show misha perky_confused_close_ss at closeleft
with charachange

mi "Aspetta… sono io Misha…"

show shizu basic_normal2_close_ss at closeright
with charachange

shi "…"

show misha sign_smile_close_ss at closeleft
with charachange

mi "Hicchan, sbrigati, hai tenuto in mano quel pezzo di takoyaki per tipo un migliaio di anni!"

show misha cross_laugh_close_ss at closeleft
with charachange

mi "Hahahahaha!"

show misha cross_smile_close_ss at closeleft
with charachange

hi "Mi piace gustarmi tutto quello che mangio. Perfino questo."

show shizu basic_sparkle_close_ss at closeright
with charachange

show shizu adjust_smug_close_ss at closeright
with charachange

"Senza preavviso, Shizune raccoglie il takoyaki dalla mia mano e se lo mette in bocca con un sorriso."

"Succede così in fretta che non c'era modo in cui avrei potuto impedirglielo."

show misha cross_laugh_close_ss at closeleft
show shizu behind_smile_close_ss at closeright
with charachange

"Prima che possa anche solo elaborare completamente quel che è appena successo, Misha esplode in una risata, e Shizune mi sorride, probabilmente la cosa più vicina al ridere che le ho mai visto fare."

show shizu adjust_happy_close_ss at closeright
with charachange

shi "…!"

mi "Bene, quello è quanto~! Wahaha! Hahahaha!"

"Shizune afferra la mia mano destra, e Misha la mia sinistra."

show shizu behind_smile_close_ss at closeright
with charachange

shi "…"

show misha hips_grin_close_ss at closeleft
with charachange

mi "Ora vieni con noi! C'è un sacco di cose da fare stanotte, dovresti provare a godertele di più!"

show misha cross_laugh_close_ss at closeleft
with charachange

mi "Hahahaha~!"

stop music fadeout 5.0

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip

"Correndo attraverso una folla già abbastanza fitta, giochiamo a un gioco dopo l' altro, dal lancio degli anelli a colpire la talpa, a giochi di cui non ho mai nemmeno sentito parlare."

"Raramente vinciamo, ma è comunque divertente."

hi "Ehi, hanno quel gioco dove si catturano i pesci rossi qui?"

play music music_dreamy fadein 0.3

show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter

shi "…"

mi "Certo! Non sapevo che ti piacesse quel gioco, Hicchan!"

hi "Bè, ho sempre voluto provarci. Non sembra troppo difficile."

show misha hips_grin_ss at twoleft
with charachange

mi "Ne sei proprio sicuro, Hicchan~?"

show misha cross_laugh_ss at twoleft
with charachange

mi "Wahahaha~! Okay, okay! Vedremo! Dovrebbe essere qui intorno da qualche parte!"

show shizu basic_normal_ss at tworight
with charachange

shi "…"

show misha perky_smile_ss at twoleft
with charachange

mi "Ma, dove metterai il tuo pesce? Hai una boccia di vetro dove tenerlo?"

hi "Beh, no…"

show misha hips_grin_ss at twoleft
with charachange

mi "Forse se lo mangerà!"

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

show misha cross_laugh_ss at twoleft
with charachange

mi "Hahahahahaha! Ahahahahahaha!!"

show misha cross_grin_ss at twoleft
with charachange

mi "Va bene, Hicchan, se vinciamo dei pesci, li daremo a te!"

hi "Oh, davvero? Un altro gioco? D' accordo, allora."

show shizu basic_happy_ss at tworight
with charachange

"Shizune mi spinge eccitata verso il chiosco, cercando di nascondere l' entusiasmo nei suoi occhi."

scene bg school_stalls2_ss at bgright
with locationchange

"Fortunatamente, nessuna delle due riesce a prendere un singolo pesce, ma io non faccio di meglio."

stop music fadeout 5.0

$ renpy.music.set_volume(0.6,2.0, "ambient")

show bg school_stalls2_ss at bgleft
with charamove

"Non posso fare a meno di ridere quando subito dopo, iniziano a tirarmi verso una bancarella particolarmente grande e colorata che ho aiutato a costruire."

"Questa me la ricordo; è stata una vera rottura di scatole metterla insieme."

"Il gestore del chiosco, un tizio dall' aria comune con capelli marroni tinti, scatta sull' attenti quando ci vede avvicinarci. Noto due cose:"

"Primo, è uno di quei giochi dove tiri una palla a una piramide di bottiglie opache e cerchi di abbatterne quante più possibile."

"Quattro palle per 50 yen, non è affatto male."

"Secondo, ci sono istruzioni su come giocare in braille. Quasi voglio dire qualcosa, e guardo per vedere se anche Shizune e Misha se ne sono accorte."

"O non se sono accorte, o non lo trovano affatto strano."

"Gestore" "Ehi! Piacere di vederti, Hakamichi! Grazie tante davvero per il vostro aiuto con questo chiosco. Vi state divertendo?"

"Shizune guarda in direzione di Misha, che le segna tutto in un attimo, poi sorride raggiante al gestore."

play music music_comedy

show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "Haha~! Di niente, proprio di niente, davvero~! Già, è grande, penso che sia il miglior festival che abbiamo messo insieme!"

show misha perky_smile_ss at twoleft
with charachange

mi "Shiraki, ci piacerebbe giocare, è okay, giusto?"

show misha hips_grin_ss at twoleft
with charachange

mi "Certamente~, sarebbe davvero bello se volesse solo dare un premio alle sue graziose, operose rappresentanti del consiglio studentesco, per tutte le ore che abbiamo speso per rendere tutto questo possibile!"

"Shiraki" "Hahaha, haha… No."

"Se non altro, Shiraki ha le palle."

hi "Ehi, io ho costruito questa bancarella, ed è stato pure un lavoro massacrante. Ho sprecato due ore della mia vita, credo di meritarmi almeno un giro gratis."

show misha hips_frown_ss at twoleft
with charachange

mi "E io!"

show shizu basic_angry_ss at tworight
with charachange

shi "…"

mi "Anche io!"

show misha perky_confused_ss at twoleft
with charachange

mi "Ah…"

"Dopo un' esitazione, finalmente cede, e ci consegna quattro palle ciascuno con una scrollata di spalle."

show misha hips_grin_ss at twoleft
show shizu behind_blank_ss at tworight
with charachange

"Appena un secondo più tardi, Shizune e Misha scaricano le loro davanti a me."

hi "Che c'è?"

hi "Non ditemi che dopo averne fatto un caso nazionale, voi due non avete nemmeno intenzione di giocare?"

hi "Non dopo il modo in cui ci siamo coalizzati contro Shiraki."

"Shiraki" "Già…"

show shizu basic_frown_ss at tworight
with charachange

shi "…"

show misha sign_smile_ss at twoleft
with charachange

mi "Lei ne resti fuori, per favore~!"

show shizu adjust_happy_ss at tworight
with charachange

"Shizune si gira verso di me e inizia ad agitare la sua mano negligentemente. Misha sembra divisa tra il tradurre per lei e il consolare il gestore del chiosco."

show shizu adjust_smug_ss at tworight
with charachange

shi "…!"

show misha hips_grin_ss at twoleft
with charachange

mi "Ahahaha! Hicchan, dov'è il tuo senso di cavalleria? Inoltre, io—Shicchan, ho una regola contro lanciare delle palle!"

show misha hips_smile_ss at twoleft
with charachange

mi "Ah, scusa, Hicchan. Neanche io so se la mia mira è molto buona. Tu però devi essere abbastanza bravo con queste cose, giusto, giusto? Non dovrebbe essere un problema per te!"

stop music fadeout 3.0

"Sembra abbastanza semplice. Le bottiglie non sono nemmeno molto lontane, l' unica difficoltà è che queste palle sono cave e leggere."

"Ne tiro una forte contro le bottiglie, e rimbalza via senza cerimonie."

show shizu behind_blank_ss at tworight
show misha perky_confused_ss at twoleft
with charachange

hi "Che diavolo?"

"Shiraki" "Ah, già, non è facile come sembra. C'è dell' acqua nelle bottiglie. Segreto del mestiere."

show misha hips_frown_ss at twoleft
with charachange

mi "Non è molto onesto!"

hi "Ecco perchè quattro palle costano solo 50 yen. Subdolo."

show shizu basic_angry_ss at tworight
with charachange

shi "…"

show misha hips_smile_ss at twoleft
with charachange

mi "Forza, Hicchan, le puoi abbattere! Hai altre undici possibilità! Vai!"

hi "Forse dovreste farlo voi."

hi "Shizune? Vuoi provarci?"

show shizu behind_blank_ss at tworight
with charachange

"Shizune scuote la testa enfaticamente da un lato all' altro."

"Rido, dopo tutto questo è piuttosto divertente."

play music music_soothing

"Caricando il tiro, lancio un' altra palla alla piramide di bottiglie e riesco a farle muovere appena appena."

show shizu basic_normal_ss at tworight
show misha perky_smile_ss at twoleft
with charachange

"Sia Shizune che Misha stanno lanciando sguardi bramosi verso una bambola a forma di gatto."

"Dopo tutto, non sono davvero così diverse."

"Qualche volta mi chiedo se Shizune suonerebbe come Misha se potesse parlare."

"No, non sono così simili."

"Lancio un' altra palla, capendo che alla fin fine è veramente semplice. Se riesco a colpire due bottiglie nella fila più in basso allo stesso tempo, è una vittoria facile."

"Di già, una piccola folla sta iniziando a raccogliersi, così la pressione è tutta su di me. Altri nove tiri."

play sound sfx_impact2

"Muovendomi come un lanciatore di baseball, lancio quanto più forte posso e le bottiglie crollano giù."

show shizu behind_blank_ss at tworight
show misha cross_laugh_ss at twoleft
with charachange

"Trionfante, reclamo il mio femminile premio di una bambola felina e Misha ride fragorosamente come se la avesse vinta lei."

"Shizune mi fissa con la sua solita espressione imperscrutabile. E' chiaro che anche lei vuole la bambola."

show shizu basic_normal2_ss at tworight
with charachange

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "Hicchan, congratulazioni~! Che cosa farai di quella bambola?"

"Non esiste una risposta giusta. Devo muovermi cautamente."

hi "Io… non lo so."

mi "Beneeeeee~ la prenderò io, se non la vuoi…"

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

show misha cross_grin_ss at twoleft
with charachange

mi "A meno che tu non la voglia tenere per te, Hicchan. Non sapevo che ti piacessero le bambole. Così sensibile."

hi "Non la voglio. Non mi serve."

show misha cross_smile_ss at twoleft
with charachange

mi "Posso averla io, allora?"

show shizu behind_blank_ss at tworight
with charachange

shi "…"

"I loro occhi stanno trafiggendo la mia anima."

"Questa è una decisione che non voglio prendere. Torno a girarmi verso il chiosco."

hi "Ehi, avete più di una di queste bambole?"

"Shiraki" "A dire il vero, sì, soltanto un' altra."

hi "Okay, rimetta tutto a posto di nuovo, voglio provare a vincere anche quella."

"Ho ancora otto tentativi."

"Appena il gioco è di nuovo pronto, tiro di nuovo quanto più forte posso, ma manco il bersaglio."

show misha hips_grin_ss at twoleft
with charachange

mi "Hahaha! Stai cercando di vincerne un' altra? Stai prendendo la via d' uscita più facile, Hicchan?"

hi "Se è così facile, puoi provarci tu."

mi "No grazie~!"

show misha perky_smile_ss at twoleft
with charachange

mi "Dì, Hicchan, puoi almeno mettere giù la bambola mentre lanci le palle?"

hi "No."

show shizu adjust_smug_ss at tworight
with charachange

shi "…"

mi "Ne è rimasta solo una, farai meglio a vincerla! Se fallisci, ti ucciderò~!"

show shizu behind_smile_ss at tworight
with charachange

shi "…"

mi "Che maniera astuta di evitare di dare a me la bambola, però! E con me, intendo dire me~!"

show shizu adjust_happy_ss at tworight
with charachange

shi "!"

show misha cross_laugh_ss at twoleft
with charachange

mi "Ahahahaha~! Sto scherzando!"

"Posso vedere che Misha non voleva dire niente di male, e Shizune sembra apprezzare il suo scherzo, sorridendo in risposta, ma dopo sembra un po' depressa."

"Decido di passarle la bambola, almeno mentre sto tentando di vincere l' altra. E' abbastanza difficile mirare mentre si tiene un gatto gigante."

show shizu behind_smile_ss at tworight
show misha perky_smile_ss at twoleft
with charachange

shi "…"

mi "Grazie, Hicchan. Shicchan sembra felice, Hicchan~! Ma, ne vincerai una anche per me, giusto?"

hi "E' quello che sto cercando di fare, no?"

stop music fadeout 5.0

show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None

hide shizu
hide misha
with Dissolve(1.0)

"Tiro di nuovo, ma la mia mira è molto fuori bersaglio stavolta."

"Anche il mio braccio sembra un po' pesante, come se il sangue non gli stesse affluendo a dovere."

"Mi rimprovero mentalmente, pensando che è patetico che io possa stancarmi a causa di una cosa simile."

"Poi capisco che forse è a causa del mio cuore. Se lo è, allora non so cosa pensare."

"E' deprimente che perfino qualcosa di insignificante come questo sia abbastanza per farmi ricordare la mia mortalità."

"Suppongo che non ci sarà mai un momento in cui potrò dimenticarmene."

"Anche oggi, quando pensavo che avrei potuto solo divertirmi, durante questa bella notte e in questo bel posto, non posso sfuggire alla ragione per cui sono qui."

"Non mi sono mai sentito talmente in pace nella mia vita, in questo posto che è diverso da qualunque altro posto dove sia mai stato."

"E' difficile ora non pensare l' impensabile:"

play music music_sadness fadein 0.3

"Che potrei essere solo stato mandato qui a morire."

"Questi ultimi giorni sono stati alcuni dei migliori della mia vita. La prima volta dopo molto tempo in cui mi sono sentito veramente vivo."

"Ma alla fine, sono qualcuno a cui viene ricordato ogni volta che sale troppe scale o lancia una palla troppo forte che potrebbe morire in qualunque momento."

"Sarò sempre limitato da questo."

"Mi sento depresso, e anche arrabbiato. Dopo tutto, mi importa della mia vita, e mi piace, e adesso è più passeggera di quanto sia mai stata prima."

"Mi chiedo cos'è che finalmente mi ucciderà. Potrebbe essere qualunque cosa, se sono così debole e patetico: una brutta caduta, un pugno al petto, una palla da baseball vagante."

"Adesso ho perso il mio desiderio di continuare a giocare a questo gioco, ma insisto comunque."

play sound sfx_heartfast

show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"Improvvisamente, sento una momentanea fitta di dolore dentro il mio petto. Appare e scompare istantaneamente, ma è abbastanza per farmi barcollare un poco."

show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)

"Shizune salta indietro, sorpresa. Si avvicina a me, fissandomi preoccupata. Misha mi mette una mano sulla spalla."

mi "Ehi, Hicchan, stai bene?"

hi "Sì, tutto a posto. Non mi sento davvero troppo bene in questo momento. Credo di avere la nausea. Non penso di poter continuare."

show misha hips_frown_close_ss at twoleft
with charachange

"Misha si rabbuia."

mi "Non sforzarti. Se stai così male, finirai solo per sentirti peggio."

show shizu basic_normal2_close_ss at tworight
with charachange

shi "…"

show misha hips_smile_close_ss at twoleft
with charachange

mi "Guarda, il festival sta solo iniziando, e abbiamo già giocato per un pezzo. Possiamo fare una piccola pausa se sei stanco."

show misha sign_smile_close_ss at twoleft
with charachange

mi "Buona idea, Shicchan, anche io mi sento un po' stanca! Credo che lo siamo un po' tutti, dopo aver corso per tutta la scuola, Hicchan!"

stop music fadeout 10.0

"Annuisco. Non sembrano notare nulla di inusuale. Bene."


$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip

"Camminiamo attraverso il mare di persone, con Misha che allegramente ci fa notare le facce di tutti quelli che conosce. Shizune stringe il gatto di pezza tra le braccia, cullandolo distrattamente. Sembra che si stiano divertendo."

"Improvvisamente, sento un rimorso di coscienza."

"A causa della mia cattiva salute, abbiamo dovuto fermarci tutti."

play music music_tranquil

show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter

shi "…"

mi "Hicchan, abbiamo tutte e due un po' di fame. E tu?"

hi "Non ho tanta fame quanta potrei averne, ma voglio qualcosa da mangiare."

show misha hips_smile_ni at twoleft
with charachange

mi "Quello è abbastanza, Hicchan~! Così, cosa dovremmo prendere da mangiare?"

hi "Per me non ha veramente importanza."

show shizu adjust_happy_ni at tworight
with charachange

shi "…"

show misha hips_grin_ni at twoleft
with charachange

mi "Ah! Che ne dici di sandwich, allora? E avremo bisogno anche di qualcosa da bere! Misha prenderà tutto!"

show misha perky_confused_ni at twoleft
with charachange

mi "Cosa?"

show shizu behind_smile_ni at tworight
with charachange

"Shizune mi guarda e sorride, e capisco che potrebbe stare cercando di rallegrarmi con uno scherzo. Rido."

show shizu adjust_happy_ni at tworight
with charachange

shi "…"

show misha perky_smile_ni at twoleft
with charachange

mi "Hicchan, qui sta diventando un po' affollato, così potremmo non riuscire a mangiare. Sta diventando anche un po' rumoroso."

show misha sign_smile_ni at twoleft
with charachange

mi "Forse dovremmo andare a mangiare sul tetto."

hi "A me va bene. Potrebbe esserci un bel panorama, e un po' di brezza."

show misha hips_grin_ni at twoleft
with charachange

mi "Okay allora! Credo che adesso dovrei andare a prendere il cibo e le bevande… Così ci rivediamo più tardi~!"

stop music fadeout 4.0

hide misha
with charaexit

"Misha ci saluta goffamente e corre via."

"Prima, non mi ero accorto di come sembravano le lanterne di carta mentre illuminano la notte scura, ma adesso che sono in grado di vederlo, è veramente uno spettacolo incredibile."

"Delle lucciole fluttuano nell' aria, il loro debole brillio fa sembrare che stiano nevicando luci nel cielo notturno."

"Questo genere di cosa sarebbe impossibile da vedere in città."

show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None

show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)

"Shizune tira la mia manica impazientemente e incrocia le braccia, accigliandosi come per dimostrarmi il suo malcontento perchè mi sono distratto."

play music music_shizune

show shizu basic_angry_close_ni
with charachange

shi "…"

hi "Lo sai che non so leggere la lingua dei segni."

show shizu behind_frown_close_ni
with charachange

shi "…"

"Ora che ci penso, non è un po' stupido da parte mia aver detto quello a una persona sorda? Non lo avrebbe potuto sentire."

show shizu behind_blank_close_ni
with charachange

"Scrollo le spalle, sperando di mostrarle che non capisco. Shizune scuote la testa e scarta la cosa agitando la sua mano."

"Forse dovrei decidermi e chiedere a Misha qualche lezione di lingua dei segni."

$ renpy.music.set_volume(0.4,2.0, "ambient")

scene bg school_roof_ni
with locationskip

"Arrampicandoci su fino al tetto, mi trovo di nuovo in soggezione alla pura grandezza di questa scuola. I terreni sono talmente ampi che non riesco a credere di non essermene accorto prima."

"Mentre cammino lungo il tetto, seguendo Shizune, non riesco a evitare di essere incantato dalle stelle splendenti nel cielo."

show shizu behind_smile_close_ni
with charaenter

"Shizune e io ci sediamo su una panchina. Sembra che sia di buon umore da come sorride dolcemente mentre la brezza soffia tra i suoi capelli."

"Guardiamo giù verso il festival, che sembra come un mare di luminescenti lanterne ambrate e ventagli di carta che si agitano brulicante di persone, alcune di loro festivamente vestite di kimono."

"Infatti, la maggior parte delle ragazze sembrano indossare dei kimono. Mi chiedo perchè Shizune e Misha non si siano vestite a festa oggi."

"Tutte e due starebbero bene in kimono. Penso per un momento a che tipi di kimono indosserebbero."

"Shizune probabilmente sceglierebbe qualcosa di tradizionale. Però, Misha è un po' più difficile da collocare."

"Misha arriva, ansimando mentre corre verso di noi, cercando di impedire al cibo che ha tra le braccia di cadere."

"Poggiando tutto a terra, si lascia cadere all' indietro."

show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove

show misha hips_grin_ni behind shizu at twoleft
with charaenter

mi "Ahahahahahahahahaha~! C'è voluto un po'! Forza, voi due non mi avete detto cosa volevate, così ho preso un po' di punch di riso, qualche sandwich, e anche un po' di dolci! Un po' di tutto!"

hi "Grande. Diamoci da fare."

"Misha stacca un morso da un piccolo sandwich triangolare."

show misha hips_smile_ni at twoleft
with charachange

mi "Così, Hicchan, che ne pensi del festival? E' bello, non è vero?"

hi "Già."

show shizu adjust_happy_close_ni at tworight
with charachange

shi "…"

mi "Le stelle sono belle stanotte. Questo non avrebbe potuto essere stato un giorno più perfetto."

scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange

"Il suono delle persone che parlano sotto di noi è come una lieve musica assieme al distante frinire dei grilli."

"Bevo un sorso dalla lattina di punch e guardo Misha, che sembra stare dormendo confortevolmente con la schiena stesa e una lattina di succo di mela mezza piena bilanciata sullo stomaco."

"Shizune siede con le sue gambe strette contro di lei, dondolandosi lentamente avanti e indietro come un bambino impaziente mentre guarda verso il cielo."

"Sono entrambe talmente graziose. Guardo in giro e posso vedere molti studenti che si tengono per mano con le loro ragazze o i loro ragazzi."

"Non troppo lontano da noi su questo tetto, ci sono delle coppiette che guardano su verso le stelle o giù verso le luci del festival, mano nella mano."

"Una parte di me vuole la stessa cosa."

"Guardando Shizune e Misha, mi chiedo se forse dovrei invitare una di loro a uscire un giorno. Mi chiedo se varrebbe il rischio."

"Le lancette dorate che si muovono intorno al quadrante del delicato orologio al polso di Shizune attraggono la mia attenzione, e vedo che sta facendosi piuttosto tardi. Ma i festeggiamenti stanno ancora andando forte."

"Shizune sta ancora tenendo per la zampa il gatto di pezza che ho vinto. Si accorge che lo sto guardando."

shi "…?"

"Sbrigativamente, me lo offre. Sorrido, volendo chiederle che cosa potrei farmene, ma non sarebbe in grado di capirmi."

"Scuoto la testa e faccio del mio meglio per dirle di tenerlo, sperando che capisca."

stop music fadeout 8.0

"Quando guardo verso la scuola, posso vedere così tante persone davanti a me, tutte felici e allegre."

"Guardarle mi fa sentire soddisfatto."

"E' stato veramente qualcosa di bello. Oggi ne è valsa la pena."

"Ma ancora non riesco a liberarmi dei sensi di colpa e della malinconia di prima, continuano a rimanermi attaccati, e non posso lasciarli andare."

"Shizune mi segna qualcosa, e non posso capirla. Non importa cosa dico, non potrà sentirmi."

play music music_twinkle fadein 2.0 fadeout 2.0

hi "Non posso capirti, Shizune."

hi "Bè, non importa. Mi chiedo se ci consideriamo entrambi colpevoli per questo. Comunque, mi dispiace per non poter capire."

hi "Sai, sono quasi, quasi contento che tu abbia tentato di costringermi a venire qui. Se provo a chiederti di uscire insieme, però, potrei dover pensare di più a quel lato del tuo carattere."

hi "No, a dire il vero… sono contento. Oggi è stato piacevole."

hi "Saresti più carina se sorridessi di più, hai un bel sorriso."

show shizu behind_frustrated_close_ni
show bg misc_sky_ni at right
with charaenter

"Frustrata, si alza, braccia dietro la schiena, e sembra autoritaria e sicura di sè contro lo sfondo delle stelle."

show shizu out_serious_close_ni
with charachange

"D' improvviso, Shizune spalanca le sue braccia verso il cielo aperto, apparentemente tenendolo tra le sue mani."

"E' come se mi stesse dicendo di guardare tutto quello che è davanti a me:"

stop ambient fadeout 2.0

show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu

"La scuola, bagnata dalle luci del festival e ravvivata dai kimono colorati, il tetto illuminato dalle lucciole, il cielo così vasto da imporre una sensazione di soggezione."

"Che cosa vuole? Col tempo lentamente lo capisco. Questa splendida scena davanti a me è la prova che ci sono cose abbastanza meravigliose che rovinarle col cattivo umore sarebbe imperdonabile."

"E posso sentire il peso della personalità di Shizune insistere su questo punto."

hi "Grazie, credo."

hide shizu
show hill pairtouch
with charachange

"Distolgo il mio sguardo, ma poi Shizune mi prende per la spalla, e il suo orologio sfiora la mia guancia."

"Con la sua mano sinistra, punta su verso il cielo."

stop music fadeout 5.0
play ambient sfx_fireworks fadein 1.0

show fireworks behind hill
with None
show screen behind fireworks
with Dissolve(5.0)

"Con leggeri botti, dei fuochi artificiali iniziano a scoppiare in cielo, ciascuno spargendo una pioggia di colori vividi che lentamente svaniscono nel buio."

"Non riesco nemmeno a ricordare l' ultima volta che ho visto dei fuochi artificiali, lasciamo stare uno spettacolo così grande. Per non dire che sembra stiano venendo lanciati dalla scuola; è quasi impossibile da credere."

"Le luci in cielo si mescolano con una seconda salva dalla città, e sembrano essere calcolate per complementarsi le une con le altre come due metà di un duetto."

"Continuano per forse quindici minuti, e poi smettono."

"Shizune si accorge che la sua mano è ancora sulla mia spalla e la ritira cautamente, sembrando un po' a disagio."

stop ambient fadeout 5.0
play music music_twinkle fadein 5.0
hide fireworks
hide screen
show hill pairnotouch
with Dissolve(5.0)

"Recuperando il suo contegno, sorride, con le mani sulle anche e il suo seno spinto di fronte a lei."

"E' in questi momenti che più sembra essere come una normale ragazza adolescente. Energica, felice, e spensierata."

"Mangio pensierosamente assieme a Shizune, mentre guardiamo in silenzio la folla sotto di noi diradarsi gradualmente."

"Siede leggermente inclinata in avanti, col mento appoggiato sulle sue mani e un' aria soddisfatta sul suo viso con solo un tocco di malinconia."

"Sempre tenendo gentilmente stretta la zampa del gatto di peluche."

"Inizio a sentirmi stanco e le dico che rivedrò lei e Misha domani, senza neanche ricordare che non può sentirmi, e comincio a camminare indietro verso i dormitori."

"Mi sento caldo e vivo, anche in questa fredda aria della notte."

"L' immagine di Shizune in piedi decisa davanti alle stesse stelle, in rifiuto della mia autocommiserazione, non abbandona facilmente la mia mente."

"Se… se ci vuole solo un momento per innamorarsi, penso che potrei starmi innamorando di lei."

"Solo un pochino."

window hide

stop music fadeout 4.0


        
#******************

#Emi Path
label it_A39:

show bg school_dormhallway at bgright
with None

"E' un po' inquietante, e ora comincio a sentirmi in dubbio anche io."
  
"Dovrei darmi la pena di andare?"

"Ho un libro che volevo leggere."

"Qualcosa su un sistema postale sotterraneo che potrebbe esistere o non esistere."

"E' anche corto. Lo potrei finire in un giorno."

"Ma sarebbe un buon modo di passare il mio tempo?"

"Bè, sì. Decisamente lo sarebbe."

"Ma suppongo che uscire sarebbe probabilmente un' idea migliore."

"Vedere il festival."

"Cercare di integrarmi con tutti gli altri fenomeni da baraccone."

"Davvero, dovrei almeno fare un tentativo di coltivare la personalità discretamente amichevole che ho sviluppato durante questa settimana."

"Forse prendere qualcosa da mangiare, suggerisce il mio stomaco."

"E' quasi ora di pranzo… potrei almeno procurarmi qualcosa da uno dei chioschi fuori."

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

"Presto sono fuori, circondato da vari studenti e persone che potrebbero essere o non essere i loro genitori."

"Ogni tanto noto qualcuno che chiaramente è solo venuto dalla città per la promessa di un festival."

"Sono facili da individuare."

"Quelli che non riescono a non fissarti, e dietro i loro occhi puoi dire che stanno pensando “Ora, che c'è che non va in {b}questo{/b}?”"

"Quasi voglio urlargli contro."

"Ma allo stesso tempo, posso negare di aver fatto lo stesso per tutta la settimana?"

"Un' ondata di qualcosa di simile al disgusto mi sommerge; senso di colpa per la mia ristrettezza mentale."

"…"

$ renpy.music.set_volume(0.6,2.0, "ambient")

scene bg school_stalls1
with locationchange

"Metto i pensieri da parte, concentrandomi sulle fitte di fame che bruciano le mie interiora come un fuoco."

"L' odore di qualcosa di fritto mi guida fino alla terra promessa, dove posso pranzare."

stop music fadeout 0.6

"Sto appena ricevendo il mio ordine quando una forte voce mi interrompe."

show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter

play music music_normal fadein 0.5

emi "Ehi, cosa accidenti stai facendo?"

hi "Comprando la colaz—ah, pranzo."

show emi sad_annoyed
with charachange

emi "Colazione?"

show emi sad_angry
with charachange

emi "Vuoi dire che ti sei appena alzato?"

hi "Uh…"

"Improvvisamente dormire per tutta la mattina sembra un crimine."

hi "No, volevo dire pranzo… davvero."

"Non ci sta credendo."

hi "Brunch?"

show emi basic_annoyed_close
with characlose

emi "Quella non è affatto una colazione sana!"

"Mi strappa il cibo di mano e mi lancia un' occhiataccia."

"Che diavolo sta facendo questa ragazza?"

hi "Ehi, quella è la mia colazione!"

show emi sad_annoyed_close
with charachange

emi "Quando ha smesso di essere il tuo pranzo?"

hi "Quello è il mio… insomma, è il mio cibo!"

"Emi si piazza le mani sulle anche e comincia a farmi la ramanzina."

show emi basic_annoyed_close
with charachange

emi "Ti sei davvero già dimenticato dellla tua dieta?"

emi "Devi essere più attento alla tua salute, Hisao!"

show emi sad_angry_close
with charachange

emi "Che ne è del tuo cuore?"

hi "Il mio cuore va bene così com'è! Più o meno."

"Tutta la risposta che ottengo è una smorfia."

show emi basic_annoyed_close
with charachange

emi "Ne dubito."

show emi basic_closedgrin_close
with charachange

emi "Non saresti qui se quello fosse il caso, non è vero?"

"Lei ha delle ottime ragioni, ovviamente."

"Ma non ho intenzione di cedere."

hi "Non è un cuore così malconcio!"

hi "Certamente può sopportare un po' di grasso di tanto in tanto!"

"Già, sicuro. E ha sopportato proprio bene anche un po' di corsa."
 
show emi basic_annoyed_close
with charachange

"Emi non sembra convinta."

"Non sorprendente, dato che non sono nemmeno riuscito a convincere me stesso."    

emi "Forse, ma non se poltrisci a letto tutto il tempo!"

"Un' espressione subdola attraversa improvvisamente il suo volto."

show emi basic_grin_close
with charachange

emi "Certamente, se tu avessi seguito una routine fin dall' inizio non saresti in questa situazione…"

hi "Ehi, ho avuto una settimana piuttosto piena di eventi, sai!"

hi "Per esempio, sono quasi morto! E ho incontrato un sacco di gente, e poi sono stato su un tetto per un po'…"

show emi sad_annoyed_close
with charachange

emi "Il che non è una scusa per batter la fiacca, sai."

emi "Una piccola esperienza quasi fatale non è una valida scusa per saltare l' esercizio fisico di base."

show emi basic_closedgrin_close
with charachange

emi "Come correre di mattina."

stop music fadeout 0.6

"Annuisce, come se qualcosa di importante fosse appena stato deciso."

play music music_emi fadein 0.5

show emi basic_happy_close
with charachange

emi "Così è stabilito, allora!"

show emi excited_proud_close
with charachange

emi "Hai visto l' errore delle tue abitudini e sei disposto ad aderire alla mia routine, giusto?"

emi "Ti vedrò pronto e scattante di mattina?"

show emi excited_happy_close
with charachange

emi "Saremo compagni di corse?"

hi "Sai, mi avevi già convinto ieri che questa fosse una buona idea."

hi "Non devi convincermi di nuovo."   
    
"Non che abbia dato una gran dimostrazione di essere convinto."
    
"Ha ragione riguardo al mangiare sano, dopotutto. Ed eccomi qui a ordinare qualcosa di gravemente malsano."
    
"Ma delizioso!"
    
"Ci sono cose più importanti del cibo delizioso, non è vero?"
    
"Come rimanere vivi?"
    
"Se Emi non fosse qui a sgridarmi per le mie decisioni errate, probabilmente…"
    
"Ehi, un momento."
    
"Una domanda improvvisa mi salta in mente."

hi "Ehi, perchè diavolo sei diventata tanto interessata al mio benessere?"

show emi basic_closedgrin_close
with charachange

"Emi scrolla le spalle e mi sorride."

show emi basic_grin_close
with charachange

emi "Sei quello nuovo."

emi "Immagino che tu non abbia ancora degli amici, giusto?"

show emi sad_grin_close
with charachange

emi "E poi, ti ho causato dei fastidi per tutta la settimana, no?"

emi "Sono in debito con te per non esserti arrabbiato."

show emi basic_happy_close
with charachange

emi "E ho detto all' infermiere che lo avrei fatto, comunque."

"Uh… huh. La piccola ragazza matta che corre vuole farmi tornare in salute."

"Bene, suppongo che ci siano fati peggiori."

hi "Okay, quello sembra… ragionevole."

hi "Grazie per la tua preoccupazione."

hi "Domattina, allora?"

hide emi
with charaexit

"Immagino che questo concluda la conversazione, così mi giro per andarmene."

emi "Non così in fretta!" 

"Sento una mano sul mio colletto e in un secondo sono stato tirato all' indietro." with vpunch

hi "Ehi, non c'è bisogno di essere così violenti!"

hi "Cosa vuoi adesso?"

show emi sad_shy_close
with charaenter

"Emi sembra quasi ferita dalla mia irritata domanda."

emi "Pensavo che potessi gradire della compagnia."

show emi basic_annoyed_close
with charachange

"I suoi occhi si stringono."

emi "E comunque, stavi solo per cercare di prendere dell' altra robaccia fritta di nascosto, non è vero?"

"Beh, non stavo per farlo, ma ora che lo dice quella sarebbe stata davvero un' ottima idea."

hi "Certo che no!"

show emi sad_annoyed_close
with charachange

"Un' altra occhiataccia."

hi "Okay, forse ne avrei preso un po'…"
    
"L' occhiataccia continua."
    
hi "Okay, un sacco."
    
"Gesù, sono un pericolo per me stesso e per gli altri, non è vero?"
    
"Finisco di dichiarare di essere d' accordo sul dover vivere in modo più sano, e immediatamente comincio a considerare la prossima abitudine malsana che mi passa di fronte."

show emi basic_closedgrin_close
with charachange

emi "Lo sapevo! Non mi posso fidare."

show emi basic_grin_close
with charachange

emi "Adesso devo veramente rimanerti incollata."

"L' intera situazione sembra sciocca."

"Posso solo immaginare cosa pensino i passanti alla vista di me che ricevo una ramanzina da una ragazza minuta grande la metà di me."

"Forse dovrei solo cedere per ora."

hi "E va bene, fai come vuoi."

"Sospiro."

"Tanto vale far buon viso a cattivo gioco."

hi "Cosa vuoi fare?"

show emi basic_confused_close
with charachange

"Emi pensa per un minuto."

emi "Beh, ho promesso a Rin che mi sarei fermata al suo murale…"

show emi basic_grin_close
with charachange

emi "Così andiamo!"

"Confesso di essere leggermente curioso anche io di vedere come sia venuto il suo murale, così di nuovo considero che ci sono fati peggiori."

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"Chino la testa in assenso e mi ritrovo a essere quasi trascinato a forza attraverso la folla quando Emi corre verso la nostra destinazione."

stop music fadeout 0.6

stop ambient fadeout 0.6

scene bg school_dormext_full at bgright
with locationchange

play music music_sadness fadein 1.0

"Una volta che abbiamo raggiunto i dormitori, sento il mio cuore martellare."

"Il mio cuore non dovrebbe accelerare dopo così poco."

"Tiro alcuni profondi respiri, desiderando di calmarmi."

"Sono una delle persone dall' aria più normale della scuola, ma devo comunque essere qui."

"Qualche volta quasi desidero di aver perso una mano o qualcosa del genere."

"Almeno allora il perchè sono qui sarebbe ovvio."

"Ma invece non sembro nemmeno malato."

"Anche adesso, mentre cerco di riprendere fiato, sembro solo fuori forma."

"Emi si gira e nota il mio stato di sofferenza."

show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

emi "Non stai per morirmi tra le mani, vero?"

stop music fadeout 3.0

show emi basic_shock
with charachange

emi "Per favore non farlo!"

show emi sad_depressed
with charachange

emi "Sarebbe tutta colpa mia, e non voglio affrontare un simile senso di colpa."

emi "E poi, dopo l' ultima volta non credo davvero di voler rivedere quello spettacolo, specialmente perchè l' infermiere dirà assolutamente che è tutta colpa mia."

play music music_daily fadein 0.7

hi "N… nah, sto bene."

hi "Suppongo di dover cominciare a correre dopotutto."

show emi basic_closedgrin
with charachange

emi "E volevi continuare a mangiare il tuo… qualunque cosa fosse fritto."

show emi excited_proud
with charachange

emi "Vedi? E' un bene che ti abbia trovato, giusto?"

"Sì lo è."

hi "Forse."

show emi basic_grin
with charachange

"Ovviamente non aggiungo che non sarei in questo stato se non mi avesse trascinato da un capo all' altro del festival."

"Ulteriore conversazione viene interrotta dall' improvvisa apparizione di Rin."

show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)
with Dissolve(1.0)

rin "Oh, siete voi."

show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full
with charamove

show rin basic_awayabsent at tworight
with charachange

rin "Ciao Emi."

show emi basic_closedhappy at twoleft
with charachange

emi "Ehi Rin! Ho portato Hisao con me perchè stava per farsi venire un attacco di cuore!"

show rin basic_absent at tworight
with charachange

hi "Non è vero!"

"La mia obiezione non viene notata."

show emi basic_grin at twoleft
with charachange

emi "Siamo passati a vedere come è venuto fuori il murale!"

"Rin annuisce lentamente."

show rin basic_awayabsent at tworight
with charachange

rin "Bè, è proprio lì."

show rin basic_deadpan at tworight
with charachange

rin "Lo puoi vedere piuttosto bene."

"Mi ritrovo a chiedermi da quanto tempo Rin sia in piedi qui di fronte al murale."

"Qualcuno si sarà fermato per guardarlo?"

"Siamo i primi?"

"Ovviamente non siamo i primi a vederlo, certo."

"Voglio dire, è abbastanza grande."

"Sarebbe uno sforzo non vederlo."

"Allo stesso tempo, non credo che nessuno ne abbia veramente parlato con Rin."

"Nessuno eccetto noi, cioè."

"Mi sento obbligato a dire qualcosa."

hi "Sembra davvero bello."

show rin negative_spaciness at tworight
with charachange

rin "Ancora non sono contenta di come ha finito per essere."

rin "Ma suppongo che possa andare."

"Sembra quasi rassegnata."

"Non sono sicuro di cosa si aspettasse come risultato, ma immagino che non ce l' abbia fatta."

scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)

"Restiamo in piedi di fronte al murale, contemplandolo."

"Faccio del mio meglio per concentrarmi sulla composizione del dipinto."

"A dire il vero è piuttosto interessante."

"I colori si muovono e si mischiano insieme, trascinandomi con loro."

"L' intera cosa ha una qualità sognante che mi fa quasi sentire assonnato."

"Cerco di trovare alcuni dei colori che io ed Emi abbiamo preso per lei."

"Non importa quanto ci provi, non riesco a vedere da nessuna parte del blu di Prussia."

"Oh bè."

"Sono sicuro che è lì da qualche parte."

scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)

"I miei piedi iniziano a farmi male, ma Rin non sembra avere voglia di muoversi."

"Emi rompe il silenzio."

show emi basic_confused at twoleft
with charachange

emi "Ehi Rin, hai mangiato?"

show rin basic_deadpan at tworight
with charachange

rin "Ovviamente. Non si può sopravvivere altrimenti."

show emi basic_hes at twoleft
with charachange

emi "Che mi dici delle ultime cinque ore?"

show rin relaxed_nonchalant at tworight
with charachange

rin "Forse. Ma ho di nuovo fame, quindi forse vuol dire che mi sbaglio."

show emi basic_closedgrin at twoleft
with charachange

"Emi sorride e batte le mani."

show emi basic_grin at twoleft
with charachange

emi "Bene! Vieni a mangiare qualcosa con noi!"

"Rin annuisce in assenso."

show rin basic_deadpannormal at tworight
with charachange

rin "D' accordo, ma dovremmo sbrigarci prima che si accorgano che me ne sono andata."

"Qualcosa mi dice che non glie ne importerebbe."

"Di chiunque stiamo parlando."

stop music fadeout 2.0

scene bg school_stalls1 at Fullpan(8.0)
with locationskip

"Mentre torniamo verso i chioschi di ristoro, guardo con amore le fritture."

"No, meglio di no."

"Sono piuttosto sicuro che comunque Emi non me lo permetterebbe."

scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange

"Troviamo un buon posto sull' erba e ci sediamo per mangiare i nostri acquisti."

"Beh, i miei acquisti, almeno. In un modo o nell' altro, ho finito per pagare per tutto il cibo."

"Sorprendentemente, il mio cibo (non fritto) è piuttosto gustoso."

"Cade il silenzio mentre Emi e io mangiamo e Rin fissa… qualcosa, occasionalmente mangiando un morso o due del suo cibo."

"Finisco il mio pasto per primo, e mi sdraio sull' erba."

"Emi alza gli occhi dal suo cibo."

play music music_dreamy fadein 0.3

show emi basic_confused at twoleft
with charachange

emi "Stanco, Hisao?"

hi "Un po', suppongo."

show emi basic_annoyed at twoleft
with charachange

emi "Bè, non dormire troppo o roba del genere domattina."

show emi excited_proud at twoleft
with charachange

emi "Domani iniziamo a correre, ricordi?"

"A dire il vero, mi era passato di mente."

"Mi stavo solo divertendo."

"Girare per il festival con queste due è stato davvero divertente."

hi "Già, metterò a punto la sveglia."

show emi basic_annoyed at twoleft
with charachange

emi "Farai meglio a esserci!"

show emi basic_closedgrin at twoleft
with charachange

emi "Mi arrabbierò se non ti presenti!"

hi "Dio non voglia."

show rin basic_lucid at tworight
with charachange

rin "Non credo che Dio c'entri."

show rin basic_deadpan at tworight
with charachange

rin "A meno che non ci sia una sorta di incidente incredibile e la tua sveglia vada in corto."

show rin basic_deadpannormal at tworight
with charachange

rin "Quello potrebbe essere un atto di Dio."

show emi basic_grin at twoleft
with charachange

emi "Bene, allora non causare nessun atto di Dio."

"Un piano prende forma nella mia mente."

"E' un piano che mi fa sentire un poco in colpa, ma lo metto comunque in esecuzione."
    
"Dannazione, mi sono guadagnato un po' di cibo fritto."
    
"E comunque, comincio a correre da domani, giusto?"
    
"Così la routine vera e propria parte allora, non adesso."
    
"Ergo, anche la dieta comincia domani, ergo posso prendere qualcosa di insalubre oggi."
    
"Una specie di ultimo addio a tutta la roba che mangiavo con selvaggio abbandono prima dell' ospedale."

hi "A dire il vero, credo che dovrei tornare alla mia stanza."

hi "Avevo alcuni compiti da fare, e se devo correre di mattina farò meglio ad andare a dormire presto…"

show emi basic_annoyed at twoleft
with charachange

"Di nuovo quegli occhi stretti in sospetto."

show emi sad_annoyed at twoleft
with charachange

emi "Sei sicuro di non volere solo svicolare per andare a comprare un po' di quella roba fritta là?"

hi "Nah, adesso sono troppo pieno per provarci."

"Batto sul mio stomaco per dare enfasi."

hi "E comunque, voi due mi avete ripulito."

show emi basic_closedhappy at twoleft
with charachange

"Emi ride. E' un suono sorprendentemente piacevole."

"Un altro rimorso di coscienza."
    
"Deve sapere che le sto mentendo, no?"
    
"O è davvero così fiduciosa?"
    
"Mi sento un po' come un mostro."

show emi excited_proud at twoleft
with charachange

emi "Tutto parte del mio grande piano, Hisao."

show emi basic_closedgrin at twoleft
with charachange

emi "Bene, allora immagino che ci rivedremo domattina."

show emi basic_grin at twoleft
with charachange

emi "Grazie per il cibo! E per averci fatto compagnia!"

"E io che pensavo che lei mi stesse facendo un favore."

show rin relaxed_surprised at tworight
with charachange

"Rin china la testa in assenso e agita un piede nella mia direzione."

rin "Non dirò “Ci vediamo domani” perchè quello sarebbe come prevedere il futuro, e sono piuttosto sicura di non poterlo fare."

hi "…"

hi "Okay."

hi "Ciao, voi due."

"Mi sento stranamente contento di aver deciso di lasciare la mia stanza oggi."

"Non una brutta maniera di cominciare la mia seconda settimana qui, suppongo."

stop music fadeout 2.0

scene bg school_stalls1
with locationchange

"Una volta che sono sicuro di essere al di fuori della linea di vista di Emi, mi precipito verso le bancarelle dei cibi e compro un po' di torta."
    
"Almeno non è fritta, giusto?"
    
"E' leggermente meglio di quello che avevo intenzione di fare."
    
"Mi sento ancora un po' in colpa per aver mentito a Emi, però."
    
"Sembra davvero preoccupata per la mia salute."
    
"Mi farò perdonare in qualche modo."
    
"Meglio tornare alla mia stanza."

"Ehi, {b}ho{/b} del lavoro da fare."

scene bg school_dormhisao
with locationskip

"Il mio libro mi sta aspettando, e mi butto sul mio letto e leggo durante lo spettacolo di fuochi artificiali."

scene bg school_dormhisao_ni
with Dissolve(2.0)

"Alla fine tutto il camminare (o più esattamente correre) avanti e indietro si fa sentire."

"Sono davvero fuori forma."

"Dopotutto potrebbe proprio essere una buona cosa che Emi mi trascini a correre di mattina."

"E' qualcosa in cui sperare."

window hide



#######################
#Rin Path

label it_A40:

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_dormext_full
show crowd
with locationskip

"Il felice tumulto della folla mi dà il benvenuto quando mi spingo oltre la porta principale ed esco."

"I terreni della scuola sono stati trasformati in terreni del festival nel corso di ieri e stamattina."

"Chioschi colorati sono allineati lungo i sentieri principali che corrono dall' entrata principale all' edificio scolastico."

"Alcune persone stanno ancora trasportando roba avanti e indietro, ma dietro la maggior parte dei banconi ci sono degli studenti rilassati che sembrano pronti a darsi da fare."

"La maggior parte degli altri studenti si sono alzati presto per finire le preparazioni."

"Un senso di colpa mi attraversa, ma presto sparisce."

"Sono solo un umile studente trasferito, dopotutto."

"Alcuni visitatori stanno già passeggiando per il campus."

"Ci sono alcune giovani famiglie con i genitori turbati che cercano di tenere il passo della loro prole sovreccitata…"

"…alcuni dei nostri studenti accompagnati dai loro genitori…" 

"…e un sacco di persone vecchie e giovani che sono qui per nessuna ragione che io possa immaginare."

play sound sfx_normalbell

"Il carillon esplode in uno scampanio e la voce squittente della direttrice annuncia l' apertura del festival attraverso l' impianto di amplificazione."

"Tutti applaudono educatamente ma senza molto entusiasmo."

# Applause sound effect?

"Un festival scolastico… non avevamo veramente i festival alla mia vecchia scuola superiore. Sembra un po' all' antica, specialmente considerando la scuola da cui provengo, ma è comunque un po' eccitante."

"Un giorno libero è benvenuto dopo la prima settimana di duro lavoro, nonostante io sia rimasto steso nel letto dell' ospedale per quattro mesi prima di questo momento."

"Mi ricordo perfino di aver desiderato di potere andare alle lezioni di matematica durante la mia permanenza in ospedale."

"Non riesco a ricordare il programma del festival, anche se Mutou lo ha esposto durante le lezioni appena l' altro giorno."

"Scendo gli scalini del dormitorio, con l' intento di fare un giro per i terreni per vedere tutta la roba che gli altri hanno organizzato, ma arrivo solo fino in fondo alle scale."

stop ambient fadeout 1.0

hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)

"Alcune persone stanno studiando il muro col dipinto di Rin, mentre l' artista stessa sta oziando in disparte, appoggiata contro il muro e con un' aria estremamente annoiata e leggermente giù di corda."

hi "Buongiorno."

show rin relaxed_surprised at tworight
with charachange

rin "Salve."

hi "Come va?"

show rin relaxed_nonchalant at tworight
with charachange

rin "Da nessuna parte."

rin "Sono bloccata."

hi "Che vuoi dire, bloccata?"

rin "Voglio dire non riesco a camminare bloccata. Penso che le mie gambe siano fuori uso a causa di ieri."

hi "Ti fanno male?"

show rin relaxed_sleepy at tworight
with charachange

rin "Difficile dirlo. Forse."

"Lo sforzo di lavorare sul murale era più grande di quanto mi abbia lasciato capire. Pensavo che fossero solo un po' di muscoli stanchi o qualcosa di simile. Vorrei chiedere qualcos' altro, ma Rin rapidamente passa a un altro argomento."

show rin basic_awayabsent at tworight
with charachange

rin "Gli amici dell' insegnante sono passati."

show rin basic_absent at tworight
with charachange

rin "Poi sono andati in città per pranzare e mi hanno chiesto di accompagnarli. E' stato un bene che le gambe mi facessero così male."

hi "Ma sei bloccata seduta qui? Quello non è un bene."

show rin basic_lucid at tworight
with charachange

rin "Mi limiterò ad aspettare finchè non posso camminare di nuovo. Dovrebbe essere o prima o poi, se ci pensi per un po'."

rin "L' insegnante era contento che avessi finito il murale."

hi "Dovrebbe esserlo."

show rin basic_awayabsent at tworight
with charachange

rin "Ma mi chiedo se è finito dopotutto."

hi "Oh?"

show rin basic_deadpanupset at tworight
with charachange

rin "Ieri pensavo di aver fatto tutto, ma adesso non ne sono più sicura. Dovrei dipingere più dettagli. Forse. Probabilmente. E' molto difficile decidere."

"Finito o no, il murale è splendido alla luce del sole."

scene bg mural at Position(xalign=0.05)
with Dissolve(2.0)

"Varie parti del corpo umano, ripetute ancora e ancora in una varietà mutante, per la maggior parte sfigurata, sono l' elemento principale."

"Sembrano grezze, come se fossero state piazzate senza pensarci e dipinte rudimentalmente, ma una gran quantità di considerazione e cura è stata applicata ad ognuna di esse."

show bg mural at Position(xalign=0.25)
with charamove

hi "Questo ha una rana che gli cresce dalla testa?"

rin "E' un pesce rosso."

show bg mural at Position(xalign=0.45)
with charamove

hi "Cos'è quello?"

#he's pointing at a randomly chosen detail on the mural. you can like zoom on it or whatever. Do pick something that isn't obviously "something"

rin "Non è nulla."

show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None

"Comunque…"

"Il muro è tanto ampio che devo girare il collo da un lato all' altro per vedere l' intero dipinto."

"E' difficile considerarlo un singolo pezzo. Gli elementi non sembrano adattarsi insieme, ma suppongo che creino una specie di intero."

"Astratto come è, non ho idea di cosa si suppone rappresenti, ma sembra bello. Quello mi basta."

"Mi piazzo vicino a Rin, appoggiandomi contro al muro come lei."

"I rumori felici del festival stanno diventando più forti mano a mano che sempre più gente entra nel campus."

"I dormitori sono distanti dalle attrazioni principali nell' edificio principale e dalle bancarelle intorno al cortile così la maggior parte dei visitatori non si sono ancora fatti strada fino a qui."

show rin negative_spaciness_close at offscreenright
with None

show rin negative_spaciness_close at tworight
show bg mural at Position(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))

"Un' espressione leggermente annoiata si assesta sul viso di Rin, facendola sembrare distaccata da tutto quel che sta avvenendo intorno a lei."

"E' terribilmente taciturna. Mi chiedo se sta soffrendo."

hi "Così che hanno detto del tuo murale le persone interessate all' arte?"

show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)

"La mia domanda sveglia Rin dal suo sogno a occhi aperti. Pigramente gira il volto nella mia direzione."

show rin basic_deadpan_close at tworight
with charachange

rin "Non ne sono sicura."

show rin basic_awayabsent_close at tworight
with charachange

rin "Penso che gli sia piaciuto? Forse sì."

hi "E tu che mi dici? Sei contenta del murale? Perchè ho più o meno partecipato, sarebbe terribile se tu fossi scontenta."

"Rin china la testa di lato, mordendosi il labbro inferiore."

show rin negative_sad_close at tworight
with charachange

rin "Penso che sia riuscito decentemente. Non è male ma non è neanche buono. Soltanto… è. Suppongo di riuscire abbastanza a svuotare la mente."

hi "Posso chiedere qualcos' altro? Cosa rappresenta davvero il dipinto? Ieri ci ho pensato, quando hai detto che non rappresenta nulla."

hi "Ma quello è un errore di logica, no? Non si può creare qualcosa dal nulla, nemmeno dell' arte."

show rin negative_annoyed_close at tworight
with charachange

"Rin aggrotta le sopracciglia e gira di nuovo la testa verso le nuvole."

rin "Non lo so. Non sono proprio brava a spiegare le cose. E' solo un murale; non ha niente di speciale. Lo ho già detto."

"Sembra irritata dalle mie domande."

rin "Non sapevo cosa avrei dipinto, così ho solo deciso di dipingere un murale."

rin "E' un murale che ritrae un murale."

show rin basic_deadpancontemplation_close at tworight
with charachange

rin  "No, aspetta. Mi è appena venuta in mente una maniera migliore di dirlo: rappresenta se stesso."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Così… la sua muralità è al massimo, almeno per quanto io riesca a fare, così se pensi che abbia qualche significato, credo che quello sia lo stesso che ha questo."

"Quello non ha senso."

"Significato… sento gli angoli della mia bocca sollevarsi in un sorriso che è solo un tantino seccato."

scene mural all
with flash

"Non ho mai capito l' arte nel senso più profondo della parola."

"Capisco le basi, come l' arte sia intesa essere solo un mezzo per scambiare idee e pensieri."

scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash

"Tuttavia, non ho mai imparato come dovrei interpretare un' opera d' arte, per scoprire in qualche modo cosa intende dire l' artista attraverso di essa."

"So che non richiede nessuna abilità particolare, ma in qualche modo, il mio cervello non riesce mai a connettere l' arte con qualcosa che non sia quel che vedo. Tutto quello che vedo è un murale."

"Posso ammirare l' abilità tecnica, dopotutto perfino io conosco la differenza tra brutta arte e arte mediocre; arte mediocre e bella arte."

"Ma arrivo solo fino a quel punto, così non chiedermi di significati, Rin."

"La sua risposta mi ha anche sicuramente reso riluttante a chiederle altro al riguardo."

stop music fadeout 0.8

hi "Così cosa farai quando ti rimetti in piedi?"

scene bg mural at Position(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash

rin "Nulla."

hi "Nulla? Ma c'è il festival, non vuoi andare a divertirti un po'?"

show rin basic_absent_close at tworight
with charachange

rin "Sto bene così."

hi "Non ti piace molto socializzare, vero?"

"Penso di stare discutendo più per lei che per me a questo punto. Non è che neanche io sia particolarmente eccitato dal festival; solo un po' curioso di vedere com'è, e quello è più o meno tutto."

"La sua risposta non è sorprendente."

show rin basic_awayabsent_close at tworight
with charachange

rin "No, non mi piace."
   
hi "Credo… neanche a me, alla fin fine."

show rin basic_deadpan_close at tworight
with charachange

rin "Dovresti andare se vuoi farlo."

hi "Lo so, ma posso farti compagnia. Non sono ancora proprio abituato a tutto questo, così è okay prendermela comoda."

hi "Posso andarmene però, se vuoi stare da sola."

show rin basic_deadpannormal_close at tworight
with charachange

rin "Mi piace che tu sia qui."

"Giriamo intorno l' un l' altra colle parole, ma finiamo per arrivare da qualche parte. Mi fa sentire stranamente felice che lei abbia detto così, così rimango."

"La sua presenza è qualcosa che piace anche a me. La strana, calda aura di serenità che lei sembra emanare rende confortevole stare in silenzio. Quello mi piace davvero."

"Guardiamo le persone che passano, entrambi silenziosi, mentre tutti gli altri stanno chiacchierando felicemente tra di loro."

"Degli studenti stanno guidando le loro famiglie al dormitorio per mostrargli le loro stanze. Passano davanti a noi e al murale, lanciandogli uno sguardo forse una volta o due."

"Presto meno attenzione a loro, e più alla mia compagna, cercando di trovare la strada che supera il criptico, illeggibile muro che ha per viso."

show rin basic_awayabsent_close at tworight
with charachange

show rin basic_absent_close at tworight
with charachange

show rin basic_awayabsent_close at tworight
with charachange

"Gli occhi di Rin vagano senza riposo da una persona all' altra che passa."

"Sta aspettando che la gente si fermi al murale, forse segretamente sperando che qualcuno faccia un commento?"

"Non penso che nessuno penserebbe che lei è l' autrice. Siamo solo seduti qui come un paio di barboni, dopotutto, e lei non ha nemmeno le mani."

"Mi chiedo se sia persino nello stile di Rin andare a caccia di complimenti. Sembra talmente distante."

play music music_rin fadein 0.3

"Più persone passano, alcune che puntano le loro dita al murale, scambiando parole che non posso capire. Qualcuno si fa cadere un gelato sulla scarpa. Peccato per lui."

hi "Sembra piacere a tutti."

"Lo suggerisco sperimentalmente, lanciando un argomento di discussione nell' aria estiva viziata che ci separa."

"Rin non risponde subito, ma ormai sono più o meno abituato alla sua occasionale lentezza quando deve parlare."

"E' come se fosse molto attenta a scegliere le sue parole, il che è davvero incredibile quando si considera il guazzabuglio che viene fuori dalla sua bocca."

show rin basic_lucid_close at tworight
with charachange

rin "Volevo fare in modo che si potesse solo guardarlo senza pensare. Poi ho capito che non ha nessun senso. Così è diventato qualcosa come una mistura di questo e quello."

show rin negative_spaciness_close at tworight
with charachange

rin "Da lontano, sembra che qualcuno abbia vomitato una mandria di farfalle sul muro. Il che è esattamente quello che quella persona presidentessa sgradevole non voleva. Quella parola è quella?"

hi "Quale parola?"

show rin basic_deadpannormal_close at tworight
with charachange

rin "Quella. Qual è la parola per più di una farfalla?"

hi "Farfalle?"

show rin basic_deadpanupset_close at tworight
with charachange

rin "No, tipo una mandria, o un branco, o un mucchio."

hi "Oh. Non lo so. Un gregge forse?"

rin "Forse alla gente piace il vomito delle farfalle."

show rin negative_confused_close at tworight
with charachange

"Rin guarda il murale, sembrando sorprendentemente infelice."

rin "Il centro potrebbe essere migliore."

show rin negative_annoyed_close at tworight
with charachange

rin "Di solito mi piacciono gli intercalari, ma questo mi ha fatto stare sulle spine. Non letteralmente, chiaro… d' altra parte mi sono anche seduta su una scheggia mentre dipingevo. Immagino che fosse letteralmente, dopotutto."

hi "Non essere così critica di te stessa."

show rin basic_deadpannormal_close at tworight
with charachange

"Mi guarda stranamente, ma tace."

stop music fadeout 3.0

scene bg school_dormext_full at bgright
with locationchange

"Più o meno a questo punto comincio a pensare che dovrei davvero andarmene e fare qualcosa di più costruttivo con la mia domenica."

"Questo è l' apice del fallimento sociale. Un intero giorno libero, un festival proprio fuori dalla mia soglia, e io cosa faccio?"

"Siedo qui con Rin; due spettatori con nulla da fare eccetto pensare che peccato sia essere solo uno spettatore."

"Anche capendo quanto sia pietoso, non faccio nulla. Non mi alzo e non parto verso un giorno di divertimento."

play sound sfx_rustling

centered "*shuffle shuffle*"

"…"

centered "*fidget*"

play sound sfx_rustling

centered "*shuffle*"

"…"

scene bg mural at Position(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange

"Rin sta agitandosi nervosamente, costantemente accavallando una gamba sull' altra e poi riportandola al posto di partenza."

"Ha un' aria molto irritata sul suo viso."

hi "Qualcosa non va?"

show rin basic_deadpanupset_close at tworight
with charachange

rin "Sì. No. Sì."

scene bg school_dormext_full at bgright
show rin basic_deadpanupset at Move((0.7,1.0,0.5,0.8),(0.7,1.0,0.5,1.0),0.5, time_warp=_ease_in_time_warp)
with locationchange

"Improvvisamente salta su in piedi. E' sorprendente, pensavo che fosse ancora immobilizzata ma apparentemente non è così."

show rin negative_confused at tworight
with charachange

rin "Devo andare e trovare Emi o qualcuno, ho bisogno di aiuto con una cosa."

hi "Posso aiutarti io."

show rin relaxed_nonchalant at tworight
with charachange

rin "No, è okay. Uno di noi deve rimanere qui nel caso che succeda qualcosa."

hi "Non essere ridicola. Niente di anche solo remotamente interessante è successo da quando sono venuto qui eccetto per quel tizio che si è fatto cadere un gelato sul piede. Lascia che ti aiuti, dato che sono annoiato."

hi "Così che c'è?"

show rin negative_annoyed at tworight
with charachange

"Le labbra di Rin si appiattiscono strettamente l' una contro l' altra in una linea quasi perfettamente orizzontale."

show rin basic_lucid at tworight
with charachange

"Chiude gli occhi e tira un profondo respiro."

"Quando riapre le palpebre lo sguardo spaventosamente severo nei suoi occhi scuri mi prende di sorpresa."

play music music_rin fadein 0.2

show rin negative_angry at tworight
with charachange

rin "Hisao, potresti non voler sentire questo o forse sì, non lo so, ma non importa e anche se importasse non mi stai lasciando alcuna scelta."

rin "Sto avendo le mie mestruazioni e ho bisogno di aiuto riguardo a quello. Però, non credo che la nostra relazione sia ancora al livello in cui potrei permetterti di calare le mie mutandine nel bagno delle donne anche se tu ti offri di farlo."

rin "Quello è il perchè tu dovresti stare qui mentre io vado a cercare Emi."

"Mentre il sangue corre alle mie guance come una marea crescente, il mio cervello tenta disperatamente di cercare una risposta."

"…ma l' unica cosa a cui posso pensare è come quella sia stata la cosa più coerente che ho sentito uscire dalla bocca di Rin durante questi quattro giorni in cui l' ho conosciuta."

hi "Sì."

hide rin
with charaexit

"Non volendo incontrare gli occhi di Rin, giro la mia faccia dall' altra parte, fingendo di stare guardando i genitori di qualcuno."

"Coll' angolo dell' occhio vedo Rin girare sui tacchi e camminare via senza altri indugi."

"Ho voglia di andare a nascondermi sotto una roccia."

"Mi chiedo per quanto Rin dovrà assentarsi… o addirittura se tornerà."

"…"

scene bg mural at Position(xalign=0.6)
with shorttimeskip

stop music fadeout 2.0

"Alla fine ritorna, comparendo apparentemente dal nulla e sedendosi di nuovo dove era, vicino al mio posto."

show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

rin "Sono tornata."

"Lo dice senza emozione, come se la mia gaffe non fosse mai capitata. Anche io preferirei scordarmi dell' intero affare, così taccio."

scene bg mural_ss at Position(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Move((0.7,1.0,0.5,.85),(0.8,1.0,0.5,.9),3.0, time_warp=_ease_in_time_warp)
with Dissolve(3.0)

"Il tempo passa da fermo, il sole luccica alto da sopra l' edificio principale. Mi colpisce direttamente negli occhi, ma li strizzo soltanto invece di muovermi."
  
"In poco tempo diventa doloroso tenere aperti gli occhi anche solo un po', e le mie tempie cominciano a farmi male."

hi "Mi fa male la testa. Credo che questa giornata mi abbia fatto venire l' emicrania, riesci a crederci?"

show rin basic_deadpan_close_ss at tworight
with charachange

rin "Hai fame?"

hi "Quello cosa ha a che vedere col mal di testa?"

show rin basic_deadpansurprised_close_ss at tworight
with charachange

rin "Nulla. Lo chiedo perchè io ne ho."

"…"

"La sua incurante serietà scioglie la mia irritazione per quanto è ridicola, e scopro che gli angoli della mia bocca stanno nuovamente alzandosi leggermente."

hi "Sai che ti dico? Anche io."

hi "Andrò a prendere qualcosa da mangiare. Cosa vuoi? Offro io."

show rin basic_lucid_close_ss at tworight
with charachange

rin "Non ha importanza."

play music music_dreamy fadein 3.0

show rin basic_deadpannormal_close_ss at tworight
with shorttimeskip

"Ritornando col cibo, dò una porzione a Rin, prendendo l' altra per me, e ci dedichiamo a mangiare senza una parola."

show rin negative_spaciness_close_ss at tworight
show rin_shadow negative at Position(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange

"Rin guarda verso l' alto, forchetta pendente dall' angolo della bocca."

rin "Cosa sono le nuvole? Ho sempre pensato che fossero pensieri del cielo o qualcosa del genere. Perchè non le puoi toccare."

hi "Pensavi così quando eri bambina?"

rin "No, la settimana scorsa."

rin "Forse perchè qualche volta i miei pensieri sembrano nuvole. Soffici e bianchi e lenti."

rin "Come se il cielo fosse nella mia mente. Come se la mia mente fosse il cielo."

hi "Il cielo della tua mente?"

rin "Chiudi gli occhi e pensa al cielo. Non potrai pensare a nient' altro finchè non smetti."

scene black
with shuteye

"Ci provo. Funziona. Magia?"

scene bg mural_ss at Position(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Position(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with openeye

"Aprendo gli occhi, vedo Rin che mi studia coi suoi occhi. E' imbarazzante perchè non dice nulla. Mi giro dall' altra parte."

scene bg misc_sky_ss at Fullpan(20.0)
with locationchange

hi "Le nuvole sono acqua. Acqua evaporata."

hi "Sai come dicono che quasi tutta l' acqua del mondo in un qualche momento della sua esistenza sarà parte di una nuvola."

hi "Ogni goccia di lacrime e sangue e sudore che spargi, sarà una nuvola. Anche tutta l' acqua dentro il tuo corpo, va lassù un po' di tempo dopo la tua morte. Potrebbe volerci un po', però."

rin "la tua spiegazione è migliore di tutte le mie."

hi "Perchè è vera."

rin "Deve essere per quello."

"Continuo a mangiare il cibo prima che si raffreddi."

"Il muro offre un po' di ombra benedetta mentre il sole gira intorno alla cupola del cielo."

"Ma il pomeriggio sta già lentamente cedendo strada alla sera così il nostro pranzo diventa più una cena. O qualinque sia la parola per un pasto irregolare come questo."

"Indipendentemente da come decido di chiamarlo, è certamente soddisfacente. Non ho mangiato nulla da una vita."

"…"

"Placato il mio appetito, emetto un sospiro soddisfatto. Rin non ha mangiato tutto ma anche lei sembra aver finito col suo cibo."

"Mi reclino indietro, assorbendo l' atmosfera. La folla si è già assottigliata, ma le attività stanno ancora continuando. Tutti sembrano stare divertendosi."

"And why not? It's warm, the kind of perfect summer day when it's hot but not too hot for comfort."
   
"Il sole tramonterà presto. Il tempo è veramente volato."

scene bg mural_ss at Position(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Position(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with locationchange

hi "Siamo stati seduti qui per sei ore."

show rin basic_deadpansurprised_close_ss at tworight
with charachange

rin "Sì, è così."

show rin basic_deadpancontemplation_close_ss at tworight
with charachange

rin "Vuoi fare qualcos' altro adesso?"

hi "No, non proprio."

show rin basic_deadpannormal_close_ss at tworight
with charachange

rin "Neanche io."

show rin basic_lucid_close_ss at tworight
with charachange

"Aggiusta la sua posizione e si reclina contro il muro, e io seguo il suo esempio, rilassandomi."

"Per interi minuti, sediamo lì senza dire una parola."

"Sto cercando di percepire l' umore di Rin dal suo comportamento, la tensione dei suoi muscoli, le minuscole espressioni che appaiono e scompaiono sul suo viso. E' inutile. E' indecifrabile come sempre."

scene bg school_dormext_full_ss
show crowd_ss
with locationchange
$ renpy.music.set_volume(0.6, 0.2, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 0.2

"La folla si muove avanti e indietro, le persone chiacchierano felici tra di loro. Ben poche prestano veramente attenzione al murale, e ancor meno a noi."

"Giocherello distrattamente con alcuni strani ciottoli."

"L' atto di fare qualcosa solamente per fare qualcosa, il culmine dell' ozio."

"Centimetro dopo centimetro, il sole scende sempre più in basso verso le chiome degli alberi, cambiando il colore del cielo vicino all' orizzonte da giallo dorato ad arancione e rosso man mano che il momento del tramonto si avvicina."

"Mi sento come se il mio stomaco fosse pieno di piombo dopo aver mangiato così pesante, ma il muro di mattoni contro la mia schiena è sorprendentemente confortevole."

"Cerco inutilmente di combattere la sensazione sonnolenta che mi sta sopraffacendo."

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

"Mi sveglio di soprassalto."

"Un basso rimbombo riverbera per i terreni della scuola. Immagini residue di scintille luminose lampeggiano nella mia vista come stelle."

"Qualcosa si alza verso il cielo dalla direzione del campo sportivo."

"Una coda di fuoco lo segue finchè un' esplosione di fiamme rosse e gialle illumina il cielo sopra la scuola con un altro forte rimbombo."

show fireworks
with dissolve

"Fuochi d' artificio."

"L' improvviso lampo di luce contro la tela del cielo notturno mi sveglia solo per farmi capire che in realtà è già buio."

"Quanto ho dormito? Mi sento stordito e non sento più il mio braccio destro."

"Quando tento di fletterlo, capisco perchè."

play music music_twinkle fadein 0.3

show rin basic_lucid_close_ni at Move((1.0,1.1,0.5,1.0),(0.9,1.1,0.5,1.0),1.0, time_warp=_ease_in_time_warp)
with Dissolve(1.0)

"Rin è pesantemente reclinata contro la mia spalla, quasi al punto di cadermi in grembo."

"Sta dormendo della grossa, neanche disturbata dai fuochi artificiali."

"La sua bocca è semiaperta e i suoi occhi sono chiusi tranquillamente. Un viso che dorme innocente come un bambino."

"Scuoto gentilmente Rin col mio braccio libero, cercando di svegliarla o se non altro, di muoverla così che il mio altro braccio sia liberato dalla presa."

"Il viso di Rin si contrae e le sue palpebre si chiudono più strettamente, come per resistere allo svegliarsi."

show rin basic_deadpanupset_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"Apre gli occhi gradualmente ma li tiene semichiusi, lasciando che la luce dei fuochi artificiali passi appena oltre le sue ciglia così che le sue iridi verdi specchiano i lampi luminosi delle esplosioni, poi mi guarda e aggrotta la fronte."

show rin basic_deadpan_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

rin "Ancora solo un pochino, okay?"

"La voce di Rin è sonnacchiosa e lenta, e lascia le sue parole borbottate quasi incomprensibilmente pigramente vaganti nell' aria."

"Sembra che non sia interamente conscia della situazione."

show rin basic_lucid_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"La testa di Rin ricade sulla mia spalla mentre si appoggia contro di me con tutto il suo peso."

"Si rannicchia contro il mio fianco, cercando di mettersi comoda ma facendo stare me molto scomodo allo stesso tempo."

"Divento intensamente, quasi dolorosamente cosciente del corpo caldo di Rin e del profondo, tranquillo movimento del suo petto contro il mio braccio, mentre il suo respiro presto ritorna al ritmo regolare."

"Non posso che ammirare la sua abilità di dormire, o la naturalezza con cui usa qualcuno che ha conosciuto per meno di una settimana come un cuscino."

"I razzi si alzano in cielo uno alla volta, spezzandosi in fiori di rosso, verde e oro, accompagnati dagli ooh ed aah degli spettatori."

"Cerco di spingere fuori dalla mia mente la sconcertante prossimità di Rin, perchè che posso farci? Spero solo che il suo “un pochino” lo sia veramente."

"Uno dopo l' altro, gli scoppi luccicanti nascono e muoiono in un batter d' occhio, colorando l' oscuro cielo notturno in un dipinto astratto costantemente mutevole."

"Ascolto i bassi rimbombi delle esplosioni e il tranquillo respiro di Rin, cercando di liberare la mia testa dal disorientamento che segue la sveglia."

"Fortunatamente, solo un pochino si rivela davvero essere solo un pochino, quando Rin riemerge di nuovo dal suo sonno e si sveglia prima che i fuochi terminino."

show rin relaxed_sleepy_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

rin "Mi sono addormentata."

show rin basic_awayabsent_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

show rin basic_lucid_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

show rin basic_awayabsent_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"Finalmente apre del tutto gli occhi e sbatte alcune volte le palpebre."

hi "Ti sei addormentata addosso a me. Due volte."

show rin basic_absent_close_ni at Position(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

rin "Non ti è piaciuto?"

hi "Uhh…, dunque…"

show rin basic_absent_close_ni at Move((0.9,1.1,0.5,1.0),(0.9,1.0,0.5,1.0),1.0, time_warp=_ease_time_warp)

"A dispetto dell' inconclusivo balbettare, Rin si siede dritta, allontanandosi da me."

hi "Bè, sei pesante."

"E' una bugia, non pesa quasi niente, ma devo stuzzicarla indietro, anche se sotto la cintura. La mia falsa protesta non ottiene alcuna reazione quando l' attenzione di Rin viene attratta verso l' alto dai lampi dei fuochi artificiali."

show rin negative_spaciness_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

"Sembra ipnotizzata dal colorato gioco delle esplosioni."

"Un lieve formicolio sale e scende per il mio braccio quando il sangue ricomincia a circolare. E' spiacevole ma mi aiuta a liberarmi di questa sensazione vertiginosa."

"Sempre più razzi si alzano in cielo, e i colori vivi delle loro esplosioni si riflettono dalle nuvole."

"Entrambi contempliamo fissamente i fuochi attraverso le chiome degli alberi, affascinati dallo spettacolo."

"Avremmo una vista del cielo vastamente migliore se ci muovessimo anche solo di un paio di metri, ma nessuno dei due si dà nemmeno la pena di suggerirlo."

show rin negative_worried_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

rin "Mi piacciono davvero i fuochi d' artificio, anche se guardarli mi fa sentire un po' triste, credo. E' come se volessero che tu li guardassi così tanto che sono rumorosi e luminosi, ma quando qualcuno guarda, sono già spariti."

show rin negative_sad_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

rin "E' come se non fossero nemmeno reali."

"…"

hi "Sono reali, te lo posso garantire."

hi "Tutto questo è… reale, sai?"

hi "Se ci pensi, nulla dura davvero a lungo. Anche qualcosa come la mia vita o la tua è solo un batter d' occhio nella storia di tutto, come uno di quei razzi. Poof, e siamo spariti."

hi "Ma siamo qui, non è vero?"

"Già, questa è la realtà. Rin, seduta accanto a me, le forti esplosioni dei fuochi d' artificio, il cielo vasto e illimitato. Queste cose sono decisamente reali, anche se non rimarranno qui per sempre."

"Mi sento caldo dentro, e mi chiedo se è perchè Rin mi è così vicina o se è solo la sensazione di essere vivo."

show rin negative_spaciness_close_ni at Position(xpos=0.9, xanchor=0.5)
with charachange

rin "Non so davvero cosa dovrei dire adesso."

hi "Non importa… forse sto soltanto parlando a me stesso."

hi "Però sai, i fuochi d' artificio sono belli… ma alla fine non è sciocco in qualche modo spendere così tanti soldi su una frazione di secondo di graziose faville?"

show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None

show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"Rin strappa il suo sguardo dallo spettacolo in progresso e si reclina all' indietro, guardandomi con una faccia disgustata."

rin "Wow, non mi sarei mai aspettata che fossi un tale cinico."

hi "Cinico è una parola piuttosto dura. Invece che quello, io mi considero un realista."

show rin relaxed_surprised_close_ni at tworight
with charachange

rin "Un realista non è solo la parola per come un cinico chiama se stesso?"

stop ambient fadeout 1.0
hide fireworks
with dissolve

"Il razzo finale esplode con un botto di argento e blu, lasciando i terreni spettralmente silenziosi per un momento finchè la folla non inizia a muoversi verso il cancello principale come una mandria di bestiame."

"Volute di fumo grigio si muovono lentamente verso i dormitori dal campo sportivo. L' odore della polvere da sparo che portano con sè, pungente e che ricorda la cenere, sembra volersi appiccicare ai miei capelli e vestiti."

hi "E' finito?"

stop music fadeout 3.0

show rin negative_spaciness_close_ni at tworight
with charachange

rin "Credo di sì."

scene bg school_dormext_full_ni
with locationchange

"Mi alzo e stiro la mia schiena dolorante. Dormire appoggiato contro un muro di mattoni non è poi stata una così buona idea dopotutto."

show rin negative_spaciness_ni at Move((0.7,1.0,0.5,0.8),(0.7,1.0,0.5,1.0),1.0, time_warp=_ease_in_time_warp)
with Dissolve(1.0)

show rin basic_absent_ni at tworight
with charachange

"Rin si alza a sua volta e si gira per guardarmi, con uno sguardo speranzoso sui suoi stanchi lineamenti."

"Anche se sembra avere problemi a mettermi a fuoco, mi sta guardando fisso, una cosa che non credo sia successa troppo spesso durante la settimana passata."

hi "Umm…così…"

"Realizzo d' un tratto che abbiamo avuto quasi un appuntamento, come per caso. Anche se non abbiamo fatto nulla."

"Ma non lo è stato… quindi perchè il sangue sta confluendo alle mie guance e la mia voce sta balbettando?"

"Non so cosa dovrei dire, specialmente dato che sembra che Rin stia aspettando che io dica qualcosa, ma fortunatamente lei risolve il mio problema per me."

show rin basic_deadpannormal_ni at tworight
with charachange

rin "Buona notte, Hisao."

hide rin
with charaexit

"Mi dà ancora uno sguardo prolungato, misurandomi dalla testa ai piedi, gira sui tacchi e se ne va, sparendo nella folla."

"…"

hi "Okay… Buona notte."

"Vengo lasciato lì in piedi, a dare la mia risposta all' aria fresca della notte."

"Sospiro."

"Il festival ha finito per non essere affatto come mi aspettavo."

"Ho finito per spendere l' intera giornata in un posto assieme a Rin, anche se nessuno di noi si è accordato su o ha suggerito che facessimo nulla."

"Semplicemente non avevo niente di meglio da fare ed evidentemente, neanche lei."

"Il calore di Rin rimane ancora per un po' nel mio corpo prima di sparire nella notte che scende."

window hide

    
#******************
#Lilly/Hanako path start

label it_A41:

scene bg school_gardens
with shorttimeskip

"Dopo avere comprato un piatto di plastica pieno di takoyaki da una bancarella che appartiene alla classe vicino alla mia, trovo da sedere nei giardini scolastici e guardo la gente che passa mentre sperimentalmente mangiucchio il piuttosto insipido pasto."

"Suppongo che non dovrei lamentarmi. E' meglio di niente e non è costato molto."

"Mentre guardo verso la scuola, osservare la gente che va e viene si dimostra essere un modo sorprendentemente divertente di passare il tempo mentre mangio."

play music music_tranquil fadein 0.3

play ambient sfx_crowd_outdoors fadein 0.3

show bg school_courtyard
show crowd
with locationchange

"Bambini accompagnati da genitori o nonni scorrazzano nel trambusto da evento a evento; una mano che trascina il loro accompagnatore e l' altra che porta un enorme, colorato snack."

"Non posso fare a meno di notare che l' età media delle persone qui tende verso gli anziani, qualcosa che ho notato anche quando stavo camminando per la città."

"Questa deve essere una di quelle città dove le uniche persone rimaste sono quelle che hanno vissuto qui per tutta la loro vita e ardentemente si rifiutano di andarsene…"

"…e quelle che vogliono vivere il resto dei loro giorni in uno dei pochi posti tranquilli in costante diminuzione."

"Immagino che quello spieghi anche molto su come la cultura scolastica di Yamaku sembri conservatrice."

scene bg school_gardens at Fullpan(8.0)
with locationchange

"Non che mi dia fastidio, affatto. Mi piace abbastanza la calma presente in Yamaku e nelle sue vicinanze."

"Il caldo, però, è tutta un' altra cosa. Stare seduto in un posto così a lungo ha focalizzato la mia mente su quanto fastidiosamente umido stia diventando il clima, adesso che la parte più calda del giorno è arrivata."

"Farò meglio a muovermi se-{w=.5}{nw}"

play sound sfx_warningbell

"Gah!"

"Il suono delle campane del carillon mi prende completamente di sorpresa mentre mi sto alzando, una reazione condivisa anche da alcune delle persone che stanno passeggiando."

"L' impianto di amplificazione crepita dopo che le campane cessano di suonare."

"La sua età diventa evidente quando la direttrice fa un annuncio a malapena comprensibile attraverso di esso, aprendo ufficialmente il festival che è già abbondantemente in corso."

"E' davvero divertente confrontare i sorrisi tranquilli dei più anziani con le smorfie alternativamente addolorate e annoiate dei loro più giovani protetti. Gli studenti, d' altra parte, sembrano preoccuparsene poco."

"Ciononostante, quando l' annuncio finalmente termina, tutti sono uniti in educati —se non eccessivamente entusiasti— applausi, e poi tornano ai propri affari."

"Infilando una mano in tasca per sembrare quanto più rilassato possibile, dò un' occhiata in giro in cerca di qualcosa da fare."

"…E' abbastanza difficile vedere molto lontano con tutta la gente intorno."

"Decido di ripiegare su una regola provata e affidabile: vai dove tutti gli altri sembrano andare. In questo momento, è il cortile scolastico e le sue vicinanze."

"Gettando il piatto usato in una pattumiera, mi dirigo verso l' edificio scolastico."

scene bg school_courtyard
show crowd
with locationchange

"Vedere il numero di chioschi intorno al perimetro della scuola mi sorprende. Molte delle classi devono aver deciso di aprirne più di uno."

"Mentre sto decidendo quale visitare per primo, noto uno striscione familiare con un bordo blu e testo rosso."

"Il chiosco di Lilly è un posto buono come un altro per cominciare. Sono curioso di vedere come sta andando, dopo tutto il lavoro che lei e la sua classe hanno fatto."

$ renpy.music.set_volume(0.6,2.0, "ambient")
stop music fadeout 2.0

scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange

"Camminando fino ad esso, comincio a capire perchè alla classe c'è voluto così tanto per organizzare tutto."

"Tranquillamente due volte più largo di molti degli altri chioschi e con equipaggiamento da cucina sparso ovunque, è più simile a un ristorante all' aperto che a un progetto per un festival."

"Dopo che uno studente davanti a me prende una ciotola di spaghetti e se ne va, mi avvicino al bancone."

"La ragazza dietro di esso sembra davvero esasperata, e mi chiede di aspettare un momento prima di sparire sotto il bancone."

"Cogliendo l' occasione, dò una rapida occhiata in giro."

"Vapore sembra starsi sollevando da ogni punto, mentre pentole e padelle cuociono a fuoco lento. I più ciechi degli studenti stanno aprendo pacchetti di ingredienti con l' aiuto di qualcuno che probabilmente è l' insegnante della classe 3-2."

"Non ci vuole molto per trovare Lilly tra di loro, che parla con l' insegnante mentre rapidamente conta le scatole e i pacchetti con le dita."

"Giudicando dalla sua espressione e il fatto che sia lei che l' insegnante sembrano essere in uno stato di leggera confusione, sembra che ci sia stato qualche problema di coordinazione."

"Prima che possa fissarli più a lungo, la ragazza dietro il bancone emerge di nuovo, solo per girarsi e chiedere dove è la scatola degli spiccioli."

"Lilly si ferma per un momento, prima che lei e la ragazza si scambino di posto al bancone e l' insegnante se ne vada di fretta da qualche parte."

show bg school_stalls2 at left
show lilly basic_smileclosed
with charaenter

li "Scusi, stiamo avendo qualche problema. Cosa gradirebbe ordinare?"

"Mi ci vuole un secondo per ricordarmi il perchè sono venuto qui. Distolgo i miei occhi per scorrere rapidamente il menù appoggiato sul bancone."

hi "Oh, uh, direi un po' di… zuppa di miso?"

show lilly basic_surprised
with charachange

li "Ah, sei tu Hisao?"

play music music_normal fadein 0.3

hi "Già. Sembra che siate piuttosto occupati."

show lilly basic_weaksmile
with charachange

"Il suo volto praticamente lo conferma quando abbandona la sua maschera da cameriera."

li "In qualche punto, c'è stato un disguido nel nostro ordine. Ora stiamo cercando di correre ai ripari, ma sembra che abbiamo solo metà di quel che ci serve."

hi "Servire porzioni più piccole non coprirebbe parte del problema?"

show lilly basic_sad
with charachange

li "Sembra che sia quello che dovremo fare, anche se vorrei che non lo facessimo. E anche il fatto che una buona metà della nostra classe sia sparita non aiuta."

"Guardo alle sue spalle per vedere quante persone stanno effettivamente lavorando al chiosco."

"Non direi possano essere più di otto."

hi "Immagino sia per quello che la vostra insegnante se ne è andata?"

show lilly basic_weaksmile
with charachange

li "Esatto. Sta cercando di raccogliere qualcun altro dei nostri compagni di classe perchè ci aiutino."

"Sentendo il suono di passi dietro di me, sbircio alle mie spalle per vedere una coppia di anziani che prendono posto in fila. Credo che farò meglio a smetterla di perdere tempo e chiacchierare."

hi "Ecco i soldi per la zuppa."

show lilly basic_smile
with charachange

li "Zuppa… oh, giusto, arriva subito."

"Lilly si gira e richiede una scodella di zuppa di miso mentre io le passo il denaro necessario."

show lilly basic_reminisce
with charachange

"Raccogliendo le monete nel suo palmo, non posso fare a meno di notare quanto efficientemente le conta con le sue pallide, lunghe dita. Finalmente soddisfatta che io le abbia dato la somma giusta, la mette in un piccolo vassoio metallico."

show lilly basic_smileclosed
with charachange

"Non ci vuole molto prima che la zuppa sia preparata e delicatamente piazzata nelle sue mani, dopodichè lei si gira e me la passa."

hi "Grazie. Tornerò per restituire la ciotola."

show lilly basic_smile
with charachange

li "Grazie, Hisao. Oh, un' altra cosa. Hai per caso visto Hanako?"

hi "Hanako… no, non oggi. Perchè?"

show lilly basic_sad
with charachange

"Dà un piccolo sospiro di abietta delusione."

li "E' okay. Stavo solo chiedendomi cosa stesse facendo per il festival."

show lilly basic_weaksmile
with charachange

li "Tornerai quando hai finito, allora?"

hi "Certo. Guarderò anche in giro per vedere se trovo Hanako."

li "Grazie, Hisao."

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"Mi allontano dal chiosco e trovo un posto a sedere, attentamente stringendo la fumante ciotola di legno tra le mani."

"Paragonata alla roba di prima, questa è ottima. Un po' fredda rispetto a come probabilmente dovrebbe essere, forse, ma il sapore basta per compensare ragionevolmente bene."

"Mentre bevo, non posso fare a meno di sentirmi un poco in colpa per non essere stato parte del festival tanto quanto gli altri."

"Non era veramente evitabile, considerato che sono stato buttato nella scuola solo una settimana fa, ma il pensiero mi pesa ancora."

"Quello, e il fatto che alcuni studenti non sembrano davvero stare godendosi il festival quanto i visitatori."

"Alla fine svuoto la mia ciotola di cibo e torno al chiosco, per restituirla."

"Considerando che non sembra esserci affatto fila, me la prendo comoda."

stop music fadeout 2.0

stop ambient fadeout 2.0

scene bg school_stalls2
with locationchange

"Sembra che la missione dell' insegnante abbia avuto successo: adesso c'è più di una dozzina di studenti che stanno dando una mano, e molte delle cose sono state disimballate."

"A dispetto del fatto che la maggior parte di loro sembri molto rilassata mentre lavorano, Lilly sembra ancora un poco stressata."

# This is where K1 and L1 would split



label it_A41a:
#Lilly Path Festival scene.

"…Giusto. So cosa fare. Anche se è solo una persona, renderò il festival più piacevole per lei."

"Mentre piazzo la ciotola sul bancone, chiamo Lilly."

show lilly basic_smile
with charaenter

li "Ah, Hisao. L' hai riportata?"

hi "Sì, ecco."

hide lilly
with charaexit

"La faccio scivolare nelle sue mani, e lei la porta a qualcuno che apparentemente è di servizio come lavapiatti. Considerando che non li ho visti qui prima, probabilmente è una punizione per il loro ritardo."

hi "Ehi, Lilly?"

show lilly basic_smileclosed
with charaenter

"Alza il capo e ritorna al bancone quando sente di nuovo la mia voce, realizzando che sono ancora qui."

hi "Vuoi andare a vedere un po' del festival?"

play music music_dreamy fadein 0.3

show lilly basic_pout
with charachange

"Gonfia le guance in disapprovazione. Sembra piuttosto graziosa, e in completa contraddizione con la sua natura normalmente riservata."

"Ci metto qualche secondo per capire cosa la stia irritando. Whoops."

hi "Ah… uhm, non volevo…"

show lilly basic_giggle
with charachange

"Lilly ridacchia, esponendo il suo prendersi gioco di me per quello che è."

li "Non sei ancora abituato alla scuola, vero?"

"Mi ha beccato."

show lilly basic_reminisce
with charachange

li "Però… dovrei veramente rimanere al nostro chiosco. C'è voluto fino adesso solo per sistemare tutto."

"Suppongo che la sua riluttanza non dovrebbe sorprendermi troppo, considerando quanto lavoro ha dedicato a questo."

hi "Tutto sembra stare andando bene adesso, però. E poi, avete dell' aiuto extra a disposizione, comunque."

show lilly basic_surprised
with charachange

"Un ragazzo che sta cucinando della soba si gira verso di noi, sogghignando."

"Studente" "Vai Lil, ti sei guadagnata una pausa. Possiamo farcela da soli, per adesso."

show lilly basic_displeased
with charachange

li "Se dici che è okay, allora suppongo di sì…"

show lilly basic_reminisce
with charachange

li "Ma, se avete bisogno di aiuto-"

"Studente" "Allora ti chiameremo. Vai, noi siamo a posto."

hide lilly
with charaexit

"Lilly finalmente abbandona la sua resistenza quando lui agita una spatola verso di lei. Trova la sua strada verso il retro del chiosco, e raccoglie il suo bastone nel processo."

"Suppongo che la prima cosa che dovremmo fare sia cercare Hanako. Lilly sembra un po' preoccupata per lei, e dubito che sia il genere di persona cui possa piacere girare in mezzo a una folla come questa, tutta sola."

hi "Così, immagino che dovremmo cercare Hanako. Da dove cominciamo?"

show lilly cane_reminisce
with charaenter

li "Hmm…"

"Entrambi diventiamo silenziosi per un momento mentre pensiamo."

hi "Forse è nella sua stanza?"

li "Ne dubito. Non tiene molte cose lì dentro, così non avrebbe niente da fare."

show lilly cane_satisfied
with charachange

li "…Ah! La biblioteca?"

"Un posto buono come un altro quando si è in cerca di un' avida lettrice, direi."

hi "Vada per la biblioteca. Per prima cosa controlleremo lì, allora."

scene bg school_lobby
with locationskip

stop music fadeout 2.0

"A parte i suoni soffocati della folla che filtrano dall' esterno, l' interno della scuola sembra quasi deserto."

"Per assicurarsi che tutti avessero spazio a sufficienza, immagino che tutti gli eventi siano stati organizzati per essere tenuti all' aperto, sui terreni della scuola. Sono decisamente molto ampi, per lo standard di qualunque altra scuola."

show lilly cane_smileclosed
with charaenter

li "E' silenzioso e tranquillo qui dentro, vero?"

hi "Già. Molto meglio del traffico e baccano che c'è fuori."

scene bg school_staircase2
with locationchange

"Facciamo con calma e lentamente camminiamo attraverso il primo piano della scuola, finalmente raggiungendo le scale per il secondo piano."

scene bg school_hallway2
show lilly cane_smileclosed
with locationchange

"Non posso fare a meno di notare come Lilly anticipa ogni porta e ostacolo, il suo bastone fermo e la sua mano che scivola lungo i corrimano dei corridoi."

hi "Conosci veramente bene la scuola, non è vero?"

show lilly cane_smile
with charaenter

"Sorride e annuisce davanti a sè."

li "Sono qui da alcuni anni ormai, così so dove è tutto."

show lilly cane_sad
with charachange

li "I dormitori ancora mi danno problemi però, qualche volta. Non sono stata lì altrettanto a lungo, e non sono bene organizzati quanto l' edificio principale."

li "Se mi ricordo bene, erano edifici inutilizzati prima che venissero rinnovati e usati come dormitori."

"Questo spiega perchè i dormitori maschili e femminili sembravano diversi dall' esterno, e perchè le loro stanze sembrino piuttosto inusuali."

"Avevo presunto che lei avesse vissuto nei dormitori fin da quando ha iniziato a frequentare la scuola, ma ora ricordo quello che ha detto ieri."

"Deve essersi trasferita durante la sua permanenza qui. Non c'è da stupirsi che non sia altrettanto familiare con la loro struttura."

hi "E' vero, lo avevi detto prima."

hi "Avevo presunto che la maggior parte degli studenti qui vivesse nei dormitori una volta iscritti. Per molti sembra così, comunque."

show lilly cane_reminisce
with charachange

"L' espressione di Lilly diventa più difficile da leggere, le mia domande hanno evidentemente toccato un punto delicato."

li "Bene… Come posso dire…"

show lilly cane_weaksmile
with charachange

li "Tutti… hanno le loro ragioni."

"Qualcosa mi dice che una di quelli che hanno “ragioni” è Hanako, e per quello lei sta girando intorno alla risposta. La mia situazione è un altro caso del genere."

"Immagino che sia una scelta che tutti qui hanno dovuto fare per sè… o, nel mio caso, che è stata fatta per me."

hi "E' inevitabile, credo. Almeno Yamaku stessa sembra un bel posto."

show lilly cane_smile
with charachange

li "Mi fa piacere sentirtelo dire. Pensavo che stesse cominciando a non piacerti."

hi "Che mi dici di te, però?"

show lilly cane_surprised
with charachange

"Il mio ritorcere l' affermazione di Lilly contro di lei la prende di sorpresa."

li "E' da molto che sono qui, perciò…"

hi "Non è quello. Sembravi solo piuttosto depressa riguardo ad Akira."

show lilly cane_smileclosed
with charachange

li "Hmm~"

hi "Che vuol dire quell' espressione?"

show lilly cane_smile
with charachange

li "Akira è già impegnata. Spiacente, Hisao."

"Lilly non può vedere quanto in fretta il mio palmo incontra la mia faccia alla sua maliziosa accusa."

hi "Ehi, ero preoccupato per te. Quello non è il modo di rispondere alla preoccupazione altrui."

show lilly cane_cheerful
with charachange

"Mentre sorride divertita, giriamo l' angolo del corridoio ed entriamo nella biblioteca."

scene ev hana_library_read_std
with locationskip

play music music_another fadein 0.3

"Quando lo facciamo, non è difficile vedere Hanako, considerando che la stanza è completamente vuota di chiunque altro."

scene bg school_library
with locationchange

"Dato che il personale non c'è, immagino che non sia necessario seguire le normale regole. La chiamo."

hi "Ehi, Hanako."

show lilly cane_surprised
with charaenter

li "Hanako è qui?"

"Quando sente le nostre voci, la testa di Hanako si solleva da dietro a un libro, probabilmente lo stesso che stava leggendo venerdì."

show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter

ha "Hisao… Lilly?"

hi "Abbiamo solo pensato di passare di qui. Lilly è riuscita a fuggire dal suo chiosco, con un pò di aiuto."

show lilly cane_pout at twoleft
with charachange

li "Quella non è stata davvero una fuga…"

show hanako emb_downsmile at tworight
show lilly cane_surprised at twoleft
with charachange

"Hanako si lascia sfuggire una risatina, sorprendendoci entrambi per un momento."

show hanako basic_bashful at tworight
with charachange

ha "Pensavo solo che… Lilly potesse non starsi godendo il festival."

hi "Bè, adesso possiamo godercelo insieme, giusto?"

show lilly cane_smileclosed at twoleft
with charachange

"Le due annuiscono felici prima che usciamo dalla biblioteca e ci dirigiamo verso le festività."

scene bg school_stalls1_ni
with shorttimeskip

stop music fadeout 2.0

$ renpy.music.set_volume(0.2,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3

"Dò qualche moneta alla ragazza dietro il bancone, e prendo le due tazze di tè in plastica. Cerco di accentuare un poco il mio inchino in deferenza al fatto che lei è molto ovviamente sorda."

"Ora che ci penso, probabilmente avrei dovuto chiedere aiuto invece di lasciare quelle due nei giardini mentre compravo da bere."

"Cercare di destreggiarmi con le due tazze di tè caldo (per loro) e una lattina di caffè (per me, da una macchina venditrice) non è esattamente facile."

"Con alcune attente manovre, però, riesco a tenere tutto stabile e dritto mentre cammino verso la panchina dove Lilly e Hanako sono sedute a chiacchierare."

show bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange

"A dire il vero è proprio un bel posto. Illuminato dalla luce della luna, è nascosto a una certa distanza dalle attrazioni principali."

"Comparato a quanto era caldo durante il giorno, questo posto è anche piacevolmente fresco a quest' ora."

"Non che importi così tanto. La maggior parte dei visitatori si sono mossi verso aree che sono o più vicine ai fuochi artificiali, o più in alto sulla collina per vedere lo spettacolo apparentemente programmato."

show lilly basic_smile_ni at twoleft
with charachange

li "Bentornato, Hisao."

show hanako basic_normal_ni at tworight
with charachange

"Ha delle buone orecchie. Non sono proprio vicino e Hanako non si era nemmeno accorta di me."

hi "Ecco qua. Scusate se è istantaneo, ma è tutto quello che gli rimaneva ormai."

"Hanako prende cautamente una tazza dalla mia mano destra, e io piazzo gentilmente l' altra tra le mani tese di Lilly."

show hanako basic_smile_ni at tworight
show lilly basic_smileclosed_ni at twoleft
with charachange

li "Allora ti è piaciuto il festival, Hisao?"

hi "Già, è stato piuttosto divertente."

"Una risposta onesta. Molto del cibo può essere stato piuttosto mediocre, ma alla fin fine è stato assai divertente, specialmente con Hanako e Lilly."

"Infatti, penso che quelle due possano essersi divertite anche più di me. Con Lilly e me al suo fianco, gran parte della natura di Hanako, introversa quando in presenza di altri, è sparita quanto basta perchè lei si divertisse."

stop ambient fadeout 1.0

$ renpy.music.set_volume(1.0,0.0, "ambient")

play ambient sfx_fireworks
play music music_twinkle fadein 0.3

scene bg misc_sky_ni
show fireworks
with dissolve

"Mentre ci siediamo e beviamo, il fischio del primo fuoco di artificio risuona prima di esplodere in una vibrante pioggia di blu contro il cielo notturno, annunciando l' inizio della fine per il festival."

"Grida entusiaste possono essere sentite dalla folla sparsa per i terreni della scuola che li celebra."

"Per interi minuti, io e Hanako guardiamo i fuochi artificiali sopra le nostre teste mentre Lilly li ascolta beatamente a occhi chiusi."

"Rosso, verde, giallo, a stella, circolare e fantasia, e ogni sorta di forme e colori riempiono l' aria, uno dopo l' altro, e danzano lungo il cielo."

"Nessun posto dove sia vissuto ha mai offerto spettacoli così lussuosi. Festival come questo erano una cosa del passato in una zona tanto metropolitana."

"Vedere una cosa del genere con queste due… probabilmente è il momento più felice che ho avuto da molto tempo."

scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange

li "E così… è fatta. Il festival sta finalmente terminando."

hi "Già."

"Dà un delicato, malinconico sospiro."

show lilly basic_concerned_ni at twoleft
with charachange

li "Per quanto possa lamentarmi di tutte le cose che dobbiamo fare, il fatto che ci saremo diplomati prima del prossimo festival di Yamaku è comunque triste."

show lilly basic_concerned_close_ni at twoleft
with characlose

"Avanzo e mi fermo accanto a Lilly, appoggiando gentilmente una mano sulla sua spalla."

hi "Non preoccuparti. Abbiamo ancora Tanabata più tardi quest' anno, giusto?"

show lilly basic_smile_close_ni at twoleft
with charachange

li "Hai ragione. Sarebbe bello andarci quando arriva."

"Minuti passano in silenzio, con solo le esplosioni dei fuochi d' artificio udibili."

"Vedere queste due mi ricorda quel consiglio che Lilly mi aveva dato mentre camminavamo in città insieme."

"“Tener cara la possibilità di farti nuovi amici”, eh?"

hi "Ehi, Lilly?"

show lilly basic_smileclosed_close_ni at twoleft
with charachange

"Gira leggermente la testa per mostrare che sta ascoltando, mentre lo sguardo di Hanako è ancora fermamente fisso sui fuochi artificiali multicolori che esplodono sopra di noi."

hi "Ti dispiace se mi unisco a voi per il tè di tanto in tanto?"

"Il sorriso sul suo volto è più che sufficiente per vedere la sua risposta."

show lilly behind_cheerful_close_ni at twoleft
with charachange

li "Sarebbe un piacere, Hisao."

stop ambient fadeout 1.0
# ^ I dunno where the fireworks are going to be ending, so move around whereever, I guess. -yujovi

window hide

stop music fadeout 2.0



###################
#Hanako Path
label it_A42:

#This is the "real" version of H1, edited to fit with the split marked in L1

# Hanako/Lilly festival
play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_stalls2
with None

show lilly basic_reminisce
with charaenter

"Lilly non sembra affatto favorevolmente impressionata, e non posso davvero biasimarla."

"Oltre ai problemi col suo chiosco, sembra essere ancora preoccupata per Hanako."

"Non posso davvero aiutarla con la prima cosa, così immagino che l' unica maniera che ho per aiutarla sia cercando di tranquillizzarla riguardo la nostra timida amica comune."

"Piazzando la ciotola sul bancone, la chiamo."

hi "Ehi, Lilly, non preoccuparti per Hanako. Andrò a cercarla e resterò con lei, okay?"

show lilly basic_weaksmile
with charachange

"Posso vedere il sollievo di Lilly chiaramente scritto sul suo viso."

li "Grazie, Hisao. E se vedi qualcuno della mia classe, puoi dirgli di tornare qui per favore?"

hi "Lo farò. Divertiti. E assicurati di fare una pausa, okay?"

show lilly basic_smile
with charachange

li "Lo farò se posso. Ci vediamo più tardi, Hisao."

scene bg school_courtyard
show crowd
with locationchange

"Lascio Lilly al chiosco e mi accingo a cercare Hanako."

"In un certo senso, mi sento in colpa per averla lasciata in mezzo alla folla, ma anche se era chiaramente sotto pressione, non posso evitare di pensare che si stia divertendo."

stop ambient fadeout 0.2
play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationskip

"I corridoi sono stracolmi di folla ondeggiante che vaga per il festival."

"Se c'è una cosa che so di Hanako, è che sarà il più lontano possibile da questo."

"E con tutti gli studenti che mostrano ad amici e familiari le loro stanze, dubito che sarà nei dormitori."

"Seguendo una cieca intuizione, mi muovo contro il flusso della folla."

"Fortunatamente, questa folla sembra leggermente meno festiva della media; assumo che sia in segno di considerazione per il corpo studente."

stop ambient fadeout 5.0

"Mentre forzo la mia strada attraverso le masse, non ci vuole molto perchè si riducano a nulla."

hide crowd
with Dissolve(2.0)

"Questo non è sorprendente, dato che sono davanti alla biblioteca."

"Nemmeno gli studenti più entusiasti si preoccuperebbero di mostrare a qualcuno questa sezione della scuola."

play music music_another fadein 0.3
scene bg school_library
with locationchange

"Mentre entro nella biblioteca, il rumore del festival si attutisce fino a un soffocato mormorio di sottofondo, e presto mi trovo nell' area di lettura sul retro della stanza."

"Dietro a uno dei banchi schermati vedo la cima di una testa, con capelli lisci e scuri che attraggono il mio occhio."

hi "Ehi, Hanako. Avevo la sensazione che ti avrei trovato qui…"

show hanako def_shock at Move((0.5,1.0,0.5,0.9),(0.5,1.0,0.5,1.0),0.5,time_warp=_ease_in_time_warp)
with charaenter

"La testa sobbalza un poco in shock prima di spiare lentamente da sopra al divisorio."

ha "H-Hisao?"

hi "Ehi. Lilly è piuttosto impegnata, così mi ha mandato a cercarti."

show hanako basic_normal
with charachange

ha "O-oh. Vuoi sederti?"

hi "A dire il vero, sono un poco affamato. Ti piacerebbe prendere qualcosa da mangiare da uno dei chioschi?"

show hanako defarms_worry
with charachange

ha "Um… io… io ho portato del cibo così…"

"Non dovrei essere sorpreso, ma valeva la pena di tentare. Aspettarsi che lei uscisse oggi era pretendere troppo."

hi "Che ne dici se mangiamo nella stanza del tè? Ci sono passato davanti mentre venivo qui, e non c' era nessuno."

hi "Possiamo preparare un po' di cibo lì, e sarà un po' più comoda. Che ne dici?"

show hanako cover_distant
with charachange

ha "C-certo. Andiamo."

show hanako basic_distant
with charachange

"Hanako chiude il suo libro e lo ripone via con movimenti abili e deliberati."

hi "Pronta ad andare?"

show hanako basic_normal
with charachange

ha "S…sì."

stop music fadeout 2.0

scene bg school_hallway3
with locationchange

"Camminiamo fianco a fianco dalla biblioteca alla stanza del tè."

"Come previsto, a malapena c'è un' anima in giro."

"Se non fosse per i mormorii attraverso i muri, non si direbbe che ci fosse un enorme festival in corso all' esterno."

show hanako emb_downtimid at tworight
with charaenter

"Hanako porta la sua borsa in entrambe le mani e si concentra solo sul pavimento di fronte a lei."

show hanako emb_downsmile at tworight
with charaenter

show hanako emb_downtimid at tworight
with charaenter

"Di tanto in tanto, sembra cambiare un poco il suo passo e cammina con passi leggermente più corti."

"La prima volta, non ci ho fatto caso, ma presto mi sono accorto che lo fa regolarmente."

hi "Va tutto bene?"

play music music_dreamy fadein 0.3

show hanako defarms_worry at tworight
with charachange

"Si ferma sul posto."

ha "C-cosa?"

hi "Non so… sembrava che stessi inciampando o qualcosa del genere…"

show hanako emb_blushing at tworight
with charachange

"Un roseo colorito cresce nelle sue guance mentre il suo sguardo ripunta verso il terreno."

show hanako emb_downtimid at tworight
with charachange

ha "Non… non è nulla."

hi "Sai, quando dici “nulla” in quel modo, le persone sono ispirate a fare altre domande."

"Per un secondo non penso che mi risponderà."

"Preparato a lasciar perdere, quasi ricomincio a camminare, quando…"

show hanako emb_emb at tworight
with charachange

ha "E' un… un gioco."

hi "Gioco?"

show hanako emb_downsmile at tworight
with charachange

ha "Vedi… il pavimento qui?"

"Che domanda bizzarra. Il pavimento sembra come qualunque altro pavimento; coperto da quelle piastrelle fatte di quadrati di linoleum."

"Nulla di degno di nota."

hi "Bè, sì. Cosa dovrei vedere?"

show hanako emb_downtimid at tworight
with charachange

ha "Qualche volta… quando non c'è nessuno… calpesto solo quelli più scuri…"

"La voce di Hanako diventa più fioca mentre la sua spiegazione continua, finchè posso a malapena sentire la sua voce nel silenzio roboante del corridoio vuoto."

hi "Più scuri?"

"Strisciando i piedi, Hanako indica con la punta della sua scarpa una piastrella che è a malapena un po' più scura delle altre."

show hanako emb_downsmile at tworight
with charachange

ha "C-come queste."

hi "Oh, giusto, così queste non vanno bene?"

"Punto a una piastrella vicina."

show hanako emb_emb at tworight
with charachange

ha "G-già. Qualcosa… qualcosa del genere."

hi "Oh, vedo. Giochi spesso a questo gioco?"

show hanako emb_downsad at tworight
with charachange

"Hanako scuote la testa."

hi "Solo quando i corridoi sono vuoti?"

show hanako emb_emb at tworight
with charachange

"Annuisce."

hi "Allora bene, non c'è bisogno di fermarsi, sto cominciando a sentirmi davvero affamato."

show hanako emb_smile at tworight
with charachange

"Annuisce di nuovo, questa vuolta con un po' più di entusiasmo."

hi "Va bene, andiamo."

hide hanako
with charaexit

"Continuiamo lungo il corridoio, e stavolta vedo che Hanako sta facendo un po' meno attenzione al pavimento."

"Mi chiedo; esattamente quanto solo deve sentirsi qualcuno per inventare un gioco come quello?"

"Ma, prima di capire cosa sto facendo, mi ritrovo a mirare ogni passo in modo che atterri sulle piastrelle giuste."

scene bg school_miyagi
with locationchange

"Il rumore del festival è leggermente più forte dentro la stanza del tè, ma la brezza che entra attraverso la finestra aperta fa sì che ne valga la pena."

"Senza pensarci, cammino fino al davanzale e inspiro profondamente. Qualche volta mi dimentico di quanto è pulita qui l' aria paragonata a quella di casa mia."

show hanako basic_bashful
with charaenter

ha "Vuoi… ti piacerebbe del tè?"

hi "Sarebbe otttimo, grazie."

hide hanako
with charaexit

"Mi viene in mente che questa è la prima volta che sono solo con Hanako senza che lei tenti di essere."

"Abbandonando la finestra, guardo mentre prepara una semplice teiera e dispone alcuni sandwich su un piatto."

"Glie lo ho visto fare diverse volte prima d' ora, ma questa volta sembra leggermente diversa."

"E' come se fosse…{w} calma."

"Finalmente piazza il piccolo vassoio sul tavolo e versa due tazze di tè."

"L' odore fresco di tè appena infuso si kischia con la brezza, e per un secondo mi sento come se fossi l' unico al mondo."

hi "Penso di sapere perchè ti piace questa stanza adesso."

show hanako defarms_worry
with charaenter

ha "Um… non capisco cosa vuoi dire."

hi "Beh, ci sono molte persone là fuori, ma qui dentro è come essere in un altro mondo."

hi "Puoi fingere che non ci sia nessuno per chilometri."

show hanako emb_downtimid
with charachange

ha "H-hai ragione."

ha "E' come se il mondo avesse dimenticato questa stanza."

show hanako emb_emb
with charachange

ha "E g-grazie a quello, tu puoi dimenticarti dell' esterno."

"In alcuni casi, quello sarebbe attraente."

"Per quanto possa dire, non esistono prepotenze convenzionali in questa scuola."

"Ma d' altro canto, non ho visto una sola persona parlare ad Hanako eccetto Lilly."

"Se vieni ignorato dal mondo, un posto dove puoi dimenticare la sua esistenza avrebbe un' attrazione particolare."

hi "Quella è un buon punto. E' come se questa stanza ti desse una sorta di completa libertà."

show hanako emb_smile
with charachange

ha "G-già."

show hanako basic_bashful
with charachange

ha "Senti… sai giocare a scacchi?"

hi "Scacchi? Ci ho giocato un po'."

hi "Immagino che tu ci abbia giocato prima d' ora?"

show hanako basic_distant
with charachange

ha "Un pochino…"

hide hanako
with charaexit

"Senza dire altro, Hanako si dirige verso uno degli armadi ed estrae un piccolo set da scacchi."

ha "Ti… ti va di…"

hi "Certo, perchè no?"

"La interrompo, ma non sembra darle fastidio."

scene bg school_miyagi
show hanako basic_normal_close
with shorttimeskip

"Arrangiamo i pezzi, e in breve tempo stiamo mandando delle pedine alla carica verso il loro inevitabile fato."

"Me la prendo con calma ed esamino intentamente ogni mossa e le sue conseguenze, mentre la nostalgia per il gioco passa in secondo piano in favore degli avvenimenti del momento."

"Per un certo tempo la partita è una prolungata battaglia di attrito, ma mi accorgo di una possibilità e apro una linea nella sua difesa."

show hanako basic_worry_close
with charachange

"Poche mosse più tardi, il suo re è chiuso in un angolo da diversi dei miei pezzi."

hi "Scacco matto."

hi "Non sei affatto male a questo gioco, sai?"

"Una valutazione onesta. La sua tecnica è piuttosto buona, ma diverse volte sono stato in grado di sfruttare la sua mancanza di previsione."

"Raccolgo un pezzo e lo esamino. Sembra relativamente nuovo, ma usurato per la sua età."

show hanako basic_smile_close
with charachange

ha "Suppongo… suppongo di no."

hi "Lilly gioca?"

show hanako def_worry_close
with charachange

"L' assenza di risposta da Hanako mi fa ripensare alla mia domanda."

ha "Un… un pò…"

ha "Q-questa è la prima volta che ho giocato contro qualcuno… che non fosse lei, o…"

show hanako emb_downsad_close
with charachange

"O…?"

"Si interrompe improvvisamente, lasciando la risposta pendente nell' aria. Qualcuno che conosceva prima di venire a Yamaku, forse."

hi "Bene, allora sono onorato di aver giocato contro di te."

show hanako emb_smile_close
with charachange

ha "Um… possiamo provare di nuovo?"

"Me lo chiede come se mi stesse chiedendo di tagliarmi le mani da solo. Lo spirito di competizione la ha afferrata?"

hi "Certo. Ma questa volta non aspettarti che ci vada piano con te…"

"Non che prima lo stessi facendo, bada. Sembra apprezzare il tono competitivo."

show hanako emb_downsmile_close
with charachange

ha "N… neanche io…"

window hide

stop music fadeout 2.0

#scene willl flow into K2 with Lilly finishing her time at the café and collecting the
#two to go to the Shanghai



#******************

label it_A43:
#Kenji rou-- er, Deep-Six

scene bg school_dormhallway at bgright
show kenji happy
with None

stop music fadeout 1.0

play music music_tranquil fadein 0.8

"Cosa ho intenzione di fare? Non ho alcun piano. Col senno di poi, è davvero stupido."

"Forse avrei dovuto invitare una ragazza? D' altra parte, tutto considerato, non credo che avrei potuto fare niente del genere. E' solo la mia prima settimana." 

"Una settimana che ho sprecato a essere impacciato quando vicino a quasi chiunque, inciampando sui miei stessi piedi nel tentativo di capire come funziona questo posto."

"Pensandoci, cosa ho concluso?"

"Chi avrei perfino invitato?"

"Dannazione, sembra che Kenji sia la mia unica possibilità realistica di avere della compagnia oggi."

"Questa è la cosa più deprimente che mi sia capitata da quando ho avuto un attacco di cuore perchè una ragazza ha confessato il suo amore per me."

"Non posso farci niente."

hi "Non so davvero. Non ho nulla da fare, immagino, ma un forte sembra un po' eccessivo."

hi "Sei sicuro di non volere uscire? Non è che i visitatori non entreranno nei dormitori oggi."

show kenji tsun
with charachange

"Sembra folgorato da questa rivelazione."

ke "Dannazione, potresti avere ragione. Questo posto non è sicuro oggi."

ke "Dobbiamo trovare qualche posto dove nasconderci."

"Diventa silenzioso per un momento, pensando."

show kenji neutral
with charachange

ke "Il tetto."

hi "Che ha il tetto?"

show kenji happy
with charachange

ke "Per oggi ci nasconderemo sul tetto."

ke "E' il posto perfetto, nessuno va mai lassù."

show kenji neutral
with charachange

ke "Incontriamoci lì tra un' ora. Devo prepararmi."

show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None

hide kenji
with charaexit

play sound sfx_impact2
with vpunch

"Sbatte la porta chiudendola e i lucchetti scattano."

"Dannazione, che c'è che non va in Kenji?"

"E pensare che ora sto seguendo la sua pazzia. Mi fa davvero sentire depresso."

"Mi sento come un fallimento."

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_courtyard
show crowd
with locationskip

"Una volta uscito, vengo salutato dal chiasso della folla."

"L' intera scuola è un fermentare di attività." 

"Ci sono chioschi ovunque, e la folla sciamante tra di essi è considerevole."

"Non mi aspettavo che il festival attraesse così tanti visitatori."

"Devo ammettere che le persone incaricate di decorare il posto si sono date molto da fare, e si nota veramente."

stop music fadeout 1.0

"La gente sembra divertirsi, e l' atmosfera è colorata, luminosa, e felice."

play music music_tragic

"Cioè, se non fossi così di cattivo umore ad un tratto."

"Al momento, è più fastidiosa che altro."

"Bè, niente da fare. Decido di attenermi al mio piano originale e mangiare, poi immagino di dover almeno vedere cosa sta combinando Kenji sul tetto."

"…"

scene bg school_stalls2 at Fullpan(8.0)
with locationchange

"Faccio un lento giro per i terreni per passare un po' di tempo, guardando i chioschi, ma non ho più voglia di giocare a nessuno dei giochi."

"I colori sgargianti mi irritano gli occhi e mi sento peggio ogni minuto che passa."

"Non riesco nemmeno a decidere cosa voglio mangiare, e l' ampia selezione combinata con le masse di energici visitatori non è di aiuto."

scene bg school_stalls1 at bgright
with locationchange

"Mi limito a dirigermi verso la bancarella più vicina che sembra offrire qualcosa di semicommestibile e a mettermi in fila."

"Risultano essere spaghetti."

"Risultano anche essere non molto buoni."

"Bene, almeno è nutrimento. Non è come se esigessi nient' altro, a questo punto."

scene bg misc_sky at Fullpan(25.0)
with locationchange

"Mentre rimescolo i miei sgradevoli spaghetti, mi chiedo oziosamente cosa stiano facendo gli altri in questo momento."

"Shizune e Misha sono sicuramente da qualche parte a organizzare le cose."

"Farò meglio a stargli alla larga, credo che non mi perdoneranno così facilmente per averle lasciate sole con questo affare."

"Mi aspetto che Emi stia correndo da tutte le parti, allegra al punto di essere deprimente."

"Non è possibile per me trovarla, ma neanche evitarla, quindi non importa."

"Lilly probabilmente starà aiutando la sua classe con quel progetto per il festival, e sarà decisamente troppo occupata per la compagnia di qualcun altro."

"Hanako non vorrà comunque parlare a nessuno, restando da sola o aiutando Lilly."

"Rin dovrebbe stare badando al suo murale e probabilmente non è di aiuto a degli ipotetici visitatori interessati."

"Andare da lei per un po' di pace e silenzio sembra la migliore opzione tra tutte, ma d' altra parte, non riesco neanche a immaginare che essere forzato a contemplare dell' arte migliori il mio umore, quindi lascerò perdere."

scene bg school_stalls1 at bgright
with locationchange

"Mentre ero perso nei miei pensieri, il mio cibo sembra essere sparito, e lo stesso per la mia fame."

"Immagino di aver rimosso l' esperienza di aver mangiato, che dovrebbe essere un bene."

"Sazio ma insoddisfatto, cammino verso l' edificio scolastico principale. E' già passata quasi un' ora."

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_lobby
show crowd
with locationskip

"La folla è ancora più fitta qui dentro che all' esterno."

scene bg school_hallway3
show crowd
with locationchange

"I corridoi sono quasi insopportabili, e non oso nemmeno pensare a come deve essere dentro le aule."

stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"Salgo le scale verso la mia destinazione."

"Il tetto."

"Fortunatamente, la porta del tetto non è chiusa a chiave, ma adesso c'è un cartello scritto a mano attaccato ad essa."

$ written_note("{size=55}{b}DIVIETO DI ACCESSO{/b}{/size}")

"No, grazie."

scene bg school_roof at bgright
with locationchange

"Il rumore del festival è sorprendentemente soffocato quassù, e il tetto sembra deserto, come previsto."

"Vicino a un punto dove la recinzione è crollata, c'è una pila di coperte che sembra stranamente fuori posto."

stop music fadeout 3.0

"Un momento."

play sound sfx_rustling

"Quella pila si è appena mossa un poco?"

"Sarebbe strano, dato che non c'è affatto vento."

"Cautamente estendo la mia mano e gli dò una spinta sperimentale."

show kenji rage_close at Alpha(0.0,1.0,0.2), Move((0.5,1.0,0.5,0.7),(0.5,1.0,0.5,1.0),0.2)
with vpunch

$ doublespeak(ke, hi, "AHHHHHHHHHHHHH!")

play music music_drama fadein 0.2

show kenji rage
with charadistant

"Spaventato, salto indietro."

ke "Chi è?"

hi "Maledizione, Kenji. Sono io."

show kenji tsun
with charachange

ke "Oh dannazione, mi hai spaventato amico."

hi "Così che stiamo facendo quassù?" 

show kenji neutral
with charachange

ke "Un picnic."

hi "Cosa?"

show kenji happy
with charachange

ke "Già. Ho coperte, ciambelle salate e whiskey. Questa è l' organizzazione finale, amico."

hi "Whiskey?"

hi "Non sei un po' troppo giovane per bere alcool?"

show kenji tsun
with charachange

ke "Ho 20 anni, sai."

hi "…non è vero."

show kenji neutral
with charachange

ke "E' vero e anche tu li hai."

hi "Cosa? E' assurdo."

show kenji tsun
with charachange

ke "Ehi, almeno TU ci ricavi qualcosa, tutto quel che ho avuto io è questa bottiglia di whiskey…"

"Sta blaterando incoerentemente, ma decido di stare al gioco."

hi "Così perchè hai una bottiglia di whiskey?"

show kenji happy
with charachange

ke "Mamma non ha potuto venire a visitarmi per il festival, così invece mi ha spedito un po' di costoso Single Malt."

hi "Una storia credibile."

ke "Ne vuoi?"

hi "…"

"Non è come se avessi niente da perdere. Questa giornata può solo migliorare."

hi "…perchè no."

hide kenji
with charaexit

show bg school_roof
with charamove_accel

show kenji happy_close at offscreenleft
with None

show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel

"Ci siediamo sulla pila di coperte che Kenji ha apparentemente trascinato fin quassù."

"Estrae una bottiglia di whiskey quasi piena e me la passa."

hi "Non hai nemmeno portato dei bicchieri?"

show kenji tsun_close at twoleft
with charachange

ke "No, questo non è un picnic da principesse romantiche. Che diavolo, amico?"

show kenji neutral_close at twoleft
with charachange

ke "Questo è un picnic virile."

ke "Niente bicchieri."

ke "Niente tovaglioli."

ke "Solo Whiskey. La bevanda dei veri uomini."

hi "Sì, si."

show kenji happy_close at twoleft
with charachange

ke "E ciambelle salate."

"Dò un' occhiata più da vicino alla bottiglia."

"Single malt whiskey invecchiato 12 anni, come ha detto."

"Scrollando le spalle, bevo un sorso. Brucia la mia gola come acido, ma il gusto non è spiacevole."

"Sento che mi va dritto alla testa, e il retrogusto mi rimane nel fondo della bocca, facendomi desiderare un altro sorso."

stop music fadeout 3.0

show kenji neutral_close at twoleft
with charachange

ke "Dovremmo delineare la nostra controffensiva e parlar male delle donne qui, dove non possono sentirci."

show kenji tsun_close at twoleft
with charachange

ke "Dannazione, ho dimenticato di portare con me i miei diagrammi."

"Decido di giocare a un gioco da bevitori con me stesso. Ogni volta che Kenji dice “cospirazione femminile”, berrò un sorso."

$wdt_off(False)

scene black
with delayblinds

centered "Quattro o cinque ore, o forse diversi giorni più tardi:\n{w} (ho perso il conto)"

#...music for this scene would be good, too.

scene ev kenji_rooftop
with delayblinds

window show

ke "Non dovresti sentirti giù, amico! Rilassati, cazzo! Seriamente, seriamente!"

hi "Sono rilassato, Dio ti stramaledica!"

ke "Dico quello che vedo!"

scene ev kenji_rooftop_kenji
with flash

ke "Pensaci. Quand'è che le case e la terra hanno cominciato a diventare sempre più costose? Quando le donne hanno iniziato a entrare nella forza lavoro, perchè creava nuclei familiari con doppio reddito."

ke "Già mi sono dimenticato i miei diagrammi, ma, e dovrai credermi sulla parola, le donne sono connesse alla decadenza di tutta la società."

show ev kenji_rooftop_large at Pan((288,376),(1024,260),1.0,time_warp=_ease_time_warp)

hi "Vedo. E' abbastanza duro da credere."

"Anche se dico così, in qualche maniera, tutto quello che Kenji dice sembra avere più senso ora."

"Tutto cade al suo posto ma non so se è perchè lui sa spiegare le cose più chiaramente quando è ubriaco, o perchè io capisco tutto meglio da ubriaco."

show ev kenji_rooftop_large at Pan((1024,260),(288,376),1.0,time_warp=_ease_time_warp)

ke "No amico, pensa. Pensa! Pensa alle implicazioni più profonde!"

ke "La gente poteva permettersi di cominciare a dire “Oh, bene dato che adesso due membri della famiglia stanno guadagnando denaro invece di uno solo, sicuramente possono permettersi qualcosa come i costi crescenti delle proprietà.”"

show ev kenji_rooftop_large at Pan((288,376),(1024,260),1.0,time_warp=_ease_time_warp)

hi "Capisco il tuo punto. Ma la terra in Giappone è sempre stata costosa."

show ev kenji_rooftop_large at Pan((1024,260),(288,376),1.0,time_warp=_ease_time_warp)

ke "…E il prezzo della terra generalmente sale quando un paese comincia a sottoporsi all' industrializzazione. …Ma no! E' a causa delle donne! Correlazione equivale a causa, sai."

show ev kenji_rooftop_large at Pan((288,376),(1024,260),1.0,time_warp=_ease_time_warp)

hi "Pensavo che la correlazione non equivalesse a causa. Bè, non importa, forse hai ragione."

show ev kenji_rooftop_large at Pan((1024,260),(288,376),1.0,time_warp=_ease_time_warp)

ke "Ho sempre ragione. Già, scommetto che le donne hanno creato anche l' industrializzazione, per coprire le loro tracce."

ke "Diabolico."

ke "Così sì, possono andarsene tutti a fottersi!"

scene bg school_roof_ni
show kenji rage_ni at Move((0.5,1.0,0.5,0.9),(0.5,1.0,0.5,1.0),0.5,time_warp=_ease_in_time_warp)
with locationchange

"Si alza in piedi, impressionandomi perchè sono abbastanza sicuro che io non potrei neanche se volessi. Urla estremamente forte come se si fosse dimenticato il concetto di volume. Mi ritraggo e quasi voglio coprirmi le orecchie."

ke "Aaagh, come sarebbe stato bello se avessi potuto essere laggiù… Ma no. Vedi, pensare in quel modo è una trappola, credi di star perdendoti qualcosa, ma alla fine di quella strada non c'è altro che disperazione…"

show kenji tsun_ni
with charachange

play music music_sadness fadein 1.5

"Kenji recupera la bottiglia e butta indietro la testa, cercando di versarsi l' alcool in bocca, ma finisce soltanto per versarselo addosso."

show kenji rage_ni
with charachange

ke "Dannazione! Vedi, la mia mira è terribile, e la cosa brutta del bere è che diventa solo peggiore mano a mano che si va avanti!"

show kenji tsun_ni
with charachange

ke "Oggi è il giorno della disperazione."

"La sua voce immediatamente scende quasi a un bisbiglio, ma inizia a parlare molto più rapidamente di prima, biascicando leggermente le parole a causa del whiskey."

"Mentre parla, agita la bottiglia in giro, versando parte dei suoi contenuti qua e là."

ke "Già, sai quale è stato l' evento più scioccante della mia vita?"

"Ho un vago ricordo di lui che mi dice del secondo evento più scioccante della sua vita, che consisteva di un uccello che gli faceva popò in testa."

"Non mi aspetto particolarmente grandi cose da questo, ma annuisco perchè continui comunque."

show kenji neutral_ni
with charachange

ke "Non ci crederesti, ma avevo una ragazza qui una volta, credo fosse l' anno scorso."

ke "Già, ti ho appena fatto scoppiare la testa, eh? Vedi, non lo ho mai detto a nessuno."

"E' vero, il pensiero mi fa scoppiare la testa. Improvvisamente, voglio la bottiglia. La prendo da Kenji e inghiotto per quanto posso."

show kenji tsun_ni
with charachange

ke "Ero più innocente allora, e credevo che fosse sana di mente, a differenza della maggior parte delle donne. Ma poi un giorno, ci ingaggiammo in… rapporti sessuali."

ke "Non è stato male, ma poi immediatamente dopo l' evento che è il punto di quelle cose, avvenne qualcosa di strano e spaventoso."

show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove

"Alza le braccia e si appoggia contro il recinto, stringendo gli occhi."

ke "Ho iniziato a sentirmi incredibilmente stanco e sonnolento! Non è normale, amico! Che cazzo?"

ke "Voglio dire, normalmente, sarebbe un momento ad alta tensione e con l' adrenalina che pompa nella vita di chiunque, ma i miei livelli di energia stavano cadendo come un mattone!"

ke "Qualcosa di sinistro stava venendo tramato, potevo sentirlo."

ke "Quello è stato quando ho capito… che le donne sono pericolose, e assorbono la vita di tutti gli uomini attraverso l' unico bene che è quasi esclusivamente sotto il loro controllo!"

ke "Disgustoso."

show kenji neutral_ni at tworight
with charachange

ke "Già, stai meglio così, fratello…"

"Kenji aveva ragione, questo è veramente il giorno della disperazione. Bevo di più per evitare di elaborare quello che ha appena detto."

ke "Ora sono l' ultimo uomo sano di mente in un mondo folle… quando altri se ne accorgono, ci sarà una guerra, una grande guerra tra gli uomini e le forze del femminismo."

ke "Ma il problema è che non tutti gli uomini combatterebbero al mio fianco… bello schifo. Potrei rendere i requisiti d' ammissione piuttosto bassi, qualunque uomo va bene. Ma non i tipi allevati dalle loro mamme o sorelle, questo è certo."

show kenji tsun_ni at tworight
with charachange

ke "E nessuno a cui piacciono i porno dove le ragazze hanno il pisello."

hi "Ha… Quella situazione mi sembra improbabile, come se non potesse capitare, come… come se non fosse molto probabile capitasse."

"L' alcool deve stare funzionando."

"Nonostante tutto, mi sento ancora depresso perchè oggi sono quassù."

"Non stavo veramente aspettando il festival con la stessa eccitazione del resto della scuola, ma lo stesso…"

"Sarebbe stato bello andarci con qualcuno. Da quassù, suonava certamente come se tutti si stessero divertendo. Forse mi sto perdendo qualcosa di buono."

"E' solo che non c' era nessuno con cui sarei potuto andare."

"O forse c' era. Così tante opportunità, guardando indietro ora, e devo averne sprecate così tante."

ke "Dannazione, questa è la vera disperazione… La parte peggiore è che qualche volta mi sento come se non avessi scelte nella mia vita, sai?"

ke "Come se non avessi mai una chance di prendere una decisione, le cose capitano e basta."

ke "Come se fosse tutto preprogrammato. Come il fato… o qualcosa del genere. Come se non ci fosse modo in cui possa avere controllo su quello che faccio."

stop music fadeout 0.5

show kenji rage_ni at tworight
with vpunch

ke "Svelto, fammi una domanda!"

hi "Uh…"

ke "Adesso!"

hi "Non posso davvero…"

show kenji tsun_ni at tworight
with charachange

ke "Vedi? Questo è solo un altro esempio! Dannazione! Merda! Dannazione! Vedi? Adesso, quando sto tentando di andare contro il mio destino e di prendere controllo della mia vita, non c'è nemmeno l' opportunità."

ke "Dannazione, amico, mi hai deluso. Mi hai deluso per l' ultima volta. Stronzo."

show kenji tsun_ni at Move((0.7,1.0,0.5,1.0),(0.7,.9,0.5,0.5),1.0,time_warp=_ease_time_warp)
with Pause(1.0)

show kenji tsun_ni at RotoZoom(0,90,.7,1.0,1.0,0.0,rot_time_warp=_ease_out_time_warp,xpos=0.7, xanchor=0.5, ypos=.9, yanchor=0.5), Move((0.7,.9,0.5,0.5),(0.7,1.0,0.5,0.3),.7,time_warp=_ease_out_time_warp)
with Pause(.7)
play sound sfx_impact
with vpunch

"Cade in ginocchio e poi di fianco, riverso sulla ghiaia del tetto."

hi "Ehi, stai bene?"

ke "No, non sto bene, non vedi che sono in preda alla disperazione?"

"Sta parlando in tono sarcastico."

show kenji neutral_ni at Move((.7,1.0,.5,0.0),(.7,1.0,.5,.7),1.0, time_warp=_ease_in_time_warp)
with charachange

"Improvvisamente, Kenji si siede, si spolvera goffamente, e punta la sua mano verso di me allungandola verso la bottiglia. Glie la metto in mano."

show kenji tsun_ni at Position(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange

ke "Che diavolo? Dannazione, hai fatto fuori quasi l' intera bottiglia. Vedi, è come se non avessi opzioni nella vita…"

ke "E' così che sarà per tutto il resto del tempo?"

hi "Bè, sono abbastanza sicuro che non sarà così per tutto il resto del tempo."

"Di qualunque cosa stia parlando. La testa mi gira. Mi alzo e mi appoggio al recinto, sperando che mi aiuti a concentrarmi un po'."

show kenji tsun_ni
show bg school_roof_ni
with charamove

play music music_kenji fadein 0.5

ke "Già, lo so. Dobbiamo combattere il potere con tutto quello che abbiamo. E' l' unico modo di vivere."

show kenji neutral_ni
with charachange

ke "Sei un tipo a posto."

show kenji happy_ni
with charachange

ke "Questo legame fraterno è quello che mi fa andare avanti in questi tempi bui."

show kenji neutral_ni
with charachange

ke "Dovremmo andare a caccia di donne."

hi "Faccia di donne? Cosa?"

show kenji neutral_close_ni
with characlose

ke "Caccia. Caccia di donne. Ma lo dobbiamo fare ora, prima che perda questo coraggio in bottiglia."

"Sta gesticolando esagitatamente. Pazzamente, perfino."

show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant

"Faccio un passo indietro."

show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"Lui fa un passo avanti."

stop music fadeout 1.0

show kenji happy_close_ni
with charachange

ke "Che hai che non va? Non sei dell' umore giusto per l' amore?"

hi "Per essere franchi… no."

show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant

"Faccio un altro passo indietro."

show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"Lui fa un altro passo avanti."

"Si china estremamente, spiacevolmente vicino verso di me."

hi "Che diavolo, piantala di venire così vicino, mi dà fastidio."

ke "Così vicino come? Ehi, non dovresti appoggiarti al recinto in quel modo, non è molto sicuro."

"Cerco di allontanarmi da Kenji, ma il mio equilibrio non è molto buono."

play music music_tension fadein 0.1

"Lottando contro le vertigini, afferro uno dei paletti, ma poi lo sento cedere appena lo carico col mio peso."

"…non va bene. Anche se il mio cervello offuscato dall' alcool non sembra essere bene in grado di registrare il perchè."

show black behind bg
with None

show n_vignette at RotoZoom(0,0,0.0,4.0,1.2,0.2, xalign=0.5, yalign=0.5)
with Pause(0.2)

show n_vignette at RotoZoom(0,0,0.0,1.3,0.0,8.0, xalign=0.5, yalign=0.5)
show kenji happy_close_ni at RotoZoom(0,0,0.0,1.0,0.0,8.0, xalign=0.5, yalign=0.5)
show bg school_roof_ni_crop at RotoZoom(0,0,0.0,1.0,0.0,8.0, xalign=0.5, yalign=0.5)


"La faccia di Kenji sembra stare diventando più piccola però, il che è un po' un sollievo."

"Molto più piccola, in effetti. E rapidamente."

"Sembra esserci un po' di vento adesso. In qualche modo mi fa sentire quasi senza peso."

"Mi sento stordito, come se la mia mente fosse stata cancellata."

hi "Sto… cadendo…?"

scene nightsky rotation
with locationchange

"Posso vedere il cielo notturno mentre giro nell' aria. La bottiglia fluttua lontano dalle mie dita e sparisce nel nulla mentre cado.."

"Capisco che questa è la giusta fine di un giorno veramente, veramente pessimo."

window hide

stop music fadeout 0.1
play sound sfx_crunchydeath

return


