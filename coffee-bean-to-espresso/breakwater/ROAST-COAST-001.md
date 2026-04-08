# Roast Dossier — “Thermal Transformation & State Change”

*A reference document on the coffee roasting process: the equipment that delivers heat, the thermodynamic envelope of the roast, the chemistry that restructures the bean, the physical changes that follow, and the aromatic compounds that emerge.*

**Dossier ID:** ROAST-COAST-001  
**Version:** 0.3.1 (second Architect review integrated — predictive scaffolds added)  
**Date:** 2026-04-08  
**Parent:** Coffee / Espresso Essay (CL-2026-010)  
**Predecessor dossier:** BEANS-COAST-001 v0.3.2  
**Tier:** T1b (Metrological — where measurement method affects reported values, the method is treated as part of the parameter definition)  
**Stance:** Guardian (curation); two rounds of Architect review integrated through v0.3.1  
**Curated from:** TC-ROAST-001 v1.1 raw returns (GPT × 5, Kimi × 5, Perplexity × 1 equipment) plus Claude curation work

**How to read the status markers:**

Each fact or measurement in this dossier carries a status marker:

- `FROZEN` — verified across multiple independent sources, stable, safe to cite.
- `PROVISIONAL` — supported by evidence but based on fewer sources or awaiting independent confirmation.
- `OPEN` — unresolved question; needs further investigation.
- `QUARANTINED` — the original source could not be independently verified; excluded from the main tables until checked.

-----

## Introduction — How to Read This Dossier

A green coffee bean is a seed that has never been heated. The moment it enters a roaster, it begins an irreversible state transformation: a hydrated biological solid, under controlled time–temperature input, is converted into a porous, degassing, thermochemically altered matrix. Nothing about this transformation is reversible. Nothing about it is casual. And nearly every claim one could make about roasted coffee depends on one question: *how far has the transformation been taken?* This dossier describes that transformation from the moment the bean enters the roaster to the moment it leaves the cooling tray.

**Why do some roasted beans look dry and matte while others look glossy and oily?** A question familiar to any coffee buyer provides a better entry point into this dossier than any definition. Stand in front of a shelf of whole-bean coffee and you will see both kinds, often side by side. The common-sense explanation — that oily beans contain more oil — is wrong. Arabica green beans contain roughly 13–17% lipids by mass (see BEANS-COAST-001 §5.1), and that bulk lipid fraction is largely conserved through roasting. Caffeine is heat-stable at roasting temperatures, and so are the triglycerides that make up most of coffee’s lipid content. A dry-looking light roast and an oily-looking dark roast typically contain *the same amount of lipid*. The difference is not compositional. It is structural.

What changes during roasting is where the lipids are *located*. In a green bean, the lipids are confined inside cellular structures — oleosomes and cell walls — and the surface is dry. As the roast progresses, three things happen in parallel: the bean expands (volume up 50–100%), its internal porosity increases (from ~20–30% to ~60% in dark roasts), and its cellular matrix weakens as hemicelluloses degrade and cell walls fracture. At light and medium roast levels, the matrix remains mostly intact and the lipids stay confined. Somewhere around or past second crack — as pyrolysis deepens, fracture networks become continuous, and the structural matrix partially collapses — the confinement breaks down. The lipids, now in a lower-viscosity state from elevated temperature and under pressure from internal gas evolution, begin to migrate outward along the fracture network to the bean surface. A glossy dark roast is not an oil-rich bean; it is a structurally over-developed bean whose confinement has failed.

This phenomenon runs through the dossier because it cannot be explained from any single section alone. It requires §1 (the heat transfer that drove the transformation), §2 (the time–temperature trajectory that determined how long the bean spent in the high-mobility regime), §3 (the chemistry of lipid stability and cell-wall degradation), §4 (the porosity and fracture data that describe the structural evolution), and §5 (the volatile loss that accompanies surface oil exposure). A reader who understands why dark roasts look oily has already absorbed the dossier’s central organisational principle: roasting is a state transformation, not a chemical substitution, and its observable outcomes are projections of a complex internal state onto surface features. The anti-claim “oily beans contain more oil” is registered as RAC-11 in §6.

**What does “medium roast” actually mean?** A second question, more technical but equally central, sharpens the same point. Medium roast is not a point and it is not even a tightly constrained state. It is an *approximate region* in a high-dimensional space whose coordinates include colour, weight loss, temperature trajectory, compound concentrations, internal thermal gradients, and volatile profile. Any one of these coordinates gives a partial description. Several of them together — for instance Agtron Gourmet ≈ 55, weight loss ≈ 14–16%, drop temperature ≈ 210–220 °C on a properly placed bean probe, chlorogenic acid loss ≈ 50–60%, and remaining sucrose ≈ zero — narrow the region, but they do not uniquely identify a state.

**This is important: the same surface anchors can hide different underlying states.** Two roasts reaching Agtron 55 via different time–temperature trajectories (slower Maillard phase with shorter development vs faster Maillard with longer development) can end up with the same colour reading but measurably different CGA loss profiles, different internal thermal gradients, different volatile distributions, and different cup outcomes. Roasting is a trajectory through a high-dimensional state space, and different trajectories can terminate in the same neighbourhood without being chemically identical. This phenomenon — state degeneracy at common surface endpoints — is one of the reasons equipment-to-cup and profile-to-cup claims are so hard to close experimentally. It is also the formal version of the dry-vs-oily observation above: two beans with the same Agtron reading can have very different surface oil states if they took different routes there.

What the anchors achieve is not state equivalence but *operational usability*: they define a region narrow enough that two roasters can meaningfully communicate about what they are trying to produce, while acknowledging that within the region there is genuine variation. This dossier consistently pairs descriptive roast terms with at least one operational anchor, and flags any source that does not. The reader should treat “medium roast” as shorthand for “this approximate region of the roast state space,” not as a physical constant.

The document covers five topics, each dealing with a different aspect of the transformation:

- **§1 Equipment & Mechanical Configuration** — the roaster types, scales, heat transfer modes, and instrumentation that deliver energy to the bean.
- **§2 Thermodynamic Envelope** — the time–temperature trajectory of a roast, including reference points, rate of rise, phase ratios, and the endothermic-to-exothermic transition.
- **§3 Roast Chemistry** — the Maillard and Strecker reactions, caramelisation, pyrolysis, and the degradation pathways of chlorogenic acids, trigonelline, caffeine, sucrose, lipids, and amino acids.
- **§4 Physical Changes & Measurable Endpoints** — weight loss, volume increase, density, colour measurement, moisture, porosity, and CO₂ retention.
- **§5 Aromatic Outcomes** — the ~800–1,000 volatile compounds that emerge, the small subset (~30) that carry most of the perceived aroma, and the precursor-to-volatile mapping that remains partially open.

Each topic section follows the same structure: (a) declared parameters with status markers, (b) a validity contract explaining when those numbers can and cannot be trusted, (c) open disputes, and (d) notes on how this information connects to later stages (brewing, drinking). This is the same architecture used by the predecessor Beans dossier (BEANS-COAST-001 v0.3.2), and readers who already know that dossier will navigate this one without re-orienting.

Two cautions for the reader. First, the ranges in this dossier span many roaster types, profiles, and bean origins. Any single real-world roast will fall within a narrower window determined by the equipment, the profile chosen, and the green coffee used. Second, this dossier describes what happens *during* roasting, not what the resulting coffee tastes like. Sensory evaluation — cupping scores, flavour wheels, descriptor language — belongs to the forthcoming Drink dossier. Where this dossier touches sensory territory, it does so only for claims that have been tied to experimentally measured compound concentrations under controlled conditions.

**[Synthesis statement, not observation:]** A single finding runs through the entire dossier: roast-degree dependence is not a qualifier but a constitutive variable. Almost every parameter in this document is a function of roast degree, and attempts to cite roast chemistry without specifying the endpoint are systematically misleading. The §3.8 discipline in TC-ROAST-001 was written to guard against this failure mode, and the curation has enforced it throughout. Where a source reported a bare percentage without roast-degree context, the value has either been dropped, flagged with appropriate status markers, or reconstructed by interpolation from sources that did specify context.

-----

## 0 — Boundary Condition

**The Roast dossier begins where the Beans dossier ends: with a green bean entering the roaster at ambient or charge temperature.** The bean’s chemical and physical state at this moment is taken as given by BEANS-COAST-001 v0.3.2. Everything in this dossier describes what happens to the bean between the charge moment and the moment it leaves the cooling tray.

**Upstream boundary.** Green-bean storage, pre-roast conditioning, and any handling between export and the roaster intake hopper are Beans-side and outside the scope of this dossier.

**Downstream boundary.** Grinding, dosing, water contact, extraction, and brewing are Brew-side and outside the scope of this dossier. Post-roast degassing is treated here as a Roast → Brew interface process (see Interface Sheet I-2).

**Not covered here:** sensory evaluation as such (cup scores, flavour wheels, SCA cupping protocols — those belong to the Drink dossier); marketing categories used as rhetoric (“third wave,” “Nordic style,” “Italian roast” — the underlying physical parameters they imply are in scope, but the rhetorical frames are not); decaffeination processes (may be added as Interface Sheet I-3 in a later revision).

**Scope of invariance.** The parameters in this dossier fall into three categories of stability, and reading them correctly requires keeping the distinction in mind:

- *Invariant* — physical constants and well-established thermodynamic relationships (specific heat of coffee, latent heat of water, the activation energies of the Maillard reaction, caffeine’s melting point at 238 °C).
- *Bounded but context-dependent* — parameters that take a range of values across roaster types, profiles, and roast degrees, but whose ranges are well established (weight loss percentages, first crack temperature ranges, Agtron numbers for given roast degrees, CGA loss percentages).
- *Process-dependent* — parameters that cannot be specified without specifying the roaster, the profile, and the target roast degree (rate-of-rise curve shape, development time ratio, volatile compound concentrations, surface oil migration timing).

The status markers (FROZEN, PROVISIONAL, OPEN, QUARANTINED) describe evidential confidence; this scope-of-invariance distinction describes the kind of stability a parameter can have in principle.

### 0.1 — Measurement Non-Equivalence

Every numerical claim in this dossier rests on an implicit measurement model. A reported temperature is not the temperature of the bean; it is the output of a probe, a software filter, and a sampling regime. A reported rate of rise is not a physical derivative of bean temperature; it is a computed time-difference over a windowed and smoothed signal. A reported weight loss is not the mass loss at the moment of drop; it is a delayed measurement after cooling and partial degassing. In formal terms:

*observed value* = *physical state* ⊗ *measurement transfer function*

where the transfer function bundles together probe thermal mass, probe placement geometry, sensor response time, signal sampling rate, software filter kernel, and calibration history. None of these factors are invariant across roasters, and several of them are not invariant even across roasts on the same machine (probe fouling, calibration drift). Three consequences follow:

1. **Bean probe temperatures (BT) from different roasters are not directly comparable.** A “BT 200 °C at first crack” value on one drum is not the same physical event as “BT 200 °C at first crack” on another drum, because the probes occupy different positions in different bean masses with different thermal geometries. The probe lag — the delay between a real bean-state change and the corresponding probe reading — is typically 10–30 seconds for a standard drum-roaster BT probe and shorter for fluid-bed probes, but varies widely. Any cross-machine temperature comparison requires either matched calibration or explicit acknowledgement of probe non-equivalence.
1. **Rate of rise values are software-dependent as well as hardware-dependent.** Cropster, Artisan, RoastLog, and OEM platforms compute RoR over different derivative windows (typically 30–60 seconds), apply different smoothing kernels, and sample at different default intervals (Artisan default is 3 s; others vary). Two platforms logging the same raw thermocouple signal can produce RoR curves that differ in amplitude and in timing of apparent features. A RoR value cited without platform and window specification is effectively unanchored.
1. **Temporal sampling can alias rapid events.** First crack is a discrete audible event; by the time the probe registers a corresponding temperature feature, the cracking has already been in progress for several seconds. The relationship between the observed probe signal and the underlying physical event is a convolution rather than a direct mapping.

**Practical rule for the reader.** Every temperature in this dossier should be read with the implicit prefix “as measured by a properly placed bean probe on a conventional drum roaster, subject to lag and smoothing.” Fluid-bed probe readings and environmental probe readings are different observables and are flagged as such wherever they appear. This is why the §3.8 discipline in TC-ROAST-001 requires probe specification on every temperature claim: without it, the measurement model is indeterminate and the number is not a physical state but a label for an unspecified observation.

This measurement model applies uniformly to §§1–5 and is not re-derived in each section. Where a specific measurement complication is especially severe (e.g. colour measurement in §4 where surface and internal colour can diverge), the section flags it inline.

### 0.2 — Roasting as a Trajectory in State Space

A green coffee bean entering a roaster and exiting as a roasted bean traces a trajectory through a high-dimensional state space. The coordinates of that space include, at minimum:

- **Thermal state** — bean temperature, internal thermal gradient, air temperature
- **Mass state** — total mass, moisture content, residual organic matter
- **Structural state** — volume, bulk density, apparent density, porosity, cell rupture fraction, surface oil fraction
- **Chemical state** — concentrations of chlorogenic acids, trigonelline, caffeine, sucrose, free amino acids, lipids, proteins, melanoidins, acrylamide, and hundreds of volatile compounds
- **Colour state** — Agtron Gourmet, ground/whole-bean differential, internal–surface gap

The state at any moment during a roast is a point in this space, and the roasting process is a path through it. Different paths can terminate at points that share some coordinates while differing in others — two roasts reaching the same Agtron number via different time–temperature profiles may occupy overlapping but non-identical neighbourhoods of the state space.

Three structural facts about this space shape the rest of the dossier:

1. **Partial observability.** Only a subset of state-space coordinates are routinely measured in practice (bean probe temperature, time, final colour, final weight loss). The rest (internal thermal gradient, porosity, most individual compound concentrations, volatile distribution) require specialised instruments and are effectively unobserved during operation. Roasting is controlled on a projection of the full state onto a handful of observable dimensions.
1. **Irreversibility.** Every step along a roast trajectory is irreversible. Water cannot be returned to the bean; Maillard products cannot be reverted to sucrose and amino acids; the porous matrix cannot be resealed. The trajectory is one-way, which is why roast-degree terms describe an arrived-at state rather than a tunable continuous variable.
1. **Degeneracy at common endpoints.** As discussed in the introduction, different trajectories can terminate at the same surface anchors (Agtron number, weight loss) while differing in deeper chemical and structural coordinates. This is the formal reason the medium-roast anchor cannot be read as a state equivalence.

**Making the degeneracy falsifiable.** The degeneracy claim above is easy to state philosophically, but to be useful it must be *testable*. The test takes the form of a discriminant observable — a measurement that can distinguish two batches with identical surface anchors but different underlying states. Three candidates are available from the §4 and §5 evidence:

- **Surface–internal colour gap.** The difference between whole-bean and ground Agtron readings measures how much of the visible colour change penetrates the bean. Two batches at the same ground Agtron can have different whole-bean Agtron values, indicating different radial thermal histories. This is tracked under BR-05 in §7.
- **CO₂ release curve shape.** The temporal profile of CO₂ loss over the first 24–72 hours post-roast is sensitive to fracture network structure and bean porosity. Two batches at the same weight loss can produce different release curves, indicating different structural states. This is measurable with time-resolved gravimetric methods (Smrke 2018).
- **Volatile profile divergence.** GC-MS measurements of the volatile distribution at matched Agtron and weight loss can reveal differences in which Maillard and Strecker pathways dominated, which in turn reflects different trajectory histories.

