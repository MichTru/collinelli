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
{robots}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="it_IT">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400..900;1,700..900&display=swap">
<link rel="stylesheet" href="assets/style.css?v={v}">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:image" content="assets/img/og.jpg">
{extra}
</head>
<body data-page="{page}">
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
  <video id="hero-video" muted loop playsinline preload="metadata" aria-hidden="true">
    <source src="assets/video/hero-drone.mp4" type="video/mp4">
  </video>
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

<section class="band sunk" id="servizi"><div class="wrap split">
  <div>
    <h2>Officina per tutte le marche.</h2>
    <p class="muted" style="margin-top:14px">In Via Celletta 8/E. Preventivi chiari concordati prima del lavoro, manutenzioni spesso pronte in giornata e auto sostitutiva quando serve.</p>
    <p style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn acc" href="officina.html#prenota">Prenota in officina</a><a class="btn" href="tel:+39054562254">0545 62254</a></p>
  </div>
  <ul class="list">{servizi_html}</ul>
</div></section>

<section class="band" id="marchi"><div class="wrap">
  <div class="head mq-head"><h2>I marchi che trattiamo</h2><button class="mq-btn" id="mq-btn" type="button" aria-label="Ferma lo scorrimento dei marchi"></button></div>
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
    title="Chi siamo, dal 1973 | Collinelli Auto",
    desc="La storia di Collinelli Auto: officina dal 1973, vendita di usato garantito dal 1997, a Bagnacavallo.",
    page="chi-siamo", extra="", body="""
<section class="intro"><div class="wrap split" style="align-items:end">
  <h1 class="big">Una famiglia di meccanici che vende auto.</h1>
  <p class="lead-text">Siamo un'azienda piccola per scelta: due sedi a Bagnacavallo, cinque persone e clienti che tornano da noi per la prossima auto e per il tagliando.</p>
</div></section>

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
  <div class="head mq-head"><h2>I marchi che trattiamo</h2><button class="mq-btn" id="mq-btn" type="button" aria-label="Ferma lo scorrimento dei marchi"></button></div>
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
VERSION = "202611271450"  # cambia a ogni pubblicazione per forzare l'aggiornamento nei browser
for name, p in PAGES.items():
    p.setdefault("v", VERSION)
    p["robots"] = '<meta name="robots" content="noindex">' if ANTEPRIMA or name == "privacy" else f'<link rel="canonical" href="{SITO}{"" if name == "index" else name + ".html"}">' 
    Path(f"{'index' if name == 'index' else name}.html").write_text(HEAD.format(**p), encoding="utf-8")
Path("robots.txt").write_text("User-agent: *\n" + ("Disallow: /\n" if ANTEPRIMA else f"Allow: /\nSitemap: {SITO}sitemap.xml\n"), encoding="utf-8")
urls = [SITO] + [f"{SITO}{n}.html" for n in ("auto", "officina", "chi-siamo", "contatti")]
Path("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
print("ok", len(PAGES))
