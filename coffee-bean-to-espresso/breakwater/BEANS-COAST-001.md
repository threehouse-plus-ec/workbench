# Beans Dossier — “Origin & Material Substrate”

*A reference document on the green (unroasted) coffee bean: what it is, where it comes from, how it is processed, what can be measured about it, and what chemical compounds it contains.*

**Dossier ID:** BEANS-COAST-001  
**Version:** 0.3.0 (release candidate — post-Council review)  
**Date:** 2026-04-06  
**Parent:** Coffee / Espresso Essay (CL-2026-010)  
**Tier:** T1b (Metrological)  
**Stance:** Guardian (with Architect and Scout review incorporated)  
**Curated from:** TC-BEANS-001 v1.1 raw returns (Claude, Kimi K2, GPT-5.4, Perplexity, Gemini — Gemini set aside pending source verification)

**How to read the status markers:**

Each fact or measurement in this dossier carries a status marker:

- `FROZEN` — verified across multiple independent sources, stable, safe to cite.
- `PROVISIONAL` — supported by evidence but based on fewer sources or awaiting independent confirmation.
- `OPEN` — unresolved question; needs further investigation.
- `QUARANTINED` — the original source could not be independently verified; excluded from the main tables until checked.

-----

## Introduction — How to Read This Dossier

A green coffee bean is a seed that has never been roasted. The sugars that will caramelise, the acids that will define brightness, the proteins that will react with those sugars to generate aroma — all are already present, or absent, before the roaster applies heat. This dossier records the state of that starting material.

The document covers five topics, each dealing with a different aspect of the green bean’s identity:

- **§1 Botanical Identity** — what species and variety the bean belongs to.
- **§2 Terroir Envelope** — the growing environment (altitude, climate, soil) and how it shapes the bean.
- **§3 Post-Harvest Processing** — what happens between picking the cherry and exporting the green bean.
- **§4 Physical Metrics** — the measurable physical properties used for grading and quality control.
- **§5 Precursor Chemistry** — the chemical compounds inside the bean that will later produce flavour and aroma during roasting.

These five topics are not arbitrary. They follow the order in which the bean’s identity is formed, and each stage is essentially irreversible: genetics are fixed when the plant is pollinated, growing conditions accumulate over months, processing intervenes after harvest, physical measurements are taken at the point of trade, and chemistry represents the final state of the bean before heat is applied.

Each topic section follows the same structure: (a) declared parameters with status markers, (b) a validity contract explaining when those numbers can and cannot be trusted, (c) open disputes, and (d) notes on how this information connects to later stages (roasting, brewing).

Two cautions for the reader. First, the ranges in this dossier span many origins, varieties, and studies. Any single batch of green coffee will fall within a narrower window. Second, this dossier describes what is *in* the bean, not what ends up *in the cup*. The journey from bean chemistry to taste passes through roasting and brewing — those are covered in separate documents.

One important finding runs through the entire dossier: current evidence suggests that post-harvest processing does not simply reveal what was already in the bean. It can actively change the bean’s chemical makeup. The full extent of this reshaping is still being studied (see §7, question BW-01).

-----

## 0 — Boundary Condition

**Nothing in this dossier has been roasted.** The moment heat triggers browning reactions (known as Maillard reactions — the same chemistry that browns bread and seared meat) or breaks down compounds through high temperature (pyrolysis), the material belongs to the Roast dossier. Fermentation during processing is included here because it happens before the bean is exported and it shapes the bean’s chemical starting state.

**Not covered here:** roast level, espresso extraction, brew methods, or taste descriptions, except where a direct, experimentally demonstrated link to green-bean composition exists. A reference table for what happens to these compounds during roasting is provided in Appendix A.

-----

## 1 — Botanical Identity

### Key terms used in this section

- **Species:** The broadest biological grouping. The two species that matter commercially are *Coffea arabica* (Arabica) and *Coffea canephora* (commonly called Robusta).
- **Variety / Cultivar:** A named type within a species. “Variety” usually means a naturally occurring subtype; “cultivar” (short for “cultivated variety”) means one that has been deliberately selected or bred by humans. In the coffee trade, these terms are often used interchangeably.
- **Landrace:** A locally adapted, genetically diverse population — not a single uniform type.
- **Hybrid group:** A family of cultivars created by crossing two different species or varieties.
- **Trade designation:** A commercial label (like “Ethiopian Heirloom”) that may not correspond to a single biological category.

### 1.1 Declared Parameters

