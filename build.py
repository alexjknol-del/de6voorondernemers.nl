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
"case":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><line x1="2" y1="13" x2="22" y2="13"/></svg>',
}
NAV=[("Home","/"),("Onderwerpen","/onderwerpen/"),("Gidsen","/gidsen/"),("Bedrijven","/bedrijven/"),("Nieuws","/nieuws/"),("Over","/over/"),("Partners","/partners/"),("Contact","/contact/")]

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
<div><h4>Kennis</h4><a href="/onderwerpen/">Onderwerpen</a><a href="/gidsen/">Gidsen</a><a href="/bedrijven/">Bedrijven</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
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
        elif b[0]=="plink": o.append(f"<p>{b[1]}</p>")
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

BEDRIJVEN=[
{"slug":"bedrijf-verkopen-advies","naam":"OvernameAdvies","dienst":"Bedrijfsovername","plaats":"Houten",
"resume":"Begeleidt bedrijfsverkopen van waardebepaling tot overdracht, met een no-cure-no-pay-aanpak.",
"specs":[("Locatie","Houten"),("Categorie","Bedrijfsovername"),("Telefoon","030-760 1505")],
"secties":[("Begeleiding bij verkoop","Een bedrijf verkopen is voor de meeste ondernemers een eenmalig traject, terwijl een koper vaak wel ervaring heeft met overnames. OvernameAdvies begeleidt het hele proces: van een eerste waardebepaling, via een verkoopmemorandum en het benaderen van geschikte kopers, tot de onderhandeling en de uiteindelijke overdracht."),
("Werkwijze","Het kantoor werkt met een no-cure-no-pay-aanpak, waarbij de vergoeding gekoppeld is aan een geslaagde verkoop. Dat past bij ondernemers die eerst een reëel beeld willen van de haalbaarheid en de verwachte opbrengst, voordat er kosten worden gemaakt.")],
"punten":["Begeleiding van waardebepaling tot overdracht","Werkwijze op basis van no cure no pay","Vestiging in Houten","Eerste gesprek vrijblijvend"],
"contact":{"adres":"Sleepboot 11b, Houten","telefoon":"030-760 1505","email":"info@overnameadvies.nl"},
"url":"https://www.overnameadvies.nl/bedrijf-verkopen","linktekst":"OvernameAdvies"},
{"slug":"fiscaal-advocaat-kantoor","naam":"HuygenLammers Advocaten","dienst":"Fiscaal recht","plaats":"Amsterdam",
"resume":"Advocatenkantoor gespecialiseerd in fiscale procedures, fiscale strafzaken en mediation.",
"specs":[("Locatie","Amsterdam"),("Categorie","Fiscaal recht"),("Telefoon","020-22 69 018")],
"secties":[("Wanneer een advocaat nodig is","Bij een langlopend boekenonderzoek, een naheffingsaanslag of een vermoeden van fraude volstaat een boekhouder of fiscalist niet altijd. HuygenLammers Advocaten behandelt fiscale procedures en fiscale strafzaken, en mag als advocatenkantoor ook bijstaan zodra een zaak een strafrechtelijk karakter krijgt."),
("Geheimhouding als voordeel","Een advocaat is gebonden aan een geheimhoudingsplicht die verder gaat dan die van andere adviseurs. Bij een vrijwillige melding van eerder niet-aangegeven vermogen of bij een verhoor door de FIOD weegt dat verschil zwaar mee.")],
"punten":["Fiscale procedures en fiscale strafzaken","Ook bijstand bij een FIOD-onderzoek","Mediation als alternatief voor procederen","Gevestigd in Amsterdam"],
"contact":{"adres":"Willemsparkweg 100b, Amsterdam","telefoon":"020-22 69 018","email":"info@huygenlammersadvocaten.nl"},
"url":"https://www.huygenlammersadvocaten.nl/fiscaal-advocaat","linktekst":"HuygenLammers Advocaten"},
{"slug":"bedrijfsfotografie-studio","naam":"Bedrijfsfotografie.nl","dienst":"Bedrijfsfotografie","plaats":"Den Haag",
"resume":"Fotografeert bedrijven, teams en zakelijke portretten, van zzp'ers tot grote organisaties.",
"specs":[("Locatie","Den Haag"),("Categorie","Bedrijfsfotografie"),("Telefoon","06 50 222 760")],
"secties":[("Eigen beeld in plaats van stockfoto's","Stockfoto's ogen generiek en zeggen weinig over hoe een bedrijf er in werkelijkheid uitziet. Bedrijfsfotografie.nl maakt beeld op locatie, van het eigen team en het eigen werk, te gebruiken op een website, bij recruitment of in een jaarverslag."),
("Zakelijke portretten op maat","Naast bedrijfsreportages levert Rogier Chang zakelijke portretten die aansluiten bij de uitstraling van een bedrijf, geschikt voor LinkedIn, een website of drukwerk. Hij fotografeert al meer dan twintig jaar bedrijven in uiteenlopende sectoren.")],
"punten":["Meer dan twintig jaar ervaring","Bedrijfsreportages en zakelijke portretten","Werkzaam vanuit Den Haag","Geschikt voor zzp'ers tot grote organisaties"],
"contact":{"adres":"Westeinde 81, Den Haag","telefoon":"06 50 222 760","email":"studio@bedrijfsfotografie.nl"},
"url":"https://www.bedrijfsfotografie.nl/bedrijfsfotograaf-den-haag/","linktekst":"Bedrijfsfotografie.nl"},
{"slug":"cloud-opslag-provider","naam":"DataOpslagNederland","dienst":"Data-opslag en back-up","plaats":"Nederlandse servers",
"resume":"Zakelijke clouddiensten op Nederlandse servers, met Nederlandstalige telefonische support.",
"specs":[("Categorie","Data-opslag en back-up"),("Locatie","Nederlandse servers"),("Telefoon","085-222 03 00")],
"secties":[("AVG-proof opslag","Bedrijven die persoonsgegevens verwerken moeten kunnen aantonen dat die gegevens passend beveiligd zijn, ook wat betreft de locatie ervan. DataOpslagNederland biedt zakelijke clouddiensten op Nederlandse servers, wat aansluit bij de AVG-eis om persoonsgegevens binnen de EU te bewaren."),
("Bescherming tegen dataverlies","Naast opslagcapaciteit is bescherming tegen ransomware een groeiend aandachtspunt: een back-up die in dezelfde omgeving staat als de actieve data kan bij een aanval alsnog verloren gaan. De dienstverlening is volledig AVG-compliant en wordt ondersteund met Nederlandstalige telefonische hulp.")],
"punten":["Opslag op Nederlandse servers","Volledig AVG-compliant","Nederlandstalige telefonische support","Gericht op zakelijke back-up en opslag"],
"contact":{"adres":None,"telefoon":"085-222 03 00","email":"info@dataopslagnederland.nl"},
"url":"https://www.dataopslagnederland.nl/cloud-opslag/","linktekst":"DataOpslagNederland"},
{"slug":"zakelijke-telefonie-centrale","naam":"PBXcomplete","dienst":"Telefonie en VoIP","plaats":"Rotterdam",
"resume":"Gespecialiseerd in dedicated VoIP-centrales, waaronder 3CX, inclusief vast-mobiel integratie.",
"specs":[("Locatie","Rotterdam"),("Categorie","Telefonie en VoIP"),("Telefoon","010-820 00 10")],
"secties":[("Bereikbaar via de cloud","Een gehoste VoIP-centrale maakt medewerkers bereikbaar op kantoor, thuis of onderweg via hetzelfde nummer, zonder de vaste hardware van een traditionele telefooncentrale. PBXcomplete richt dedicated VoIP-centrales in, waaronder 3CX, afgestemd op de situatie van het bedrijf."),
("Koppeling en flexibiliteit","Naast telefonie levert het bedrijf IP-telefoons en vast-mobiel integratie, en houdt bij de inrichting rekening met koppeling met bestaande systemen zoals een CRM of Microsoft Teams, en met de schaalbaarheid die een groeiend bedrijf nodig heeft.")],
"punten":["Dedicated VoIP-centrales, waaronder 3CX","IP-telefoons en vast-mobiel integratie","Koppeling met CRM en Microsoft Teams mogelijk","Gevestigd in Rotterdam"],
"contact":{"adres":"Bierstraat 119, Rotterdam","telefoon":"010-820 00 10","email":"info@pbxcomplete.nl"},
"url":"https://www.pbxcomplete.nl/blog/zakelijke-telefonie/","linktekst":"PBXcomplete"},
{"slug":"brandveiligheid-onderhoud","naam":"Royal Safety","dienst":"Brandveiligheid","plaats":"Oostvoorne",
"resume":"Controle en onderhoud van brandblussers volgens NEN 2559, inclusief certificering.",
"specs":[("Locatie","Oostvoorne"),("Categorie","Brandveiligheid"),("Telefoon","010-268 19 27")],
"secties":[("Wettelijke controleverplichting","Voor draagbare brandblussers geldt een controleverplichting van eens in de twee jaar, voor brandslanghaspels jaarlijks, met eens in de vijf jaar een uitgebreidere controle vanwege het risico op legionella. Royal Safety voert deze controles uit volgens NEN 2559."),
("Onderhoudscontract","Naast losse keuringen levert het bedrijf onderhoudscontracten waarbij blusmiddelen worden geleverd en de tijdige controle bewaakt wordt. De certificering is geschikt voor zowel overheidsinstanties als verzekeringsmaatschappijen.")],
"punten":["Controle volgens NEN 2559","Certificering voor overheid en verzekeraars","Ook onderhoudscontracten mogelijk","Gevestigd in Oostvoorne"],
"contact":{"adres":"Dalweg 24, Oostvoorne","telefoon":"010-268 19 27","email":"info@royalsafety.nl"},
"url":"https://www.royalsafety.nl/diensten-onderhoud/brandveiligheid/brandblusser-controle-bedrijf/","linktekst":"Royal Safety"},
{"slug":"taaltraining-werkvloer","naam":"Speak And Spoke","dienst":"Taaltraining","plaats":"Almere",
"resume":"Incompanytrainingen Nederlands NT2, Engels, Duits, Frans, Spaans en Pools, gericht op de werkvloer.",
"specs":[("Locatie","Almere"),("Categorie","Taaltraining"),("Telefoon","036-234 0487")],
"secties":[("Training op de werkvloer","In teams met meerdere nationaliteiten leidt een onduidelijke instructie sneller tot fouten, vooral in productie- en bouwomgevingen. Speak And Spoke verzorgt incompanytrainingen op locatie, gericht op de taal en situaties die daadwerkelijk in het werk voorkomen."),
("Talenaanbod","De trainingen omvatten Nederlands NT2, Engels, Duits, Frans, Spaans en Pools, opgebouwd rond een analyse van de communicatieproblemen, gevolgd door training op maat en begeleiding bij het toepassen ervan in de praktijk.")],
"punten":["Incompanytrainingen op de werkvloer","Zes talen, waaronder Nederlands NT2","Gericht op vaktermen en veiligheidsinstructies","Gevestigd in Almere"],
"contact":{"adres":"Randstad 22-46, Almere","telefoon":"036-234 0487","email":"info@speakandspoke.nl"},
"url":"https://speakandspoke.nl/","linktekst":"Speak And Spoke"},
{"slug":"bedrijfsuitje-organiseren","naam":"The Team Building","dienst":"Bedrijfsuitjes","plaats":"Utrecht",
"resume":"Escape rooms, axe throwing, karting en interactieve games voor groepen tot circa 180 personen.",
"specs":[("Locatie","Utrecht"),("Categorie","Bedrijfsuitjes"),("Telefoon","030 290 17 38")],
"secties":[("Activiteiten op één locatie","The Team Building biedt onder meer escape rooms, axe throwing, karting en interactieve games aan, geschikt voor groepen tot circa 180 personen. Alle activiteiten zijn op één locatie te combineren, met catering erbij."),
("Praktische organisatie","Gratis parkeergelegenheid en een centrale ligging in Utrecht schelen in de logistiek, zeker bij grotere groepen die vanuit verschillende plekken komen. Boekingen en vragen over dieetwensen lopen via het reserveringsadres.")],
"punten":["Groepen tot circa 180 personen","Escape rooms, axe throwing en karting","Catering op locatie","Gratis parkeren en centrale ligging"],
"contact":{"adres":"Admiraal Helfrichlaan 6, Utrecht","telefoon":"030 290 17 38","email":"boekingen@theteambuilding.nl"},
"url":"https://theteambuilding.nl/","linktekst":"The Team Building"},
{"slug":"website-laten-maken-bureau","naam":"Kraakmakend","dienst":"Webdesign","plaats":"Rotterdam",
"resume":"Full service internetbureau voor websites, webdesign, SEO-teksten en huisstijlen.",
"specs":[("Locatie","Rotterdam"),("Categorie","Webdesign"),("Telefoon","06 29 29 0 999")],
"secties":[("Meer dan alleen design","Een website die er goed uitziet maar nauwelijks vindbaar is, levert weinig op. Kraakmakend combineert webdesign met SEO-teksten en een content management systeem waarmee een bedrijf zelf teksten en pagina's kan aanpassen."),
("Aansluiten bij de huisstijl","Het bureau houdt bij nieuwe websites rekening met een bestaande huisstijl, in plaats van een standaardsjabloon te leveren. Na oplevering is een jaar ondersteuning inbegrepen.")],
"punten":["Websites, webdesign en SEO-teksten","Ook huisstijlen en drukwerk","Een jaar gratis ondersteuning na oplevering","Gevestigd in Rotterdam"],
"contact":{"adres":"Willem Buytewechstraat 45, Rotterdam","telefoon":"06 29 29 0 999","email":"info@kraakmakend.nl"},
"url":"https://kraakmakend.nl/website-laten-maken-rotterdam/","linktekst":"Kraakmakend"},
]
def bedrijf(s): return next(x for x in BEDRIJVEN if x["slug"]==s)

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
{"slug":"ondernemen-zonder-blinde-vlekken","titel":"Ondernemen zonder blinde vlekken","cat":"Ondernemen","datum":"2026-09-05","datum_nl":"5 september 2026","lees":7,
"resume":"Rechtsvorm, btw, financiering, verzekeringen, personeel en voorwaarden: zes onderwerpen die vroeg strak gezet minder herstelwerk opleveren.",
"body":[
("p","Ondernemen begint vaak met een idee, een klant en een inschrijving bij de KvK. Daarna wordt het snel minder romantisch. Je krijgt te maken met btw, aansprakelijkheid, contracten, software, verzekeringen en soms personeel. Wie die basis vroeg strak zet, voorkomt later dure reparaties."),
("p","Veel fouten ontstaan niet door slechte bedoelingen, maar door uitstel. Een offerte blijft vaag. De administratie loopt drie maanden achter. Een klant betaalt niet, terwijl er geen duidelijke voorwaarden zijn afgesproken. Zulke situaties kosten tijd op het moment dat je die juist nodig hebt voor verkoop en uitvoering."),
("h2","Ondernemen begint met zes vaste onderwerpen"),
("p","Bijna elke ondernemer raakt dezelfde zes thema\u2019s. Rechtsvorm, administratie en btw, financiering, verzekeringen, personeel en voorwaarden. De volgorde verschilt per bedrijf, maar je ontkomt er zelden aan. Een webdesigner zonder personeel heeft andere risico\u2019s dan een aannemer, maar beiden moeten facturen bewaren en afspraken vastleggen."),
("plink","De rechtsvorm komt vaak als eerste op tafel. Een eenmanszaak start snel en goedkoop, maar jij blijft priv\u00e9 aansprakelijk voor zakelijke schulden. Een bv schermt risico\u2019s beter af, al betaal je voor oprichting, administratie en vaak meer advies. De KvK geeft praktische uitleg over <a href=\"https://www.kvk.nl/starten/een-eenmanszaak-of-bv-als-rechtsvorm-kiezen/\" target=\"_blank\" rel=\"noopener\">eenmanszaak of bv kiezen</a>, maar de beste keuze hangt af van omzet, risico en plannen."),
("p","Kijk daarbij niet alleen naar belasting. Een ondernemer met \u20ac45.000 winst en weinig risico kan prima uitkomen met een eenmanszaak. Iemand die grote projecten aanneemt met schadeclaims tot tienduizenden euro\u2019s, kijkt anders naar aansprakelijkheid. Papierwerk is vervelend, maar een verkeerde rechtsvorm kan nog vervelender zijn."),
("h2","Administratie en btw: saai tot het misgaat"),
("p","Een goede administratie hoeft niet mooi te zijn. Ze moet kloppen. Bewaar facturen, bonnen, bankafschriften, contracten en urenregistraties op een plek waar je ze later terugvindt. De wettelijke bewaarplicht is in veel gevallen zeven jaar, en voor onroerend goed zelfs langer."),
("plink","Btw vraagt ritme. De meeste starters doen per kwartaal aangifte, met vaste deadlines aan het eind van de maand na dat kwartaal. Een factuur van 28 maart valt dus in het eerste kwartaal, ook als de klant pas in april betaalt. De Belastingdienst beschrijft de stappen voor <a href=\"https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw_aangifte_doen_en_betalen\" target=\"_blank\" rel=\"noopener\">btw-aangifte doen en betalen</a> en past boetes toe bij te laat indienen of betalen."),
("p","Een praktisch voorbeeld helpt. Stel dat je in april \u20ac12.100 inclusief btw factureert voor advieswerk. Daarin zit \u20ac2.100 btw die niet van jou is. Zet dat bedrag direct apart op een spaarrekening. Dan voelt de aangifte in juli minder als een onverwachte aanslag."),
("h2","Digitale basis op orde"),
("plink","Software lost geen rommel op, maar voorkomt wel veel zoekwerk. Gebruik een boekhoudpakket dat banktransacties koppelt en facturen automatisch nummert. Werk je veel op locatie, kies dan apparatuur die tegen dagelijks gebruik kan. Een betrouwbare <a href=\"https://www.computerzaak.nl/\" target=\"_blank\" rel=\"noopener\">zakelijke computerzaak</a> is dan geen luxe, maar onderdeel van je bedrijfsvoering."),
("p","Let ook op toegang en back-ups. Geef je boekhouder eigen toegang tot je pakket, niet jouw wachtwoord via WhatsApp. Sla belangrijke documenten dubbel op, bijvoorbeeld in de cloud en op een lokale schijf. Een kapotte laptop vlak voor de btw-deadline is geen sterk verhaal bij de fiscus."),
("h2","Financiering bepaalt meer dan je maandlast"),
("p","Geld ophalen klinkt aantrekkelijk, zeker als je groei ziet. Toch bepaalt financiering niet alleen hoeveel ruimte je krijgt. Ze bepaalt ook wie meepraat, welke zekerheden je geeft en hoe snel je winst moet maken. Een lening voelt anders dan een investeerder met aandelen."),
("p","Bij een banklening betaal je rente en aflossing. De bank vraagt vaak jaarcijfers, prognoses en soms priv\u00e9zekerheid. Een leverancier kan betalingstermijnen rekken, maar dan hangt je voorraad aan \u00e9\u00e9n partij. Crowdfunding werkt weer anders, omdat je met veel kleine geldgevers communiceert en publieke verwachtingen wekt."),
("p","Reken scenario\u2019s door voordat je tekent. Wat gebeurt er als omzet drie maanden 30% lager uitvalt? Kun je dan nog huur, software, aflossing en jezelf betalen? Een financieringsplan zonder tegenvallers is geen plan, maar een wens. Gebruik daarom bedragen uit offertes en contracten, niet uit je hoofd."),
("p","Eigen geld heeft ook een prijs. Stop je \u20ac20.000 spaargeld in voorraad, dan kun je dat niet gebruiken voor priv\u00e9buffer of belasting. Dat is niet per se verkeerd. Het vraagt wel om een grens. Spreek met jezelf af hoeveel je maximaal inlegt voordat je opnieuw naar het model kijkt."),
("h2","Risico\u2019s verzekeren zonder alles dicht te smeren"),
("p","Verzekeren begint met de vraag wat je zelf kunt dragen. Een kapotte telefoon van \u20ac800 is vervelend, maar niet dodelijk. Een beroepsfout van \u20ac80.000 kan je bedrijf wel omverduwen. Daarom verdienen aansprakelijkheid en arbeidsongeschiktheid vroeg aandacht."),
("p","Een bedrijfsaansprakelijkheidsverzekering dekt schade aan personen of spullen. Denk aan koffie over de laptop van een klant. Beroepsaansprakelijkheid gaat over financi\u00eble schade door jouw advies of werk. Die grens is belangrijk, want veel ondernemers denken dat \u00e9\u00e9n polis alles afdekt."),
("p","Arbeidsongeschiktheid schuiven starters vaak door. De premie voelt hoog, vooral in het eerste jaar. Toch kan \u00e9\u00e9n gebroken pols genoeg zijn om zes weken omzet te missen. Een buffer helpt, maar zes maanden vaste lasten sparen lukt niet iedereen."),
("p","Voorwaarden horen bij risicobeperking. Ze werken alleen als je ze v\u00f3\u00f3r of bij het sluiten van de overeenkomst deelt. Stuur je algemene voorwaarden pas mee met de factuur, dan ben je te laat. Zet ze daarom bij offertes, opdrachtbevestigingen en online bestellingen."),
("h2","Personeel verandert je bedrijf direct"),
("p","De eerste medewerker is meer dan extra handen. Je krijgt loonadministratie, arboverplichtingen, verzekeringen en regels rond ziekte. Bij ziekte betaal je loon meestal maximaal twee jaar door. Dat risico verrast ondernemers die alleen naar het brutoloon keken."),
("p","Reken een dienstverband breed door. Iemand met \u20ac3.000 bruto per maand kost door premies, vakantiegeld, pensioen en verzuimrisico vaak flink meer. Een vuistregel van 25% tot 35% opslag is geen gek startpunt. De exacte kosten hangen af van sector en cao."),
("p","Freelancers lijken simpeler, maar schijnzelfstandigheid blijft een risico. Werk je met vaste tijden, eigen instructies en nauwelijks ondernemersvrijheid, dan lijkt de samenwerking op loondienst. Leg de opdracht goed vast en toets hoe het werk feitelijk loopt. De praktijk weegt zwaarder dan de titel boven het contract."),
("p","Leidinggeven vraagt ook tijd. Een nieuwe collega moet worden ingewerkt, krijgt vragen en maakt fouten. Plan die uren in, vooral bij kleine teams. Anders verdwijnt je eigen productietijd en voelt groei ineens als achterstand."),
("h2","Voorwaarden en keuzes jaarlijks bijwerken"),
("p","Een onderneming staat niet stil. Omzet groeit, klanten veranderen en risico\u2019s schuiven mee. Wat in jaar \u00e9\u00e9n passend was, kan in jaar drie krap zitten. Plan daarom elk jaar een zakelijk onderhoudsmoment, net zoals je dat met je auto doet."),
("p","Loop dan zes punten langs. Past de rechtsvorm nog bij winst en risico? Klopt de administratie met de manier waarop je werkt? Zijn financieringen nog betaalbaar bij lagere omzet? Dekken verzekeringen de grootste klappen? Sluit personeelsbeleid aan op groei? En gebruiken klanten jouw voorwaarden echt?"),
("p","Zo\u2019n controle hoeft geen dik rapport op te leveren. Een lijst met tien acties is genoeg. Denk aan nieuwe voorwaarden meesturen, btw apart zetten, polisbedragen controleren of een extra back-up instellen. Kleine reparaties kosten minder dan herstel na schade."),
("p","Ondernemen blijft keuzes maken met onvolledige informatie. Niemand ziet alle risico\u2019s vooraf. Wie de zes vaste onderwerpen serieus neemt, bouwt wel rust in. Dat merk je niet alleen bij problemen, maar juist op gewone werkdagen waarop alles doorloopt."),
]},

