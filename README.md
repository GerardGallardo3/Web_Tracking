# Web Tracking

Hem estat implementant un codi en Python a partir del qual hem estat capaços de realitzar un Web Tracker que presenta les següents funcionalitats:

-	Trackejar les diferents websites a les que un usuari s’ha connectat i obtenir així els llocs web que actuen com a First-Party, és a dir, aquells pels que l’usuari ha estat navegant.

-	Obtenir els llocs web que actuen com a Third-Party, els quals també estan obtenint les cookies de l’usuari tot i que aquest no hagi estat connectat en cap moment, és a dir, aquells llocs web que reben les cookies (informació de l’usuari) que l’usuari ha acceptat a les principals webs que ha anat visitant en el moment de l’acceptació de les First-Party cookies.

-	Analitzar aquells llocs web que comparteixen la informació obtinguda a partir de l’acceptació de les cookies per tal de poder detectar els possibles vincles entre aquests tot aplicant Cookie Syncing (un dels principals usos del Web Tracking que hem estat analitzant en profunditat prèviament), és a dir, detectant així aquells vincles entre llocs web que comparteixen la informació que tenen de l’usuari per tal de poder adquirir nova informació de l’usuari a partir de la posada en comú de la informació de l’usuari que totes dues parts han recollit prèviament.

Així doncs, un cop recollida tota aquesta informació, hem creat una nova base de dades on hem recollit tota aquesta informació. Cal esmentar que aquesta base de dades ha estat creada exclusivament a partir de les dades que hem generat a partir de l’execució del codi del Web Tracker mencionat anteriorment.

Finalment, a partir d’aquesta nova base de dades, hem aconseguit transportar totes aquestes dades cap a la plataforma de visualització de dades de Power BI per tal de poder generar un graf on mostrar de manera molt més representativa aquests resultats obtinguts.