|Parameter                       |Value                                                                                                       |Status|Confidence|Source                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------|------|----------|--------------------------------|
|Arabica chromosome count        |44 chromosomes (four copies of each — a “tetraploid,” meaning it has double the usual set)                  |FROZEN|STRONG    |Salojärvi 2024; Scalabrin 2020  |
|Robusta chromosome count        |22 chromosomes (the standard two copies — a “diploid”)                                                      |FROZEN|STRONG    |Multiple concordant             |
|How Arabica originated          |A natural cross between two other species: *C. canephora* (Robusta) and *C. eugenioides*                    |FROZEN|STRONG    |Salojärvi 2024                  |
|When this cross occurred        |350,000–610,000 years ago                                                                                   |FROZEN|STRONG    |Salojärvi 2024 (Nature Genetics)|
|Pollination                     |Arabica pollinates itself (unique in the coffee genus); Robusta requires cross-pollination from other plants|FROZEN|STRONG    |WCR; SCA literature             |
|Foundational lineages           |Nearly all cultivated Arabica descends from two groups: Typica and Bourbon                                  |FROZEN|STRONG    |WCR Varieties Catalog (2024)    |
|Genetic diversity in cultivation|Cultivated Arabica contains less than 1% of the genetic diversity found in wild populations                 |FROZEN|STRONG    |Salojärvi 2024                  |

**Context (not a property of the bean itself):** Arabica accounts for roughly 60% of global coffee production, Robusta roughly 40% (International Coffee Organization data; these shares shift over time).

### 1.2 Cultivar Classification

Classification follows the World Coffee Research (WCR) Varieties Catalog, the most widely accepted reference. Terms are labelled by their biological category (see key terms above).

**Bourbon–Typica lineage (varieties / cultivar groups):** Typica (tall plant, low yield, highly vulnerable to coffee leaf rust, valued for sweetness and clarity in the cup); Bourbon (moderately tall, higher yield than Typica, exists in red and yellow variants); Caturra (a natural dwarf mutation of Bourbon, high rust vulnerability); Catuaí (a cross between Caturra and Mundo Novo, compact, high yield, moderate rust vulnerability); Mundo Novo (a natural cross between Typica and Bourbon, vigorous and tall).

**Ethiopian landraces:** Genetically diverse, locally adapted populations — not single uniform types. The commercial label “Ethiopian Heirloom” is a trade designation that lumps together more than 10,000 identified varieties.

**Kenyan selections:** SL-28 and SL-34 (developed by Scott Agricultural Laboratories in Kenya in the 1930s; genetically related to the Bourbon group; prized for cup quality but vulnerable to rust). Ruiru 11 (a hybrid combining SL28 and Rume Sudan genetics from the 1980s; rust resistant). Batian (a cross between Ruiru 11 and SL28; rust resistant, balanced cup).

**Gesha/Geisha (cultivar):** Originally from the Gori Gesha forest in Ethiopia. Produces elongated seeds with low-to-moderate yield. The 2024 genome study showed it shares ancestry with both wild Ethiopian populations and the Bourbon/Typica groups. Its reputation for exceptional quality depends heavily on where and how it is grown and processed — it is not automatically superior regardless of conditions (see Anti-Claim AC-07).

**Disease-resistant hybrid groups:** Catimor (Caturra × Timor Hybrid); Sarchimor (Villa Sarchi × Timor Hybrid); Castillo (a Colombian selection); Starmaya (a first-generation hybrid). All carry disease-resistance genes from Robusta, introduced through the Timor Hybrid — a natural cross between Arabica and Robusta discovered on the island of Timor in the early twentieth century. Cup quality varies.

### 1.3 Validity Contract

- Chromosome counts are fixed genetic facts and will not change.
- Cultivar classifications follow the WCR Varieties Catalog (2024 edition). Where trade usage and WCR classification disagree, WCR takes precedence in this dossier.
- “Ethiopian Heirloom” must not be treated as a single variety in any analysis built on this dossier.

### 1.4 Open Disputes

- The terms “variety,” “cultivar,” and “landrace” are used inconsistently across scientific papers, breeding programmes, and the coffee trade. This dossier follows the WCR convention but notes that reclassification of some entries (e.g. SL-28, Gesha) into broader genetic groups is ongoing.

### 1.5 Connections to Other Work — Recent Genetic Research (2020–2026)

|Study                                                                                                                                                               |Status     |Source                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|
|Salojärvi et al. 2024: detailed genetic maps of Arabica and its parent species; traced the split between wild and cultivated populations to roughly 30,500 years ago|FROZEN     |Nature Genetics 56:721–731                             |
|Scalabrin et al. 2020: first complete Arabica genome (Red Bourbon variety), identified 46,562 genes                                                                 |FROZEN     |Scientific Reports 10:4642                             |
|Kona Typica genome 2024: a separate Arabica genome assembly with 65,458 genes identified                                                                            |PROVISIONAL|PRJCA043259; reported by one source only               |
|Berny Mier y Teran et al. 2025: global field trials comparing Arabica varieties                                                                                     |PROVISIONAL|Frontiers in Plant Science; reported by one source only|
|*C. stenophylla* genetic study 2025: identified genetic markers linked to drought tolerance in a climate-resilient coffee species                                   |QUARANTINED|Source could not be independently verified             |