The operational statement is this: **two roasts with identical surface anchors are distinguishable (the degeneracy is observable, not just philosophical) if at least one of the three discriminant observables above differs beyond measurement uncertainty.** This converts the state-degeneracy claim from a conceptual point into an experimental programme. BR-05, BR-02 (DTR-outcome closure), and any future systematic comparison of roast profiles should use at least one discriminant to verify that apparent equivalence is not surface-only.

The anti-claims register in §6, the validity contracts in each section, and the status markers throughout all derive ultimately from this state-space view: claims are valid where the observed projection matches the underlying state, and suspect where a projection is being used as if it specified the full state. The reader who keeps the trajectory-in-state-space framing in mind will find the rest of the dossier easier to navigate.

-----

## 1 — Equipment & Mechanical Configuration

### Key terms used in this section

- **Drum roaster:** A rotating cylindrical chamber in which coffee beans are heated by a combination of contact with the hot drum wall (conduction), hot air flowing through the drum (convection), and thermal radiation from the drum surface. The dominant mode in specialty coffee.
- **Fluid-bed roaster:** A chamber in which hot air at high velocity suspends the beans in a “fluid” state, heating them almost entirely by convection. Also called an air roaster or spouted-bed roaster.
- **Bean probe (BT):** A thermocouple embedded in the bean mass that approximates the temperature of the beans themselves. “Approximates” because probe lag and placement vary.
- **Environmental probe (ET):** A thermocouple in the hot air path or drum environment that measures the air temperature around the beans. Sometimes called “MET” (machine environment temperature).
- **Probe lag:** The time delay between a real temperature change in the beans and the corresponding change registered by the probe. Varies by roaster type, probe thickness, and probe placement.
- **Roasting software:** Platforms like Cropster, Artisan, and RoastLog that log temperature, rate of rise, gas input, airflow, and event markers (first crack, drop) during a roast.
- **Agtron number:** A colour measurement on the Agtron Gourmet or Commercial scale, widely used to quantify roast degree (detailed in §4).

### 1.1 Declared Parameters — Roaster Types

|Roaster type                       |Dominant heat transfer                                                                       |Typical batch / throughput range                                     |Notes                                                                                                     |Status     |
|-----------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------|
|Drum, direct-flame                 |Mixed-mode: conduction at bean–drum contact, convection from hot air, some radiation         |Sample: 50–500 g; shop: 1–15 kg; production: 15–70 kg per batch      |Surface conduction risk for scorching if drum hot and airflow low; higher thermal inertia, slower response|PROVISIONAL|
|Drum, indirect-flame / hot-air drum|Mixed-mode, convection-weighted (specific fraction not known with precision — see note below)|Similar to direct-flame drums, 1–70 kg per batch                     |Lower drum-surface temperature; more even bean-surface heating                                            |PROVISIONAL|
|Recirculating drum                 |Convection-dominant; increased gas residence time                                            |30–240 kg batch or equivalent                                        |Higher energy efficiency; requires careful exhaust and contaminant management                             |PROVISIONAL|
|Fluid-bed / spouted-bed            |Nearly pure convection; negligible conduction except rare wall contact                       |Lab/sample to industrial continuous; few hundred grams to ≥1,000 kg/h|Very fast thermal response; short roast times possible (≈3–6 min at industrial scale)                     |PROVISIONAL|
|Tangential roaster                 |Strong convection with some impact/conduction                                                |Industrial, hundreds of kg/h                                         |Rotating slotted drum or disk throws beans into hot-air stream; tight residence-time control              |PROVISIONAL|
|Centrifugal roaster                |Convection-dominant; some conduction where beans contact metal                               |Pilot to industrial                                                  |Used where gentle handling and rapid heat transfer are needed                                             |PROVISIONAL|
|IR-assisted / hybrid               |Radiation at surface plus convection; conduction via drum still present                      |Mainly shop and small production scales                              |IR component can increase surface heating rate; risk of surface overdevelopment without adequate mixing   |PROVISIONAL|

**On heat transfer mode fractions.** Several agent returns (Perplexity, Kimi) cite a “~70% convection / ~30% conduction” figure for modern indirect-flame drums, attributed to engineering analyses and manufacturer communications. This dossier does not freeze that number. Heat transfer in a drum roaster is not a stable global fraction — it varies during the roast itself (charge, turning point, drying phase, Maillard phase, development) as bean mass, airflow, drum wall temperature, and bean–bean contact change. It varies across machines as drum geometry, perforation pattern, and airflow design differ. It varies across operators as airflow and burner settings differ. The honest statement is that **modern indirect-flame drums with forced airflow are convection-weighted rather than conduction-weighted**, and that the convection-weighted regime does not hold for legacy solid drums without forced airflow. A specific single number like “70/30” should be read as a rough engineering label for a region, not as a measured parameter. Any claim that depends on a precise heat-transfer fraction (e.g. cup-outcome predictions tied to drum type) is standing on a number that is not known at that precision.

### 1.2 Declared Parameters — Scale Categories

|Scale                |Batch / throughput                        |Typical equipment                                                    |Control characteristics                                                                                                          |Status                      |
|---------------------|------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------|
|Sample roaster       |≈50–500 g per batch                       |Small gas/electric drum, mini fluid-bed, centrifugal sample units    |Very low thermal inertia; fast response but high probe noise; probe lag can be large relative to total roast time                |FROZEN (industry convention)|
|Shop / boutique      |≈1–15 kg per batch                        |Drum (direct/indirect flame), some small recirculating or IR-assisted|Moderate thermal inertia; responsive enough for profile shaping; typical BT/ET logging with manual or semi-automatic control     |FROZEN (industry convention)|
|Production batch     |≈15–70 kg per batch                       |Larger drum or recirculating roasters; some hybrid convection systems|High thermal inertia; slower response to gas and airflow changes; PLC-controlled; more stable between batches once at equilibrium|FROZEN (industry convention)|
|Industrial continuous|Typically ≥250 kg/h (240–1,000 kg/h lines)|Continuous drum–convection lines, fluid-bed and tangential roasters  |Residence time controlled by conveyor or pneumatic retention; strong emphasis on energy efficiency and consistency               |FROZEN (industry convention)|

**Note on the upper batch boundary.** Perplexity reports production batch as 15–70 kg, which is tighter than the task-card placeholder of 15–250 kg. Kimi reports the wider 15–250 kg range. The tighter Perplexity figure comes from manufacturer documentation (PROBAT, Loring, Bühler); the wider Kimi figure comes from practitioner classification. This dossier adopts 15–70 kg as the typical per-batch range for “production batch” roasters, and treats 70–250 kg as the crossover region to industrial scale. This distinction matters because the heat transfer regime and control problem change around the upper boundary.

### 1.3 Instrumentation

|Instrument                 |What it measures                                           |Standard / common / research / aspirational                         |Notes                                                                                                  |Status     |
|---------------------------|-----------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------|
|Bean temperature probe (BT)|Bean mass temperature                                      |Standard on specialty and modern industrial roasters                |Crucial for profile logging; probe placement and mass strongly affect lag and noise                    |FROZEN     |
|Environmental probe (ET)   |Air temperature in drum / hot-air path                     |Standard to common                                                  |Used with BT to infer heat-transfer dynamics; sometimes labelled “MET”                                 |FROZEN     |
|Exhaust temperature        |Air leaving drum                                           |Common on production/industrial systems                             |Inferred overall energy balance and filter/afterburner loading; not directly interpreted for bean state|FROZEN     |
|Drum speed sensor          |Tachometer or encoder                                      |Common on drum roasters ≥5 kg; sometimes fixed on very small drums  |Adjusts mixing intensity and contact time; affects conduction vs convection balance                    |FROZEN     |
|Airflow / pressure         |Fan-speed control, manometer, differential-pressure sensors|Common to research-level; increasingly standard on high-end roasters|Key for convection dominance and smoke removal; calibration and units differ by manufacturer           |FROZEN     |
|Gas pressure / burner duty |Pressure transducers or digital valve setpoints            |Common                                                              |Logged as proxy for energy input; not directly comparable across machines without calibration          |FROZEN     |
|In-bean moisture sensors   |Dielectric or microwave sensors                            |Research-only / aspirational                                        |Used in a few academic studies; not yet standard                                                       |PROVISIONAL|
|Real-time colour sensors   |Optical sensors in roast chamber or trier; sometimes NIR   |Research / aspirational                                             |Early-stage implementations for automatic end-point detection; subject to fouling and calibration drift|PROVISIONAL|

**Probe thickness trade-off.** Kimi reports that roughly 3 mm is a common industry recommendation balancing response time and durability; thinner probes (~1.5 mm) respond faster but are more fragile. No peer-reviewed study establishes an optimal probe diameter; the recommendations are experience-based.

### 1.4 Software Platforms

|Platform      |Type            |Key features                                                                        |Status              |
|--------------|----------------|------------------------------------------------------------------------------------|--------------------|
|Cropster      |Commercial SaaS |Full supply chain integration; inventory; cupping; gas/airflow replay; cloud storage|FROZEN (widely used)|
|Artisan       |Open-source     |Real-time plotting; community-supported; highly configurable; local + optional cloud|FROZEN (widely used)|
|RoastLog      |Commercial SaaS |Business management focus; inventory; scheduling; cloud                             |FROZEN (widely used)|
|Typica        |Open-source     |Basic roast logging; simpler interface; local                                       |PROVISIONAL         |
|OEM integrated|Roaster-specific|Varies by manufacturer                                                              |PROVISIONAL         |

**Critical note on cross-platform comparison.** GPT, Kimi, and Perplexity all flag that roasting software platforms “converge on a common data model” (time, BT, ET, RoR, milestones, gas, airflow, drum speed, roast colour, weight loss) *but do not create metrological equivalence between machines*. Cropster and Artisan use different algorithms for RoR calculation, different default sampling rates (Artisan default is 3 s; Cropster differs), and different smoothing windows. Direct numerical comparison across platforms requires careful calibration or is simply invalid.

### 1.5 Cooling Systems

|Cooling method              |Implementation                                            |Time scale                                                          |Notes                                                                                                                                          |Status|
|----------------------------|----------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------|
|Tray cooling with forced air|Perforated tray with stirring arms; strong ambient-air fan|~2–4 min to near-ambient for ≤15 kg batches; longer for larger loads|Standard in shop and mid-scale production roasters; can be sized to allow simultaneous roast and cool                                          |FROZEN|
|Conveyor / belt cooler      |Perforated belt with crossflow air                        |Variable; matched to continuous throughput                          |Common in industrial lines; facilitates integration with destoners and packaging                                                               |FROZEN|
|Water quench                |Fine water mist applied near end of roast or in cooling   |Seconds to reduce surface temperature; internal temperature lags    |Used mainly in commodity/soluble coffee to reduce weight loss and fix colour; generally avoided in specialty due to flavour and safety concerns|FROZEN|

### 1.6 Validity Contract

- All temperature-related claims in this dossier assume properly calibrated thermocouples with known placement. Specific numeric “first crack” or “drop” temperatures cannot be compared across different probe geometries or positions without calibration curves.
- Batch-size ranges and scale definitions are industrial conventions, not ISO/SCA standards. They are valid as order-of-magnitude anchors but not as strict thresholds.
- Heat-transfer mode fractions in drum roasters (“convection-weighted,” “conduction-weighted”) are qualitative regime labels, not measured parameters. Specific numeric fractions (e.g. “70% convection”) circulate in engineering literature but do not survive scrutiny as a stable global figure — see §1.1 note. Claims that depend on a precise fraction should be treated as speculative.
- Qualitative statements about cup characteristics by roaster type (e.g. “air roasters yield cleaner cups”) are primarily practitioner claims and not valid as general causal claims without roast-profile, green-origin, and brew-method control.
- Cooling-time ranges assume typical specialty practice at standard ambient conditions; industrial systems may intentionally operate at different cooling rates.

### 1.7 Open Disputes

- **Conduction versus convection dominance in drum roasters.** Some practitioner sources describe traditional drum roasters as conduction-dominant; more recent engineering analyses describe modern well-ventilated drums as convection-weighted. Best reconciliation: drums are mixed-mode; the balance depends on machine, airflow, charge temperature, and phase of roast. Specific numeric fractions should not be taken as stable parameters (see §1.1 note). The qualitative shift from legacy solid drums to modern ventilated drums is real; the quantitative fraction is not pinned down.
- **Cup impact of heat-transfer mode.** Practitioner narratives often claim that conduction-heavy roasts yield more body and “roasty” flavours, while high-convection systems yield cleaner, more articulate acidity. Published experiments that compare equipment types rarely match roast degree and profile tightly, so equipment-vs-cup claims remain weakly evidenced.
- **Utility of advanced instrumentation.** There is disagreement among roasters about the value of additional probes (multiple BT, exhaust sensors, real-time colour) versus simplicity. Inconsistent calibration and added noise can mislead operators relative to sensory and colour cues.
- **Water quenching acceptability.** Industrial literature presents water quenching as a legitimate tool to reduce weight loss and fix colour at high throughput; specialty roasting regards it as detrimental to flavour development. This is a genuine craft-vs-industrial divide, not an empirical dispute.

### 1.8 Downstream Interface

Equipment determines the shape of the time–temperature trajectory that §2 describes and the heat-transfer regime that shapes the chemistry in §3. Different roasters produce different final-state porosity and density profiles (§4). A given roast profile — even one specified as Agtron 55 with 14.5% weight loss — can produce different cup outcomes on different equipment, which is one of the reasons equipment-type-to-cup claims are so hard to close.

-----

## 2 — Thermodynamic Envelope

### Key terms used in this section

- **Charge temperature:** The bean probe temperature at the moment the beans are dropped into the preheated roaster.
- **Turning point:** The minimum bean probe temperature reached shortly after charge, as the beans absorb heat from the drum before equilibrating. The trajectory then reverses and begins climbing.
- **Yellowing:** The stage in a roast (approximately 150 °C bean probe) when moisture is largely gone and the beans shift from green to yellow, marking the onset of the Maillard reaction.
- **First crack:** An audible cracking sound (like popcorn) as water vapour and CO₂ escape from the bean, typically around 190–205 °C bean probe. Marks the onset of light-roast territory.
- **Second crack:** A second, sharper cracking sound at higher temperatures (typically 225–235 °C BT), marking dark-roast territory. Associated with structural breakdown and pyrolysis.
- **Drop:** The moment the roaster door is opened and the beans are released to the cooling tray.
- **Rate of rise (RoR or RoR):** The time derivative of bean temperature, typically expressed as °C/min or °F/min over a 30–60 second window. The primary modern roast-control variable.
- **Development time ratio (DTR):** The proportion of total roast time spent between first crack and drop, expressed as a percentage. A practitioner control parameter.

### 2.1 Declared Parameters — Reference Temperature Points

*All temperatures below are bean probe (BT) unless otherwise noted. Per §3.8 of TC-ROAST-001, temperatures without probe specification are flagged* `[PROBE-UNSPECIFIED]` *and held as PROVISIONAL.*

