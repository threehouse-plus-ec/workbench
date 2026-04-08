# Beans Dossier — “Origin & Material Substrate”

*A reference document on the green (unroasted) coffee bean: what it is, where it comes from, how it is processed, what can be measured about it, and what chemical compounds it contains.*

**Dossier ID:** BEANS-COAST-001  
**Version:** 0.3.2 (release version — final precision pass)  
**Date:** 2026-04-06  
**Parent:** Coffee / Espresso Essay (CL-2026-010)  
**Tier:** T1b (Metrological — where measurement method affects reported values, the method is treated as part of the parameter definition)  
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

Most readers come to coffee with one question already in mind: what is the difference between Arabica and Robusta, and is one really better than the other? The short answer is that they are two distinct biological species with measurably different chemistry. Arabica (*Coffea arabica*) carries more sucrose and less caffeine, develops a wider range of aromatic precursors, and grows best at cool, high elevations. Robusta (*Coffea canephora*) carries roughly twice the caffeine, more bitter compounds (chlorogenic acids), and tolerates hot lowland conditions where Arabica cannot survive. These differences run through every section of this dossier — genetics (§1), where each species can grow (§2), how processing affects them (§3), how they look in physical grading (§4), and what compounds they contain (§5). The longer answer — whether one is “better” — depends entirely on what you mean by better, and the dossier deliberately avoids ranking them. Arabica dominates the specialty market for historical and market reasons that are linked to prevailing sensory preferences; Robusta is increasingly important for climate resilience and is the subject of serious quality-improvement research. Both belong in any honest account of what coffee is.

The document covers five topics, each dealing with a different aspect of the green bean’s identity:

- **§1 Botanical Identity** — what species and variety the bean belongs to.
- **§2 Terroir Envelope** — the growing environment (altitude, climate, soil) and how it shapes the bean.
- **§3 Post-Harvest Processing** — what happens between picking the cherry and exporting the green bean.
- **§4 Physical Metrics** — the measurable physical properties used for grading and quality control.
- **§5 Precursor Chemistry** — the chemical compounds inside the bean that will later produce flavour and aroma during roasting.

These five topics are not arbitrary. They follow the order in which the bean’s identity is formed, and each stage is essentially irreversible: genetics are fixed when the plant is pollinated, growing conditions accumulate over months, processing intervenes after harvest, physical measurements are taken at the point of trade, and chemistry represents the final state of the bean before heat is applied.

Each topic section follows the same structure: (a) declared parameters with status markers, (b) a validity contract explaining when those numbers can and cannot be trusted, (c) open disputes, and (d) notes on how this information connects to later stages (roasting, brewing).

Two cautions for the reader. First, the ranges in this dossier span many origins, varieties, and studies. Any single batch of green coffee will fall within a narrower window. Second, this dossier describes what is *in* the bean, not what ends up *in the cup*. The journey from bean chemistry to taste passes through roasting and brewing — those are covered in separate documents.

**[Synthesis statement, not observation:]** One important finding runs through the entire dossier: current evidence suggests that post-harvest processing does not simply reveal what was already in the bean. It can change the bean’s measurable chemistry through three distinct pathways — by altering the concentrations of compounds the seed already contained, by allowing microbially generated compounds in the surrounding fruit and fermentation environment to be absorbed into or retained by the bean, and by triggering biochemical responses in the still-living seed itself. The relative importance of these pathways, and the magnitude of each, depends on the processing method and is still being studied (see §7, question BW-01).

-----

## 0 — Boundary Condition

**Nothing in this dossier has been roasted.** The moment heat triggers browning reactions (known as Maillard reactions — the same chemistry that browns bread and seared meat) or breaks down compounds through high temperature (pyrolysis), the material belongs to the Roast dossier. Fermentation during processing is included here because it happens before the bean is exported and it shapes the bean’s chemical starting state.

**Not covered here:** roast level, espresso extraction, brew methods, or taste descriptions, except where a direct, experimentally demonstrated link to green-bean composition exists. A reference table for what happens to these compounds during roasting is provided as Interface Sheet I-1, which sits at the boundary between this dossier and the (forthcoming) Roast dossier.

