# AI Specialist — Appunti ed esercizi Python

Raccolta personale di appunti, esempi ed esercizi svolti durante il corso **AI Specialist**. Il repository segue il percorso dalle basi di Python alla manipolazione dei dati e ai primi esperimenti di machine learning.

I materiali sono pensati per lo studio e il ripasso: comprendono notebook con spiegazioni e prove, script di esercitazione e piccoli dataset di supporto. La raccolta viene aggiornata con il proseguire delle lezioni e può contenere appunti incompleti, tentativi e soluzioni da rivedere.

## Contenuti

Le cartelle numerate seguono l'ordine delle lezioni. I file `.ipynb` raccolgono appunti e codice eseguibile; gli script `.py` contengono esempi ed esercizi.

| Cartella | Argomenti |
| --- | --- |
| [1_intro](1_intro/) | Introduzione a Python, variabili, tipi, conversioni e operatori |
| [2_strings](2_strings/) | Stringhe e operazioni sul testo |
| [3_conditionalstructure](3_conditionalstructure/) | Condizioni e strutture `if`, `elif`, `else` |
| [4_math_random](4_math_random/) | Calcoli e uso dei moduli `math` e `random` |
| [5_Errors](5_Errors/) | Errori ed eccezioni |
| [6_Lists](6_Lists/) | Liste e operazioni sulle sequenze |
| [7_Loops](7_Loops/) | Cicli e iterazioni |
| [8_dictionaries_sets](8_dictionaries_sets/) | Dizionari e insiemi |
| [9_Functions](9_Functions/) | Funzioni, parametri, valori di ritorno e scope |
| [10_Lists_Comprehension](10_Lists_Comprehension/) | List comprehension |
| [11_pandas_series_df](11_pandas_series_df/) | Series, DataFrame e gestione di dati con pandas |
| [12_regressione](12_regressione/) | Regressione e previsione dei prezzi degli immobili |
| [13_File](13_File/) | Lettura e scrittura di file di testo, CSV e JSON |
| [14_classificazione](14_classificazione/) | Classificazione delle cancellazioni di prenotazioni alberghiere |
| [15_oop](15_oop/) | Introduzione a classi e oggetti |
| [16_type_hints](16_type_hints/) | Annotazioni di tipo per variabili, collezioni e funzioni |
| [A_Esercizi](A_Esercizi/) | Prima raccolta di esercizi di consolidamento |
| [B_Esercizi](B_Esercizi/) | Ulteriori esercizi di consolidamento |

## Esercitazioni sui dati e sul machine learning

- **[Analisi dei dati con pandas](11_pandas_series_df/notebook.ipynb)**: operazioni su Series e DataFrame, selezione e trasformazione dei dati, lettura e salvataggio di CSV.
- **[Regressione sui prezzi degli immobili](12_regressione/notebook.ipynb)**: esplorazione dei dati, gestione dei valori mancanti, trasformazione delle variabili, pipeline e confronto tra modelli di regressione.
- **[Cancellazioni delle prenotazioni hotel](14_classificazione/esercizio_hotel.ipynb)**: preparazione dei dati, regressione logistica e Random Forest, valutazione delle previsioni, analisi dell'overfitting e ricerca degli iperparametri.
- **[Confronto delle colonne del dataset hotel](14_classificazione/confronto_colonne_hotel.ipynb)**: esperimenti sull'effetto della selezione delle variabili e discussione dei limiti della valutazione.

I risultati riportati nei notebook appartengono alle singole esercitazioni e alle relative scelte sui dati.

## Come consultare i materiali

Per iniziare, segui le cartelle in ordine numerico oppure apri direttamente l'argomento che vuoi ripassare. Per eseguire il codice servono **Python 3** e un ambiente per notebook, ad esempio **JupyterLab**.

Le librerie esterne usate nei notebook di analisi dati e machine learning sono principalmente `pandas`, `numpy`, `matplotlib`, `seaborn` e `scikit-learn`. Molti esercizi introduttivi usano soltanto la libreria standard di Python.

### Preparazione dell'ambiente

Clona il repository e apri un terminale nella sua cartella:

```powershell
git clone https://github.com/MasCorra/ai-specialist-python-lessons.git
cd ai-specialist-python-lessons
```

Su **Windows, con PowerShell**, puoi creare un ambiente virtuale, installare le librerie e avviare JupyterLab con:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn
.\.venv\Scripts\jupyter.exe lab
```

Su **macOS o Linux**, i comandi corrispondenti sono:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn
.venv/bin/jupyter lab
```

I comandi richiamano direttamente l'ambiente virtuale, senza richiederne l'attivazione. Il repository non include attualmente un file con le versioni delle dipendenze: questi comandi sono una base per preparare l'ambiente, senza garantire la riproduzione esatta di tutti gli output salvati.

Riferimenti: [ambienti virtuali Python](https://docs.python.org/3.11/library/venv.html) e [installazione di Jupyter](https://jupyter.org/install).

### Esecuzione di notebook e script

- Apri il notebook dalla cartella della lezione e seleziona il kernel dell'ambiente in cui hai installato le librerie.
- Esegui le celle dall'alto verso il basso: molte dipendono dalle variabili definite nelle celle precedenti.
- Per gli script, spostati nella cartella dell'esercizio e avviali con l'interprete dell'ambiente virtuale. Ad esempio, da `1_intro` su Windows: `..\.venv\Scripts\python.exe ex1.py`.

## Note sui file e sui percorsi

I CSV e i file di esempio presenti nelle cartelle delle lezioni sono utilizzati dagli esercizi. Molti percorsi sono relativi alla cartella di lavoro: se un file non viene trovato, controlla di eseguire il notebook o lo script dalla cartella corretta.

Il notebook `14_classificazione/confronto_colonne_hotel.ipynb` contiene un percorso assoluto locale da adattare alla posizione del repository sul proprio computer. Il notebook principale sugli hotel cerca invece `hotels.csv` nella cartella di lavoro e, se manca, prova a scaricarlo dalla fonte indicata nel codice.

Alcuni esercizi sulla gestione dei file creano o sovrascrivono file di esempio. Leggi le celle o lo script prima di eseguirli.

---

Questa raccolta documenta il mio percorso di apprendimento: esempi, commenti e approfondimenti possono essere corretti e ampliati durante lo studio.