|Reference point                |Typical BT range           |Roast degree context                   |Status                  |Source                                                                                                          |
|-------------------------------|---------------------------|---------------------------------------|------------------------|----------------------------------------------------------------------------------------------------------------|
|Charge temperature             |180–230 °C (drum preheated)|Varies by roaster and target roast     |PROVISIONAL             |Practitioner literature (Kimi); software documentation (GPT, Perplexity)                                        |
|Turning point                  |82–104 °C                  |Minimum BT after charge                |PROVISIONAL             |Industry standard (Kimi); Artisan logs (GPT, Perplexity)                                                        |
|Yellowing                      |~150 °C                    |End of drying phase                    |PROVISIONAL             |Maillard onset (Kimi, GPT concordant)                                                                           |
|First crack onset              |196–205 °C                 |Light to medium roasts; probe-dependent|PROVISIONAL — RANGE ONLY|Practitioner (Kimi); Artisan documentation (GPT); commonly cited ~196 °C figure explicitly disputed as universal|
|First crack end                |205–220 °C                 |Light-end of light roast               |PROVISIONAL             |Practitioner (Kimi)                                                                                             |
|Second crack onset             |225–235 °C                 |Dark roast threshold                   |PROVISIONAL             |Practitioner (Kimi)                                                                                             |
|Drop temperature (light roast) |180–205 °C                 |Just after first crack                 |PROVISIONAL             |Practitioner (Kimi); SCA Q-grader anchor (GPT)                                                                  |
|Drop temperature (medium roast)|210–220 °C                 |Balanced development                   |PROVISIONAL             |Practitioner (Kimi); SCA Q-grader anchor (GPT)                                                                  |
|Drop temperature (dark roast)  |240+ °C                    |Beyond second crack                    |PROVISIONAL             |Practitioner (Kimi)                                                                                             |

**Critical note on “first crack at 196 °C.”** This is the single most commonly cited specific temperature in roasting literature, and it is wrong as a universal claim. First crack is fundamentally an audible event produced by water vapour and CO₂ escaping the bean under pressure. The temperature at which the probe registers this event depends on probe type, probe placement, roaster design, batch size, bean density, and moisture content. Variation of ±10–20 °C between machines for the same bean is normal. The 196–205 °C range above is a useful reference for drum roasters with standard BT probe placement, but it is not universal and must not be treated as a fixed temperature target. This is registered as RAC-06 in §6.

### 2.2 SCA Colour Anchors

GPT provided Agtron reference points from SCA Q-grader preparation literature that are more portable than milestone temperatures because they are method-defined rather than probe-dependent:

|Anchor                           |Ground Agtron|Whole-bean Agtron|Status|
|---------------------------------|-------------|-----------------|------|
|“Optimum” roast (Q-grader target)|~63          |~58              |FROZEN|
|“Too light” threshold            |~75          |~68              |FROZEN|
|“Too dark” threshold             |~55          |~45              |FROZEN|

These are standardised reference points for sensory evaluation, not thermodynamic endpoints, but they provide a method-independent way to anchor roast degree.

### 2.3 Rate of Rise (RoR)

Rate of rise is mathematically the time derivative of bean temperature: *dT/dt*, typically computed over a 30 or 60 second window. Modern roast control treats it as the primary control variable. Its interpretation in the literature splits sharply between practitioner control heuristics and peer-reviewed physics.

|Metric                           |Typical range     |Status                         |
|---------------------------------|------------------|-------------------------------|
|Peak RoR (after turning point)   |8–14 °C/min       |PROVISIONAL (practitioner)     |
|RoR at first crack               |4–7 °C/min        |PROVISIONAL (practitioner)     |
|Desired curve shape              |Smoothly declining|PRACTITIONER CONSENSUS         |
|Standard measurement window      |30–60 seconds     |FROZEN (software documentation)|
|Artisan default sampling interval|3 s               |FROZEN                         |

**“Crash and flick.”** A sharp RoR drop (“crash”) followed by a rebound (“flick”), typically around first crack. Widely treated in practitioner literature as a red-flag control pattern to be avoided. Evidence that it actually degrades cup quality is contested — strong craft consensus exists, but controlled sensory evidence is limited. This is registered as RAC-04 in §6.

**Cross-software RoR comparisons are unsafe.** Cropster and Artisan use different smoothing algorithms and different derivative windows. A RoR value logged in Cropster is not directly comparable to one logged in Artisan, even for the same raw temperature data.

### 2.4 Phase Ratios

Roasters conventionally divide a roast into three phases and aim for target proportions of total time in each:

|Phase                                        |Practitioner target|Actual range|Evidential basis                                                  |Status                    |
|---------------------------------------------|-------------------|------------|------------------------------------------------------------------|--------------------------|
|Drying (charge → yellowing)                  |40–50%             |35–55%      |Practitioner consensus; no peer-reviewed support                  |PROVISIONAL (practitioner)|
|Maillard / browning (yellowing → first crack)|30–35%             |25–40%      |Practitioner consensus                                            |PROVISIONAL (practitioner)|
|Development (first crack → drop)             |15–25%             |12–30%      |Practitioner consensus; specific 20–25% DTR target is widely cited|PROVISIONAL (practitioner)|

**Phase ratio targets are craft heuristics, not experimentally validated optima.** GPT and Kimi agree on this point explicitly. The 20–25% DTR target originates with Scott Rao’s *The Coffee Roaster’s Companion* (2014) and has been widely adopted, but no peer-reviewed study has systematically tested its effect on cup quality. Some roasters report excellent results with DTR as low as 12% (bright, acidic profiles) and as high as 30% (deep, developed profiles). This is registered as RAC-03 in §6.

### 2.5 Apparent Exothermic Behaviour Around First Crack

Practitioner and some technical literature describe an “endothermic-to-exothermic transition” around first crack, where the bean’s thermal behaviour shifts from absorbing heat (for moisture loss and early Maillard chemistry) to generating heat (from continuing Maillard, caramelisation, and early pyrolysis). The observation — that bean probes often show a reduced rate of external heat input required to maintain the temperature rise around first crack — is real and widely reproducible. The interpretation is less secure than practitioner diagrams sometimes suggest.

**A more careful framing.** Around first crack, apparent exothermic behaviour emerges from the combination of (a) continuing chemical heat release from Maillard and early pyrolysis reactions, (b) reduced evaporative cooling as moisture is largely depleted, and (c) altered heat-transfer geometry as the bean expands and becomes more porous. These three effects together can look like a phase transition on a probe trace, but they are not sharply separable and the transition is not discrete. Strictly speaking, there is no single “exothermic phase” that begins at a defined moment — there is a continuous shift in the balance of energy terms, which the probe registers as a change in required gas input to maintain the temperature trajectory.

The practical observation is reliable. The cleaner statement is: **around first crack, a roaster can typically reduce external heat input without the bean temperature falling**, because the combination of reduced evaporative cooling and chemical heat release now compensates for a larger share of the heat demand than earlier in the roast. Whether this constitutes a “transition” or merely a progressive shift in an energy balance is partly a matter of framing.

### 2.6 Energy Accounting — A Qualitative Closure Scaffold

Direct calorimetric measurements of coffee roasting (kJ/kg of green coffee) are surprisingly sparse in the open literature. What is commonly reported instead are proxy variables: gas pressure profiles, airflow settings, burner duty cycle, and drum speed. This dossier does not attempt to freeze an absolute energy figure. Per TC-ROAST-001 §5.2, proxies are acceptable where absolute energy data is absent, and they should not be silently upgraded into energy balances.

However, refusing to freeze specific numbers does not mean the thermodynamics must be left entirely black-boxed. At minimum, a qualitative energy closure scaffold is available, and it is worth stating explicitly because it constrains which parameters can vary independently:

> **Q_in ≈ Q_evap + Q_chem + Q_loss + Q_storage**

where:

|Term         |Meaning                                                                                                          |Dominant phase                               |Qualitative bound                                                                    |
|-------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------|
|**Q_in**     |Total energy delivered to the bean mass (convection + conduction + radiation from the roaster)                   |All phases                                   |Bounded above by the burner/electrical input minus roaster losses                    |
|**Q_evap**   |Energy consumed by water evaporation (≈2.26 MJ per kg of water removed, plus sensible heat from 25 °C to boiling)|Drying phase, tapering through Maillard phase|Directly tied to green-bean moisture content (§4.4) and weight-loss accounting (§4.1)|
|**Q_chem**   |Net chemical energy: endothermic Maillard-phase reactions early, exothermic Maillard/pyrolysis reactions late    |Maillard phase and development               |Sign flips during the roast; magnitude poorly quantified in coffee specifically      |
|**Q_loss**   |Energy lost to exhaust gases, drum walls, and radiation from the roaster body                                    |All phases; larger at higher ET              |Roaster-dependent; addressed by roaster thermal inertia and insulation               |
|**Q_storage**|Net sensible heat stored in the bean mass as its temperature rises                                               |All phases                                   |Tied to heat capacity of coffee (~1.1–1.3 kJ/kg·K) and bean temperature trajectory   |

**Why this scaffold matters even without frozen numbers.** First, it anchors §2 to thermodynamics rather than pure trajectory description. Two roast profiles with different Q_evap histories (e.g. different moisture at charge) must differ somewhere — in Q_in, Q_loss, Q_storage, or the timing of Q_chem — even if they produce the same final Agtron. Second, it links §2 directly to §3 (Q_chem and reaction windows) and to §4 (Q_evap and weight loss accounting). Third, it provides a structural reason why equipment-to-cup claims are so hard to close: two different roasters may deliver different Q_in trajectories with different Q_loss distributions to reach the same endpoint, implying different internal thermal gradients even at matched Agtron.

**Status of the scaffold.** PROVISIONAL, and explicitly qualitative. Each term above has order-of-magnitude estimates in the food science literature (Q_evap from latent heat of water times moisture fraction; Q_storage from coffee heat capacity times ΔT; Q_loss from roaster energy audits), but the specific coffee-roasting literature is thin. A serious closure would require calorimetric data during active roasts, which is not routinely available. What the scaffold provides is not prediction but **constrained trajectory space**: not every profile is physically consistent, and identifying the constraint set is a prerequisite for meaningful profile comparison.

### 2.7 Validity Contract

- Milestone temperatures are only meaningful when the source specifies probe type, probe location, and roaster class.
- RoR values are sensitive to sampling rate, smoothing, and derivative window; cross-software comparisons can differ even for the same raw roast.
- Agtron colour anchors are generally more portable for roast-degree comparison than milestone temperatures.
- Phase ratios should be treated as bounded heuristics, not hard thermodynamic laws.
- Absolute energy claims require direct calorimetric or fuel/power accounting; proxy variables should not be promoted to energy balances.
- Probe lag varies between drum (slower-responding due to higher thermal mass) and fluid bed (faster-responding, but different placement dynamics). Cross-roaster-type comparisons require explicit acknowledgement of this difference.

### 2.8 Open Disputes

- **Universal first crack temperature.** 196 °C is frequently cited as “the” first crack temperature. Evidence strongly contradicts this as universal; the value varies 10–20 °C across equipment. Resolution: first crack is defined by the audible event, not by the temperature, and any temperature citation must specify probe and roaster context.
- **DTR optimality.** 20–25% is widely cited as optimal; experimental support is weak; working roasters report good results across a much wider range.
- **Crash-and-flick cup impact.** Strong practitioner consensus against; limited controlled sensory evidence.
- **Fixed phase ratio targets.** Commonly taught; evidential basis weak; should be used as starting guidelines rather than rules.
- **Endothermic/exothermic transition timing.** The phenomenon is real; the precise operational detection is less secure than some practitioner diagrams suggest.

### 2.9 Downstream Interface

The time–temperature trajectory determines which Maillard pathways dominate (§3.1). Volatile compound yield (§5) depends on the full trajectory, not just the endpoint — two roasts reaching the same Agtron number via different paths can produce different volatile profiles. This is part of why the precursor-to-volatile mapping question (BR-04) remains open.

-----

## 3 — Roast Chemistry

### Key terms used in this section

- **Maillard reaction:** The reaction between reducing sugars (glucose, fructose) and amino acids that produces colour, flavour, and aroma. The same chemistry that browns bread and seared meat. Dominates roughly 150–200 °C.
- **Strecker degradation:** A secondary Maillard pathway producing aldehydes — key aroma compounds derived from specific amino acids (e.g., methional from methionine).
- **Caramelisation:** Sucrose breakdown independent of amino acids, producing smaller sugars and browning products. Dominates roughly 170–200 °C. Distinct from Maillard, though often co-occurring.
- **Pyrolysis:** Thermal decomposition of compounds at higher temperatures (above ~220 °C bean probe), producing carbon-heavy fragments, smoke, and bitter compounds.
- **Chlorogenic acids (CGAs):** A family of plant phenolic compounds that contribute bitterness and astringency. Explained in BEANS-COAST-001 §5.
- **Trigonelline:** A nitrogen-containing compound related to vitamin B3 that breaks down during roasting into aromatic pyridines, pyrroles, and nicotinic acid.
- **Melanoidins:** Dark-coloured polymeric compounds formed in late Maillard stages. Poorly characterised structurally but contribute to coffee’s colour, body, and antioxidant activity.
- **Acrylamide:** A regulated food-safety compound formed during roasting from asparagine and reducing sugars via the Maillard pathway.

### 3.1 Declared Parameters — Reaction Windows

|Reaction class      |Temperature window (BT)|Dominant roast phase                          |Key products                                                                      |Status|
|--------------------|-----------------------|----------------------------------------------|----------------------------------------------------------------------------------|------|
|Moisture evaporation|Charge to ~150 °C      |Drying phase                                  |Water vapour                                                                      |FROZEN|
|Maillard reaction   |140–200 °C             |Maillard phase, continuing through development|Pyrazines, furans, melanoidins, Strecker aldehydes, hundreds of volatile compounds|FROZEN|
|Strecker degradation|~150–200 °C            |Maillard phase                                |Aldehydes (methional, phenylacetaldehyde, etc.)                                   |FROZEN|
|Caramelisation      |170–200 °C             |Late Maillard phase, parallel to Maillard     |Smaller sugars, browning products, furans                                         |FROZEN|
|Pyrolysis           |>220 °C                |Development and beyond second crack           |Carbon-heavy fragments, smoke, phenolic compounds                                 |FROZEN|

**A methodological note on overlapping reaction regimes.** GPT flags that in the bean matrix, caramelisation overlaps with Maillard and pyrolysis rather than occurring in isolation. The simplified sugar-only caramelisation thresholds from food-science textbooks should be read as illustrative, not as clean operational boundaries inside a roasting bean. Similarly, **pyrolysis is not a distinct onset at a sharp temperature but a regime in which fragmentation reactions progressively dominate over synthesis reactions.** The “>220 °C” threshold in the table above marks the temperature above which pyrolytic decomposition becomes a significant contributor to the overall reaction mix, not a phase boundary. In the same region, Maillard chemistry continues and caramelisation still occurs. The cleanest reading of the reaction windows table is that each temperature range identifies where a given reaction class *peaks* or becomes important, not where it begins or ends.

### 3.2 Declared Parameters — Compound Degradation (Roast-Degree Anchored)

*This table replaces and extends Interface Sheet I-1 from the Beans dossier. Kimi provided the most granular roast-degree-anchored data, cross-checked against the GPT return which argued for holding bare loss percentages as provisional pending endpoint-normalised tables.*

