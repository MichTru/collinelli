"""Genera le pagine HTML del sito Collinelli Auto da un'unica testata comune."""
from pathlib import Path
import re

HEAD = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#111112">
{robots}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="it_IT">
{preload}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400..900;1,700..900&display=swap">
<link rel="stylesheet" href="assets/style.css?v={v}">
{intro_js}
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:image" content="{base}assets/img/og.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
{extra}
</head>
<body data-page="{page}">
{intro_html}
<div id="top"></div>
<main id="main">
{body}
</main>
<div id="foot"></div>
<script src="data/auto.js?v={v}"></script>
<script src="assets/app.js?v={v}"></script>
</body>
</html>
"""

LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"AutoDealer","name":"Collinelli Auto S.r.l.","foundingDate":"1973",
"address":{"@type":"PostalAddress","streetAddress":"Via Chiusa 53/F","postalCode":"48012","addressLocality":"Bagnacavallo","addressRegion":"RA","addressCountry":"IT"},
"telephone":"+39 0545 934418","email":"info@collinelliauto.com","geo":{"@type":"GeoCoordinates","latitude":44.411867,"longitude":11.979302},
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"12:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"15:00","closes":"19:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"12:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"15:00","closes":"18:00"}],
"department":{"@type":"AutoRepair","name":"Collinelli Auto, officina","telephone":"+39 0545 62254","address":{"@type":"PostalAddress","streetAddress":"Via Celletta 8/E","postalCode":"48012","addressLocality":"Bagnacavallo","addressCountry":"IT"}}}
</script>"""