-----

## 2 — Terroir Envelope

*Terroir refers to the combination of environmental conditions — altitude, climate, soil, rainfall, and shade — that shape how the coffee plant grows and what ends up inside the bean.*

### 2.1 Declared Parameters

|Parameter                |Arabica                      |Robusta       |Status|Confidence|Notes                                               |
|-------------------------|-----------------------------|--------------|------|----------|----------------------------------------------------|
|Typical growing elevation|1,200–2,200 m above sea level|200–800 m     |FROZEN|MODERATE  |Varies strongly with latitude                       |
|Optimal temperature      |15–24 °C                     |24–30 °C      |FROZEN|STRONG    |                                                    |
|Annual rainfall          |1,200–2,200 mm               |2,200–3,000 mm|FROZEN|STRONG    |A distinct dry period is needed to trigger flowering|
|Soil pH (optimal)        |5.5–6.0 (slightly acidic)    |5.0–6.5       |FROZEN|MODERATE  |                                                    |

### 2.2 How Altitude Affects Bean Chemistry

Higher altitude generally means cooler temperatures, which slows cherry ripening. This extended growing period affects the chemical compounds that accumulate inside the bean. The following table summarises the best-quantified relationships, all from a single well-designed Ethiopian study (Worku et al. 2018):

|What changes                                         |Direction            |How much (per 100 m gain in altitude)     |Conditions              |Status     |
|-----------------------------------------------------|---------------------|------------------------------------------|------------------------|-----------|
|Caffeine                                             |Decreases            |–0.12 g/kg                                |Ethiopian Arabica       |FROZEN     |
|Chlorogenic acids (bitter/astringent compounds)      |Decreases            |–1.23 g/kg                                |Ethiopian Arabica       |FROZEN     |
|Sucrose (the main sugar) — washed beans              |Increases            |+3.02 g/kg                                |Washed processing only  |FROZEN     |
|Sucrose — naturally processed beans                  |No significant effect|+0.36 g/kg (not statistically significant)|Natural processing only |FROZEN     |
|Perceived acidity (cup score) — shaded trees         |Increases            |+0.22 points                              |Under shade trees       |FROZEN     |
|Perceived acidity — unshaded trees                   |No significant effect|—                                         |Full sun                |FROZEN     |
|Bean density (how heavy per unit volume) at 800–900 m|—                    |619.75 ± 13.72 kg/m³                      |Nepal, Arabica          |PROVISIONAL|
|Bean density at 1,400–1,500 m                        |—                    |687.5 ± 8.18 kg/m³                        |Nepal, Arabica          |PROVISIONAL|
|Fatty acid content                                   |Increases            |Not precisely quantified                  |China (Pu’er) study 2024|PROVISIONAL|

**The most important finding in this table:** The effect of altitude on sucrose depends on how the coffee is processed. In washed beans, sucrose clearly increases with altitude. In naturally processed beans, it does not. This means that growing environment and processing method are not independent — they interact.

### 2.3 Validity Contract

- Altitude itself does not directly cause these changes. It is a stand-in for temperature, oxygen levels, and sunlight, which all change together as you go higher. This dossier does not treat altitude as a direct cause.
- The effects of environment depend on interactions: altitude combined with shade, altitude combined with processing method, altitude combined with variety. Claims based on a single variable (“higher = better”) are oversimplifications.
- Claims that specific soil minerals produce specific flavours lack controlled experimental support. The evidence is mostly observational.

### 2.4 Open Disputes

|Claim                                          |Strength of evidence                                                   |
|-----------------------------------------------|-----------------------------------------------------------------------|
|Higher altitude produces denser beans          |STRONG (multiple studies confirm)                                      |
|Higher altitude increases sugar and acid levels|MODERATE (mechanism understood, but depends on other factors)          |
|Higher altitude improves cup scores            |MODERATE (consistent pattern, but hard to isolate from other variables)|
|Specific soil minerals create specific flavours|WEAK (mostly uncontrolled observations)                                |
|Shade slows cherry ripening                    |STRONG (well-established biology)                                      |
|Shade produces specific flavour outcomes       |MODERATE (some support, but many confounding factors)                  |
|“Terroir” as a holistic quality predictor      |PRACTITIONER (useful concept, but limited predictive power)            |

### 2.5 Connections to Other Dossiers

The sucrose × altitude × processing interaction has direct consequences for roasting: the amount of sugar available for browning reactions depends on both where the coffee was grown *and* how it was processed, not on growing conditions alone. Shade management is not uniformly beneficial — its effects depend on the elevation band.

-----

## 3 — Post-Harvest Processing

*Processing is what happens between picking the coffee cherry and exporting the dried green bean. It involves removing the fruit layers, fermenting, and drying. Different methods produce different chemical outcomes in the bean.*

### Key terms

