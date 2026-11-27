# Collinelli Auto – sito

Sito statico (HTML, CSS, JS senza framework) per Collinelli Auto S.r.l., Bagnacavallo.

## Pagine
- `index.html` home: video col drone, recensioni, chi siamo, auto in vendita, servizi, marchi, sedi
- `auto.html` parco auto con filtri e ordinamento (i filtri restano nell'indirizzo, si possono condividere)
- `scheda.html?id=...` scheda auto: galleria, caratteristiche, dotazioni, richiesta info e prova su strada
- `officina.html`, `chi-siamo.html`, `contatti.html`, `privacy.html`

## Come si modifica
- Testi delle pagine: `build.py`, poi `python3 build.py` rigenera gli HTML
- Testata, piede, orari e contatti: `assets/app.js` (oggetto `AZ`)
- Auto in vendita: `data/auto.js` (temporaneo, verrà sostituito dal pannello admin)
- Video hero a tutto schermo: `assets/video/hero-drone.mp4` orizzontale (H.264, 1920x1080, 10-20 s in loop, senza audio, max 8-10 MB) e, consigliato, `assets/video/hero-drone-verticale.mp4` (1080x1920, max 6 MB) per i telefoni. Se manca la verticale, su telefono si usa l'orizzontale ritagliata al centro; se mancano entrambe si vede la foto dell'ultima auto arrivata.

## Messa online sul dominio vero
In `build.py` impostare `ANTEPRIMA = False` (e `SITO` se il dominio cambia), poi `python3 build.py`:
toglie il `noindex`, aggiunge i canonical e apre `robots.txt` con la sitemap.
Finché resta `True` Google non indicizza l'anteprima su GitHub Pages.

## Prossimo passo: pannello admin
`db/schema.sql` contiene le tabelle Supabase `auto` e `richieste`. In `assets/app.js` basta sostituire `getCars()` con la lettura dal database; i moduli salveranno le richieste in `richieste` invece di aprire l'app di posta.

## Da avere dall'azienda prima di andare online
- Logo vettoriale (SVG) e video col drone: per ora il logo è PNG, ricavato dai file in `brand/`
- Partita IVA e dati societari per il piè di pagina
- Testo privacy e cookie
- Orari dell'officina (quelli in pagina sono dello showroom, da AutoScout24)
- Conferma dei flag "neopatentati" auto per auto sul libretto
- Foto proprie delle sedi e della squadra