**Scope of invariance.** The parameters in this dossier fall into three categories of stability, and reading them correctly requires keeping the distinction in mind. *Invariant* parameters are fixed properties of the species or genome that do not change between samples (chromosome counts, parentage, polyploidy timing). *Bounded but context-dependent* parameters take a range of values across origins, varieties, and growing conditions, but the range itself is well established (sucrose content, lipid content, typical altitudes). *Process-dependent* parameters vary with how the bean is handled after harvest and cannot be specified without specifying the process (mucilage retention, fermentation microbiology, water activity). The status markers (FROZEN, PROVISIONAL, OPEN, QUARANTINED) describe evidential confidence; this scope-of-invariance distinction describes the kind of stability the parameter can have in principle.

-----

## 1 — Botanical Identity

### Key terms used in this section

- **Species:** The broadest biological grouping. The two species that matter commercially are *Coffea arabica* (Arabica) and *Coffea canephora* (commonly called Robusta).
- **Variety / Cultivar:** A named type within a species. “Variety” usually means a naturally occurring subtype; “cultivar” (short for “cultivated variety”) means one that has been deliberately selected or bred by humans. In the coffee trade, these terms are often used interchangeably.
- **Landrace:** A locally adapted, genetically diverse population — not a single uniform type.
- **Hybrid group:** A family of cultivars created by crossing two different species or varieties.
- **Trade designation:** A commercial label (like “Ethiopian Heirloom”) that may not correspond to a single biological category.

### 1.1 Declared Parameters

|Parameter                       |Value                                                                                                                                                                                                             |Status|Confidence|Source                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|----------|--------------------------------|
|Arabica chromosome count        |44 chromosomes (four copies of each — a “tetraploid,” meaning it has double the usual set)                                                                                                                        |FROZEN|STRONG    |Salojärvi 2024; Scalabrin 2020  |
|Robusta chromosome count        |22 chromosomes (the standard two copies — a “diploid”)                                                                                                                                                            |FROZEN|STRONG    |Multiple concordant             |
|How Arabica originated          |A natural cross between two other species: *C. canephora* (Robusta) and *C. eugenioides*                                                                                                                          |FROZEN|STRONG    |Salojärvi 2024                  |
|When this cross occurred        |350,000–610,000 years ago                                                                                                                                                                                         |FROZEN|STRONG    |Salojärvi 2024 (Nature Genetics)|
|Pollination                     |Arabica is largely self-compatible and predominantly self-pollinating (unusual within the coffee genus, where most species require cross-pollination); Robusta is self-incompatible and requires cross-pollination|FROZEN|STRONG    |WCR; SCA literature             |
|Foundational lineages           |Nearly all cultivated Arabica descends from two groups: Typica and Bourbon                                                                                                                                        |FROZEN|STRONG    |WCR Varieties Catalog (2024)    |
|Genetic diversity in cultivation|Cultivated Arabica retains less than 1% of the genetic diversity (measured as single-nucleotide polymorphism diversity) found in wild Ethiopian populations                                                       |FROZEN|STRONG    |Salojärvi 2024                  |

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

**[Synthesis statement, not observation:]** The most consequential pattern in this table is an interaction, not a single effect. In the Worku et al. (2018) dataset, the relationship between altitude and sucrose depends on how the coffee is processed: in washed beans, sucrose clearly increases with altitude; in naturally processed beans, the effect is not statistically significant. Whether this conditional pattern generalises beyond the Ethiopian samples studied is not yet established, but in the best-controlled dataset currently available it is robust. The implications for the “latent potential” framing of the bean are discussed in §10 and tracked under question BW-05 in §7.

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

The following bacteria and yeasts have been identified as dominant in different fermentation conditions. These are representative findings from selected studies, not universal rules. Each row is anchored to its source study so that the reader can trace the claim:

