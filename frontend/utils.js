// Funciones puras del frontend (sin DOM) para poder probarlas con Node.
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
function normalize(s) {
  return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
}
// Prefijo usado como "raíz" aproximada para resaltar variantes (agua/aguas, café/cafetales).
function stemPrefix(w) {
  return w.length <= 4 ? w : w.slice(0, Math.max(4, w.length - 2));
}
// Resalta con <mark> las palabras de la consulta; escapa el HTML del texto.
function highlight(text, query) {
  const words = normalize(query).split(/\W+/).filter((w) => w.length > 2).map(stemPrefix);
  if (!words.length) return escapeHtml(text);
  const plain = normalize(text);
  const marks = new Array(text.length).fill(false);
  for (const w of words) {
    let i = plain.indexOf(w);
    while (i !== -1) {
      let j = i + w.length;
      while (j < plain.length && /\w/.test(plain[j])) j++;
      for (let k = i; k < j; k++) marks[k] = true;
      i = plain.indexOf(w, j);
    }
  }
  let out = '', open = false;
  for (let i = 0; i < text.length; i++) {
    if (marks[i] && !open) { out += '<mark>'; open = true; }
    if (!marks[i] && open) { out += '</mark>'; open = false; }
    out += escapeHtml(text[i]);
  }
  return out + (open ? '</mark>' : '');
}
function formatMs(ms) {
  if (ms === null || ms === undefined || Number.isNaN(ms)) return '—';
  return ms < 1 ? ms.toFixed(2) + ' ms' : ms < 100 ? ms.toFixed(1) + ' ms' : Math.round(ms) + ' ms';
}
// Proporción de documentos del top-k de A que también aparecen en B (Jaccard).
function coverage(a, b) {
  const A = new Set(a), B = new Set(b), u = new Set([...A, ...B]);
  if (!u.size) return 0;
  let inter = 0; A.forEach((x) => { if (B.has(x)) inter++; });
  return inter / u.size;
}
if (typeof module !== 'undefined') module.exports = { escapeHtml, normalize, highlight, formatMs, coverage, stemPrefix };
