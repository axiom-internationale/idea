(() => {
  const canvas = document.querySelector('.constellation');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const CONNECT_DIST = 120;
  const MOUSE_RADIUS = 180;
  const MOUSE_STRENGTH = 0.012;

  const AGENT_NODES = [
    { tag: 'GS', color: '#ff6646', radius: 6, glow: 16 },
    { tag: 'CE', color: '#ff9a50', radius: 4, glow: 8 },
    { tag: 'CF', color: '#ffd36b', radius: 4, glow: 8 },
    { tag: 'CT', color: '#9c8cff', radius: 4, glow: 8 },
    { tag: 'CM', color: '#c9e76c', radius: 4, glow: 8 },
  ];

  const AMBIENT_COUNT = 22;
  let nodes = [];
  let w = 0, h = 0, dpr = 1;
  let mouse = { x: -9999, y: -9999 };
  let running = false;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    if (rect.width < 10 || rect.height < 10) return false;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = rect.width;
    h = rect.height;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return true;
  }

  function isDark() {
    return document.documentElement.dataset.theme === 'dark';
  }

  function buildNodes() {
    nodes = [];
    const cx = w / 2, cy = h / 2;

    AGENT_NODES.forEach((a, i) => {
      const angle = (i / AGENT_NODES.length) * Math.PI * 2 - Math.PI / 2;
      const spread = i === 0 ? 0 : 100 + Math.random() * 70;
      nodes.push({
        x: cx + Math.cos(angle) * spread,
        y: cy + Math.sin(angle) * spread,
        vx: (Math.random() - 0.5) * 0.15,
        vy: (Math.random() - 0.5) * 0.15,
        baseX: cx + Math.cos(angle) * spread,
        baseY: cy + Math.sin(angle) * spread,
        radius: a.radius,
        color: a.color,
        glow: a.glow,
        tag: a.tag,
        isAgent: true,
        anchorStrength: i === 0 ? 0.008 : 0.003,
      });
    });

    for (let i = 0; i < AMBIENT_COUNT; i++) {
      const margin = 40;
      const bx = margin + Math.random() * (w - margin * 2);
      const by = margin + Math.random() * (h - margin * 2);
      nodes.push({
        x: bx, y: by,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3,
        baseX: bx, baseY: by,
        radius: 1.5 + Math.random() * 1.5,
        color: null, glow: 0, tag: null,
        isAgent: false, anchorStrength: 0.001,
      });
    }
  }

  function update() {
    nodes.forEach(n => {
      n.x += n.vx;
      n.y += n.vy;
      n.vx += (n.baseX - n.x) * n.anchorStrength;
      n.vy += (n.baseY - n.y) * n.anchorStrength;

      const dx = mouse.x - n.x;
      const dy = mouse.y - n.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < MOUSE_RADIUS && dist > 1) {
        const force = (1 - dist / MOUSE_RADIUS) * MOUSE_STRENGTH;
        n.vx += dx * force;
        n.vy += dy * force;
      }

      n.vx *= 0.98;
      n.vy *= 0.98;
      if (n.x < 0) n.vx += 0.2;
      if (n.x > w) n.vx -= 0.2;
      if (n.y < 0) n.vy += 0.2;
      if (n.y > h) n.vy -= 0.2;
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    const dark = isDark();
    const lineBase = dark ? '255,255,255' : '20,20,20';
    const ambientColor = dark ? 'rgba(255,255,255,0.35)' : 'rgba(20,20,20,0.25)';

    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONNECT_DIST) {
          const alpha = (1 - dist / CONNECT_DIST) * (a.isAgent || b.isAgent ? 0.12 : 0.05);
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(${lineBase},${alpha})`;
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }

    nodes.forEach(n => {
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
      if (n.isAgent) {
        if (n.glow > 0) {
          ctx.shadowColor = n.color;
          ctx.shadowBlur = n.glow;
        }
        ctx.fillStyle = n.color;
      } else {
        ctx.shadowColor = 'transparent';
        ctx.shadowBlur = 0;
        ctx.fillStyle = ambientColor;
      }
      ctx.fill();
      ctx.shadowBlur = 0;

      if (n.tag) {
        ctx.font = '500 9px "DM Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillStyle = dark ? 'rgba(255,255,255,0.5)' : 'rgba(20,20,20,0.45)';
        ctx.fillText(n.tag, n.x, n.y - n.radius - 6);
      }
    });
  }

  function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
  }

  function start() {
    if (running) return;
    if (!resize()) return;
    running = true;
    buildNodes();
    if (prefersReduced) {
      draw();
    } else {
      loop();
    }
  }

  const heroEl = canvas.closest('.hero');
  heroEl.addEventListener('pointermove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });
  heroEl.addEventListener('pointerleave', () => {
    mouse.x = -9999;
    mouse.y = -9999;
  });

  // Try starting immediately, on load, and via polling until CSS is settled
  start();
  window.addEventListener('load', start);
  let attempts = 0;
  const poll = setInterval(() => {
    if (running || ++attempts > 20) { clearInterval(poll); return; }
    start();
  }, 100);

  window.addEventListener('resize', () => {
    if (!running) return;
    const oldW = w, oldH = h;
    if (!resize() || oldW < 1) return;
    const sx = w / oldW, sy = h / oldH;
    nodes.forEach(n => {
      n.x *= sx; n.y *= sy;
      n.baseX *= sx; n.baseY *= sy;
    });
    if (prefersReduced) draw();
  });
})();
