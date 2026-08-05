# Welding

## Norm

The norm for welding and allied processes 'EN ISO 2553' has been renewed since 2013, with a small update in 2019.

It's basically a compromise between European and American norms, with some slight differences: European → System A, American → System B.

![European System A vs American System B](../assets/design-playbook/welding/image091.png)

!!! tip "Rule"
    Always use the welding symbols according to SYSTEM A.

In the title block on our drawings, it is mentioned that we use the European viewset / standard and 'ISO 13920-AE' for general tolerances for welded structures and the geometrical tolerances.

![Title block referencing the European viewset and ISO 13920-AE](../assets/design-playbook/welding/image092.png)

In case higher tolerances than according to ISO 13920-AE are required, mainly about deformation due to welding, add a special remark in the tail of the welding symbol.

It is also possible to refer to a WPS (Welding Procedure Specification) if known.

A welding symbol is always composed of:

1. Arrow line
2. Reference line
3. Tail

![The three parts of a welding symbol: arrow line, reference line, tail](../assets/design-playbook/welding/image093.png){ width="300" }

## Elementary welding symbols and how to use them

The elementary symbols are defined by norm ISO 2553 and can't be adapted or modified. In case any clarification has to be made, use supplementary symbols and the tail.

**Butt weld** — welding bead < 45°

![Butt weld symbol](../assets/design-playbook/welding/image094.png){ width="280" }
![Butt weld symbol, alternate](../assets/design-playbook/welding/image095.png){ width="200" }

A certain depth is burnt into the connected parts.

There are a lot of different butt weld symbols that refer to different joint preparations, but it's appropriate to not designate the welding preparation and use the symbol that doesn't define the joint preparation, leaving it up to the production:

![Generic butt weld symbol without joint preparation](../assets/design-playbook/welding/image096.png){ width="180" }

**Fillet weld** — welding bead from 45° to 90°

![Fillet weld symbol](../assets/design-playbook/welding/image097.png){ width="200" }
![Fillet weld symbol, applied example](../assets/design-playbook/welding/image098.png){ width="320" }

Adding of a certain amount of material on the connected parts — commonly known as corner welds.

![Fillet weld example 1](../assets/design-playbook/welding/image099.png){ width="220" }
![Fillet weld example 2](../assets/design-playbook/welding/image100.png){ width="220" }

**Combination of Butt and Fillet**

Where you burn into the connected parts and add a second layer of material on top of it — for this kind of more advanced weld, ask a manager.

![Combined butt and fillet weld symbol](../assets/design-playbook/welding/image101.png){ width="220" }

**Edge weld** — welding bead > 90°

![Edge weld symbol](../assets/design-playbook/welding/image102.png){ width="220" }

Adding of a certain amount of material on the connected parts.

![Edge weld applied example](../assets/design-playbook/welding/image103.png){ width="180" }

**Flare V weld** — to connect 2 round surfaces

![Flare V weld symbol](../assets/design-playbook/welding/image104.png){ width="200" }

**Flare bevel** — to connect 1 round surface on a flat one

![Flare bevel weld symbol](../assets/design-playbook/welding/image105.png){ width="180" }
![Flare bevel weld applied example](../assets/design-playbook/welding/image106.png){ width="200" }

To be used to weld a net onto a frame; dimensions of the net have to be clearly identified:

![Net welded onto a frame with dimensions specified](../assets/design-playbook/welding/image107.png)

**Plug weld** — to fill holes and connect groove / tongue connections

![Plug weld symbol](../assets/design-playbook/welding/image108.png){ width="200" }

**Resistance Spot Weld or Projection Weld** — to be used for welding nuts

![Resistance spot / projection weld symbol](../assets/design-playbook/welding/image109.png){ width="250" }

**Stud weld** — for stud bolts

![Stud weld symbol](../assets/design-playbook/welding/image110.png){ width="300" }

## Supplementary welding symbols and how to use them

These symbols are used to add info on how to perform the weld, but not on the operations to perform afterwards (those are specified in text on the tail of the symbol).

**Field weld** — the weld is done on site, during mounting. This can be very useful to avoid misalignment of flanges, for example.

![Field weld symbol](../assets/design-playbook/welding/image111.png){ width="220" }

**Flush** — to specify that the weld has to be flush-finished

![Flush weld symbol](../assets/design-playbook/welding/image112.png){ width="260" }

**Convex**

![Convex weld symbol](../assets/design-playbook/welding/image113.png){ width="260" }

**Concave**

![Concave weld symbol](../assets/design-playbook/welding/image114.png){ width="260" }

**Weld all-round symbol** — to indicate with a single symbol that the part needs to be welded all the way around, in case the weld type and dimension of the weld remain the same.

![Weld all-round symbol example 1](../assets/design-playbook/welding/image115.png){ width="220" }
![Weld all-round symbol example 2](../assets/design-playbook/welding/image116.png){ width="190" }
![Weld all-round symbol example 3](../assets/design-playbook/welding/image117.png){ width="140" }