- **Mucilage:** The sticky, sugary layer surrounding the bean inside the cherry. How much of it stays on the bean during drying is the key variable distinguishing processing methods.
- **Fermentation:** Microbial activity (bacteria and yeasts breaking down sugars) that occurs naturally during processing. It can be encouraged, controlled, or minimised depending on the method.
- **Water activity (aw):** A measure of how much water in the bean is available for microbial growth (explained further in §4). Safe storage requires aw below 0.70.

### 3.1 Declared Parameters

|Method                |What happens to the mucilage                                               |Fermentation time                               |Typical drying time|Status     |
|----------------------|---------------------------------------------------------------------------|------------------------------------------------|-------------------|-----------|
|Washed (wet)          |Completely removed by fermentation and washing                             |12–72 hours in water                            |10–15 days         |FROZEN     |
|Natural (dry)         |Stays on — the whole cherry dries intact                                   |Continuous throughout drying                    |15–30 days         |FROZEN     |
|Honey / pulped-natural|Partially kept (10–100%, creating a spectrum from “white” to “black” honey)|During drying                                   |10–22 days         |FROZEN     |
|Anaerobic             |Varies                                                                     |24–120 hours in sealed, oxygen-free tanks       |Varies             |FROZEN     |
|Carbonic maceration   |Stays on initially                                                         |24–120 hours in a carbon-dioxide-rich atmosphere|Varies             |PROVISIONAL|

**What these methods do to the bean’s chemistry:**

- Washed processing tends to produce beans with less variation in sugar-related compounds and a “cleaner” chemical profile. [MODERATE confidence — consistent finding, but not precisely quantified]
- Natural processing tends to leave more residual sugar in the bean and creates more variation in moisture distribution. [MODERATE — established pattern, but not universal]
- Processing method significantly affects the levels of bioactive compounds and aromatic precursors in the green bean (Várady et al. 2022, statistically significant at P = 0.04 for chlorogenic acid differences). [FROZEN]

### 3.2 Microbes Involved in Fermentation

The following bacteria and yeasts have been identified as dominant in different fermentation conditions. These are representative findings from selected studies, not universal rules:

|Fermentation condition     |Dominant bacteria                                                       |Dominant yeasts                            |Status     |
|---------------------------|------------------------------------------------------------------------|-------------------------------------------|-----------|
|Washed (underwater)        |*Weissella*, *Leuconostoc*, *Lactiplantibacillus* (lactic acid bacteria)|—                                          |PROVISIONAL|
|Semi-anaerobic (low oxygen)|*Acetobacter* (acetic acid bacteria, increased)                         |—                                          |PROVISIONAL|
|Fully anaerobic (no oxygen)|—                                                                       |*Pichia*, *Issatchenkia*, *Wickerhamomyces*|PROVISIONAL|

### 3.3 Validity Contract

- Processing changes the internal chemistry of the bean, not just the surface. This is supported by research from the Specialty Coffee Association and by Várady et al. (2022/2024). How much it changes depends on the specific method and conditions.
- “Carbonic maceration” is borrowed from winemaking terminology, but the coffee industry uses the term loosely. In wine, it refers to fermentation happening inside intact grape cells. In coffee, it often just means fermentation in a sealed, CO₂-rich container.
- Processing is included in this dossier (rather than a separate one) because it happens before the bean is exported and defines the chemical state in which the bean enters trade.

### 3.4 Open Disputes

- There is no evidence-based universal rule for optimal fermentation times. They vary with climate, altitude, and the specific microbial community present.
- Many claims about anaerobic and carbonic maceration producing specific flavour outcomes have not been validated by controlled experiments. Some of this language is marketing rather than science.

### 3.5 Connections to Other Dossiers — Common Defects

|Defect                                     |Cause                                                         |How it is detected                                           |Status|
|-------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|------|
|Over-fermentation                          |Fermentation went too long or was uncontrolled                |Sour, vinegary, or medicinal off-flavours                    |FROZEN|
|Mould / ochratoxin A (OTA, a harmful toxin)|Uneven drying, moisture above 12.5%, water activity above 0.70|Visible mould; OTA cannot be removed by roasting             |FROZEN|
|Phenolic taint                             |Contaminated water or uncontrolled fermentation               |Medicinal or “band-aid” flavours                             |FROZEN|
|Quakers                                    |Underripe cherries that lack sugars and amino acids           |Invisible in green beans; appear as pale beans after roasting|FROZEN|

-----

## 4 — Physical Metrics

*These are the measurable physical properties used by buyers, graders, and roasters to assess green coffee quality and predict how it will behave during roasting and storage.*

### Key terms

