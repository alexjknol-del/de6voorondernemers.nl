#!/usr/bin/env python3
# Generator voor de6voorondernemers.nl - onafhankelijke kennisgids over ondernemen in Nederland.
import os, json, html, hashlib
def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"
BASE="https://de6voorondernemers.nl"; SITE="De 6 voor Ondernemers"; EMAIL="info@de6voorondernemers.nl"
AUTEUR="Nadia Berger"; AUTEUR_ROL="Redacteur ondernemen"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site"); CSS_VER=_ver("assets/css/style.css")
def esc(s): return html.escape(str(s), quote=True)
DISC="Dit artikel geeft algemene informatie en is geen fiscaal, juridisch of financieel advies. Regels en bedragen wijzigen jaarlijks. Voor een concrete situatie zijn een boekhouder, accountant of adviseur de aangewezen partij."

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 11h18"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><rect x="5" y="11" width="4" height="9"/><rect x="10" y="7" width="4" height="13"/><rect x="15" y="4" width="4" height="16"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
NAV=[("Home","/"),("Onderwerpen","/onderwerpen/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Contact","/contact/")]

def head(t,d,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title><meta name="description" content="{esc(d)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website"><meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}"><meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{can}">
<meta name="theme-color" content="#1F2A38">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Public+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}</head><body>
<header class="site-head"><nav class="nav" id="nav">
  <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>De 6 voor Ondernemers</b><span>Kennisgids</span></span></a>
  {nav}
  <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
</nav></header>
"""

def footer():
    return f"""<footer class="foot"><div class="wrap"><div class="cols">
  <div><a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>De 6 voor Ondernemers</b><span style="color:#78838F">Kennisgids</span></span></a>
    <p class="note">De 6 voor Ondernemers is een onafhankelijke kennisgids over ondernemen in Nederland. Het platform verleent geen diensten, bemiddelt niet en geeft geen advies over individuele situaties.</p></div>
  <div><h4>Kennis</h4><a href="/onderwerpen/">Onderwerpen</a><a href="/gidsen/">Gidsen</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
  <div><h4>Informatie</h4><a href="/over/">Over dit platform</a><a href="/contact/">Contact</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a></div>