|Fermentation condition     |Dominant bacteria                                                       |Dominant yeasts                            |Source                                                                 |Status     |
|---------------------------|------------------------------------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------|-----------|
|Washed (underwater)        |*Weissella*, *Leuconostoc*, *Lactiplantibacillus* (lactic acid bacteria)|—                                          |PMC 2025 (review reported via Kimi); cross-referenced in Várady 2022   |PROVISIONAL|
|Semi-anaerobic (low oxygen)|*Acetobacter* (acetic acid bacteria, increased)                         |—                                          |PMC 8172976 (Caparoso region study, via altitude/microbiome literature)|PROVISIONAL|
|Fully anaerobic (no oxygen)|—                                                                       |*Pichia*, *Issatchenkia*, *Wickerhamomyces*|PMC 12427761 (2025 self-induced anaerobic fermentation study, via Kimi)|PROVISIONAL|

**Caution:** All three rows derive from a small number of studies and are reported by one or two of the five research agents. They should not be treated as universal microbial signatures of these processing conditions. Independent replication is needed before promotion to FROZEN.

### 3.3 Validity Contract

- Processing changes the bean’s measurable chemistry, not just its surface coating. The change can occur through three pathways: altered concentrations of compounds already present in the seed, absorption or retention of compounds generated in the surrounding fermentation environment, and biochemical responses in the still-living seed. Current evidence supports detectable but variably quantified incorporation from the fermentation environment; the penetration depth (whether compounds reach the endosperm or remain near the outer layers) and the magnitude relative to endogenous compound pools are not yet well established. This is supported by research from the Specialty Coffee Association and by Várady et al. (2022/2024). The dossier does not currently claim that microbes synthesise new compounds *inside* the bean. The magnitude of change depends on the specific method and conditions.
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

|What is measured              |Target / Range                                                                                                                                                                                    |How it is measured                                                                     |Standard                    |Status|
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------|------|
|Moisture content              |10–12% (specialty target); 9–13% (acceptable under SCA/ICO rules)                                                                                                                                 |Reference: oven-drying at 105 °C (ISO standard 6673). Field: electronic moisture meters|SCA, ICO                    |FROZEN|
|Water activity (aw)           |0.55–0.65 (recommended); below 0.70 for practical storage safety (industry threshold; most spoilage moulds are inhibited below this value, though some xerophilic species can grow slightly lower)|Dedicated water activity meter                                                         |SCA                         |FROZEN|
|Bulk density (Arabica)        |670–750 g/L                                                                                                                                                                                       |Weigh a known volume of beans in a graduated cylinder                                  |Industry practice           |FROZEN|
|Screen size                   |Screens 13–20 (sizes from ~5.2 mm to ~8.0 mm)                                                                                                                                                     |Standardised sieves with round holes                                                   |SCA and regional conventions|FROZEN|
|Defect count (specialty grade)|Zero major defects; no more than 5 minor defects in a 350 g sample                                                                                                                                |Visual inspection under controlled lighting                                            |SCA GACCS                   |FROZEN|

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

### 5.3 Exploratory Correlations (Low Evidential Weight)

*The relationships in this section are presented in tabular form for parallelism with §5.1, but they carry substantially lower evidential weight than the FROZEN ranges above. They should be read as exploratory observations awaiting independent confirmation, not as established relationships.*

All four entries below derive from a single research agent (Kimi) drawing on a small number of secondary sources. They are flagged here for transparency but should be treated as preliminary observations, not established findings. Independent confirmation against primary literature is needed before any of these can be promoted to FROZEN.

|Relationship                                          |Direction                                                                                               |Source basis                                                          |Status                    |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------|
|Fat content ↔ caffeine                                |Beans with more fat tend to have less caffeine                                                          |Single agent (Kimi); secondary review                                 |PROVISIONAL — single agent|
|Fat content ↔ chlorogenic acids, sucrose, trigonelline|Beans with more fat tend to have more of these compounds                                                |Single agent (Kimi); secondary review                                 |PROVISIONAL — single agent|
|Trigonelline ↔ caffeine (in green beans)              |Tend to increase together                                                                               |Single agent (Kimi); secondary review                                 |PROVISIONAL — single agent|
|Caffeine: genetic vs environmental                    |Roughly 94% of a bean’s caffeine level is attributed to species genetics rather than growing environment|Single agent (Kimi); originally Ky et al. 2001 plus subsequent reviews|PROVISIONAL — single agent|

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

