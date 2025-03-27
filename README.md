# kiparla-annotazione

## Decisioni prese

* I nomi propri hanno il lemma capitalizzato
* le `xpos` per ora sono state rimosse. In futuro valutiamo se ha senso riesumare quella colonna e usarla per un tagset specifico del parlato
* teniamo le strutture **non proiettive** senza alterare la sintassi per ottenere la proiettività
* parole interrotte (es `~versità` o `pensio~`): nel caso in cui è facilmente intuibile dal contesto quale sia la parola in questione, usiamo quella come lemma e la PoS che avremmo attribuito come PoS. Se il contesto non è abbastanza informativo, usiamo `X` come PoS e la stessa form come lemma. L'informazione che fosse una parola interrotta comunque non viene sovrascritta perché c'è una feature apposita nel MISC
* dialetto e parole straniere: teniamo la PoS che ha quella parola in italiano. Per il lemma, lo teniamo uguale alla form. Usiamo `OrigLang=[ISO|dia|unknown]` nel MISC per i casi di code switching (i.e., non i prestiti o i forestierismi). Questo per i casi dove la questione è palese. Se il token è ambiguo non lo segniamo e ci sarà comunque il metadato `# contains variation` a livello di maximal unit (ovvero, quando almeno una delle unità contenute iniziava per cancelletto)
* `tipo`, `raga`, congiunzioni con valore discorsivo etc... > siamo conservative e teniamo la PoS da dizionario
* `come` > `ADP` per casi tipo "sì vedi un po' come i laureandi non devono andare sulla torre degli asinelli" e "ci vuole il turn-around come lo chiamano i in inglese" e `PRON` per "voi principalmente come vi muovete in città?"
* `mio`, `tuo` etc... > `ADJ`
* `chi`, `dove`, `quando` etc > `PRON`
* `che` > `PRON` quando dipende da nome, `SCONJ` quando dipende da altro
* numeri tutti `NUM`
* articoli > lemma `il`
* pronomi > lemma uguale alla form

## Assignments

| who | assignment | done | revised | features |
| --- | ---        | ---  | ---     | --- |
| Caterina | TOD1005bis fino a frase 372 | | | |
| Cristina | TOD1005bis da frase 373 in poi | | | |
| Silvia | BOD2018 fino a frase 310 | done | done | done (*mancano pronomi) |
| Manuela | BOD2018 da 311 in poi | done | done | done (*mancano pronomi) |
| Manuela | BOA3017 fino a frase 420 | done | done | |
| Ludovica | BOA3017 da 421 in poi | done | done | |
| Eleonora | PBB004 fino a frase 450 | done | done | |

## Dubbi sui file

### BOA3017

#### Trascrizione

* 462: finalmente l'insalata? > io la mangio l'insalata
* [194]: mangia in realtà dice magna
* tedesca di dresda che abbiamo > secondo me dice avemo
* comunque pensavo di tornare ... voglia di fare > comunque pensavo di torna ... di fa
* per cena vorrei essere qua > vorrei esse qua
* 765 - come devi fare > come devi fa
* la percentuale deve essere alta > la percentuale deve esse alta
* a trattenere troppo > a trattene troppo
* oggi non torni a casa a dormire > a casa a dormi
* ti fa pure schifo perché lo mangi > ti fa pure schifo perché lo magni?
* sparare sempre e comunque > spara sempre e comunque
* da quando sono nata penso > da quando so nata penso

## Fillers

- mhmh
- ah
- eh
- oh
- mh
- beh
- vabbè
- ehm
- ihih > forse {ride}?
- vabbè

 ## Appunti BOD2018 (Silvia)

- 112—> sempre con tutte ragazze - tutte singole // tutte?

- uno art. lemmatizzato di default “uno” (controllare)

## Appunti PBB004 (Eleonora)

- (84, 84) _c'entrare_ o _centrare_?
- (244 e 246) _fa_ in _anni fa_ ?
- _Santo_ / _Don_ nome proprio ? --------------------- [Ludovica] io l'ho trattato come aggettivo (san) o nome (don)

## Appunti Ludovica

^((?!TID|#).)*$

## Appunti Caterina TOD1005bis
numero righe a sinistra (1,2....)
- 4: nessun altra lingua - ho lasciato DET DET NOUN, anche se sonon stata in dubbio se sostituire 'altra' con ADJ > [Ludovica] https://universal.grew.fr/?custom=67e3cbf89dcc1
- 8: che SCONJ > PRON
- 10: li PRON > lemmatizzazione? non tocco i pronomi...
- 12: forse questa unità va spezzata, molto lunga!
- 28: che SCONJ > PRON (sostituzione che ho fatto in modo sistematico), per PREP > SCONJ
- 30: per PREP > SCONJ
- 34: quale lemma per foni?
- 36: spezzare!!!
- 77: reti?? > check, forse radici
- 118: spezzare!

- 7: richerebbe > corretto in 'richiederebbe'

## Da controllare

### BOD2018

da solo
po'

ISSUES up to now

    Proper nouns > lemma is capitalized

    Acronyms?

    BOA3017:

    esse o esse (sent376. Tu829)

    PBB004:

    Erressea

    Metalinguistic:

    BOA3017

    Canta (sent 200, 202, 203)

    PVU e pshh e xxxxxs?

    Dubbi generici:

    BOA3017


    Angillete?

    Auxiliaries

    Italian auxiliary verbs can be divided into:

    copulas

    stare in “sto arrivando”

    tense auxiliaries, used to form compound tenses represented by avere “to have” and essere “to be”;

    passive auxiliaries, used to form passive verb forms represented by essere “to be” and venire lit. “to come”.

    Following the UD guidelines, Italian modal verbs are handled as modal auxiliaries (e.g. potere “can”, dovere “must”).

    Parole inglesi

    Turn around

    Open space

    Pronomi

    Interruzioni

    X

    Dialetto

(raga in BOA3017)

237:8

411:2

1:3


(fanculo in BOA3017)

94:26

94:23

383:4 frantumi?