INTRO_SVG = '<div class="intro-ov" aria-hidden="true"><div class="intro-bg"></div><svg class="intro-c" viewBox="0 0 700 710"><defs><mask id="intro-m" maskUnits="userSpaceOnUse" x="0" y="0" width="700" height="710"><path d="M473 222 L460 197 L422 134 L418 129 L407 123" stroke-width="48.1" style="--l:127.2;--d:150ms;--t:60ms;--e:cubic-bezier(.5,0,1,1)"/><path d="M407 123 L403 119 L397 108 L373 84 L340 58 L325 49 L295 36 L283 32 L250 25 L229 24 L196 26 L175 29 L157 34 L145 38 L112 54 L88 70 L76 80 L59 98 L48 113 L39 128 L33 146 L30 161 L27 188 L32 215 L36 227 L47 248 L62 269 L83 290 L98 301 L110 309 L131 319 L161 328 L182 331 L187 334 L191 338" stroke-width="76.1" style="--l:746.6;--d:210ms;--t:361ms;--e:linear"/><path d="M195 339 L224 325 L230 324" stroke-width="78.1" style="--l:44.4;--d:571ms;--t:60ms;--e:linear"/><path d="M230 324 L236 328 L248 329 L317 323 L341 319 L377 312 L437 296 L476 282 L503 271 L548 249 L575 232 L602 213 L632 185 L648 167 L660 149 L668 134 L671 125 L675 101 L673 86 L671 77 L663 65 L654 57 L648 54 L639 51 L627 49 L606 49 L594 50 L561 58 L510 76 L474 92 L407 126" stroke-width="73.2" style="--l:856.4;--d:631ms;--t:414ms;--e:linear"/><path d="M407 126 L356 166 L329 189 L284 233 L259 260 L241 284 L238 290 L229 320" stroke-width="72.6" style="--l:274.3;--d:1045ms;--t:131ms;--e:linear"/><path d="M193 342 L185 384 L169 426 L163 453 L160 471 L159 495 L164 531 L167 546 L174 564 L182 579 L194 594 L209 607 L224 616 L245 623 L268 623 L273 620" stroke-width="83.5" style="--l:359.5;--d:1176ms;--t:172ms;--e:linear"/><path d="M273 620 L271 563 L273 545 L281 512 L290 488 L309 452 L327 428 L344 410 L359 397 L383 382 L404 375 L413 372 L425 371 L437 372 L455 377 L464 382 L476 394 L481 403 L486 421 L486 442 L481 469 L475 484 L463 508 L449 529 L436 544 L415 564 L397 578 L379 590 L358 601 L328 613 L298 620 L281 622 L276 625" stroke-width="49.4" style="--l:734.8;--d:1348ms;--t:355ms;--e:linear"/><path d="M276 625 L278 643 L287 682 L281 702" stroke-width="40.5" style="--l:85.5;--d:1703ms;--t:60ms;--e:cubic-bezier(0,0,.4,1)"/></mask></defs><path class="c-shape" fill="#f2c215" fill-rule="evenodd" mask="url(#intro-m)" d="M659.6,48.1 646.2,42.3 625.6,39.1 596.8,40.4 568.6,45.5 531.4,56.4 498.1,68.6 460.9,84.0 412.2,106.4 385.3,78.2 366.7,62.2 344.9,46.8 316.0,31.4 287.8,21.2 262.2,15.4 234.6,12.8 205.1,14.1 176.3,18.6 145.5,27.6 126.9,35.3 100.0,49.4 80.8,62.2 65.4,75.0 49.4,91.7 32.7,115.4 25.6,129.5 17.9,151.3 12.8,182.7 13.5,203.2 16.0,218.6 22.4,240.4 32.1,261.5 41.0,276.3 53.8,292.9 69.9,309.6 80.8,318.6 98.7,331.4 125.6,345.5 150.0,354.5 159.0,356.4 160.3,357.7 146.8,388.5 135.9,419.9 129.5,444.2 125.0,471.8 125.0,510.9 128.2,530.1 135.9,554.5 145.5,573.7 159.0,592.3 173.1,606.4 189.1,617.9 209.0,627.6 226.3,632.7 246.8,635.3 263.5,634.6 265.4,637.2 276.9,682.7 280.1,692.3 282.7,696.2 286.5,696.2 296.8,690.4 300.0,685.9 291.7,654.5 288.5,635.9 289.1,632.1 315.4,626.3 339.1,618.6 359.0,610.3 383.3,597.4 401.3,585.9 423.7,568.6 449.4,543.6 458.3,532.7 477.6,503.2 487.8,480.8 492.9,464.7 496.2,448.7 497.4,434.6 496.8,417.9 491.7,398.1 481.4,381.4 473.7,373.7 462.2,366.0 451.9,361.5 437.8,358.3 413.5,358.3 386.5,364.7 373.1,369.9 357.1,378.2 333.3,394.9 314.1,413.5 298.7,432.7 285.3,453.8 269.2,489.1 260.9,518.6 256.4,547.4 255.8,580.1 259.6,610.9 255.8,611.5 244.9,608.3 230.1,600.0 218.6,589.7 209.6,578.2 202.6,564.7 196.8,549.4 191.0,519.2 191.0,483.3 193.6,464.7 197.4,448.1 205.8,422.4 213.5,403.2 229.5,367.9 236.5,355.1 240.4,353.2 296.8,344.2 348.7,333.3 397.4,320.5 437.8,307.7 484.0,290.4 531.4,269.2 562.2,253.2 598.7,230.1 626.9,207.1 648.1,185.3 667.3,159.6 680.8,133.3 686.5,110.9 685.9,87.8 682.1,74.4 678.2,66.7 673.7,60.3 665.4,51.9ZM457.7,392.9 467.9,403.8 473.7,417.3 475.6,427.6 475.0,448.7 471.8,463.5 462.2,488.5 453.8,503.8 439.7,524.4 430.8,535.3 411.5,554.5 391.7,570.5 374.4,582.1 350.0,594.9 332.7,601.9 307.1,609.6 287.8,612.8 285.9,609.0 286.5,572.4 290.4,549.4 296.8,525.0 307.1,497.4 318.6,473.7 339.1,442.3 348.1,431.4 369.9,410.3 385.9,398.7 401.9,390.4 422.4,384.6 437.8,384.6 449.4,387.8ZM659.6,80.8 663.5,92.3 663.5,107.7 661.5,116.7 651.9,139.1 639.7,157.7 625.0,175.6 600.6,199.4 575.0,219.2 539.7,241.0 498.1,261.5 467.9,273.7 431.4,285.9 398.1,294.9 355.1,303.2 311.5,308.3 260.9,309.0 256.4,307.7 260.3,300.6 283.3,269.2 300.6,248.7 328.2,219.2 367.3,181.4 413.5,143.6 455.1,212.2 464.7,219.2 467.9,219.9 469.9,218.6 475.0,210.3 476.3,202.6 448.7,155.8 432.7,131.4 434.6,128.2 453.2,117.3 488.5,98.7 530.8,80.1 572.4,66.0 597.4,60.3 610.9,58.3 624.4,58.3 636.5,60.9 642.3,63.5 651.3,69.9ZM322.4,62.2 339.7,73.1 362.8,91.7 389.7,119.2 362.8,137.8 326.3,165.4 276.9,207.7 254.5,229.5 230.8,255.1 209.6,280.8 191.0,306.4 173.7,305.1 153.8,300.6 137.2,294.9 119.9,286.5 101.9,275.0 88.5,264.1 74.4,250.0 64.1,237.2 50.6,213.5 44.9,197.4 41.7,177.6 42.9,155.1 49.4,134.0 61.5,112.2 73.1,98.1 82.7,88.5 100.6,73.7 123.1,59.6 153.2,46.2 181.4,38.5 200.0,35.9 236.5,35.9 269.2,41.0 298.7,50.6Z"/></svg></div>'
INTRO_JS = '<script>try{if(!sessionStorage.getItem("intro")&&!matchMedia("(prefers-reduced-motion:reduce)").matches)document.documentElement.classList.add("intro")}catch(e){}</script>'

