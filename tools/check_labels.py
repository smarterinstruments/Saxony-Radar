import asyncio,sys
from playwright.async_api import async_playwright
JS="""() => { const svg=document.querySelector('#radarSvg svg'); const texts=[...svg.querySelectorAll('g.dot text')]; const sect=[...svg.querySelectorAll(':scope > text')].filter(t=>t.getAttribute('font-size')==='16'); const circles=[...svg.querySelectorAll('g.dot circle')];
 const bb=e=>{const b=e.getBBox();return {x0:b.x,x1:b.x+b.width,y0:b.y,y1:b.y+b.height,n:e.textContent||''}};
 const hit=(a,b)=>!(a.x1<=b.x0||b.x1<=a.x0||a.y1<=b.y0||b.y1<=a.y0);
 const T=texts.map(bb), S=sect.map(bb), Cc=circles.map(c=>({x0:+c.getAttribute('cx')-8,x1:+c.getAttribute('cx')+8,y0:+c.getAttribute('cy')-8,y1:+c.getAttribute('cy')+8,g:c.parentElement}));
 const out=[];
 for(let i=0;i<T.length;i++){for(let j=i+1;j<T.length;j++) if(hit(T[i],T[j])) out.push(['label-label',T[i].n,T[j].n]);
  for(const s of S) if(hit(T[i],s)) out.push(['label-sector',T[i].n,s.n]);
  for(let k=0;k<Cc.length;k++) if(Cc[k].g!==texts[i].parentElement && hit(T[i],Cc[k])) out.push(['label-dot',T[i].n,Cc[k].g.dataset.id]);}
 return {labels:T.length,overlaps:out}; }"""
async def main(path):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':900})
        await pg.goto('file://'+path); await pg.wait_for_timeout(900)
        for lang in ['de','en','cs']:
            await pg.click('#b-'+lang); await pg.wait_for_timeout(500)
            r=await pg.evaluate(JS); print(lang,'labels',r['labels'],'overlaps',len(r['overlaps']),r['overlaps'][:8])
        await pg.click('#b-de'); await pg.wait_for_timeout(300); await pg.screenshot(path='/home/claude/vc-radar/sx_radar_labels.png',clip={'x':70,'y':600,'width':790,'height':300})
        await b.close()
asyncio.run(main(sys.argv[1]))
