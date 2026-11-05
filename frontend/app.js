(function () {
  const $ = (s) => document.querySelector(s);
  const EJEMPLOS = ['Cañón del Sumidero', 'temblor fuerte', 'enfermedad transmitida por zancudos', 'exportación de café orgánico', 'robótica en escuelas', 'cacao y chocolate'];
  const state = { engine: 'bm25', engines: [], tab: 'buscar' };
  const api = async (path, opts) => { const r = await fetch('/api' + path, opts); if (!r.ok) throw new Error(r.status); return r.json(); };

  function card(r, q) {
    return `<article class="card"><h3><a href="#" data-doc="${escapeHtml(r.id)}">${highlight(r.titulo, q)}</a></h3>
      <p>${highlight(r.snippet, q)}</p><small>${escapeHtml(r.id)} · ${escapeHtml(r.tema)} · score ${r.score}</small></article>`;
  }
  function buildEnginePicker() {
    const box = $('#engine-picker'); box.innerHTML = '';
    state.engines.forEach((e) => {
      const b = document.createElement('button'); b.type = 'button'; b.dataset.engine = e.id; b.title = e.description;
      b.textContent = e.label; b.className = e.id === state.engine ? 'on' : '';
      b.addEventListener('click', () => { state.engine = e.id; syncPicker(); run(); });
      box.appendChild(b);
    });
  }
  function syncPicker() { document.querySelectorAll('#engine-picker button').forEach((b) => b.classList.toggle('on', b.dataset.engine === state.engine)); }
  function setTab(t) {
    state.tab = t;
    document.querySelectorAll('.tabs button').forEach((b) => b.classList.toggle('active', b.dataset.tab === t));
    document.querySelectorAll('.panel').forEach((p) => p.classList.toggle('active', p.id === 'tab-' + t));
    run();
  }
  async function run() {
    const q = $('#q').value.trim();
    history.replaceState(null, '', q ? `?q=${encodeURIComponent(q)}&engine=${state.engine}` : location.pathname);
    try {
      if (state.tab === 'latencia') return loadStats();
      if (!q) return;
      if (state.tab === 'buscar') {
        const d = await api(`/search?q=${encodeURIComponent(q)}&engine=${state.engine}&k=5`);
        $('#meta').textContent = `${d.total} resultados · ${formatMs(d.took_ms)} en el servidor`;
        $('#results').innerHTML = d.results.length ? d.results.map((r) => card(r, q)).join('') : '<p class="empty">Sin resultados para este motor.</p>';
      } else {
        const d = await api(`/compare?q=${encodeURIComponent(q)}&k=5`);
        $('#cmp-meta').textContent = 'Solapamiento (Jaccard) entre motores: ' + Object.entries(d.jaccard).map(([k, v]) => `${k.replace('|', '↔')} ${v}`).join(' · ');
        $('#cmp').innerHTML = Object.entries(d.engines).map(([n, v]) => {
          const e = state.engines.find((x) => x.id === n);
          return `<section><h2>${escapeHtml(e ? e.label : n)} <small>${formatMs(v.took_ms)}</small></h2>${v.results.length ? v.results.map((r) => card(r, q)).join('') : '<p class="empty">Sin resultados.</p>'}</section>`;
        }).join('');
      }
    } catch (e) { $('#meta').textContent = 'Error al consultar la API: ' + e.message; }
  }
  async function loadStats() {
    const s = await api('/stats'); const tb = $('#lat tbody');
    tb.innerHTML = Object.entries(s.latency_ms).map(([n, v]) => `<tr><td>${escapeHtml(n)}</td><td>${v.count}</td><td>${formatMs(v.p50)}</td><td>${formatMs(v.p95)}</td><td>${formatMs(v.p99)}</td></tr>`).join('') || '<tr><td colspan="5">Aún no hay búsquedas.</td></tr>';
  }
  async function openDoc(id) {
    const d = await api('/documents/' + encodeURIComponent(id));
    $('#dlg-t').textContent = d.titulo; $('#dlg-x').textContent = d.texto; $('#dlg-f').textContent = d.fuente;
    const dlg = $('#dlg'); dlg.showModal ? dlg.showModal() : dlg.setAttribute('open', '');
  }
  async function init() {
    $('#examples').innerHTML = EJEMPLOS.map((e) => `<button type="button" class="chip">${escapeHtml(e)}</button>`).join('');
    $('#examples').addEventListener('click', (ev) => { if (ev.target.classList.contains('chip')) { $('#q').value = ev.target.textContent; run(); } });
    $('#form').addEventListener('submit', (ev) => { ev.preventDefault(); run(); });
    document.querySelectorAll('.tabs button').forEach((b) => b.addEventListener('click', () => setTab(b.dataset.tab)));
    $('#results').addEventListener('click', (ev) => { const a = ev.target.closest('a[data-doc]'); if (a) { ev.preventDefault(); openDoc(a.dataset.doc); } });
    $('#cmp').addEventListener('click', (ev) => { const a = ev.target.closest('a[data-doc]'); if (a) { ev.preventDefault(); openDoc(a.dataset.doc); } });
    $('#reset').addEventListener('click', async () => { await api('/stats/reset', { method: 'POST' }); loadStats(); });
    try { state.engines = await api('/engines'); } catch (e) { $('#meta').textContent = 'No se pudo contactar la API.'; return; }
    const p = new URLSearchParams(location.search);
    if (p.get('engine') && state.engines.some((e) => e.id === p.get('engine'))) state.engine = p.get('engine');
    if (p.get('q')) $('#q').value = p.get('q');
    buildEnginePicker();
    if ($('#q').value) run();
  }
  window.__app = { init, run, state };
  document.addEventListener('DOMContentLoaded', init);
  if (document.readyState !== 'loading') init();
})();