|Compound                 |Green content (from BEANS-COAST-001 §5.1)|Light roast loss      |Medium roast loss (Agtron ~55)              |Dark roast loss                                  |Status                                            |
|-------------------------|-----------------------------------------|----------------------|--------------------------------------------|-------------------------------------------------|--------------------------------------------------|
|Chlorogenic acids (total)|3.5–8.4% (Arabica); 7–14% (Robusta)      |~30–40%               |~50–60%                                     |~80–95%                                          |PROVISIONAL                                       |
|Trigonelline             |0.8–1.3% (Arabica); 0.6–1.0% (Robusta)   |Partial; ~200 °C onset|Substantial                                 |Extensive                                        |PROVISIONAL (quantitative fractions uncertain)    |
|Caffeine                 |0.8–1.7% (Arabica); 1.7–4.0% (Robusta)   |<2%                   |<3%                                         |<5%                                              |FROZEN (the key fact is stability)                |
|Sucrose                  |5–9% (Arabica); 0.9–5% (Robusta)         |~50–70%               |Near-complete                               |Complete                                         |FROZEN                                            |
|Free amino acids         |0.3–3%                                   |Variable by residue   |Variable by residue                         |Substantial; arginine largely consumed           |PROVISIONAL                                       |
|Lipids (triglycerides)   |13–17% (Arabica); 7–11% (Robusta)        |Minimal               |Minimal                                     |Minimal in bulk; surface migration in dark roasts|FROZEN (bulk stability); PROVISIONAL (surface oil)|
|Proteins                 |10–15%                                   |Partial denaturation  |Partial denaturation; Maillard participation|Extensive participation; melanoidin formation    |PROVISIONAL                                       |

**On the Interface Sheet I-1 placeholder values.** The Beans dossier Interface Sheet I-1 previously carried a “~54% CGA loss” figure without roast-degree context, which GPT correctly flagged as insufficient. Kimi’s endpoint-anchored table above now resolves this gap: light ~30–40%, medium (Agtron 55) ~50–60%, dark ~80–95%. The “54%” figure sits within the medium roast range and is now properly bounded. Similarly, the “~7.7% trigonelline loss” placeholder is explicitly rejected by GPT as too specific to float without endpoint context; the curation agrees and leaves trigonelline loss as “partial → substantial → extensive” rather than assigning a single number.

**Caffeine stability is the most robust finding in this section.** Caffeine’s melting point is 238 °C, higher than typical roasting temperatures. HPLC analysis reported by Kimi (sourced to PMC 11586412) shows: green 166.72 mg/L, light 196.35 mg/L, medium 203.63 mg/L, dark 189.85 mg/L — indicating minimal caffeine destruction and the apparent increase in lighter roasts is dominated by weight-loss concentration effects. This resolves RAC-01 decisively.

### 3.3 Food Safety — Acrylamide

Acrylamide is a regulated food-safety concern formed during the Maillard reaction from asparagine and reducing sugars. Coffee is one of several regulated matrices under EU Regulation 2017/2158.

|Parameter                       |Value                                         |Context                                        |Status                                            |Source                          |
|--------------------------------|----------------------------------------------|-----------------------------------------------|--------------------------------------------------|--------------------------------|
|Formation mechanism             |Maillard pathway: asparagine + reducing sugars|Low-moisture conditions above 120 °C           |FROZEN                                            |EU Reg 2017/2158; EFSA 2015     |
|Peak formation                  |Early-to-mid Maillard phase (pre–first crack) |Declines as asparagine is depleted             |FROZEN (direction); PROVISIONAL (timing specifics)|Regulatory and review literature|
|EU benchmark (roasted coffee)   |400 μg/kg                                     |Mitigation benchmark, not safe/unsafe threshold|FROZEN                                            |EU Reg 2017/2158                |
|EU benchmark (instant coffee)   |850 μg/kg                                     |Separate category                              |FROZEN                                            |EU Reg 2017/2158                |
|Typical levels in roasted coffee|150–400 μg/kg; median ~203 μg/kg              |EFSA data; varies by bean and profile          |PROVISIONAL                                       |EFSA (cited by Kimi)            |
|Robusta vs Arabica              |Higher in Robusta                             |Higher asparagine content in green Robusta     |PROVISIONAL                                       |Kimi                            |

**Regulatory framing matters.** The 400 μg/kg and 850 μg/kg figures are *investigation thresholds*, not legal limits and not direct toxicological thresholds for consumers. A coffee exceeding 400 μg/kg triggers a regulatory investigation, not a ban. This distinction is often muddled in popular reporting and should not be muddled here.

### 3.4 Melanoidins, Polymerisation, and the Unclosed Mass Balance

Melanoidins are the dark, high-molecular-weight polymers formed in late Maillard stages. They are structurally poorly defined — better described by their properties than by a single molecular formula. They contribute to coffee’s colour, mouthfeel (body), and measurable antioxidant activity. The claim that “roasting destroys nutritional value” (RAC-10) is contradicted primarily by melanoidin formation: roasting transforms some compounds, loses others, and creates new ones including melanoidins and nicotinic acid (vitamin B3, from trigonelline breakdown).

**The mass balance across the roast is not closed in the open literature.** This is a more consequential observation than it first appears, and it needs to be named explicitly. The literature reports, with reasonable confidence, how much of each precursor (sucrose, chlorogenic acids, trigonelline, amino acids) is destroyed during roasting. It reports, in aggregate, the total weight loss of the bean. But the accounting does not close: the mass lost from the precursor pool is not fully traced into the volatile pool, the melanoidin pool, the water vapour pool, the CO₂ pool, and the residual char pool. Specific pathways are known qualitatively, and a few (e.g. Strecker degradation routes) are quantified in model systems. The comprehensive mass balance — *all precursor mass in* = *all product mass out* — does not exist as a closed accounting in the published literature.

Melanoidins specifically are an **unknown-fraction sink**. They are known to form, known to contribute to colour and body, and known to account for some portion of the mass lost from the sucrose, amino acid, and chlorogenic acid pools. What fraction of each precursor ends up in the melanoidin pool at any given roast endpoint is not well characterised. This is partly because melanoidins are not a single compound (they are a heterogeneous family of polymers with varying molecular weights) and partly because extracting and quantifying them is analytically difficult.

The consequence for this dossier is that several apparent asymmetries in §3 (strong data on degradation, weaker data on formation) are not curation artefacts but reflect the actual state of the literature. The §3.2 compound degradation table is one-sided by necessity. The volatile-formation side is covered in §5 at the class level, but the quantitative precursor-to-product mapping remains open and is tracked as BR-04. The polymer-sink side (melanoidins, brown polymers, char fractions in dark roasts) is acknowledged here but not tabulated because the data to tabulate is not available. **This is a research gap, not a curation gap**, and is tracked as a new open question BR-06 (see §7).

**The triadic structure of BR-06.** The mass balance gap can be decomposed into three terms with different epistemic status, which is worth making explicit because it organises the research programme:

1. **Precursor loss** — reasonably well quantified at the level of individual compound classes (CGAs, trigonelline, sucrose, free amino acids) in the §3.2 table. Endpoint-anchored ranges are available; uncertainty is bounded.
1. **Volatile formation** — partially mapped. Qualitative pathways are established; quantitative yields per precursor are underdetermined. This is BR-04.
1. **Polymer sink** — essentially unmapped. Melanoidins and brown polymer fractions are known to form, but the fraction of each precursor pool that ends up in the polymer sink at any given roast endpoint is not characterised. This is BR-06 proper.

**A formal definition of the gap.** Even without quantitative values, the closure error can be written as:

> **closure error** = **precursor loss** − ( **volatile formation** + **CO₂ + H₂O release** + **measured residues** + **polymer sink** )

At roast completion, this error should equal zero (conservation of mass). In practice, literature values for the first two terms come from compound-level measurements, the third from gravimetric degassing studies, the fourth from residual-compound HPLC, and the fifth from melanoidin isolation studies. The four known terms rarely add up to the measured precursor loss in a fully closed way, and the residual is implicitly attributed to the polymer sink. A direct measurement of the polymer sink fraction would close the balance; no such measurement is routinely available in the coffee literature.

This formal definition is the practical content of BR-06. Cross-linked to BR-04 (volatile formation) and to §4.1 weight-loss accounting, it defines what would need to be measured to close the mass balance: (a) the polymer fraction of roasted coffee at multiple endpoints, (b) the precursor residuals at those same endpoints, and (c) the volatile and gas-phase loss integrated over the roast. None of these is individually difficult; the difficulty is doing all three simultaneously on the same batch under controlled conditions.

### 3.5 Validity Contract

- Every quantitative loss percentage in this section must be paired with a roast endpoint. Claims without roast-degree context are not usable and should be flagged `[ROAST-DEGREE-UNDEFINED]`.
- “Bean temperature” without probe definition is inadequate for chemical comparison because BT, ET, IR surface, and exhaust temperatures are not interchangeable.
- Apparent increases in compound concentration on a mass basis may partly reflect concentration-after-weight-loss rather than absolute synthesis. The caffeine apparent-increase in lighter roasts is the canonical example.
- Food-safety benchmark levels are regulatory control values, not direct consumer toxicology.
- Reaction pathways are well-established qualitatively; reaction kinetics in the specific bean matrix are only partially mapped. Most reported loss figures are averages across conditions rather than mechanistic constants.

### 3.6 Open Disputes

- **Exact CGA loss fractions by roast endpoint.** GPT flags that reviews agree on strong decline but differ on reported percentages depending on roast degree, species, and analytical method. Kimi provides the endpoint-anchored ranges adopted in §3.2, but these should be cross-checked against the Alcantara 2025 and Obando 2024 primary sources before promotion to FROZEN.
- **Trigonelline loss quantification.** The literature supports substantial decline but not a portable single percentage. Left as “partial → substantial → extensive” in §3.2.
- **Acrylamide peak timing.** General consensus on early peak (pre–first crack); limited published data on profile-specific timing.
- **Surface oil migration in dark roasts.** Widely observed practitioner phenomenon; quantitative studies of migration rate and its cup impact are sparse. In v0.3.1, this dispute has been given a formal structural scaffold in §4.6 (Π_oil transport model with percolation framing) and a quantitative research programme in BR-07 (§7). The dispute is still open on the numerical side but no longer qualitative on the mechanism.

### 3.7 Downstream Interface

The precursor pools degraded in this section are the substrate for the volatile compounds described in §5. Maillard and Strecker pathways generate furans, pyrazines, pyrroles, and sulfur compounds. CGA degradation yields phenolic volatiles (guaiacol, 4-vinylguaiacol). Trigonelline yields pyridines and pyrroles. Lipid oxidation yields aldehydes and ketones. The mapping between precursor class and volatile class is mechanistically established; the quantitative yields are not. This is the central content of BR-04.

-----

## 4 — Physical Changes & Measurable Endpoints

### Key terms used in this section

- **Weight loss:** The percentage reduction in mass from green bean to roasted bean, typically 11–20% depending on roast degree.
- **Bulk density:** The mass per unit volume of a container of beans, including the air spaces between beans. Distinct from true (or apparent) density, which measures the bean material itself.
- **Porosity:** The fraction of bean volume occupied by air spaces (internal voids and cell cavities) after roasting. Green beans have ~20–30% porosity; dark roasts can reach ~60%.
- **Agtron Gourmet scale:** A near-infrared reflectance measurement of roasted coffee colour, typically reported as a number from ~25 (very dark) to ~95 (very light). The industry-standard roast-degree indicator.
- **CIELAB:** A colour space (L*a*b*) used in some research and some roasting systems (e.g. Probat’s Colorette) that measures perceptual lightness and colour coordinates.
- **Water activity (aw):** The fraction of water in the bean that is “free” for microbial growth or chemical reaction. Relevant post-roast for storage stability.

### 4.1 Declared Parameters — Weight Loss (Roast-Degree Anchored)

Kimi provided a finer eight-bucket classification than the three-bucket light/medium/dark scheme. This dossier adopts Kimi’s classification because it aligns with practitioner terminology and provides more usable granularity.

|Roast level             |Weight loss|Typical value|Composition                  |Status     |
|------------------------|-----------|-------------|-----------------------------|-----------|
|Green (unroasted)       |0%         |—            |Baseline                     |FROZEN     |
|City- (very light)      |10–11%     |~10.3%       |Mostly moisture              |PROVISIONAL|
|City (light)            |11–13%     |~12%         |Moisture + early organic loss|PROVISIONAL|
|City+ (light-medium)    |12–14%     |~13%         |Increasing organic loss      |PROVISIONAL|
|Full City (medium)      |14–15%     |~14.5%       |Balanced moisture/organic    |PROVISIONAL|
|Full City+ (medium-dark)|15–16%     |~15%         |Significant organic loss     |PROVISIONAL|
|French (dark)           |15–17%     |~15.6%       |Heavy organic loss           |PROVISIONAL|
|Italian / very dark     |16–20+%    |~16.6%+      |Extreme organic loss         |PROVISIONAL|

**On the bucket counts.** The three-bucket scheme (light 11–13%, medium 14–16%, dark 17–20%) used by GPT and the task-card placeholder is a simplification of the eight-bucket scheme above. Both are valid at different levels of resolution. For curation purposes, the eight-bucket scheme is kept here for granularity and the three-bucket scheme is implicit by grouping (City/City- = light, City+ through Full City+ = medium, French/Italian = dark).

### 4.2 Declared Parameters — Volume, Density, Porosity

|Parameter                |Green  |Light  |Medium |Dark      |Status     |
|-------------------------|-------|-------|-------|----------|-----------|
|Volume increase          |0%     |50–70% |70–90% |90–100%+  |PROVISIONAL|
|Bulk density decrease    |0%     |20–30% |30–40% |40–50%    |PROVISIONAL|
|Apparent density decrease|0%     |15–25% |25–35% |35–45%    |PROVISIONAL|
|Porosity (total)         |~20–30%|~35–45%|~45–55%|Up to ~60%|PROVISIONAL|

**Porosity source note.** The ~60% dark-roast porosity figure is anchored by Kimi to a 2025 *Journal of Food Engineering* paper (doi:10.1016/j.jfoodeng.2024.112726). The porosity measurements in that study used a pilot-scale spouted bed roaster. Drum roaster porosity may differ; the figure should be treated as PROVISIONAL until cross-checked against drum-roaster data.

### 4.3 Colour Measurement

|System           |Technology               |Scale          |Typical working range |Status                                |
|-----------------|-------------------------|---------------|----------------------|--------------------------------------|
|Agtron Gourmet   |Near-infrared reflectance|0–100+         |25–95 (lower = darker)|FROZEN (industry standard)            |
|Agtron Commercial|Near-infrared reflectance|Different scale|—                     |FROZEN                                |
|ColorTrack       |Laser reflectometry      |Proprietary    |—                     |PROVISIONAL                           |
|Probat Colorette |Tristimulus CIELAB L*    |L* value       |—                     |PROVISIONAL                           |
|Tonino           |Visible spectroscopy     |Proprietary    |—                     |PROVISIONAL (portable consumer device)|

### Agtron-to-Roast-Degree Mapping

|Agtron range (Gourmet)|Roast level               |Description                 |
|----------------------|--------------------------|----------------------------|
|80–100                |Very light (City-, Nordic)|High acidity, origin-forward|
|70–80                 |Light (City)              |Specialty light roast       |
|55–70                 |Medium-light (City+)      |Balanced, origin-forward    |
|45–55                 |Medium (Full City)        |Classic specialty           |
|35–45                 |Medium-dark (Full City+)  |Full body, caramel notes    |
|25–35                 |Dark (Vienna/French)      |Bold, smoky, reduced origin |
|<25                   |Very dark (Italian)       |Charred, burnt notes        |

**Surface vs internal colour.** Agtron measures surface colour, which may not perfectly match the bean’s internal degree of roast. The surface-internal gap is itself a measurable parameter and has been correlated with development phase characteristics — a bean roasted very fast may have a dark surface and a lighter core, while a bean roasted more slowly may be more uniform. For roast control, bean probe temperature remains a complementary signal. The Q-grader workflow uses ground Agtron (which mixes surface and interior) as its primary anchor.

### 4.4 Moisture Content Post-Roast