The register distinguishes two types of problematic claim. **Type A** claims make a causal or factual assertion that the evidence does not support. **Type B** claims are market or evaluative language whose meaning depends on the metric of “quality” being used. Both types appear frequently in coffee discourse, but they require different responses: Type A is testable and can in principle be resolved by evidence; Type B is partly sociological and can only be addressed by clarifying what “quality” means in a given context.

### Type A — Unsupported causal or factual claims

|ID   |The claim                                                |Why it is problematic                                                                                                                                                                                                                                                         |Status                    |
|-----|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
|AC-01|“Ethiopian coffee = fruity”                              |An oversimplified shorthand, not a causal relationship. Ethiopia has >10,000 varieties grown across diverse conditions.                                                                                                                                                       |ACTIVE                    |
|AC-02|“Higher altitude = better coffee”                        |A correlation that masks complex interactions with temperature, shade, variety, and processing method                                                                                                                                                                         |ACTIVE                    |
|AC-03|“Natural process = more flavour”                         |Confuses the processing method with the many fermentation variables within it                                                                                                                                                                                                 |ACTIVE                    |
|AC-05|“Older beans are stale”                                  |Oversimplifies; deliberately aged coffees are a recognised category                                                                                                                                                                                                           |ACTIVE                    |
|AC-06|“Processing merely reveals what is already in the bean”  |Evidence shows processing can change the bean’s measurable chemistry through several distinct pathways (altered concentrations of native compounds, absorption from the fermentation environment, biochemical responses in the living seed). The extent depends on the method.|ACTIVE — EVIDENCE CONTRARY|
|AC-09|“Volcanic soils inherently produce higher quality coffee”|Frequently claimed, but controlled experiments isolating soil type from other variables are rare                                                                                                                                                                              |ACTIVE                    |
|AC-10|“Bigger beans = better coffee”                           |Screen size measures uniformity (important for even roasting), not flavour quality                                                                                                                                                                                            |ACTIVE                    |

### Type B — Market language and evaluative framing

|ID   |The claim                                 |Why it is problematic                                                                                                                                                                |Status|
|-----|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
|AC-04|“Single-origin guarantees quality”        |“Quality” here is a market category, not a measurable property. Single-origin lots can be excellent or mediocre; the label is about traceability, not analytical merit.              |ACTIVE|
|AC-07|“Gesha quality is intrinsic and universal”|Conflates the variety’s genetic potential with the growing and processing conditions needed to express it. The “intrinsic quality” framing is partly market-driven.                  |ACTIVE|
|AC-08|“Washed = higher quality”                 |A bias toward one processing method, partly historical and partly market-driven. Not supported as a universal rule, but the underlying preference is real and shapes specialty trade.|ACTIVE|

-----

## 7 — Open Questions

*These are questions raised during the research and review process that could not be fully answered. Three have been assigned formal tracking numbers for future investigation.*