</div><div class="foot-bottom"><span>&copy; 2026 {esc(SITE)}</span>
<span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span></div></div></footer>
</body></html>"""

def crumb(i): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":k+1,"name":n,"item":BASE+u} for k,(n,u) in enumerate(i)]}
def crumbs_html(i):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in i[:-1]]; o.append(f'<span>{esc(i[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'
def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True); open(f,"w",encoding="utf-8").write(c)
def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
    return "".join(o)
def byline(): return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

ONDERWERPEN=[
 {"slug":"rechtsvorm-kiezen","naam":"Rechtsvorm kiezen",
  "resume":"De keuze tussen eenmanszaak en bv draait om aansprakelijkheid en belastingdruk, en die weging verschuift met de winst.",
  "specs":[("Eenmanszaak","Privé aansprakelijk"),("BV","Rechtspersoon"),("Omslagpunt","Afhankelijk van winst")],
  "secties":[("Aansprakelijkheid als eerste vraag","Bij een eenmanszaak en een vof lopen zakelijke schulden door naar het privévermogen. Een bv is een aparte rechtspersoon, waardoor die scheiding er in beginsel wel is. Bij bestuurdersaansprakelijkheid of persoonlijke borgstelling vervalt dat voordeel deels, wat de bescherming minder absoluut maakt dan vaak wordt aangenomen."),
   ("Fiscaal omslagpunt","Een eenmanszaak valt onder de inkomstenbelasting, met ondernemersaftrek en de mkb-winstvrijstelling. Een bv betaalt vennootschapsbelasting, waarna uitkeren naar privé opnieuw belast wordt. Het punt waarop een bv gunstiger uitpakt verschuift jaarlijks met de tarieven en met de afbouw van de zelfstandigenaftrek, en is daarmee geen vast bedrag.")],
  "punten":["Aansprakelijkheid weegt zwaarder dan fiscaliteit","Bescherming van een bv is niet absoluut","Het fiscale omslagpunt verschuift jaarlijks","Omzetten kan later, met kosten"]},
 {"slug":"administratie-en-btw","naam":"Administratie en btw",
  "resume":"De bewaarplicht is zeven jaar en de aangiftetermijnen liggen vast; daar zit weinig ruimte in.",
  "specs":[("Bewaarplicht","7 jaar"),("Aangifte","Per kwartaal of maand"),("Vastgoed","10 jaar")],
  "secties":[("Wat bewaard moet blijven","De wettelijke bewaarplicht bedraagt zeven jaar voor de basisadministratie, en tien jaar voor gegevens over onroerende zaken. Facturen, bankafschriften, contracten en de urenadministratie vallen daaronder. Digitaal bewaren mag, mits de gegevens leesbaar en controleerbaar blijven gedurende die hele periode."),
   ("Btw in de praktijk","De aangifte volgt meestal een kwartaalritme. Betalen gebeurt over gefactureerde bedragen, ook wanneer de klant nog niet heeft betaald, wat bij lange betaaltermijnen tot een tijdelijk tekort leidt. Bij oninbare vorderingen bestaat een teruggaafregeling, maar die vraagt een expliciete stap.")],
  "punten":["Zeven jaar bewaren, tien bij vastgoed","Btw is verschuldigd bij factuur, niet bij betaling","Kwartaalaangifte is de standaard","Urenadministratie telt mee voor de aftrek"]},
 {"slug":"financiering","naam":"Financiering",
  "resume":"De vorm van financiering bepaalt wie er meebeslist, en dat weegt vaak zwaarder dan de rente.",
  "specs":[("Vreemd vermogen","Terugbetalen"),("Eigen vermogen","Aandeel afstaan"),("Zekerheid","Vaak gevraagd")],
  "secties":[("Lenen of aandelen uitgeven","Een lening moet terugbetaald worden maar laat de zeggenschap intact. Een investeerder die aandelen krijgt hoeft niet terugbetaald te worden, maar krijgt invloed en een deel van de toekomstige waarde. Dat verschil is doorgaans bepalender dan het rentepercentage."),
   ("Zekerheden en borgstelling","Banken vragen bij kleinere ondernemingen vaak een persoonlijke borgstelling, waarmee de scheiding tussen zakelijk en privé alsnog doorbroken wordt. Wie een bv opricht juist vanwege die scheiding, doet er goed aan de borgstellingsvoorwaarden nauwkeurig te bekijken.")],
  "punten":["Lening houdt zeggenschap intact","Investeerder deelt in de toekomstige waarde","Borgstelling doorbreekt de scheiding met privé","Werkkapitaal is een andere behoefte dan investering"]},
 {"slug":"verzekeringen","naam":"Verzekeringen",
  "resume":"Aansprakelijkheid en arbeidsongeschiktheid zijn de twee risico's die een onderneming kunnen beëindigen.",
  "specs":[("AVB","Aansprakelijkheid"),("AOV","Arbeidsongeschiktheid"),("Beroeps","Bij advies")],
  "secties":[("Bedrijfs- en beroepsaansprakelijkheid","Een bedrijfsaansprakelijkheidsverzekering dekt schade aan personen en zaken. Een beroepsaansprakelijkheidsverzekering dekt vermogensschade door een fout in advies of ontwerp, en dat is een andere categorie. Adviseurs, ontwerpers en ICT-partijen hebben doorgaans juist die tweede nodig."),
   ("Arbeidsongeschiktheid","Zelfstandigen vallen niet onder een werknemersverzekering. Zonder aov ontbreekt inkomen bij langdurige uitval, terwijl de vaste lasten doorlopen. Alternatieven zoals een broodfonds dekken doorgaans een beperkte periode, wat bij langdurige uitval niet voldoende is.")],
  "punten":["Bedrijfs- en beroepsaansprakelijkheid zijn verschillend","Zelfstandigen hebben geen vangnet bij uitval","Broodfonds dekt een beperkte periode","Dekking en uitsluitingen jaarlijks nalopen"]},
 {"slug":"personeel-aannemen","naam":"Personeel aannemen",
  "resume":"De eerste medewerker brengt verplichtingen mee die verder gaan dan het salaris zelf.",
  "specs":[("Loonheffing","Aanmelden"),("Cao","Mogelijk verplicht"),("Kosten","Ruim boven bruto")],
  "secties":[("Wat er bij komt kijken","Naast het brutoloon komen werkgeverslasten, vakantiegeld, pensioenpremie en de kosten van loondoorbetaling bij ziekte. De werkelijke kosten liggen daarmee aanzienlijk boven het brutoloon. Een sectorale cao kan bovendien verplicht van toepassing zijn, ook zonder dat de onderneming zich daarbij heeft aangesloten."),
   ("Alternatieven en schijnzelfstandigheid","Werken met zelfstandigen lijkt eenvoudiger, maar wanneer de feitelijke situatie op een dienstverband lijkt, kan de Belastingdienst dat als zodanig aanmerken. Bepalend zijn gezagsverhouding, de verplichting het werk zelf te doen en de aanwezigheid van loon, niet de tekst van de overeenkomst.")],
  "punten":["Werkelijke kosten liggen ruim boven bruto","Een cao kan verplicht van toepassing zijn","Loondoorbetaling bij ziekte is een groot risico","De feitelijke situatie bepaalt of iets een dienstverband is"]},
 {"slug":"voorwaarden-en-contracten","naam":"Algemene voorwaarden en contracten",
  "resume":"Voorwaarden werken alleen wanneer ze vóór of bij het sluiten van de overeenkomst zijn overhandigd.",
  "specs":[("Moment","Voor of bij sluiten"),("Consument","Zwarte en grijze lijst"),("Verwijzing","Niet voldoende")],
  "secties":[("Ter hand stellen","Algemene voorwaarden gelden pas wanneer de wederpartij er redelijkerwijs kennis van heeft kunnen nemen. Een verwijzing op een factuur is te laat, omdat de overeenkomst dan al is gesloten. Meesturen bij de offerte of vooraf laten aanvinken bij een online bestelling voldoet wel."),
   ("Bescherming van consumenten","Bij overeenkomsten met consumenten gelden een zwarte lijst van verboden bedingen en een grijze lijst van vermoedelijk onredelijke bedingen. Een beding uit die eerste categorie is zonder meer vernietigbaar, hoe duidelijk het ook is opgeschreven.")],
  "punten":["Overhandigen voor of bij het sluiten","Verwijzing op de factuur is te laat","Zwarte lijst geldt bij consumenten altijd","Betalingstermijn en eigendomsvoorbehoud vastleggen"]},
]
def onderwerp(s): return next(x for x in ONDERWERPEN if x["slug"]==s)

GIDSEN=[
 {"slug":"starten-als-zelfstandige","titel":"Starten als zelfstandige: de eerste stappen op volgorde","ic":"scale",
  "resume":"Inschrijven is de makkelijkste stap. De beslissingen eromheen bepalen hoeveel werk er later bij komt.",
  "body":[("p","Een onderneming starten begint bij de Kamer van Koophandel, maar de inschrijving zelf is een formaliteit. Wat daarvoor en daarna geregeld wordt, bepaalt hoe soepel het eerste jaar verloopt."),
   ("h2","Voor de inschrijving"),("ul",["De rechtsvorm bepalen, met aansprakelijkheid als eerste afweging.","Nagaan of er vergunningen of diploma-eisen gelden voor de activiteit.","Controleren of de gekozen naam vrij is en geen inbreuk maakt op een merk.","Een zakelijke rekening openen, ook bij een eenmanszaak waar dat niet verplicht is."]),
   ("h2","Bij de inschrijving"),("p","De inschrijving bij de Kamer van Koophandel leidt automatisch tot aanmelding bij de Belastingdienst, die een btw-identificatienummer en een omzetbelastingnummer verstrekt. De activiteitencode die daarbij wordt gekozen, bepaalt onder welke sector de onderneming valt en kan gevolgen hebben voor verplichte regelingen."),
   ("h2","Direct daarna"),("p","Administratie inrichten voordat de eerste factuur wordt verstuurd, scheelt achteraf reconstrueren. Dat betekent een systeem voor facturen en bonnen, een urenregistratie voor de aftrek, en een aparte reservering voor btw en inkomstenbelasting."),
   ("callout","Reserveer vanaf de eerste factuur een vast percentage voor belastingen op een aparte rekening. De eerste aanslag komt vaak later dan verwacht en dan over een langere periode tegelijk."),
   ("h2","In het eerste jaar"),("p","De ondernemersaftrek vraagt om voldoende bestede uren, wat een urenadministratie noodzakelijk maakt vanaf dag één. Achteraf reconstrueren wordt bij controle zelden geaccepteerd."),
   ("p",DISC)]},
 {"slug":"prijs-bepalen","titel":"Een tarief bepalen dat standhoudt","ic":"doc",
  "resume":"Een uurtarief afleiden van een loondienstsalaris leidt vrijwel altijd tot een te laag bedrag.",
  "body":[("p","De meest gemaakte fout bij het bepalen van een tarief is uitgaan van wat iemand in loondienst verdiende. Dat bedrag houdt geen rekening met wat er als zelfstandige zelf betaald moet worden."),
   ("h2","Wat er bovenop moet"),("ul",["Vakantiedagen en feestdagen die niet worden doorbetaald.","Ziekte en arbeidsongeschiktheid, of de premie daarvoor.","Pensioenopbouw die zelf geregeld wordt.","Verzekeringen, administratie, gereedschap en scholing.","Niet-declarabele tijd voor acquisitie, offertes en administratie."]),
   ("h2","Declarabele uren zijn beperkt"),("p","Van een werkweek gaat een aanzienlijk deel op aan zaken die niet gefactureerd worden. Rekenen met veertig declarabele uren per week gedurende vijftig weken geeft een beeld dat in de praktijk zelden gehaald wordt; twintig tot vijfentwintig declarabele uren is realistischer."),
   ("h2","Uurtarief of vaste prijs"),("p","Een uurtarief beloont langzamer werken en straft ervaring af. Een vaste prijs per opdracht koppelt de vergoeding aan het resultaat, wat bij toenemende ervaring gunstiger uitpakt, mits de opdracht scherp is afgebakend."),
   ("h2","Verhogen"),("p","Tarieven die jarenlang gelijk blijven, dalen in reële termen. Een jaarlijkse aanpassing die vooraf is aangekondigd, roept minder discussie op dan een sprong na vijf jaar."),
   ("p",DISC)]},
]

ARTIKELEN=[
 {"slug":"cashflow-boven-winst","titel":"Waarom cashflow belangrijker is dan winst","cat":"Financiën","datum":"2026-07-20","datum_nl":"20 juli 2026","lees":4,
  "resume":"Winstgevende ondernemingen gaan failliet wanneer het geld te laat binnenkomt.",
  "body":[("p","Winst is een boekhoudkundig begrip dat ontstaat op het moment van factureren. Cashflow gaat over het moment waarop geld daadwerkelijk beweegt. Dat verschil kan een gezonde onderneming laten omvallen."),
   ("h2","Waar het misloopt"),("p","Een factuur met een betaaltermijn van zestig dagen telt direct mee in de winst, terwijl de btw erover al eerder afgedragen moet worden en leveranciers eerder betaald willen worden. Bij groei wordt dat gat groter, niet kleiner, omdat er meer voorgefinancierd wordt."),
   ("h2","Wat helpt"),("ul",["Kortere betaaltermijnen afspreken en die bewaken.","Een deel vooraf factureren bij grotere opdrachten.","Facturen versturen op het moment van levering, niet aan het eind van de maand.","Een buffer aanhouden voor minstens enkele maanden vaste lasten."]),
   ("h2","Groei kost geld"),("p","Meer opdrachten betekent meer inkoop, meer uren en meer voorfinanciering, terwijl de betalingen achterlopen. Snelle groei is daarmee een periode van verhoogd risico, ook bij een gezonde marge."),
   ("p",DISC)]},
 {"slug":"algemene-voorwaarden-in-de-praktijk","titel":"Algemene voorwaarden die in de praktijk niet gelden","cat":"Juridisch","datum":"2026-07-08","datum_nl":"8 juli 2026","lees":3,
  "resume":"Voorwaarden die pas op de factuur worden genoemd, hebben in een geschil doorgaans geen waarde.",
  "body":[("p","Veel ondernemers hebben algemene voorwaarden laten opstellen en gaan ervan uit dat die daarmee gelden. In een geschil blijkt geregeld dat ze niet van toepassing zijn."),
   ("h2","Het moment is bepalend"),("p","Voorwaarden moeten voor of uiterlijk bij het sluiten van de overeenkomst ter beschikking zijn gesteld. Een tekst op de achterkant van een factuur komt te laat, omdat de afspraak op dat moment al bestond."),
   ("h2","Twee sets voorwaarden"),("p","Wanneer beide partijen naar hun eigen voorwaarden verwijzen, geldt in Nederland doorgaans de set van degene die er als eerste naar verwees, tenzij de ander die uitdrukkelijk van de hand wijst. Een enkele zin in de opdrachtbevestiging kan daarmee doorslaggevend zijn."),
   ("h2","Wat wel werkt"),("ul",["Meesturen bij de offerte, met een verwijzing in de tekst.","Bij online sluiten een aanvinkoptie met een leesbare link.","Bij herhaalde samenwerking eenmalig vastleggen dat ze op alle opdrachten van toepassing zijn."]),
   ("p",DISC)]},
]

def tile(s):
    return f"""<a class="tile" href="/onderwerpen/{s['slug']}/"><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:96].rsplit(' ',1)[0])}...</p></a>"""
def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijke kennisgids over ondernemen: rechtsvorm, administratie, financiering, verzekeringen, personeel en voorwaarden."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    gids="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    h=head("De 6 voor Ondernemers | kennisgids over ondernemen",
      "Onafhankelijke kennisgids over ondernemen in Nederland. Rechtsvorm, administratie en btw, financiering, verzekeringen, personeel en voorwaarden.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div><span class="eyebrow">{IC['scale']}Kennisgids</span>
  <h1>Ondernemen, <em>zes keer uitgelegd</em></h1>
  <p class="lead">Rechtsvorm, administratie, financiering, verzekeringen, personeel en voorwaarden: de zes onderwerpen waar vrijwel elke onderneming mee te maken krijgt, zonder verkoopbelang.</p>
  <div class="hero-actions"><a class="btn btn-plum" href="/onderwerpen/">Bekijk de onderwerpen {IC['arrow']}</a><a class="btn btn-ghost" href="/gidsen/">Naar de gidsen</a></div>
  <div class="hero-meta"><span>{IC['check']}6 onderwerpen</span><span>{IC['check']}Verplichtingen benoemd</span><span>{IC['check']}Geen dienstverlener</span></div></div>
  <div class="hero-art"><img src="/assets/img/hero.svg" alt="Illustratie van een werkplek van een ondernemer" width="480" height="340"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['doc']}Onderwerpen</span><h2>De zes onderwerpen</h2>
  <p class="lead">Per onderwerp de kern, de verplichtingen die gelden en de punten waarop het in de praktijk misgaat.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Twee praktische gidsen</h2></div>
  <div class="grid cols-2">{gids}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p></div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Een onderwerp gemist?</h2><p>Deze gids groeit op basis van vragen die binnenkomen. Suggesties en correcties zijn welkom bij de redactie.</p>
  <a class="btn btn-gold" href="/contact/">Mail de redactie {IC['arrow']}</a></div></div></section>"""
    write("/",h+footer())

