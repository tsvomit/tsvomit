# Serie "CAM 02": lote 1 (10 clips)

**Concepto:** un solo patio, una sola cámara, animales distintos y **una anomalía sutil por vídeo** que se descubre en la segunda vista. Eso empuja repeticiones y envíos por DM, que son las dos señales que reparten Reels.

## Reglas de producción

1. Genera primero el **PATIO BASE** en Flow y úsalo como imagen de referencia en los 10 prompts. Así todos los vídeos parecen la misma cámara.
2. Por cada clip: 4 imágenes en Flow → elige la de anatomía más limpia → 3 tomas en Kling 2.5 (5 s, modo estándar, cámara fija).
3. Si Kling no hace la anomalía, no pasa nada: pásame la toma y la creo en edición (cortes, congelados, duplicados). También sirve cualquier fallo natural que aparezca, porque el vídeo viral original funcionó por eso.
4. Sube los clips a la carpeta `clips/` de esta sesión y yo los monto con `edit_cctv.py`.
5. Etiqueta siempre como "contenido generado con IA" al publicar.

## Bloque de estilo (pégalo al final de cada prompt de imagen)

```
Style: low-quality night-vision CCTV security camera frame, infrared monochrome with a slight green tint, wide-angle lens with mild barrel distortion, camera mounted high on a house wall looking down at a suburban backyard, heavy sensor grain, video compression artifacts, blown-out IR glare on the nearest surfaces, white glowing reflective animal eyes, poor resolution, looks like real amateur home footage, not cinematic, no depth of field, no text, no watermark. Vertical 9:16.
```

## PATIO BASE (referencia para todos)

```
Empty suburban backyard at night seen from a high fixed security camera: round trampoline with a black safety net in the center, dark wooden fence at the back, a white plastic garden chair on the left, a coiled green garden hose on the lawn, a small metal shed in the top-right corner, a swing set at the far right edge, damp grass. No animals. [ESTILO]
```

## Prompt de Kling común (base)

```
Static locked-off security camera, no camera movement, no zoom. Natural realistic animal movement with real weight and physics, small irregular motions. Subtle infrared flicker and video noise. Realistic amateur CCTV footage.
```

**Negative prompt (siempre):** `camera shake, zoom, pan, cinematic lighting, color, cartoon, extra limbs, morphing, slow motion, text changes`

---

## Los 10 clips

### 1. Conejos, el 7.º conejo (conteo)
- **Flow:** `Exactly six rabbits of different sizes evenly spread on the trampoline, two mid-air, four crouched, all clearly countable, none overlapping. [ESTILO]`
- **Kling:** base + `The rabbits jump one after another in staggered rhythm. At about 3.5 seconds a seventh rabbit is suddenly sitting in the bottom-left corner of the trampoline, calm, looking at the camera, without having entered the frame.`
- **Texto:** `Cuenta los conejos`
- **Descripción:** `¿Cuántos conejos ves? 🐰 (IA)`

### 2. Conejos, salto sin aterrizaje (desaparición)
- **Flow:** `Five rabbits on the trampoline, one at the peak of a high jump, ears back, the others crouched, sharp eye glow. [ESTILO]`
- **Kling:** base + `The rabbits bounce in turn. At about 3 seconds the rabbit at the peak of the jump does not come down: it is simply gone before landing. Nothing else changes.`
- **Texto:** `Míralo otra vez`
- **Descripción:** `Cámara del patio, 3:17 AM (IA)`

### 3. Conejos, algo enorme (escala)
- **Flow:** `Six small rabbits jumping on the trampoline, and at the very bottom edge of the frame the tips of two very large rabbit ears just visible, out of focus. [ESTILO]`
- **Kling:** base + `The small rabbits keep bouncing. Slowly, one very large rabbit head rises into the bottom of the frame, ears first, and stays there, motionless.`
- **Texto:** `¿Qué es eso?`

### 4. Cabras, la que mira a cámara
- **Flow:** `Four goats jumping on the trampoline, one goat standing perfectly still in the center looking straight at the camera with glowing eyes. [ESTILO]`
- **Kling:** base + `Three goats bounce. The fourth goat stands still and slowly turns its head to look straight at the camera and stays like that.`
- **Texto:** `Mírala`

### 5. Mapaches, columpio vacío
- **Flow:** `Three raccoons sitting on the trampoline edge and a swing set in the background with one empty swing. [ESTILO]`
- **Kling:** base + `The raccoons wash their hands and bounce lightly. In the background the empty swing starts swinging by itself, steady, with nobody on it.`
- **Texto:** `¿Quién lo mueve?`

### 6. Patitos, el que sube
- **Flow:** `Eight ducklings on a small plastic kids' slide leaning on the fence, seven sliding down in a line, one at the top. [ESTILO]`
- **Kling:** base + `The ducklings slide down one after another. One duckling slides UP the slide, against gravity, calmly, and no one reacts.`
- **Texto:** `Cuenta los patitos`

### 7. Zorros, el que se pone de pie
- **Flow:** `Three foxes playing in a lawn sprinkler, water drops glowing in infrared, one fox standing upright on its hind legs. [ESTILO]`
- **Kling:** base + `Two foxes play and jump through the water. The third fox stays upright on two legs, arms at its sides, watching the others.`
- **Texto:** `¿Ese es un zorro?`

### 8. Conejos, loop de desaparición total
- **Flow:** `Eight rabbits jumping on the trampoline in a tight group. [ESTILO]`
- **Kling:** base + `The rabbits jump. In the last second all rabbits vanish at once and only the net keeps shaking on its own.`
- **Nota:** en edición el bucle vuelve al inicio, donde están todos otra vez, así que no se nota dónde termina.
- **Texto:** `¿Adónde se fueron?`

### 9. Conejitos bebé, el peluche
- **Flow:** `Twelve baby rabbits piled on the trampoline, bouncing like popcorn, one of them slightly bigger and stiffer than the rest, like a stuffed toy. [ESTILO]`
- **Kling:** base + `The baby rabbits bounce like popcorn. One bigger one bounces passively, stiff, only moved by the others, and never moves by itself.`
- **Texto:** `Encuentra el falso`

### 10. Ciervos, el que no salpica
- **Flow:** `Two deer standing in a kids' inflatable pool in the yard, one drinking, one looking at the camera. [ESTILO]`
- **Kling:** base + `The deer moves through the water and the water ripples around it. The second deer stands in the same water and causes no ripples at all.`
- **Texto:** `Mira el agua`

---

## Calendario del primer mes

| Semana | Publicar | Objetivo |
|---|---|---|
| 1 | Clips 2, 1, 4 | Ver qué anomalía engancha más |
| 2 | Clips 3, 8, 5 | Repetir el tipo que gane |
| 3 | Clips 9, 6, 7 + nuevos del tipo ganador | Duplicar lo que funcione |
| 4 | 4 a 5 variantes del mejor formato | Buscar los 5 de 100 K |

**Regla de decisión (a las 24 h):**
- Si un Reel tiene retención a 3 s inferior al 60 %, el gancho falla: cambia el primer fotograma.
- Si tiene retención buena y pocos envíos, la anomalía no se entiende: hazla más clara.
- Si supera los 20 K en 24 h, haz 3 variantes de ese formato en los 3 días siguientes.

**Sobre la meta:** 5 Reels de 100 K al mes es ambicioso para una cuenta nueva y nadie puede garantizarlo. Lo que sí controlas es el volumen (15 a 20 Reels al mes) y repetir lo que funcione. El vídeo viral original tuvo mucho de suerte y de ser el primero de su tipo.