|ID   |Question                                                                                                                                                       |Tracking number|Status         |Current best answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|BW-01|Does processing create new compounds in the bean, or does it only select from what was already there?                                                          |CL-2026-016    |UNDERDETERMINED|Processing acts through at least three distinct pathways: (1) altering concentrations of compounds already present in the seed at harvest; (2) generating compounds in the surrounding fermentation environment that are then absorbed into or retained by the bean; (3) triggering biochemical responses in the still-living seed during the stress of fermentation and drying. The dossier does not currently claim that microbes synthesise compounds *inside* the bean. The relative magnitude of these three pathways depends on the processing method — anaerobic and inoculated processes appear to involve more of pathways (2) and (3) than traditional washed processing. This is a graded answer, not a binary one.|
|BW-02|Is the SCA defect grading sample 300 g or 350 g?                                                                                                               |—              |RESOLVED       |350 g, per the current SCA standard (2023/2024). The 300 g figure comes from older international standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|BW-03|When did the Arabica species originate — 10,000–50,000 years ago or 350,000–610,000 years ago?                                                                 |—              |RESOLVED       |350,000–610,000 years ago (Salojärvi et al. 2024, Nature Genetics). The shorter timeframe, from one research agent, is not supported by the primary literature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|BW-04|Can specific green-bean compounds be reliably mapped to specific roasted-coffee aromas?                                                                        |CL-2026-017    |OPEN           |Not yet. No complete mapping exists. This is a genuine research gap.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|BW-05|If sucrose accumulation with altitude depends on processing method (Worku 2018), what does this mean for the idea that the bean has a fixed “latent potential”?|CL-2026-018    |OPEN           |It means the “latent potential” idea works for genetics and growing conditions but breaks down at the processing stage. Processing does not just reveal what the environment put there — it determines whether the environment’s contribution is expressed at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

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
- v0.2.0 (2026-04-06): Added status markers to all parameters; moved roasting-loss data to a separate section; standardised section structure; tightened language.
- v0.3.0 (2026-04-06): Incorporated review from Architect and Scout stances; resolved two open questions (sample size: 350 g; polyploidy timing: 350–610 kya); assigned tracking numbers to three remaining open questions; updated anti-claim AC-06 status; added tier designation; rewrote for accessibility (plain language, definitions, reduced jargon); added Arabica vs Robusta framing in introduction; added consolidated reference list (§11).
- v0.3.1 (2026-04-06): Council precision pass — sharpened BW-01 and processing-related language to distinguish three mechanistic pathways (concentration changes, environmental absorption, seed biochemistry) and explicitly disclaimed in-bean microbial synthesis; labelled interpretive synthesis statements in introduction, §2.2, and §10; subdivided anti-claims register into Type A (causal/factual) and Type B (market/evaluative) categories; added source anchors to §3.2 microbial table and §5.3 correlation table; softened biological phrasings (pollination, market dominance, portable spectroscopy); relabelled Appendix A as Interface Sheet I-1 to remove the controlled scope breach.
- v0.3.2 (2026-04-06): Final precision pass — added mass-balance and penetration-depth caveat to absorption pathway in §3.3; qualified Worku 2018 generalisation in introduction, §2.2, and §10 (“in the best-controlled dataset currently available”); marked §5.3 as “Exploratory Correlations (Low Evidential Weight)” with explicit reader caution; softened water activity threshold to acknowledge xerophilic species; clarified the <1% diversity figure as SNP diversity relative to wild Ethiopian populations; added roast-degree-dependence caveat to Interface Sheet I-1; added “Scope of invariance” statement to §0 distinguishing invariant / bounded / process-dependent parameters; strengthened metrological identity in tier line (measurement method as part of parameter definition); added Roast-dossier forward hook to closing line (non-volatile precursors → volatile aromatics).

-----

## 10 — Conclusion: What the Bean Encodes

*This section is interpretive synthesis, not measured content. It draws conclusions from the parameters and disputes documented in §1–§7. Readers who want only the verified facts should stop at §9.*

The green coffee bean arrives at the roaster as a finished biological object. Its genetic blueprint was fixed hundreds of thousands of years ago by a single cross between two wild species. Its density, sugar content, and acid balance were shaped over months of growth under specific conditions of altitude, temperature, rainfall, and shade. Its microbial history was determined during fermentation and drying. By the time it reaches a grading table, it carries a precise chemical inventory — one that sets the upper limit of what any roast or brew can extract from it.

Three findings from this review deserve emphasis.

First, Arabica’s genetic narrowness is a structural vulnerability, not a footnote. Cultivated Arabica retains less than 1% of the diversity found in wild populations. Every variety in the specialty market traces back to the same Bourbon–Typica bottleneck. The species’ future under climate pressure depends on wild material that currently sits in Ethiopian forests and gene banks, not in commercial plantations.

