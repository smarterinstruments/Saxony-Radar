import json, re
d=json.load(open('data/radar_sx.json'))
L=open('tools/template.html',encoding='utf-8').read().split('\n')
def idx(prefix,start=0):
    for i in range(start,len(L)):
        if L[i].startswith(prefix): return i
    raise SystemExit('missing '+prefix)
ics,ien,ide=idx('  cs: {'),idx('  en: {'),idx('  de: {')
ABOUT={'cs':[
 ['Co radar sleduje','Veřejné aktivity firem a institucí saského polovodičového ekosystému: nové produkty a technologie, investice a expanze, projekty a granty, akce, partnerství, ocenění a změny ve vedení. Náhled připravil CNSC pro Silicon Saxony v rámci memoranda o spolupráci z 12. 11. 2026.'],
 ['Odkud data pocházejí','Seznam organizací vychází z veřejného adresáře členů Silicon Saxony (734 profilů, z nich 480 patří do mikroelektronického hodnotového řetězce), doplněného rešerší CNSC ve veřejných zdrojích. Zařazení do segmentů taxonomie CNSC je pracovní: u každé organizace je uvedena jistota zařazení a čeká se na potvrzení Silicon Saxony.'],
 ['Jak číst radar','Výseče jsou segmenty hodnotového řetězce, prstence čerstvost: tento týden (do 7 dnů) a tento měsíc (8–31 dnů). Stupeň říká jen to, kdy jsme naposledy zaznamenali veřejnou aktivitu; není to hodnocení firmy. Filtr Segment v záložce Firmy umožňuje vybrat jednotlivé kódy taxonomie včetně podsegmentů 2.4.1–2.4.6.'],
 ['Stav náhledu','Aktivity jsou zatím sebrány z veřejných LinkedIn stránek a YouTube kanálů vybraných firem a institucí (sběr 15.–16. 11. 2026); YouTube kanály čteme přes veřejné RSS feedy, takže jdou sledovat automaticky každý týden; týdenní podcast Silicon Saxony „What\'s Chippening“ vedeme jako stálý zdroj, každý díl je jedna položka s odkazy na zmíněné saské organizace; u skupinových stránek (Infineon, GlobalFoundries, Bosch) jde o zprávy celé skupiny. U ostatních organizací sběr teprve začíná, proto jsou vedeny bez sledované aktivity.'],
 ['Co tu není','Interní informace klastrů, obchodně citlivé údaje firem a osobní údaje kontaktních osob. Radar pracuje jen s veřejnými informacemi. Opravy a doplnění: info@semicz.cz, předmět „Radar Sasko“.']],
'de':[
 ['Was der Radar erfasst','Öffentliche Aktivitäten von Unternehmen und Instituten des sächsischen Halbleiter-Ökosystems: neue Produkte und Technologien, Investitionen und Erweiterungen, Projekte und Förderungen, Veranstaltungen, Partnerschaften, Auszeichnungen und Führungswechsel. Die Vorschau hat CNSC für Silicon Saxony im Rahmen der Absichtserklärung vom 12. 11. 2026 erstellt.'],
 ['Woher die Daten stammen','Die Liste der Organisationen stammt aus dem öffentlichen Mitgliederverzeichnis von Silicon Saxony (734 Profile, davon 480 in der Mikroelektronik-Wertschöpfungskette), ergänzt durch CNSC-Recherchen in öffentlichen Quellen. Die Zuordnung zu den Segmenten der CNSC-Taxonomie ist vorläufig: Jede Organisation trägt eine Sicherheitsstufe der Zuordnung und wartet auf die Bestätigung durch Silicon Saxony.'],
 ['Wie der Radar zu lesen ist','Die Sektoren sind Segmente der Wertschöpfungskette, die Ringe zeigen die Aktualität: diese Woche (bis 7 Tage) und diesen Monat (8–31 Tage). Die Stufe sagt nur, wann wir zuletzt eine öffentliche Aktivität erfasst haben; sie ist keine Bewertung des Unternehmens. Der Filter Segment im Reiter Unternehmen wählt einzelne Taxonomie-Codes aus, einschließlich der Untersegmente 2.4.1–2.4.6.'],
 ['Stand der Vorschau','Aktivitäten wurden bisher von den öffentlichen LinkedIn-Seiten und YouTube-Kanälen ausgewählter Unternehmen und Institute erfasst (Stand 15.–16. 11. 2026); YouTube-Kanäle werden über ihre öffentlichen RSS-Feeds gelesen und lassen sich so wöchentlich automatisch verfolgen; der wöchentliche Silicon-Saxony-Podcast „What\'s Chippening“ ist eine ständige Quelle, jede Folge ein Eintrag mit Verweisen auf die genannten sächsischen Organisationen; bei Konzernseiten (Infineon, GlobalFoundries, Bosch) handelt es sich um Konzernmeldungen. Für die übrigen Organisationen beginnt die Erfassung erst, deshalb erscheinen sie ohne erfasste Aktivität.'],
 ['Was hier nicht steht','Interne Informationen der Cluster, geschäftlich sensible Unternehmensdaten und personenbezogene Daten von Ansprechpartnern. Der Radar arbeitet ausschließlich mit öffentlichen Informationen. Korrekturen und Ergänzungen: info@semicz.cz, Betreff „Radar Sachsen“.']],
'en':[
 ['What the radar tracks','Public activities of companies and institutes in the Saxon semiconductor ecosystem: new products and technologies, investments and expansion, projects and grants, events, partnerships, awards and leadership changes. The preview was prepared by CNSC for Silicon Saxony under the memorandum of understanding of 12 Nov 2026.'],
 ['Where the data comes from','The organisation list comes from the public Silicon Saxony member directory (734 profiles, 480 of them in the microelectronics value chain), complemented by CNSC research in public sources. CNSC taxonomy segments are provisional: each organisation carries a confidence level and awaits confirmation by Silicon Saxony.'],
 ['How to read the radar','Sectors are value-chain segments, rings show freshness: this week (up to 7 days) and this month (8–31 days). The level only says when we last recorded public activity; it is not a rating of the company. The Segment filter in the Companies tab selects individual taxonomy codes, including the sub-segments 2.4.1–2.4.6.'],
 ['Status of the preview','Activities have so far been collected from the public LinkedIn pages and YouTube channels of selected companies and institutes (collected 15–16 Nov 2026); YouTube channels are read through their public RSS feeds, so they can be tracked automatically every week; Silicon Saxony\'s weekly podcast “What\'s Chippening” is a standing source, each episode is one item linked to the Saxon organisations it mentions; for group pages (Infineon, GlobalFoundries, Bosch) the items are group news. Collection for the other organisations is only starting, so they are shown without tracked activity.'],
 ['What is not here','Internal cluster information, commercially sensitive company data and personal data of contact persons. The radar works with public information only. Corrections and additions: info@semicz.cz, subject “Radar Saxony”.']]}