|Roast level|Moisture content|Notes                                   |Status     |
|-----------|----------------|----------------------------------------|-----------|
|Green      |8–12%           |Initial state (per BEANS-COAST-001 §4.1)|FROZEN     |
|Light      |3–4%            |Significant retention                   |PROVISIONAL|
|Medium     |2–3%            |Typical post-roast                      |PROVISIONAL|
|Dark       |1–2%            |Very dry                                |PROVISIONAL|
|Very dark  |<1%             |Extreme dehydration                     |PROVISIONAL|

Post-roast moisture is context-sensitive: cooling method, ambient humidity, and time-to-packaging all affect the values above. They should be read as typical ranges soon after cooling, not long-term storage values.

### 4.5 CO₂ Content and Degassing

Roasted coffee contains trapped CO₂ generated during roasting. This CO₂ evolves over days to weeks post-roast and constitutes the natural Roast → Brew interface.

|Parameter                      |Value               |Context                    |Status                            |
|-------------------------------|--------------------|---------------------------|----------------------------------|
|CO₂ content post-roast (light) |4–6 mL/g            |Higher retention           |PROVISIONAL                       |
|CO₂ content post-roast (dark)  |6–10 mL/g           |More CO₂ produced          |PROVISIONAL                       |
|First 24 h degassing           |~40% of total CO₂   |Rapid initial release      |PROVISIONAL                       |
|Peak brewing window (pour-over)|5–14 days post-roast|Practitioner consensus     |PROVISIONAL (practitioner)        |
|Peak brewing window (espresso) |7–21 days post-roast|Longer rest needed         |PROVISIONAL (practitioner)        |
|Degassing duration             |Weeks to months     |Continues at declining rate|FROZEN (well-established kinetics)|

**Numerical reconciliation.** GPT reports CO₂ content as “a few mL/g, up to ~10 mL/g” without subdividing by roast degree. Kimi provides the roast-degree split above (4–6 for light, 6–10 for dark). The primary literature (Smrke 2018, Anderson 2003, Wang 2014) supports degassing kinetics as FROZEN but leaves specific content values as ranges. This dossier adopts Kimi’s finer granularity as PROVISIONAL pending primary-source verification.

**Production-vs-retention tension.** The table above pairs higher CO₂ content with darker roasts, but there is a structural tension worth acknowledging: dark roasts have *higher* porosity and more developed fracture networks (§4.2 and §4.6), which would predict *faster* CO₂ escape and therefore *lower* steady-state retention, not higher. The reported numbers can be reconciled in two ways. First, the production rate in dark roasts is high enough that even with faster escape the remaining retained fraction at any given time post-cooling exceeds that of a light roast. Second, the values reported in the literature are typically measured soon after cooling (hours to a day), when the production advantage has not yet been overtaken by the escape disadvantage. Over longer time windows — days to weeks post-roast — a dark roast’s degassing curve typically falls below a light roast’s on a per-gram basis, because the same structural features that allow oil migration (§4.6) also allow faster gas loss. A careful reading of the table is that “CO₂ content post-roast (dark) 6–10 mL/g” refers to the early retention, not to steady-state retention, and the crossover between light-roast and dark-roast retention happens somewhere in the first few days. This tension is one of the things that makes the fixed “peak brewing window” heuristic imprecise: the production and escape curves are both roast-degree-dependent and they cross at a time that itself depends on roast degree.

### 4.6 Transport & Emergence — The Oil Migration Model

*This subsection formalises the oil migration phenomenon introduced in the dossier opening. It converts a qualitative description into a predictive scaffold with a named dimensionless criterion and a percolation framing. The formalisation is intended as a testable hypothesis, not a validated model — at present it functions as a structural organising device for the §3, §4, and §5 evidence, and as a research programme.*

**The phenomenon to be explained.** Green and light-roasted beans have dry, matte surfaces. Dark-roasted beans, past a threshold, develop visible surface oil. The transition is often observed as threshold-like rather than smoothly continuous: batches below the threshold look dry; batches a little past it look glossy. The bulk lipid fraction is largely unchanged across the transition (triglycerides are heat-stable at roasting temperatures; see §3.2). What changes is *where* the lipid is located and whether the bean’s internal structure supports outward transport.

**The driving forces and constraints.** Three mechanisms drive lipid motion from the bean interior toward the surface:

1. **Pressure gradient.** CO₂ generated during roasting and water vapour from residual moisture create a positive internal pressure relative to ambient. The pressure is roast-degree-dependent: more CO₂ is generated at darker roast levels, and retention is sustained by the (still evolving) cellular matrix. Estimated magnitude: a few atmospheres of transient internal pressure is consistent with reported degassing kinetics (Anderson 2003; Wang 2014; Smrke 2018), though direct measurement inside a bean during and immediately after roasting is difficult.
1. **Capillary flow.** Once a fracture network is partially established, surface tension of the lipid phase against the cellular matrix drives capillary transport along connected channels. This is a weaker driving force than the pressure gradient but operates over longer timescales (hours to days post-roast).
1. **Viscosity drop with temperature.** Lipid viscosity falls sharply with temperature. A lipid mixture that is nearly immobile at 25 °C is fluid at 200 °C. As the roast progresses, the lipid phase becomes progressively more mobile; as cooling proceeds, mobility drops again but not to zero.

The transport is constrained by two structural properties:

- **Permeability** of the fracture network. A bean with many small, isolated internal voids has low effective permeability. A bean with fewer but larger, connected voids has higher effective permeability.
- **Connectivity threshold**. Below a critical fracture density, voids remain isolated and no macroscopic transport pathway exists. Above it, a continuous path from interior to surface becomes available.

**A minimal dimensionless criterion.** Following standard transport-process reasoning, the propensity for lipid migration can be captured in a single dimensionless ratio:

> Π_oil ∼ (k · ΔP) / μ(T)

where:

|Symbol  |Meaning                                            |Determined by                                                                 |
|--------|---------------------------------------------------|------------------------------------------------------------------------------|
|**k**   |Effective permeability of the fracture network (m²)|Structural state (§4.2 porosity, §7 BR-05 surface–internal gap)               |
|**ΔP**  |Internal–external pressure difference (Pa)         |CO₂ + vapour generation minus escape (§4.5 CO₂ content and degassing kinetics)|
|**μ(T)**|Temperature-dependent lipid viscosity (Pa·s)       |§2 temperature trajectory and post-roast cooling rate                         |

Π_oil is high when permeability is large, internal pressure is large, and viscosity is low. It is small when any of the three is small.

**Percolation threshold.** The observed threshold-like transition from dry to oily beans is consistent with a **percolation transition** in the fracture network. Below a critical fracture density (or equivalently, below a critical effective porosity for a given geometry), the voids remain disconnected and the effective permeability k is near zero regardless of ΔP and μ. Above the threshold, a spanning cluster of connected fractures forms, k jumps discontinuously, and lipid transport from interior to surface becomes possible.

**Working hypothesis.** Surface oil becomes visible when Π_oil exceeds a threshold set by fracture percolation — that is, when the structural state crosses the percolation transition *and* ΔP and μ(T) favour transport. This predicts that:

- Dark roasts (high porosity, past second crack) cross the percolation threshold and develop surface oil.
- Fast roasts that reach dark-roast colour without developing the same porosity and fracture density may stay below the threshold and remain drier than a slow dark roast to the same colour — a discriminant observable for the state degeneracy described in §0.2.
- Post-roast oil appearance over days is explained by continued capillary transport at lower temperatures, where Π_oil has dropped but remains positive.
- Storage oil migration rate should correlate with time-integrated post-roast temperature and with initial fracture density at drop.

**Status of the model.** PROVISIONAL — this is a scaffold, not a validated transport model. The quantitative values of k, ΔP, and μ(T) for roasting coffee beans are not well characterised in the open literature. What the scaffold provides is:

- a structural explanation for the threshold-like nature of the dry-to-oily transition (percolation, not gradual gradient),
- a testable prediction (state-degeneracy discriminant via fracture density at matched Agtron),
- a cross-section linkage connecting §3 (lipid stability), §4 (porosity), and §5 (degassing and volatile loss) through a single framework,
- a formal definition of where measurement is needed to close the gap between qualitative narrative and predictive structure.

**Connection to the anti-claims register.** RAC-11 (“oily beans contain more oil”) is now explicitly grounded: the claim is compositionally false and the actual mechanism is structural. See §6.

**Connection to the open questions register.** The quantitative closure of this model is tracked as a new open question **BR-07** in §7 (percolation threshold parameterisation, permeability measurement in roasted coffee, in-bean pressure measurement during and after roast).

### 4.7 Cooling Phase

|Parameter                             |Value                                    |Context                                            |Status                                              |
|--------------------------------------|-----------------------------------------|---------------------------------------------------|----------------------------------------------------|
|Tray cooling time (small batch ≤15 kg)|<4 minutes to near-ambient               |Typical shop roaster, forced air                   |FROZEN (Perplexity, Kimi concordant; GPT consistent)|
|Tray cooling time (production)        |4–8 minutes                              |Larger batches                                     |PROVISIONAL                                         |
|Water quench                          |Rare in specialty; industrial only       |Avoided in specialty for flavour reasons           |FROZEN                                              |
|Forced air cooling effect             |Better volatile retention vs slow cooling|Mechanistically plausible; controlled evidence thin|PROVISIONAL                                         |

**Cooling rate and volatile retention.** GPT, Kimi, and Perplexity all flag that rapid cooling plausibly preserves more volatiles than slow cooling by cutting continued reactions and volatile escape short. The mechanism is established; the quantitative cooling-rate-vs-volatile-retention curve is thinly studied. No controlled experiments isolate cooling rate as the only variable. This is a genuine research gap.

### 4.8 Validity Contract

- Weight-loss percentages must specify the measurement basis: green mass to roasted mass, species, roast degree, and whether water quenching was used.
- Colour values require controlled timing after roast and consistent sample preparation. Cropster documentation notes that roast colour continues to change during the first hours after roast.
- Whole-bean and ground Agtron values are not directly interchangeable; cross-measurement requires noting which was used.
- Bulk density and apparent (true) density are distinct quantities. Density claims without method specification are not cross-comparable. BEANS-COAST-001 §4.3 flags the same distinction for green beans.
- Porosity measurements depend strongly on method (micro-CT, pycnometry, mercury porosimetry, gas adsorption); cross-study numerical comparison is difficult.
- CO₂ content must distinguish in-roaster evolution, cooling-tray loss, and post-packaging degassing. The numbers above refer to immediate post-cooling retention.

### 4.9 Open Disputes

- **Exact weight-loss bins.** The eight-bucket scheme is more granular than the three-bucket scheme but boundaries between adjacent buckets are fuzzy. Some studies on Robusta report broader values. PROVISIONAL across the board.
- **CO₂ content range.** GPT reports “a few mL/g, up to ~10 mL/g” as a single range; Kimi subdivides by roast degree. The primary literature supports the kinetics but leaves absolute values bounded rather than fixed.
- **Cooling rate effects on cup quality.** Practitioner consensus says rapid cooling matters; controlled experimental evidence is thin.
- **Optimal resting period.** RAC-09. Light roasts may benefit from longer rest (10–14+ days); dark roasts peak earlier (2–5 days) and stale faster; the universal 7–14 day claim is too coarse.

### 4.10 Downstream Interface

CO₂ content, moisture, and cooling-rate-induced volatile retention are all Roast → Brew interface properties. They are documented more fully in Interface Sheet I-2. Porosity and fracture structure affect grinding behaviour and extraction, which are Brew-side concerns.

-----

## 5 — Aromatic Outcomes

### Key terms used in this section

- **Volatile compound:** A compound with sufficient vapour pressure at room or brewing temperature to reach the nose and contribute to aroma. Roasted coffee contains approximately 800–1,000 identified volatile compounds.
- **Non-volatile precursor:** A compound present in the green bean that does not itself smell or taste like coffee but is transformed during roasting into volatile aromatics. Defined in BEANS-COAST-001 §5.
- **Key odorant:** A volatile compound whose concentration exceeds its odour threshold by enough to measurably contribute to the perceived aroma. Approximately 30 compounds carry most of the sensory load.
- **Odour activity value (OAV):** A compound’s concentration divided by its odour threshold. OAV > 1 means the compound is above threshold and potentially perceptible.
- **GC-MS:** Gas chromatography–mass spectrometry. The reference method for identifying and quantifying volatile compounds.
- **GC-O:** Gas chromatography–olfactometry. GC coupled with a human nose at the detector, used to identify which compounds are odour-active.

### 5.1 Declared Parameters — Volatile Compound Classes

|Class               |Approximate count|Key aroma contribution     |Main precursor pathway                   |Roast-degree dominance|Status     |
|--------------------|-----------------|---------------------------|-----------------------------------------|----------------------|-----------|
|Furans              |~100+            |Caramel, sweet, burnt sugar|Sugars (Maillard, caramelisation)        |Medium                |FROZEN     |
|Pyrazines           |~80+             |Nutty, roasted, earthy     |Sugars + amino acids (Maillard, Strecker)|Medium                |FROZEN     |
|Pyrroles            |~50+             |Nutty, caramel, smoky      |Sugars, trigonelline                     |Medium-dark           |FROZEN     |
|Pyridines           |~30+             |Bitter, burnt, coffee-like |Trigonelline degradation                 |Medium-dark           |FROZEN     |
|Ketones             |~60+             |Fruity, buttery, musty     |Lipid oxidation, Maillard                |Medium                |FROZEN     |
|Aldehydes           |~70+             |Fruity, grassy, malty      |Lipid oxidation, Strecker degradation    |Light-medium          |FROZEN     |
|Phenols             |~40+             |Smoky, spicy, medicinal    |CGA degradation                          |Medium-dark           |FROZEN     |
|Sulfur compounds    |~30+             |Roasted, meaty, sulfurous  |Sulfur amino acids                       |Medium                |FROZEN     |
|Esters              |~25+             |Fruity, floral             |Various                                  |Variable              |PROVISIONAL|
|**Total identified**|**~800–1,000**   |                           |                                         |                      |FROZEN     |

**Note on the ~800–1,000 figure.** GPT and Kimi both flag this as a review-level statement rather than a fixed census. The exact number depends on which analytical methods are used (GC-MS, GC-MS with different column chemistries, SPME, SIFT-MS, two-dimensional GC) and whether the corpus covers multiple roasters, origins, and roast degrees. The figure should be read as “class-level stable” rather than as a precise compound count.

### 5.2 Key Aroma Compounds

Kimi and GPT concordantly identify the following compounds as among the key odorants — those with the highest odour activity values, such that their concentration reliably exceeds their odour threshold. This is not an exhaustive list (the full key-odorant set is closer to 30 compounds depending on analytical method and matrix) but covers the most frequently cited.

