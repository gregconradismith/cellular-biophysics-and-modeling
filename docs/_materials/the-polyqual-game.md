---
title: "The PolyQual Game!"
kind: "page"
date: "1970-01-01"
slug: "the-polyqual-game"
permalink: "/pages/the-polyqual-game/"
render_with_liquid: false
---

<iframe class="embedded-page" title="Embedded interactive content" srcdoc="&lt;!-- wp:paragraph --&gt;
&lt;p&gt;&lt;/p&gt;
&lt;!-- /wp:paragraph --&gt;

&lt;!-- wp:html --&gt;
&lt;!doctype html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;title&gt;Polyqual (Qualitative Analysis Quiz)&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;style&gt;:root { --pad: 14px; --bg: #0b0c10; --card: #121319; --ink: #e8ecf1; --muted:#9aa4b2; }
    * { box-sizing: border-box; }
    body { margin:0; background:var(--bg); color:var(--ink); font:16px/1.45 system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }.wrap { max-width: 980px; margin: 24px auto; padding: 0 14px; }.card { background:var(--card); border:1px solid #22242d; border-radius:18px; padding: var(--pad); box-shadow: 0 12px 30px rgba(0,0,0,.35); position: relative; }
    h1 { margin: 0 0 8px; font-weight: 700; letter-spacing:.2px; }
    p  { margin: 0 0 16px; color: var(--muted); }.row { display:flex; gap:10px; flex-wrap:wrap; margin: 10px 0 6px; align-items:center; position: relative; z-index: 2; }
    button, label { font-size: 15px; }
    button {
      background:#1c1f2a; color:var(--ink); border:1px solid #2a2f3a; padding:10px 14px; border-radius:12px; cursor:pointer;
      -webkit-tap-highlight-color: transparent; user-select: none;
    }
    button:hover { filter: brightness(1.08); }
    button:active { transform: translateY(1px); }
    button[disabled] { opacity:.6; cursor: not-allowed; }
    canvas { width:100%; height:auto; background:#0f1117; border-radius:14px; border:1px solid #22242d; display:block; position: relative; z-index: 1; }.grid { display:grid; grid-template-columns:1fr; gap:10px; }.status { min-height: 24px; margin-top: 8px; }.codes { display:flex; gap:14px; margin-top:8px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }.mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; white-space: pre; }.hidden { display: none !important; }.spacer { flex: 1 1 auto; }.score { font-weight: 600; letter-spacing:.2px; }.score small { color: var(--muted); font-weight: 500; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class=&quot;wrap&quot;&gt;
  &lt;div class=&quot;card&quot;&gt;
    &lt;h1&gt;Polyqual (Qualitative Analysis Quiz)&lt;/h1&gt;
    &lt;p&gt;Two random, related polynomials are generated. Decide if their qualitative sign patterns of
      &lt;span class=&quot;mono&quot;&gt;f, f&#x27;, f&#x27;&#x27;&lt;/span&gt; match. Choose an answer to reveal the stair plots and symbol tables.&lt;/p&gt;

    &lt;div class=&quot;row&quot;&gt;
      &lt;button id=&quot;new&quot; type=&quot;button&quot; onclick=&quot;newPair()&quot;&gt;New Pair&lt;/button&gt;
      &lt;button id=&quot;guessSimilar&quot; type=&quot;button&quot; onclick=&quot;handleGuess(&#x27;similar&#x27;)&quot;&gt;Qualitatively Similar&lt;/button&gt;
      &lt;button id=&quot;guessDifferent&quot; type=&quot;button&quot; onclick=&quot;handleGuess(&#x27;different&#x27;)&quot;&gt;Qualitatively Different&lt;/button&gt;
      &lt;div class=&quot;spacer&quot;&gt;&lt;/div&gt;
      &lt;span id=&quot;score&quot; class=&quot;score&quot;&gt;Score: 0 / 0 &lt;small&gt;(0%)&lt;/small&gt;&lt;/span&gt;
      &lt;button id=&quot;resetScore&quot; type=&quot;button&quot; onclick=&quot;resetScore()&quot;&gt;Reset Score&lt;/button&gt;
    &lt;/div&gt;
    &lt;div class=&quot;row&quot;&gt;
      &lt;label&gt;&lt;input type=&quot;checkbox&quot; id=&quot;showF&quot; onchange=&quot;if(window.revealed) render()&quot;&gt; Show stair row for &lt;span class=&quot;mono&quot;&gt;sign(f)&lt;/span&gt;&lt;/label&gt;
      &lt;button id=&quot;download&quot; type=&quot;button&quot; title=&quot;Download current plots as a PNG&quot; onclick=&quot;downloadPNG()&quot; disabled&gt;Download PNG&lt;/button&gt;
    &lt;/div&gt;

    &lt;div class=&quot;grid&quot;&gt;
      &lt;canvas id=&quot;plot&quot; width=&quot;1100&quot; height=&quot;360&quot; aria-label=&quot;Polynomial plot&quot;&gt;&lt;/canvas&gt;
      &lt;canvas id=&quot;stairs&quot; width=&quot;1100&quot; height=&quot;220&quot; aria-label=&quot;Sign stair plots&quot;&gt;&lt;/canvas&gt;
    &lt;/div&gt;

    &lt;div class=&quot;status&quot; id=&quot;status&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
    &lt;div class=&quot;codes&quot; id=&quot;codes&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
/* ---------------- Utilities ---------------- */
const rng = () =&gt; Math.random();
const randn = (() =&gt; { // Box-Muller
  let spare = null;
  return () =&gt; {
    if (spare !== null) { const v = spare; spare = null; return v; }
    let u=0, v=0, s=0;
    do { u = Math.random()*2-1; v = Math.random()*2-1; s = u*u + v*v; } while (!s || s&gt;=1);
    const mul = Math.sqrt(-2*Math.log(s)/s);
    spare = v*mul;
    return u*mul;
  };
})();

function polyval(coeffs, x) {
  // coeffs in descending powers (MATLAB style)
  let y = 0, n = coeffs.length;
  for (let i=0;i&lt;n;i++) y = y*x + coeffs[i];
  return y;
}
function polyder(coeffs) {
  const n = coeffs.length;
  if (n &lt;= 1) return [0];
  const d = new Array(n-1);
  for (let i=0;i&lt;n-1;i++) d[i] = coeffs[i]*(n-1-i);
  return d;
}
function sign(v) { return v&gt;0 ? 1: v&lt;0 ? -1: 0; }
function mapSignToChar(v) { return v===-1?&#x27;-&#x27;:(v===0?&#x27;x&#x27;:&#x27;+&#x27;); }
const sameShape = (a,b)=&gt; a.length===b.length &amp;&amp; a.every((ch,i)=&gt;ch===b[i]);

function compressByChange(sp, sdp, sddp) {
  // Append a new column when ANY of the three streams changes (matches MATLAB loop)
  const spA=[sp[0]], sdpA=[sdp[0]], sddpA=[sddp[0]];
  for (let i=1;i&lt;sp.length;i++) {
    if (spA[spA.length-1]!==sp[i] || sdpA[sdpA.length-1]!==sdp[i] || sddpA[sddpA.length-1]!==sddp[i]) {
      spA.push(sp[i]); sdpA.push(sdp[i]); sddpA.push(sddp[i]);
    }
  }
  return { spA, sdpA, sddpA };
}

/* ---------------- Model (single round) ---------------- */
const params = { sigma: 5, wiggleFactor: 0.5, offset: 10 };
const X = Array.from({length: 201}, (_,i)=&gt; -1 + i*0.01); // -1:0.01:1

function makeRound() {
  const {sigma, wiggleFactor, offset} = params;
  const N = 2 + (1 + Math.floor(rng()*3)); // 3..5
  const a1 = Array.from({length:N}, ()=&gt; sigma*randn());
  const a2 = a1.map(c =&gt; c + (sigma*wiggleFactor)*randn()); // a2 = a1 + wiggle*randn

  const da1 = polyder(a1), da2 = polyder(a2);
  const dda1 = polyder(da1), dda2 = polyder(da2);

  const p1 = X.map(x =&gt; offset + polyval(a1, x));
  const p2 = X.map(x =&gt; offset + polyval(a2, x));
  const dp1 = X.map(x =&gt; polyval(da1, x));
  const dp2 = X.map(x =&gt; polyval(da2, x));
  const ddp1= X.map(x =&gt; polyval(dda1, x));
  const ddp2= X.map(x =&gt; polyval(dda2, x));

  const sp1   = p1.map(sign),  sp2   = p2.map(sign);
  const sdp1  = dp1.map(sign), sdp2  = dp2.map(sign);
  const sddp1 = ddp1.map(sign),sddp2 = ddp2.map(sign);

  const c1 = compressByChange(sp1, sdp1, sddp1);
  const c2 = compressByChange(sp2, sdp2, sddp2);

  const blueRows = [
    c1.spA.map(mapSignToChar).join(&#x27;&#x27;),   // f
    c1.sdpA.map(mapSignToChar).join(&#x27;&#x27;),  // f&#x27;
    c1.sddpA.map(mapSignToChar).join(&#x27;&#x27;)  // f&#x27;&#x27;
  ];
  const redRows = [
    c2.spA.map(mapSignToChar).join(&#x27;&#x27;),
    c2.sdpA.map(mapSignToChar).join(&#x27;&#x27;),
    c2.sddpA.map(mapSignToChar).join(&#x27;&#x27;)
  ];

  return { p1, p2, sp1, sp2, sdp1, sdp2, sddp1, sddp2, blueRows, redRows };
}

function decideVerdict(round, useF) {
  const samePrime   = sameShape(round.blueRows[1], round.redRows[1]);
  const sameDPrime  = sameShape(round.blueRows[2], round.redRows[2]);
  if (useF) {
    const sameF = sameShape(round.blueRows[0], round.redRows[0]);
    return (sameF &amp;&amp; samePrime &amp;&amp; sameDPrime) ? &#x27;qualitatively similar&#x27;: &#x27;qualitatively different&#x27;;
  } else {
    return (samePrime &amp;&amp; sameDPrime) ? &#x27;qualitatively similar&#x27;: &#x27;qualitatively different&#x27;;
  }
}

/* ---------------- View: drawing ---------------- */
function drawCurves(ctx, X, y1, y2) {
  const W = ctx.canvas.width, H = ctx.canvas.height;
  ctx.clearRect(0,0,W,H);

  // compute bounds
  const all = y1.concat(y2);
  const ymax = Math.max(0,...all), ymin = Math.min(0,...all);
  const pad = 0.08*(ymax - ymin || 1);
  const yhi = ymax + pad, ylo = ymin - pad;

  // scales
  const toX = t =&gt; ( (t+1)/2 ) * (W-24) + 12;
  const toY = y =&gt; H - ( (y - ylo)/(yhi - ylo) ) * (H-24) - 12;

  // dashed green zero line
  ctx.save();
  ctx.lineWidth = 1.5; ctx.strokeStyle = &#x27;#00cc66&#x27;; ctx.setLineDash([6,4]);
  ctx.beginPath(); ctx.moveTo(12, toY(0)); ctx.lineTo(W-12, toY(0)); ctx.stroke();
  ctx.restore();

  // curves
  ctx.lineWidth = 2.2;

  ctx.strokeStyle = &#x27;#5fb0ff&#x27;; // blue first
  ctx.beginPath();
  ctx.moveTo(toX(X[0]), toY(y1[0]));
  for (let i=1;i&lt;X.length;i++) ctx.lineTo(toX(X[i]), toY(y1[i]));
  ctx.stroke();

  ctx.strokeStyle = &#x27;#ff6b6b&#x27;; // red second
  ctx.beginPath();
  ctx.moveTo(toX(X[0]), toY(y2[0]));
  for (let i=1;i&lt;X.length;i++) ctx.lineTo(toX(X[i]), toY(y2[i]));
  ctx.stroke();
}

function drawStairs(ctx, X, s1, s2, label) {
  const W = ctx.canvas.width, H = ctx.canvas.height;
  ctx.clearRect(0,0,W,H);

  const pad = 22;                   // inner top/bottom padding (for labels &amp; breathing room)
  const usableH = Math.max(20, H - 2*pad);
  const mid = pad + usableH/2;
  const spread = usableH * 0.38;    // distance of ±1 from the zero line

  const toX = t =&gt; ((t+1)/2)*(W-24) + 12;
  const toY = v =&gt; (v===1) ? (mid - spread): (v===-1 ? (mid + spread): mid);

  // dashed green zero line at y = mid
  ctx.save();
  ctx.strokeStyle = &#x27;#00cc66&#x27;;
  ctx.setLineDash([6, 4]);
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(12, mid);
  ctx.lineTo(W-12, mid);
  ctx.stroke();
  ctx.restore();

  // stairs helper: first series solid, second series dashed so both are visible
  function stairs(arr, color, dashed=false) {
    ctx.save();
    ctx.strokeStyle = color;
    ctx.lineWidth = 2.8;
    ctx.lineCap = &#x27;round&#x27;;
    ctx.lineJoin = &#x27;round&#x27;;
    if (dashed) ctx.setLineDash([6,4]);
    ctx.beginPath();
    let xPrev = toX(X[0]), yPrev = toY(arr[0]);
    ctx.moveTo(xPrev, yPrev);
    for (let i=1;i&lt;X.length;i++) {
      const x = toX(X[i]), y = toY(arr[i]);
      ctx.lineTo(x, yPrev);      // horizontal step
      if (y !== yPrev) ctx.lineTo(x, y); // vertical jump
      yPrev = y;
    }
    ctx.stroke();
    ctx.restore();
  }

  stairs(s1, &#x27;#5fb0ff&#x27;, false); // blue first (solid)
  stairs(s2, &#x27;#ff6b6b&#x27;, true);  // red second (dashed)

  // bigger label
  ctx.fillStyle = &#x27;#c7cfdd&#x27;;
  ctx.font = &#x27;bold 18px ui-monospace, Menlo, Consolas, monospace&#x27;;
  ctx.fillText(label, 14, pad - 4);
}

/* ---------------- Controller / UI ---------------- */
const plotEl = document.getElementById(&#x27;plot&#x27;);
const stairsEl = document.getElementById(&#x27;stairs&#x27;);
const statusEl = document.getElementById(&#x27;status&#x27;);
const codesEl = document.getElementById(&#x27;codes&#x27;);
const showF = document.getElementById(&#x27;showF&#x27;);
const scoreEl = document.getElementById(&#x27;score&#x27;);

let round = null;
window.revealed = false; // make accessible in inline handlers
let correctCount = 0;
let totalCount = 0;

function pct(a, b) { return b ? Math.round((a/b)*100): 0; }
function updateScore() {
  scoreEl.innerHTML = `Score: ${correctCount} / ${totalCount} &lt;small&gt;(${pct(correctCount,totalCount)}%)&lt;/small&gt;`;
}

function render() {
  const ctxPlot = plotEl.getContext(&#x27;2d&#x27;);
  drawCurves(ctxPlot, X, round.p1, round.p2);

  const shouldShowDetails = window.revealed;
  stairsEl.classList.toggle(&#x27;hidden&#x27;, !shouldShowDetails);
  codesEl.classList.toggle(&#x27;hidden&#x27;, !shouldShowDetails);

  // enable/disable guess + download
  document.getElementById(&#x27;guessSimilar&#x27;).disabled = shouldShowDetails;
  document.getElementById(&#x27;guessDifferent&#x27;).disabled = shouldShowDetails;
  document.getElementById(&#x27;download&#x27;).disabled = !shouldShowDetails;

  if (shouldShowDetails) {
    // Build rows top→bottom
    const rows = [];
    if (showF.checked) rows.push({ s1: round.sp1,   s2: round.sp2,   label: &quot;f&quot;  });
    rows.push({          s1: round.sdp1,  s2: round.sdp2,  label: &quot;f&#x27;&quot; });
    rows.push({          s1: round.sddp1, s2: round.sddp2, label: &quot;f&#x27;&#x27;&quot; });

    // enforce a minimum height per row
    const N = rows.length;
    const gap = 6;
    const MIN_PER_ROW = 110;
    const neededH = N * MIN_PER_ROW + (N-1) * gap;
    stairsEl.height = Math.max(neededH, 220); // allow growth

    const sctx = stairsEl.getContext(&#x27;2d&#x27;);
    sctx.clearRect(0, 0, stairsEl.width, stairsEl.height);

    const eachH = Math.floor((stairsEl.height - gap*(N-1)) / N);

    let yOffset = 0;
    for (let i=0; i&lt;N; i++) {
      const off = document.createElement(&#x27;canvas&#x27;);
      off.width = stairsEl.width;
      off.height = eachH;
      const octx = off.getContext(&#x27;2d&#x27;);
      drawStairs(octx, X, rows[i].s1, rows[i].s2, rows[i].label);
      sctx.drawImage(off, 0, yOffset);
      yOffset += eachH + gap;
    }

    // verdict + symbol table
    statusEl.textContent = (round._lastGuessResult || &#x27;&#x27;);

    const mkCol = (title, blueRow, redRow) =&gt; {
      const col = document.createElement(&#x27;div&#x27;);
      col.innerHTML = `&lt;div class=&quot;mono&quot; style=&quot;opacity:.7&quot;&gt;${title}&lt;/div&gt;
        &lt;div class=&quot;mono&quot; style=&quot;color:#5fb0ff;&quot;&gt;${blueRow}&lt;/div&gt;
        &lt;div class=&quot;mono&quot; style=&quot;color:#ff6b6b;&quot;&gt;${redRow}&lt;/div&gt;`;
      return col;
    };
    codesEl.innerHTML = &#x27;&#x27;;
    if (showF.checked) codesEl.appendChild(mkCol(&#x27;f&#x27;,  round.blueRows[0], round.redRows[0]));
    codesEl.appendChild(mkCol(&quot;f&#x27;&quot;,  round.blueRows[1], round.redRows[1]));
    codesEl.appendChild(mkCol(&quot;f&#x27;&#x27;&quot;, round.blueRows[2], round.redRows[2]));
  } else {
    statusEl.textContent = &quot;Are they qualitatively similar?&quot;;
    codesEl.innerHTML = &#x27;&#x27;;
  }
}

function newPair() {
  round = makeRound();
  window.revealed = false;
  round._lastGuessResult = &#x27;&#x27;;
  render();
}

function handleGuess(guess) {
  const currentVerdict = decideVerdict(round, showF.checked); // use f only if checkbox is on
  const correct = (currentVerdict === &#x27;qualitatively similar&#x27; &amp;&amp; guess === &#x27;similar&#x27;) ||
                  (currentVerdict === &#x27;qualitatively different&#x27; &amp;&amp; guess === &#x27;different&#x27;);

  totalCount += 1;
  if (correct) correctCount += 1;
  updateScore();

  round._lastGuessResult = correct
    ? &#x27;✅ Correct&#x27;: `❌ Incorrect — it is ${currentVerdict}.`;

  window.revealed = true;
  render();
}

function resetScore() {
  correctCount = 0;
  totalCount = 0;
  updateScore();
}

function downloadPNG() {
  // Compose plot + stairs into a single image
  const w = plotEl.width;
  const hPlot = plotEl.height;
  const hStairs = stairsEl.classList.contains(&#x27;hidden&#x27;) ? 0: stairsEl.height;
  const gap = 8;

  const out = document.createElement(&#x27;canvas&#x27;);
  out.width = w;
  out.height = hPlot + (hStairs ? gap + hStairs: 0);

  const octx = out.getContext(&#x27;2d&#x27;);

  // dark background (match canvas)
  octx.fillStyle = &#x27;#0f1117&#x27;;
  octx.fillRect(0, 0, out.width, out.height);

  octx.drawImage(plotEl, 0, 0);
  if (hStairs) octx.drawImage(stairsEl, 0, hPlot + gap);

  const link = document.createElement(&#x27;a&#x27;);
  link.download = &#x27;polyqual_round.png&#x27;;
  link.href = out.toDataURL(&#x27;image/png&#x27;);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

/* first load */
updateScore();
newPair();

/* Keyboard shortcuts */
window.addEventListener(&#x27;keydown&#x27;, (e) =&gt; {
  if (e.key === &#x27;Enter&#x27;) newPair();
  if (e.key.toLowerCase() === &#x27;s&#x27; &amp;&amp; !document.getElementById(&#x27;guessSimilar&#x27;).disabled) handleGuess(&#x27;similar&#x27;);
  if (e.key.toLowerCase() === &#x27;d&#x27; &amp;&amp; !document.getElementById(&#x27;guessDifferent&#x27;).disabled) handleGuess(&#x27;different&#x27;);
});
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

&lt;!-- /wp:html --&gt;

&lt;!-- wp:paragraph --&gt;
&lt;p&gt;No worries... an exam question that involves qualitative analysis will not involve subtle differences that are difficult to see.  That sometimes happens above.  &lt;/p&gt;
&lt;!-- /wp:paragraph --&gt;"></iframe>