Second, the most important quantitative finding in the environmental literature is an interaction, not a simple trend: in the best-controlled dataset currently available (Worku et al. 2018), sucrose accumulation with altitude is statistically significant in washed beans but not in naturally processed ones. Whether this conditional relationship generalises to other origins, varieties, and growing systems remains an open question, but it is sufficient to motivate the broader claim that growing environment and processing are not independent factors — they are coupled. The popular idea that the bean contains a fixed “latent potential” that processing merely reveals is useful but incomplete. Processing does not just expose what altitude deposited; it determines whether altitude’s contribution is expressed at all.

Third, the gap between what can be measured and what is routinely measured remains large. Laboratory instruments can quantify chlorogenic acids, caffeine, trigonelline, and sucrose with high precision. Water activity meters can predict storage safety better than moisture content alone. Portable near-infrared spectroscopy is being developed for rapid non-destructive screening of several compounds, though field-level accuracy varies by analyte and is still a subject of active research. Yet most green coffee in trade is still graded primarily by visual defect count and moisture percentage — metrics that capture only a fraction of the bean’s actual state.

This dossier does not claim to be complete. It records the state of knowledge as of April 2026, drawn from five independent research agents and cross-checked against scientific papers, standards-body documents, and practitioner expertise. Where sources conflict, the conflict is preserved. Where evidence is weak, it is marked accordingly. The ten anti-claims in §6 are not editorial positions — they are statements whose evidence was tested and found insufficient.

The bean encodes its genetics, its environment, its fermentation history, and its moisture state. It does not encode roast profile, brewing method, or serving conditions. Those belong to later documents — beginning with the Roast dossier, where the central question becomes how non-volatile precursors are transformed into the volatile aromatic compounds that define the cup. This one ends where heat begins.

-----

## 11 — References

*Sources are organised by tier (per §8). Where a digital object identifier (DOI) or stable URL is available, it is provided. Items marked with † were the most heavily relied upon during curation.*

### Tier 1 — Peer-reviewed scientific papers

†Salojärvi, J., Rambani, A., Yu, Z., et al. (2024). The genome and population genomics of allopolyploid *Coffea arabica* reveal the diversification history of modern coffee cultivars. *Nature Genetics*, 56(4), 721–731. doi:10.1038/s41588-024-01695-w

Scalabrin, S., Toniutti, L., Di Gaspero, G., et al. (2020). A single polyploidization event at the origin of the tetraploid genome of *Coffea arabica* is responsible for the extremely low genetic variation in wild and cultivated germplasm. *Scientific Reports*, 10, 4642. doi:10.1038/s41598-020-61216-7

†Worku, M., De Meulenaer, B., Duchateau, L., & Boeckx, P. (2018). Effect of altitude on biochemical composition and quality of green arabica coffee beans can be affected by shade and postharvest processing method. *Food Research International*, 105, 278–285. doi:10.1016/j.foodres.2017.11.016

Caporaso, N., Whitworth, M. B., Grebby, S., & Fisk, I. D. (2018). Non-destructive analysis of sucrose, caffeine and trigonelline on single green coffee beans by hyperspectral imaging. *Food Research International*, 106, 193–203. PMC 5886291

Ky, C.-L., Louarn, J., Dussert, S., Guyot, B., Hamon, S., & Noirot, M. (2001). Caffeine, trigonelline, chlorogenic acids and sucrose diversity in wild *Coffea arabica* L. and *C. canephora* P. accessions. *Food Chemistry*, 75(2), 223–230. doi:10.1016/S0308-8146(01)00204-7

Jaiswal, R., Matei, M. F., Ullrich, F., & Kuhnert, N. (2019). Comparison and quantification of chlorogenic acids for differentiation of green Robusta and Arabica coffee beans. *Food Research International*, 124, 56–63. doi:10.1016/j.foodres.2019.01.040

Várady, M., Tauchen, J., Klouček, P., & Popelka, P. (2022). Effect of method of processing specialty coffee beans (natural, washed, honey, fermentation, maceration) on bioactive and volatile compounds. *LWT — Food Science and Technology*, 172, 114245. PubMed 38327481