|Compound                        |Class            |Aroma descriptor            |Precursor pathway                          |Roast-degree dominance  |Status     |
|--------------------------------|-----------------|----------------------------|-------------------------------------------|------------------------|-----------|
|2-furfurylthiol                 |Sulfur compound  |Roasted coffee, sulfurous   |Cysteine + furans                          |Medium-high             |FROZEN     |
|Methional                       |Sulfur aldehyde  |Potato, savoury, broth      |Methionine (Strecker)                      |Light-medium            |FROZEN     |
|β-damascenone                   |Ionone derivative|Fruity, floral, apple       |Carotenoid degradation                     |Light-medium            |FROZEN     |
|2,3-butanedione (diacetyl)      |Diketone         |Buttery, caramel            |Sugar degradation                          |Medium                  |FROZEN     |
|2,3-pentanedione                |Diketone         |Buttery, fruity             |Sugar degradation                          |Medium                  |FROZEN     |
|4-vinylguaiacol                 |Phenol           |Spicy, clove, smoky         |Ferulic acid (CGA)                         |Medium-dark             |FROZEN     |
|Guaiacol                        |Phenol           |Smoky, phenolic             |CGA degradation                            |Dark                    |FROZEN     |
|2-ethyl-3-methylpyrazine        |Pyrazine         |Nutty, roasted, earthy      |Maillard                                   |Medium                  |FROZEN     |
|2,5-dimethylpyrazine            |Pyrazine         |Roasted, nutty, earthy      |Maillard                                   |Medium                  |FROZEN     |
|3-mercapto-3-methylbutyl formate|Sulfur compound  |Catty, blackcurrant         |Cysteine-derived                           |Variable                |PROVISIONAL|
|Linalool                        |Terpenoid        |Floral, citrus              |Terpenoid origin (survives from green bean)|Light (origin-dependent)|PROVISIONAL|
|Maltol                          |Furanone         |Sweet, caramel, cotton candy|Sugar degradation                          |Medium                  |PROVISIONAL|

### 5.3 Precursor-to-Volatile Mapping — The Central Open Question

This is the pivotal content of the Roast dossier and the direct successor to BW-04 in the Beans dossier. The mapping is well-established *qualitatively* — the table below shows the main established pathways — but is only partially closed *quantitatively*.

|Precursor class                          |Green-bean concentration         |Volatile products                                                     |Pathway                                |Yield data                                  |Status      |
|-----------------------------------------|---------------------------------|----------------------------------------------------------------------|---------------------------------------|--------------------------------------------|------------|
|Sucrose                                  |5–9% (Arabica); 0.9–5% (Robusta) |Furans, pyrazines, aldehydes, ketones                                 |Maillard, caramelisation, fragmentation|Mass balance not closed                     |OPEN (BR-04)|
|Free amino acids                         |0.3–3%                           |Pyrazines, sulfur compounds, Strecker aldehydes                       |Maillard, Strecker degradation         |Partial via in-bean experiments (Mayer 2009)|OPEN (BR-04)|
|Chlorogenic acids                        |3.5–14% (total)                  |Phenols (guaiacol, 4-vinylguaiacol), lactones, quinic-acid derivatives|Thermal degradation                    |Partial                                     |OPEN (BR-04)|
|Trigonelline                             |0.8–1.3%                         |Pyridines, pyrroles, nicotinic acid                                   |Thermal decomposition                  |Partial (Varga 2002 on model systems)       |OPEN (BR-04)|
|Lipids                                   |13–17% (Arabica); 7–11% (Robusta)|Aldehydes, ketones, alcohols                                          |Oxidation, hydrolysis                  |Weak                                        |OPEN (BR-04)|
|Carotenoids                              |Trace (not in Beans §5.1)        |β-damascenone, ionone derivatives                                     |Thermal degradation                    |Weak                                        |OPEN (BR-04)|
|Sulfur amino acids (cysteine, methionine)|Subset of amino acid pool        |2-furfurylthiol, methional, sulfur compounds                          |Maillard with in-bean experiments      |Mayer 2009 provides strongest evidence      |PROVISIONAL |

**What is known, what is open.** Qualitative pathway assignments are established: sugars + amino acids drive the Maillard/Strecker chemistry that produces most of the volatile nitrogen and sulfur compounds; CGAs drive phenolic pathways; lipids drive oxidative aldehyde and ketone formation; trigonelline drives pyridine/pyrrole formation; carotenoids drive ionone chemistry. **What is not known quantitatively** is what fraction of a given precursor becomes a given volatile under a defined roast endpoint. Mayer et al. 2009 (in-bean spiking experiments) provides the strongest evidence for specific precursor-to-volatile links for furfurylthiol, pyrazines, and diketones, but comprehensive yield mapping remains a genuine research gap rather than a curation gap.

This is tracked as **BR-04** in §7, inheriting directly from BW-04 in BEANS-COAST-001.

### 5.4 Volatile Profile by Roast Degree

**A distributional view.** The table below shows how the relative weighting of major volatile classes shifts across roast degrees. The honest reading is that *all classes are present at all roast levels* (once past the drying phase) and that what changes is their *relative proportions* — not which class is “dominant” in an on/off sense. A better mental model than “one class per roast” is a mixture distribution over overlapping compound classes, with the mixture weights drifting continuously as the roast progresses. The words “most weighted” in the table below should be read as “class with the highest relative contribution at this endpoint,” not as “the only class present.”

|Roast level (Agtron Gourmet)|Most heavily weighted classes                         |Character aroma notes                 |Status     |
|----------------------------|------------------------------------------------------|--------------------------------------|-----------|
|Very light (RL 80+)         |Aldehydes, terpenoids, early furans                   |Fruity, floral, grassy, origin-forward|PROVISIONAL|
|Light (RL 70–80)            |Furans, early pyrazines, residual terpenoids          |Fruity, nutty, light caramel          |PROVISIONAL|
|Medium (RL 45–55)           |Pyrazines, furans, diketones                          |Caramel, toasted, nutty, balanced     |PROVISIONAL|
|Medium-dark (RL 35–45)      |Pyrazines and phenols co-weighted, pyrroles increasing|Chocolate, spice, smoky notes emerging|PROVISIONAL|
|Dark (RL 25–35)             |Phenols, pyrroles, sulfur compounds                   |Smoky, bitter, burnt, reduced origin  |PROVISIONAL|
|Very dark (RL <25)          |Phenols, pyridines, pyrolysis products                |Harsh, burnt, acrid                   |PROVISIONAL|

**Why the table is not FROZEN anywhere.** The earlier version of this table (v0.2.0) marked the medium row as FROZEN based on concordant GPT and Kimi agent reports. On reflection, this was inconsistent with the distributional framing: if the claim is “these classes are most heavily weighted,” the claim is a statement about a continuous shifting of relative proportions, not a discrete categorical assignment that can be FROZEN. All rows are now PROVISIONAL to reflect the continuous nature of the underlying shift. The *qualitative* statement that pyrazines and furans are heavily weighted in medium roasts is robust and concordantly supported; the *discrete-category* statement was an over-simplification the table layout encouraged.

**The simplified one-class-per-roast framing is too crude** — and even the “most heavily weighted” framing above is a compression. The actual transition is continuous: as the trajectory moves through the state space described in §0.2, precursor pools are consumed at different rates, new compounds form at different rates, and the volatile distribution shifts accordingly. Any snapshot of “what dominates” at a given Agtron reading is a projection of that continuously shifting distribution onto a categorical label.

### 5.5 Cooling-Tray Chemistry and Volatile Loss

The cooling tray is brief but not chemically inert. Volatiles continue to escape, oxidation continues, and the bean’s chemistry is not frozen until it reaches ambient temperature.

|Parameter                                        |Value                                     |Status                                             |
|-------------------------------------------------|------------------------------------------|---------------------------------------------------|
|Initial volatile loss (first 24 hours post-roast)|20–40% of total aromatics (rough estimate)|WEAK (practitioner estimate; not directly measured)|
|Most affected compounds                          |Low molecular weight, high volatility     |PROVISIONAL                                        |
|Better retained compounds                        |Higher molecular weight, more polar       |PROVISIONAL                                        |
|Optimal brewing window                           |5–14 days post-roast (highly variable)    |PROVISIONAL (practitioner)                         |

### 5.6 Sensory Linkage — Strict Evidence Floor

Per TC-ROAST-001 v1.1 §5.5, this section reports compound-to-cup-attribute links only where peer-reviewed work has experimentally tied GC-MS-or-equivalent compound measurements to cup-score attributes under controlled conditions. Cupping competition results, flavour wheel mappings, and roaster blog correlations do not satisfy this bar.

**Material currently passing the evidence floor.** Mayer et al. 2009 in-bean experiments provide the strongest precursor-to-volatile links for 2-furfurylthiol, pyrazines, and diketones. Obando et al. 2024 (PMC 11477549) provides roast-degree-dependent development curves for several key aroma compounds. Pajuelo-Muñoz et al. 2026 tracks aromatic volatile biomarkers through the roasting process. Vezzulli et al. 2023 compares volatile compounds in green and roasted Arabica specialty coffee.

**Material explicitly excluded.** Flavour wheel mappings, cupping competition descriptor correlations, marketing-literature claims about specific origin flavours tied to specific compounds, and any “this compound causes this flavour” statement without controlled concentration–sensory pairing.

### 5.7 Validity Contract

- Review statements about 800–1,000 volatiles are safe at class level, not as a fixed census.
- Aroma-impact claims require odour-threshold context (odour activity value); abundance alone is insufficient.
- Precursor → volatile mapping is strongest where isotope labelling or in-bean spiking experiments were performed, weakest where authors infer pathways only from correlation.
- Cooling-tray and early post-drop volatile losses should be separated from long-term package degassing wherever possible.
- Aroma descriptors from sensory panels are valid only when the panel was trained and the protocol was controlled; transferred descriptors from other food matrices are not valid for coffee without coffee-specific validation.

### 5.8 Open Disputes

- **Which exact compounds belong to the top ~30 key odorants.** The broad principle is robust; different analytical methods and sensory panels prioritise different compounds.
- **Roast-degree dominance by class.** Reviews broadly agree on the shifting pattern; simplified one-class-per-roast statements are too crude.
- **Quantitative precursor yield.** Strongly underdetermined in the open literature. Often inferred, rarely closed by mass balance. This is BR-04. Its formation-side complement (melanoidin and polymer sink fractions) is tracked as BR-06.
- **Cooling phase chemistry.** How much chemistry continues during cooling is under-studied. Rapid vs slow cooling may produce measurably different aromatic outcomes but is not well-quantified.

### 5.9 Downstream Interface

The volatile compound profile at the moment the bean leaves the cooling tray is the starting state for the Brew dossier. Volatile loss continues during storage (Interface Sheet I-2), during grinding, and during brewing itself. By the time the coffee reaches the cup, the volatile profile has been modified by at least three stages of transformation beyond what this dossier describes.

-----

## 6 — Anti-Claims Register

*The register distinguishes two types of problematic claim. **Type A** claims make a causal or factual assertion that the evidence does not support. **Type B** claims are market or evaluative language whose meaning depends on the metric of “quality” being used. Both types appear frequently in coffee discourse, but they require different responses.*

### Type A — Unsupported causal or factual claims

|ID    |The claim                                             |Why it is problematic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |Status                    |Evidence source                                |
|------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------|
|RAC-01|“Light roasts are higher in caffeine than dark roasts”|Caffeine is highly heat-stable (melting point 238 °C); HPLC data (PMC 11586412) shows minimal degradation. Apparent concentration differences arise from weight-loss effects and dosing-by-volume vs dosing-by-mass conventions.                                                                                                                                                                                                                                                                                                                                                                                                                                   |ACTIVE — EVIDENCE CONTRARY|Kimi, GPT (concordant)                         |
|RAC-02|“Dark roasts are less acidic”                         |Conflates multiple definitions of acidity. Titratable acidity, pH, and sensory brightness do not move identically with roast degree. Some acids (CGA-derived) do decrease; others form; perceived acidity does not track chemical acidity linearly.                                                                                                                                                                                                                                                                                                                                                                                                                |ACTIVE                    |Kimi, GPT                                      |
|RAC-05|“Air roasters produce cleaner cups than drum roasters”|Equipment-vs-cup claims are systematically confounded by operator skill, profile design, and bean origin. No controlled study isolates equipment type as the sole variable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |ACTIVE                    |Perplexity, Kimi, GPT (concordant)             |
|RAC-06|“First crack always occurs at 196 °C”                 |Probe-dependent and roaster-dependent. Variation of ±10–20 °C across machines is normal. First crack is defined by the audible event, not the temperature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |ACTIVE — EVIDENCE CONTRARY|Perplexity, Kimi, GPT (concordant)             |
|RAC-08|“Slow roasts are baked, fast roasts are scorched”     |Useful heuristic but oversimplified. Total time alone does not determine quality; the interaction of RoR, phase ratios, and maximum surface temperatures matters more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |ACTIVE                    |GPT, Kimi                                      |
|RAC-10|“Roasting destroys nutritional value”                 |Overbroad. Roasting degrades some compounds (partial CGA and trigonelline loss) but also forms others (melanoidins, nicotinic acid from trigonelline). The blanket claim does not hold.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |ACTIVE                    |GPT, Kimi (concordant)                         |
|RAC-11|“Oily beans contain more oil”                         |Compositional misreading of a structural phenomenon. The bulk lipid fraction of a roasted bean is essentially the same as the green bean (triglycerides are heat-stable at roasting temperatures). Surface oil on dark-roasted beans is the result of internal oil *migrating* to the surface along a connected fracture network, not of additional oil being created. A dry-looking light roast and an oily-looking dark roast from the same green coffee typically contain the same total lipid mass; the difference is where that lipid is located and whether it has reached a percolation threshold in the fracture network. See §4.6 for the transport model.|ACTIVE — EVIDENCE CONTRARY|GPT (bulk lipid stability); structural analysis|

### Type B — Market language and evaluative framing

|ID    |The claim                                                            |Why it is problematic                                                                                                                                                                                                                                                                    |Status|Evidence source       |
|------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|----------------------|
|RAC-03|“Development time ratio of 20–25% is optimal”                        |Widely cited practitioner heuristic (Scott Rao, 2014). No peer-reviewed controlled study establishes 20–25% as an optimum. Working roasters report good results across a much wider range (12–30%). “Optimal” is evaluative without a specified goal.                                    |ACTIVE|GPT, Kimi (concordant)|
|RAC-04|“Crash and flick must be avoided”                                    |Strong practitioner consensus (Scott Rao school). The empirical link to cup outcomes is contested. Mild crash-and-flick patterns may have minimal cup impact when overall development time and end temperature are appropriate.                                                          |ACTIVE|GPT, Kimi             |
|RAC-07|“Nordic-style roasting preserves more origin character”              |Conflates a roast-degree range with a sensory category. “Origin character” is an evaluative term without a fixed operational definition. Partly market-driven positioning. Light roasts do preserve different volatile profiles, but “more origin character” requires sensory validation.|ACTIVE|Kimi, GPT             |
|RAC-09|“Roasted coffee improves for 7–14 days post-roast (degassing window)”|Practitioner consensus with significant individual variation. Optimal window varies by roast degree (light longer, dark shorter), brew method (espresso 7–21 days, pour-over 5–14 days), and bean characteristics. “Improves” is evaluative.                                             |ACTIVE|GPT, Kimi, Perplexity |

-----

## 7 — Open Questions

*These are questions raised during curation that could not be fully answered from the agent returns. Five have been assigned formal tracking numbers for future investigation.*