def p_ond_index():
    path="/onderwerpen/"; c=[("Home","/"),("Onderwerpen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Onderwerpen","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/onderwerpen/{s['slug']}/"} for i,s in enumerate(ONDERWERPEN)]},crumb(c)]
    h=head("Onderwerpen ondernemen | "+SITE,"Overzicht van onderwerpen rond ondernemen: rechtsvorm, administratie en btw, financiering, verzekeringen, personeel en voorwaarden.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['doc']}Overzicht</span>
  <h1>Onderwerpen</h1><p class="lead">Zes onderwerpen die samen de basis vormen van een onderneming, met de verplichtingen die erbij horen.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>"""
    write(path,h+footer())

def p_ond(s):
    path=f"/onderwerpen/{s['slug']}/"; c=[("Home","/"),("Onderwerpen","/onderwerpen/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in s["punten"])
    anders=[x for x in ONDERWERPEN if x["slug"]!=s["slug"]][:3]
    h=head(f"{s['naam']} | uitgelegd | {SITE}", s["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose"><span class="eyebrow">{IC['scale']}Onderwerp</span>
  <h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="specs">{sp}</dl></div>
  <div class="wrap prose">{sec}<h2>Kort samengevat</h2><ul class="ticks" style="margin-bottom:16px">{pt}</ul>
  <p class="disc">{esc(DISC)}</p>{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Andere onderwerpen</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div></div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Gidsen | starten en tarief bepalen | "+SITE,"Praktische gidsen over de eerste stappen als zelfstandige en over het bepalen van een tarief dat standhoudt.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span>
  <h1>Gidsen</h1><p class="lead">Twee onderwerpen waarin de volgorde van beslissingen bepaalt hoeveel werk er later bij komt.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC[g['ic']]}Gids</span>
  <h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>{blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over financiën en voorwaarden | "+SITE,"Achtergrondartikelen over ondernemen in de praktijk, van cashflow tot voorwaarden die niet blijken te gelden.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span>
  <h1>Artikelen</h1><p class="lead">Achtergrond bij wat in de praktijk misgaat, en waarom.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['clock']}{esc(a['cat'])}</span>
  <h1>{esc(a['titel'])}</h1><p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ARTIKELEN if x['slug']!=a['slug'])}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over De 6 voor Ondernemers | wat dit platform is | "+SITE,
      "De 6 voor Ondernemers is een onafhankelijke kennisgids over ondernemen. Geen dienstverlener, geen bemiddeling en geen advies over individuele situaties.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een kennisgids, geen adviesbureau</h1>
  <p class="lead">De 6 voor Ondernemers behandelt zes onderwerpen waar vrijwel elke Nederlandse onderneming vroeg of laat mee te maken krijgt, van rechtsvorm tot algemene voorwaarden.</p>
  <h2>Waarom deze gids bestaat</h2>
  <p>Informatie over ondernemen komt vaak van partijen die tegelijk een dienst aanbieden: een boekhoudpakket, een verzekering of een financiering. Dat maakt lastig te beoordelen wat werkelijk nodig is. Deze gids beschrijft de onderwerpen los van welk product dan ook.</p>
  <div class="callout"><p><strong>Geen adviesbureau.</strong> Dit platform verleent geen diensten, bemiddelt niet en geeft geen advies over individuele situaties. Er zijn geen samenwerkingen met aanbieders van software, verzekeringen of financiering.</p></div>
  <h2>Wat hier wel staat</h2>
  <p>Per onderwerp de hoofdregel, de verplichtingen die daarbij horen en de punten waarop het in de praktijk misgaat. Bedragen en percentages worden bewust beperkt genoemd, omdat die jaarlijks wijzigen.</p>
  <h2>Actualiteit</h2>
  <p>Fiscale regels, tarieven en drempelbedragen wijzigen jaarlijks. De teksten beschrijven daarom vooral de systematiek en niet de exacte bedragen. Voor een beslissing met financiële gevolgen blijft toetsing bij een boekhouder of adviseur verstandig.</p>
  <p style="margin-top:16px"><a class="btn btn-plum" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Naar de onderwerpen</a></p></div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#nadia","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de onderwerpen en gidsen van De 6 voor Ondernemers.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['scale']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Nadia schrijft de onderwerpen, de gidsen en de artikelen op deze site.</p></div></div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Van de boekhouding naar de redactie</h2>
  <p>Nadia werkte jaren op een administratiekantoor met veel kleine ondernemers als klant, waar dezelfde problemen terugkwamen: btw die niet gereserveerd was, algemene voorwaarden die niet golden, en een tarief dat te laag was vastgesteld en jarenlang niet werd aangepast.</p>
  <h2>Systematiek boven bedragen</h2>
  <p>Nadia is geen accountant of belastingadviseur. De teksten beschrijven hoe regelingen werken en waar de aandachtspunten zitten, zonder exacte bedragen die snel verouderen. Voor een berekening op maat blijft een boekhouder of adviseur de aangewezen partij.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie op deze pagina is een tekening, geen foto.</p>
  <h2>Contact</h2>
  <p>Correcties en suggesties komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor De 6 voor Ondernemers? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['mail']}Contact</span>
  <h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een correctie op een tekst, met vindplaats of bron.</li><li>Een onderwerp dat nog ontbreekt in de gids.</li><li>Een signaal dat een regeling of bedrag is gewijzigd.</li></ul>
  <h2>Waar niet</h2>
  <p>Individuele situaties worden niet beoordeeld en er wordt geen fiscaal of financieel advies gegeven. Voor een concrete vraag zijn een boekhouder, een accountant, de Kamer van Koophandel of de Belastingdienst de aangewezen partijen.</p></div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>De 6 voor Ondernemers is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend wat in dat bericht staat, en dat wordt alleen gebruikt om te antwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst.</p>",
      "<h2>Lettertypen</h2><p>De lettertypen worden geladen via een externe dienst, wat bij het tonen van een pagina een verzoek naar die dienst met zich meebrengt.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. Het overzicht van onderwerpen is een goed vertrekpunt.</p>
  <p><a class="btn btn-plum" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Alle onderwerpen</a></p></div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/onderwerpen/","/gidsen/","/nieuws/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/onderwerpen/{s['slug']}/" for s in ONDERWERPEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.de6voorondernemers.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_ond_index()
    for s in ONDERWERPEN: p_ond(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
