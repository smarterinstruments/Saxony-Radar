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
 ['Stav náhledu','Aktivity jsou zatím sebrány jen z veřejných LinkedIn stránek vybraných firem a institucí (sběr 15. 11. 2026); u skupinových stránek (Infineon, GlobalFoundries, Bosch) jde o zprávy celé skupiny. U ostatních organizací sběr teprve začíná, proto jsou vedeny bez sledované aktivity.'],
 ['Co tu není','Interní informace klastrů, obchodně citlivé údaje firem a osobní údaje kontaktních osob. Radar pracuje jen s veřejnými informacemi. Opravy a doplnění: info@semicz.cz, předmět „Radar Sasko“.']],
'de':[
 ['Was der Radar erfasst','Öffentliche Aktivitäten von Unternehmen und Instituten des sächsischen Halbleiter-Ökosystems: neue Produkte und Technologien, Investitionen und Erweiterungen, Projekte und Förderungen, Veranstaltungen, Partnerschaften, Auszeichnungen und Führungswechsel. Die Vorschau hat CNSC für Silicon Saxony im Rahmen der Absichtserklärung vom 12. 11. 2026 erstellt.'],
 ['Woher die Daten stammen','Die Liste der Organisationen stammt aus dem öffentlichen Mitgliederverzeichnis von Silicon Saxony (734 Profile, davon 480 in der Mikroelektronik-Wertschöpfungskette), ergänzt durch CNSC-Recherchen in öffentlichen Quellen. Die Zuordnung zu den Segmenten der CNSC-Taxonomie ist vorläufig: Jede Organisation trägt eine Sicherheitsstufe der Zuordnung und wartet auf die Bestätigung durch Silicon Saxony.'],
 ['Wie der Radar zu lesen ist','Die Sektoren sind Segmente der Wertschöpfungskette, die Ringe zeigen die Aktualität: diese Woche (bis 7 Tage) und diesen Monat (8–31 Tage). Die Stufe sagt nur, wann wir zuletzt eine öffentliche Aktivität erfasst haben; sie ist keine Bewertung des Unternehmens. Der Filter Segment im Reiter Unternehmen wählt einzelne Taxonomie-Codes aus, einschließlich der Untersegmente 2.4.1–2.4.6.'],
 ['Stand der Vorschau','Aktivitäten wurden bisher nur von den öffentlichen LinkedIn-Seiten ausgewählter Unternehmen und Institute erfasst (Stand 15. 11. 2026); bei Konzernseiten (Infineon, GlobalFoundries, Bosch) handelt es sich um Konzernmeldungen. Für die übrigen Organisationen beginnt die Erfassung erst, deshalb erscheinen sie ohne erfasste Aktivität.'],
 ['Was hier nicht steht','Interne Informationen der Cluster, geschäftlich sensible Unternehmensdaten und personenbezogene Daten von Ansprechpartnern. Der Radar arbeitet ausschließlich mit öffentlichen Informationen. Korrekturen und Ergänzungen: info@semicz.cz, Betreff „Radar Sachsen“.']],
'en':[
 ['What the radar tracks','Public activities of companies and institutes in the Saxon semiconductor ecosystem: new products and technologies, investments and expansion, projects and grants, events, partnerships, awards and leadership changes. The preview was prepared by CNSC for Silicon Saxony under the memorandum of understanding of 12 Nov 2026.'],
 ['Where the data comes from','The organisation list comes from the public Silicon Saxony member directory (734 profiles, 480 of them in the microelectronics value chain), complemented by CNSC research in public sources. CNSC taxonomy segments are provisional: each organisation carries a confidence level and awaits confirmation by Silicon Saxony.'],
 ['How to read the radar','Sectors are value-chain segments, rings show freshness: this week (up to 7 days) and this month (8–31 days). The level only says when we last recorded public activity; it is not a rating of the company. The Segment filter in the Companies tab selects individual taxonomy codes, including the sub-segments 2.4.1–2.4.6.'],
 ['Status of the preview','Activities have so far been collected only from the public LinkedIn pages of selected companies and institutes (collected 15 Nov 2026); for group pages (Infineon, GlobalFoundries, Bosch) the items are group news. Collection for the other organisations is only starting, so they are shown without tracked activity.'],
 ['What is not here','Internal cluster information, commercially sensitive company data and personal data of contact persons. The radar works with public information only. Corrections and additions: info@semicz.cz, subject “Radar Saxony”.']]}
CS=[('Radar aktivit členů','Radar hodnotového řetězce'),('členů klastru','organizací v Sasku'),('v 8 segmentech hodnotového řetězce','v 10 segmentech hodnotového řetězce'),('každý bod je jeden člen s','každý bod je jedna firma s'),('jeden člen; popisek','jedna firma; popisek'),('zatím žádný člen','zatím žádná firma'),('firemní stránky členů na LinkedIn, weby členů, semicz.cz; stupeň není hodnocení člena','firemní stránky na LinkedIn, weby firem, tisk; stupeň není hodnocení firmy'),('Kmenová data z katalogu klastru a semicz.cz.','Kmenová data z veřejného adresáře členů Silicon Saxony a rešerše CNSC; zařazení čeká na potvrzení Silicon Saxony.'),('Členové','Firmy'),('členové','firmy'),('členů','firem'),('člena','firmy'),('členy','firmy'),('členech','firmách'),('člen ','firma '),('člen','firma')]
EN=[('Member Activity Radar','Semiconductor Value Chain Radar'),('Member activity radar','Value chain radar'),('cluster members','organisations in Saxony'),('in 8 value-chain segments','in 10 value-chain segments'),('members’ LinkedIn company pages, member websites, semicz.cz; the level is not a rating of the member','LinkedIn company pages, company websites, press; the level is not a rating of the company'),('Master data from the cluster catalogue and semicz.cz.','Master data from the public Silicon Saxony member directory and CNSC research; segments await confirmation by Silicon Saxony.'),('Members','Companies'),('members','companies'),('Member','Company'),('member','company')]
DE=[('Radar der Mitgliederaktivitäten','Radar der Halbleiter-Wertschöpfungskette'),('Clustermitglieder','Organisationen in Sachsen'),('in 8 Segmenten der Wertschöpfungskette','in 10 Segmenten der Wertschöpfungskette'),('jeder Punkt ist ein Mitglied mit','jeder Punkt ist ein Unternehmen mit'),('ein Mitglied; ','ein Unternehmen; '),('noch kein Mitglied','noch kein Unternehmen'),('Stammdaten aus dem Clusterkatalog und semicz.cz.','Stammdaten aus dem öffentlichen Mitgliederverzeichnis von Silicon Saxony und CNSC-Recherche; die Zuordnung wartet auf die Bestätigung durch Silicon Saxony.'),('LinkedIn-Unternehmensseiten der Mitglieder, Websites der Mitglieder, semicz.cz; die Stufe ist keine Bewertung des Mitglieds','LinkedIn-Unternehmensseiten, Websites der Unternehmen, Presse; die Stufe ist keine Bewertung des Unternehmens'),('Mitgliedern','Unternehmen'),('Mitglieder','Unternehmen'),('Mitglieds','Unternehmens'),('Mitglied','Unternehmen')]
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
("['overview','news','members','centres','events','about']","['overview','news','members','events','about']"),
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
html=T.replace('/*__DATA__*/',body)
open('sx.html','w',encoding='utf-8').write(html)
print(len(html),'companies',len(d['members']),'news',len(d['news']),'events',len(d['events']))
