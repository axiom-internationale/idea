// Templatized Law Firm AI Health Report.
// Reads per-company data from a JSON sidecar passed via:
//   typst compile report_template.typ out.pdf --input data=path/to/company.json

#let data = json(sys.inputs.at("data"))

#set page(
  width: 420mm,
  height: 297mm,
  margin: 0pt,
)

#set text(font: "Arial")

#let coral = rgb("#F4603E")
#let warm-orange = rgb("#FF8C42")
#let deep-coral = rgb("#D94E2E")
#let dark-burnt = rgb("#B8381E")
#let charcoal = rgb("#2D2D2D")
#let soft-black = rgb("#3A3A3A")
#let light-grey = rgb("#F5F5F5")
#let mid-grey = rgb("#E0E0E0")
#let warm-white = rgb("#FFF9F6")
#let white-bright = white.transparentize(20%)
#let white-label = white.transparentize(15%)
#let white-grid = white.transparentize(55%)
#let white-soft = white.transparentize(40%)

// Shorthand for the three problems
#let p1 = data.problems.at(0)
#let p2 = data.problems.at(1)
#let p3 = data.problems.at(2)

#grid(
  columns: (210mm, 210mm),
  rows: 297mm,

  // ========== LEFT PAGE ==========
  box(width: 210mm, height: 297mm, fill: white, clip: true)[
    // Subtle warm tint at top
    #place(left + top, dx: 0mm, dy: 0mm,
      rect(width: 210mm, height: 60mm,
        fill: gradient.linear(warm-white, white, dir: ttb)))

    // Top accent bar — thin coral gradient strip
    #place(left + top, dx: 0mm, dy: 0mm,
      rect(width: 210mm, height: 2.5pt,
        fill: gradient.linear(coral, warm-orange, dir: ltr)))

    // Top-left decorative circle cluster
    #place(left + top, dx: -14mm, dy: -14mm,
      circle(radius: 32mm, fill: light-grey.transparentize(30%)))
    #place(left + top, dx: -6mm, dy: -6mm,
      circle(radius: 18mm, fill: coral.transparentize(94%)))

    // Top-right decorative ring
    #place(right + top, dx: 25mm, dy: -20mm,
      circle(radius: 40mm, stroke: 0.3pt + mid-grey.transparentize(50%), fill: none))
    #place(right + top, dx: 25mm, dy: -20mm,
      circle(radius: 28mm, fill: light-grey.transparentize(60%)))

    // Logo
    #place(left + top, dx: 16mm, dy: 14mm,
      image("../../src/website/media/mini_sun.png", width: 18mm),
    )
    // Company name
    #place(right + top, dx: -16mm, dy: 14mm,
      align(right)[
        #text(size: 14pt, weight: "bold", fill: charcoal, tracking: 0.5pt)[Axiom]\
        #text(size: 14pt, weight: "bold", fill: charcoal, tracking: 0.5pt)[Intelligence]\
        #text(size: 14pt, weight: "bold", fill: charcoal, tracking: 0.5pt)[Inc.]
      ],
    )
    // Gradient accent line under header
    #place(left + top, dx: 16mm, dy: 38mm,
      line(length: 178mm, stroke: 0.6pt + gradient.linear(coral.transparentize(40%), mid-grey, dir: ltr)))

    // Report type label — left-aligned below location line
    #place(left + top, dx: 16mm, dy: 66mm,
      text(size: 8pt, fill: soft-black.transparentize(30%), tracking: 1pt)[LAW FIRM AI HEALTH REPORT]
    )
    // Date — right-aligned on same line
    #place(right + top, dx: -16mm, dy: 66mm,
      text(size: 8pt, fill: soft-black.transparentize(30%), tracking: 1pt)[#data.report_date]
    )

    // Client name
    #place(left + top, dx: 16mm, dy: 43mm,
      text(size: 26pt, weight: "bold", fill: charcoal)[#data.firm_name]
    )

    // Practice area pill + location
    #place(left + top, dx: 16mm, dy: 56mm)[
      #box(fill: coral.transparentize(85%), inset: (x: 8pt, y: 4pt), radius: 4pt,
        stroke: 0.3pt + coral.transparentize(60%),
        text(size: 9pt, weight: "bold", fill: deep-coral)[#data.practice_area]
      )
      #h(6pt)
      #text(size: 9pt, fill: soft-black.transparentize(30%))[#data.city_state · #data.zip_code]
    ]

    // Gradient divider
    #place(left + top, dx: 16mm, dy: 73mm,
      line(length: 178mm, stroke: 0.6pt + gradient.linear(coral.transparentize(40%), mid-grey, dir: ltr)))

    // Subtle warm wash behind content section
    #place(left + top, dx: 12mm, dy: 73mm,
      rect(width: 186mm, height: 206mm, radius: 14pt,
        fill: gradient.linear(coral.transparentize(97%), white.transparentize(100%), dir: ttb)))

    // Decorative accent circle — right-side depth
    #place(right + top, dx: -5mm, dy: 120mm,
      circle(radius: 32mm, fill: coral.transparentize(95%)))
    #place(right + top, dx: -5mm, dy: 120mm,
      circle(radius: 32mm, stroke: 0.3pt + coral.transparentize(90%), fill: none))

    // Decorative accent circle — bottom-left balance
    #place(left + bottom, dx: -12mm, dy: 25mm,
      circle(radius: 22mm, fill: coral.transparentize(96%)))
    #place(left + bottom, dx: -12mm, dy: 25mm,
      circle(radius: 22mm, stroke: 0.2pt + coral.transparentize(92%), fill: none))

    // Section header — coral banner with gradient
    #place(left + top, dx: 16mm, dy: 78mm)[
      #box(width: 178mm,
        fill: gradient.linear(coral, deep-coral, dir: ltr),
        inset: (x: 12pt, y: 8pt), radius: 6pt,
        text(size: 10pt, weight: "bold", fill: white, tracking: 2pt)[WHERE YOUR FIRM IS LOSING CLIENTS?]
      )
    ]


    // Problem 1 — with numbered badge
    #place(left + top, dx: 16mm, dy: 93mm)[
      #place(dx: 2.5pt, dy: 2.5pt)[
        #box(width: 178mm, height: 100%, radius: 8pt, fill: mid-grey.transparentize(50%))
      ]
      #box(width: 178mm, inset: (left: 14pt, top: 10pt, bottom: 10pt, right: 10pt), radius: 8pt,
        fill: warm-white,
        stroke: (left: 3.5pt + coral, top: 0.5pt + mid-grey, right: 0.5pt + mid-grey, bottom: 0.5pt + mid-grey))[
        #grid(columns: (18pt, 1fr), column-gutter: 8pt, align: (center + horizon, left),
          box(width: 18pt, height: 18pt, radius: 9pt,
            fill: gradient.linear(coral, deep-coral, dir: ttb), stroke: none,
            align(center + horizon, text(size: 8pt, weight: "bold", fill: white)[1])
          ),
          text(size: 7pt, weight: "bold", fill: deep-coral, tracking: 0.5pt)[PROBLEM]
        )
        #v(4pt)
        #text(size: 13pt, weight: "bold", fill: charcoal)[#p1.headline]\
        #v(5pt)
        #text(size: 9pt, fill: coral)[#sym.circle.filled.small ]
        #text(size: 9pt, fill: soft-black.transparentize(15%))[*What we saw:* #p1.evidence]
      ]
    ]

    // Problem 2 — with numbered badge
    #place(left + top, dx: 16mm, dy: 130mm)[
      #place(dx: 2.5pt, dy: 2.5pt)[
        #box(width: 178mm, height: 100%, radius: 8pt, fill: mid-grey.transparentize(50%))
      ]
      #box(width: 178mm, inset: (left: 14pt, top: 10pt, bottom: 10pt, right: 10pt), radius: 8pt,
        fill: warm-white,
        stroke: (left: 3.5pt + coral, top: 0.5pt + mid-grey, right: 0.5pt + mid-grey, bottom: 0.5pt + mid-grey))[
        #grid(columns: (18pt, 1fr), column-gutter: 8pt, align: (center + horizon, left),
          box(width: 18pt, height: 18pt, radius: 9pt,
            fill: gradient.linear(coral, deep-coral, dir: ttb), stroke: none,
            align(center + horizon, text(size: 8pt, weight: "bold", fill: white)[2])
          ),
          text(size: 7pt, weight: "bold", fill: deep-coral, tracking: 0.5pt)[PROBLEM]
        )
        #v(4pt)
        #text(size: 13pt, weight: "bold", fill: charcoal)[#p2.headline]\
        #v(5pt)
        #text(size: 9pt, fill: coral)[#sym.circle.filled.small ]
        #text(size: 9pt, fill: soft-black.transparentize(15%))[*What we saw:* #p2.evidence]
      ]
    ]

    // Problem 3 — with numbered badge
    #place(left + top, dx: 16mm, dy: 167mm)[
      #place(dx: 2.5pt, dy: 2.5pt)[
        #box(width: 178mm, height: 100%, radius: 8pt, fill: mid-grey.transparentize(50%))
      ]
      #box(width: 178mm, inset: (left: 14pt, top: 10pt, bottom: 10pt, right: 10pt), radius: 8pt,
        fill: warm-white,
        stroke: (left: 3.5pt + coral, top: 0.5pt + mid-grey, right: 0.5pt + mid-grey, bottom: 0.5pt + mid-grey))[
        #grid(columns: (18pt, 1fr), column-gutter: 8pt, align: (center + horizon, left),
          box(width: 18pt, height: 18pt, radius: 9pt,
            fill: gradient.linear(coral, deep-coral, dir: ttb), stroke: none,
            align(center + horizon, text(size: 8pt, weight: "bold", fill: white)[3])
          ),
          text(size: 7pt, weight: "bold", fill: deep-coral, tracking: 0.5pt)[PROBLEM]
        )
        #v(4pt)
        #text(size: 13pt, weight: "bold", fill: charcoal)[#p3.headline]\
        #v(5pt)
        #text(size: 9pt, fill: coral)[#sym.circle.filled.small ]
        #text(size: 9pt, fill: soft-black.transparentize(15%))[*What we saw:* #p3.evidence]
      ]
    ]

    // ONE FIX frosted panel — gradient fill with stronger presence
    #place(left + top, dx: 16mm, dy: 204mm)[
      #place(dx: 2pt, dy: 2pt)[
        #box(width: 178mm, height: 100%, radius: 10pt, fill: mid-grey.transparentize(50%))
      ]
      #box(
        width: 178mm,
        fill: gradient.linear(coral.transparentize(86%), coral.transparentize(92%), dir: ttb),
        inset: (x: 14pt, y: 12pt),
        radius: 10pt,
        stroke: 0.8pt + coral.transparentize(40%),
      )[
        #box(fill: gradient.linear(coral, deep-coral, dir: ltr), inset: (x: 10pt, y: 5pt), radius: 5pt,
          text(size: 11pt, weight: "bold", tracking: 2pt, fill: white)[ONE FIX]
        )
        #v(8pt)
        #text(size: 12pt, weight: "bold", fill: charcoal)[A full AI-readiness audit so you know exactly where leads are leaking.]
        #v(8pt)
        #line(length: 100%, stroke: 0.4pt + coral.transparentize(50%))
        #v(6pt)
        #text(size: 7.5pt, weight: "bold", fill: coral, tracking: 1pt)[START WITH]
        #v(4pt)
        #text(size: 11pt, weight: "bold", fill: charcoal)[Audit]
        #h(4pt)
        #text(size: 10pt, fill: soft-black)[· \$1,000 per month]
        #v(5pt)
        #text(size: 9pt, fill: soft-black.transparentize(20%), style: "italic")[We map your intake, site, and ads — then hand you a prioritised fix list.]
        #v(6pt)
        #text(size: 11pt, fill: charcoal)[Reply: ]
        #box(
          fill: coral.transparentize(82%),
          inset: (x: 7pt, y: 4pt),
          radius: 5pt,
          stroke: 0.3pt + coral.transparentize(60%),
          text(size: 10pt, weight: "bold", fill: deep-coral)[priyanshu.sharma\@axiomintelligence.xyz]
        )
      ]
    ]

    // Footer divider line
    #place(center + bottom, dx: 0mm, dy: -16mm,
      line(length: 120mm, stroke: 0.4pt + gradient.linear(mid-grey.transparentize(80%), mid-grey, mid-grey.transparentize(80%), dir: ltr)))

    // Footer — city locations (matches right page)
    #place(center + bottom, dx: 0mm, dy: -10mm,
      text(size: 8.5pt, weight: "bold", fill: soft-black.transparentize(60%), tracking: 1pt)[Bhiwadi  #sym.dash.em  Los Angeles  #sym.dash.em  New York  #sym.dash.em  San Diego]
    )

    // Bottom warm gradient band
    #place(left + bottom, dx: 0mm, dy: 0mm,
      rect(width: 210mm, height: 8mm,
        fill: gradient.linear(white.transparentize(100%), coral.transparentize(75%), dir: ltr)))

    // Bottom-right decorative circles
    #place(right + bottom, dx: 20mm, dy: 20mm,
      circle(radius: 35mm, fill: coral.transparentize(95%)))
    #place(right + bottom, dx: 10mm, dy: 10mm,
      circle(radius: 20mm, fill: coral.transparentize(92%)))

    // Right-edge coral strip (visual fold connection)
    #place(right + top, dx: 0mm, dy: 0mm,
      rect(width: 1.2mm, height: 297mm,
        fill: gradient.linear(coral.transparentize(70%), coral.transparentize(40%), coral.transparentize(70%), dir: ttb)))
  ],

  // ========== RIGHT PAGE ==========
  box(width: 210mm, height: 297mm,
    fill: gradient.linear(
      rgb("#E8522B"), coral, warm-orange, rgb("#FFA05C"),
      angle: 140deg,
    ),
    clip: true,
  )[
    #set text(fill: white)

    // ---- Background texture — layered circles for depth ----
    #place(right + top, dx: 40mm, dy: -55mm,
      circle(radius: 95mm, stroke: 0.3pt + white.transparentize(93%), fill: none))
    #place(right + top, dx: 40mm, dy: -55mm,
      circle(radius: 65mm, fill: white.transparentize(96%)))
    #place(left + bottom, dx: -35mm, dy: 65mm,
      circle(radius: 70mm, stroke: 0.3pt + white.transparentize(93%), fill: none))
    #place(left + bottom, dx: -35mm, dy: 65mm,
      circle(radius: 50mm, fill: white.transparentize(96%)))
    // Mid-right accent circle
    #place(right + top, dx: -10mm, dy: 120mm,
      circle(radius: 45mm, fill: white.transparentize(97%)))
    #place(right + top, dx: -10mm, dy: 120mm,
      circle(radius: 45mm, stroke: 0.2pt + white.transparentize(94%), fill: none))

    // ---- Top accent bar ----
    #place(left + top, dx: 0mm, dy: 0mm,
      rect(width: 210mm, height: 2mm,
        fill: gradient.linear(white.transparentize(40%), white.transparentize(80%), dir: ltr)))

    // ---- Left edge stripe ----
    #place(left + top, dx: 0mm, dy: 0mm,
      rect(width: 2mm, height: 297mm,
        fill: gradient.linear(white.transparentize(40%), white.transparentize(88%), dir: ttb)))

    // ---- Bottom accent bar ----
    #place(left + bottom, dx: 0mm, dy: 0mm,
      rect(width: 210mm, height: 1.2mm,
        fill: gradient.linear(white.transparentize(85%), white.transparentize(50%), dir: ltr)))

    // ---- Header ----
    #place(left + top, dx: 18mm, dy: 10mm)[
      #text(size: 10pt, weight: "bold", fill: white, tracking: 2.5pt)[REVENUE GROWTH]
      #h(4pt)
      #box(width: 6mm, height: 0.8pt, fill: white.transparentize(30%), baseline: -2pt)
    ]
    #place(left + top, dx: 18mm, dy: 21mm,
      line(length: 28mm, stroke: 2pt + white.transparentize(30%)),
    )
    #place(left + top, dx: 18mm, dy: 27mm,
      text(size: 9pt, fill: white-soft, style: "italic")[Projected trajectory  |  2026 -- 2029],
    )

    // ---- Y-axis labels ----
    #place(left + top, dx: 10mm, dy: 35mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[\$120K])
    #place(left + top, dx: 10mm, dy: 59mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[\$100K])
    #place(left + top, dx: 10mm, dy: 83mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[\$80K])
    #place(left + top, dx: 10mm, dy: 107mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[\$60K])
    #place(left + top, dx: 10mm, dy: 131mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[\$40K])
    #place(left + top, dx: 10mm, dy: 155mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[\$20K])

    // Y-axis tick marks
    #place(dx: 20mm, dy: 38mm, line(length: 2mm, stroke: 0.4pt + white-soft))
    #place(dx: 20mm, dy: 62mm, line(length: 2mm, stroke: 0.4pt + white-soft))
    #place(dx: 20mm, dy: 86mm, line(length: 2mm, stroke: 0.4pt + white-soft))
    #place(dx: 20mm, dy: 110mm, line(length: 2mm, stroke: 0.4pt + white-soft))
    #place(dx: 20mm, dy: 134mm, line(length: 2mm, stroke: 0.4pt + white-soft))
    #place(dx: 20mm, dy: 158mm, line(length: 2mm, stroke: 0.4pt + white-soft))

    // ---- Grid — solid ----
    #place(dx: 22mm, dy: 38mm, line(length: 172mm, stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 22mm, dy: 62mm, line(length: 172mm, stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 22mm, dy: 86mm, line(length: 172mm, stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 22mm, dy: 110mm, line(length: 172mm, stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 22mm, dy: 134mm, line(length: 172mm, stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 22mm, dy: 158mm, line(length: 172mm, stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 52mm,  dy: 32mm, line(end: (0mm, 132mm), stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 94mm,  dy: 32mm, line(end: (0mm, 132mm), stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 136mm, dy: 32mm, line(end: (0mm, 132mm), stroke: 0.4pt + white.transparentize(50%)))
    #place(dx: 178mm, dy: 32mm, line(end: (0mm, 132mm), stroke: 0.4pt + white.transparentize(50%)))

    // ---- S-curve: wide glow ----
    #place(dx: 22mm, dy: 8mm, line(start: (5mm, 154mm), end: (12mm, 152mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (12mm, 152mm), end: (20mm, 148mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (20mm, 148mm), end: (28mm, 142mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (28mm, 142mm), end: (38mm, 132mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (38mm, 132mm), end: (48mm, 118mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (48mm, 118mm), end: (58mm, 102mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (58mm, 102mm), end: (68mm, 84mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (68mm, 84mm), end: (80mm, 68mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (80mm, 68mm), end: (92mm, 54mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (92mm, 54mm), end: (105mm, 43mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (105mm, 43mm), end: (118mm, 35mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (118mm, 35mm), end: (132mm, 30mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (132mm, 30mm), end: (148mm, 27mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (148mm, 27mm), end: (162mm, 25mm), stroke: 7pt + white.transparentize(82%)))
    #place(dx: 22mm, dy: 8mm, line(start: (162mm, 25mm), end: (172mm, 24mm), stroke: 7pt + white.transparentize(82%)))

    // ---- S-curve: mid glow ----
    #place(dx: 22mm, dy: 8mm, line(start: (5mm, 154mm), end: (12mm, 152mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (12mm, 152mm), end: (20mm, 148mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (20mm, 148mm), end: (28mm, 142mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (28mm, 142mm), end: (38mm, 132mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (38mm, 132mm), end: (48mm, 118mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (48mm, 118mm), end: (58mm, 102mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (58mm, 102mm), end: (68mm, 84mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (68mm, 84mm), end: (80mm, 68mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (80mm, 68mm), end: (92mm, 54mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (92mm, 54mm), end: (105mm, 43mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (105mm, 43mm), end: (118mm, 35mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (118mm, 35mm), end: (132mm, 30mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (132mm, 30mm), end: (148mm, 27mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (148mm, 27mm), end: (162mm, 25mm), stroke: 4pt + white.transparentize(70%)))
    #place(dx: 22mm, dy: 8mm, line(start: (162mm, 25mm), end: (172mm, 24mm), stroke: 4pt + white.transparentize(70%)))

    // ---- S-curve: crisp line ----
    #place(dx: 22mm, dy: 8mm, line(start: (5mm, 154mm), end: (12mm, 152mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (12mm, 152mm), end: (20mm, 148mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (20mm, 148mm), end: (28mm, 142mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (28mm, 142mm), end: (38mm, 132mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (38mm, 132mm), end: (48mm, 118mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (48mm, 118mm), end: (58mm, 102mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (58mm, 102mm), end: (68mm, 84mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (68mm, 84mm), end: (80mm, 68mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (80mm, 68mm), end: (92mm, 54mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (92mm, 54mm), end: (105mm, 43mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (105mm, 43mm), end: (118mm, 35mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (118mm, 35mm), end: (132mm, 30mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (132mm, 30mm), end: (148mm, 27mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (148mm, 27mm), end: (162mm, 25mm), stroke: 2.2pt + white))
    #place(dx: 22mm, dy: 8mm, line(start: (162mm, 25mm), end: (172mm, 24mm), stroke: 2.2pt + white))

    // Gradient fill under curve
    #place(dx: 27mm, dy: 8mm + 154mm,
      rect(width: 167mm, height: 10mm, fill: white.transparentize(88%)))
    #place(dx: 50mm, dy: 8mm + 142mm,
      rect(width: 144mm, height: 12mm, fill: white.transparentize(89%)))
    #place(dx: 70mm, dy: 8mm + 118mm,
      rect(width: 124mm, height: 24mm, fill: white.transparentize(91%)))
    #place(dx: 90mm, dy: 8mm + 84mm,
      rect(width: 104mm, height: 34mm, fill: white.transparentize(93%)))
    #place(dx: 110mm, dy: 8mm + 54mm,
      rect(width: 84mm, height: 30mm, fill: white.transparentize(95%)))


    // Data points — quad ring
    #place(dx: 22mm + 20mm - 10pt,  dy: 8mm + 148mm - 10pt, circle(radius: 11pt, fill: white.transparentize(88%)))
    #place(dx: 22mm + 20mm - 7pt,   dy: 8mm + 148mm - 7pt,  circle(radius: 8pt,  fill: white.transparentize(60%)))
    #place(dx: 22mm + 20mm - 4pt,   dy: 8mm + 148mm - 4pt,  circle(radius: 5pt,  fill: white.transparentize(25%)))
    #place(dx: 22mm + 20mm - 2.5pt, dy: 8mm + 148mm - 2.5pt, circle(radius: 3pt,  fill: white))

    #place(dx: 22mm + 68mm - 10pt,  dy: 8mm + 84mm - 10pt, circle(radius: 11pt, fill: white.transparentize(88%)))
    #place(dx: 22mm + 68mm - 7pt,   dy: 8mm + 84mm - 7pt,  circle(radius: 8pt,  fill: white.transparentize(60%)))
    #place(dx: 22mm + 68mm - 4pt,   dy: 8mm + 84mm - 4pt,  circle(radius: 5pt,  fill: white.transparentize(25%)))
    #place(dx: 22mm + 68mm - 2.5pt, dy: 8mm + 84mm - 2.5pt, circle(radius: 3pt,  fill: white))

    #place(dx: 22mm + 118mm - 10pt, dy: 8mm + 35mm - 10pt, circle(radius: 11pt, fill: white.transparentize(88%)))
    #place(dx: 22mm + 118mm - 7pt,  dy: 8mm + 35mm - 7pt,  circle(radius: 8pt,  fill: white.transparentize(60%)))
    #place(dx: 22mm + 118mm - 4pt,  dy: 8mm + 35mm - 4pt,  circle(radius: 5pt,  fill: white.transparentize(25%)))
    #place(dx: 22mm + 118mm - 2.5pt, dy: 8mm + 35mm - 2.5pt, circle(radius: 3pt, fill: white))

    #place(dx: 22mm + 172mm - 10pt, dy: 8mm + 24mm - 10pt, circle(radius: 11pt, fill: white.transparentize(88%)))
    #place(dx: 22mm + 172mm - 7pt,  dy: 8mm + 24mm - 7pt,  circle(radius: 8pt,  fill: white.transparentize(60%)))
    #place(dx: 22mm + 172mm - 4pt,  dy: 8mm + 24mm - 4pt,  circle(radius: 5pt,  fill: white.transparentize(25%)))
    #place(dx: 22mm + 172mm - 2.5pt, dy: 8mm + 24mm - 2.5pt, circle(radius: 3pt, fill: white))

    // Year labels with tick
    #place(dx: 38mm,  dy: 166mm, line(end: (0mm, 3mm), stroke: 0.5pt + white-soft))
    #place(dx: 84mm,  dy: 166mm, line(end: (0mm, 3mm), stroke: 0.5pt + white-soft))
    #place(dx: 130mm, dy: 166mm, line(end: (0mm, 3mm), stroke: 0.5pt + white-soft))
    #place(dx: 182mm, dy: 166mm, line(end: (0mm, 3mm), stroke: 0.5pt + white-soft))
    #place(dx: 35mm,  dy: 171mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[2026])
    #place(dx: 81mm,  dy: 171mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[2027])
    #place(dx: 127mm, dy: 171mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[2028])
    #place(dx: 179mm, dy: 171mm, text(size: 8.5pt, weight: "bold", fill: white-bright)[2029])

    // Revenue pills with connectors
    #place(dx: 22mm + 20mm, dy: 8mm + 148mm - 5mm,
      line(end: (4mm, -10mm), stroke: 0.5pt + white.transparentize(50%)))
    #place(dx: 22mm + 24mm, dy: 8mm + 148mm - 22mm)[
      #box(fill: dark-burnt, inset: (x: 5pt, y: 2.5pt), radius: 4pt,
        text(size: 6.5pt, weight: "bold", fill: white)[\$20K])
    ]
    #place(dx: 22mm + 68mm, dy: 8mm + 84mm - 5mm,
      line(end: (4mm, -10mm), stroke: 0.5pt + white.transparentize(50%)))
    #place(dx: 22mm + 72mm, dy: 8mm + 84mm - 22mm)[
      #box(fill: dark-burnt, inset: (x: 5pt, y: 2.5pt), radius: 4pt,
        text(size: 6.5pt, weight: "bold", fill: white)[\$55K])
    ]
    #place(dx: 22mm + 118mm, dy: 8mm + 35mm - 5mm,
      line(end: (4mm, -10mm), stroke: 0.5pt + white.transparentize(50%)))
    #place(dx: 22mm + 122mm, dy: 8mm + 35mm - 22mm)[
      #box(fill: dark-burnt, inset: (x: 5pt, y: 2.5pt), radius: 4pt,
        text(size: 6.5pt, weight: "bold", fill: white)[\$90K])
    ]

    // ---- Stat circles (infographic style) ----
    // Main circle — $120K
    #place(right + top, dx: -12mm, dy: 24mm)[
      #circle(radius: 30mm, fill: white.transparentize(82%))
      #place(center + horizon)[
        #align(center)[
          #text(size: 11pt, weight: "bold", fill: charcoal)[Agentic UGC\ Content / Ads]
        ]
      ]
    ]
    // Smaller circle — 46%
    #place(right + top, dx: -50mm, dy: 76mm)[
      #circle(radius: 34mm, fill: white.transparentize(78%))
      #place(center + horizon)[
        #align(center)[
          #text(size: 11pt, weight: "bold", fill: charcoal)[Agentic Workflow /\ Automation]
        ]
      ]
    ]

    // Third circle — 3.2X (left side)
    #place(left + top, dx: 28mm, dy: 78mm)[
      #circle(radius: 24mm, fill: white.transparentize(80%))
      #place(center + horizon)[
        #align(center)[
          #text(size: 10pt, weight: "bold", fill: charcoal)[Agentic GTM\ & SDR]
        ]
      ]
    ]
    // Fourth circle — 18+ (right side, below 3.2X)
    #place(right + top, dx: -110mm, dy: 125mm)[
      #circle(radius: 18mm, fill: white.transparentize(76%))
      #place(center + horizon)[
        #align(center)[
          #text(size: 10pt, weight: "bold", fill: charcoal)[Personalisation\ & Branding]
        ]
      ]
    ]

    // ---- Divider — gradient fade ----
    #place(left + top, dx: 8mm, dy: 177mm,
      line(length: 196mm, stroke: 1.5pt + gradient.linear(white.transparentize(50%), white, white.transparentize(50%), dir: ltr)))

    // ---- Primary callout — frosted container panel ----
    #place(left + top, dx: 8mm, dy: 180mm)[
      #box(
        width: 196mm,
        height: 102mm,
        fill: white.transparentize(88%),
        inset: (x: 14pt, y: 12pt),
        radius: 14pt,
        stroke: 0.3pt + white.transparentize(70%),
      )[
        #text(size: 48pt, weight: "bold", fill: charcoal)[\$100K]#text(size: 38pt, weight: "bold", fill: charcoal)[ -- ]#text(size: 48pt, weight: "bold", fill: charcoal)[120K]\
        #v(1pt)
        #box(fill: white.transparentize(75%), inset: (x: 10pt, y: 5pt), radius: 6pt,
          stroke: 0.3pt + white.transparentize(60%),
          text(size: 12pt, fill: charcoal)[Projected annual revenue increase (till 2029)]
        )
        // Metrics — 2x2 grid (uniform size)
        #v(2pt)
        #grid(
          columns: (59mm, 59mm),
          rows: (auto, auto),
          row-gutter: 5pt,
          column-gutter: 5pt,
          box(width: 59mm, fill: white.transparentize(80%), inset: (x: 8pt, y: 7pt), radius: 7pt,
            stroke: 0.3pt + white.transparentize(60%))[
            #text(size: 24pt, weight: "bold", fill: charcoal)[46]#text(size: 15pt, weight: "bold", fill: charcoal)[%]
            #h(3pt)
            #text(size: 9pt, fill: soft-black.transparentize(30%))[YoY revenue growth]
          ],
          box(width: 59mm, fill: white.transparentize(80%), inset: (x: 8pt, y: 7pt), radius: 7pt,
            stroke: 0.3pt + white.transparentize(60%))[
            #text(size: 24pt, weight: "bold", fill: charcoal)[3.2]#text(size: 15pt, weight: "bold", fill: charcoal)[X]
            #h(3pt)
            #text(size: 9pt, fill: soft-black.transparentize(30%))[Return on investment]
          ],
          box(width: 59mm, fill: white.transparentize(80%), inset: (x: 8pt, y: 7pt), radius: 7pt,
            stroke: 0.3pt + white.transparentize(60%))[
            #text(size: 24pt, weight: "bold", fill: charcoal)[94]#text(size: 15pt, weight: "bold", fill: charcoal)[%]
            #h(3pt)
            #text(size: 9pt, fill: soft-black.transparentize(30%))[Client retention rate]
          ],
          box(width: 59mm, fill: white.transparentize(80%), inset: (x: 8pt, y: 7pt), radius: 7pt,
            stroke: 0.3pt + white.transparentize(60%))[
            #text(size: 24pt, weight: "bold", fill: charcoal)[18]#text(size: 15pt, weight: "bold", fill: charcoal)[+]
            #h(3pt)
            #text(size: 9pt, fill: soft-black.transparentize(30%))[Enterprise clients served]
          ],
        )
      ]
    ]

    // ---- Footer — city locations ----
    #place(center + bottom, dx: 0mm, dy: -10mm,
      text(size: 8.5pt, weight: "bold", fill: white.transparentize(35%), tracking: 1pt)[Bhiwadi  #sym.dash.em  Los Angeles  #sym.dash.em  New York  #sym.dash.em  San Diego]
    )

    // ---- NEXT STEP + Attribution — full-width bottom row ----
    #place(left + bottom, dx: 13mm, dy: -18mm)[
      #grid(
        columns: (120mm, 60mm),
        column-gutter: 4mm,
        // NEXT STEP card
        box(
          width: 120mm,
          fill: white,
          inset: (x: 16pt, y: 14pt),
          radius: 8pt,
        )[
            #box(fill: coral, inset: (x: 10pt, y: 5pt), radius: 5pt,
              text(size: 11pt, weight: "bold", tracking: 2pt, fill: white)[NEXT STEP]
            )
            #v(10pt)
            #text(size: 12pt, weight: "bold", fill: charcoal)[20-minute walkthrough of these three issues.]\
            #v(6pt)
            #text(size: 11pt, fill: charcoal)[Reply: ]
            #box(
              fill: coral.transparentize(82%),
              inset: (x: 7pt, y: 4pt),
              radius: 5pt,
              stroke: 0.3pt + coral.transparentize(60%),
              text(size: 10pt, weight: "bold", fill: deep-coral)[priyanshu.sharma\@axiomintelligence.xyz]
            )
        ],
        // Attribution — white panel
        box(
          width: 60mm,
          fill: white,
          inset: (x: 10pt, y: 12pt),
          radius: 8pt,
        )[
          #align(center)[
            #image("../../src/website/media/mini_sun.png", width: 14mm)
            #v(4pt)
            #line(length: 30mm, stroke: 0.4pt + mid-grey)
            #v(4pt)
            #text(size: 9pt, fill: charcoal.transparentize(40%), tracking: 1.5pt)[PREPARED BY]\
            #v(3pt)
            #text(size: 16pt, weight: "bold", fill: charcoal)[Priyanshu Sharma]\
            #v(2pt)
            #text(size: 12pt, weight: "bold", fill: charcoal.transparentize(20%))[Founding Partner]\
            #v(2pt)
            #text(size: 11pt, weight: "bold", fill: charcoal.transparentize(20%))[Axiom Intelligence]\
            #v(2pt)
            #link("https://axiomintelligence.xyz/dfy/law")[
              #box(
                fill: coral.transparentize(85%),
                inset: (x: 5pt, y: 2pt),
                radius: 3pt,
                stroke: 0.3pt + coral.transparentize(60%),
                text(size: 9pt, weight: "bold", fill: deep-coral)[axiomintelligence.xyz/dfy/law]
              )
            ]
            #v(4pt)
            #line(length: 30mm, stroke: 0.3pt + mid-grey.transparentize(40%))
            #v(3pt)
            #text(size: 6pt, fill: charcoal.transparentize(60%))[Based on public web and\ Google Business Profile at the\ time of review. Not legal advice.\ Confidential to #data.firm_name.]
          ]
        ],
      )
    ]
  ],
)