CS=[('Radar aktivit členů','Radar hodnotového řetězce'),('členů klastru','organizací saského ekosystému'),('v 8 segmentech hodnotového řetězce','v 10 segmentech hodnotového řetězce'),('každý bod je jeden člen s','každý bod je jedna firma s'),('jeden člen; popisek','jedna firma; popisek'),('zatím žádný člen','zatím žádná firma'),('firemní stránky členů na LinkedIn, weby členů, semicz.cz; stupeň není hodnocení člena','firemní stránky na LinkedIn, weby firem, tisk; stupeň není hodnocení firmy'),('Kmenová data z katalogu klastru a semicz.cz.','Kmenová data z veřejného adresáře členů Silicon Saxony a rešerše CNSC; zařazení čeká na potvrzení Silicon Saxony.'),('Členové','Firmy'),('členové','firmy'),('členů','firem'),('člena','firmy'),('členy','firmy'),('členech','firmách'),('člen ','firma '),('člen','firma')]
EN=[('Member Activity Radar','Semiconductor Value Chain Radar'),('Member activity radar','Value chain radar'),('cluster members','organisations in the Saxon ecosystem'),('in 8 value-chain segments','in 10 value-chain segments'),('members’ LinkedIn company pages, member websites, semicz.cz; the level is not a rating of the member','LinkedIn company pages, company websites, press; the level is not a rating of the company'),('Master data from the cluster catalogue and semicz.cz.','Master data from the public Silicon Saxony member directory and CNSC research; segments await confirmation by Silicon Saxony.'),('Members','Companies'),('members','companies'),('Member','Company'),('member','company')]
DE=[('Radar der Mitgliederaktivitäten','Radar der Halbleiter-Wertschöpfungskette'),('Clustermitglieder','Organisationen im sächsischen Ökosystem'),('in 8 Segmenten der Wertschöpfungskette','in 10 Segmenten der Wertschöpfungskette'),('jeder Punkt ist ein Mitglied mit','jeder Punkt ist ein Unternehmen mit'),('ein Mitglied; ','ein Unternehmen; '),('noch kein Mitglied','noch kein Unternehmen'),('Stammdaten aus dem Clusterkatalog und semicz.cz.','Stammdaten aus dem öffentlichen Mitgliederverzeichnis von Silicon Saxony und CNSC-Recherche; die Zuordnung wartet auf die Bestätigung durch Silicon Saxony.'),('LinkedIn-Unternehmensseiten der Mitglieder, Websites der Mitglieder, semicz.cz; die Stufe ist keine Bewertung des Mitglieds','LinkedIn-Unternehmensseiten, Websites der Unternehmen, Presse; die Stufe ist keine Bewertung des Unternehmens'),('Mitgliedern','Unternehmen'),('Mitglieder','Unternehmen'),('Mitglieds','Unternehmens'),('Mitglied','Unternehmen')]
def patch(a,b,pairs,lang):
    ia=next(i for i in range(a,b) if L[i].lstrip().startswith('about:['))
    ib=next(i for i in range(ia,b+1) if L[i].lstrip().startswith(']}'))
    for i in range(a,ia):
        def rep(m):
            s=m.group(0)
            for x,y in pairs: s=s.replace(x,y)
            return s
        L[i]=re.sub(r"'(?:[^'\\]|\\.)*'",rep,L[i])
        L[i]=re.sub(r"tabs:\[('[^']*'),('[^']*'),('[^']*'),('[^']*'),('[^']*'),('[^']*')\]",r"tabs:[\1,\2,\3,\5,\6]",L[i])
    js="       about:[\n"+",\n".join("        "+json.dumps(x,ensure_ascii=False) for x in ABOUT[lang])+"\n"
    return ia,ib,js
