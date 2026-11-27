-- Collinelli Auto: tabella del parco auto per il pannello admin (Supabase / Postgres)
create table public.auto (
  id            text primary key,              -- slug usato nell'indirizzo della scheda
  marca         text not null,
  modello       text not null,
  versione      text not null,
  prezzo        integer not null check (prezzo > 0),
  iva           boolean not null default false, -- true = prezzo + IVA (veicoli commerciali)
  iva_esposta   boolean not null default false,
  km            integer not null check (km >= 0),
  immatricolazione text not null,              -- formato MM/AAAA
  carburante    text not null,
  cambio        text not null check (cambio in ('Manuale','Automatico')),
  marce         text,
  cv            integer not null,
  litri         text,
  colore        text,
  proprietari   integer,
  carrozzeria   text not null,
  neopatentati  boolean not null default false, -- verificato sul libretto: max 105 kW e 75 kW/t
  evidenza      boolean not null default false,
  dotazioni     text[] not null default '{}',
  foto          text[] not null default '{}',   -- percorsi nello storage "foto-auto", la prima è la copertina
  venduta       boolean not null default false,
  inserita      date not null default current_date,
  aggiornata    timestamptz not null default now()
);

alter table public.auto enable row level security;
-- chiunque legge le auto non vendute; solo gli utenti del pannello scrivono
create policy "lettura pubblica" on public.auto for select using (venduta = false);
create policy "scrittura staff" on public.auto for all to authenticated using (true) with check (true);

-- richieste dai moduli del sito (info auto, prova su strada, officina)
create table public.richieste (
  id         bigint generated always as identity primary key,
  tipo       text not null,       -- informazioni | prova | officina | contatto
  auto_id    text references public.auto(id) on delete set null,
  nome       text not null,
  telefono   text,
  email      text,
  messaggio  text,
  dati       jsonb not null default '{}',
  creata     timestamptz not null default now(),
  gestita    boolean not null default false
);
alter table public.richieste enable row level security;
create policy "invio pubblico" on public.richieste for insert with check (true);
create policy "lettura staff" on public.richieste for select to authenticated using (true);
create policy "gestione staff" on public.richieste for update to authenticated using (true);