|ID   |Question                                                                                                                                                                                                                                                                                                          |Tracking number|Status|Current best answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|BR-01|What fraction of a drum roaster’s heat transfer is actually convective, and how does it vary with airflow, charge temperature, and roast degree?                                                                                                                                                                  |CL-2026-019    |OPEN  |Qualitative: modern indirect-flame drums with forced airflow are convection-weighted; legacy solid drums without forced airflow are closer to conduction-dominant. Quantitative: specific fractions that circulate in engineering literature do not survive as stable numbers — heat transfer varies dynamically during the roast and across machines. No comprehensive peer-reviewed measurement exists.                                                                                                                                                                     |
|BR-02|Can development time ratio be experimentally tied to measurable cup outcomes under controlled conditions?                                                                                                                                                                                                         |CL-2026-020    |OPEN  |RAC-03 is ACTIVE because no such study exists. Practitioner claims cluster around 20–25%; working roasters succeed across 12–30%. A controlled study matching green coffee, equipment, and profile except for DTR would resolve it.                                                                                                                                                                                                                                                                                                                                           |
|BR-03|How does cooling rate affect volatile retention and continued reactions in the bean?                                                                                                                                                                                                                              |CL-2026-021    |OPEN  |Mechanism is plausible and widely asserted by practitioners. Quantitative comparative evidence is thin. Controlled studies isolating cooling rate as the only variable are needed.                                                                                                                                                                                                                                                                                                                                                                                            |
|BR-04|Can specific green-bean precursors be mapped to specific roasted-coffee volatiles with quantitative yield data?                                                                                                                                                                                                   |CL-2026-022    |OPEN  |Inherited from BEANS-COAST-001 BW-04. Qualitative pathways are established (sugars + amino acids → Maillard/Strecker products; CGAs → phenols; trigonelline → pyridines/pyrroles; lipids → aldehydes and ketones; carotenoids → ionone derivatives). Mayer et al. 2009 provides the strongest in-bean experimental evidence for specific links. Comprehensive yield mapping remains a genuine research gap.                                                                                                                                                                   |
|BR-05|What is the actual surface vs internal roast degree gap in drum vs fluid-bed roasters, and how does it affect grinding and extraction?                                                                                                                                                                            |CL-2026-023    |OPEN  |Widely observed; poorly quantified. Agtron measurements of ground vs whole-bean samples provide a partial proxy but do not fully resolve the question.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|BR-06|What fraction of each precursor pool ends up in the melanoidin / brown polymer sink at a defined roast endpoint, and what is the full precursor → volatile + polymer + gas mass balance?                                                                                                                          |CL-2026-024    |OPEN  |Complement to BR-04. The degradation side is reasonably well quantified; the formation side splits between volatiles (partially mapped, BR-04) and polymers (essentially unmapped). The full mass balance across the roast is not closed in the published literature.                                                                                                                                                                                                                                                                                                         |
|BR-07|Can the oil migration / Π_oil transport model (§4.6) be closed quantitatively? Specifically: what is the percolation threshold for the fracture network in roasting coffee, what are typical effective permeabilities k in roasted beans, and what is the internal pressure ΔP during and immediately after roast?|CL-2026-025    |OPEN  |Introduced in v0.3.1 as the formal successor to the qualitative “surface oil migration” dispute in §3.6. The three required measurements (k, ΔP, μ(T) for coffee lipids) are individually tractable with existing methods (micro-CT for fracture network topology, pressure sensors for in-bean ΔP, standard rheometry for lipid viscosity at temperature) but have not been performed jointly for coffee. Closure of this model would also resolve RAC-11 (oily beans contain more oil) from a qualitative anti-claim to a quantitatively demonstrated structural phenomenon.|

-----

## 8 — Source Authority Hierarchy

|Priority   |Type of source                          |Examples (from this curation)                                                                                                                                                      |
|-----------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|1 (highest)|Peer-reviewed scientific papers         |Alcantara 2025; Bolka 2020; Grassi 2023; Mayer 2009; Obando 2024; Pajuelo-Muñoz 2026; Vezzulli 2023; da Costa 2023; Smrke 2018; Wang 2014; Debona 2024; Debona 2025; Varga 2002    |
|2          |Standards and regulatory bodies         |EU Commission Regulation 2017/2158 (acrylamide); EFSA CONTAM 2015 Opinion; Specialty Coffee Association (SCA); International Organisation for Standardisation (ISO)                |
|3          |Research institutions                   |Coffee Science Foundation; World Coffee Research; CIRAD; American Chemical Society educational materials                                                                           |
|4          |Scientific books                        |Flament, *Coffee Flavor Chemistry* (2002); Illy & Viani, *Espresso Coffee* (2005); Rao, *The Coffee Roaster’s Companion* (2014)                                                    |
|5          |Industry practitioners and manufacturers|PROBAT, Loring, Bühler (manufacturer documentation); Cropster, Artisan, RoastLog (software documentation); Barista Hustle, Perfect Daily Grind, Scott Rao, Rob Hoos, Morten Münchow|
|6 (lowest) |Marketing material                      |Flagged as `[MARKETING]`; included only where no better source exists                                                                                                              |

-----

## 9 — Where This Dossier Came From

This dossier was built from raw research notes gathered by external AI research agents under Task Card TC-ROAST-001 v1.1, plus curation work performed during the dossier’s construction. The agents searched different sources and returned notes independently. The results were compared, cross-checked, and merged into this document by the curator operating under Guardian stance.

|Agent           |Files received                                                                                 |Role in this dossier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|GPT-5.4 Thinking|5 (all groups)                                                                                 |Most recent peer-reviewed literature (2023–2026); strongest epistemic discipline on numeric claims; consistent flagging of roast-degree dependence and probe specification issues                                                                                                                                                                                                                                                                                                                       |
|Kimi K2         |5 (all groups, after one re-dispatch — see `ROAST-webapp-scaffold-kimi-20260408-PROVENANCE.md`)|Breadth and granularity on chemistry; 13 named key aroma compounds with pathway assignments; roast-degree-anchored CGA loss table resolving the Beans Interface Sheet I-1 placeholder; eight-bucket weight-loss classification; porosity data anchored to 2025 *J. Food Eng.*                                                                                                                                                                                                                           |
|Perplexity      |1 (equipment only; other four files status unclear)                                            |Manufacturer documentation (PROBAT, Loring, Bühler); convection-weighted drum heat-transfer framing; tighter production-batch range (15–70 kg); instrumentation standard/common/research classification                                                                                                                                                                                                                                                                                                 |
|Claude (curator)|N/A — curation work                                                                            |Task card drafting (TC-ROAST-001 v1.1); dossier skeleton (v0.1.0); populated draft (v0.2.0); first Architect-review integration (v0.3.0); second Architect-review integration with predictive scaffolds (v0.3.1); cross-agent reconciliation; status-marker assignment; anti-claims register assembly; BR-01 through BR-07 tracking-number assignment. The Claude slot was not dispatched as an independent agent return; by Supervisor decision (2026-04-08), the curation work itself fills this slot.|

**Revision history:**

- v0.1.0 (2026-04-08): Skeleton created — empty structure with headings, tables, and placeholders ready to receive agent returns.
- v0.2.0 (2026-04-08): First populated draft. GPT × 5 and Kimi × 5 full intakes merged; Perplexity × 1 equipment intake merged; Kimi Roast web-app scaffold preserved as a side artefact. All five parameter groups populated from reconciliation. Anti-claims register moved from `[PENDING]` to active statuses with evidence sources. BR-01 through BR-05 assigned. Interface Sheet I-1 updated with Kimi’s roast-degree-anchored CGA loss table.
- v0.3.0 (2026-04-08): Architect review integrated. Five priority recommendations executed: (1) new §0.1 Measurement Non-Equivalence subsection formalising the “observed value = physical state ⊗ measurement transfer function” framing with three consequences (BT non-comparability, software-dependent RoR, temporal sampling aliasing); (2) medium-roast anchor reframed as an approximate region in high-dimensional space with explicit state degeneracy at common surface endpoints; (3) new §0.2 Roasting as a Trajectory in State Space subsection naming the coordinates (thermal, mass, structural, chemical, colour) and three structural facts (partial observability, irreversibility, endpoint degeneracy); (4) §3.4 Melanoidins rewritten to name the unclosed mass balance as “unknown-fraction sink” explicitly, new open question BR-06 (CL-2026-024) added as complement to BR-04, cross-link added in §5.8; (5) heat-transfer ~70/30 figure downgraded from structural prominence — §1.1 table cells, §1.6 validity contract, §1.7 open disputes, BR-01 answer, and §9 provenance all updated to reflect the honest statement that no stable global fraction exists. Additional edits: §5.4 volatile-profile table reframed from “dominant classes” to “most heavily weighted classes” with a distributional framing and a note rejecting the earlier FROZEN status on the medium row as inconsistent with the distributional view; Interface Sheet I-2 promoted from descriptive table to state-vector specification (Σ_roast-exit = ⟨A, w, φ, γ, μ, δ, t₀⟩) with explicit notes on what it is and is not and how the Brew dossier should consume it.
- v0.3.1 (2026-04-08): Second Architect review integrated. The first Architect review hardened the dossier structurally; the second pushed it toward framework-level reference with predictive structure. Eight edits: (1) new §4.6 Transport & Emergence subsection formalising oil migration with dimensionless criterion Π_oil ∼ (k · ΔP) / μ(T), percolation threshold framing, and four testable predictions, §§4.6–4.10 renumbered; (2) §2.6 Energy Input upgraded from “absolute data sparse” disclaimer to a qualitative closure scaffold Q_in ≈ Q_evap + Q_chem + Q_loss + Q_storage with a term-by-term table linking §2 to §3 and §4; (3) §2.5 “Endothermic–Exothermic Transition” rewritten as “Apparent Exothermic Behaviour Around First Crack” to soften the phase-transition framing per reviewer’s safer-phrasing suggestion; (4) §0.2 degeneracy claim made falsifiable via three discriminant observables (surface–internal colour gap, CO₂ release curve shape, volatile profile divergence) with an operational statement tying the observables to the experimental programme; (5) §3.4 melanoidin sink given triadic decomposition (precursor loss / volatile formation / polymer sink) and a formal closure-error expression; (6) §3.1 pyrolysis boundary softened from onset to regime language; (7) §4.5 CO₂ production-vs-retention tension acknowledged as a structural inconsistency between higher dark-roast porosity (favouring faster escape) and higher reported dark-roast content (favouring production dominance), with the crossover timing flagged; (8) RAC-11 “oily beans contain more oil” added to Type A anti-claims register, fixing an orphan reference from v0.3.0. Interface Sheet I-2.1 extended with a separate table documenting two extended Σ coordinates (σ = surface oil fraction, ∇T = internal gradient proxy) that are conceptually desirable but currently held outside the minimal vector pending measurement standardisation. New open question BR-07 (CL-2026-025) added: quantitative closure of the oil migration / Π_oil transport model.

-----

## 10 — Conclusion: What the Roast Transforms

*This section is interpretive synthesis, not measured content. It draws conclusions from the parameters and disputes documented in §1–§7. Readers who want only the verified facts should stop at §9.*

The green coffee bean arrives at the roaster as a finished biological object — a hydrated seed with a defined chemical inventory shaped by its genetics, its terroir, and its processing history, as documented in the Beans dossier. Between the moment it enters the roaster and the moment it leaves the cooling tray, it undergoes an irreversible state transformation that is only partially understood. It loses water, then mass. It expands, cracks, and develops a porous internal structure. Its non-volatile precursor compounds are partially consumed and partially transformed into an enormous set of volatile aromatic compounds — roughly a thousand have been identified, a few dozen carry most of the perceived aroma, and the quantitative mapping from precursor to volatile remains an open research question.

Three findings from this curation deserve emphasis.

First, the practitioner-science gap in roasting is wider than in any other coffee domain covered so far. The physics of heat transfer is well established. The chemistry of Maillard and Strecker reactions is well established. But the control heuristics that working roasters use to produce specific cup outcomes — phase ratio targets, development time ratios, rate-of-rise curve shapes, crash-and-flick avoidance — are almost entirely practitioner-derived and have not been experimentally validated in controlled studies. This is not a flaw in the practitioners. It is a statement about what has and has not been funded and published. The dossier preserves the gap rather than pretending it does not exist, flagging practitioner claims with `[PRACTITIONER]` and resisting the temptation to promote craft consensus to scientific consensus.

Second, roast-degree dependence is not a qualifier. It is the constitutive variable of this entire domain. Almost every chemical claim about roasted coffee has to be read with an endpoint attached. “Chlorogenic acids lose about 54% during roasting” is a meaningless statement; “chlorogenic acids lose about 50–60% at Agtron Gourmet 55” is a usable one. The dossier has enforced this discipline throughout, with the §3.8 discipline from the task card carried into the status markers and the reconciliation decisions. The reader should carry it into any downstream use.

Third, the precursor-to-volatile mapping (BR-04, inheriting from BW-04 in the Beans dossier) is the central open question at the Beans/Roast boundary. The qualitative pathways are clear: sugars and amino acids drive the Maillard and Strecker chemistry responsible for most nitrogen- and sulfur-containing odorants; chlorogenic acids drive phenolic pathways; lipids drive aldehyde and ketone formation through oxidation; trigonelline drives pyridine and pyrrole formation; carotenoids drive ionone-family chemistry. What is not clear — and is not available in the open literature as a closed mass balance — is what fraction of any given precursor becomes any given volatile under a defined roast endpoint. Mayer et al. 2009 and a handful of subsequent studies provide partial evidence for specific links, especially for sulfur compounds and pyrazines. But the comprehensive map does not exist. This is a genuine research gap, not a curation failure, and it deserves to be named as such.

This dossier does not claim to be complete. It records the state of knowledge as of April 2026, drawn from three external research agents and the curation work of a fourth. Where sources conflict, the conflict is preserved. Where evidence is weak, it is marked accordingly. Where a claim is practitioner-derived, it is labelled as such. The ten anti-claims in §6 are not editorial positions — they are statements whose evidence was tested and found insufficient. The five open questions in §7 are not failures — they are places where further investigation is the honest response.

The bean enters the roaster green and leaves it transformed. It does not yet know how it will be ground, how it will be brewed, or how it will be drunk. Those belong to later documents — beginning with the Brew dossier, where the central question becomes how the porous matrix of roasted coffee yields its soluble and volatile contents to water. This dossier ends where water meets the bean.

-----

## Interface Sheet I-1 — Precursor Handoff from the Beans Dossier

*This interface sheet records the state of precursor compounds at the moment the green bean enters the roaster, as established by the Beans dossier, and the thermal stability of each compound as roasting proceeds. The Beans side is FROZEN; the Roast side inherits the roast-degree discipline applied throughout this dossier. This version supersedes the placeholder in BEANS-COAST-001 v0.3.2 Appendix A.*

**Important caveat:** All loss percentages in the Roast columns depend strongly on roast degree and on the specific time–temperature profile used. The values below are typical for medium roasts in conventional drum roasters.

|Compound         |Green bean concentration (from BEANS-COAST-001 §5.1)|Light roast loss    |Medium roast loss (Agtron ~55)|Dark roast loss                                  |Roast products                                                                |Status                               |
|-----------------|----------------------------------------------------|--------------------|------------------------------|-------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------|
|Chlorogenic acids|3.5–8.4% (Arabica); 7–14% (Robusta)                 |~30–40%             |~50–60%                       |~80–95%                                          |Phenolic compounds, lactones, quinic/caffeic acid, bitter degradation products|PROVISIONAL                          |
|Trigonelline     |0.8–1.3% (Arabica); 0.6–1.0% (Robusta)              |Partial             |Substantial                   |Extensive                                        |Nicotinic acid (vitamin B3), pyridines, pyrroles, aromatic heterocycles       |PROVISIONAL                          |
|Caffeine         |0.8–1.7% (Arabica); 1.7–4.0% (Robusta)              |<2% loss            |<3% loss                      |<5% loss                                         |Unchanged; survives roasting almost intact                                    |FROZEN                               |
|Sucrose          |5–9% (Arabica); 0.9–5% (Robusta)                    |~50–70% loss        |Near-complete                 |Complete                                         |Reducing sugars → Maillard products + caramelisation products                 |FROZEN                               |
|Free amino acids |0.3–3%                                              |Variable by residue |Substantial by medium roast   |Extensive; arginine largely consumed             |Strecker aldehydes; Maillard intermediates; melanoidin precursors             |PROVISIONAL                          |
|Lipids           |13–17% (Arabica); 7–11% (Robusta)                   |Minimal             |Minimal in bulk               |Minimal in bulk; surface migration in dark roasts|Bulk: unchanged; surface: oxidation products, migrated oil                    |FROZEN (bulk) / PROVISIONAL (surface)|
|Proteins         |10–15%                                              |Partial denaturation|Maillard participation        |Extensive participation                          |Melanoidins; brown polymeric compounds                                        |PROVISIONAL                          |