{"slug":"buitenkant-pand-jarenlang-mooi","titel":"Zo houd je de buitenkant van je pand jarenlang mooi","cat":"Ondernemen","datum":"2026-09-03","datum_nl":"3 september 2026","lees":4,
"resume":"Een schone gevel houdt je pand jaren jonger. Ontdek vijf praktische manieren om groene aanslag voor te blijven en je buitenkant strak te houden.",
"body":[
("p","Een gevel vertelt vaak meer over een pand dan de voordeur ooit zal doen. Toch kijken de meeste mensen er pas echt naar als de groene waas al goed zichtbaar is. En dat gaat sneller dan je denkt, want op een noordmuur vormt zich in \u00e9\u00e9n vochtig seizoen al een dunne laag algen. Met een paar slimme gewoontes houd je die aanslag voor en blijft je buitenkant jarenlang strak."),
("h2","Pak groene aanslag aan voordat die zich vastzet"),
("plink","Hoe eerder je ingrijpt, hoe lichter het werk. Een dunne, verse laag algen spoel je er zo af, maar laat je mos maanden staan, dan grijpt het zich vast in de voegen en houdt het vocht tegen de steen aan. Wacht dus niet tot de hele muur groen ziet, maar reageer bij de eerste waas onderaan de gevel. Voor een grondige beurt kun je je <a href=\"https://www.actief-cleaningservices.nl/schoonmaakonderhoud/gevelreiniging/breda/\" target=\"_blank\" rel=\"noopener\">gevel laten reinigen in Breda of omgeving</a> door een specialist die de aanslag tot in de voeg weghaalt in plaats van alleen de bovenlaag. Zo begin je meteen met een schone basis."),
("h2","Kies een reinigingsmethode die bij je steen past"),
("p","De juiste techniek voorkomt dat je meer kapotmaakt dan je schoonmaakt. Hogedrukreiniging werkt snel tegen mos en algen, maar bij zachte baksteen of oude voegen kan te veel druk steen en specie wegslaan. Voor kwetsbaar metselwerk is stoomreiniging op lage druk veiliger, omdat de hitte van rond de honderdvijftig graden de sporen doodt zonder het oppervlak te forceren. Zit er ingevreten roet of graffiti op, dan is een speciale reiniger nodig die de vuillaag eerst losweekt. Laat altijd een klein proefvlak behandelen, zodat je ziet wat een methode met jouw gevel doet voordat de hele muur aan de beurt komt."),
("h2","Bescherm de gevel met een impregneerlaag"),
("plink","Na het reinigen is het moment om terugkeer van de aanslag af te remmen. Door de gevel te impregneren met een waterafstotend middel dringt regen minder diep in de steen en krijgen algen en mos veel minder houvast. Zo\u2019n laag laat de muur gewoon ademen, dus vocht van binnenuit kan nog steeds ontsnappen. Een professionele reiniging door <a href=\"https://www.actief-cleaningservices.nl/\" target=\"_blank\" rel=\"noopener\">Actief Cleaning Services</a> wordt vaak in \u00e9\u00e9n traject gecombineerd met zo\u2019n beschermlaag, waardoor het resultaat jaren langer meegaat dan bij een kale beurt. Reken op een bescherming die je vijf tot tien jaar rust geeft."),
("h2","Houd de gevel droog en vrij van begroeiing"),
("p","Vocht is de motor achter bijna alle aanslag, dus alles wat de muur droog houdt, werkt in je voordeel. Controleer of de dakgoot en regenpijpen niet lekken, want een natte streep onder een verstopte goot is een broedplaats voor algen. Snoei overhangende takken en klimop terug, zodat er meer zon en wind bij de gevel komen en die na een bui sneller opdroogt. Zorg ook dat opspattend water en bladeren zich niet onderaan de muur ophopen. Deze kleine ingrepen kosten weinig, maar ze rekken de tijd tussen twee reinigingsbeurten flink op."),
("h2","Stem het onderhoud af op de ligging en het seizoen"),
("p","Niet elke gevel vraagt hetzelfde ritme, dus kijk naar de plek voordat je een planning maakt. Een muur op het noorden of vlak bij bomen blijft langer nat en vraagt vaker aandacht dan een zonnige voorkant. Voor de meeste panden is een controle om de twee tot vijf jaar genoeg om de aanslag de baas te blijven. Loop in het najaar even langs de gevel als de bladeren vallen en het vaker regent, want juist dan zet nieuwe aanslag zich vast. Zo grijp je in op het moment dat het echt telt en niet pas als de schade zichtbaar is."),
("h2","Klaar voor een gevel die jaren mooi blijft?"),
("p","Met vroeg ingrijpen, de juiste methode, een beschermlaag en wat aandacht voor droogte houd je de buitenkant van je pand jarenlang representatief. Wil je weten wat er voor jouw gevel nodig is zonder je er zelf in te verdiepen? Vraag vrijblijvend een offerte aan en laat een vakman meekijken naar de beste aanpak."),
]},

 {"slug":'webshop-verkopen-voorbereiding','titel':'Een webshop verkopen: wat een koper als eerste opvraagt',"cat":'Ondernemen',"datum":'2026-08-19',"datum_nl":'19 augustus 2026','lees':5,
  'resume':'De waarde van een webshop wordt bepaald door wat aantoonbaar is, niet door wat er wordt verteld.',
  "body":[
  ('p', 'Bij de verkoop van een webshop struikelt het proces zelden op de prijs. Het struikelt op de vraag of de cijfers die op tafel liggen te controleren zijn.'),
  ('h2', 'Wat een koper opvraagt'),
  ('ul', ['Omzet en marge per maand over minimaal twee jaar.', 'De verdeling van de omzet over verkeerbronnen.', 'Het aandeel van de grootste leverancier en de grootste productgroep.', 'Terugkerende kosten: abonnementen, hosting, marketing, opslag.']),
  ('p', 'Vooral het derde punt bepaalt de uiteindelijke waardering. Een webshop waarvan zestig procent van de omzet uit één productgroep bij één leverancier komt, is kwetsbaarder dan dezelfde omzet uit een gespreid assortiment.'),
  ('h2', 'Afhankelijkheid van de eigenaar'),
  ('p', 'De tweede vraag die altijd komt, is hoeveel uur de eigenaar er per week in steekt en wat er gebeurt als die wegvalt. Een shop waarin de eigenaar zelf inkoopt, de klantenservice doet en de campagnes beheert, verkoopt lastiger dan een shop met vastgelegde processen.'),
  ('plink', 'Vastleggen hoe het werk gebeurt, is daarmee een concrete voorbereiding op verkoop. Een handleiding van tien pagina\'s die een opvolger op weg helpt, telt zwaarder dan de meeste verkopers verwachten. Hoe die factoren in een waardebepaling doorwerken staat bij <a href="https://www.webshopovername.nl/kennisbank/webshop-waarde-bepalen" rel="nofollow">Webshopovername</a>.'),
  ('h2', 'Het juiste moment'),
  ('p', 'Verkopen na een dalend jaar kost onvermijdelijk waarde, omdat een koper de trend doortrekt. Verkopen op het hoogtepunt van een tijdelijke hype is evenmin verstandig, omdat de koper dat doorziet en de onderbouwing dan onder druk komt.'),
  ('plink', 'Het gunstigste moment is doorgaans na twee stabiele of licht stijgende jaren, met een assortiment dat niet aan één trend hangt. Wie wil zien wat er op dit moment wordt aangeboden en tegen welke vraagprijs, vindt dat op <a href="https://www.webshopovername.nl/bedrijven-te-koop" rel="nofollow">webshopovername.nl</a>.'),
  ('h2', 'Voorbereiding in de praktijk'),
  ('p', 'Scheid privé en zakelijk in de administratie voordat de verkoop start. Kosten die deels privé zijn geboekt, maken elke marge discutabel en kosten in de onderhandeling meer dan ze ooit hebben opgeleverd.'),
  ('p', 'Zorg daarnaast dat domeinnaam, hosting, socialemedia-accounts en het merk op naam van de onderneming staan en niet op naam van een persoon of een oud-medewerker. Dat is de kleinste stap in het traject en tegelijk de meest voorkomende vertraging bij de overdracht.'),
  ('h2', 'De rol van een tussenpersoon'),
  ('p', 'Een verkoper die zelf een koper zoekt, komt vrijwel altijd uit bij zijn eigen netwerk en daarmee bij een beperkt aantal kandidaten. Dat drukt de prijs, simpelweg omdat er geen alternatief op tafel ligt om mee te vergelijken.'),
  ('p', 'Een platform of adviseur die meerdere kandidaten aandraagt, verandert die verhouding. Het kost een percentage en levert in de meeste trajecten meer op dan het kost, vooral wanneer de shop in een niche zit waarin de kopers niet vanzelf te vinden zijn.'),
  ("p", DISC),
 ]},
{"slug":"fysiotherapie-maastricht-eerste-afspraak","titel":"Fysiotherapie in Maastricht: wat te weten is voor een eerste afspraak","cat":"Gezondheid","datum":"2026-08-12","datum_nl":"12 augustus 2026","lees":3,
"resume":"Wachten tot een klacht vanzelf overgaat werkt zelden; een gerichte eerste afspraak legt de basis voor een structurele aanpak.",
"body":[("p","Ondernemers zijn gewend om door te zetten. Deadlines, vergaderingen en lange werkdagen achter een scherm vragen veel van het lichaam, dat zich aanpast totdat het dat niet meer doet. Een hardnekkige nekklacht, een schouder die niet meer soepel beweegt of rugpijn die de concentratie breekt, zijn signalen die niet genegeerd kunnen blijven. Fysiotherapie is dan geen luxe, maar een praktische stap."),
("h2","Wanneer fysiotherapie zinvol is"),("p","Veel mensen wachten te lang voordat ze naar een fysiotherapeut gaan. Ze verwachten dat klachten vanzelf overgaan, maar bij overbelasting of een scheve houding door jarenlang bureauwerk is dat zelden het geval. Een fysiotherapeut kijkt niet alleen naar het pijnpunt zelf, maar naar de bewegingspatronen die eraan ten grondslag liggen. Zo wordt een terugkerend probleem structureel aangepakt in plaats van tijdelijk gestild."),
("h2","Wat te verwachten is bij een eerste afspraak"),("p","Tijdens het eerste consult worden de klachten besproken en voert de fysiotherapeut een lichamelijk onderzoek uit. Denk aan houdingsanalyse, bewegingstests en gerichte vragen over dagelijkse activiteiten. Op basis daarvan wordt een behandelplan opgesteld. Bij klachten die voortkomen uit een zittend beroep, zoals chronische nekspanning of een bekkenkanteling, zijn vijf tot acht sessies gemiddeld voldoende om merkbare verbetering te boeken, mits de oefeningen thuis ook worden uitgevoerd."),
("h2","Fysiotherapie in Maastricht vinden"),("plink","Maastricht heeft een behoorlijk aanbod aan fysiotherapiepraktijken, maar de kwaliteit en specialisatie verschilt. Voor wie op zoek is naar een praktijk die werkt met evidence-based methoden en ook sportrevalidatie aanbiedt, is het de moeite waard om gericht te zoeken. <a href=\"https://www.physio-health.nl/\" target=\"_blank\" rel=\"noopener\">Physio Health Maastricht</a> is een praktijk waar zowel reguliere fysiotherapie als specifiekere trajecten zoals manuele therapie en dry needling worden aangeboden. Dat maakt het een geschikte keuze bij klachten die wat complexer zijn dan een doorsnee spierpijn."),
("h2","Verzekering en vergoeding"),("p","Fysiotherapie valt niet meer automatisch in het basispakket. Vanaf de achttiende behandeling in een kalenderjaar wordt bij niet-chronische klachten doorgaans zelf betaald. Bij een aanvullende verzekering bestaat recht op een bepaald aantal sessies per jaar, afhankelijk van het pakket. Vooraf navragen voorkomt verrassingen. Bij chronische aandoeningen die op de lijst van het Zorginstituut staan, worden de eerste twintig sessies wel vergoed vanuit de basisverzekering."),
("h2","Preventie loont meer dan herstel"),("p","De meest onderschatte aanpak is preventief: naar de fysiotherapeut gaan voordat klachten echt spelen. Een screeningsafspraak per jaar, waarbij een professional houding en bewegingspatroon beoordeelt, voorkomt dat kleine onbalansen uitgroeien tot slopende klachten. Zeker bij regelmatig lang zitten, zwaar tillen of intensief sporten is zo'n preventief consult geen overbodige luxe, maar slim onderhoud van het lichaam.")]},
{"slug":"lichaam-opknappen-assen-fysiotherapie","titel":"Het lichaam laten opknappen in Assen: wat vooraf te weten","cat":"Gezondheid","datum":"2026-08-12","datum_nl":"12 augustus 2026","lees":3,
"resume":"Een lichte klacht negeren kost uiteindelijk meer tijd dan hem meteen laten behandelen.",
"body":[("p","Ondernemers hebben hun lichaam gewoon nodig. Een week met rugpijn betekent afspraken verzetten, klussen die uitlopen of klanten die wachten. Als er iets hapert, zoals een stijve nek, een knie die opspeelt of een schouder die niet meer wil, is snel en goed ingrijpen gewenst, zonder maandenlang aanmodderen."),
("h2","Wat Refix doet"),("p","Refix is een fysiotherapiepraktijk die klachten aan spieren, gewrichten en pezen behandelt. Denk aan manuele therapie voor een vastzittende rug of nek, sportfysiotherapie na overbelasting tijdens het hardlopen, en revalidatie na een blessure of operatie. In plaats van alleen de pijn te dempen, wordt gekeken naar de oorzaak. Bij een houding die de hele dag voorovergebogen achter een laptop doorbrengt, wordt niet alleen de nek behandeld maar ook de houding onder handen genomen, zodat de klacht niet blijft terugkomen."),
("h2","Behandelen zonder gedoe met de verzekering"),("p","Fysiotherapie zit meestal in de aanvullende verzekering, maar het aantal behandelingen dat vergoed wordt verschilt flink per pakket. Sommige langdurige klachten vallen onder de chronische lijst en worden dan grotendeels vergoed, terwijl een simpele nekklacht vaak uit de aanvullende dekking wordt betaald. Refix helpt vooraf uitzoeken wat in een individueel geval vergoed wordt, zodat een onverwachte rekening halverwege een traject wordt voorkomen."),
("h2","Snel geholpen in Assen"),("plink","Voor de regio is het handig om te weten dat bij <a href=\"https://refix.nl/locaties/assen/\" target=\"_blank\" rel=\"noopener\">Refix Assen</a> fysiotherapie mogelijk is zonder lange wachttijd. Een eerste afspraak is vaak snel te plannen, en de behandeltijden zijn ruim genoeg om ook buiten werkuren langs te komen. Zo blijft herstel mogelijk zonder de agenda leeg te hoeven maken."),
("h2","Een kleine klacht, grote gevolgen bij wachten"),("p","Een lichte pijn in knie of schouder lijkt onschuldig, waardoor er anders wordt bewogen om het lichaamsdeel te ontzien. Precies daar zit het gevaar: door dat compenseren worden andere spieren en gewrichten verkeerd belast, en voor het bekend is, ontstaat er een tweede klacht. Wat als een sessie had gekund, wordt dan een langdurig traject. Vroeg langsgaan is bijna altijd sneller en goedkoper dan wachten tot normaal bewegen nauwelijks nog lukt."),
("h2","Een tip die weinig bekend is"),("p","Navragen bij de eerste afspraak of de fysiotherapeut een nulmeting doet van kracht of beweeglijkheid, levert concrete cijfers als startpunt op. Een paar weken later is zwart-op-wit te zien hoeveel vooruitgang er is geboekt, wat beter werkt dan welke aansporing dan ook om de oefeningen thuis vol te houden. Herstel voelt vaak traag, maar meetbaar bewijs dat het wel opschiet, houdt de motivatie vast tot volledig herstel.")]},
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
def tile_bedrijf(b):
    return f"""<a class="tile" href="/bedrijven/{b['slug']}/"><h3>{esc(b['naam'])}</h3><p>{esc(b['resume'][:96].rsplit(' ',1)[0])}...</p></a>"""
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
<div class="section-head"><span class="eyebrow">{IC['case']}Bedrijvengids</span><h2>Aanbevolen bedrijven</h2>
<p class="lead">Een selectie van bedrijven die relevante diensten en producten leveren aan ondernemers, gekozen op relevantie en niet op betaling.</p></div>
<div class="grid cols-3">{"".join(tile_bedrijf(b) for b in BEDRIJVEN[:6])}</div>
<p style="margin-top:22px"><a class="more" href="/bedrijven/">Alle bedrijven bekijken {IC['arrow']}</a></p></div></section>

