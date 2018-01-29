#encoding "utf-8"

//Phrase -> Adj Noun interp (Phrase.Name);
Phrase -> Word<gram=~"PR", gram="S", wfm=/[А-Яа-я]{3,20}/> interp (Phrase.Name);
Phrase -> Word<lat, wfm=~/(DocumentSplitter)/> interp (Phrase.Name);