!!! tip "Rule"
    This symbol is also used for circular welding to insist on the fact that the weld has to be continuous and the start & stop points are the same.

![Weld all-round symbol used for circular welding](../assets/design-playbook/welding/image118.png){ width="220" }

**Weld between 2 points** — to indicate a continuous weld along several edges, in all directions, having the exact same characteristics from start to end points.

![Weld between two points example 1](../assets/design-playbook/welding/image119.png){ width="280" }
![Weld between two points example 2](../assets/design-playbook/welding/image120.png){ width="230" }

!!! note
    The arrow can be drawn with ALT + 26.

**Chain intermittent welds**

![Chain intermittent weld example](../assets/design-playbook/welding/image121.png)

!!! tip "Rules"
    - The number of welds has to be specified only if relevant.
    - The lengths of weld and of space don't have to be exact to the mm, but rounded.

**Staggered intermittent weld** — less deformation of thin plates

![Staggered intermittent weld example](../assets/design-playbook/welding/image122.png)

!!! tip "Rules"
    - The number of welds has to be specified only if relevant.
    - The lengths of weld and of space don't have to be exact to the mm, but rounded.

## Arrow placement and information

European standards use the following rules:

- According to SYSTEM A, the dashed line is always underneath the reference line.
- The arrow always points to a visible line (never to a hidden line).
- The location of the weld (in red) is defined by the position of the arrow and the position of the welding symbol regarding the dashed line:

![Fig.1](../assets/design-playbook/welding/image123.png){ width="200" }
![Fig.2](../assets/design-playbook/welding/image124.png){ width="220" }
![Fig.3](../assets/design-playbook/welding/image125.png){ width="200" }

- One side is welded: the side of the arrow. The symbol is placed on top. (Fig.1)
- One side is welded: the opposite side of the arrow. The symbol is placed at the bottom. (Fig.2)
- Both sides have the same weld: the dashed line is removed. (Fig.3)
- Both sides have different welds: the dashed line is kept. (Fig.4)

![Fig.4 - dashed line kept for different welds on both sides](../assets/design-playbook/welding/image126.png){ width="260" }

- When it's not important to specify which part needs to be prepared, or when no preparation is needed, multiple (broken) lines can be used to indicate identical welds.

![Multiple broken lines indicating identical welds](../assets/design-playbook/welding/image127.png){ width="200" }

- When it's important to specify which part needs to be prepared, use a broken arrow.

![Broken arrow specifying which part needs preparation](../assets/design-playbook/welding/image128.png){ width="180" }

## Additional information on welding symbols

Additional information and special remarks about the weld can be added to the symbol in the tail.

!!! tip "Rule"
    The tail has to be **open** for additional information and **closed** for a reference to any document (such as a WPS).

![Open vs closed tail on a welding symbol](../assets/design-playbook/welding/image129.png)

Common remarks are:

- Watertight
- Leave flow holes free
- Leave free near mounting holes
- Smooth finish (polish)
- Flat grind finish
- Prepare for watertight sealing
- ...

Combinations of these remarks are also possible.

![Combined remarks example 1](../assets/design-playbook/welding/image130.png){ width="280" }
![Combined remarks example 2](../assets/design-playbook/welding/image131.png){ width="280" }
![Combined remarks example 3](../assets/design-playbook/welding/image132.png){ width="280" }

Crucial welds should be named and refer to the 'WPS' (Welding Procedure Specification) — has to be discussed with a manager.

![Weld referencing a WPS document](../assets/design-playbook/welding/image133.png){ width="220" }

## Weld size indication

Defining the size of the weld should be calculated by a welding engineer, but for simple applications you can use the following thumb rules.

**Fillet weld**

Following the European standard, the size of the corner weld must be indicated by `a`.

![Fillet weld size indicated by 'a'](../assets/design-playbook/welding/image134.png){ width="180" }

American standards use `z`.

![American fillet weld size indicated by 'z'](../assets/design-playbook/welding/image135.png){ width="260" }

`a` is calculated as follows:

- Double sided weld: a ≥ 0.6 x t
- Single sided weld: a ≥ 0.8 x t

Where `t` is the thickness of the thinnest plate.

!!! warning "Important"
    Always check that there is enough space to weld. If `a3` is specified, 3 x 1.4 = 4.2 mm minimum of available surface is required.

**Butt weld**

If there is no weld size mentioned → full weld-through.

![Butt weld with no size mentioned - full weld-through](../assets/design-playbook/welding/image136.png){ width="200" }

If there is a weld size mentioned → depth of penetration.

![Butt weld with size mentioned - depth of penetration](../assets/design-playbook/welding/image137.png){ width="200" }

If the application isn't that simple anymore, it's better to calculate or discuss with a manager or a welding engineer. To calculate you can use the following tools:

- Fillet weld calculation static load: <https://werktuigbouw.nl/sub22.htm>
- Butt weld calculation dynamic load: <https://werktuigbouw.nl/sub22.htm>
- `R:\Nota's Ontwerp en Technische Catalogi\00_Technisch Praktisch-Theorie\Lassen-toelaatbare belasting WL.pdf`