<section class="section"><div class="wrap">
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

def p_bedrijven_index():
    path="/bedrijven/"; c=[("Home","/"),("Bedrijven",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Bedrijven","inLanguage":"nl-NL"},
    {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":b["naam"],"url":BASE+f"/bedrijven/{b['slug']}/"} for i,b in enumerate(BEDRIJVEN)]},crumb(c)]
    h=head("Bedrijvengids | dienstverleners voor ondernemers | "+SITE,"Een gids met bedrijven die relevante diensten en producten leveren aan ondernemers, van bedrijfsovername tot webdesign.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['case']}Bedrijvengids</span>
<h1>Bedrijven</h1><p class="lead">Een selectie van bedrijven die relevante diensten en producten leveren aan ondernemers, gekozen op relevantie en niet op betaling.</p></div>
<div class="grid cols-3">{"".join(tile_bedrijf(b) for b in BEDRIJVEN)}</div></div></section>"""
    write(path,h+footer())

def p_bedrijf(b):
    path=f"/bedrijven/{b['slug']}/"; c=[("Home","/"),("Bedrijven","/bedrijven/"),(b["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"LocalBusiness","@id":BASE+path,"name":b["naam"],"description":b["resume"],
    "telephone":b["contact"]["telefoon"],"email":b["contact"]["email"],"url":b["url"]},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in b["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in b["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in b["punten"])
    rows=[("Adres",b["contact"].get("adres")),("Telefoon",b["contact"]["telefoon"]),("E-mail",b["contact"]["email"])]
    contact_rows="".join(f"<p style=\"margin:.3em 0\">{esc(l)}: {esc(v)}</p>" for l,v in rows if v)
    anders=[x for x in BEDRIJVEN if x["slug"]!=b["slug"]][:3]
    h=head(f"{b['naam']} | {b['dienst']} | {SITE}", b["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose"><span class="eyebrow">{IC['case']}Bedrijvengids</span>
<h1>{esc(b['naam'])}</h1><p class="lead">{esc(b['resume'])}</p></div>
<div class="wrap"><dl class="specs">{sp}</dl></div>
<div class="wrap prose">{sec}<h2>In het kort</h2><ul class="ticks" style="margin-bottom:16px">{pt}</ul>
<div class="callout"><p><strong>Contactgegevens</strong></p>{contact_rows}<p style="margin-top:10px"><a class="btn btn-plum" href="{b['url']}" target="_blank" rel="noopener">{esc(b['linktekst'])} {IC['arrow']}</a></p></div></div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Andere bedrijven</h2></div>
<div class="grid cols-3">{"".join(tile_bedrijf(x) for x in anders)}</div></div></section>"""
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

def p_partners():
    path="/partners/"; c=[("Home","/"),("Partners",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Partners","inLanguage":"nl-NL"}]
    h=head("Partners | "+SITE,"Partners en bronnen waar De 6 voor Ondernemers naar verwijst.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">Partners</span><h1>Partners en bronnen</h1>
<p class="lead">De 6 voor Ondernemers verwijst hier naar externe partners en bronnen.</p>
<div class="grid" style="grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px">
<div class="card"><h3>Van der Zwaard</h3><p>Van der Zwaard is een accountants- en belastingadvieskantoor in Den Haag, met dienstverlening voor ondernemers op het gebied van boekhouding, administratie en belastingadvies.</p><p style="margin-top:10px"><a href="https://www.vanderzwaard.nl/diensten/belastingadvies/" target="_blank" rel="noopener">belastingconsulent den haag</a></p></div>
<div class="card"><h3>DLSA Letselschade Advocaten</h3><p>DLSA is gespecialiseerd in letselschade, onder meer voor (oud-)militairen met gezondheidsklachten door chroom-6 of PTSS, en begeleidt schadeclaims tegen Defensie.</p><p style="margin-top:10px"><a href="https://dlsa.nl/ptss-veteranen/" target="_blank" rel="noopener">veteranen met ptss</a></p></div>
<div class="card"><h3>Stofzakkie</h3><p>Stofzakkie is een webshop voor stofzuigerzakken en stofzuigeraccessoires, geschikt voor uiteenlopende merken en typen stofzuigers.</p><p style="margin-top:10px"><a href="https://www.stofzakkie.nl/" target="_blank" rel="noopener">Stofzakkie</a></p></div>
<div class="card"><h3>CF Kunststofprofielen</h3><p>CF Kunststofprofielen levert kunststof profielen voor diverse toepassingen, waaronder kamerprofielen voor het afwerken van wanden en plafonds.</p><p style="margin-top:10px"><a href="https://www.cf-kunststofprofielen.nl/profielen/kamerprofielen" target="_blank" rel="noopener">kamerprofiel</a></p></div>
<div class="card"><h3>LeadToday</h3><p>LeadToday is een Nederlands online marketing bureau dat mkb-bedrijven ondersteunt met leadgeneratie, SEO en online adverteren.</p><p style="margin-top:10px"><a href="https://www.leadtoday.nl/online-marketing-bureau-rotterdam" target="_blank" rel="noopener">online marketing bureau rotterdam</a></p></div>
<div class="card"><h3>FinanceFactor</h3><p>FinanceFactor is gespecialiseerd in executive search binnen finance, en bemiddelt tussen bedrijven en ervaren financiële professionals.</p><p style="margin-top:10px"><a href="https://www.financefactor.nl/" target="_blank" rel="noopener">executive search finance</a></p></div>
<div class="card"><h3>Officetrader</h3><p>Officetrader verzorgt bedrijfsontruimingen, waarbij kantoren en bedrijfspanden compleet en efficiënt worden leeggemaakt.</p><p style="margin-top:10px"><a href="https://officetrader.nl/bedrijfsontruimingen/" target="_blank" rel="noopener">Bedrijfsontruiming - Officetrader</a></p></div> <div class="card"><h3>Horecarama</h3><p>Horecarama levert klein materiaal voor de horeca, waaronder voedselbakken en -dozen voor opslag en transport.</p><p style="margin-top:10px"><a href="https://www.horecarama.nl/klein-materiaal/voedsel-bakken-en-dozen/plastic-bakjes/" target="_blank" rel="noopener">Plastic bakjes</a></p></div> <div class="card"><h3>Milieustickerkopen</h3><p>Milieustickerkopen.nl helpt automobilisten aan de juiste milieusticker voor het rijden in Duitse milieuzones.</p><p style="margin-top:10px"><a href="https://milieustickerkopen.nl/e-plakette-duitsland" target="_blank" rel="noopener">E-plakette Duitsland</a></p></div> <div class="card"><h3>Mokken.nl</h3><p>Mokken.nl is een webshop voor mokken, waaronder gepersonaliseerde varianten met een naam erop.</p><p style="margin-top:10px"><a href="https://www.mokken.nl/mokken-met-naam" target="_blank" rel="noopener">mok met naam</a></p></div> <div class="card"><h3>Aanstekers.nl</h3><p>Aanstekers.nl levert bedrukte aanstekers voor promotionele doeleinden, waaronder het Atomic-model.</p><p style="margin-top:10px"><a href="https://www.aanstekers.nl/atomic-aanstekers-bedrukken" target="_blank" rel="noopener">Atomic aanstekers</a></p></div> <div class="card"><h3>Tankgigant</h3><p>Tankgigant is gespecialiseerd in watertanks voor opslag en transport van water, voor zowel particulier als zakelijk gebruik.</p><p style="margin-top:10px"><a href="https://www.tankgigant.nl/" target="_blank" rel="noopener">watertanks</a></p></div> <div class="card"><h3>Werkspoorraakt</h3><p>Werkspoorraakt biedt flexibele kantoorruimtes aan, onder meer voor ondernemers die kantoorruimte huren in Utrecht.</p><p style="margin-top:10px"><a href="https://www.werkspoorraakt.nl/kantoor-utrecht/" target="_blank" rel="noopener">kantoorruimte huren in Utrecht</a></p></div> <div class="card"><h3>Huissteden</h3><p>Huissteden levert accessoires en onderdelen voor naaimachines, waaronder het Janome voetpedaal.</p><p style="margin-top:10px"><a href="https://www.huissteden.nl/accessoires-onderdelen/naaimachines-accessoires/voetpedalen/janome-voetpedaal-voor-naaimachines" target="_blank" rel="noopener">Janome voetpedaal</a></p></div> <div class="card"><h3>Lindenhaeghe</h3><p>Lindenhaeghe verzorgt opleidingen in de financiële sector, waaronder de basisopleiding Wft.</p><p style="margin-top:10px"><a href="https://lindenhaeghe.nl/wft/basis" target="_blank" rel="noopener">Wft Basis</a></p></div> <div class="card"><h3>Certify360</h3><p>Certify360 is actief in opleiding en certificering en biedt trajecten aan voor professionals in diverse sectoren.</p><p style="margin-top:10px"><a href="https://certify360.com" target="_blank" rel="noopener">certify360</a></p></div> <div class="card"><h3>Elan Notarissen</h3><p>Elan Notarissen heeft meerdere vestigingen in Nederland, waaronder een notaris in Harlingen.</p><p style="margin-top:10px"><a href="https://elannotarissen.nl/vestigingen/erica-heeres-harlingen/" target="_blank" rel="noopener">Notaris Harlingen</a></p></div> <div class="card"><h3>Goodzo</h3><p>Goodzo ondersteunt bedrijven bij IT-outsourcing, waaronder het uitbesteden van applicatiebeheer.</p><p style="margin-top:10px"><a href="https://www.goodzo.nl/outsourcing/applicatie-beheer" target="_blank" rel="noopener">applicatie beheer uitbesteden</a></p></div> <div class="card"><h3>Care-IS</h3><p>Care-IS vergelijkt vermogensbeheerders in Nederland, waaronder Wierda vermogensbeheer.</p><p style="margin-top:10px"><a href="https://care-is.nl/vermogensbeheer/vergelijken/wierda-vermogensbeheer/" target="_blank" rel="noopener">Wierda vermogensbeheer</a></p></div> <div class="card"><h3>Ondernemersklankbord</h3><p>Ondernemersklankbord begeleidt ondernemers met advies van ervaren vakgenoten, onder meer bij het verkopen van een bedrijf.</p><p style="margin-top:10px"><a href="https://ondernemersklankbord.nl/bedrijf-verkopen/" target="_blank" rel="noopener">bedrijf verkopen</a></p></div> <div class="card"><h3>Increasy</h3><p>Increasy biedt white label linkbuilding aan voor bureaus die linkbuilding voor hun klanten willen uitbesteden.</p><p style="margin-top:10px"><a href="https://increasy.nl/white-label-linkbuilding/" target="_blank" rel="noopener">White label linkbuilding</a></p></div> <div class="card"><h3>Linkbuilding Specialist</h3><p>Linkbuilding Specialist helpt bedrijven die linkbuilding willen uitbesteden aan een gespecialiseerd bureau.</p><p style="margin-top:10px"><a href="https://linkbuilding-specialist.nl/linkbuilding-uitbesteden/" target="_blank" rel="noopener">Linkbuilding uitbesteden</a></p></div> <div class="card"><h3>BJZ.nu</h3><p>BJZ.nu is een online vacatureplatform voor juridische functies, van advocatuur tot bedrijfsjurist.</p><p style="margin-top:10px"><a href="https://www.bjz.nu/" target="_blank" rel="noopener">BJZ.nu</a></p></div>
</div>
</div></section>"""
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
    u=["/","/over/","/redactie/","/onderwerpen/","/gidsen/","/bedrijven/","/nieuws/","/partners/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/onderwerpen/{s['slug']}/" for s in ONDERWERPEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/bedrijven/{b['slug']}/" for b in BEDRIJVEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f" <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n Cache-Control: public, max-age=31536000, immutable\n/*\n X-Content-Type-Options: nosniff\n Referrer-Policy: strict-origin-when-cross-origin\n")
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
    p_bedrijven_index()
    for b in BEDRIJVEN: p_bedrijf(b)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_partners(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
