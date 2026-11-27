"""Genera le pagine HTML del sito Collinelli Auto da un'unica testata comune."""
from pathlib import Path

HEAD = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#111112">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="it_IT">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='9' fill='%23ffc400'/%3E%3Ctext x='20' y='29' font-family='Arial' font-weight='900' font-size='26' text-anchor='middle' fill='%23111112'%3EC%3C/text%3E%3C/svg%3E">
{extra}
</head>
<body data-page="{page}">
<div id="top"></div>
<main id="main">
{body}
</main>
<div id="foot"></div>
<script src="data/auto.js"></script>
<script src="assets/app.js"></script>
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
    title="Collinelli Auto – Auto usate garantite e officina a Bagnacavallo",
    desc="Auto usate selezionate, controllate in officina e garantite 12 mesi. Vendita e assistenza a Bagnacavallo (RA) dal 1973.",
    page="home", extra=LD, body=f"""
<section class="hero">
  <video id="hero-video" muted loop playsinline preload="metadata" aria-hidden="true">
    <source src="assets/video/hero-drone.mp4" type="video/mp4">
  </video>
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
    <p class="big">Una famiglia di meccanici che vende auto.</p>
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

<section class="band sunk" id="servizi"><div class="wrap split">
  <div>
    <h2>Officina per tutte le marche.</h2>
    <p class="muted" style="margin-top:14px">In Via Celletta 8/E. Preventivi chiari concordati prima del lavoro, manutenzioni spesso pronte in giornata e auto sostitutiva quando serve.</p>
    <p style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn acc" href="officina.html#prenota">Prenota in officina</a><a class="btn" href="tel:+39054562254">0545 62254</a></p>
  </div>
  <ul class="list">{servizi_html}</ul>
</div></section>

<section class="band" id="marchi"><div class="wrap">
  <div class="head"><h2>I marchi che trattiamo</h2><p class="muted">Usato di tutte le principali case. Se il modello che cerchi non c'è, lo troviamo anche con l'importazione parallela.</p></div>
  <div class="brands" id="brands"></div>
</div></section>

<section class="band sunk"><div class="wrap">
  <div class="head"><h2>Vieni a trovarci</h2><a class="more" href="contatti.html">Contatti e orari</a></div>
  <div class="places" id="home-places"></div>
</div></section>
"""),

"auto": dict(
    title="Auto usate in vendita – Collinelli Auto Bagnacavallo",
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
    title="Scheda auto – Collinelli Auto", desc="Foto, caratteristiche, dotazioni e prezzo dell'auto. Garanzia 12 mesi.",
    page="scheda", extra="", body=""),

"officina": dict(
    title="Officina a Bagnacavallo – Collinelli Auto",
    desc="Officina per auto di tutte le marche a Bagnacavallo: tagliandi, diagnosi, climatizzatori, cambi automatici, revisioni, auto sostitutiva.",
    page="officina", extra="", body=f"""
<div class="wrap pagehead"><h1>Officina per tutte le marche</h1><p class="muted">Dal 1973 ripariamo auto a Bagnacavallo. Meccanica, elettronica e diagnosi con personale che si aggiorna sulle nuove tecnologie.</p></div>
<section class="band"><div class="wrap split">
  <div>
    <h2 style="font-size:28px;margin-bottom:18px">Cosa facciamo</h2>
    <ul class="list">{servizi_html}</ul>
  </div>
  <div style="display:grid;gap:22px">
    <div class="guarantee"><div><b>Prezzi concordati prima</b><br><span class="muted">Ti diamo il preventivo e lavoriamo solo dopo il tuo ok.</span></div></div>
    <div class="guarantee"><div><b>Spesso pronta in giornata</b><br><span class="muted">Le manutenzioni ordinarie si chiudono quasi sempre in giornata.</span></div></div>
    <div class="guarantee"><div><b>Sconto per chi ha comprato da noi</b><br><span class="muted">Se la tua auto viene dal nostro showroom, la manutenzione costa meno.</span></div></div>
    <div id="place-officina"></div>
  </div>
</div></section>
<section class="band sunk" id="prenota"><div class="wrap split">
  <div><h2>Prenota un intervento</h2><p class="muted" style="margin-top:14px">Lasciaci auto, lavoro e giorno che preferisci: ti richiamiamo per confermare l'appuntamento.</p></div>
  <div id="form-officina"></div>
</div></section>
"""),

