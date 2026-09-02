(() => {
  const canvas = document.querySelector('.constellation');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const CONNECT_DIST = 190;
  const MOUSE_RADIUS = 250;
  const MOUSE_STRENGTH = 0.01;
  const MAX_PARTICLES = 55;
  const PARTICLE_SPAWN_RATE = 0.18;

  const AGENT_NODES = [
    { tag: 'GS', color: '#ff6646', radius: 8, glow: 24, pulseSpeed: 0.8 },
    { tag: 'CE', color: '#ff9a50', radius: 5.5, glow: 14, pulseSpeed: 1.1 },
    { tag: 'CF', color: '#ffd36b', radius: 5.5, glow: 14, pulseSpeed: 0.9 },
    { tag: 'CT', color: '#9c8cff', radius: 5.5, glow: 14, pulseSpeed: 1.0 },
    { tag: 'CM', color: '#c9e76c', radius: 5.5, glow: 14, pulseSpeed: 0.7 },
  ];

  const FAR_COUNT = 120;
  const MID_COUNT = 90;

  let nodes = [];
  let farNodes = [];
  let particles = [];
  let w = 0, h = 0, dpr = 1;
  let mouse = { x: -9999, y: -9999 };
  let running = false;
  let time = 0;

  function hexToRgba(hex, alpha) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `rgba(${r},${g},${b},${alpha})`;
  }

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
    farNodes = [];
    particles = [];
    const cx = w / 2, cy = h / 2;

    AGENT_NODES.forEach((a, i) => {
      const angle = (i / AGENT_NODES.length) * Math.PI * 2 - Math.PI / 2;
      const spread = i === 0 ? 0 : 210 + Math.random() * 150;
      nodes.push({
        x: cx + Math.cos(angle) * spread,
        y: cy + Math.sin(angle) * spread,
        vx: (Math.random() - 0.5) * 0.1,
        vy: (Math.random() - 0.5) * 0.1,
        baseX: cx + Math.cos(angle) * spread,
        baseY: cy + Math.sin(angle) * spread,
        baseRadius: a.radius,
        radius: a.radius,
        color: a.color,
        glow: a.glow,
        baseGlow: a.glow,
        tag: a.tag,
        isAgent: true,
        anchorStrength: i === 0 ? 0.008 : 0.003,
        pulseSpeed: a.pulseSpeed,
        pulsePhase: Math.random() * Math.PI * 2,
      });
    });

    for (let i = 0; i < MID_COUNT; i++) {
      const margin = 12;
      const bx = margin + Math.random() * (w - margin * 2);
      const by = margin + Math.random() * (h - margin * 2);
      nodes.push({
        x: bx, y: by,
        vx: (Math.random() - 0.5) * 0.2,
        vy: (Math.random() - 0.5) * 0.2,
        baseX: bx, baseY: by,
        baseRadius: 1.3 + Math.random() * 1.8,
        radius: 1.3 + Math.random() * 1.8,
        color: null, glow: 0, baseGlow: 0, tag: null,
        isAgent: false,
        anchorStrength: 0.0007,
      });
    }

    for (let i = 0; i < FAR_COUNT; i++) {
      farNodes.push({
        x: Math.random() * w,
        y: Math.random() * h,
        radius: 0.3 + Math.random() * 0.7,
        baseAlpha: 0.08 + Math.random() * 0.18,
        twinkleSpeed: 0.3 + Math.random() * 0.8,
        twinklePhase: Math.random() * Math.PI * 2,
      });
    }
  }

  function update() {
    time += 0.016;

    nodes.forEach(n => {
      if (n.isAgent) {
        const pulse = Math.sin(time * n.pulseSpeed + n.pulsePhase);
        n.radius = n.baseRadius + pulse * 1.5;
        n.glow = n.baseGlow + pulse * 5;
      }

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

    if (particles.length < MAX_PARTICLES && Math.random() < PARTICLE_SPAWN_RATE) {
      const a = nodes[Math.floor(Math.random() * nodes.length)];
      let closest = null, closestDist = CONNECT_DIST;
      for (let i = 0; i < nodes.length; i++) {
        if (nodes[i] === a) continue;
        const dx = a.x - nodes[i].x, dy = a.y - nodes[i].y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < closestDist) { closestDist = d; closest = nodes[i]; }
      }
      if (closest) {
        const fromAgent = a.isAgent ? a : (closest.isAgent ? closest : null);
        particles.push({
          from: a, to: closest,
          progress: 0,
          speed: 0.006 + Math.random() * 0.014,
          color: fromAgent ? fromAgent.color : null,
          radius: fromAgent ? 1.6 : 1.0,
        });
      }
    }

    particles = particles.filter(p => {
      p.progress += p.speed;
      return p.progress < 1;
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    const dark = isDark();
    const lineBase = dark ? '255,255,255' : '20,20,20';

    farNodes.forEach(fn => {
      const twinkle = 0.5 + 0.5 * Math.sin(time * fn.twinkleSpeed + fn.twinklePhase);
      const alpha = fn.baseAlpha * twinkle;
      ctx.beginPath();
      ctx.arc(fn.x, fn.y, fn.radius, 0, Math.PI * 2);
      ctx.fillStyle = dark
        ? `rgba(255,255,255,${alpha})`
        : `rgba(20,20,20,${alpha * 0.6})`;
      ctx.fill();
    });

    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist >= CONNECT_DIST) continue;

        const bothAgent = a.isAgent && b.isAgent;
        const oneAgent = a.isAgent || b.isAgent;
        let alpha, lw;

        if (bothAgent) {
          alpha = (1 - dist / CONNECT_DIST) * 0.3;
          lw = 1.6;
        } else if (oneAgent) {
          alpha = (1 - dist / CONNECT_DIST) * 0.16;
          lw = 0.9;
        } else {
          alpha = (1 - dist / CONNECT_DIST) * 0.09;
          lw = 0.5;
        }

        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);

        if (bothAgent) {
          const grad = ctx.createLinearGradient(a.x, a.y, b.x, b.y);
          grad.addColorStop(0, hexToRgba(a.color, alpha));
          grad.addColorStop(1, hexToRgba(b.color, alpha));
          ctx.strokeStyle = grad;
        } else if (oneAgent) {
          const agent = a.isAgent ? a : b;
          ctx.strokeStyle = hexToRgba(agent.color, alpha * 0.7);
        } else {
          ctx.strokeStyle = `rgba(${lineBase},${alpha})`;
        }
        ctx.lineWidth = lw;
        ctx.stroke();
      }
    }

    particles.forEach(p => {
      const x = p.from.x + (p.to.x - p.from.x) * p.progress;
      const y = p.from.y + (p.to.y - p.from.y) * p.progress;
      const fade = Math.sin(p.progress * Math.PI);

      ctx.beginPath();
      ctx.arc(x, y, p.radius, 0, Math.PI * 2);
      if (p.color) {
        ctx.shadowColor = p.color;
        ctx.shadowBlur = 8;
        ctx.fillStyle = hexToRgba(p.color, fade * 0.85);
      } else {
        ctx.shadowBlur = 3;
        ctx.shadowColor = dark ? 'rgba(255,255,255,0.3)' : 'rgba(0,0,0,0.15)';
        ctx.fillStyle = dark
          ? `rgba(255,255,255,${fade * 0.55})`
          : `rgba(20,20,20,${fade * 0.4})`;
      }
      ctx.fill();
      ctx.shadowBlur = 0;
    });

    nodes.forEach(n => {
      ctx.beginPath();
      ctx.arc(n.x, n.y, Math.max(n.radius, 0.5), 0, Math.PI * 2);
      if (n.isAgent) {
        ctx.shadowColor = n.color;
        ctx.shadowBlur = Math.max(n.glow, 0);
        ctx.fillStyle = n.color;
      } else {
        ctx.shadowColor = 'transparent';
        ctx.shadowBlur = 0;
        ctx.fillStyle = dark ? 'rgba(255,255,255,0.4)' : 'rgba(20,20,20,0.3)';
      }
      ctx.fill();
      ctx.shadowBlur = 0;

      if (n.tag) {
        ctx.font = '500 10px "DM Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillStyle = dark ? 'rgba(255,255,255,0.6)' : 'rgba(20,20,20,0.5)';
        ctx.fillText(n.tag, n.x, n.y - n.radius - 7);
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
    farNodes.forEach(fn => { fn.x *= sx; fn.y *= sy; });
    if (prefersReduced) draw();
  });
})();