ia,ib,js=patch(ide,idx('  nl: {'),DE,'de'); L[ia:ib]=[js.rstrip('\n')]
ia,ib,js=patch(ien,ide,EN,'en'); L[ia:ib]=[js.rstrip('\n')]
ia,ib,js=patch(ics,idx('  en: {'),CS,'cs'); L[ia:ib]=[js.rstrip('\n')]
T='\n'.join(L)
rep=[("<title>CNSC Member Activity Radar</title>","<title>Semiconductor Value Chain Radar – Saxony preview</title>"),
("localStorage.getItem('cnsc-radar-lang'); if (['en','de','zh','nl'].includes(_l))","localStorage.getItem('sx-radar-lang'); if (['en','cs'].includes(_l))"),
("if (['en','de','zh','nl'].includes(_h0))","if (['en','cs'].includes(_h0))"),
("[['cs','CZ'],['en','EN'],['de','DE'],['nl','NL'],['zh','中文']]","[['de','DE'],['en','EN'],['cs','CZ']]"),
("['cs','en','de','nl','zh'].forEach","['de','en','cs'].forEach"),
("['overview','news','members','centres','events','about']","['overview','map','news','members','events','about']"),
("if (['news','members','centres','events','about'].includes(hash))","if (['map','news','members','centres','events','about'].includes(hash))"),
("subject=CNSC%20Radar%20%E2%80%93%20zp%C4%9Btn%C3%A1%20vazba","subject=Radar%20hodnotov%C3%A9ho%20%C5%99et%C4%9Bzce%20%E2%80%93%20zp%C4%9Btn%C3%A1%20vazba")]
for a,b in rep:
    assert a in T, a[:60]
    T=T.replace(a,b)
T=T.replace("'cnsc-radar-lang'","'sx-radar-lang'")
assert "let LANG = 'cs'" in T
T=T.replace("let LANG = 'cs'","let LANG = 'de'",1)
assert '</style>' in T
T=T.replace('</style>',':root{--seg-software:var(--seg-apps);--seg-metrology:var(--seg-test);--seg-subsystems:var(--seg-eco);--seg-distribution:var(--seg-research);--seg-downstream:#64748B;--seg-ecosystem:#0891B2}\n</style>',1)

CARD='<div class="card" id="member-${m.id}"'
assert CARD in T
T=T.replace(CARD,'<div class="card" data-cc="${esc(m.code||\'\')}" id="member-${m.id}"')
JS="""
;(function(){
  let CC='';
  function apply(){
    document.querySelectorAll('#memberList .card').forEach(c=>{const v=c.dataset.cc||'';c.style.display=(!CC||v===CC||(CC==='2.4'&&v.startsWith('2.4')))?'':'none';});
    document.querySelectorAll('#memberList .stage').forEach(s=>{const n=[...s.querySelectorAll('.card')].filter(c=>c.style.display!=='none').length;s.style.display=n?'':'none';const sc=s.querySelector('.sc');if(sc&&sc.textContent!==String(n))sc.textContent=n;});
  }
  function ui(){
    const list=$('memberList');if(!list)return;
    let bar=$('ccBar');if(!bar){bar=document.createElement('div');bar.id='ccBar';bar.style.cssText='margin:0 0 14px;font:500 14px Inter,sans-serif';list.parentNode.insertBefore(bar,list);}
    const en=LANG==='en';
    const codes={};D.members.forEach(m=>{codes[m.code]=(codes[m.code]||0)+1});
    const order=Object.keys(codes).sort((a,b)=>a.localeCompare(b,undefined,{numeric:true}));
    const nm=c=>{const m=D.members.find(x=>x.code===c);const t=(m?(LANG==='de'?m.de:en?m.en:m.cs):'').replace(/^[^ ]+ /,'').split(' (')[0];return c+' '+t;};
    bar.innerHTML='<label>'+(en?'Segment: ':'Segment: ')+'<select id="ccSel" style="font:inherit;padding:6px 10px;border-radius:8px;border:1px solid var(--line);background:transparent;color:inherit;max-width:100%"><option value="">'+(LANG==='de'?'Alle':en?'All':'Všechny')+' ('+D.members.length+')</option><option value="2.4"'+(CC==='2.4'?' selected':'')+'>2.4 '+(LANG==='de'?'Subsysteme und Komponenten (alle)':en?'Subsystems and components (all)':'Subsystémy a komponenty (vše)')+' ('+order.filter(c=>c.startsWith('2.4')).reduce((a,c)=>a+codes[c],0)+')</option>'+order.map(c=>'<option value="'+c+'"'+(c===CC?' selected':'')+'>'+esc(nm(c))+' ('+codes[c]+')</option>').join('')+'</select></label>';
    $('ccSel').onchange=e=>{CC=e.target.value;apply();};
    apply();
  }
  const ml=$('memberList');
  if(ml){new MutationObserver(()=>ui()).observe(ml,{childList:true});ui();}
})();
"""
k=T.rindex('</script>')
T=T[:k]+JS+T[k:]
dump=lambda v: json.dumps(v,ensure_ascii=False)
parts=[];keys=list(d.keys())
for i,k in enumerate(keys):
    v=d[k];end=',' if i<len(keys)-1 else ''
    if isinstance(v,list): parts.append(f'  {dump(k)}: [\n'+',\n'.join(f'    {dump(x)}' for x in v)+f'\n  ]{end}')
    else: parts.append(f'  {dump(k)}: {dump(v)}{end}')