"chi-siamo": dict(
    title="Chi siamo – Collinelli Auto dal 1973",
    desc="La storia di Collinelli Auto: officina dal 1973, vendita di usato garantito dal 1997, a Bagnacavallo.",
    page="chi-siamo", extra="", body="""
<div class="wrap pagehead"><h1>Una famiglia di meccanici che vende auto.</h1><p class="muted">Siamo un'azienda piccola di proposito: cinque persone, due sedi a Bagnacavallo, clienti che tornano.</p></div>
<section class="band"><div class="wrap">
  <div class="years">
    <div><b>1973</b><p>Gilberto Collinelli apre la sua officina come artigiano autoriparatore.</p></div>
    <div><b>Alfa Romeo</b><p>Per quasi trent'anni l'officina lavora a fianco del marchio, fino ai primi anni 2000.</p></div>
    <div><b>1997</b><p>Entra in azienda il figlio Marco e nasce la vendita di auto usate in Via Chiusa 53/F.</p></div>
    <div><b>Oggi</b><p>Vendita e officina insieme: le occasioni Collinelli sono controllate e garantite 12 mesi.</p></div>
  </div>
</div></section>
<section class="band yellow"><div class="wrap split">
  <h2 style="font-size:clamp(30px,4vw,48px)">Come lavoriamo</h2>
  <ul class="list" style="border-color:var(--on-acc)">
    <li style="border-color:var(--on-acc)"><b>Rapporto diretto</b><span>Parli con chi ha controllato l'auto, non con un call center.</span></li>
    <li style="border-color:var(--on-acc)"><b>Trasparenza</b><span>Prezzi chiari e storia del veicolo spiegata prima della firma.</span></li>
    <li style="border-color:var(--on-acc)"><b>Dopo la vendita</b><span>L'assistenza continua nella nostra officina, a pochi minuti dallo showroom.</span></li>
    <li style="border-color:var(--on-acc)"><b>Auto su richiesta</b><span>Con l'importazione parallela troviamo anche il modello che non abbiamo in piazzale.</span></li>
  </ul>
</div></section>
<section class="band"><div class="wrap">
  <div class="head"><h2>Le marche che trattiamo di più</h2></div>
  <p class="muted" style="font-size:19px;max-width:62ch">Alfa Romeo, Audi, BMW, Fiat, Ford, Kia, Lancia, Mercedes-Benz, Mini, Opel, Peugeot, Renault, Volkswagen.</p>
  <p style="margin-top:24px"><a class="btn acc" href="auto.html">Guarda le auto in vendita</a></p>
</div></section>
"""),

"contatti": dict(
    title="Contatti e orari – Collinelli Auto Bagnacavallo",
    desc="Showroom in Via Chiusa 53/F e officina in Via Celletta 8/E a Bagnacavallo (RA). Telefono, email, orari e indicazioni.",
    page="contatti", extra=LD, body="""
<div class="wrap pagehead"><h1>Contatti</h1><p class="muted">Due sedi a Bagnacavallo, a pochi minuti l'una dall'altra.</p></div>
<section class="band" style="padding-top:28px"><div class="wrap">
  <div class="places" id="places"></div>
</div></section>
<section class="band sunk"><div class="wrap split">
  <div><h2>Scrivici</h2><p class="muted" style="margin-top:14px">Per un'auto in vendita, una permuta, un finanziamento o un modello da cercare. Ti rispondiamo entro un giorno lavorativo.</p>
    <iframe class="map" style="margin-top:28px" title="Mappa dello showroom Collinelli Auto" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=44.411867,11.979302&z=15&output=embed"></iframe>
  </div>
  <div id="form-contatti"></div>
</div></section>
"""),

"privacy": dict(
    title="Privacy e cookie – Collinelli Auto", desc="Informativa privacy e cookie di Collinelli Auto S.r.l.",
    page="privacy", extra="", body="""
<div class="wrap pagehead" style="padding-bottom:80px"><h1>Privacy e cookie</h1>
<p class="muted">Il testo dell'informativa privacy e cookie va fornito dall'azienda o dal suo consulente prima della pubblicazione del sito.</p></div>
"""),
}

for name, p in PAGES.items():
    Path(f"{'index' if name == 'index' else name}.html").write_text(HEAD.format(**p), encoding="utf-8")
print("ok", len(PAGES))