SERVIZI = [
    ("Tagliandi", "Manutenzione programmata secondo il libretto della casa, senza perdere la garanzia del costruttore."),
    ("Riparazioni meccaniche", "Auto di tutte le marche e veicoli commerciali leggeri."),
    ("Diagnosi elettrica ed elettronica", "Strumenti aggiornati per leggere centraline, spie e sensori."),
    ("Climatizzatori", "Controllo, ricarica e ricerca perdite dell'impianto."),
    ("Cambi automatici", "Lavaggio e sostituzione dell'olio del cambio automatico."),
    ("Revisioni", "Ti seguiamo per la revisione periodica del veicolo."),
    ("Auto sostitutiva", "Per non restare a piedi mentre lavoriamo sulla tua."),
]
servizi_html = "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in SERVIZI)

PAGES = {
"index": dict(
    title="Auto usate garantite a Bagnacavallo | Collinelli Auto",
    desc="Auto usate selezionate e garantite 12 mesi, officina per tutte le marche. Collinelli Auto a Bagnacavallo (RA), tra Lugo e Ravenna, dal 1973.",
    page="home", extra=LD, body=f"""
<section class="hero">
  <img class="hero-img" src="assets/img/sede-showroom.jpg" alt="Lo showroom Collinelli Auto a Bagnacavallo" width="1672" height="941" fetchpriority="high">
  <video id="hero-video" muted loop playsinline preload="metadata" aria-hidden="true"></video>
  <button class="pause" id="vpause" type="button" aria-label="Metti in pausa il video" hidden></button>
  <div class="wrap">
    <h1>Auto usate garantite, dal 1973.</h1>
    <p class="lead">Vendita e officina a Bagnacavallo: ogni auto passa dai nostri meccanici e parte con 12 mesi di garanzia.</p>
    <p style="margin-top:28px"><a class="btn acc" href="#auto" style="min-height:54px;padding:0 28px;font-size:16px">Guarda le auto in vendita</a></p>
  </div>
</section>

<section class="band sunk" style="padding-block:clamp(32px,4vw,52px)"><div class="wrap reviews">
  <div class="score"><b>4,7</b><span class="stars" aria-hidden="true">★★★★★</span><p class="muted"><a href="https://www.autoscout24.it/concessionari/collinelli-auto-srl/recensioni" rel="noopener">44 recensioni su AutoScout24</a></p></div>
  <div class="quotes">
    <blockquote>Molto professionale, disponibile, cortese.<cite>Luca, cliente</cite></blockquote>
    <blockquote>Venditore che raccomando, cordiale e simpatico.<cite>Cliente su AutoScout24</cite></blockquote>
  </div>
</div></section>

<section class="band yellow" id="chi-siamo"><div class="wrap">
  <div class="split" style="align-items:end;margin-bottom:clamp(32px,4vw,52px)">
    <h2 class="big">Una famiglia di meccanici che vende auto.</h2>
    <div>
      <p style="font-size:18px">Gilberto Collinelli apre l'officina nel 1973 e per quasi trent'anni lavora con Alfa Romeo. Nel 1997 entra il figlio Marco e nasce la vendita di usato in Via Chiusa. Oggi siamo cinque persone, due sedi, e clienti che tornano.</p>
      <p style="margin-top:20px"><a class="btn dark" href="chi-siamo.html">La nostra storia</a></p>
    </div>
  </div>
  <div class="promises">
    <div><h3>Garanzia 12 mesi</h3><p>Su ogni auto, con attestazione di conformità consegnata insieme alle chiavi.</p></div>
    <div><h3>Controllata in officina</h3><p>Prima della vendita ogni auto viene verificata dai nostri meccanici, non da terzi.</p></div>
    <div><h3>Assistenza dopo l'acquisto</h3><p>Chi compra da noi ha uno sconto sulle manutenzioni nella nostra officina.</p></div>
  </div>
</div></section>

<section class="band" id="auto"><div class="wrap">
  <div class="head"><h2>Auto in vendita</h2><a class="more" href="auto.html">Vedi tutte le auto</a></div>
  <form class="search" action="auto.html" role="search" aria-label="Cerca un'auto" style="margin:0 0 28px">
    <label class="f"><span class="skip">Marca</span><select name="marca" id="s-marca"></select></label>
    <label class="f"><span class="skip">Carrozzeria</span><select name="carrozzeria" id="s-carrozzeria"></select></label>
    <label class="f"><span class="skip">Prezzo massimo</span><select name="max">
      <option value="">Qualsiasi prezzo</option><option value="10000">Fino a 10.000 €</option><option value="12000">Fino a 12.000 €</option><option value="15000">Fino a 15.000 €</option><option value="20000">Fino a 20.000 €</option><option value="25000">Fino a 25.000 €</option></select></label>
    <button class="btn acc" type="submit">Cerca</button>
  </form>
  <div class="row" id="recent"></div>
  <div class="chips" style="margin-top:28px">
    <a href="auto.html?neopatentati=1">Per neopatentati</a>
    <a href="auto.html?max=12000">Fino a 12.000 €</a>
    <a href="auto.html?cambio=Automatico">Cambio automatico</a>
    <a href="auto.html?carburante=Ibrida">Ibride</a>
    <a href="auto.html?km=30000">Pochi chilometri</a>
    <a href="auto.html?carrozzeria=Furgone">Furgoni da lavoro</a>
  </div>
</div></section>

<section class="band" id="marchi"><div class="wrap">
  <div class="head"><h2>I marchi che trattiamo</h2></div>
</div>
<div class="marquee" id="marquee"></div>
</section>

<section class="band sunk"><div class="wrap">
  <div class="head"><h2>Vieni a trovarci</h2><a class="more" href="contatti.html">Contatti e orari</a></div>
  <div class="places" id="home-places"></div>
</div></section>
"""),

"auto": dict(
    title="Auto usate in vendita a Bagnacavallo | Collinelli Auto",
    desc="Tutte le auto usate in vendita da Collinelli Auto: prezzi, chilometri, foto e dotazioni. Garanzia 12 mesi.",
    page="auto", extra="", body="""
<div class="wrap pagehead"><h1>Auto in vendita</h1><p class="muted">Usato selezionato, controllato nella nostra officina e garantito 12 mesi.</p></div>
<div class="wrap catalog" style="padding-bottom:70px">
  <form class="filters" id="filters" aria-label="Filtri"></form>
  <div>
    <div class="bar">
      <button class="btn openf" type="button" id="openf">Filtra</button>
      <label class="f" style="margin-left:auto"><span class="skip">Ordina per</span><select id="sort">
        <option value="recenti">Ultimi arrivi</option><option value="prezzo-su">Prezzo più basso</option><option value="prezzo-giu">Prezzo più alto</option><option value="km">Meno chilometri</option><option value="anno">Più recenti</option></select></label>
    </div>
    <p class="npinfo" id="npinfo" hidden>Per tre anni dalla patente B puoi guidare auto fino a 105 kW di potenza e con un rapporto potenza/tara fino a 75 kW/t. Su ogni auto segnata controlliamo i due valori sul libretto.</p>
    <div class="cars" id="list" aria-live="polite"></div>
  </div>
</div>
"""),

"scheda": dict(
    title="Auto usata | Collinelli Auto", desc="Foto, caratteristiche, dotazioni e prezzo dell'auto. Garanzia 12 mesi.",
    page="scheda", extra="", body=""),

"officina": dict(
    title="Officina auto a Bagnacavallo | Collinelli Auto",
    desc="Officina per auto di tutte le marche a Bagnacavallo: tagliandi, diagnosi, climatizzatori, cambi automatici, revisioni, auto sostitutiva.",
    page="officina", extra="", body=f"""
<section class="intro"><div class="wrap off-top">
  <div>
    <h1>Officina per tutte le marche</h1>
    <p class="lead-text" style="margin-top:14px">Dal 1973 ripariamo auto a Bagnacavallo. Preventivo chiaro prima di iniziare, lavori spesso pronti in giornata.</p>
    <div class="acts" style="margin-top:22px"><a class="btn acc" href="#prenota">Prenota un intervento</a><a class="btn" href="tel:+39054562254">Chiama 0545 62254</a></div>
  </div>
  <aside class="off-card">
    <h2>Officina e assistenza</h2>
    <address>Via Celletta 8/E<br>48012 Bagnacavallo (RA)</address>
    <p><a href="tel:+39054562254">0545 62254</a><br><a href="mailto:assistenza@collinelliauto.com">assistenza@collinelliauto.com</a></p>
    <a class="more" href="https://www.google.com/maps/search/?api=1&query=Via+Celletta+8+Bagnacavallo" rel="noopener">Indicazioni stradali</a>
  </aside>
</div></section>

<section class="band"><div class="wrap">
  <h2 style="margin-bottom:18px">Cosa facciamo</h2>
  <ul class="svc-list">{servizi_html}</ul>
</div></section>

<section class="band sunk"><div class="wrap">
  <h2 style="margin-bottom:18px">Perché portarla da noi</h2>
  <div class="why">
    <div><h3>Prezzi concordati prima</h3><p class="muted">Ti diamo il preventivo e lavoriamo solo dopo il tuo ok.</p></div>
    <div><h3>Spesso pronta in giornata</h3><p class="muted">Le manutenzioni ordinarie si chiudono quasi sempre in giornata, con auto sostitutiva se serve.</p></div>
    <div><h3>Sconto se l'hai comprata da noi</h3><p class="muted">Per le auto vendute dal nostro showroom la manutenzione costa meno.</p></div>
  </div>
</div></section>

<section class="band" id="prenota"><div class="wrap">
  <h2>Prenota un intervento</h2>
  <p class="muted" style="margin:10px 0 20px;max-width:60ch">Lasciaci auto, lavoro e giorno che preferisci: ti richiamiamo per confermare l'appuntamento.</p>
  <div id="form-officina" class="form-card"></div>
</div></section>
"""),

"chi-siamo": dict(
    title="Chi siamo, dal 1973 | Collinelli Auto",
    desc="La storia di Collinelli Auto: officina dal 1973, vendita di usato garantito dal 1997, a Bagnacavallo.",
    page="chi-siamo", extra="", body="""
<section class="intro"><div class="wrap split" style="align-items:end">
  <h1 class="big">Una famiglia di meccanici che vende auto.</h1>
  <p class="lead-text">Siamo un'azienda piccola per scelta: due sedi a Bagnacavallo, cinque persone e clienti che tornano da noi per la prossima auto e per il tagliando.</p>
</div></section>

<figure class="photo-band" style="margin-block:8px"><img src="assets/img/sede-showroom.jpg" alt="Lo showroom Collinelli Auto in Via Chiusa 53/F a Bagnacavallo, visto dall'alto" width="1672" height="941" loading="lazy"></figure>

<section class="band"><div class="wrap split">
  <div class="sticky-col">
    <h2>Dal 1973 a oggi</h2>
    <p class="muted" style="margin-top:14px;max-width:40ch">Prima l'officina, poi la vendita. È per questo che ogni auto che vendiamo passa dalle mani dei nostri meccanici.</p>
  </div>
  <ol class="timeline">
    <li><b>1973</b><h3>Nasce l'officina</h3><p>Gilberto Collinelli, oggi presidente dell'azienda, apre la sua attività di artigiano autoriparatore.</p></li>
    <li><b>Anni '70 – 2000</b><h3>Accanto ad Alfa Romeo</h3><p>Per quasi trent'anni l'officina lavora con il marchio Alfa Romeo, fino ai primi anni 2000.</p></li>
    <li><b>1997</b><h3>Arriva Marco e nasce la vendita</h3><p>Il figlio Marco entra in azienda e apre lo showroom di usato in Via Chiusa 53/F, accanto all'officina di sempre.</p></li>
    <li><b>Oggi</b><h3>Le occasioni Collinelli</h3><p>Auto scelte una per una, controllate in officina, garantite 12 mesi e consegnate con l'attestazione di conformità.</p></li>
  </ol>
</div></section>

<section class="band yellow"><div class="wrap">
  <h2 style="margin-bottom:clamp(24px,3vw,40px)">Come lavoriamo</h2>
  <div class="values">
    <div><h3>Rapporto diretto</h3><p>Parli con chi ha controllato l'auto, non con un call center.</p></div>
    <div><h3>Prezzi chiari</h3><p>Storia del veicolo e costi spiegati prima della firma, senza sorprese.</p></div>
    <div><h3>Dopo la vendita</h3><p>L'assistenza continua nella nostra officina, con uno sconto sulle manutenzioni.</p></div>
    <div><h3>Auto su richiesta</h3><p>Con l'importazione parallela troviamo anche il modello che non abbiamo in piazzale.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="head"><h2>Due sedi, a pochi minuti l'una dall'altra</h2></div>
  <div class="places" id="about-places"></div>
</div></section>

<section class="band sunk"><div class="wrap reviews">
  <div class="score"><b>4,7</b><span class="stars" aria-hidden="true">★★★★★</span><p class="muted"><a href="https://www.autoscout24.it/concessionari/collinelli-auto-srl/recensioni" rel="noopener">44 recensioni su AutoScout24</a></p></div>
  <div class="quotes">
    <blockquote>Molto professionale, disponibile, cortese.<cite>Luca, cliente</cite></blockquote>
    <blockquote>Venditore che raccomando, cordiale e simpatico.<cite>Cliente su AutoScout24</cite></blockquote>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="head"><h2>I marchi che trattiamo</h2></div>
</div>
<div class="marquee" id="marquee"></div>
<div class="wrap" style="margin-top:36px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn acc" href="auto.html">Guarda le auto in vendita</a><a class="btn" href="contatti.html">Passa a trovarci</a></div>
</section>
"""),

"contatti": dict(
    title="Contatti e orari | Collinelli Auto Bagnacavallo",
    desc="Showroom in Via Chiusa 53/F e officina in Via Celletta 8/E a Bagnacavallo (RA). Telefono, email, orari e indicazioni.",
    page="contatti", extra=LD, body="""
<section class="intro"><div class="wrap">
  <h1>Contatti</h1>
  <p class="status" id="status"></p>
  <div class="quick" id="quick"></div>
</div></section>

<section class="band" style="padding-top:12px"><div class="wrap">
  <div class="sites" id="sites"></div>
</div></section>

<section class="band sunk" id="scrivi"><div class="wrap split">
  <div>
    <h2>Scrivici</h2>
    <p class="muted" style="margin-top:14px;max-width:44ch">Per un'auto in vendita, una permuta, un finanziamento o un modello da cercare. Ti ricontattiamo noi.</p>
    <ul class="helps">
      <li>Finanziamenti</li><li>Valutazione dell'usato in permuta</li><li>Ricerca auto su richiesta</li><li>Trattative anche per telefono</li>
    </ul>
  </div>
  <div id="form-contatti"></div>
</div></section>
"""),

"privacy": dict(
    title="Privacy e cookie | Collinelli Auto", desc="Informativa privacy e cookie di Collinelli Auto S.r.l.",
    page="privacy", extra="", body="""
<div class="wrap pagehead" style="padding-bottom:80px"><h1>Privacy e cookie</h1>
<p class="muted">Il testo dell'informativa privacy e cookie va fornito dall'azienda o dal suo consulente prima della pubblicazione del sito.</p></div>
"""),
}

