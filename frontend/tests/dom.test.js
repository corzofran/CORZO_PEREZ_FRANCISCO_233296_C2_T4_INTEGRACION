// Prueba de integración: el frontend real contra la API real (BASE_URL). Se omite si no hay servidor.
const test = require('node:test'); const assert = require('node:assert');
const { JSDOM } = require('jsdom'); const fs = require('fs'); const path = require('path');
const BASE = process.env.BASE_URL || 'http://127.0.0.1:8000';
test('flujo completo en el DOM', { skip: !process.env.BASE_URL && 'define BASE_URL para correr esta prueba' }, async () => {
  const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8').replace(/<script[^>]*><\/script>/g, '');
  const dom = new JSDOM(html, { url: BASE + '/?q=marimba&engine=bm25', runScripts: 'outside-only', pretendToBeVisual: true });
  const w = dom.window; w.fetch = (u, o) => fetch(new URL(u, BASE), o);
  w.eval(fs.readFileSync(path.join(__dirname, '..', 'utils.js'), 'utf8'));
  w.eval(fs.readFileSync(path.join(__dirname, '..', 'app.js'), 'utf8'));
  const esperar = async (cond, ms = 5000) => { const t = Date.now(); while (Date.now() - t < ms) { if (cond()) return; await new Promise((r) => setTimeout(r, 50)); } throw new Error('timeout'); };
  const d = w.document;
  await esperar(() => d.querySelectorAll('#engine-picker button').length === 4);
  assert.strictEqual(d.querySelectorAll('#engine-picker button.on').length, 1);
  await esperar(() => d.querySelectorAll('#results .card').length > 0);
  assert.ok(d.querySelector('#results mark'), 'debe resaltar la consulta');
  assert.match(d.querySelector('#meta').textContent, /resultados/);
  d.querySelector('[data-tab=comparar]').click();
  await esperar(() => d.querySelectorAll('#cmp section').length === 4);
  d.querySelector('[data-tab=latencia]').click();
  await esperar(() => d.querySelectorAll('#lat tbody tr').length >= 1 && /\d/.test(d.querySelector('#lat tbody').textContent));
});
