# Qasioun Restaurants — Website Hero Film
## Cinematic Concept & Production Storyboard

**Client:** Qasioun Restaurants, Irbid, Jordan
**Deliverable:** Premium website hero video, built entirely from existing vertical Instagram footage
**Date:** 13 September 2026
**Status:** Concept approved — ready for production

---

## 0. Source Audit

Everything in this document is anchored to four real files. No shot is invented.

| Ref | File | Duration | Format | Cuts | Avg shot |
|---|---|---|---|---|---|
| **A** | `qasioun_all_halls_overview.mp4` | 59.57 s | 720×1280 @ 30 fps | 19 | 2.8 s |
| **B** | `qasioun_countyard_fountain_event_halls_tour.mp4` | 12.88 s | 720×1280 @ 25 fps | 8 | 1.4 s |
| **C** | `qasioun_family_zoo_garden_experience.mp4` | 27.53 s | 720×1280 @ 30 fps | 17 | 1.5 s |
| **D** | `qasioun_food_and_dining_experience.mp4` | 42.30 s | 720×1280 @ 30 fps | 40 | 1.0 s |

**143 seconds of source. We need 24. The library is sufficient — selection, not shortage, is the challenge.**

### Verified take boundaries

Automated scene detection over-reports on handheld footage — it fires on camera movement as well as on cuts, and it misses soft transitions entirely. Every boundary below was confirmed by frame-accurate extraction at 0.4 s intervals, and **these are the numbers the edit is cut to.**

**Reel A** — note the white-flash transition at 2.3–2.6 s, which the detector missed completely:

| Take | Content | Used as |
|---|---|---|
| 0.00 – 2.25 | Facade at dusk | **Shot 1** |
| *2.3 – 2.6* | *White flash transition (in-camera)* | *Transition 1→2* |
| 2.70 – 4.15 | Al-Yasamin plaque | **Shot 2** |
| 4.30 – 7.00 | Al-Yasamin interior, wide | **Shot 6** |
| 7.10 – 9.05 | Table, medium | — |
| 9.10 – 12.90 | **Placemat with tagline** | **Shot 7** |

**Reel B** — the most efficient reel in the library; five of its eight takes are usable:

| Take | Content | Used as |
|---|---|---|
| 0.00 – 1.45 | **The fountain** | **Shot 3** |
| 1.50 – 2.90 | Interior hall | — |
| 2.95 – 4.45 | Window table, daylight | — |
| 4.50 – 5.95 | Evening hall, guests | — |
| 6.00 – 7.45 | Stone wall, florals | — |
| 7.50 – 8.95 | Bougainvillea arch | **Shot 4** |
| 9.00 – 10.40 | Blue-hour hall | — |
| 10.45 – 11.60 | Guest photographing | **Shot 9** |
| 11.65 – 12.88 | Mezze spread | — |

**Reel C** — the peacock runs 2.4 s, far longer than needed:

| Take | Content | Used as |
|---|---|---|
| 9.15 – 10.30 | Common pheasant | — |
| 10.35 – 12.75 | **Peacock** (best tail framing 11.4–12.6) | **Shot 5** |

**Reel D:**

| Take | Content | Used as |
|---|---|---|
| 4.05 – 5.50 | **The pour** | **Shot 8** |
| 33.80 – 35.70 | Hall + lilies, blue hour | **Shot 11** |
| 35.75 – 36.60 | Terrace, empty | — |
| 36.65 – 38.10 | **Performance troupe** | **Shot 10** |
| 39.20 – 40.45 | Performers, close | — |
| 40.50 – 42.30 | Existing logo end card | *reference only* |

> **On the existing end card:** their current outro (father lifting his son, arms raised, drummer beside him) is the most emotionally powerful image in all 143 seconds — but the logo begins fading over it at **40.55 s**, only 0.08 s after the cut. There is no clean frame. It cannot be used, and it is why Shot 11 draws on a different take. **Worth telling the owner: if a camera ever returns to Qasioun, that is the shot to get clean.**

### Four constraints that shaped every decision

**1. Resolution is the hard ceiling.** Every clip is 720×1280 at 1.6–2.1 Mbps. A 16:9 centre crop yields 720×405 — a 4.7× area upscale to reach 1080p. This is the single biggest technical risk, and Section 6 addresses it shot by shot.

**2. Instagram furniture is burned in.** Verified positions:

| Element | Reel | Y position (of 1280) | Present when |
|---|---|---|---|
| `@QASIOUNRESTAURANTS` + IG icon | A | ≈ 320 – 340 | **from ≈ 4.4 s onward** |
| White caption text | A | ≈ 915 – 955 | 0.0 – ≈ 6.5 s |
| Blue hall-name chips | A | ≈ 1075 – 1110 | from ≈ 2.8 s |
| Centred caption bar | B | ≈ 360 – 400 | throughout |
| *(none found)* | **C** | — | — |
| *(none found)* | **D** | — | — |

The handle's late arrival in reel A is what makes Shot 1 possible: before 4.4 s the frame is clear all the way to y ≈ 900, so the facade crop can sit high enough to keep the signage. **After 4.4 s the usable band narrows to y ≈ 360 – 900**, which is why Shots 6 and 7 crop lower than Shot 1.

Reel **D is completely clean** — which is fortunate, because it holds the food, the chefs and the finale. A 405-tall crop placed inside the safe band removes all burn-ins with no patching or inpainting. Crop values per shot are in Section 3, and **each must be positioned individually** — a single global centre crop decapitates the facade signage.

**3. The cutting rhythm is wrong for the genre.** Source averages 1.0–1.5 s per shot. Luxury hospitality needs 2.5–4 s holds. Only four takes in the entire library run past 3 s. The edit is therefore built from the longest available takes, with optical-flow retiming filling the rest — and the retime ratios in Section 3 are real, not aspirational.

