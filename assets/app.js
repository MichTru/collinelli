{
/* ---------- dati azienda ---------- */
const AZ = {
  nome: "Collinelli Auto",
  showroom: { nome: "Showroom e vendita", via: "Via Chiusa 53/F", cap: "48012 Bagnacavallo (RA)", tel: "0545 934418", mail: "info@collinelliauto.com", maps: "https://www.google.com/maps/search/?api=1&query=Collinelli+Auto+Via+Chiusa+53+Bagnacavallo" },
  officina: { nome: "Officina e assistenza", via: "Via Celletta 8/E", cap: "48012 Bagnacavallo (RA)", tel: "0545 62254", mail: "assistenza@collinelliauto.com", maps: "https://www.google.com/maps/search/?api=1&query=Via+Celletta+8+Bagnacavallo" },
  facebook: "https://www.facebook.com/pages/Collinelli-Auto-Srl/609828095705340",
  // orari showroom (fonte: AutoScout24), lunedì = 0
  orari: [
    ["Lunedì", [["9:00", "12:30"], ["15:00", "19:00"]]], ["Martedì", [["9:00", "12:30"], ["15:00", "19:00"]]],
    ["Mercoledì", [["9:00", "12:30"], ["15:00", "19:00"]]], ["Giovedì", [["9:00", "12:30"], ["15:00", "19:00"]]],
    ["Venerdì", [["9:00", "12:30"], ["15:00", "19:00"]]], ["Sabato", [["9:00", "12:30"], ["15:00", "18:00"]]], ["Domenica", []]
  ]
};
const MARCHI = ["Alfa Romeo", "Audi", "BMW", "DR", "Fiat", "Ford", "Kia", "Lancia", "Mercedes-Benz", "Mini", "Nissan", "Opel", "Peugeot", "Renault", "Toyota", "Volkswagen"];
const slug = s => s.toLowerCase().normalize("NFD").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const mins = t => { const [h, m] = t.split(":"); return h * 60 + +m; };
const dayIdx = () => (new Date().getDay() + 6) % 7;
function openStatus() {
  const now = new Date(), d = dayIdx(), m = now.getHours() * 60 + now.getMinutes();
  for (const [a, z] of AZ.orari[d][1]) if (m >= mins(a) && m < mins(z)) return { open: true, text: `Showroom aperto ora, chiude alle ${z}` };
  for (const [a] of AZ.orari[d][1]) if (m < mins(a)) return { open: false, text: `Showroom chiuso ora, riapre oggi alle ${a}` };
  for (let i = 1; i <= 7; i++) {
    const n = (d + i) % 7, s = AZ.orari[n][1];
    if (s.length) return { open: false, text: `Showroom chiuso ora, riapre ${i === 1 ? "domani" : AZ.orari[n][0].toLowerCase()} alle ${s[0][0]}` };
  }
}
const telHref = t => "tel:+39" + t.replace(/\s/g, "");

/* ---------- sorgente dati: oggi il file data/auto.js, domani il database del pannello ---------- */
const getCars = async () => (window.AUTO || []).slice();

/* ---------- utilità ---------- */
const $ = (s, r = document) => r.querySelector(s);
const esc = v => String(v ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const eur = n => new Intl.NumberFormat("it-IT", { style: "currency", currency: "EUR", maximumFractionDigits: 0 }).format(n);
const num = n => new Intl.NumberFormat("it-IT").format(n);
const year = c => +c.immatricolazione.split("/")[1];
const full = p => window.FOTO_BASE + p;
const thumb = p => window.FOTO_BASE + p.replace(/(-scaled)?\.jpg$/i, "-700x450.jpg");
const title = c => `${c.marca} ${c.modello}`;
const priceHtml = c => `${eur(c.prezzo)}${c.iva ? "<small>+ IVA</small>" : ""}`;
const params = () => new URLSearchParams(location.search);
const uniq = (a, k) => [...new Set(a.map(x => x[k]))].sort((x, y) => x.localeCompare(y, "it"));

const ICON = {
  phone: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
  mail: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
  pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
  shield: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>',
  left: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 5-7 7 7 7"/></svg>',
  right: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 5 7 7-7 7"/></svg>',
  pause: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>',
  play: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
  menu: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
};

/* ---------- testata e piede comuni ---------- */
const page = document.body.dataset.page;
const NAV = [["auto.html", "Auto in vendita", "auto"], ["officina.html", "Officina", "officina"], ["chi-siamo.html", "Chi siamo", "chi-siamo"], ["contatti.html", "Contatti", "contatti"]];

$("#top").outerHTML = `
<a class="skip" href="#main">Vai al contenuto</a>
<header class="top"><div class="wrap">
  <a class="logo" href="index.html"><img src="assets/img/logo-giallo.png" alt="Collinelli Auto" width="211" height="46"></a>
  <nav class="nav" id="nav" aria-label="Menu principale">
    ${NAV.map(([h, t, k]) => `<a href="${h}"${(page === k || (page === "scheda" && k === "auto")) ? ' aria-current="page"' : ""}>${t}</a>`).join("")}
  </nav>
  <a class="btn acc call" href="${telHref(AZ.showroom.tel)}">${ICON.phone}${AZ.showroom.tel}</a>
  <button class="burger" id="burger" aria-label="Apri il menu" aria-expanded="false" aria-controls="nav">${ICON.menu}</button>
</div></header>`;

$("#foot").outerHTML = `
<footer class="foot"><div class="wrap">
  <div class="cols">
    <div class="brand"><img src="assets/img/logo-giallo.png" alt="Collinelli Auto" width="202" height="44" loading="lazy"><p>Collinelli Auto S.r.l.<br>Auto usate selezionate, garantite 12 mesi, e officina per tutte le marche a Bagnacavallo.</p></div>
    <div><h2>${AZ.showroom.nome}</h2><ul><li>${AZ.showroom.via}, ${AZ.showroom.cap}</li><li><a href="${telHref(AZ.showroom.tel)}">${AZ.showroom.tel}</a></li><li><a href="mailto:${AZ.showroom.mail}">${AZ.showroom.mail}</a></li></ul></div>
    <div><h2>${AZ.officina.nome}</h2><ul><li>${AZ.officina.via}, ${AZ.officina.cap}</li><li><a href="${telHref(AZ.officina.tel)}">${AZ.officina.tel}</a></li><li><a href="mailto:${AZ.officina.mail}">${AZ.officina.mail}</a></li></ul></div>
    <div><h2>Pagine</h2><ul>${NAV.map(([h, t]) => `<li><a href="${h}">${t}</a></li>`).join("")}<li><a href="${AZ.facebook}" rel="noopener">Facebook</a></li></ul></div>
  </div>
  <div class="legal"><span>© ${new Date().getFullYear()} Collinelli Auto S.r.l.</span><a href="privacy.html">Privacy e cookie</a></div>
</div></footer>
<div class="dock"><a class="btn acc" href="${telHref(AZ.showroom.tel)}">${ICON.phone}Chiama</a><a class="btn" href="${AZ.showroom.maps}" rel="noopener">${ICON.pin}Indicazioni</a></div>`;

$("#burger").addEventListener("click", e => {
  const open = $("#nav").classList.toggle("open");
  e.currentTarget.setAttribute("aria-expanded", open);
});

/* ---------- pezzi riutilizzabili ---------- */
const imgTag = (p, alt, cls = "") => `<img${cls ? ` class="${cls}"` : ""} src="${esc(thumb(p))}" data-full="${esc(full(p))}" alt="${esc(alt)}" loading="lazy" decoding="async">`;
// se manca la miniatura 700x450 carica la foto originale
document.addEventListener("error", e => {
  const i = e.target;
  if (i.tagName === "IMG" && i.dataset.full && i.src !== i.dataset.full) i.src = i.dataset.full;
}, true);

const card = c => `
<a class="car" href="scheda.html?id=${encodeURIComponent(c.id)}">
  <div class="ph">${imgTag(c.foto[0], title(c))}${c.neopatentati ? '<span class="np">Neopatentati</span>' : ""}</div>
  <div class="bd">
    <h3>${esc(title(c))}<span>${esc(c.versione)}</span></h3>
    <div class="specs"><span>${esc(c.immatricolazione)}</span><span>${num(c.km)} km</span><span>${esc(c.carburante)}</span><span>${esc(c.cambio)}</span></div>
    <div class="price">${priceHtml(c)}</div>
  </div>
</a>`;

const hoursTable = () => {
  const d = dayIdx();
  return `<table class="hours"><tbody>${AZ.orari.map(([g, f], i) => `<tr${i === d ? ' class="today"' : ""}><td>${g}${i === d ? " <span>oggi</span>" : ""}</td><td>${f.length ? f.map(([a, z]) => `${a}–${z}`).join(", ") : "Chiuso"}</td></tr>`).join("")}</tbody></table>`;
};

/* nastro dei marchi: logo in assets/img/marchi/<nome>.png, se manca si vede il nome */
// dimensiona ogni logo sulla stessa area visiva, così una scritta lunga e un tondo pesano uguale
window.fitLogo = i => {
  const r = i.naturalWidth / i.naturalHeight;
  let h = Math.sqrt(5000 / r), w = h * r;
  if (w > 168) { w = 168; h = w / r; }
  if (h > 62) { h = 62; w = h * r; }
  i.style.width = Math.round(w) + "px"; i.style.height = Math.round(h) + "px";
  i.classList.add("ok"); i.nextElementSibling?.remove();
};
function marquee(cars) {
  const el = $("#marquee"); if (!el) return;
  const stock = new Set(cars.map(c => c.marca));
  const item = (b, hidden) => {
    const inner = `<img src="assets/img/marchi/${slug(b)}.png" alt="${hidden ? "" : esc(b)}" onload="fitLogo(this)"><span>${esc(b)}</span>`;
    const attrs = hidden ? ' tabindex="-1"' : "";
    return stock.has(b) ? `<a href="auto.html?marca=${encodeURIComponent(b)}"${attrs}>${inner}</a>` : `<div>${inner}</div>`;
  };
  const btn = $("#mq-btn");
  if (btn) {
    btn.innerHTML = ICON.pause;
    btn.onclick = () => {
      const p = el.classList.toggle("paused");
      btn.innerHTML = p ? ICON.play : ICON.pause;
      btn.setAttribute("aria-label", p ? "Fai scorrere i marchi" : "Ferma lo scorrimento dei marchi");
    };
  }
  el.innerHTML = `<div class="track">${MARCHI.map(b => item(b)).join("")}<div class="dup" aria-hidden="true">${MARCHI.map(b => item(b, true)).join("")}</div></div>`;
}

const placeCard = (s, extra = "") => `
<div class="place">
  <h3>${s.nome}</h3>
  <address>${s.via}<br>${s.cap}</address>
  <div class="acts">
    <a class="btn acc" href="${telHref(s.tel)}">${ICON.phone}${s.tel}</a>
    <a class="btn" href="mailto:${s.mail}">${ICON.mail}Scrivi</a>
    <a class="btn" href="${s.maps}" rel="noopener">${ICON.pin}Indicazioni</a>
  </div>
  ${extra}
</div>`;

/* modulo di contatto: compone una mail pronta (sul sito finale verrà salvata nel pannello) */
function contactForm({ to, subject, intro = "", fields = "", body = "" }) {
  const id = "f" + Math.random().toString(36).slice(2, 7);
  setTimeout(() => {
    const f = document.getElementById(id);
    f.addEventListener("submit", e => {
      e.preventDefault();
      const d = Object.fromEntries(new FormData(f));
      if (!d.tel && !d.email) { f.querySelector("[name=tel]").focus(); f.querySelector(".err").hidden = false; return; }
      const lines = Object.entries(d).filter(([, v]) => v).map(([k, v]) => `${k[0].toUpperCase() + k.slice(1)}: ${v}`);
      const dest = d.argomento === "Officina" ? AZ.officina.mail : to;
      location.href = `mailto:${dest}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join("\n"))}`;
      f.querySelector(".sent").hidden = false;
    });
  });
  return `<form class="modal-form" id="${id}" novalidate style="display:grid;gap:14px">
    ${intro}
    <label class="f">Nome e cognome<input name="nome" autocomplete="name" required></label>
    <label class="f">Telefono<input name="tel" type="tel" autocomplete="tel" inputmode="tel"></label>
    <label class="f">Email<input name="email" type="email" autocomplete="email"></label>
    ${fields}
    <label class="f">Messaggio<textarea name="messaggio">${esc(body)}</textarea></label>
    <p class="note err" hidden>Inserisci almeno un telefono o un'email per farti richiamare.</p>
    <button class="btn acc" type="submit">Invia richiesta</button>
    <p class="sent" hidden>Si è aperta la tua app di posta con la richiesta pronta da inviare. Se non si apre, scrivi a ${to}.</p>
  </form>`;
}

function openModal(html) {
  let d = $("#modal");
  if (!d) { d = document.createElement("dialog"); d.id = "modal"; document.body.append(d); d.addEventListener("click", e => { if (e.target === d) d.close(); }); }
  d.innerHTML = `<div class="modal"><button class="x" aria-label="Chiudi">×</button>${html}</div>`;
  d.querySelector(".x").onclick = () => d.close();
  d.showModal();
}

/* ---------- pagine ---------- */
const RENDER = {
  async home() {
    const cars = await getCars();
    const recent = cars.slice().sort((a, b) => b.inserita.localeCompare(a.inserita));
    const lead = recent.find(c => c.evidenza) || recent[0];
    const v = $("#hero-video");
    v.poster = full(lead.foto[0]);
    const still = matchMedia("(prefers-reduced-motion:reduce)").matches;
    const pb = $("#vpause");
    v.addEventListener("playing", () => { pb.hidden = false; });
    pb.onclick = () => {
      if (v.paused) { v.play(); pb.innerHTML = ICON.pause; pb.setAttribute("aria-label", "Metti in pausa il video"); }
      else { v.pause(); pb.innerHTML = ICON.play; pb.setAttribute("aria-label", "Riproduci il video"); }
    };
    pb.innerHTML = ICON.pause;
    if (!still) v.play().catch(() => {});
    const opt = (k, t) => `<option value="">${t}</option>` + uniq(cars, k).map(v => `<option>${esc(v)}</option>`).join("");
    $("#s-marca").innerHTML = opt("marca", "Tutte le marche");
    $("#s-carrozzeria").innerHTML = opt("carrozzeria", "Tutte le carrozzerie");
    $("#recent").innerHTML = recent.slice(0, 8).map(card).join("");
    marquee(cars);
  },

  async auto() {
    const cars = await getCars();
    const f = $("#filters");
    const sel = (k, t) => `<label class="f">${t}<select name="${k}"><option value="">Tutte</option>${uniq(cars, k).map(v => `<option>${esc(v)}</option>`).join("")}</select></label>`;
    const prices = [8000, 10000, 12000, 15000, 18000, 20000, 25000, 30000];
    const kms = [20000, 40000, 60000, 80000, 100000];
    const years = [...new Set(cars.map(year))].sort((a, b) => b - a);
    f.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center"><h2>Filtra</h2><button type="button" class="btn openf" id="closef">Chiudi</button></div>
      ${sel("marca", "Marca")}${sel("carrozzeria", "Carrozzeria")}${sel("carburante", "Alimentazione")}${sel("cambio", "Cambio")}
      <label class="f">Prezzo fino a<select name="max"><option value="">Qualsiasi</option>${prices.map(p => `<option value="${p}">${eur(p)}</option>`).join("")}</select></label>
      <label class="f">Chilometri fino a<select name="km"><option value="">Qualsiasi</option>${kms.map(k => `<option value="${k}">${num(k)} km</option>`).join("")}</select></label>
      <label class="f">Immatricolata dal<select name="anno"><option value="">Qualsiasi</option>${years.map(y => `<option>${y}</option>`).join("")}</select></label>
      <label class="check"><input type="checkbox" name="neopatentati" value="1">Adatte ai neopatentati</label>
      <button type="button" class="reset" id="reset">Azzera i filtri</button>
      <button type="button" class="btn acc openf" id="showf">Mostra le auto</button>`;
    const p = params();
    for (const el of f.elements) {
      if (!el.name) continue;
      const v = p.get(el.name);
      if (v == null) continue;
      if (el.type === "checkbox") el.checked = v === "1"; else el.value = v;
    }
    if (p.get("ordina")) $("#sort").value = p.get("ordina");

    const draw = () => {
      const d = Object.fromEntries(new FormData(f));
      const sort = $("#sort").value;
      let list = cars.filter(c =>
        (!d.marca || c.marca === d.marca) && (!d.carrozzeria || c.carrozzeria === d.carrozzeria) &&
        (!d.carburante || c.carburante === d.carburante) && (!d.cambio || c.cambio === d.cambio) &&
        (!d.max || c.prezzo <= +d.max) && (!d.km || c.km <= +d.km) && (!d.anno || year(c) >= +d.anno) &&
        (!d.neopatentati || c.neopatentati));
      const S = { recenti: (a, b) => b.inserita.localeCompare(a.inserita), "prezzo-su": (a, b) => a.prezzo - b.prezzo, "prezzo-giu": (a, b) => b.prezzo - a.prezzo, km: (a, b) => a.km - b.km, anno: (a, b) => year(b) - year(a) };
      list.sort(S[sort] || S.recenti);
      $("#npinfo").hidden = !d.neopatentati;
      $("#list").innerHTML = list.length ? list.map(card).join("") :
        `<div class="empty" style="grid-column:1/-1"><h3>Nessuna auto con questi filtri</h3><p class="muted">Togli qualche filtro, oppure chiamaci: se cerchi un modello preciso possiamo trovarlo anche tramite importazione.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn" type="button" id="reset2">Azzera i filtri</button><a class="btn acc" href="${telHref(AZ.showroom.tel)}">${ICON.phone}${AZ.showroom.tel}</a></div></div>`;
      const r2 = $("#reset2"); if (r2) r2.onclick = reset;
      const q = new URLSearchParams(Object.entries(d).filter(([, v]) => v));
      if (sort !== "recenti") q.set("ordina", sort);
      history.replaceState(null, "", location.pathname + (q.toString() ? "?" + q : ""));
    };
    const reset = () => { f.reset(); draw(); };
    f.addEventListener("change", draw);
    $("#sort").addEventListener("change", draw);
    $("#reset").onclick = reset;
    $("#openf").onclick = () => f.classList.add("open");
    $("#closef").onclick = $("#showf").onclick = () => f.classList.remove("open");
    draw();
  },

  async scheda() {
    const cars = await getCars();
    const c = cars.find(x => x.id === params().get("id"));
    const main = $("#main");
    if (!c) {
      main.innerHTML = `<section class="band"><div class="wrap empty"><h1>Quest'auto non è più disponibile</h1><p class="muted">Potrebbe essere già stata venduta. Guarda le altre auto in vendita.</p><a class="btn acc" href="auto.html">Auto in vendita</a></div></section>`;
      return;
    }
    document.title = `${title(c)} ${c.versione} usata – Collinelli Auto`;
    const desc = `${title(c)} ${c.versione}, ${c.immatricolazione}, ${num(c.km)} km, ${c.carburante.toLowerCase()}, ${eur(c.prezzo)}${c.iva ? " + IVA" : ""}. Garanzia 12 mesi, Bagnacavallo (RA).`;
    document.querySelector('meta[name="description"]')?.setAttribute("content", desc);
    const ld = document.createElement("script");
    ld.type = "application/ld+json";
    ld.textContent = JSON.stringify({
      "@context": "https://schema.org", "@type": "Car", name: `${title(c)} ${c.versione}`, brand: { "@type": "Brand", name: c.marca }, model: c.modello,
      vehicleConfiguration: c.versione, bodyType: c.carrozzeria, fuelType: c.carburante, vehicleTransmission: c.cambio, color: c.colore || undefined,
      mileageFromOdometer: { "@type": "QuantitativeValue", value: c.km, unitCode: "KMT" }, dateVehicleFirstRegistered: c.immatricolazione.split("/").reverse().join("-"),
      itemCondition: "https://schema.org/UsedCondition", image: c.foto.map(full),
      offers: { "@type": "Offer", price: c.prezzo, priceCurrency: "EUR", availability: "https://schema.org/InStock", seller: { "@type": "AutoDealer", name: "Collinelli Auto S.r.l." } }
    });
    document.head.append(ld);
    const rows = [
      ["Immatricolazione", c.immatricolazione], ["Chilometri", num(c.km) + " km"], ["Alimentazione", c.carburante],
      ["Cambio", c.cambio + (c.marce ? `, ${c.marce}` : "")], ["Potenza", `${c.cv} CV (${Math.round(c.cv * 0.7355)} kW)`],
      ["Motore", c.litri ? `${c.litri} litri` : ""], ["Carrozzeria", c.carrozzeria], ["Colore", c.colore],
      ["Proprietari", c.proprietari ? (c.proprietari === 1 ? "Unico proprietario" : c.proprietari) : ""],
      ["Neopatentati", c.neopatentati ? "Sì, guidabile" : ""], ["IVA", c.iva ? "Prezzo IVA esclusa (22%)" : c.ivaEsposta ? "IVA esposta in fattura" : ""]
    ].filter(r => r[1]);
    const similar = cars.filter(x => x.id !== c.id).sort((a, b) => (b.carrozzeria === c.carrozzeria) - (a.carrozzeria === c.carrozzeria) || Math.abs(a.prezzo - c.prezzo) - Math.abs(b.prezzo - c.prezzo)).slice(0, 3);
    const name = `${title(c)} ${c.versione}`;
    main.innerHTML = `
    <div class="wrap">
      <nav class="crumbs" aria-label="Percorso"><a href="auto.html">Auto in vendita</a> / ${esc(c.marca)}</nav>
      <div class="detail">
        <div class="gal-col">
          <div class="gallery">
            <div class="slides" id="slides">${c.foto.map((p, i) => `<button type="button" data-i="${i}" aria-label="Ingrandisci foto ${i + 1}"><img src="${esc(full(p))}" alt="${esc(name)}, foto ${i + 1}" ${i ? 'loading="lazy"' : 'fetchpriority="high"'}></button>`).join("")}</div>
            <button class="gal-nav prev" id="prev" aria-label="Foto precedente">${ICON.left}</button>
            <button class="gal-nav next" id="next" aria-label="Foto successiva">${ICON.right}</button>
          </div>
          <div class="thumbs" id="thumbs">${c.foto.map((p, i) => `<button type="button" data-i="${i}" aria-label="Foto ${i + 1}"${i ? "" : ' aria-current="true"'}>${imgTag(p, "")}</button>`).join("")}</div>
        </div>
        <aside class="side">
          <div><h1>${esc(title(c))}</h1><p class="ver">${esc(c.versione)}</p></div>
          <div class="specs" style="font-size:15px"><span>${esc(c.immatricolazione)}</span><span>${num(c.km)} km</span><span>${esc(c.carburante)}</span><span>${esc(c.cambio)}</span><span>${c.cv} CV</span></div>
          <div class="price">${priceHtml(c)}</div>
          <div class="acts">
            <a class="btn acc" href="${telHref(AZ.showroom.tel)}">${ICON.phone}Chiama ${AZ.showroom.tel}</a>
            <button class="btn" type="button" id="ask">${ICON.mail}Chiedi informazioni</button>
            <button class="btn" type="button" id="drive">Prenota una prova su strada</button>
          </div>
          <div class="guarantee">${ICON.shield}<div><b>Garanzia 12 mesi</b><br><span class="muted">Controllata nella nostra officina prima della vendita, consegnata con attestazione di conformità.</span></div></div>
          <p class="note">${AZ.showroom.via}, Bagnacavallo. Finanziamenti e permuta su richiesta.</p>
        </aside>
        <div class="info">
          <section><h2>Caratteristiche</h2>
            <table class="sheet"><tbody>${rows.map(([k, v]) => `<tr><td>${k}</td><td>${esc(v)}</td></tr>`).join("")}</tbody></table></section>
          <section><h2>Dotazioni</h2>
            <ul class="equip">${c.dotazioni.map(d => `<li>${esc(d)}</li>`).join("")}</ul></section>
        </div>
      </div>
    </div>
    <section class="band sunk"><div class="wrap"><div class="head"><h2>Potrebbero interessarti</h2><a class="more" href="auto.html">Tutte le auto</a></div>
      <div class="cars">${similar.map(card).join("")}</div></div></section>`;

    const slides = $("#slides"), th = [...$("#thumbs").children];
    const go = i => { i = (i + c.foto.length) % c.foto.length; slides.scrollTo({ left: i * slides.clientWidth, behavior: matchMedia("(prefers-reduced-motion:reduce)").matches ? "auto" : "smooth" }); };
    const cur = () => Math.round(slides.scrollLeft / slides.clientWidth);
    slides.addEventListener("scroll", () => { const i = cur(); th.forEach((b, j) => b.toggleAttribute("aria-current", j === i)); th[i]?.scrollIntoView({ block: "nearest", inline: "nearest" }); }, { passive: true });
    th.forEach(b => b.onclick = () => go(+b.dataset.i));
    $("#prev").onclick = () => go(cur() - 1);
    $("#next").onclick = () => go(cur() + 1);
    document.addEventListener("keydown", e => {
      if ($("#modal")?.open && !$("#modal .lb")) return;
      if (e.key === "ArrowLeft") lbOpen ? lbGo(-1) : go(cur() - 1);
      if (e.key === "ArrowRight") lbOpen ? lbGo(1) : go(cur() + 1);
    });
    let lbOpen = false, lbI = 0;
    const lbGo = s => { lbI = (lbI + s + c.foto.length) % c.foto.length; $("#lbimg").src = full(c.foto[lbI]); };
    slides.addEventListener("click", e => {
      const b = e.target.closest("button"); if (!b) return;
      lbI = +b.dataset.i;
      let d = $("#modal");
      if (!d) { d = document.createElement("dialog"); d.id = "modal"; document.body.append(d); }
      d.innerHTML = `<div class="lb"><div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><div style="display:flex;gap:8px"><button class="gal-nav" style="position:static;translate:none" id="lbp" aria-label="Foto precedente">${ICON.left}</button><button class="gal-nav" style="position:static;translate:none" id="lbn" aria-label="Foto successiva">${ICON.right}</button></div><button class="x" aria-label="Chiudi">×</button></div><img id="lbimg" src="${esc(full(c.foto[lbI]))}" alt="${esc(name)}"></div>`;
      d.querySelector(".x").onclick = () => d.close();
      $("#lbp").onclick = () => lbGo(-1); $("#lbn").onclick = () => lbGo(1);
      d.onclose = () => { lbOpen = false; go(lbI); };
      lbOpen = true; d.showModal();
    });
    $("#ask").onclick = () => openModal(`<h2 style="font-size:24px">Chiedi informazioni</h2><p class="muted">${esc(name)}, ${eur(c.prezzo)}</p>` + contactForm({ to: AZ.showroom.mail, subject: `Informazioni: ${name}`, body: `Vorrei avere informazioni su ${name} (${eur(c.prezzo)}).` }));
    $("#drive").onclick = () => openModal(`<h2 style="font-size:24px">Prenota una prova su strada</h2><p class="muted">${esc(name)}</p>` + contactForm({ to: AZ.showroom.mail, subject: `Prova su strada: ${name}`, fields: `<label class="f">Giorno preferito<input name="giorno" type="date"></label>`, body: `Vorrei provare ${name}.` }));
  },

  officina() {
    $("#form-officina").innerHTML = contactForm({
      to: AZ.officina.mail, subject: "Richiesta appuntamento officina",
      fields: `<label class="f">Auto e targa<input name="auto" placeholder="Es. Fiat Panda, AB123CD"></label>
        <label class="f">Lavoro da fare<select name="servizio"><option>Tagliando</option><option>Riparazione</option><option>Diagnosi elettronica</option><option>Climatizzatore</option><option>Cambio automatico</option><option>Revisione</option><option>Altro</option></select></label>
        <label class="f">Giorno preferito<input name="giorno" type="date"></label>`
    });
    $("#place-officina").innerHTML = placeCard(AZ.officina);
  },

  async "chi-siamo"() {
    $("#about-places").innerHTML = placeCard(AZ.showroom, `<p class="note">Vendita, permute e finanziamenti.</p>`) + placeCard(AZ.officina, `<p class="note">Tagliandi, riparazioni e revisioni per tutte le marche.</p>`);
    marquee(await getCars());
  },

  contatti() {
    const st = openStatus();
    $("#status").className = "status " + (st.open ? "on" : "off");
    $("#status").textContent = st.text;
    $("#quick").innerHTML = [
      [telHref(AZ.showroom.tel), ICON.phone, "Chiama lo showroom", AZ.showroom.tel],
      [telHref(AZ.officina.tel), ICON.phone, "Chiama l'officina", AZ.officina.tel],
      ["#scrivi", ICON.mail, "Scrivici", "Ti ricontattiamo noi"],
      [AZ.showroom.maps, ICON.pin, "Indicazioni", "Via Chiusa 53/F"]
    ].map(([h, i, t, s], k) => `<a href="${h}"${k === 3 ? ' rel="noopener"' : ""}${k === 0 ? ' class="main"' : ""}>${i}<b>${t}</b><span>${s}</span></a>`).join("");
    const site = (s, q, extra) => `
      <article class="site">
        <iframe class="map" title="Mappa: ${s.nome}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=${q}&z=15&output=embed"></iframe>
        <div class="site-bd">
          <h2>${s.nome}</h2>
          <address>${s.via}, ${s.cap}</address>
          <dl>
            <div><dt>Telefono</dt><dd><a href="${telHref(s.tel)}">${s.tel}</a></dd></div>
            <div><dt>Email</dt><dd><a href="mailto:${s.mail}">${s.mail}</a></dd></div>
          </dl>
          ${extra}
          <a class="btn" href="${s.maps}" rel="noopener">${ICON.pin}Apri in Google Maps</a>
        </div>
      </article>`;
    $("#sites").innerHTML = site(AZ.showroom, "44.411867,11.979302", `<h3>Orari</h3>${hoursTable()}`) +
      site(AZ.officina, encodeURIComponent("Via Celletta 8, 48012 Bagnacavallo"), `<h3>Orari</h3><p class="muted">Per orari e appuntamenti chiama il ${AZ.officina.tel}.</p><h3>Servizi</h3><ul class="tags">${["Tagliandi", "Riparazioni", "Diagnosi elettronica", "Climatizzatori", "Cambi automatici", "Revisioni", "Auto sostitutiva"].map(s => `<li>${s}</li>`).join("")}</ul><a class="btn acc" href="officina.html#prenota">Prenota in officina</a>`);
    const topics = ["Acquisto di un'auto", "Permuta", "Finanziamento", "Ricerca di un modello", "Officina", "Altro"];
    $("#form-contatti").innerHTML = contactForm({
      to: AZ.showroom.mail, subject: "Richiesta dal sito",
      fields: `<fieldset class="topics"><legend>Di cosa hai bisogno?</legend>${topics.map((t, i) => `<label><input type="radio" name="argomento" value="${t}"${i ? "" : " checked"}><span>${t}</span></label>`).join("")}</fieldset>`
    });
  }
};

/* blocchi presenti su più pagine */
const hoursEl = $("#hours"); if (hoursEl) hoursEl.innerHTML = hoursTable();
const placesEl = $("#home-places");
if (placesEl) {
  const st = openStatus(), oggi = AZ.orari[dayIdx()][1];
  placesEl.innerHTML = placeCard(AZ.showroom, `<p class="status ${st.open ? "on" : "off"}" style="margin:0">${esc(st.text)}</p><p class="muted">Oggi: ${oggi.length ? oggi.map(([a, z]) => `${a}–${z}`).join(", ") : "chiuso"}. <a href="contatti.html">Tutti gli orari</a></p>`) +
    placeCard(AZ.officina, `<p class="muted">Tagliandi, riparazioni, diagnosi e revisioni per tutte le marche. Per appuntamenti chiama il ${AZ.officina.tel}.</p>`);
}

(RENDER[page] || (() => {}))();
}