body=('{\n'+'\n'.join(parts)+'\n}').replace('</','<\\/')

# ---- German text for news, events and cards ----
for a,c in [("L({cs: n.cs, en: n.en})","L({cs:n.cs,en:n.en,de:n.de})"),("L({cs:m.cs,en:m.en})","L({cs:m.cs,en:m.en,de:m.de})"),("L({cs:e.cs, en:e.en})","L({cs:e.cs,en:e.en,de:e.de})"),("L({cs:n.cs,en:n.en})","L({cs:n.cs,en:n.en,de:n.de})")]:
    assert a in T, a
    T=T.replace(a,c)
# ---- Silicon Saxony membership badge on cards ----
OLD_P0="`<p>${esc(L({cs:m.cs,en:m.en,de:m.de}))}</p>`"
assert OLD_P0 in T
T=T.replace(OLD_P0,"`<p>${esc(L({cs:m.cs,en:m.en,de:m.de}))}</p>` + `<div class=\"ssm\"><span class=\"chip ${m.ssm===false?'nonmem':'mem'}\">${m.ssm===false?({cs:'není členem Silicon Saxony · rešerše CNSC',en:'not a Silicon Saxony member · CNSC research',de:'kein Silicon-Saxony-Mitglied · CNSC-Recherche'})[LANG]:({cs:'člen Silicon Saxony',en:'Silicon Saxony member',de:'Silicon-Saxony-Mitglied'})[LANG]}</span></div>`",1)
T=T.replace("</style>",".ssm{margin:0 0 2px}.chip.mem{color:var(--muted)}.chip.nonmem{border:1px dashed var(--muted);color:var(--muted);background:transparent}.vc-chip.nonmem{border-style:dashed}\n</style>",1)
# ---- IPCEI badges on member cards ----
OLD_P="`<p>${esc(L({cs:m.cs,en:m.en,de:m.de}))}</p>`"
assert OLD_P in T
T=T.replace(OLD_P,"`<p>${esc(L({cs:m.cs,en:m.en,de:m.de}))}</p>` + ((m.ipcei||[]).length ? `<div class=\"ipc\">${m.ipcei.map(x=>`<a class=\"chip ipc\" href=\"${esc(x.u)}\" target=\"_blank\" rel=\"noopener\" title=\"${esc(x.s)}\">IPCEI ${esc(x.p)} ${x.y}${x.s&&/assoz/i.test(x.s)?' · '+({cs:'přidružený',en:'associate',de:'assoziiert'})[LANG]:''} ↗</a>`).join('')}</div>` : '')",1)
T=T.replace("</style>",".ipc{display:flex;flex-wrap:wrap;gap:4px;margin:2px 0 4px}.chip.ipc{background:var(--warn-bg);color:var(--warn);border:1px solid var(--warn);font-weight:600}.chip.ipc:hover{text-decoration:underline}\n</style>",1)
# ---- clickable organisation names in the overview level boxes ----
OLD_WHO="const who = D.members.filter(m => ringOf(m.id) === r.n).map(m => m.short);"
assert OLD_WHO in T
T=T.replace(OLD_WHO,"const who = D.members.filter(m => ringOf(m.id) === r.n).sort((a,b)=>a.short.localeCompare(b.short)).map(m => `<a href=\"#member-${esc(m.id)}\" data-go=\"${esc(m.id)}\" class=\"wk\" title=\"${esc(m.n)}\">${esc(m.short)}</a>`);",1)
OLD_KEY="  $('seglist').innerHTML = '';\n}"
assert OLD_KEY in T
T=T.replace(OLD_KEY,"  $('seglist').innerHTML = '';\n  $('key').querySelectorAll('[data-go]').forEach(a => a.onclick = e => { e.preventDefault(); goMember(a.dataset.go); });\n}",1)
T=T.replace("</style>",".rk .w a.wk{color:inherit;text-decoration:none;border-bottom:1px dotted var(--line2)}.rk .w a.wk:hover{color:var(--accent);border-bottom-color:var(--accent)}\n</style>",1)
# ---- clickable source chips (LinkedIn page / YouTube channel / episode) ----
OLD_SRC="if (n.src && srcById[n.src]) h += `<span class=\"chip src\">${esc(L(srcById[n.src]))}</span>`;"
assert OLD_SRC in T
NEW_SRC="if (n.src && srcById[n.src]) { const m0 = ms[0]; let href = ''; if (n.src === 'linkedin' && m0 && m0.li) href = 'https://www.linkedin.com/' + m0.li + '/'; else if (n.src === 'youtube' && m0 && m0.yt) href = 'https://www.youtube.com/channel/' + m0.yt; else if (n.u) href = n.u; h += href ? `<a class=\"chip src\" href=\"${esc(href)}\" target=\"_blank\" rel=\"noopener\" title=\"${esc(href)}\">${esc(L(srcById[n.src]))} ↗</a>` : `<span class=\"chip src\">${esc(L(srcById[n.src]))}</span>`; }"
T=T.replace(OLD_SRC,NEW_SRC,1)
T=T.replace("</style>",".chip.src[href]{cursor:pointer}.chip.src[href]:hover{text-decoration:underline}\n</style>",1)
# ---- YouTube link on member cards ----
OLD_LI="m.li ? `<a href=\"https://www.linkedin.com/${esc(m.li)}/\" target=\"_blank\" rel=\"noopener\">${esc(t.li)} ↗</a>` : ''"
assert OLD_LI in T
T=T.replace(OLD_LI,OLD_LI+", m.yt ? `<a href=\"https://www.youtube.com/channel/${esc(m.yt)}\" target=\"_blank\" rel=\"noopener\">YouTube ↗</a>` : ''",1)