- **Moisture content:** The percentage of the bean’s total weight that is water.
- **Water activity (aw):** A number between 0 and 1 that measures how much of the water in the bean is “free” — that is, available for microbes to use and for chemical reactions to occur. A bean can have acceptable moisture content but still be unstable if its water activity is too high. Think of it this way: moisture tells you how much water is present; water activity tells you how much of it is dangerous.
- **Bulk density:** How heavy a container of beans is per unit volume, including the air spaces between beans. This is different from the density of the bean material itself (true density). When this dossier says “density,” it means bulk density unless stated otherwise.
- **Screen size:** Beans are sorted by passing them through metal plates with round holes. The hole sizes are measured in sixty-fourths of an inch. A “Screen 18” bean passes through an 18/64-inch (7.1 mm) hole but not a smaller one.

### 4.1 Declared Parameters

|What is measured              |Target / Range                                                    |How it is measured                                                                     |Standard                    |Status|
|------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------|------|
|Moisture content              |10–12% (specialty target); 9–13% (acceptable under SCA/ICO rules) |Reference: oven-drying at 105 °C (ISO standard 6673). Field: electronic moisture meters|SCA, ICO                    |FROZEN|
|Water activity (aw)           |0.55–0.65 (recommended); must be below 0.70 (SCA threshold)       |Dedicated water activity meter                                                         |SCA                         |FROZEN|
|Bulk density (Arabica)        |670–750 g/L                                                       |Weigh a known volume of beans in a graduated cylinder                                  |Industry practice           |FROZEN|
|Screen size                   |Screens 13–20 (sizes from ~5.2 mm to ~8.0 mm)                     |Standardised sieves with round holes                                                   |SCA and regional conventions|FROZEN|
|Defect count (specialty grade)|Zero major defects; no more than 5 minor defects in a 350 g sample|Visual inspection under controlled lighting                                            |SCA GACCS                   |FROZEN|

### 4.2 Regional Grading Systems

Different countries use different names for their size grades:

|Grade name              |Country        |Requirement                                                            |Status|
|------------------------|---------------|-----------------------------------------------------------------------|------|
|Supremo                 |Colombia       |Screen 17 or larger (~6.7 mm+)                                         |FROZEN|
|Excelso                 |Colombia       |Screen 14–16 (~5.6–6.3 mm)                                             |FROZEN|
|AA                      |Kenya          |Screen 17–18 (~6.7–7.1 mm)                                             |FROZEN|
|AB                      |Kenya          |Screen 15–16 (~6.0–6.3 mm)                                             |FROZEN|
|PB (Peaberry)           |Kenya          |Screen 13 (~5.2 mm; a single round bean instead of the usual flat pair)|FROZEN|
|SHB (Strictly Hard Bean)|Central America|Grown above 1,200–1,350 m (an altitude-based grade, not a size grade)  |FROZEN|

### 4.3 Validity Contract

- Moisture content and water activity measure different things and are not interchangeable. Water activity is the better predictor of storage safety and shelf life.
- Bulk density and true density are different measurements. Comparing density values from different sources only makes sense if the same method was used.
- Screen size tells you about uniformity (important for even roasting), not about flavour quality. A small, clean bean can taste better than a large, defective one.

### 4.4 Open Disputes

- **Sample size question (resolved):** Some older references cite a 300 g sample for defect grading; the current SCA standard specifies 350 g. The 300 g figure comes from older international standards or Robusta-specific protocols.
- Bean density alone does not predict quality. Variety, processing, and storage conditions all play a role.

### 4.5 How Defects Are Counted

The SCA system counts defects using equivalence ratios — not every flawed bean counts as one full defect:

|Type of defect                    |How many = 1 full defect|Status|
|----------------------------------|------------------------|------|
|Full black bean                   |1                       |FROZEN|
|Partial black bean                |2–3                     |FROZEN|
|Broken or chipped bean            |5                       |FROZEN|
|Floater (an abnormally light bean)|5                       |FROZEN|
|Insect-damaged bean               |2–5                     |FROZEN|

-----

## 5 — Precursor Chemistry

*The green bean contains hundreds of chemical compounds. This section focuses on the ones that matter most for flavour and aroma — not because they taste good in raw form, but because they are the raw materials (precursors) that roasting will later transform into the flavours we recognise in coffee.*

### Key terms

- **Dry weight basis (dwb):** Concentrations expressed as a percentage of the bean’s weight after all water has been removed. This allows fair comparison between beans with different moisture levels.
- **Chlorogenic acids (CGAs):** A family of plant compounds that contribute to bitterness and astringency. Robusta has more of them than Arabica, which is one reason Robusta tends to taste harsher.
- **Sucrose:** Ordinary table sugar. The most important single sugar in green coffee. During roasting, it breaks down and reacts with amino acids to produce the browning reactions (Maillard reactions) responsible for much of coffee’s flavour and colour.
- **Trigonelline:** A compound related to vitamin B3. It breaks down during roasting into aromatic compounds (pyridines) that contribute to coffee’s smell.
- **Caffeine:** A bitter-tasting stimulant. Unlike most other compounds here, caffeine is highly heat-stable and survives roasting almost unchanged.
- **Lipids (fats):** Contribute to mouthfeel (the “body” of the coffee) and act as carriers for aromatic compounds.
- **Free amino acids:** Small protein fragments that react with sugars during roasting (Maillard reactions) to produce flavour and colour.