Sualeh, A., Daba, A., Kiflu, S., & Mohammed, A. (2020). Biochemical composition of green and roasted coffee beans and their association with coffee quality from different districts of southwest Ethiopia. *Heliyon*, 6(12), e05812. PMC 7773871

Bosselmann, A. S., Dons, K., Oberthur, T., Olsen, C. S., Ræbild, A., & Usma, H. (2009). The influence of shade trees on coffee quality in small holder coffee agroforestry systems in Southern Colombia. *Agriculture, Ecosystems & Environment*, 129(1–3), 253–260.

Cassamo, C. T., Draper, D., Romeiras, M. M., et al. (2022). Shade and altitude implications on the physical and chemical attributes of green coffee beans from Gorongosa Mountain, Mozambique. *Agronomy*, 12(10), 2540. doi:10.3390/agronomy12102540

Somporn, C., Kamtuo, A., Theerakulpisut, P., & Siriamornpun, S. (2012). Effects of roasting degree on radical scavenging activity, phenolics and volatile compounds of arabica coffee beans (*Coffea arabica* L. cv. Catimor). *International Journal of Food Science & Technology*, 47(11), 2287–2294. PubMed 22252511

Tolessa, K., D’heer, J., Duchateau, L., & Boeckx, P. (2017). Influence of growing altitude, shade and harvest period on quality and biochemical composition of Ethiopian specialty coffee. *Journal of the Science of Food and Agriculture*, 97(9), 2849–2857. doi:10.1002/jsfa.10594

Berny Mier y Teran, J. C., Bertrand, B., Marraccini, P., et al. (2025). Global field trials of Arabica coffee varieties under contrasting environments. *Frontiers in Plant Science*, 16. doi:10.3389/fpls.2025.1583595

Fenrich, C. R., et al. (2023). Proteomic analysis of higher and lower altitude cultivars of *Coffea arabica*. *Eureka*. doi:10.29173/eureka28796

Aragón-Guzmán, E., et al. (2024). Systematic review of environmental drivers of green coffee quality. *Frontiers in Sustainable Food Systems*. doi:10.3389/fsufs.2024.1386956

Williams, P. R. D., et al. (2022). Does coffee have terroir and how should it be assessed? *Foods*. PMC 9265435

Clifford, M. N. (1985). Chemical and physical aspects of green coffee and coffee products. In M. N. Clifford & K. C. Willson (Eds.), *Coffee: Botany, Biochemistry and Production of Beans and Beverage* (pp. 305–374). Croom Helm.

### Tier 2 — Standards bodies

Specialty Coffee Association (SCA). (2023/2024). *Green Arabica Coffee Classification System (GACCS)*. SCA Coffee Standards. Available at: https://sca.coffee/research/coffee-standards

International Organisation for Standardisation. (2003). *ISO 6673:2003 — Green coffee: Determination of loss in mass at 105 °C*. Geneva: ISO. Available at: https://www.iso.org/standard/38375.html

International Coffee Organization (ICO). (2010). *National quality standards for green coffee* (Document ED 1918). Available at: https://www.ico.org/documents/ed1918e.pdf

Specialty Coffee Association. (2018, 2025). *Coffee Standards*. Periodically updated reference document covering moisture, water activity, and grading.

### Tier 3 — Research institutions

World Coffee Research. (2024). *Arabica Coffee Varieties Catalog* (4th edition). Available at: https://varieties.worldcoffeeresearch.org/

World Coffee Research. *Coffea arabica Genome*. Project page and data resource. Available at: https://worldcoffeeresearch.org/resources/coffea-arabica-genome

CIRAD (Centre de coopération internationale en recherche agronomique pour le développement). (2024). The genomes of Arabica coffee and its parents finally deciphered. Press release and project documentation.

Coffee Science Foundation. (2024). Research grants and publications on green coffee defects, sensory evaluation, and processing chemistry. Available via the Specialty Coffee Association.

