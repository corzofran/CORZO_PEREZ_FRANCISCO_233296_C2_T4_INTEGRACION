const test = require('node:test'); const assert = require('node:assert');
const { escapeHtml, highlight, formatMs, coverage, normalize } = require('../utils.js');
test('escapeHtml', () => assert.strictEqual(escapeHtml('<a href="x">&</a>'), '&lt;a href=&quot;x&quot;&gt;&amp;&lt;/a&gt;'));
test('normalize quita acentos', () => assert.strictEqual(normalize('Cañón'), 'canon'));
test('highlight ignora acentos y escapa HTML', () => {
  assert.strictEqual(highlight('El café <b>sube</b>', 'cafe'), 'El <mark>café</mark> &lt;b&gt;sube&lt;/b&gt;');
});
test('highlight marca variantes', () => assert.ok(highlight('Las cafeterias abren', 'cafetal').includes('<mark>cafeterias</mark>')));
test('highlight sin palabras útiles', () => assert.strictEqual(highlight('a b', 'de'), 'a b'));
test('formatMs', () => { assert.strictEqual(formatMs(0.123), '0.12 ms'); assert.strictEqual(formatMs(12.34), '12.3 ms'); assert.strictEqual(formatMs(250.4), '250 ms'); assert.strictEqual(formatMs(null), '—'); });
test('coverage Jaccard', () => { assert.strictEqual(coverage(['a', 'b'], ['b', 'c']), 1 / 3); assert.strictEqual(coverage([], []), 0); });