### 5.1 Declared Parameters (Green Bean, Dry Weight Basis)

|Compound                           |Arabica range|Robusta range      |Status     |Confidence|
|-----------------------------------|-------------|-------------------|-----------|----------|
|Total carbohydrates                |50–60%       |34–55%             |FROZEN     |STRONG    |
|Sucrose                            |5–9%         |0.9–5%             |FROZEN     |STRONG    |
|Reducing sugars (glucose, fructose)|~1% or less  |Similar            |FROZEN     |STRONG    |
|Chlorogenic acids (total)          |3.5–8.4%     |7–14%              |FROZEN     |STRONG    |
|Caffeine                           |0.8–1.7%     |1.7–4.0%           |FROZEN     |STRONG    |
|Trigonelline                       |0.8–1.3%     |0.6–1.0%           |FROZEN     |STRONG    |
|Lipids (fats)                      |13–17%       |7–11%              |FROZEN     |STRONG    |
|Proteins                           |10–15%       |10–15%             |FROZEN     |STRONG    |
|Free amino acids                   |0.3–3%       |Higher than Arabica|PROVISIONAL|MODERATE  |
|Minerals (ash)                     |3–5%         |3–5%               |FROZEN     |STRONG    |

### 5.2 Where Sources Disagreed on Ranges

When different research agents returned different numbers, the dossier adopted the range shown above based on the following reasoning:

|Compound                   |Narrower estimate                               |Wider estimate                                      |Adopted |Why                                                                                                 |
|---------------------------|------------------------------------------------|----------------------------------------------------|--------|----------------------------------------------------------------------------------------------------|
|Robusta sucrose            |0.9–4.85% (from a well-controlled imaging study)|4.0–7.0% (from a broader but less controlled survey)|0.9–5%  |The imaging study had tighter methodology; the wider range may include measurement-basis differences|
|Chlorogenic acids (Arabica)|2.8–5.4% (Ethiopian samples only)               |4.0–8.4% (global survey)                            |3.5–8.4%|The Ethiopian range is one origin; the wider range captures more genetic diversity                  |
|Free amino acids           |0.3–0.6% (one agent)                            |0.4–3% (another agent)                              |0.3–3%  |The wide range reflects genuine diversity across origins and varieties                              |

### 5.3 How Compounds Relate to Each Other

Some compounds in the green bean are statistically correlated. These relationships were reported by one research agent (Kimi) and await independent confirmation:

|Relationship                                          |Direction                                                                                       |Status     |
|------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------|
|Fat content ↔ caffeine                                |Beans with more fat tend to have less caffeine                                                  |PROVISIONAL|
|Fat content ↔ chlorogenic acids, sucrose, trigonelline|Beans with more fat tend to have more of these compounds                                        |PROVISIONAL|
|Trigonelline ↔ caffeine (in green beans)              |Tend to increase together                                                                       |PROVISIONAL|
|Caffeine determination                                |Roughly 94% of a bean’s caffeine level is determined by its species, not its growing environment|PROVISIONAL|

### 5.4 Validity Contract

- All concentration ranges are expressed on a dry-weight basis unless marked otherwise.
- These ranges cover many origins and varieties. Any single lot will fall within a narrower window.
- Scientists do not yet have a complete map of which green-bean compounds produce which specific roasted-coffee flavours. The compounds listed in §5.1 are non-volatile precursors — they do not smell or taste like coffee themselves, but they are the raw materials from which volatile aromatic compounds are generated during roasting. This dossier does not endorse claims that a specific precursor level guarantees a specific flavour.
- Mapping from green-bean chemistry to roasted-coffee aroma is a statistical relationship, not a fully understood causal mechanism. This is a genuine gap in current knowledge, not a limitation of this review.

### 5.5 Open Disputes

- Exact concentration ranges for chlorogenic acids and lipids differ between studies depending on measurement method, how “dry weight” was defined, and which origins and varieties were sampled.
- Which class of precursors matters most for flavour (chlorogenic acids vs sucrose vs proteins) is not settled. The current consensus is that they all interact.
- Rapid screening methods (such as near-infrared spectroscopy) show variable accuracy for predicting sugar and lipid content compared with laboratory methods.

-----

## 6 — Anti-Claims Register

*These are statements that are widely repeated in coffee discourse but are not adequately supported by the evidence reviewed in this dossier. They are not opinions — they are claims whose evidential basis was tested and found insufficient.*