# True finché il sito è un'anteprima (GitHub Pages): evita che Google lo indicizzi come doppione
ANTEPRIMA = True
SITO = "https://www.collinelliauto.it/"
ANTEPRIMA_URL = "https://michtru.github.io/collinelli/"
VERSION = "202611271602"  # cambia a ogni pubblicazione per forzare l'aggiornamento nei browser
for name, p in PAGES.items():
    p.setdefault("v", VERSION)
    p["preload"] = '<link rel="preload" as="image" href="assets/img/sede-showroom.jpg">\n' if name == "index" else ""
    p["base"] = ANTEPRIMA_URL if ANTEPRIMA else SITO
    p["intro_js"] = INTRO_JS if name == "index" else ""
    p["intro_html"] = INTRO_SVG if name == "index" else ""
    p["robots"] = '<meta name="robots" content="noindex">' if ANTEPRIMA or name == "privacy" else f'<link rel="canonical" href="{SITO}{"" if name == "index" else name + ".html"}">' 
    Path(f"{'index' if name == 'index' else name}.html").write_text(HEAD.format(**p), encoding="utf-8")
Path("robots.txt").write_text("User-agent: *\n" + ("Disallow: /\n" if ANTEPRIMA else f"Allow: /\nSitemap: {SITO}sitemap.xml\n"), encoding="utf-8")
ids = re.findall(r'id: "([^"]+)"', Path("data/auto.js").read_text(encoding="utf-8"))
urls = [SITO] + [f"{SITO}{n}.html" for n in ("auto", "officina", "chi-siamo", "contatti")] + [f"{SITO}scheda.html?id={i}" for i in ids]
Path("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
print("ok", len(PAGES))