**4. The "family zoo garden" is not a garden.** It is a covered night enclosure: wire mesh, sawdust, industrial fluorescents. Colour sampling confirms a magenta cast (#8475BF, #9D709C averages). It also contains identifiable children's faces. It appears in this film as exactly one abstract texture shot, and Section 6 explains why.

---

## 1. Creative Concept

### The idea is already theirs

At **A / 9.55 s**, on the navy placemat on every table, in gold Thuluth calligraphy:

> ### قاسيون دايماً يجمعنا
> *Qasioun always brings us together.*

We are not writing a concept. We are filming the sentence Qasioun already prints on its own tables. This matters commercially: nothing in the film can be accused of overclaiming, because the claim is the client's own, in the client's own handwriting, already in the guest's hands.

### The sentence is the structure

| Act | Arabic | Meaning | What it shows |
|---|---|---|---|
| **I** | **قاسيون** | *Qasioun* | Where it is — arrival, threshold, the grounds |
| **II** | **دايماً** | *always* | What happens here every day — the room, the table, the craft |
| **III** | **يجمعنا** | *brings us together* | Who it is for — the celebration, the gathering |

Three acts, derived rather than imposed. The film opens on a building and closes on people, and the turn between them is the placemat at 12.4 s, where the brand states its promise in gold.

### Emotional message

Not *"look at our food."*

> **"There is a place in this city that holds your family's occasions."**

The footage earns this. In 143 seconds it contains a Ramadan iftar service, a graduation table set for **CLASS OF 2026**, a conference hall, a wedding and engagement hall (صالة العروضات), a live traditional music troupe, and families eating together at blue hour. Qasioun is not a restaurant that also does events. It is where Irbid gathers, and the food is how it does that.

### What the visitor should feel in the first seconds

**Arrival somewhere lit and waiting for you.**

Not appetite — appetite comes at 14.6 s with the pour. The opening emotion is *recognition and welcome*: warm bulbs against a deep dusk sky, a name in light, a door that is open. The visual grammar is a threshold being crossed, and the viewer is the one crossing it.

---

## 2. Video Structure

| Property | Value |
|---|---|
| **Total duration** | **24.0 seconds** |
| **Shot count** | **11** |
| **Loop** | Seamless — 0.6 s cross-dissolve, logo as the hinge |
| **Frame rate** | 24 fps (film cadence; 25/30 fps sources conformed) |
| **Master resolution** | 2560×1440, delivered at 1920×1080 |
| **Audio** | None — hero autoplays muted. The cut must work silent. |

### Act map

| Act | Shots | Runtime | Share | Rhythm |
|---|---|---|---|---|
| **I — قاسيون** | 1–5 | 0.0–10.2 s | 42 % | Slow establish, then quicken |
| **II — دايماً** | 6–9 | 10.2–17.8 s | 32 % | Tightest cutting, most detail |
| **III — يجمعنا** | 10–11 | 17.8–24.0 s | 26 % | Opens out, long final hold |

Shot lengths compress through Act II and expand in Act III. The finale (4.2 s) is the longest hold after the opener (3.5 s) — energy crescendos at the celebration, then resolves into stillness.

### Scene order

```
I.  ARRIVAL      1  Facade at dusk ............ 3.5 s  ██████████
                 2  Al-Yasamin threshold ...... 1.6 s  ████
                 3  The fountain .............. 2.8 s  ████████   ◆ signature
                 4  Bougainvillea arch ........ 1.3 s  ███
                 5  Iridescence (peacock) ..... 1.0 s  ██

II. ALWAYS       6  Al-Yasamin dolly-in ....... 2.2 s  ██████
                 7  The placemat .............. 2.2 s  ██████     ◆ thesis
                 8  The pour .................. 1.6 s  ████
                 9  The guest's eye ........... 1.6 s  ████

III. TOGETHER   10  The celebration ........... 2.0 s  █████
                11  The gathering → logo ...... 4.2 s  ████████████  ◆ resolve
```

### Format rhythm

Eight shots are full-bleed 16:9. Three sit in a **1:1 window (1080×1080)** with blurred, colour-matched wings.

The windowed shots are the fountain, the placemat and the pour — the three most detail-critical images in the film. Windowing them means a **1.5× upscale instead of 4.7×**, so the shots that carry the most meaning are also the sharpest. The frame closing in for an intimate detail and opening out again reads as deliberate aperture breathing, not as a compromise. It occurs at two moments only (5.1 s, and across 12.4–16.2 s), so it is a rhythm, not a flicker.

---

## 3. Shot-by-Shot Breakdown

Crop syntax is ffmpeg: `crop=w:h:x:y` against the 720×1280 source. Retime values below 1.00× are slow-motion.

---

### Shot 1 — THE ARRIVAL
**0.0 → 3.5 s · 3.5 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **A** @ 0.10 – 2.20 s (2.10 s) — the complete facade take |
| **Retime** | Freeze frame @ 0.10 for output 0.00–0.95, then **0.82×** across 0.95–3.50 |
| **Crop** | `crop=720:405:0:120` — high placement |
| **Safe** | Caption at y≈915 excluded; **the handle does not appear until 4.4 s**, which is what makes this high crop possible. |

**Visually.** Dusk over Irbid. The Qasioun building rises across the frame: cream limestone cladding, a glazed upper storey, and the name in illuminated blue channel letters — **مطاعم قاسيون** above a smaller *Qasioun Restaurant*. A string of warm festoon bulbs runs the length of the parapet, and the gold word **رمضان** glows at frame left. The sky behind is deep, saturated blue-hour. Outdoor seating and greenery sit in soft foreground.

The high crop is essential — the default centre crop cuts the signage off entirely and leaves a busy retail frontage that reads as a mall food court.

**Camera.** Source is handheld with slow natural drift. Stabilise, then add a 1.00 → 1.05 push-in across the full 3.5 s. The move should be barely perceptible — a breath, not a zoom.

**On the freeze.** The facade take runs only 2.10 s, and stretching it across 3.5 s would mean a 0.60× retime — heavier than anything else in the film. Instead, the first 0.95 s (which is black fading up, while the logo draws on) holds a **still frame**, and live motion begins exactly as the image becomes visible. The retime drops to a comfortable 0.82×, and the design improves: the picture appears to *come alive* as it fades up. What looked like a shortage became the better idea.

**AI.** Topaz Proteus upscale 720×405 → 2560×1440. Stabilisation. Chronos retime to 0.82×. Highlight recovery on the bulbs so they bloom rather than clip. **No generative work** — this shot contains Arabic signage.

**Transition out.** **The source already contains the transition.** Reel A has a real in-camera white flash at 2.3–2.6 s, immediately after this take — the reason automated scene detection missed the cut. Use it: grade it warm and gold rather than blown white, and let the facade's festoon bulbs bloom up into it. It is free, it is real, and it is more convincing than any plug-in dissolve. 0.3 s.

---

### Shot 2 — THE THRESHOLD
**3.5 → 5.1 s · 1.6 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **A** @ 2.75 – 4.10 s (1.35 s) — take runs 2.70–4.15 |
| **Retime** | 0.84× |
| **Crop** | `crop=720:405:0:380` |
| **Safe** | Caption at y≈915 excluded; handle not yet present (arrives 4.4 s). |

**Visually.** A backlit plaque on a stone wall beside a staircase: **صالة الياسمين** in navy Arabic calligraphy over a cream and gold ground, *Al-Yasamin Lounge* beneath, framed by an Islamic geometric border. This is the film's first piece of real brand craft, and it does the job a title card would otherwise have to do — it tells the viewer the building has named rooms, which is the whole "destination, not restaurant" argument in one object.

**Camera.** Slight lateral drift in source. Add a gentle 1.00 → 1.03 push. Rack the vignette so the plaque's backlight is the brightest thing on screen.

**AI.** Upscale and stabilise only. **Generative work is forbidden here** — this frame is 60 % Arabic type, and video models destroy Arabic script.

**Transition out.** Match-cut on light: the plaque's warm backlight wipes to the fountain's gold inlay, which occupies the same screen position and colour. 0.25 s.

---

### Shot 3 — THE FOUNTAIN ◆
**5.1 → 7.9 s · 2.8 s · 1:1 window (1080×1080)**

| | |
|---|---|
| **Source** | **B** @ 0.10 – 1.40 s (1.30 s) |
| **Retime** | 0.46× — *or* generative orbit, see below |
| **Crop** | `crop=720:720:0:450` → 1080×1080 (1.5× upscale) |
| **Safe** | Below B's caption bar at y≈384. |

**Visually.** The single most brand-defining object in the entire library. An octagonal fountain, its broad basin inlaid with a radiating geometric star in ochre-gold, dusty mauve and cream, bordered in black; a tiered stone centre column topped with a glass finial; water sheeting over the tiers. It sits on a paved courtyard under a canopy, with outdoor seating beyond.

Nothing else in the footage carries Damascene heritage this literally. Hold it long, frame it square, and let it be the film's signature image.

**Camera.** Source is a 1.3 s handheld push. Two routes:

- **Conservative** — retime to 0.46× with Chronos optical flow, add a 1.00 → 1.06 push. Fully real. The 0.46× ratio is aggressive but the motion is simple lateral drift, which interpolates cleanly.
- **Recommended** — take one upscaled frame and generate a slow 12° orbit via Higgsfield or Runway image-to-video. **This is the best justified use of generative AI in the film**: a single object on a plain paved floor, no architecture to invent, no faces, no Arabic type, and it delivers a considered camera move the phone never captured. Composite the real water motion back over the generated plate if the model softens it.

**AI.** 1.5× upscale — the gentlest in the film, which is why this shot will be the sharpest thing on screen. Ambient wings per Section 5.

**Transition out.** The wings brighten and open outward; Shot 4's magenta floods in from frame edges. 0.35 s.

---

### Shot 4 — THE BOUGAINVILLEA
**7.9 → 9.2 s · 1.3 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **B** @ 7.60 – 8.90 s (1.30 s) |
| **Retime** | 1.00× — real time |
| **Crop** | `crop=720:405:0:437` |

**Visually.** A cascade of magenta bougainvillea spilling over a circular backlit mirror, with hanging beads and a white marble surround. This is a guest photo-op wall, and it should be read as exactly that — proof that people come here to take pictures of themselves. It also supplies the film's only jolt of saturated colour, which is why it sits at the end of Act I as a palate-cleanser before the interiors.

The magenta maps directly onto the brand's existing `--color-bougainvillea: #b83253`.

**Camera.** Source drift is sufficient. No added move — after three pushes in a row, one static shot resets the eye.

**AI.** Upscale, stabilise. No generative work.

**Transition out.** Straight cut on colour. Magenta → the peacock's iridescent teal is a complementary snap, and the hardest cut in the film. Intentional.

---

### Shot 5 — IRIDESCENCE
**9.2 → 10.2 s · 1.0 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **C** @ 11.70 – 12.70 s (1.00 s) |
| **Retime** | 1.00× |
| **Crop** | `crop=640:360:40:470` → 4× upscale |

**Visually.** Extreme tight framing on a peacock's tail — iridescent blue-green eye-feathers filling the frame. **No mesh, no wall, no sawdust, no faces, no floor.** Read as texture rather than as an animal in an enclosure. One second, then gone.

This is the entire zoo offering, compressed into a hint. The hero's job is to suggest *there is more here than dining*; the website section below the fold does the explaining, with context and captions the hero cannot carry.

**Camera.** Locked. The bird's own movement supplies the life.

**AI.** The heaviest lift in the film — 4× crop *and* 4× upscale. Two mandatory corrections: neutralise the magenta fluorescent cast (pull magenta from the whites, per the #9D709C source average), and add grain at double the film's base level to mask interpolation.

> **Honest note.** This is technically the weakest shot. If it does not survive grading, cut it. The film runs 23.0 s with Shot 4 extended to 2.3 s and loses nothing structurally. **Do not fight for this shot.**

**Transition out.** Fast dissolve through darkness into Act II. 0.4 s — the longest transition so far, marking the act break.

---

### Shot 6 — AL-YASAMIN
**10.2 → 12.4 s · 2.2 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **A** @ 4.60 – 6.40 s (1.80 s) — take runs 4.30–7.00 |
| **Retime** | 0.82× |
| **Crop** | `crop=720:405:0:470` |
| **Safe** | **Tightest band in the film** — below handle (y≈340), above caption (y≈915). Verify frame by frame. |

**Visually.** The strongest interior in the library. Fluted white columns recede down the hall. A warm cove-lit arched niche glows at the far end. Chairs alternate terracotta leather and quilted grey-cream — **and every chair back carries the circular Qasioun crest in gold.** White lilies stand on marble tables dressed with navy placemats. Greenery softens the foreground.

That crest, repeated down the length of the room, is the shot's argument: this place brands itself with care.

**Camera.** The source already dollies forward. Stabilise and extend it — the move should feel like walking in, not looking in.

**AI.** Upscale, stabilise, retime. **Critical grade note:** power-window the ceiling down 30 %. The gypsum ceiling with its visible downlights is the least premium element in frame, and darkening it is worth more than any other single adjustment.

**Transition out.** Continue the forward move straight into Shot 7 — the camera arrives at the table it has been walking toward. Cut on motion, 0 s. The dolly makes it invisible.

---

### Shot 7 — THE PROMISE ◆
**12.4 → 14.6 s · 2.2 s · 1:1 window (1080×1080)**

| | |
|---|---|
| **Source** | **A** @ 9.50 – 11.30 s (1.80 s) — take runs **9.10–12.90**, the longest in reel A |
| **Retime** | 0.82× |
| **Crop** | `crop=640:640:40:420` → 1080×1080 (1.69× upscale) |
| **Safe** | Clears the chip at y≈1075 and the handle at y≈340. Caption has ended by 6.5 s. |

**Visually.** The thesis shot. A navy placemat bearing **قاسيون دايماً يجمعنا** in gold Thuluth, framed by a fine white Islamic geometric border. A white plate at left, a knife and spoon at right, one with a gold-chased handle. Warm light falls across cream marble.

The brand states its own promise, in its own calligraphy, in gold, at the centre of a square frame. Everything before this shot is the building; everything after it is the people. **This is the hinge of the film.**

**Camera.** Slow lateral drift right, 1.00 → 1.04 push. The Arabic must settle and be readable for a clear beat — this is the one moment in 24 seconds where the viewer is asked to read.

**AI.** 1.69× upscale, the second gentlest in the film — deliberately, because this frame must hold up under attention. **Absolutely no generative work**: this is Arabic calligraphy, and generative models will turn it into nonsense glyphs. Sharpen the calligraphy edges manually if needed.

**Transition out.** The gold of the calligraphy blooms and carries into the gold of the pouring sauce. Both shots stay windowed, so the wings never open between them. 0.3 s.

---

### Shot 8 — THE POUR
**14.6 → 16.2 s · 1.6 s · 1:1 window (1080×1080)**

| | |
|---|---|
| **Source** | **D** @ 4.20 – 5.40 s (1.20 s) |
| **Retime** | 0.75× |
| **Crop** | `crop=720:720:0:400` → 1080×1080 (1.5× upscale) |
| **Safe** | **D carries no burn-ins.** |

**Visually.** A cream ceramic pitcher, held in a black-gloved hand, pours a thick pale tahini sauce in a slow unbroken ribbon. Below, a dish garnished with a carved carrot flower, mint, pomegranate seeds and a cherry tomato. The background falls away into blurred dark wood. Genuinely shallow depth of field — the softest, most filmic image in the library, and the only one with real bokeh.

This is the appetite beat, and the only one the film needs. Chefs at Qasioun wear black with gold Arabic embroidery and black gloves; the craft is already on screen.

**Camera.** Locked. The pour is the movement.

**AI.** Upscale, retime to 0.75×. **Never generate food.** AI food reads as fake within half a second — wrong viscosity, impossible reflections, melting garnish. This shot is real or it is nothing.

**Transition out.** The wings open outward as the sauce lands. 0.35 s, back to full-bleed for the rest of the film.

---

### Shot 9 — THE GUEST'S EYE
**16.2 → 17.8 s · 1.6 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **B** @ 10.50 – 11.60 s (1.10 s) |
| **Retime** | 0.69× |
| **Crop** | `crop=720:405:0:430` |
| **Safe** | Below B's caption bar (y≈384). |

**Visually.** A young woman photographs the table on her phone. Across the marble: grilled meats on charred foil, fattoush, stuffed vine leaves, wraps, salads — a full Levantine mezze spread. Her phone screen shows the shot she is taking. Her hair falls through the right of frame in soft focus.

This is the most honest shot in the film. It is not a model, not a food stylist — it is a guest doing what guests actually do at Qasioun, which is to photograph the table before touching it. The reason the client has 143 seconds of Instagram footage in the first place is visible inside the frame.

**Camera.** Handheld, stabilised but not smoothed to zero. A little residual motion keeps the documentary honesty.

**AI.** Upscale, stabilise, retime. No generative work — faces and food.

**Transition out.** Cut on the phone-screen flash into the celebration. 0.2 s.

---

### Shot 10 — THE CELEBRATION
**17.8 → 19.8 s · 2.0 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **D** @ 36.70 – 38.10 s (1.40 s) |
| **Retime** | 0.70× |
| **Crop** | `crop=720:405:0:437` |
| **Safe** | **D carries no burn-ins.** |

**Visually.** A traditional Levantine music troupe moves across polished marble — men in black sherwal trousers, embroidered waistcoats and tasselled sashes, one carrying a drum. Guests watch from tables at frame left. Blue Eid decorations hang from the ceiling. Movement, music, celebration.

Act III opens on energy. This is the visual proof of *يجمعنا* — Qasioun does not merely seat people, it stages their occasions.

**Camera.** Slow pan following the troupe. Stabilise lightly; keep the handheld energy, because this is the one shot that should feel alive rather than composed.

**AI.** Upscale, retime. **No generative work** — multiple faces in frame, and generative models will warp them.

**Transition out.** Cross-dissolve, 0.5 s. Energy settles into warmth; the longest dissolve in the film prepares the resolve.

---

### Shot 11 — THE GATHERING → LOGO ◆
**19.8 → 24.0 s · 4.2 s · full-bleed 16:9**

| | |
|---|---|
| **Source** | **D** @ 34.00 – 35.60 s (1.60 s) |
| **Retime** | 0.76× for 2.1 s, then freeze-frame hold 2.1 s |
| **Crop** | `crop=720:405:0:437` |
| **Safe** | **D carries no burn-ins.** |

**Visually.** The best-composed frame in the entire library, and the only one with three genuine planes of depth:

- **Foreground** — white lilies and a navy Qasioun placemat, thrown soft
- **Mid-ground** — families seated along tables, eating together, orange crested chairs
- **Background** — floor-to-ceiling glass, and beyond it Irbid at deep blue hour

Warm interior against cold blue city. Brand detail in front, real people in the middle, the town outside. This is *قاسيون دايماً يجمعنا* as a single photograph, and the film has been walking toward it since the facade.

**Camera.** Source drifts slowly right. Play at 0.76× through 21.9 s, then **freeze on the final frame** and hold for 2.1 s with a barely-there 1.00 → 1.02 push on the still. Motion resolving into stillness as the mark appears.

**Logo resolve, 21.9 → 24.0 s.**
The frozen frame darkens under a rising scrim. The square-Kufic mark draws on in a fine gold hairline (stroke-on, 0.8 s), fills to solid, and the bilingual wordmark fades beneath it. Final state: mark and wordmark centred over a dark, still, warm room.

**AI.** Upscale, retime. **No generative work** — faces and architecture. Push the background window blues toward the brand navy `#0b131a` in the grade so the glass reads as deep and rich rather than grey.

**Transition out — the loop.** Cross-dissolve back to Shot 1 over 0.6 s. Both frames are dark, both are centred on the logo in the same screen position, both are blue-dominant. **The logo is the hinge**: the mark on the frozen gathering becomes the mark over the facade at dusk, and the loop closes invisibly. A viewer who watches twice will not find the seam.

---

## 4. Hero Opening — The First Five Seconds

The first five seconds decide whether anyone stays. Frame-accurate:

| Time | Picture | Type & logo | Motion |
|---|---|---|---|
| **0.00 – 0.15** | Near-black. A trace of blue in the upper frame. | — | Still |
| **0.15 – 0.95** | Black holds over a **frozen frame** of A @ 0.10. | Kufic mark **draws on** in a 1 px gold hairline (`#c5a059`), centred, 320 px wide. Stroke-on, eased. | Still (held frame) |
| **0.95 – 2.20** | **Facade rises from black** — 15 % → 100 % opacity over 1.25 s. The frozen frame releases into live motion at 0.95 exactly, so the picture appears to come alive as it becomes visible. Festoon bulbs ignite first, then the blue channel letters, then the sky. | Mark holds as a hairline over the image. | Motion begins; push-in 1.00 → 1.02 |
| **2.20 – 3.10** | Facade at full exposure. Deep blue-hour sky, warm bulbs, stone. | **أهلاً بكم في قاسيون** fades up beneath the mark (Amiri, gold). Below it, smaller: *Qasioun Restaurants*, Cinzel, letterspaced, alabaster. | Push continues, 1.02 → 1.04 |
| **3.10 – 3.50** | Facade holds. | Full lockup settled. | Push to 1.05 |
| **3.50 – 5.10** | **The real in-camera white flash** (A @ 2.3–2.6, graded warm gold) → **Al-Yasamin plaque**. | Mark shrinks to the corner; headline holds. | Gentle 1.03 push |

### Why this order

**The mark before the building.** The viewer meets the brand as a drawn line before they meet the place. It is a promise of craft, made in 0.8 s, before a single photograph of the restaurant has to carry any weight.

**Light igniting, not a fade-in.** Bringing the bulbs up first, then the signage, then the sky, stages it as a building *switching on* for the evening — the literal visual of *we are open, and we were expecting you*. A flat opacity ramp would waste the shot.

**Deep blue behind warm gold.** The strongest colour contrast available anywhere in the library sits in the first frame the viewer sees.

**Five seconds buys two shots, not one.** By 5.1 s the viewer has seen the building *and* crossed its threshold. The journey has demonstrably started, which is what earns the next nineteen seconds.

> **Poster frame:** the graded still at **2.60 s** — full facade exposure, logo lockup settled, before the push has drifted. This is also the `prefers-reduced-motion` and `save-data` fallback, so it must stand alone as a photograph. It does.

---

## 5. Visual Style

### Colour grading

Measured averages across the source: **#A4845E, #917F55, #86643D, #9A897D**. The footage is natively warm amber-ochre-taupe, which sits naturally against the existing brand tokens in `index.html` — `--color-gold: #c5a059`, `--color-terracotta: #c4683c`, `--color-bg: #0b131a`.

| Element | Direction | Why |
|---|---|---|
| **Shadows** | Lift to **8–10 IRE**, tinted toward `#0b131a` navy | **Do not crush blacks.** At 1.6–2.1 Mbps, crushed shadows expose compression blocking. Lifted, navy-tinted shadows hide it *and* tie to the brand background. |
| **Midtones** | +8 warm toward amber/gold | Extends what the footage already does |
| **Highlights** | Protect and roll off; allow bulbs and gold trays to bloom | Clipped highlights read cheap |
| **Saturation** | Global −10 %, then gold/amber +15 %, bougainvillea magenta +10 %, **greens −20 %** | The plants read plastic at source saturation |
| **Print emulation** | Kodak 2383 film LUT at 40 % | Warmth and highlight rolloff without the full cinematic cliché |
| **Grain** | 35 mm, ~4 % | **Not optional.** Grain masks upscaling softness and compression mush. It is what makes 720p read as film rather than as low-res. |
| **Halation** | Subtle bloom on speculars | Festoon bulbs, gold trays, the backlit plaque |

**Avoid heavy orange-and-teal.** The footage is already warm; pushing it further cheapens it into a stock-video look. The cool note comes from the real blue-hour skies and window glass, not from graded shadows.

### Lighting

We cannot relight, but we can reshape — and two moves carry most of the value:

**1. Darken every ceiling by 30 %.** Power-window the top third of every interior. Bright gypsum ceilings with visible A/C ducts and downlights are the single least premium element in the entire library. Darkening them makes the rooms look twice as expensive, costs nothing, and risks nothing. **This is the highest-leverage adjustment in the whole grade.**

**2. Vignette downward.** Pull the eye to table height in every interior — where the crested chairs, lilies, marble and placemats are.

Secondary: warm the practical lights (cove strips, pendants, festoon bulbs) a further +200 K, and cool the window glass toward brand navy. Warm inside, cool outside — the visual language of shelter.

### Cinematic mood

> **Dusk, warmth, and welcome.** Unhurried. Confident. Never hungry-looking.

The register is a destination hotel film, not a restaurant advert. Two rules enforce it: **no shot shorter than 1.0 s**, and **no whip-pans or speed-ramps except the single resolve at 21.9 s.** The source is full of Instagram-style whips; every one of them is cut around.

### Typography

**Arabic primary, Latin secondary** — matching the real signage, which already sets **مطاعم قاسيون** large with *Qasioun Restaurant* small beneath.

| Role | Face | Treatment |
|---|---|---|
| **Arabic headline** | **Amiri** | 64 px desktop, gold `#c5a059`, generous line height |
| **Latin sub-line** | **Cinzel** | 18 px, letterspaced 0.18em, alabaster `#f8f6f0` |
| **Arabic body / CTA** | **IBM Plex Sans Arabic** | 16 px, 500 weight |

All four are already loaded in `index.html`.

**Placement.** Centred lockup. The Kufic mark is symmetrical, so centring is the only treatment that respects it — and centred type survives both the 16:9 and 9:16 crops without relayout.

**Safe zone.** All type must sit within the central **1080 px** of the 1920 canvas. This band is inside the 1:1 window, inside the mobile 9:16 crop, and clear of the ambient wings. Nothing outside it is guaranteed to be visible on every device.

**Scrim.** A bottom-up linear gradient, `#0b131a` at 0 % → 55 %, under all type at all times. Type legibility can never depend on what the footage happens to be doing.

**Live text, not burned in.** Headline and CTA live in the HTML, not in the video file. They stay selectable, translatable, accessible to screen readers, and legible if the video fails to load.

### Logo appearance

| Moment | Treatment |
|---|---|
| **0.15 – 0.95 s** | 1 px gold hairline, stroke-on, centred, 320 px |
| **0.95 – 3.50 s** | Holds as hairline over the facade |
| **3.50 s** | Shrinks to a corner watermark at 40 % opacity |
| **3.50 – 21.9 s** | **Absent.** The footage breathes. |
| **21.9 – 24.0 s** | Draws on gold, fills solid, wordmark fades beneath |

The mark is a **square-Kufic diamond**: interlocking navy maze linework, four gold trefoil petals at the cardinal points, a gold diamond at centre. Over footage it renders in solid gold `#c5a059` or alabaster — never in its navy-on-white form, which will not hold against moving image.

### Ambient wings — reference implementation

For the three windowed shots. **Tested on Shot 3 — this graph runs and outputs 1920×1080 as written:**

```bash
ffmpeg -i SOURCE.mp4 -filter_complex "
  [0:v]crop=720:720:0:450,scale=1080:1080:flags=lanczos[fg];
  [0:v]crop=720:720:0:450,scale=1920:1920:flags=lanczos,
       crop=1920:1080:0:420,gblur=sigma=60,
       eq=brightness=-0.28:saturation=0.55[bg];
  [bg][fg]overlay=(W-w)/2:0
" -c:v libx264 -crf 16 out.mp4
```

The wings are the *same frame*, blurred and darkened — **not AI-generated and not a solid colour**. Nothing is invented, the colour always matches because it is the same pixels, and the edges read as ambient spill.

**Two corrections from the render test:**

1. **`brightness=-0.28`, not `-0.18`.** At −0.18 the wings still carry enough detail to compete with the window for attention. −0.28 pushes them back to ambient glow, which is the job.
2. **The window edge is a hard vertical seam** at these settings. The 1 px gold hairline at 35 % opacity down each inner edge is therefore **not decorative — it is what resolves the seam into a deliberate frame.** Add it, plus a vignette across the whole canvas.

> **Production note from the same test:** the fountain sits on **wooden shims with a power cable visible at frame left**. It is invisible at Instagram scale and obvious at 1080×1080. Darken the lower quarter of the window in the grade, or raise the crop to `0:400` and accept a slightly tighter top. **Check this before the upscale, not after.**

Full-bleed shots, for comparison:

```bash
ffmpeg -i SOURCE.mp4 -vf "crop=720:405:0:120,scale=2560:1440:flags=lanczos" out.mp4
```

---

## 6. AI Generation Strategy

### The governing rule

> **AI may improve pixels that exist. AI may not invent pixels that mean something.**

Resolution, frame rate, stabilisation and noise are pixel quality. Architecture, faces, food and Arabic type are meaning. The first is safe; the second is where the client's brief said *do not invent* — and where the technology genuinely fails.

### Tier 1 — Enhancement only (all 11 shots)

Non-generative. Nothing is created; existing pixels are reconstructed.

| Task | Tool | Setting |
|---|---|---|
| **Upscale** | Topaz Video AI — **Proteus** | Interiors and detail; manual dehalo/deblock |
| **Upscale** | Topaz Video AI — **Iris** | Shots 9, 10, 11 (faces present) |
| **Retime** | Topaz **Chronos** / **Apollo** | Ratios per Section 3 |
| **Stabilise** | Resolve or Topaz | Preserve some handheld on Shots 9–10 |
| **Grain & halation** | Resolve / After Effects | Applied last, after upscale |

**Order matters:** deblock → upscale → retime → stabilise → grade → grain. Grain before upscale gets amplified into noise; grain last reads as film.

### Tier 2 — Generative, narrowly justified (1 shot)

**Shot 3, the fountain, is the only shot where generative video earns its place.** It passes all four tests: one object, plain paved ground, no faces, no Arabic type, no architecture. A generated slow orbit gives a considered camera move the phone never captured, and the worst failure case — slightly wrong water — is fixable by compositing the real water back over the plate.

| | |
|---|---|
| **Tool** | Higgsfield (best camera-move control) or Runway Gen-3 image-to-video |
| **Input** | One Topaz-upscaled frame from B @ 0.40 s |
| **Prompt direction** | Slow 12° orbit, locked height, no zoom, no people, no new objects |
| **Guard** | Composite real water motion back over the generated plate |
| **Fallback** | 0.46× Chronos retime of the real clip — ship this if the orbit shows any warping in the inlay geometry |

**Google Flow / Veo** is worth a parallel test on this same shot for its stronger physical coherence on water, but Higgsfield's camera-path control is the better fit for a specified orbit. Run both; pick by eye. Budget one shot's worth of iteration, not a pipeline.

### Tier 3 — Generative, forbidden

| Never generate | Why |
|---|---|
| **Arabic signage or calligraphy** | Models turn Arabic into nonsense glyphs. Shots 1, 2, 7 are 40–60 % Arabic type. **This alone disqualifies generative treatment on four of the best shots.** |
| **Faces** | Shots 9, 10, 11. Warping is instant and fatal to trust. |
| **Food** | Wrong viscosity, impossible reflections, melting garnish. Reads fake in under a second. |
| **Architecture** | The client's explicit constraint, and correctly so. The real building is modern, clean and photogenic; an invented one would be a lie the owner has to live next to. |
| **The logo** | Vector asset. Composite it; never let a model near it. |

### Preserving realism

Five rules that keep 720p source reading as premium rather than as upscaled phone video:

1. **Grain last, always.** The single most effective anti-AI-look measure available.
2. **Never sharpen past the source's real detail.** Over-sharpening produces the crunchy halo that reads "AI upscale" immediately. Where Topaz over-reaches, dial Proteus recovery back and let grain carry the texture.
3. **Keep residual handheld motion** on Shots 9 and 10. Perfectly smooth motion on documentary footage is the tell. Imperfection is evidence of a real camera.
4. **Grade for the compression.** Lifted navy shadows hide blocking; crushed blacks expose it. This is why the grade in Section 5 lifts rather than crushes.
5. **Cut before the eye can audit.** The two heaviest upscales — Shot 5 at 4× and Shot 3 at 0.46× retime — are 1.0 s and windowed respectively. Duration is a quality tool.

### Shot-by-shot verdict

| Shot | Upscale | Real / AI | Generative? |
|---|---|---|---|
| 1 Facade | 4.7× Proteus | **100 % real** | ✗ Arabic signage |
| 2 Threshold | 4.7× Proteus | **100 % real** | ✗ Arabic type |
| 3 Fountain | **1.5×** | Real, or AI orbit | **✓ recommended** |
| 4 Bougainvillea | 4.7× Proteus | **100 % real** | ✗ unnecessary |
| 5 Peacock | 4× Proteus | **100 % real** | ✗ (cut if it fails) |
| 6 Al-Yasamin | 4.7× Proteus | **100 % real** | ✗ architecture |
| 7 Placemat | **1.69×** | **100 % real** | ✗✗ calligraphy |
| 8 Pour | **1.5×** | **100 % real** | ✗✗ food |
| 9 Guest's eye | 4.7× Iris | **100 % real** | ✗✗ face + food |
| 10 Celebration | 4.7× Iris | **100 % real** | ✗✗ faces |
| 11 Gathering | 4.7× Iris | **100 % real** | ✗✗ faces |

**Ten of eleven shots are fully real.** One uses generative AI for a camera move on an inanimate object, with a real-footage fallback ready. That ratio is the point: the film's credibility is its largest asset, and it is worth more than any shot we could synthesise.

---

## 7. Website Hero Implementation

### Desktop

| Property | Specification |
|---|---|
| **Resolution** | 1920×1080 (master 2560×1440 for retina) |
| **Codecs** | AV1 → WebM/VP9 → H.264 MP4 (`<source>` fallback chain) |
| **Bitrate** | 4–6 Mbps VBR |
| **Target size** | **< 6 MB** |
| **Attributes** | `autoplay muted loop playsinline preload="none"` |
| **Poster** | Graded still at 2.60 s, WebP, < 120 KB |
| **Layout** | Full-bleed, `100vh` capped at `900px`, `object-fit: cover` |

`preload="none"` with a poster means the page paints instantly and the video streams in behind it. The hero must never be what blocks LCP.

```html
<section class="hero" dir="rtl">
  <video class="hero__video" autoplay muted loop playsinline
         preload="none" poster="/assets/hero-poster.webp"
         aria-hidden="true" tabindex="-1">
    <source src="/assets/hero-desktop.webm" type="video/webm">
    <source src="/assets/hero-desktop.mp4"  type="video/mp4">
  </video>
  <div class="hero__scrim"></div>
  <div class="hero__content">
    <img class="hero__mark" src="/assets/qasioun-mark.svg" alt="" width="96" height="96">
    <h1 class="hero__title">أهلاً بكم في قاسيون</h1>
    <p class="hero__sub">Qasioun Restaurants</p>
    <p class="hero__tagline">قاسيون دايماً يجمعنا</p>
    <div class="hero__actions">
      <a class="btn btn--gold" href="#reservations">احجز طاولتك</a>
      <a class="btn btn--ghost" href="#menu">تصفح القائمة</a>
    </div>
  </div>
</section>
```

`aria-hidden` and `tabindex="-1"` keep a decorative, silent, text-free video out of the accessibility tree, where it would only add noise.

### Mobile — the format advantage

**Mobile gets the better film.** Ship the **native 9:16 at full 720×1280, uncropped.**

This is not a compromise; it is the single largest quality win available. The footage was shot vertical. On phones there is no crop, no 4.7× upscale, no ambient wings, and no discarded frame area — every pixel is original. **The desktop cut is the compromised one.**

| Property | Specification |
|---|---|
| **Resolution** | 720×1280 native — **no upscale, no crop** |
| **Bitrate** | 2.5–3.5 Mbps |
| **Target size** | **< 3 MB** |
| **Height** | `100dvh` — `dvh`, not `vh`, or mobile browser chrome will crop the logo |
| **Type** | Headline 32 px, tagline 18 px; CTAs stack full-width |

Same edit, same 24 s, same shot order — a separate export, not a separate grade. The three windowed shots (3, 7, 8) simply revert to their full vertical frames on mobile, since there is no wide canvas to fill.

```html
<video autoplay muted loop playsinline preload="none" poster="...">
  <source src="/assets/hero-mobile.webm"  type="video/webm" media="(max-width: 767px)">
  <source src="/assets/hero-desktop.webm" type="video/webm">
  <source src="/assets/hero-mobile.mp4"   type="video/mp4"  media="(max-width: 767px)">
  <source src="/assets/hero-desktop.mp4"  type="video/mp4">
</video>
```

### Graceful degradation

```css
@media (prefers-reduced-motion: reduce) {
  .hero__video { display: none; }
  .hero { background: url('/assets/hero-poster.webp') center/cover; }
}
```

```js
// Honour data-saver: poster only.
const c = navigator.connection;
if (c?.saveData || /2g/.test(c?.effectiveType ?? '')) {
  document.querySelector('.hero__video')?.remove();
}
```

Also: **pause when off-screen.** An `IntersectionObserver` that pauses the hero once scrolled past saves battery and CPU for the rest of the page, and costs six lines.

### Delivery checklist

- [ ] Master 2560×1440, 24 fps, ProRes 422 HQ
- [ ] Desktop: WebM/VP9 + MP4/H.264, < 6 MB
- [ ] Mobile: 720×1280 native, WebM + MP4, < 3 MB
- [ ] Poster WebP < 120 KB (frame 2.60 s)
- [ ] Loop verified seamless across the 24 s → 0 s dissolve
- [ ] **Zero Instagram burn-ins** — frame-by-frame QC on every cut
- [ ] Legibility checked against the brightest frame, not the average
- [ ] Tested at 1280×720, 1920×1080, 2560×1440, 390×844
- [ ] LCP under 2.5 s with video streaming

---

## 8. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| **4.7× upscale on eight shots reads soft** | **High** | Grain, lifted shadows, short durations. The three detail-critical shots are windowed at 1.5×. **Accept that this film will look best at moderate viewing size** — it is a web hero, not a cinema trailer. |
| **0.46× retime on the fountain shows artefacts** | Medium | Generative orbit is the primary route; 0.46× Chronos is the fallback. Test both before committing. |
| **Shot 5 (peacock) never reaches the bar** | Low | Cut it. 23 s film, no structural loss. Planned for. |
| **Burn-in missed on a frame** | **High** | Crop values are verified but **must be re-checked per frame** — captions animate in and out. Full-frame QC pass, not spot checks. |
| **Blue-hour continuity** | Low | Shots 1, 10, 11 are dusk; 3, 4, 9 are daylight or covered. Grade the daylight shots cooler and darker so the film reads as one continuous evening. |
| **Children's faces in Shot 10** | Medium | Guests are mid-ground and small. If the client wants certainty, use D @ 36.70 framed on the troupe with guests soft — or secure releases. **Raise this with the owner before launch.** |

### Recommended next step

**Produce Shot 3 (the fountain) and Shot 11 (the gathering) first, as a 7-second test.** They are the signature image and the resolve, they exercise both the 1.5× windowed path and the 4.7× full-bleed path, and they settle the generative-orbit question. If those two hold up, the remaining nine are routine. If they do not, we learn it in a day rather than a fortnight.

---

## Appendix — Timeline Reference

| # | Shot | Out | Dur | Src | Source TC | Retime | Crop | Format |
|---|---|---|---|---|---|---|---|---|
| 1 | The Arrival | 0.0 | 3.5 | A | 0.10–2.20 | freeze + 0.82× | `720:405:0:120` | Full-bleed |
| 2 | The Threshold | 3.5 | 1.6 | A | 2.75–4.10 | 0.84× | `720:405:0:380` | Full-bleed |
| 3 | **The Fountain** | 5.1 | 2.8 | B | 0.10–1.40 | 0.46× | `720:720:0:450` | **1:1 window** |
| 4 | The Bougainvillea | 7.9 | 1.3 | B | 7.60–8.90 | 1.00× | `720:405:0:437` | Full-bleed |
| 5 | Iridescence | 9.2 | 1.0 | C | 11.70–12.70 | 1.00× | `640:360:40:470` | Full-bleed |
| 6 | Al-Yasamin | 10.2 | 2.2 | A | 4.60–6.40 | 0.82× | `720:405:0:470` | Full-bleed |
| 7 | **The Promise** | 12.4 | 2.2 | A | 9.50–11.30 | 0.82× | `640:640:40:420` | **1:1 window** |
| 8 | The Pour | 14.6 | 1.6 | D | 4.20–5.40 | 0.75× | `720:720:0:400` | **1:1 window** |
| 9 | The Guest's Eye | 16.2 | 1.6 | B | 10.50–11.60 | 0.69× | `720:405:0:430` | Full-bleed |
| 10 | The Celebration | 17.8 | 2.0 | D | 36.70–38.10 | 0.70× | `720:405:0:437` | Full-bleed |
| 11 | **The Gathering** | 19.8 | 4.2 | D | 34.00–35.60 | 0.76× + freeze | `720:405:0:437` | Full-bleed |

**Total: 24.0 s · 11 shots · seamless loop**

---

*قاسيون دايماً يجمعنا*