|ID   |The claim                                                |Why it is problematic                                                                                                    |Status                    |
|-----|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------|
|AC-01|“Ethiopian coffee = fruity”                              |An oversimplified shorthand, not a causal relationship. Ethiopia has >10,000 varieties grown across diverse conditions.  |ACTIVE                    |
|AC-02|“Higher altitude = better coffee”                        |A correlation that masks complex interactions with temperature, shade, variety, and processing method                    |ACTIVE                    |
|AC-03|“Natural process = more flavour”                         |Confuses the processing method with the many fermentation variables within it                                            |ACTIVE                    |
|AC-04|“Single-origin guarantees quality”                       |A marketing concept, not an analytical one                                                                               |ACTIVE                    |
|AC-05|“Older beans are stale”                                  |Oversimplifies; deliberately aged coffees are a recognised category                                                      |ACTIVE                    |
|AC-06|“Processing merely reveals what is already in the bean”  |Evidence shows processing can change the bean’s internal chemistry, not just expose it. The extent depends on the method.|ACTIVE — EVIDENCE CONTRARY|
|AC-07|“Gesha quality is intrinsic and universal”               |Conflates the variety’s genetic potential with the growing and processing conditions needed to express it                |ACTIVE                    |
|AC-08|“Washed = higher quality”                                |A bias toward one processing method, not supported as a universal rule                                                   |ACTIVE                    |
|AC-09|“Volcanic soils inherently produce higher quality coffee”|Frequently claimed, but controlled experiments isolating soil type from other variables are rare                         |ACTIVE                    |
|AC-10|“Bigger beans = better coffee”                           |Screen size measures uniformity (important for even roasting), not flavour quality                                       |ACTIVE                    |

-----

## 7 — Open Questions

*These are questions raised during the research and review process that could not be fully answered. Three have been assigned formal tracking numbers for future investigation.*

|ID   |Question                                                                                                                                                       |Tracking number|Status         |Current best answer                                                                                                                                                                                                                                                                                                                   |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|BW-01|Does processing create new compounds in the bean, or does it only select from what was already there?                                                          |CL-2026-016    |UNDERDETERMINED|Processing appears to be a secondary biological event: microbes during fermentation introduce compounds that were not present in the cherry at harvest. The extent varies by method — anaerobic and inoculated processes introduce more new material than traditional washed processing. This is a graded answer, not a simple yes/no.|
|BW-02|Is the SCA defect grading sample 300 g or 350 g?                                                                                                               |—              |RESOLVED       |350 g, per the current SCA standard (2023/2024). The 300 g figure comes from older international standards.                                                                                                                                                                                                                           |
|BW-03|When did the Arabica species originate — 10,000–50,000 years ago or 350,000–610,000 years ago?                                                                 |—              |RESOLVED       |350,000–610,000 years ago (Salojärvi et al. 2024, Nature Genetics). The shorter timeframe, from one research agent, is not supported by the primary literature.                                                                                                                                                                       |
|BW-04|Can specific green-bean compounds be reliably mapped to specific roasted-coffee aromas?                                                                        |CL-2026-017    |OPEN           |Not yet. No complete mapping exists. This is a genuine research gap.                                                                                                                                                                                                                                                                  |
|BW-05|If sucrose accumulation with altitude depends on processing method (Worku 2018), what does this mean for the idea that the bean has a fixed “latent potential”?|CL-2026-018    |OPEN           |It means the “latent potential” idea works for genetics and growing conditions but breaks down at the processing stage. Processing does not just reveal what the environment put there — it determines whether the environment’s contribution is expressed at all.                                                                    |

-----

## 8 — How Sources Were Ranked

|Priority   |Type of source                 |Examples                                                                                                                         |
|-----------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|1 (highest)|Peer-reviewed scientific papers|Salojärvi 2024; Worku 2018; Caporaso 2018; Ky 2001; Jaiswal 2019                                                                 |
|2          |Standards organisations        |Specialty Coffee Association (SCA); International Organisation for Standardisation (ISO); International Coffee Organization (ICO)|
|3          |Research institutions          |World Coffee Research (WCR); CIRAD (French agricultural research centre); Coffee Science Foundation                              |
|4          |Scientific books               |Illy & Viani, *Espresso Coffee*; Flament, *Coffee Flavor Chemistry*; Hoffmann, *The World Atlas of Coffee*                       |
|5          |Industry practitioners         |Barista Hustle; Scott Rao; Cropster; Roast Magazine                                                                              |
|6 (lowest) |Marketing material             |Included only when no better source exists, and always labelled as such                                                          |

-----

## 9 — Where This Dossier Came From

This dossier was built from raw research notes gathered by five independent AI research agents, each given the same set of questions and evidence rules (Task Card TC-BEANS-001 v1.1). The agents searched different sources and returned notes independently. The results were then compared, cross-checked, and merged into this document.

