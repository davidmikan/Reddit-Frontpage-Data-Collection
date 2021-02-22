# Übersicht

Sämtliche Skripts, die bei der Datenerhebung verwendet wurden, sind im Ordner [scraper](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/tree/main/scraper). Hierbei enthält [pg.py](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/blob/main/scraper/pg.py) die PostGroup Klasse, welche zur Interaktion mit der Reddit API [praw](https://praw.readthedocs.io/en/latest/#) und zum Abspeichern der Daten eingesetzt wurde.

Der Ordner [raw_data](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/tree/main/raw_data) enthält jegliche generierten JSON-Dateien mit den Rohdaten im Originalzustand.

Im Ordner [dataset](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/tree/main/dataset) befindet sich datapoints_complete.csv, dies sind die Datenpunkte, die für die Auswertung im praktischen Teil meiner vorwissenschaftlichen Arbeit verwendet wurden. Sie wurden in dem Subreddit r/memes erhoben, der Datensatz ist 94949 Reihen lang und enthält Datenpunkte gehörig zu 6330 Posts.

Das Skript [ggplotter.py](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/blob/main/plotter/ggplotter.py) wurde für alle Visualisierungen benutzt. Es verwendet die Library [plotnine](https://plotnine.readthedocs.io/en/stable/) zum Rendern der Plots, welche auf matplotlib basiert und ein Port der Library ggplot2 für die Programmiersprache R ist.

Der [plots](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/tree/main/plotter/plots)-Ordner enthält sowohl alle in der Arbeit verwendeten, als auch experimentelle andere Visualisierungen der Daten. Ausschließlich jene, die in der Arbeit vorkommen, sind jedoch als vollständig zu betrachten.

[fonts](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/tree/main/fonts) enthält die in Fließtext und Visualisierungen der Arbeit verwendete Schriftart Atkinson Hyperlegible, sie ist kostenlos unter einer Lizenz verfügbar, die die Verwendung, weitere Verbreitung, Modifikation und kommerzielle Verwendung erlaubt (die genaue Lizenz ist [hier](https://www.brailleinstitute.org/wp-content/uploads/2020/11/Atkinson-Hyperlegible-Font-License-2020-1104.pdf) abrufbar).

Alle Versuche, die in der Arbeit als Beweise aufgeführt werden, sind in [tests](https://github.com/itsMik4n/Reddit-Frontpage-Data-Collection/tree/main/tests) zu finden.