-----

## Interface Sheet I-2 — Handoff to the Brew Dossier (Degassing and Storage)

*This interface sheet exists at the boundary between Roast and Brew. It describes the state of the roasted bean between the moment it leaves the cooling tray and the moment it is ground for brewing.*

### I-2.1 Minimal State Vector at Roast Exit

The Brew dossier will need a formal input state — a tuple of observables that characterises “what arrived at the grinder” with enough specificity that Brew-side reasoning can proceed without re-deriving the Roast-side chemistry. The reviewer of v0.2.0 correctly flagged that the v0.2.0 interface sheets were descriptive tables rather than state vectors, and that promoting them to state-vector status would enable the downstream dossier to consume a structured input rather than prose.

**Minimal state vector Σ_roast-exit** (the observables that together characterise a batch of roasted coffee at the moment it leaves the cooling tray, with sufficient precision for Brew-side reasoning):

Σ_roast-exit = ⟨ **A**, **w**, **φ**, **γ**, **μ**, **δ**, **t₀** ⟩

where:

|Symbol|Observable                       |Unit    |Typical range (medium roast) |Notes                                                                 |
|------|---------------------------------|--------|-----------------------------|----------------------------------------------------------------------|
|**A** |Agtron Gourmet (ground)          |unitless|45–55                        |Surface colour; does not specify internal gradient                    |
|**w** |Weight loss from green           |%       |14–16                        |Mass-balance anchor; does not specify what was lost                   |
|**φ** |Total porosity                   |%       |~45–55                       |Structural state; method-dependent (micro-CT, pycnometry)             |
|**γ** |CO₂ content                      |mL/g    |4–10 (roast-degree dependent)|Drives degassing kinetics; measurement method matters                 |
|**μ** |Post-cooling moisture            |%       |2–3                          |Context-sensitive (ambient humidity, packaging delay)                 |
|**δ** |Days since roast (age)           |days    |0+                           |Degassing and volatile-loss clock; essential for brew-window reasoning|
|**t₀**|Time elapsed in active trajectory|seconds |varies                       |Roast history back-reference (drop time, DTR, charge conditions)      |

**What Σ is and is not.** Σ is a minimal observable vector, not a complete state specification. A complete specification would need to include the full compound concentration vector (hundreds of volatile compounds, melanoidin fraction, individual precursor residuals, lipid oxidation state) plus the internal thermal and structural gradient fields. Those are not measured in practice. Σ is what is routinely measurable and what the Brew dossier can plausibly require as input. Two batches with identical Σ are similar but not necessarily interchangeable — the state degeneracy discussed in the introduction applies here as well.

**How the Brew dossier should consume Σ.** When Brew-side reasoning depends on “what kind of coffee is being brewed,” the authoritative statement is the value of Σ for that batch, not a descriptive label (“medium roast”, “three-day-old”). Descriptive labels are useful as shorthand in prose; Σ is the formal interface. A Brew-side claim that depends on a value not in Σ (e.g. “assumes extensive surface oil migration”) must either derive that value from Σ or explicitly flag itself as requiring additional Roast-side observations beyond the minimal vector.

**Extended Σ — two coordinates flagged for future inclusion.** The Architect review of v0.3.0 noted that Σ could be extended with surface oil fraction and with an internal-gradient proxy. Both are conceptually valuable and both currently fail a quantitative-measurement test, so they are documented here as extended coordinates rather than folded into the minimal vector:

|Symbol|Candidate observable                                                        |Current status                                                                                     |Why extended rather than minimal                                                                                                                                                                                                                                                                                   |
|------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**σ** |Surface oil fraction                                                        |Practitioner-visual (dry / spotty / glossy / pooling); no standard instrument for routine operation|Strongly coupled to §4.6 Π_oil and to RAC-11. A visual-reflectance proxy would work in principle but has not been standardised. Adding σ to the minimal vector would require either a qualitative ordinal coordinate (breaking the quantitative character of Σ) or a measurement apparatus that does not yet exist.|
|**∇T**|Internal thermal gradient proxy (e.g. whole-bean Agtron minus ground Agtron)|Measurable with standard Agtron workflow; not usually logged                                       |Strongly coupled to BR-05 (surface-vs-internal gap) and to the degeneracy discriminant programme in §0.2. Adding ∇T to the minimal vector is practical; it is held in the extended set pending an explicit decision on whether the Brew dossier needs gradient information as a first-class input.                 |

The distinction between minimal Σ and extended Σ is deliberate. The minimal vector is tight, quantitative, and routinely measurable — it is what the Brew dossier can require today without commissioning new instrumentation. The extended set documents where the interface should grow as measurement capability improves. A v0.4.0 or later revision of this dossier may promote ∇T into the minimal vector once the Brew dossier’s input requirements are settled; σ is unlikely to promote without a measurement standard.

### I-2.2 Descriptive Boundary Parameters

The table below gives the underlying descriptive parameters from which Σ is constructed. Values here are drawn from the §4 and §5 tables and carry the same status markers.

|Parameter                           |Value                                      |Notes                                                    |Status     |
|------------------------------------|-------------------------------------------|---------------------------------------------------------|-----------|
|CO₂ content post-roast (light)      |4–6 mL/g                                   |Lower generation; higher relative retention              |PROVISIONAL|
|CO₂ content post-roast (dark)       |6–10 mL/g                                  |More CO₂ generated; faster initial loss                  |PROVISIONAL|
|First 24 h degassing                |~40% of total CO₂ released                 |Rapid initial release carries volatiles                  |PROVISIONAL|
|Degassing duration                  |Weeks to months, declining                 |Never fully stops until depleted                         |FROZEN     |
|Practitioner rest window (pour-over)|5–14 days post-roast                       |Practitioner consensus; variable                         |PROVISIONAL|
|Practitioner rest window (espresso) |7–21 days post-roast                       |Longer rest for espresso extraction                      |PROVISIONAL|
|Volatile loss first 24 h            |~20–40% of total aromatics (rough estimate)|Carried by CO₂ escape; low molecular weight most affected|WEAK       |
|Post-cooling moisture (medium roast)|2–3%                                       |Sensitive to ambient humidity and packaging delay        |PROVISIONAL|
|Surface oil migration (dark roasts) |Visible post-roast; increases with time    |Practitioner-observed; quantitative studies sparse       |PROVISIONAL|

**Key sources for this interface:** Smrke et al. 2018 (time-resolved gravimetric degassing); Anderson et al. 2003 (CO₂ diffusion kinetics); Wang 2014 (CO₂ formation and degassing behaviour, University of Guelph thesis).

-----

## 11 — References

*Sources organised by tier (per §8). Two daggers (†) mark the load-bearing sources for this dossier. DOIs and stable URLs provided where available.*

### Tier 1 — Peer-reviewed scientific papers

†Mayer, F., Czerny, M., & Grosch, W. (2009). Study on the role of precursors in coffee flavor formation using in-bean experiments. *Journal of Agricultural and Food Chemistry*. doi:10.1021/jf901683v

†Alcantara, et al. (2025). Effect of roasting on chemical composition of coffee. *Food Chemistry*. https://www.sciencedirect.com/science/article/abs/pii/S0308814625004194

Bolka, M., et al. (2020). Effects of coffee roasting technologies on cup quality and health-related compounds of coffee beans. *Trends in Food Science & Technology*. https://pubmed.ncbi.nlm.nih.gov/33282263/

Debona, D., et al. (2024). Kinetic modelling of Maillard reaction products and protein content during roasting of coffee beans. *LWT — Food Science and Technology*, 203, 116237. doi:10.1016/j.lwt.2024.116237

Debona, D., et al. (2025). Comprehensive evaluation of volatile compounds and sensory profiles of coffee throughout the roasting process. *Food Research International*, 103837. doi:10.1016/j.foodres.2025.103837

Grassi, S., et al. (2023). Monitoring chemical changes of coffee beans during roasting. *Food Analytical Methods*. doi:10.1007/s12161-023-02473-w

Ludwig, I. A., Clifford, M. N., Lean, M. E. J., Ashihara, H., & Crozier, A. (2014). Coffee: biochemistry and potential impact on health. *Food & Function*. https://pubmed.ncbi.nlm.nih.gov/24671262/

Obando, M., et al. (2024). Effect of roasting level on the development of key aroma compounds in coffee. *Foods* (via PMC 11477549). https://pmc.ncbi.nlm.nih.gov/articles/PMC11477549/

Pajuelo-Muñoz, et al. (2026). Tracking aromatic volatile biomarkers through coffee bean processing. *Foods* (via PMC 12985535). https://pmc.ncbi.nlm.nih.gov/articles/PMC12985535/

Vezzulli, F., et al. (2023). Volatile compounds in green and roasted Arabica specialty coffee. *Foods* (via PMC 9914344). https://pmc.ncbi.nlm.nih.gov/articles/PMC9914344/

da Costa, C. T., et al. (2023). Thermal contaminants in coffee induced by roasting: a review. *International Journal of Environmental Research and Public Health* (via PMC 10138461). https://pmc.ncbi.nlm.nih.gov/articles/PMC10138461/

Smrke, S., Opitz, S. E. W., Vovk, I., & Yeretzian, C. (2018). Time-resolved gravimetric method to assess degassing of roasted coffee. *Journal of Agricultural and Food Chemistry*. https://pubmed.ncbi.nlm.nih.gov/29091435/

Anderson, B. A., et al. (2003). The diffusion kinetics of carbon dioxide in fresh roasted coffee. *Journal of Food Engineering*. https://www.sciencedirect.com/science/article/abs/pii/S0260877402004326

Wang, X. (2014). *Understanding the formation of CO₂ and its degassing behaviour in roasted coffee*. Master’s thesis, University of Guelph. https://atrium.lib.uoguelph.ca/server/api/core/bitstreams/ee9d7e24-7df2-42b0-a66a-e88dc6f2c70e/content

Varga, N., Hau, J., Vera, F. A., & Welti, D. H. (2002). Alkylpyridiniums. 1. Formation in model systems via thermal degradation of trigonelline. *Journal of Agricultural and Food Chemistry*, 50(5), 1032–1039. doi:10.1021/jf011234k

Yusibani, E., et al. (2023). The effect of temperature and roasting time on the physical properties of Arabica and Robusta Gayo coffee bean. *Journal of Applied Agricultural Science and Technology*. https://www.jaast.org/index.php/jaast/article/view/75

Hu, G., et al. (2019). Acrylamide in coffee: review. *Food Frontiers* (review/source note). https://pubmed.ncbi.nlm.nih.gov/31166336/

Schenker, S., et al. Physical changes during coffee roasting in rotary conduction-type heating units. (Reported via Kimi; primary bibliographic details to be verified.)

Development of coffee bean porosity and thermophysical properties during roasting. (2025). *Journal of Food Engineering*. doi:10.1016/j.jfoodeng.2024.112726

Caffeine content in filter coffee brews as a function of degree of roast and extraction yield. (2024). Via PMC 11586412. https://pmc.ncbi.nlm.nih.gov/articles/PMC11586412/

### Tier 2 — Standards and regulatory bodies

Commission Regulation (EU) 2017/2158. Establishing mitigation measures and benchmark levels for the reduction of the presence of acrylamide in food. *Official Journal of the European Union*. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32017R2158

EFSA Panel on Contaminants in the Food Chain (CONTAM). (2015). Scientific opinion on acrylamide in food. *EFSA Journal*, 13(6), 4104. doi:10.2903/j.efsa.2015.4104

Specialty Coffee Association. (2024). *What Color is Your Coffee?* *25 Magazine*, Issue 21. https://sca.coffee/sca-news/25/issue-21/what-color-is-your-coffee

Specialty Coffee Association Education. *How to Prepare for the Q Grader Course*. https://education.sca.coffee/how-to-prepare-for-the-q-grader-course

### Tier 3 — Research institutions and educational

American Chemical Society. *Why does your coffee taste and smell delicious?* https://www.acs.org/content/dam/acsorg/pressroom/reactions/infographics/why-does-your-coffee-taste-and-smell-delicious.pdf

### Tier 4 — Scientific books

Flament, I. (2002). *Coffee Flavor Chemistry*. John Wiley & Sons.

Illy, A., & Viani, R. (Eds.). (2005). *Espresso Coffee: The Science of Quality* (2nd ed.). Elsevier Academic Press.

Rao, S. (2014). *The Coffee Roaster’s Companion*. Self-published.

### Tier 5 — Industry practitioner and manufacturer documentation

Cropster. (2022). *Back to Basics: What is a Profile?* https://www.cropster.com/blog-post/back-to-basics-what-is-a-profile/

Cropster Help. (2026). *About Rate of Rise (RoR)*. https://help.cropster.com/en_US/using-roasting-intelligence/about-rate-of-rise-ror

Artisan. (2024). *Setup*. https://artisan-scope.org/docs/setup/

Barista Hustle. (2023). *HTR 1.06 Temperature Probes*. https://www.baristahustle.com/lesson/htr-1-06-temperature-probes/

Perfect Daily Grind. (2020). *Coffee Roasting Probes and Tips on Using Them*. https://perfectdailygrind.com/2020/05/coffee-roasting-probes-and-tips-on-using-them/

Perfect Daily Grind. (2024). *Drum vs Fluid Bed: How Different Coffee Roasters Affect Flavour*. https://perfectdailygrind.com/2024/02/drum-fluid-bed-how-roasters-affect-coffee-flavour/

PROBAT sample and production roaster datasheets. (Manufacturer documentation; cited via Perplexity.)

Loring S35 Kestrel datasheet. (Manufacturer documentation; cited via Perplexity.)

Bühler RoastMaster continuous line specifications. (Manufacturer documentation; cited via Perplexity.)

### Note on sources excluded from this list

Several Tier 5 blog sources cited by Kimi in the equipment and thermodynamics returns (Sheldrake Coffee, Berto Online, Reborn Coffee, Rubasse Roasters, Achilles Coffee, Headcount Coffee, Biodynamic Coffee, Torque Coffee) are acknowledged as the source of specific numerical or qualitative claims within the body but are not promoted into the reference list, consistent with the Beans dossier practice of reserving the reference list for sources that carry analytical weight. Where a single Tier 5 claim is the only available source for a parameter, the status has been set to PROVISIONAL rather than FROZEN.

Four Perplexity files covering thermodynamics, chemistry, physical, and aromatics were not received at the time of v0.2.0 curation. If they arrive later, they will be merged in a subsequent revision and may result in status upgrades from PROVISIONAL to FROZEN for parameters where Perplexity’s standards-body reach provides independent corroboration.

-----

*Dossier v0.3.1 — two Architect reviews integrated under Guardian stance. Predictive scaffolds added for oil migration transport (§4.6), energy closure (§2.6), mass balance (§3.4), and measurement model (§0.1). FROZEN parameters are stable for citation. PROVISIONAL entries await further confirmation. OPEN questions are tracked under CL-2026-019 through CL-2026-025.*
