import json, pathlib
SP = pathlib.Path('/tmp/claude-0/-home-user-chromium/5718da5e-e7ac-59de-9275-7bf646dc8103/scratchpad')
corpus = json.loads((SP/'corpus.json').read_text())

HTML = r'''<title>Image Prompt Studio</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root{
  --paper:#E6E7E9; --frame:#F8F9FA; --sunk:#DDDFE2; --rebate:#24262A;
  --ink:#16181B; --ink2:#5A6068; --ink3:#878D95;
  --mark:#C4342A; --mark-soft:#C4342A1F; --line:#CDD0D4; --line2:#B9BEC4;
  --shadow:0 1px 2px #16181b12, 0 6px 16px -10px #16181b26;
  --sans:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --cond:"Archivo Narrow","Arial Narrow",var(--sans);
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#121315; --frame:#1B1D20; --sunk:#0E0F11; --rebate:#08090A;
  --ink:#E7E9EC; --ink2:#9198A1; --ink3:#6B727B;
  --mark:#E4584A; --mark-soft:#E4584A24; --line:#2C2F34; --line2:#3A3E45;
  --shadow:0 1px 2px #0006, 0 8px 20px -12px #0009;
}}
:root[data-theme="dark"]{
  --paper:#121315; --frame:#1B1D20; --sunk:#0E0F11; --rebate:#08090A;
  --ink:#E7E9EC; --ink2:#9198A1; --ink3:#6B727B;
  --mark:#E4584A; --mark-soft:#E4584A24; --line:#2C2F34; --line2:#3A3E45;
  --shadow:0 1px 2px #0006, 0 8px 20px -12px #0009;
}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.55;margin:0;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding-inline:16px;padding-block:0 64px}
h1,h2,h3{margin:0;text-wrap:balance}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--mark);outline-offset:2px;border-radius:3px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

/* ---------- masthead ---------- */
.mast{border-bottom:1px solid var(--line);margin-bottom:22px}
.mast-in{display:flex;flex-wrap:wrap;gap:14px 20px;align-items:flex-end;
  justify-content:space-between;padding-block:26px 18px}
.brand{display:flex;align-items:baseline;gap:11px;flex-wrap:wrap}
h1{font-family:var(--cond);font-size:clamp(27px,5.5vw,38px);font-weight:700;
  letter-spacing:-.01em;line-height:1}
.brand .sub{font-family:var(--mono);font-size:11px;color:var(--ink3);
  letter-spacing:.06em;text-transform:uppercase}
.tally{font-family:var(--mono);font-size:11.5px;color:var(--ink2);
  letter-spacing:.04em;display:flex;gap:14px;flex-wrap:wrap}
.tally b{color:var(--mark);font-weight:600}
.lede{max-width:64ch;color:var(--ink2);font-size:14.5px;padding-bottom:22px}

/* ---------- light table (builder) ---------- */
.rig{background:var(--frame);border:1px solid var(--line);border-radius:4px;
  box-shadow:var(--shadow);overflow:hidden;margin-bottom:34px}
.rig-hd{display:flex;align-items:center;gap:10px;background:var(--rebate);
  color:#E7E9EC;padding:9px 14px;font-family:var(--mono);font-size:10.5px;
  letter-spacing:.14em;text-transform:uppercase}
.rig-hd .dot{width:7px;height:7px;border-radius:50%;background:var(--mark);flex:none}
.rig-bd{padding:16px 14px 18px;display:grid;gap:14px}
.fields{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(190px,1fr))}
.field{display:grid;gap:5px;min-width:0}
.field>span{font-family:var(--cond);font-size:11.5px;font-weight:600;
  letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}
.field .num{color:var(--mark)}
select,input[type=text]{width:100%;min-width:0;background:var(--paper);
  color:var(--ink);border:1px solid var(--line2);border-radius:3px;
  padding:8px 9px;font-family:var(--sans);font-size:13.5px}
select{appearance:none;background-image:linear-gradient(45deg,transparent 50%,var(--ink3) 50%),linear-gradient(135deg,var(--ink3) 50%,transparent 50%);
  background-position:calc(100% - 15px) 51%,calc(100% - 10px) 51%;
  background-size:5px 5px,5px 5px;background-repeat:no-repeat;padding-right:30px}
.out{background:var(--sunk);border:1px solid var(--line);border-radius:3px;
  padding:13px 14px;font-family:var(--mono);font-size:13px;line-height:1.72;
  white-space:pre-wrap;word-break:break-word;min-height:96px}
.out em{color:var(--ink3);font-style:normal}
.rig-ft{display:flex;gap:9px;flex-wrap:wrap;align-items:center}
.btn{background:var(--mark);color:#fff;border:none;border-radius:3px;
  padding:9px 17px;font-family:var(--cond);font-size:13.5px;font-weight:600;
  letter-spacing:.06em;text-transform:uppercase;cursor:pointer}
.btn.ghost{background:transparent;color:var(--ink2);border:1px solid var(--line2)}
.btn:hover{filter:brightness(1.08)}
.hint{font-size:12.5px;color:var(--ink3);margin-left:auto}

/* ---------- controls ---------- */
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;
  background:var(--paper);border-bottom:1px solid var(--line);
  padding-block:11px;margin-bottom:20px}
.bar-in{display:flex;gap:9px;flex-wrap:wrap;align-items:center}
.search{flex:1 1 210px;min-width:0}
.tabs{display:flex;gap:5px;flex-wrap:wrap}
.tab{background:transparent;border:1px solid var(--line2);border-radius:3px;
  padding:6px 11px;font-family:var(--cond);font-size:12.5px;font-weight:600;
  letter-spacing:.07em;text-transform:uppercase;color:var(--ink2);cursor:pointer}
.tab[aria-pressed="true"]{background:var(--rebate);border-color:var(--rebate);color:#F1F2F4}
.tab .c{font-family:var(--mono);font-size:10px;opacity:.6;margin-left:5px}

/* ---------- contact sheet ---------- */
section{margin-bottom:30px}
.sect-hd{display:flex;align-items:baseline;gap:11px;flex-wrap:wrap;
  padding-bottom:9px;margin-bottom:13px;border-bottom:1px solid var(--line)}
.sect-hd h2{font-family:var(--cond);font-size:18px;font-weight:700;letter-spacing:.01em}
.sect-hd .c{font-family:var(--mono);font-size:11px;color:var(--ink3)}
.sheet{display:grid;gap:9px;grid-template-columns:repeat(auto-fill,minmax(268px,1fr))}
.fr{display:grid;grid-template-columns:34px 1fr;background:var(--frame);
  border:1px solid var(--line);border-radius:3px;overflow:hidden;min-width:0}
.fr:hover{border-color:var(--line2)}
.rb{background:var(--rebate);color:#7C838C;font-family:var(--mono);font-size:10px;
  display:flex;flex-direction:column;align-items:center;justify-content:flex-start;
  padding-block:9px;gap:6px;letter-spacing:.04em}
.rb .sp{width:9px;height:6px;border-radius:1.5px;background:#31353A}
.fr-bd{padding:9px 11px 11px;min-width:0;display:grid;gap:5px;align-content:start}
.fr-top{display:flex;align-items:center;gap:8px;justify-content:space-between}
.fr-code{font-family:var(--mono);font-size:12.5px;font-weight:600;color:var(--mark);
  word-break:break-word}
.fr-note{font-size:11.5px;color:var(--ink3);font-style:italic}
.fr-p{font-family:var(--mono);font-size:11.8px;line-height:1.62;color:var(--ink2);
  word-break:break-word}
.fr-desc{font-size:12.5px;color:var(--ink3)}
.cp{background:transparent;border:1px solid var(--line2);border-radius:2px;
  color:var(--ink3);font-family:var(--cond);font-size:10.5px;font-weight:600;
  letter-spacing:.09em;text-transform:uppercase;padding:2px 7px;cursor:pointer;flex:none}
.cp:hover{color:var(--mark);border-color:var(--mark)}
.cp.done{color:#fff;background:var(--mark);border-color:var(--mark)}
.fr.wide{grid-column:1/-1}
@media(min-width:760px){.sheet.pre{grid-template-columns:repeat(2,1fr)}.fr.wide{grid-column:auto}}
.empty{color:var(--ink3);font-family:var(--mono);font-size:13px;padding:34px 0;text-align:center}
footer{border-top:1px solid var(--line);margin-top:34px;padding-top:16px;
  font-size:12.5px;color:var(--ink3);display:flex;gap:8px 18px;flex-wrap:wrap}
footer code{font-family:var(--mono);font-size:11.5px;color:var(--ink2)}
</style>

<div class="wrap">
  <header class="mast">
    <div class="mast-in">
      <div class="brand">
        <h1>Image Prompt Studio</h1>
        <span class="sub">Contact sheet</span>
      </div>
      <div class="tally" id="tally"></div>
    </div>
  </header>

  <p class="lede">Korpus prompt untuk edit dan generate foto. Teks prompt bahasa
  Inggris karena model gambar membacanya lebih akurat. Rakit di meja bawah, atau
  telusuri katalognya dan salin satu per satu.</p>

  <div class="rig">
    <div class="rig-hd"><span class="dot"></span><span>Meja rakit &mdash; prompt tersusun otomatis</span></div>
    <div class="rig-bd">
      <div class="fields">
        <label class="field"><span><span class="num">1</span> &middot; Aksi</span>
          <select id="f-act"></select></label>
        <label class="field"><span><span class="num">2</span> &middot; Identity lock</span>
          <select id="f-lock"></select></label>
        <label class="field"><span><span class="num">3</span> &middot; Kamera</span>
          <select id="f-cam"></select></label>
        <label class="field"><span><span class="num">4</span> &middot; Cahaya</span>
          <select id="f-lit"></select></label>
        <label class="field"><span><span class="num">5</span> &middot; Efek</span>
          <select id="f-fx"></select></label>
        <label class="field"><span><span class="num">6</span> &middot; Larangan</span>
          <select id="f-ban"></select></label>
      </div>
      <div class="out" id="out"></div>
      <div class="rig-ft">
        <button class="btn" id="copy-out">Salin prompt</button>
        <button class="btn ghost" id="reset">Atur ulang</button>
        <span class="hint" id="wc"></span>
      </div>
    </div>
  </div>

  <div class="bar">
    <div class="bar-in">
      <input class="search" id="q" type="text" placeholder="Cari kode, efek, atau kata dalam prompt&hellip;" aria-label="Cari korpus">
      <div class="tabs" id="tabs"></div>
    </div>
  </div>

  <div id="sheets"></div>

  <footer>
    <span>Dipasang sebagai skill <code>image-prompt-studio</code></span>
    <span>Target: Nano Banana (Gemini Image) &amp; ChatGPT / GPT Image</span>
  </footer>
</div>

<script>
const DATA = __CORPUS__;

/* ---------- catalogue model ---------- */
const BANS = DATA.bans.map((b,i)=>({group:b.group,code:'Larangan '+(i+1),prompt:b.prompt,note:''}));
const CATS = [
  {id:'preset', label:'Preset', items:DATA.presets.map(p=>({...p,code:p.name}))},
  {id:'angle',  label:'Ubah sudut', items:DATA.angle},
  {id:'lock',   label:'Identity lock', items:DATA.locks.concat(BANS)},
  {id:'camera', label:'Kamera', items:DATA.camera},
  {id:'light',  label:'Cahaya', items:DATA.lighting},
  {id:'fx',     label:'Efek', items:DATA.effects},
];
const total = CATS.reduce((a,c)=>a+c.items.length,0);
document.getElementById('tally').innerHTML =
  `<span><b>${DATA.presets.length}</b> preset</span><span><b>${DATA.camera.length}</b> kode kamera</span>`+
  `<span><b>${DATA.lighting.length}</b> cahaya</span><span><b>${DATA.effects.length}</b> efek</span>`+
  `<span><b>${DATA.angle.length}</b> ubah sudut</span>`+
  `<span><b>${total}</b> total</span>`;

/* ---------- clipboard ---------- */
async function copy(text, btn){
  let ok = false;
  try{ await navigator.clipboard.writeText(text); ok = true; }
  catch(e){
    try{
      const t = document.createElement('textarea');
      t.value = text; t.setAttribute('readonly','');
      t.style.cssText = 'position:fixed;top:-2000px;opacity:0';
      document.body.appendChild(t); t.select();
      ok = document.execCommand('copy'); t.remove();
    }catch(e2){ ok = false; }
  }
  if(!btn) return ok;
  const was = btn.textContent;
  btn.textContent = ok ? 'Tersalin' : 'Pilih manual';
  btn.classList.toggle('done', ok);
  setTimeout(()=>{ btn.textContent = was; btn.classList.remove('done'); }, 1400);
  return ok;
}

/* ---------- builder ---------- */
function fill(sel, items, blank, valueOf){
  sel.innerHTML = '';
  const o = document.createElement('option');
  o.value = ''; o.textContent = blank; sel.appendChild(o);
  let last = null, grp = null;
  items.forEach(it=>{
    if(it.group !== last){ last = it.group;
      grp = document.createElement('optgroup'); grp.label = it.group; sel.appendChild(grp); }
    const op = document.createElement('option');
    op.value = valueOf(it); op.textContent = it.code;
    (grp || sel).appendChild(op);
  });
}
const F = {act:'f-act',lock:'f-lock',cam:'f-cam',lit:'f-lit',fx:'f-fx',ban:'f-ban'};
const el = {}; for(const k in F) el[k] = document.getElementById(F[k]);
const v = it => it.prompt;
fill(el.act,  DATA.presets, '— pilih aksi —', v);
fill(el.lock, DATA.locks,   '— pilih tingkat lock —', v);
fill(el.cam,  DATA.camera,  '— pertahankan sudut asli —', v);
fill(el.lit,  DATA.lighting,'— biarkan cahaya apa adanya —', v);
fill(el.fx,   DATA.effects, '— tanpa efek —', v);
fill(el.ban,  BANS,         '— tanpa larangan tambahan —', v);

function period(s){ s = s.trim(); return /[.!?]$/.test(s) ? s : s + '.'; }
function build(){
  const parts = [];
  if(el.act.value)  parts.push(period(el.act.value));
  if(el.lock.value) parts.push(period(el.lock.value));
  if(el.cam.value)  parts.push(period(el.cam.value));
  if(el.lit.value)  parts.push(period(el.lit.value));
  if(el.fx.value)   parts.push(period(el.fx.value));
  if(el.ban.value)  parts.push(period(el.ban.value));
  const out = document.getElementById('out');
  const text = parts.join(' ');
  if(!text){ out.innerHTML = '<em>Pilih minimal satu blok di atas &mdash; hasilnya muncul di sini.</em>';
             document.getElementById('wc').textContent = ''; return ''; }
  out.textContent = text;
  const w = text.trim().split(/\s+/).length;
  document.getElementById('wc').textContent =
    w + ' kata' + (w > 120 ? ' — agak panjang, pertimbangkan dipangkas' : '');
  return text;
}
Object.values(el).forEach(s=>s.addEventListener('change', build));
document.getElementById('copy-out').addEventListener('click', e=>copy(build(), e.currentTarget));
function preset(){
  const pick = (sel, test) => {
    const o = [...sel.options].find(x=>test(x.textContent)); if(o) sel.value = o.value; };
  pick(el.act,  t=>t.startsWith('Upgrade to DSLR'));
  pick(el.lock, t=>t.startsWith('Tingkat 2'));
  pick(el.cam,  t=>t === '/chestlevel');
  pick(el.lit,  t=>t === 'Golden hour');
  pick(el.fx,   t=>t === 'Grain 35mm');
  pick(el.ban,  t=>false);
  build();
}
document.getElementById('reset').addEventListener('click', ()=>{
  Object.values(el).forEach(s=>s.value=''); build(); });
preset();

/* ---------- catalogue render ---------- */
const sheets = document.getElementById('sheets');
const tabs = document.getElementById('tabs');
let active = 'all', query = '';
try{ active = localStorage.getItem('ips-tab') || 'all'; }catch(e){}
if(!['all',...CATS.map(c=>c.id)].includes(active)) active = 'all';

[{id:'all',label:'Semua',n:total}, ...CATS.map(c=>({id:c.id,label:c.label,n:c.items.length}))]
.forEach(t=>{
  const b = document.createElement('button');
  b.className = 'tab'; b.type = 'button'; b.dataset.id = t.id;
  b.innerHTML = t.label + '<span class="c">' + t.n + '</span>';
  b.addEventListener('click', ()=>{ active = t.id;
    try{ localStorage.setItem('ips-tab', t.id); }catch(e){} render(); });
  tabs.appendChild(b);
});

function esc(s){ return s.replace(/[&<>"]/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function frame(it, cat){
  const d = document.createElement('div');
  d.className = 'fr' + (cat === 'preset' || cat === 'angle' ? ' wide' : '');
  const n = it.n != null ? String(it.n).padStart(2,'0') : '';
  d.innerHTML =
    `<div class="rb">${n ? esc(n) : ''}<span class="sp"></span><span class="sp"></span></div>`+
    `<div class="fr-bd">`+
      `<div class="fr-top"><span class="fr-code">${esc(it.code)}</span>`+
      `<button class="cp" type="button">Salin</button></div>`+
      (it.desc ? `<div class="fr-desc">${esc(it.desc)}</div>` : '')+
      (it.note ? `<div class="fr-note">${esc(it.note)}</div>` : '')+
      `<div class="fr-p">${esc(it.prompt)}</div>`+
    `</div>`;
  d.querySelector('.cp').addEventListener('click', e=>copy(it.prompt, e.currentTarget));
  return d;
}
function render(){
  [...tabs.children].forEach(b=>b.setAttribute('aria-pressed', b.dataset.id === active));
  sheets.textContent = '';
  const q = query.trim().toLowerCase();
  let shown = 0;
  CATS.filter(c=>active === 'all' || active === c.id).forEach(cat=>{
    const groups = new Map();
    cat.items.forEach(it=>{
      if(q && !(it.code + ' ' + it.prompt + ' ' + (it.desc||'') + ' ' + (it.note||'') + ' ' + it.group)
              .toLowerCase().includes(q)) return;
      if(!groups.has(it.group)) groups.set(it.group, []);
      groups.get(it.group).push(it);
    });
    groups.forEach((items, g)=>{
      shown += items.length;
      const s = document.createElement('section');
      s.innerHTML = `<div class="sect-hd"><h2>${esc(g || cat.label)}</h2>`+
                    `<span class="c">${cat.label} &middot; ${items.length}</span></div>`;
      const sh = document.createElement('div');
      sh.className = 'sheet' + (cat.id === 'preset' || cat.id === 'angle' ? ' pre' : '');
      items.forEach(it=>sh.appendChild(frame(it, cat.id)));
      s.appendChild(sh); sheets.appendChild(s);
    });
  });
  if(!shown){
    const e = document.createElement('p'); e.className = 'empty';
    e.textContent = 'Tidak ada yang cocok dengan "' + query + '".';
    sheets.appendChild(e);
  }
}
const qi = document.getElementById('q');
let t; qi.addEventListener('input', ()=>{ clearTimeout(t);
  t = setTimeout(()=>{ query = qi.value; render(); }, 120); });
render();
</script>'''

out = HTML.replace('__CORPUS__', json.dumps(corpus, ensure_ascii=False))
p = SP/'image-prompt-studio.html'
p.write_text(out)
print('bytes:', len(out))
print('title ok:', '<title>' in out[:8192])