|Agent           |Files returned              |What it contributed that others did not                                                                                                                                                                                           |
|----------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Claude Opus 4.6 |1 (covering all five topics)|The Worku 2018 altitude × processing interaction data; Salojärvi 2024 genome study                                                                                                                                                |
|Kimi K2         |5                           |A separate Arabica genome assembly (Kona Typica); microbial species in fermentation; compound correlation data; defect counting ratios                                                                                            |
|GPT-5.4 Thinking|5                           |Direct citation of the ISO moisture measurement standard; the most recent (2025–2026) processing research; the distinction between bulk and true density                                                                          |
|Perplexity      |5                           |The largest number of sources overall; a proteomics study (Fenrich 2023); key studies on shade and soil effects; FAO and ICO standards; the volcanic soil anti-claim                                                              |
|Gemini          |1 (set aside)               |A genetic study on a climate-resilient coffee species (*C. stenophylla*); a study on soil microbes at different altitudes — but the sources could not be independently verified, so this material is excluded from the main tables|

**Revision history:**

- v0.1.0 (2026-04-06): Initial draft.
- v0.2.0 (2026-04-06): Added status markers to all parameters; moved roasting-loss data to Appendix A; standardised section structure; tightened language.
- v0.3.0 (2026-04-06): Incorporated review from Architect and Scout stances; resolved two open questions (sample size: 350 g; polyploidy timing: 350–610 kya); assigned tracking numbers to three remaining open questions; updated anti-claim AC-06 status; added tier designation; rewrote for accessibility (plain language, definitions, reduced jargon).

-----

## 10 — Conclusion: What the Bean Encodes

The green coffee bean arrives at the roaster as a finished biological object. Its genetic blueprint was fixed hundreds of thousands of years ago by a single cross between two wild species. Its density, sugar content, and acid balance were shaped over months of growth under specific conditions of altitude, temperature, rainfall, and shade. Its microbial history was determined during fermentation and drying. By the time it reaches a grading table, it carries a precise chemical inventory — one that sets the upper limit of what any roast or brew can extract from it.

Three findings from this review deserve emphasis.

First, Arabica’s genetic narrowness is a structural vulnerability, not a footnote. Cultivated Arabica retains less than 1% of the diversity found in wild populations. Every variety in the specialty market traces back to the same Bourbon–Typica bottleneck. The species’ future under climate pressure depends on wild material that currently sits in Ethiopian forests and gene banks, not in commercial plantations.

Second, the most important quantitative finding in the environmental literature is an interaction, not a simple trend: sucrose accumulation with altitude is significant only in washed beans, not in naturally processed ones (Worku et al. 2018). This means that growing environment and processing are not independent factors — they are coupled. The popular idea that the bean contains a fixed “latent potential” that processing merely reveals is useful but incomplete. Processing does not just expose what altitude deposited; it determines whether altitude’s contribution is expressed at all.

Third, the gap between what can be measured and what is routinely measured remains large. Laboratory instruments can quantify chlorogenic acids, caffeine, trigonelline, and sucrose with high precision. Water activity meters can predict storage safety better than moisture content alone. Portable spectroscopy is approaching field-level accuracy for several compounds. Yet most green coffee in trade is still graded primarily by visual defect count and moisture percentage — metrics that capture only a fraction of the bean’s actual state.

This dossier does not claim to be complete. It records the state of knowledge as of April 2026, drawn from five independent research agents and cross-checked against scientific papers, standards-body documents, and practitioner expertise. Where sources conflict, the conflict is preserved. Where evidence is weak, it is marked accordingly. The ten anti-claims in §6 are not editorial positions — they are statements whose evidence was tested and found insufficient.

The bean encodes its genetics, its environment, its fermentation history, and its moisture state. It does not encode roast profile, brewing method, or serving conditions. Those belong to later documents. This one ends where heat begins.

-----

## Appendix A — What Happens to These Compounds During Roasting (Reference for the Roast Dossier)

This table falls outside the scope of the Beans dossier — it describes changes that occur during roasting. It is included here only to show how the green-bean compounds connect to the next stage.

|Compound         |What happens during roasting|Notes                                                                                                                      |Status     |
|-----------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|Chlorogenic acids|Roughly 54% are lost        |Break down into smaller phenolic compounds that contribute to bitterness                                                   |PROVISIONAL|
|Trigonelline     |Roughly 7.7% is lost        |Converts to nicotinic acid (vitamin B3) and aromatic pyridine compounds                                                    |PROVISIONAL|
|Caffeine         |Roughly 2.5% is lost        |Very heat-stable; survives roasting almost unchanged                                                                       |FROZEN     |
|Sucrose          |Nearly all is lost          |Breaks down into simpler sugars that then react with amino acids (Maillard reactions) to produce colour, flavour, and aroma|FROZEN     |
|Amino acids      |Variable losses             |Some (serine, cysteine) lose more than half; others (arginine) are completely consumed                                     |PROVISIONAL|

-----

*Dossier v0.3.0 — reviewed under Guardian, Architect, and Scout stances. FROZEN parameters are stable for citation. PROVISIONAL entries await further confirmation. OPEN questions are tracked under CL-2026-016, -017, and -018.*