Food and Agriculture Organization of the United Nations. *Annex 7: Green Coffee Classification and Grading*. Available at: https://www.fao.org/4/x6939e/x6939e13.htm

### Tier 4 — Scientific books

Illy, A., & Viani, R. (Eds.). (2005). *Espresso Coffee: The Science of Quality* (2nd ed.). Elsevier Academic Press.

Flament, I. (2001). *Coffee Flavor Chemistry*. John Wiley & Sons.

Hoffmann, J. (2018). *The World Atlas of Coffee* (2nd ed.). Mitchell Beazley.

Rao, S. (2014). *The Coffee Roaster’s Companion*. Self-published.

Wellman, F. L. (1961). *Coffee: Botany, Cultivation and Utilization*. Leonard Hill Books.

### Tier 5 — Industry and practitioner sources

Specialty Coffee Association. (2018, ongoing). *25 Magazine*, Issues 10 and 24. Articles on fermentation effects and green-grading sensory science. Available at: https://sca.coffee/sca-news/25

Cropster. (2020). *Master Green Grading: A Coffee Roaster’s Guide*. Available at: https://www.cropster.com/blog-post/green-grading-coffee/

Roast Magazine. (2025). Beyond Elevation: How Bean Density Informs Roasting and Flavor. Available at: https://www.roastmagazine.com/stories/beyond-elevation

Royal Coffee. (2016). Green Coffee Analytics, Part I: Moisture Content and Total Water. Available at: https://royalcoffee.com/

Barista Hustle. (2023). *Roasting Science 2.03: Density and Porosity*. Online educational module.

Green Coffee Collective. *Physical Measurements of Green Coffee*. Available at: https://greencoffeecollective.com/blogs/learn/

### Note on sources excluded from this list

The C. stenophylla genetic study reported by one research agent (Gemini) could not be independently verified against the cited DOI (10.3389/fgene.2025.1554029) and is excluded from this reference list. The “Kona Typica genome 2024” entry (PRJCA043259) is held as PROVISIONAL and is not yet given a full citation pending verification of the publication associated with the BioProject accession number.

-----

## Interface Sheet I-1 — Handoff to the Roast Dossier

*This is not part of the Beans dossier. It is an interface document that exists at the boundary between Beans and Roast, included here for the convenience of readers who need to follow the chemistry across the boundary. The content describes what happens during roasting and therefore lies outside the Beans boundary condition (§0). When the Roast dossier exists, this material will live there and be referenced from here rather than reproduced.*

**Important caveat:** All loss percentages below are scalar approximations that depend strongly on roast degree and on the specific time–temperature profile used. A light roast and a dark roast can produce loss values that differ by a factor of two or more for some compounds. The values shown represent typical mid-range outcomes for medium roasts in conventional drum roasters. They should not be applied uncritically to other roast profiles.

|Compound         |What happens during roasting                                              |Notes                                                                                                                      |Status     |
|-----------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|Chlorogenic acids|Roughly 54% are lost (medium roast; range varies widely with roast degree)|Break down into smaller phenolic compounds that contribute to bitterness                                                   |PROVISIONAL|
|Trigonelline     |Roughly 7.7% is lost (medium roast)                                       |Converts to nicotinic acid (vitamin B3) and aromatic pyridine compounds                                                    |PROVISIONAL|
|Caffeine         |Roughly 2.5% is lost                                                      |Very heat-stable; survives roasting almost unchanged                                                                       |FROZEN     |
|Sucrose          |Nearly all is lost                                                        |Breaks down into simpler sugars that then react with amino acids (Maillard reactions) to produce colour, flavour, and aroma|FROZEN     |
|Amino acids      |Variable losses (depend on roast degree and individual amino acid)        |Some (serine, cysteine) lose more than half; others (arginine) are largely consumed at darker roasts                       |PROVISIONAL|

-----

*Dossier v0.3.2 — reviewed under Guardian, Architect, and Scout stances. FROZEN parameters are stable for citation. PROVISIONAL entries await further confirmation. OPEN questions are tracked under CL-2026-016, -017, and -018.*