# ---- radar label placement without overlaps ----
a=T.index("  // labels: horizontal text next to the dot;")
z=T.index("  labels.forEach(l => {")
NEW_LABELS=r"""  // labels: greedy placement without overlaps (candidates around the dot; obstacles = other dots, placed labels, sector labels, canvas edge), then a repair pass
  const LH = 17;
  const _cv = document.createElement('canvas').getContext('2d'); _cv.font = '600 14px Inter, sans-serif';
  const tw = s => { try { return Math.max(_cv.measureText(s).width, s.length * 6.5) + 4; } catch (e) { return s.length * 7.6 + 4; } };
  const secRects = segs.map(s => { const [a0, a1] = span[s.id]; const m = (a0 + a1) / 2, lr = R[2] + 18, x = C + lr * Math.cos(m), y = CY + lr * Math.sin(m); const anc = Math.abs(Math.cos(m)) < .25 ? 'middle' : (Math.cos(m) > 0 ? 'start' : 'end'); const yoff = Math.abs(Math.cos(m)) < .25 ? (Math.sin(m) < 0 ? -8 : 18) : 6; const w = (s.code + ' ' + L(s)).length * 9.4; const x0 = anc === 'start' ? x : anc === 'end' ? x - w : x - w / 2; return {x0, x1: x0 + w, y0: y + yoff - 17, y1: y + yoff + 5}; });
  const dotRects = dots.map(d => ({x0: d.x - 11, x1: d.x + 11, y0: d.y - 11, y1: d.y + 11, d}));
  const hit = (r, q) => !(r.x1 <= q.x0 || q.x1 <= r.x0 || r.y1 <= q.y0 || q.y1 <= r.y0);
  const candsFor = (d, wide) => {
    const outward = Math.cos(Math.atan2(d.y - CY, d.x - C)) >= 0;
    const side = outward ? 'start' : 'end', other = outward ? 'end' : 'start', sx = outward ? 13 : -13;
    const c = [];
    const push = (dx, dy, anc) => c.push({dx, dy, anc});
    push(sx, 5, side); push(-sx, 5, other); push(0, -15, 'middle'); push(0, 25, 'middle');
    [13, 26, 39].forEach(k => { push(sx, 5 - k, side); push(sx, 5 + k, side); push(-sx, 5 - k, other); push(-sx, 5 + k, other); push(0, -15 - k, 'middle'); push(0, 25 + k, 'middle'); });
    if (wide) [52, 65, 78, 91, 104].forEach(k => { push(sx, 5 - k, side); push(sx, 5 + k, side); push(-sx, 5 - k, other); push(-sx, 5 + k, other); push(0, -15 - k, 'middle'); push(0, 25 + k, 'middle'); [26, 40].forEach(e => { push(sx + (outward ? e : -e), 5 - k, side); push(sx + (outward ? e : -e), 5 + k, side); }); });
    return c;
  };
  const rectOf = (d, c, w) => { const x = d.x + c.dx, y = d.y + c.dy; const x0 = c.anc === 'start' ? x : c.anc === 'end' ? x - w : x - w / 2; return {x0: x0 - 1, x1: x0 + w + 1, y0: y - 13, y1: y + 4, x, y}; };
  const inBounds = r => r.x0 >= 2 && r.x1 <= W - 2 && r.y0 >= 2 && r.y1 <= H - 2;
  const labels = [];
  const choose = (d, w, others, wide) => {
    let best = null, bestScore = Infinity; const cs = candsFor(d, wide);
    for (let ci = 0; ci < cs.length; ci++) {
      const r = rectOf(d, cs[ci], w); if (!inBounds(r)) continue;
      let bad = 0;
      for (const q of dotRects) if (q.d !== d && hit(r, q)) bad += 4;
      for (const q of others) if (hit(r, q)) bad += 4;
      for (const q of secRects) if (hit(r, q)) bad += 2;
      const score = bad * 1000 + ci;
      if (score < bestScore) { bestScore = score; best = {c: cs[ci], r}; }
      if (bad === 0) break;
    }
    return {best, clash: bestScore >= 1000};
  };
  const order = dots.slice().sort((p, q) => p.ring - q.ring || Math.hypot(p.x - C, p.y - CY) - Math.hypot(q.x - C, q.y - CY));
  order.forEach(d => { const w = tw(d.m.short); const {best, clash} = choose(d, w, labels.map(l => l.r), false); labels.push({d, w, r: best.r, c: best.c, clash}); });
  for (let pass = 0; pass < 3; pass++) {
    let fixedAny = false;
    labels.forEach(l => { if (!l.clash) return; const others = labels.filter(o => o !== l).map(o => o.r); const {best, clash} = choose(l.d, l.w, others, true); l.r = best.r; l.c = best.c; l.clash = clash; if (!clash) fixedAny = true; });
    if (!fixedAny) break;
  }
  labels.forEach(l => { l.x = l.r.x; l.y = l.r.y; l.anchor = l.c.anc; l.right = l.c.anc === 'start'; l.moved = !(l.c.dy === 5 && Math.abs(l.c.dx) === 13); });
"""
T=T[:a]+NEW_LABELS+T[z:]
OLD_LINE="""    if (Math.abs(l.y - (d.y + 5)) > 7) h += `<line x1="${d.x.toFixed(1)}" y1="${d.y.toFixed(1)}" x2="${(l.x + (l.right ? -3 : 3)).toFixed(1)}" y2="${(l.y - 4).toFixed(1)}" stroke="#5d6677" stroke-width="1"/>`;"""
assert OLD_LINE in T
T=T.replace(OLD_LINE,"""    if (l.moved) { const ex = l.anchor === 'middle' ? l.x : (l.x + (l.anchor === 'start' ? -3 : 3)); const ey = l.y > d.y ? l.y - 12 : l.y + 3; h += `<line x1="${d.x.toFixed(1)}" y1="${d.y.toFixed(1)}" x2="${ex.toFixed(1)}" y2="${ey.toFixed(1)}" stroke="#5d6677" stroke-width="1"/>`; }""")
OLD_TXT="""text-anchor="${l.right ? 'start' : 'end'}" font-size="14" font-weight="600" fill="#eef1f6" font-family="Inter,sans-serif">${esc(d.m.short)}</text></g>`;"""
assert OLD_TXT in T
T=T.replace(OLD_TXT,"""text-anchor="${l.anchor}" font-size="14" font-weight="600" fill="#eef1f6" font-family="Inter,sans-serif">${esc(d.m.short)}</text></g>`;""")
# ---- search covers the map ----
OLD_RUN="    document.querySelectorAll('nav.tabs button[data-tab]').forEach(b => badge(b.dataset.tab, words.length ? (per[b.dataset.tab] || 0) : 0));"
assert OLD_RUN in T
T=T.replace(OLD_RUN,"""    document.querySelectorAll('#vcmap .vc-chip[data-go]').forEach(b => { if (!words.length){ b.classList.remove('qdim'); return; } const m = memById[b.dataset.go]; const n = m && last[m.id]; const txt = norm(m ? [m.n, m.short, m.city, m.code, m.cs, m.en, m.de, n && n.cs, n && n.en, n && n.de].filter(Boolean).join(' ') : ''); const hit = words.every(w => txt.includes(w)); b.classList.toggle('qdim', !hit); if (hit) per.map = (per.map || 0) + 1; });
    document.querySelectorAll('#vcmap .vc-seg').forEach(s => s.classList.toggle('qhide', !!words.length && !s.querySelector('.vc-chip[data-go]:not(.qdim)')));
    document.querySelectorAll('#vcmap .vc-stage').forEach(s => s.classList.toggle('qhide', !!words.length && !s.querySelector('.vc-seg:not(.qhide)')));
"""+OLD_RUN,1)
T=T.replace("['renderAll', 'renderNews', 'renderRadar'].forEach(wrap);","['renderAll', 'renderNews', 'renderRadar', 'renderMap'].forEach(wrap);",1)
# ---- value-chain map tab ----
T=T.replace("tabs:['Přehled','Novinky',","tabs:['Přehled','Mapa hodnotového řetězce','Novinky',",1)
T=T.replace("tabs:['Overview','News',","tabs:['Overview','Value chain map','News',",1)
T=T.replace("tabs:['Überblick','Meldungen',","tabs:['Überblick','Wertschöpfungskette','Meldungen',",1)
MAP_CSS=""".vcmap{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;align-items:start}
.vc-stage{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:10px 12px 12px;min-width:0}
.vc-stage.wide{grid-column:1/-1}
.vc-stage h3{margin:0 0 2px;font-size:14px;letter-spacing:.01em}
.vc-stage .vc-n{font:11px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted);margin-bottom:8px}
.vc-seg{border-top:1px solid var(--line);padding:8px 0 4px}
.vc-seg:first-of-type{border-top:0}
.vc-seg h4{margin:0 0 6px;font-size:12px;font-weight:600;color:var(--muted);display:flex;justify-content:space-between;gap:8px}
.vc-seg h4 code{font:11px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent);margin-right:6px}
.vc-chips{display:flex;flex-wrap:wrap;gap:4px}
.vc-chip{font:12px/1.1 inherit;padding:4px 7px 4px 6px;border:1px solid var(--line);border-left:3px solid var(--c,var(--accent));border-radius:7px;background:transparent;color:inherit;cursor:pointer;max-width:100%;text-align:left}
.vc-chip:hover{background:var(--line)}
.vc-chip.r1{box-shadow:inset 0 0 0 1px var(--ring1);font-weight:600}
.vc-chip.r2{box-shadow:inset 0 0 0 1px var(--ring2)}
.vc-chip .d{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:5px;vertical-align:1px;background:var(--ring4)}
.vc-chip.r1 .d{background:var(--ring1)}.vc-chip.r2 .d{background:var(--ring2)}
.vc-chip .ipcm{font:600 9px/1 inherit;color:var(--warn);border:1px solid var(--warn);border-radius:4px;padding:1px 3px;margin-left:4px;vertical-align:1px}
.vc-stages{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px}
.vc-stbtn{font:600 12px/1 inherit;padding:7px 11px;border-radius:999px;border:1px solid var(--line);background:transparent;color:inherit;cursor:pointer}
.vc-stbtn:hover{background:var(--line)}
.vc-stbtn.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.vc-stbtn .n{opacity:.7;margin-left:5px;font-weight:500}
#vcmap .vc-chip.qdim{opacity:.12}
#vcmap .vc-seg.qhide,#vcmap .vc-stage.qhide{display:none}
.vc-flow{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;margin:0 0 12px;color:var(--muted);font-size:12px}
.vc-flow b{color:inherit;font-weight:600}
.vc-legend{display:flex;flex-wrap:wrap;gap:12px;font-size:12px;color:var(--muted);margin:12px 0 0}
.card.hl{outline:2px solid var(--accent);outline-offset:2px}
@media (min-width:1100px){.vcmap{grid-template-columns:repeat(4,1fr)}}
"""
T=T.replace("</style>",MAP_CSS+"</style>",1)
MAP_HTML="""  <section class="panel" id="p-map" role="tabpanel">
    <h2 id="mapH"></h2>
    <p class="sub" id="mapSub"></p>
    <div class="vc-stages" id="vcstages" role="group"></div>
    <div class="vcmap" id="vcmap"></div>
    <div class="vc-legend" id="vclegend"></div>
  </section>
"""
T=T.replace('  <section class="panel" id="p-news" role="tabpanel">',MAP_HTML+'  <section class="panel" id="p-news" role="tabpanel">',1)
MAP_JS=r"""
const MAPT={cs:{h:'Mapa hodnotového řetězce',sub:'Všechny organizace na jednom obrázku, uspořádané podle taxonomie CNSC: sloupce jsou fáze řetězce, boxy segmenty, štítky jednotlivé firmy a instituce. Kliknutím na štítek otevřete kartu organizace. Tečka ukazuje čerstvost poslední veřejné aktivity (tmavá: tento týden, střední: tento měsíc, světlá: starší nebo zatím nesledováno).',legend:['tento týden','tento měsíc','starší nebo zatím nesledováno'],flow:'Tok hodnotového řetězce',ipc:'IPCEI = účastník IPCEI Mikroelektronika (2018) nebo IPCEI ME/CT (2023) podle veřejných zdrojů; čárkovaný rámeček = není členem Silicon Saxony (rešerše CNSC); podrobnosti na kartě'},
 en:{h:'Value chain map',sub:'All organisations in one picture, arranged by the CNSC taxonomy: columns are stages of the chain, boxes are segments, chips are individual companies and institutes. Click a chip to open the organisation card. The dot shows the freshness of the last public activity (dark: this week, medium: this month, light: older or not yet tracked).',legend:['this week','this month','older or not yet tracked'],flow:'Value chain flow',ipc:'IPCEI = participant in IPCEI Microelectronics (2018) or IPCEI ME/CT (2023) according to public sources; dashed border = not a Silicon Saxony member (CNSC research); details on the card'},
 de:{h:'Wertschöpfungskette',sub:'Alle Organisationen in einem Bild, geordnet nach der CNSC-Taxonomie: Spalten sind Stufen der Kette, Kästen die Segmente, Chips die einzelnen Unternehmen und Institute. Klick auf einen Chip öffnet die Organisationskarte. Der Punkt zeigt die Aktualität der letzten öffentlichen Aktivität (dunkel: diese Woche, mittel: diesen Monat, hell: älter oder noch nicht erfasst).',legend:['diese Woche','diesen Monat','älter oder noch nicht erfasst'],flow:'Fluss der Wertschöpfungskette',ipc:'IPCEI = Teilnehmer am IPCEI Mikroelektronik (2018) oder IPCEI ME/KT (2023) laut öffentlichen Quellen; gestrichelter Rahmen = kein Silicon-Saxony-Mitglied (CNSC-Recherche); Details auf der Karte'}};
const MAPG=[
 {id:'design',codes:['1.1','1.2','1.3','1.4'],t:{cs:'1 Návrh a software',en:'1 Design & software',de:'1 Design & Software'}},
 {id:'equip',codes:['2.1','2.2','2.3'],t:{cs:'2 Zařízení a metrologie',en:'2 Equipment & metrology',de:'2 Anlagen & Messtechnik'}},
 {id:'subsys',codes:['2.4.1','2.4.2','2.4.3','2.4.4','2.4.5','2.4.6','2.5','F'],t:{cs:'2.4 Subsystémy, služby, infrastruktura',en:'2.4 Subsystems, services & fab infrastructure',de:'2.4 Subsysteme, Dienstleistungen, Fab-Infrastruktur'}},
 {id:'materials',codes:['3.1','3.2'],t:{cs:'3 Materiály',en:'3 Materials',de:'3 Materialien'}},
 {id:'fab',codes:['4.2','4.3','4.4','4.5','4.6'],t:{cs:'4 Výroba čipů',en:'4 Chip manufacturing',de:'4 Chipfertigung'}},
 {id:'pack',codes:['5.1','5.2','5.3'],t:{cs:'5 Pouzdření a test',en:'5 Packaging & test',de:'5 Packaging & Test'}},
 {id:'apps',codes:['6.1','6.2','6.3','6.4','6.5','6.6','D'],t:{cs:'6 Aplikace a distribuce',en:'6 Applications & distribution',de:'6 Anwendungen & Distribution'}},
 {id:'eco',codes:['7.1','7.2','7.3'],wide:true,t:{cs:'7 Výzkum, vzdělávání, politika a klastry',en:'7 Research, skills, policy & clusters',de:'7 Forschung, Bildung, Politik & Cluster'}}];
let MAPSEL=null;
function segName(m){ return String(L({cs:m.cs,en:m.en,de:m.de})).replace(/^[^ ]+ /,'').split(' (')[0]; }
function goMember(id){ showTab('members'); const el=document.getElementById('member-'+id); if(!el) return; el.scrollIntoView({behavior:'smooth',block:'center'}); document.querySelectorAll('.card.hl').forEach(c=>c.classList.remove('hl')); el.classList.add('hl'); setTimeout(()=>el.classList.remove('hl'),4000); }
function renderMap(){
  const t=MAPT[LANG]||MAPT.en; $('mapH').textContent=t.h; $('mapSub').textContent=t.sub;
  const byCode={}; D.members.forEach(m=>{(byCode[m.code]=byCode[m.code]||[]).push(m)});
  Object.values(byCode).forEach(a=>a.sort((x,y)=>{const rx=ringOf(x.id),ry=ringOf(y.id); return rx!==ry?rx-ry:x.short.localeCompare(y.short)}));
  const used=new Set(MAPG.flatMap(g=>g.codes));
  const rest=Object.keys(byCode).filter(c=>!used.has(c)); if(rest.length) MAPG[MAPG.length-1].codes.push(...rest.filter(c=>!MAPG[MAPG.length-1].codes.includes(c)));
  const chip=m=>`<button class="vc-chip r${ringOf(m.id)}${(m.ipcei||[]).length?' ipc':''}${m.ssm===false?' nonmem':''}" data-go="${esc(m.id)}" title="${esc(m.n)} · ${esc(m.city)}${(m.ipcei||[]).length?' · IPCEI '+m.ipcei.map(x=>x.p+' '+x.y).join(', '):''}" style="--c:var(--seg-${esc(m.s)})"><span class="d"></span>${esc(m.short)}${(m.ipcei||[]).length?' <span class="ipcm">IPCEI</span>':''}</button>`;
  const cnt=g=>g.codes.reduce((a,c)=>a+((byCode[c]||[]).length),0);
  $('vcstages').innerHTML=`<button type="button" class="vc-stbtn${MAPSEL?'':' on'}" data-st="">${esc(({cs:'Vše',en:'All',de:'Alle'})[LANG]||'All')}<span class="n">${D.members.length}</span></button>`+MAPG.map(g=>`<button type="button" class="vc-stbtn${MAPSEL===g.id?' on':''}" data-st="${g.id}">${esc(L(g.t))}<span class="n">${cnt(g)}</span></button>`).join('');
  $('vcstages').querySelectorAll('.vc-stbtn').forEach(bt=>bt.onclick=()=>{const v=bt.dataset.st||null; MAPSEL=(MAPSEL===v)?null:v; renderMap();});
  $('vcmap').innerHTML=MAPG.filter(g=>!MAPSEL||g.id===MAPSEL).map(g=>{const segs=g.codes.filter(c=>byCode[c]); const n=segs.reduce((a,c)=>a+byCode[c].length,0); if(!n) return '';
    return `<div class="vc-stage${g.wide?' wide':''}"><h3>${esc(L(g.t))}</h3><div class="vc-n">${n}</div>`+segs.map(c=>`<div class="vc-seg"><h4><span><code>${esc(c)}</code>${esc(segName(byCode[c][0]))}</span><span>${byCode[c].length}</span></h4><div class="vc-chips">${byCode[c].map(chip).join('')}</div></div>`).join('')+`</div>`;}).join('');
  $('vclegend').innerHTML=[1,2,4].map((r,i)=>`<span><span class="vc-chip r${r}" style="pointer-events:none;padding:2px 6px"><span class="d"></span>${esc(t.legend[i])}</span></span>`).join('')+`<span>${esc(t.ipc)}</span>`;
  $('vcmap').querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>goMember(b.dataset.go));
}
"""
T=T.replace("function renderAll() {",MAP_JS+"function renderAll() {",1)
T=T.replace("function renderAll() { renderStatic(); renderStats(); renderRadar(); renderTop(); renderNews(); renderMembers(); renderCentres(); renderEvents(); renderAbout(); }","function renderAll() { renderStatic(); renderStats(); renderRadar(); renderTop(); renderNews(); renderMembers(); renderCentres(); renderEvents(); renderAbout(); renderMap(); }",1)
assert 'renderMap();' in T and 'id="p-map"' in T and "'map','news'" in T
html=T.replace('/*__DATA__*/',body)
open('sx.html','w',encoding='utf-8').write(html)
print(len(html),'companies',len(d['members']),'news',len(d['news']),'events',len(d['events']))
