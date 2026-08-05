![](Documents/converted/media/image1.png){width="1.6136417322834646in" height="0.5613998250218722in"}

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **DESIGN BIBLE**                                                                                                                                                       |
+========================================================================================================================================================================+
| **Index**                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [1. General design rules [4](#general-design-rules)](#general-design-rules)                                                                                            |
|                                                                                                                                                                        |
| [1.1. Guidelines for a good design [4](#guidelines-for-a-good-design)](#guidelines-for-a-good-design)                                                                  |
|                                                                                                                                                                        |
| [1.2. Build-up structure in Windchill/CEDM and names [5](#build-up-structure-in-windchillcedm-and-names)](#build-up-structure-in-windchillcedm-and-names)              |
|                                                                                                                                                                        |
| [Main file and zones [5](#main-file-and-zones)](#main-file-and-zones)                                                                                                  |
|                                                                                                                                                                        |
| [Machines and components [6](#machines-and-components)](#machines-and-components)                                                                                      |
|                                                                                                                                                                        |
| [Structure of a machine: [7](#structure-of-a-machine)](#structure-of-a-machine)                                                                                        |
|                                                                                                                                                                        |
| [Spare parts [8](#spare-parts)](#spare-parts)                                                                                                                          |
|                                                                                                                                                                        |
| [1.3. Corrupt parts and how to solve them [9](#corrupt-parts-and-how-to-solve-them)](#corrupt-parts-and-how-to-solve-them)                                             |
|                                                                                                                                                                        |
| [How to detect a corrupted part [9](#how-to-detect-a-corrupted-part)](#how-to-detect-a-corrupted-part)                                                                 |
|                                                                                                                                                                        |
| [Recommended types of files [11](#recommended-types-of-files)](#recommended-types-of-files)                                                                            |
|                                                                                                                                                                        |
| [Common problems [12](#common-problems)](#common-problems)                                                                                                             |
|                                                                                                                                                                        |
| [Simplification [18](#simplification)](#simplification)                                                                                                                |
|                                                                                                                                                                        |
| [Healing step by step [21](#healing-step-by-step)](#healing-step-by-step)                                                                                              |
|                                                                                                                                                                        |
| [2. Bolt connections [22](#bolt-connections)](#bolt-connections)                                                                                                       |
|                                                                                                                                                                        |
| [2.1. General rules [22](#general-rules)](#general-rules)                                                                                                              |
|                                                                                                                                                                        |
| [2.2. Fastener type [22](#_Toc165532431)](#_Toc165532431)                                                                                                              |
|                                                                                                                                                                        |
| [2.3. Choice of correct bolt length [23](#choice-of-correct-bolt-length)](#choice-of-correct-bolt-length)                                                              |
|                                                                                                                                                                        |
| [3. Hole / slot dimensions [24](#hole-slot-dimensions)](#hole-slot-dimensions)                                                                                         |
|                                                                                                                                                                        |
| [4. Structure and platform information [24](#structure-and-platform-information)](#structure-and-platform-information)                                                 |
|                                                                                                                                                                        |
| [4.1. General rules [24](#general-rules-1)](#general-rules-1)                                                                                                          |
|                                                                                                                                                                        |
| [4.2. Fasteners size [26](#fasteners-size)](#fasteners-size)                                                                                                           |
|                                                                                                                                                                        |
| [4.3. ID numbering in WA en parts [27](#id-numbering-in-wa-en-parts)](#id-numbering-in-wa-en-parts)                                                                    |
|                                                                                                                                                                        |
| [4.4. Profile information [28](#profile-information)](#profile-information)                                                                                            |
|                                                                                                                                                                        |
| [4.5. Chemical anchor information [29](#chemical-anchor-information)](#chemical-anchor-information)                                                                    |
|                                                                                                                                                                        |
| [4.6. Mechanical anchor information [30](#mechanical-anchor-information)](#mechanical-anchor-information)                                                              |
|                                                                                                                                                                        |
| [4.7. Boplan information [31](#boplan-information)](#boplan-information)                                                                                               |
|                                                                                                                                                                        |
| [5. Mounting machine(parts) on structures [32](#mounting-machineparts-on-structures)](#mounting-machineparts-on-structures)                                            |
|                                                                                                                                                                        |
| [6. Sheet metal information [33](#sheet-metal-information)](#sheet-metal-information)                                                                                  |
|                                                                                                                                                                        |
| [6.1. K-factor Bending [33](#k-factor-bending)](#k-factor-bending)                                                                                                     |
|                                                                                                                                                                        |
| [6.2. Minimum bend radius HARDOX 400 [34](#minimum-bend-radius-hardox-400)](#minimum-bend-radius-hardox-400)                                                           |
|                                                                                                                                                                        |
| [7. Info LaserCut [35](#info-lasercut)](#info-lasercut)                                                                                                                |
|                                                                                                                                                                        |
| [7.1. Tolerances on dimensions [35](#tolerances-on-dimensions)](#tolerances-on-dimensions)                                                                             |
|                                                                                                                                                                        |
| [8. Info Saw Work SW [35](#info-saw-work-sw)](#info-saw-work-sw)                                                                                                       |
|                                                                                                                                                                        |
| [9. Database agreements [35](#database-agreements)](#database-agreements)                                                                                              |
|                                                                                                                                                                        |
| [9.1. Material color [35](#material-color)](#material-color)                                                                                                           |
|                                                                                                                                                                        |
| [10. Welding [37](#welding)](#welding)                                                                                                                                 |
|                                                                                                                                                                        |
| [10.1. Norm [37](#norm)](#norm)                                                                                                                                        |
|                                                                                                                                                                        |
| [10.2. Elementary welding symbols and how to use them [38](#elementary-welding-symbols-and-how-to-use-them)](#elementary-welding-symbols-and-how-to-use-them)          |
|                                                                                                                                                                        |
| [10.3. Supplementary welding symbols and how to use them [42](#supplementary-welding-symbols-and-how-to-use-them)](#supplementary-welding-symbols-and-how-to-use-them) |
|                                                                                                                                                                        |
| [10.4. Arrow placement and information [45](#arrow-placement-and-information)](#arrow-placement-and-information)                                                       |
|                                                                                                                                                                        |
| [10.5. Additional information on welding symbols [46](#additional-information-on-welding-symbols)](#additional-information-on-welding-symbols)                         |
|                                                                                                                                                                        |
| [10.6. Weld size indication [47](#weld-size-indication)](#weld-size-indication)                                                                                        |
|                                                                                                                                                                        |
| [11. Platforms (to be updated) [48](#platforms-to-be-updated)](#platforms-to-be-updated)                                                                               |
|                                                                                                                                                                        |
| [12. Geared motors (Siemens) [49](#geared-motors-siemens)](#geared-motors-siemens)                                                                                     |
|                                                                                                                                                                        |
| [12.1. Siemens Mall: Select the correct Mains voltage [49](#siemens-mall-select-the-correct-mains-voltage)](#siemens-mall-select-the-correct-mains-voltage)            |
|                                                                                                                                                                        |
| [12.2. Siemens Mall : how to select file type SAT [49](#siemens-mall-how-to-select-file-type-sat)](#siemens-mall-how-to-select-file-type-sat)                          |
|                                                                                                                                                                        |
| [13. Classification [50](#classification)](#classification)                                                                                                            |
|                                                                                                                                                                        |
| [13.1. Classification checkbox [50](#classification-checkbox)](#classification-checkbox)                                                                               |
|                                                                                                                                                                        |
| [13.2. Approval planning [50](#approval-planning)](#approval-planning)                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                 |
+====================+====================+====================+==================================================================+
| **Document history**                                                                                                            |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| **Revision**       | **Date**           | **User**           | **Description**                                                  |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| A.1                |                    | JED                | Original                                                         |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.1                | 22/04/2020         | JED                | Name change + update                                             |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.2                | 29/09/2020         | JED                | Update structure and platform information + database agreements  |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.3                | 18/04/2023         | JCV                | Attached classification checkbox                                 |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.4                | 26/06/2023         | JCV                | Corrupt parts and how to solve them                              |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
|                    | 22/09/2023         | WMD                | Info Saw Work                                                    |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.5                | 22/11/2023         | JCV                | Update on welding                                                |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.6                | 15/01/2024         | OCV                | Update of chapter Build-up structure in Windchill/CEDM and names |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.7                | 02/05/2024         | OCV                | Update of chapter welding - clarification                        |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
| B.8                | 27/03/2025         | JCV                | Norms on electrics                                               |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+
|                    |                    |                    |                                                                  |
+--------------------+--------------------+--------------------+------------------------------------------------------------------+

**\**

# General design rules

## Guidelines for a good design

1.  Know what the customer wants by reviewing the quote, sales contract, mind reading , and current technology.

2.  Make sure your design fulfils all requested functions and explore alternative or cheaper designs.

3.  Consider the manufacturing process and use standardization and other resources to optimize production.

4.  Make your design user-friendly and easy to operate.

5.  Ensure your design is safe for users, bystanders, and the environment by following relevant safety regulations.

6.  Account for transportation constraints, such as weight and size limitations, during design.

7.  Make sure your design is serviceable with easy-to-access parts for repair, inspection, and adjustment.

8.  Choose the best fabrication method and material for each component.

9.  Use reliable and readily available commercial components.

10. Allow sufficient clearance between moving parts.

11. Use different materials for sliding components that are exposed to dirt and dust.

12. Lubricate moving parts carefully.

13. Avoid intricate and complex welded assemblies.

14. Provide adequate access and visibility for the welder.

15. Choose the best welding technique for the job.

16. Consider corrosion protection and surface finishes.

17. Create clear and organized plans that leave nothing to chance, with sufficient tolerances and instructions for future reference.

18. Mark necessary measurements in a rational manner.

19. Choose an appropriate paper size for your design drawings.

20. Create a logbook or file with calculations, supplier advice, reports, feedback, and other relevant information about your design.

## Build-up structure in Windchill/CEDM and names

The General rule is that the build-up and naming of the machines and assemblies follow the P&ID and machines list.

### Main file and zones

In the P&ID, the installation is divided in zones. This is the first level of the structure in CEDM\
From this example of P&ID:\
![Une image contenant texte, capture d'écran, circuit Description générée automatiquement](Documents/converted/media/image2.png){width="5.90625in" height="3.3548950131233597in"}

Structure CEDM is:\
![Une image contenant texte, capture d'écran, Police, nombre Description générée automatiquement](Documents/converted/media/image3.png){width="3.3541666666666665in" height="1.7224103237095363in"}

In detail :

- The main assembly name is composed of the project code "AGYY-00X" followed by "-00".

  - YY is the 2 last digits of the year of creation of the project;

  - "X" is an iterative number;

  - The project code is defined by AXAPTA.

- 00_Customer scope : this assembly groups all existing, or to be built, constructions on the project area at customer's site. As examples :

  - Building, concrete boxes,...

  - Electricity, water, compressed air connections,...

  - Machines that are not in ADREM's scope

  - Bins, containers, consumables and any other utilities required by the installation

- All zones, organized following the process of material, then other processes and finally general topics:

  - 01 F2 FEEDING until 03 S5-SEPARATOR 0.87 is the process of material

  - 04 M2 MEDIUM TREATMENT is a separate process

  - 05 PUMPS AND PIPING and 06 Electrical Devices are general topics

  - **The names of the zones are the ones from the P&ID!**

**Note : all assemblies for zones and general topics have to be toggled Gathering Parts.**

### Machines and components

In each zone, the structure follows the flow of the material. In case of split of the flow, we first follow the heavy fraction (sinking in a separation bath) and then the light one (floating).\
![Une image contenant texte, capture d'écran, diagramme, Logiciel de graphisme Description générée automatiquement](Documents/converted/media/image4.png){width="6.354166666666667in" height="3.0483464566929133in"}\
![Window](Documents/converted/media/image5.png){width="4.11515748031496in" height="1.9690244969378827in"}

The general rule for naming is: AAA BBB -- CCC - AGYY-00X-ZZ

> \[011 F2-DV1 -- diverter valve 1 -- AG23-00X-03\]

- AAA: is an iterative number in the zone (to sort according the process flow) \[011\]

- BBB: is the ID of the machine \[F2-DV1\]

- CCC: is the machine name \[diverter valve\]

- AGYY-00X-ZZ: is the subcode under which the part will be ordered \[AG23-00X-03\]

**Note : all assemblies for machines can't be toggled Gathering Parts.**

The machine codes are defined in the P&ID and in the machines' list.

It is possible to group machines together under 1 assembly:

![Une image contenant texte, capture d'écran, Police, ligne Description générée automatiquement](Documents/converted/media/image6.png){width="3.4171434820647417in" height="0.5625787401574803in"}

In this case, the assembly that groups the machines is toggled gathering part and the name doesn't contain any subproject code.

The name of the assemblies for machines include the related subproject codes and can't be toggled gathering parts.

**Note : keep in mind that only the assemblies including a subproject code will be set in AXAPTA.**

**That means for example that grouping 2 machines with the same subproject code is a nonsense.**

### Structure of a machine:

![Afbeelding met tekst, schermopname, nummer, Lettertype Automatisch gegenereerde beschrijving](Documents/converted/media/image7.png){width="3.8968657042869643in" height="1.5302198162729659in"}A machine must contain all the parts needed to load separately as a whole.\
For example, the wash drum assembly must contain the following:\
- the structure\
- the platforms\
- the safety grids\
- the parts themselves :\
- the drum\
- the drive\
- the injector\
- the funnels,\
- \...

a)  The structure of a machine is build up as followed:\
    The top assembly is as described in the previous Alinea and is marked as Gathering Part\
    If there are parts that need to be ordered in an other sub-project, the name of the top assembly is without an AG code.\
    The assemblies that need to be ordered in another sub project, have in the end of their name the subproject code. These assemblies must be used to explode in AX to retrieve the needs.

b)  All other assemblies will have the following name CC_DDD

- CC is :

  - FA = functional assembly

  - WA = weld assembly

  - BA = bolt assembly

- DDD is the name of the part

c)  Bolts in the machine structure

- Each part or assembly that is mounted in a Bold Assembly (BA) should be put in an Functional Assembly (FA) together with the fasteners needed to submount the part or assembly.\
  The FA is marked as Gathering Part.

[Example 1]{.underline} :\
\
![](Documents/converted/media/image8.png){width="6.043155074365704in" height="1.5166218285214348in"}\
\
[Example 2]{.underline} :\
\
![Afbeelding met tekst, schermopname, lijn, Parallel Automatisch gegenereerde beschrijving](Documents/converted/media/image9.png){width="5.587911198600175in" height="1.5651334208223973in"}

### Spare parts

When a third party component is used in the project then the spare parts for the colmponents should be added in the assembly. The spare parts need to be placed in a container with the name "SPARE_PARTS" which is set to no scan.

## Corrupt parts and how to solve them

Nowadays, we can load many kinds of 3D models into our drawing program.\
But many models coming from suppliers are drawn on a different program and have different resolution. That sometimes can cause problems.\
These models are corrupted and can have a big impact for loading, saving and adapting the drawing in 3D and 2D.\
In most cases the system will try to solve these parts by calculating the surfaces, but when there are a lot of corrupt parts, the system can't handle the process and goes into time-out and stop loading the package. Surely, this requires some attention.\
Below you can find a roadmap for dealing with corrupted parts.

### How to detect a corrupted part 

- **Visual inspection**\
  \
  When loading a part, it's mostly visible that the part is corrupt via the labels or cyan coloured faces or edges.

![Afbeelding met Auto-onderdeel, cirkel, connector Automatisch gegenereerde beschrijving](Documents/converted/media/image10.png){width="3.0188681102362205in" height="2.350670384951881in"}

> Transparent faces can also be a indication of face parts that can cause corruption.

![Afbeelding met Auto-onderdeel, Huishoudelijke ijzerwaren, gereedschap, hendel Automatisch gegenereerde beschrijving](Documents/converted/media/image11.png){width="3.1752734033245846in" height="2.3622047244094486in"}

- ![](Documents/converted/media/image12.png){width="0.41672462817147854in" height="0.729268372703412in"}**Function 'Check Part'\
  \
  \**
  Sometimes it's less visually obvious that the part is corrupt and that's why we should [always perform a 'check part' on any imported cad file]{.mark}.\
  ![Afbeelding met tekst, schermopname, Lettertype, software Automatisch gegenereerde beschrijving](Documents/converted/media/image13.png){width="4.527083333333334in" height="1.8298611111111112in"}\
  \
  \
  \
  \
  \
  \
  \
  \
  \
  \
  ![images.kkeu.de/is/image/BEG/Veiligheidsborden_e\...](Documents/converted/media/image14.jpeg){width="0.6041666666666666in" height="0.6041666666666666in"}[Big files will take a long time to check.]{.mark}\
  If the file contain too much detail, please start with the simplification of the part as explained under chapter 'Simplification' page 20.\
  \
  By selecting the object and performing a Maximal check, the system will check the part on corruption.\
  \
  ![Afbeelding met tekst, hendel, metaalwaren Automatisch gegenereerde beschrijving](Documents/converted/media/image15.png){width="3.915094050743657in" height="2.578989501312336in"}\
  \
  Make sure to keep the 'labels' checked on to view where the problem occurs.\
  ![Afbeelding met tekst, gereedschap, hendel, sleutel Automatisch gegenereerde beschrijving](Documents/converted/media/image16.png){width="4.415094050743657in" height="1.877584208223972in"}

> In some cases the function will also heal the part.\
> If you get following remark when checking a part, the system is working on a fix for it and advises to check it again.\
> ![Afbeelding met tekst, schermopname, nummer, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image17.png){width="4.26415135608049in" height="2.3924748468941384in"}\
> If you check it again, you might get lucky and the system has successfully healed it.\
> ![Afbeelding met tekst, sleutel, schermopname, gereedschap Automatisch gegenereerde beschrijving](Documents/converted/media/image18.png){width="3.3962259405074366in" height="2.056307961504812in"}

### Recommended types of files 

According the situation, you should opt for these file types:

- ![images.kkeu.de/is/image/BEG/Veiligheidsborden_e\...](Documents/converted/media/image14.jpeg){width="0.6041666666666666in" height="0.6041666666666666in"}**LSP** or **PKG** ![](Documents/converted/media/image19.png){width="3.1458333333333335in" height="0.20833333333333334in"}\
  \
  The main advantage of a LSP file is, that it's build in modelling, so there is a low probability of corruption. Even colours and part weight are correct straight from the box.\
  \
  A disadvantage using this type of file is, that you need to make a copy before saving it. In case people forget, the system will lock this part and makes it impossible to make any adjustments, like changing the part name.

- **STEP** ![](Documents/converted/media/image20.png){width="3.2083333333333335in" height="0.21875in"}**\
  \**
  Step files are commonly available, but aren't the best option for our drawing program.\
  \
  When loading step files, always perform a check part. In most cases the part will be ok.\
  In case the parts contains errors, it still might be solvable.\
  If it contains to much errors, switch to the next file type.

> It can help to adjust the settings in modelling when loading a step file like this:
>
> ![Afbeelding met tekst, elektronica, schermopname, software Automatisch gegenereerde beschrijving](Documents/converted/media/image21.png){width="1.9397528433945757in" height="1.9397528433945757in"} ![Afbeelding met tekst, schermopname, nummer, Lettertype Automatisch gegenereerde beschrijving](Documents/converted/media/image22.png){width="1.0203248031496064in" height="1.9297462817147857in"}**\**

- ![](Documents/converted/media/image23.png){width="2.9375in" height="0.4479166666666667in"}**SAT** or **IGES**

> Sat and Iges files are also commonly available, but have the big disadvantage that they don't have a build up structure and just place all parts under the structure browser without an assembly.\
> It\'s advised to also start with a check part and see if the part is ok or not.

Depending on the situation, some parts will be better in step and then some will be better in sat.\
Feel free to even make combinations of good parts from different files to make an assembly.

### Common problems 

- **RESOLUTION**

> Most problems occur when the resolution of the part is too low.\
> To be consulted under following tab:

![Afbeelding met tekst, schermopname, scherm, software Automatisch gegenereerde beschrijving](Documents/converted/media/image24.png){width="2.5283016185476814in" height="2.2350853018372705in"}

> All parts designed in modelling have a standard resolution of 1.0E-5 mm.\
> If the resolution becomes too large and the part has many rounding's with a radius or ribs smaller than the resolution, modelling errors will be generated.\
> Manually increasing the resolution under part properties isn't possible.
>
> **Common solutions**:

- ![Afbeelding met tekst, schermopname, cirkel, tekenfilm Automatisch gegenereerde beschrijving](Documents/converted/media/image25.png){width="2.1658431758530186in" height="1.7547167541557305in"}![Afbeelding met accessoire, houder, poeder Automatisch gegenereerde beschrijving](Documents/converted/media/image26.png){width="2.26415135608049in" height="1.7814009186351707in"}![Shift Key Stock Photo - Download Image Now - Shift Key, Computer Key, Cut Out - iStock](Documents/converted/media/image27.jpeg){width="0.3298611111111111in" height="0.19791666666666666in"}![What is a Tab?](Documents/converted/media/image28.jpeg){width="0.3125in" height="0.21319444444444444in"}Cut faces\
  \
  By cutting away the faces that give problems, it might be possible to delete the sharp edge that is giving trouble.\
  Just hover over the face and press the 'tab' key until the whole boss or pocket is selected and it's possible to use the 'cut' tool.\
  \
  \
  \
  \
  \
  \
  \
  \
  \
  \
  In some cases it's not possible to use the 'tab' key.\
  Then it's better to keep pressing the 'shift' key and manually select the faces until it's possible to close the loop and use the 'cut' tool.

- Cut logos and details\
  \
  Logos and details like threaded holes are often to sharp for the resolution of the part and will cause corruption.\
  Simply delete it by using the 'cut' tool.

> ![Afbeelding met tekst, schermopname, batterij Automatisch gegenereerde beschrijving](Documents/converted/media/image29.png){width="2.877357830271216in" height="1.8957195975503063in"} ![Afbeelding met ontwerp Beschrijving automatisch gegenereerd met gemiddelde betrouwbaarheid](Documents/converted/media/image30.png){width="1.226415135608049in" height="1.8991918197725284in"}

- Removing edges, rounding's and void shells\
  \
  Sharp edges and rounding's on a part can also cause corruption.\
  It's best to remove them and if you like, you can reapply the bend on the edge.\
  \
  Keep in mind that bend's have a high impact on the details of a part and the file size of it. If it's not necessary, just avoid them.

> ![Afbeelding met ontwerp Beschrijving automatisch gegenereerd met lage betrouwbaarheid](Documents/converted/media/image31.png){width="1.9215146544181978in" height="2.3909930008748908in"} ![Afbeelding met tekst, schermopname, Grafische software, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image32.png){width="2.188678915135608in" height="2.2347583114610674in"}\
> \
> Void shells are small pockets inside the solid of a part, that often are caused by the simplification of the part. Hole clearances for fasteners and plastic flow holes and ribs are an example of this.\
> The can be found by using the 'check part' function and the labels will show their position. Simply cut them away with the 'cut' tool.

- **Too much detail**

> Some models contain too much detail and this requires a lot of calculation to load.\
> If it's not really necessary in a mechanical side of view, delete them.\
> ![Afbeelding met cilinder Automatisch gegenereerde beschrijving](Documents/converted/media/image33.png){width="4.066037839020122in" height="2.054083552055993in"}
>
> ![Afbeelding met ontwerp, batterij Beschrijving automatisch gegenereerd met gemiddelde betrouwbaarheid](Documents/converted/media/image34.png){width="4.218438320209974in" height="2.094339457567804in"}

- ![](Documents/converted/media/image35.png){width="2.8541666666666665in" height="0.17708333333333334in"}**Face parts\**
  Some parts are missing a face and the system can't calculate it to be a solid, this is called a face part. If there are to many faces missing, it's better to try another file type or another solid that is very similar.\
  But sometimes it's solvable via following functions:

  - ![](Documents/converted/media/image36.png){width="0.8333333333333334in" height="0.20833333333333334in"}\
    \
    'Show Gaps' will indicate where a face is missing and indicate them with orange edges.\
    \
    ![Afbeelding met tekst, schermopname, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image37.png){width="3.320754593175853in" height="2.62746719160105in"}

  - ![](Documents/converted/media/image38.png){width="0.8958333333333334in" height="0.21875in"}\
    \
    \
    \
    Sometimes it's advised to delete surfaces that are causing the problems.\
    The 'Delete Face' tool can be used to do delete as many faces required.\
    \
    ![Afbeelding met tekst, schermopname, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image39.png){width="3.26415135608049in" height="2.757186132983377in"}

  - ![](Documents/converted/media/image40.png){width="0.40625in" height="0.7395833333333334in"}\
    \
    \
    With the tool 'Insert Face', you generate a face where we previously deleted it.\
    \
    By pressing the 'shift' key and selecting the edges until you connect a loop where the face is missing.\
    \
    ![Afbeelding met tekst, schermopname, software, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image41.png){width="3.6040157480314963in" height="3.2452832458442695in"}\
    \
    ![Afbeelding met schermopname, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image42.png){width="3.603772965879265in" height="2.5669739720034994in"}

  - ![](Documents/converted/media/image43.png){width="0.5104877515310586in" height="0.6980139982502187in"}\
    \
    \
    \
    \
    \
    \
    \
    Parallel to 'Insert Face', you can use 'Grow Surface' if the complexity of the part allows it.\
    Keep in mind that 'Grow Surface' is a more automated solving tool that will take longer to be calculated by the system and are more prone to fail.\
    In case the part is too complex, it's preferred to manually cut and insert faces where needed.\
    \
    When using the 'Grow Surface' tool, simply select the part.\
    The edges where the face is missing will be indicated in orange.

> ![Afbeelding met schermopname, tekst, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image44.png){width="3.8662959317585304in" height="4.0188681102362205in"}\
> \
> If succeeded, the part will change into a solid instead of a face part.

- **Part corruption to complex to solve\
  \**
  In some cases the part will be too corrupt to solve it.\
  \
  In this case it's better to search for a better CAD file on the databases, or search our own library for a similar part that might be mechanically the same but has other specifications and adapt the name and attributes accordingly.

> Like in this example, we searched the databases for an encoder and found out the model we need is corrupted.\
> After loading different variations of the encoder, we discovered a cad model that's not corrupt and used this as our base model to save in the system and adapted the name to the one we've needed.
>
> ![Afbeelding met schermopname, tekst, diagram, Grafische software Automatisch gegenereerde beschrijving](Documents/converted/media/image45.png){width="5.511811023622047in" height="1.875546806649169in"}\
> \
> If that's not possible, as a last resort, you can always sketch the contours of the part and extrude it so the basic details like mounting hole positions and general size of the part are correct.\
> \
> ![](Documents/converted/media/image46.png){width="4.724409448818897in" height="3.8219181977252843in"}

### Simplification 

- **Removing unnecessary assemblies, face parts and containers\
  \**
  Imported parts can sometimes be stored under a redundant assembly or can contain containers with quilts due to the program it was saved originally.\
  \
  It\'s advised to remove these assemblies and give it an appropriate name.\
  \
  ![Afbeelding met tekst, schermopname, nummer, Lettertype Automatisch gegenereerde beschrijving](Documents/converted/media/image47.png){width="1.952830271216098in" height="1.810518372703412in"}

- **Keep it simple**\
  \
  To keep the library neat, it's better to save a commercial part as simple as possible.\
  \
  Small details like internal electronics or the balls inside of a bearing aren't important for the mechanic installation of the part, so feel free to delete them.

  - ![](Documents/converted/media/image48.png){width="2.6462029746281717in" height="0.19794400699912512in"}If the article doesn't contain specific details that are mechanically important, it is appropriate to save it as a part.\
    \
    By using the 'Unite' function, you can glue different parts together as one.\
    \
    ![Afbeelding met schermopname, tekst, lijn, software Automatisch gegenereerde beschrijving](Documents/converted/media/image49.png){width="5.118110236220472in" height="0.7565463692038495in"}\
    \
    It\'s better not to unite all pieces at once, but do it part by part.\
    Each time after uniting 2 parts, perform a check part.\
    That way you can find out which part becomes corrupt and discover why it's happening.\
    \
    In this example, the encoder from the screenshot on top of this page, I've deleted all unimportant details and glued together all remaining pieces until one part.

  - ![Afbeelding met tekst, schermopname, Lettertype, lijn Automatisch gegenereerde beschrijving](Documents/converted/media/image50.png){width="1.4861111111111112in" height="0.8354166666666667in"}If the article does contain specific details that are mechanically important, it is appropriate to save it as an assembly and set the assembly as an inseparable.\
    \
    By using the 'Inseparable' function, you will force the system to only generate an articlenumber for the assembly and not the underlying parts.\
    \
    ![Afbeelding met tekst, schermopname, Lettertype, software Automatisch gegenereerde beschrijving](Documents/converted/media/image51.png){width="5.118110236220472in" height="1.1418678915135607in"}\
    \
    If we take the example of the encoder again, we see that the mounting bracket can be used for different positions.\
    So it might be better to keep this detail and use the function 'selective unshare' in case the mounting position should change.\
    \
    To keep the article as one, we create an assembly containing the encoder, bracket and fasteners.\
    By setting the assembly as inseparable, only the assembly will get an articlenumber and not the underlying parts.\
    \
    ![Afbeelding met tekst, schermopname, Lettertype, lijn Automatisch gegenereerde beschrijving](Documents/converted/media/image52.png){width="5.118110236220472in" height="0.6667957130358705in"}

### Healing step by step 

![](Documents/converted/media/image53.png){width="6.3in" height="7.124305555555556in"}\
**\**

# Bolt connections

## General rules

- Only use SB bolts & nuts according to EN1090-2 when required

- Always use large washers in combination with conical spring washers to protect the paint and galvanisation

- Always use tens as a bolt length (e.g. 10,20,30,100,...)

- Always limit the amount of different bolt sizes in one project

![^Remark:^](Documents/converted/media/image550.svg){alt="Waarschuwing" width="0.28194444444444444in" height="0.30434820647419075in"}

When the machine is INOX and the structure is galvanized

→Use HDGA bolts but place PA washers (DIN9021) in between

\+ Fiber Klingersil C4324 2 mm sheet between machine and structure\
(Fiber Klingersil C4324 2 mm see *chapter [5](#mounting-machineparts-on-structures)*)

![](Documents/converted/media/image56.png){width="0.8854166666666666in" height="1.0508245844269466in"}

Fastener type

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Regular structure/platform build and machine mount to structure                                                                                     |
+=============================================================================================+===========================+===========================+
| ![](Documents/converted/media/image57.png){width="0.96875in" height="1.0909722222222222in"} | **Fasteners material: Hot dip Galvanized (HDGA)**     |
|                                                                                             +---------------------------+---------------------------+
|                                                                                             | **Component**             | **Standard / norm**       |
|                                                                                             +---------------------------+---------------------------+
|                                                                                             | Hexagon head bolt         | DIN 933 / DIN 931         |
|                                                                                             +---------------------------+---------------------------+
|                                                                                             | Hexagon nut               | DIN 934                   |
|                                                                                             +---------------------------+---------------------------+
|                                                                                             | Large plain washer        | DIN 9021                  |
|                                                                                             +---------------------------+---------------------------+
|                                                                                             | Conical spring washer     | DIN 6796                  |
+---------------------------------------------------------------------------------------------+---------------------------+---------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Structure /platform build and machine mount according to norm EN 1090-2                                                                                                                                                                                                                                                                       |
+========================================================================================================+==================================================================================================+================================+================================+================================+================================+
| ![](Documents/converted/media/image58.png){width="0.8423611111111111in" height="0.9791666666666666in"} | **Fasteners material: Hot dip Galvanized (HDGA)**                                                                                                                                                                                    |
|                                                                                                        +-----------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|                                                                                                        | **Component**                                                                                                                     | **Standard / norm**                                                                              |
|                                                                                                        +-----------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|                                                                                                        | SB bolt and nut                                                                                                                   | EN15048-1                                                                                        |
|                                                                                                        +-----------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|                                                                                                        | Large plain washer                                                                                                                | ISO7093-1 with 200HV                                                                             |
|                                                                                                        +-----------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|                                                                                                        | Conical spring washer                                                                                                             | DIN 6796                                                                                         |
+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Machine build                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![](Documents/converted/media/image59.png){width="1.1228062117235345in" height="1.625in"}![](Documents/converted/media/image60.png){width="1.4020833333333333in" height="1.6931036745406824in"}           | **Fasteners material:**                                                                                                           |
|                                                                                                                                                                                                           |                                                                                                                                   |
|                                                                                                                                                                                                           | **- electrolytic galvanizing (ELVZ)**                                                                                             |
|                                                                                                                                                                                                           |                                                                                                                                   |
|                                                                                                                                                                                                           | **- INOX A2 \***                                                                                                                  |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | **Component**                                                                                    | **Standard / norm**            |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | Hexagon head bolt                                                                                | DIN 933 / DIN 931              |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | Hexagon locknut                                                                                  | DIN 985                        |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | Regular plain washer                                                                             | DIN 125                        |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | Large plain washer                                                                               | DIN 9021                       |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | *\*Remark: Always mount INOX with copper grease*                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------+
| ![](Documents/converted/media/image61.png){width="1.09375in" height="0.9604166666666667in"}                                                                                                               | Hexagon head bolt                                                                                | DIN 933 / DIN 931              |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | Large plain washer\*                                                                             | DIN 9021                       |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | Conical spring washer                                                                            | DIN 6796                       |
|                                                                                                                                                                                                           +--------------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                                                                           | *\*Special case: When there is not enough space for a large plain washer, use small washer with Loctite 243 nutlock.*             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
| ![](Documents/converted/media/image62.png){width="1.2583333333333333in" height="0.7708333333333334in"}                                                                                                    | Threaded rod or bolt                                            |                                                                 |
|                                                                                                                                                                                                           +-----------------------------------------------------------------+-----------------------------------------------------------------+
|                                                                                                                                                                                                           | 2x Hexagon nut\*                                                | DIN 934                                                         |
|                                                                                                                                                                                                           +-----------------------------------------------------------------+-----------------------------------------------------------------+
|                                                                                                                                                                                                           | (Large) plain washer                                            | DIN 9021 / DIN125                                               |
|                                                                                                                                                                                                           +-----------------------------------------------------------------+-----------------------------------------------------------------+
|                                                                                                                                                                                                           | *\*Use 2 regular nuts because there is no tension for spring washers*                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

## Choice of correct bolt length

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Required bolt length                                                                                                                                                                      |
+====================+==========================================================================================================================+====================+======================+
| **Size**           | ![](Documents/converted/media/image63.png){width="1.3145833333333334in" height="1.5291666666666666in"}**Clamp length +** |                    |                      |
+--------------------+                                                                                                                          +--------------------+----------------------+
| M8                 |                                                                                                                          | 15                 | 16                   |
+--------------------+                                                                                                                          +--------------------+----------------------+
| M10                |                                                                                                                          | 18.5               | 20                   |
+--------------------+                                                                                                                          +--------------------+----------------------+
| M12                |                                                                                                                          | 22.5               | 25                   |
+--------------------+                                                                                                                          +--------------------+----------------------+
| M16                |                                                                                                                          | 28                 | 30                   |
+--------------------+                                                                                                                          +--------------------+----------------------+
| M20                |                                                                                                                          | 33.5               | 36                   |
+--------------------+                                                                                                                          +--------------------+----------------------+
| M24                |                                                                                                                          | 40                 | 44                   |
+--------------------+--------------------------------------------------------------------------------------------------------------------------+--------------------+----------------------+

Basic rule to approach required bolt length:

→ Clamp length + diameter x 2

\* Remark: try to limit the additional thread to the minimal

# Hole / slot dimensions

**Application:**

- Holes in structures and platforms (Hot dip, Steel or stainless steel)

- Stairs and railings

- Structure to structure mounting

- Machine to structure mounting

- Weld steel or stainless steel framework and/or hot dip galvanized framework on which lasered components (cover plates etc.) will be mounted

+-------------------------------+
| **Standard applications**     |
+===============+===============+
| M8            | Ø10           |
+---------------+---------------+
| M10           | Ø13           |
+---------------+---------------+
| M12           | Ø15           |
+---------------+---------------+
| M16           | Ø20           |
+---------------+---------------+
| M20           | Ø25           |
+---------------+---------------+
| M24           | Ø30           |
+---------------+---------------+

**Application:**

- Machine build

- Inox components

- Holes in lasered and bended platework

- Holes in welded assemblies consisting of lasered and bended platework, on condition that the parts are designed with jigsaw pattern or tooth-groove pattern

- 

+-----------------------------+
| **Precise applications**    |
+==============+==============+
| M8           | Ø9           |
+--------------+--------------+
| M10          | Ø11          |
+--------------+--------------+
| M12          | Ø13          |
+--------------+--------------+
| M16          | Ø18          |
+--------------+--------------+
| M20          | Ø23          |
+--------------+--------------+
| M24          | Ø28          |
+--------------+--------------+

# Structure and platform information

## General rules

- Place slots instead of holes in the lasered plates.

- Keep 50mm distance from the side wall to mount with impact wrench

- Use round numbers to position the holes (e.g. 10,20,100,150,..)

- **Connection flanges at least 10mm thickness**

Example A

![^Remark:^](Documents/converted/media/image550.svg){alt="Waarschuwing" width="0.28194444444444444in" height="0.30434820647419075in"}

Don't use vertical slots with horizontal beams to prevent sliding down.

Example B

![](Documents/converted/media/image66.png){width="3.0632174103237095in" height="2.379861111111111in"}![](Documents/converted/media/image67.png){width="2.4713812335958005in" height="2.196558398950131in"}![](Documents/converted/media/image68.png){width="2.076992563429571in" height="1.862150043744532in"}

![50mm](Documents/converted/media/image69.png){width="1.7860837707786528in" height="3.6956517935258093in"}

**\**

## Fasteners size

**M20:** General structure build

**M16**: Reinforcements on structure build

![](Documents/converted/media/image70.png){width="4.135416666666667in" height="3.5378051181102363in"}

![](Documents/converted/media/image71.png){width="2.53125in" height="2.842431102362205in"}

**M16:** Machines or attachment to structure

![](Documents/converted/media/image72.png){width="2.4479166666666665in" height="2.477328302712161in"}

## ID numbering in WA en parts

In each WA or Part we need a ID nummer welded on it.\
The ID is made up with three characters. "ABB"\
A : for the ranking nummer of the zone\
BB: a sequence nummer (0 to 99, following A0 to A9)

If possible start the sequence nummers as how to build up.\
\
The excel list must be used by the supplier to weld the ID nummer on the parts

![Afbeelding met tekst, schermopname, software, Multimediasoftware Automatisch gegenereerde beschrijving](Documents/converted/media/image73.png){width="6.3in" height="3.078472222222222in"}\
\
![Afbeelding met tekst, schermopname, nummer, lijn Automatisch gegenereerde beschrijving](Documents/converted/media/image74.png){width="6.3in" height="3.0756944444444443in"}

## Profile information

**Allowed tracing dimensions for profiles according to DIN 997**

![](Documents/converted/media/image75.png){width="1.4833333333333334in" height="1.9444444444444444in"}![](Documents/converted/media/image76.png){width="0.8840277777777777in" height="1.8659722222222221in"}

  -------------------------------------------------------------
  Size         p    Size          e       Size             p
  --------- ------- ------------- ------- ------------- -------
  IPN 80      \-    **UPN 80**    27      **IPE 80**      \-

  IPN 100     \-    **UPN 100**   30      **IPE 100**     \-

  IPN 120     \-    **UPN 120**   35      **IPE 120**     \-

  IPN 140     \-    **UPN 140**   35      **IPE 140**     \-

  IPN 160     \-    **UPN 160**   40      **IPE 160**     \-

  IPN 180     \-    **UPN 180**   40      **IPE 180**     55

  IPN 200     \-    **UPN 200**   45      **IPE 200**     60

  IPN 220     58    **UPN 220**   45      **IPE 220**     70

  IPN 240     66    **UPN 240**   50      **IPE 240**     80

  IPN 260     73    **UPN 260**   50      **IPE 270**     85

  IPN 280     79    **UPN 280**   55      **IPE 300**     90

  IPN 300     85    **UPN 300**   60      **IPE 330**     100

                    **UPN 320**   60      **IPE 360**     100

                    **UPN 350**   60      **IPE 400**     110

                    **UPN 380**   60      **IPE 450**     110

                    **UPN 400**   60      **IPE 500**     110

                                          **IPE 550**     120

                                          **IPE 600**     130

                                                        

                                                        

  Size       **p**  **Size**      **p**   **Size**       **p**

  HEA 100     60    **HEB 100**   60      **HEM 100**     70

  HEA 120     70    **HEB 120**   70      **HEM 120**     80

  HEA 140     80    **HEB 140**   80      **HEM 140**     80

  HEA 160     90    **HEB 160**   90      **HEM 160**     90

  HEA 180     100   **HEB 180**   100     **HEM 180**     100

  HEA 200     110   **HEB 200**   110     **HEM 200**     110

  HEA 220     130   **HEB 220**   130     **HEM 220**     130

  HEA 240     150   **HEB 240**   150     **HEM 240**     150

  HEA 260     170   **HEB 260**   170     **HEM 260**     170

  HEA 280     190   **HEB 280**   190     **HEM 280**     190

  HEA 300     210   **HEB 300**   210     **HEM 300**     210

  HEA 320     210   **HEB 320**   210     **HEM 320**     210

  HEA 340     210   **HEB 340**   210     **HEM 340**     210

  HEA 360     210   **HEB 360**   210     **HEM 360**     210

  HEA 400     210   **HEB 400**   210     **HEM 400**     210

  HEA 450     210   **HEB 450**   210     **HEM 450**     210

  HEA 500     210   **HEB 500**   210     **HEM 500**     210

  HEA 550     210   **HEB 550**   210     **HEM 550**     210

  HEA 600     210   **HEB 600**   210     **HEM 600**     210

  HEA 650     210   **HEB 650**   210     **HEM 650**     210

  HEA 700     210   **HEB 700**   210     **HEM 700**     210

  HEA 800     210   **HEB 800**   210     **HEM 800**     210
  -------------------------------------------------------------

## Chemical anchor information 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Application**                                                                                                                                                                                                   |
+=======================================================================================================+=====================================================+=====================================================+
| Heavy structures/ machines / tanks that are NOT mounted directly to the floor                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Bolt connection**                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ![](Documents/converted/media/image77.png){width="1.84375in" height="3.0104166666666665in"}           | **Fasteners material: Hot dip galvanized**                                                                |
|                                                                                                       +-----------------------------------------------------------------------------------------------------------+
|                                                                                                       | Above the mount plate                                                                                     |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | Threaded rod                                        |                                                     |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | 2x Hexagon nut                                      | DIN 934                                             |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | Large plain washer                                  | DIN 9021                                            |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | Underneath the mount plate                                                                                |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | Large plain washer                                  | DIN 9021                                            |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | Hexagon nut                                         | DIN 934                                             |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+
| **Hole dimensions**                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | **Thread size**                                     | **Hole size in mount plate**                        |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | M16 rod (18mm bore)                                 | 24mm                                                |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | M20 rod (22mm bore)                                 | 28mm                                                |
|                                                                                                       +-----------------------------------------------------+-----------------------------------------------------+
|                                                                                                       | M24 rod (28mm bore)                                 | 34mm                                                |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+
| **Hole positioning**                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| General conditions                                                                                    | With obstacles in 1m range above the mount plate                                                          |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ![](Documents/converted/media/image78.png){width="1.791887576552931in" height="1.6041666666666667in"} | ![](Documents/converted/media/image79.png){width="2.0833333333333335in" height="1.6947911198600174in"}    |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **Mount position**                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
|                                                                                                       | Standard application inside a building:                                                                   |
|                                                                                                       |                                                                                                           |
|                                                                                                       | **50mm**                                                                                                  |
+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

## Mechanical anchor information

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Application**                                                                                                                                                                                                                                                                                                             |
+==============================================================================================================================================================================================================================================+===============================+==============================================+
| Small structures/machines/tanks that are mounted directly to the floor                                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Types:**                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+----------------------------------------------+
| ![Mechanical Anchors - Mechanical Expansion Anchors ancient times to secure building components. - Ripple Construction Products Pvt Ltd](Documents/converted/media/image81.jpeg){width="1.7083333333333333in" height="1.7083333333333333in"} | M8                            | M8/20x80 ELVZ                                |
|                                                                                                                                                                                                                                              |                               |                                              |
|                                                                                                                                                                                                                                              |                               | *Remark: only to secure electrical cabinets* |
|                                                                                                                                                                                                                                              +-------------------------------+----------------------------------------------+
|                                                                                                                                                                                                                                              | M12                           | M12/80x160 ELVZ                              |
|                                                                                                                                                                                                                                              +-------------------------------+----------------------------------------------+
|                                                                                                                                                                                                                                              | M16                           | M16/100x220 ELVZ                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+----------------------------------------------+
| Hole dimensions according to the ***2.Hole / slot dimensions standard applications***                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Boplan information

Place the conical stopper on a distance center to center of **60**mm **(on new model from 2024)**. This prevents opening of the door by itself. This will create a slightly overlap in the CAD file.

![](Documents/converted/media/image82.png){width="3.8043482064741907in" height="3.715865048118985in"}

# Mounting machine(parts) on structures

To separate inox parts from galva parts, use this material instead of rubber :\
Fiber Klingersil C4324 2 mm

**[Advantage]{.underline}** : the thickness doesn't change if there is any pressure on it.\
**[color]{.underline}** in 3d model : ![](Documents/converted/media/image83.png){width="1.3439370078740158in" height="0.29170713035870516in"}

![](Documents/converted/media/image84.png){width="5.656248906386701in" height="1.7291666666666667in"}

Example : art **21706208, Fiberseal_Inputbox**![Afbeelding met tafel Automatisch gegenereerde beschrijving](Documents/converted/media/image85.png){width="5.892577646544182in" height="5.574305555555555in"}**\**

# Sheet metal information

## K-factor Bending

We take the k-factor equal to in sheet metal to unfold plates:\
*(determined in 2004 by Valvan)*

*For trommels :\
conical plates: k=1\
cylindrical plates: k=0.5*

![](Documents/converted/media/image86.png){width="1.8335892388451445in" height="0.7084317585301837in"}

+-------------------------------------------------+
| **Bending radius\                               |
| (shared by Cretes '2014')**                     |
+:=====================:+:=======================:+
| **Plate thickness t** | **Inner bend radius R** |
+-----------------------+-------------------------+
| 1                     | 1,3                     |
+-----------------------+-------------------------+
| 1,5                   | 1,9                     |
+-----------------------+-------------------------+
| 2                     | 2,6                     |
+-----------------------+-------------------------+
| 3                     | 3,8                     |
+-----------------------+-------------------------+
| 4                     | 5                       |
+-----------------------+-------------------------+
| 5                     | 7                       |
+-----------------------+-------------------------+
| 6                     | 8                       |
+-----------------------+-------------------------+
| 8                     | 10                      |
+-----------------------+-------------------------+
| 10                    | 13                      |
+-----------------------+-------------------------+
| 12                    | 15                      |
+-----------------------+-------------------------+
| 15                    | 20                      |
+-----------------------+-------------------------+

## Minimum bend radius HARDOX 400

+--------------------------------------------------------------------+
| **HARDOX 400**                                                     |
+:=====================:+:=============:+:=============:+:==========:+
| **Plate thickness t** | **R/t ratio** | **W/t ratio** | **Bend R** |
+-----------------------+---------------+---------------+------------+
| 1                     | 2,5           | 8,5           | **3**      |
+-----------------------+---------------+---------------+------------+
| 2                     | 2,5           | 8,5           | **5**      |
+-----------------------+---------------+---------------+------------+
| 3                     | 2,5           | 8,5           | **8**      |
+-----------------------+---------------+---------------+------------+
| 4                     | 2,5           | 8,5           | **10**     |
+-----------------------+---------------+---------------+------------+
| 5                     | 2,5           | 8,5           | **13**     |
+-----------------------+---------------+---------------+------------+
| 6                     | 2,5           | 8,5           | **15**     |
+-----------------------+---------------+---------------+------------+
| 7                     | 2,5           | 8,5           | **18**     |
+-----------------------+---------------+---------------+------------+
| 8                     | 3,0           | 10            | **24**     |
+-----------------------+---------------+---------------+------------+
| 9                     | 3,0           | 10            | **27**     |
+-----------------------+---------------+---------------+------------+
| 10                    | 3,0           | 10            | **30**     |
+-----------------------+---------------+---------------+------------+
| 11                    | 3,0           | 10            | **33**     |
+-----------------------+---------------+---------------+------------+
| 12                    | 3,0           | 10            | **36**     |
+-----------------------+---------------+---------------+------------+
| 13                    | 3,0           | 10            | **39**     |
+-----------------------+---------------+---------------+------------+
| 14                    | 3,0           | 10            | **42**     |
+-----------------------+---------------+---------------+------------+
| 15                    | 3,0           | 10            | **45**     |
+-----------------------+---------------+---------------+------------+
| 16                    | 3,0           | 10            | **48**     |
+-----------------------+---------------+---------------+------------+
| 17                    | 3,0           | 10            | **51**     |
+-----------------------+---------------+---------------+------------+
| 18                    | 3,0           | 10            | **54**     |
+-----------------------+---------------+---------------+------------+
| 19                    | 3,0           | 10            | **57**     |
+-----------------------+---------------+---------------+------------+
| 20                    | 4,5           | 12            | **90**     |
+-----------------------+---------------+---------------+------------+
| \>20                  | 4,5           | 12            |            |
+-----------------------+---------------+---------------+------------+

![](Documents/converted/media/image87.png){width="3.7395833333333335in" height="4.104389763779528in"}

# Info LaserCut

## Tolerances on dimensions

![Afbeelding met tekst, schermopname, nummer, Lettertype Automatisch gegenereerde beschrijving](Documents/converted/media/image88.png){width="6.3in" height="2.6930555555555555in"}

# Info Saw Work SW

If a model is drawn shorter than its width, height or diameter (e.g. a PB 100x50 must be sawn to 80mm), then in Modeling with "3D documentation" a measurement must be added to the length of the model with postfix "LEN". If this is not done, the wrong length will be assigned to this piece.

This is also the way to dimension a flexible pipe. (cfr Design Bible *Piping*)

# Database agreements

## Material color

+--------------------+--------------------------------------+
| **Material**       | **Part color**                       |
+====================+======================================+
| Steel              | GS STAAL                             |
|                    |                                      |
|                    | *Remark: specify RAL color in order* |
+--------------------+--------------------------------------+
| Stainless steel    | GS RVS                               |
+--------------------+--------------------------------------+
| Galvanized parts   | GS GALVA ZINCOR                      |
+--------------------+--------------------------------------+
| Cruesabro & Hardox | GS STAAL GEHARD                      |
+--------------------+--------------------------------------+
| PU                 | GS PU-RIEM                           |
+--------------------+--------------------------------------+
| Rubber             | GS RUBBER                            |
+--------------------+--------------------------------------+

![](Documents/converted/media/image89.png){width="3.707638888888889in" height="3.732638888888889in"}

Parts that needs to be painted, use the RAL 5011 (not the project color) in the instance color.\
If only the outer side needs to be painted, use the RAL 5011 (not the project color) in the surface color (for example the outside surface of a trommel)

![](Documents/converted/media/image90.png){width="2.474025590551181in" height="1.294215879265092in"}

Steel parts that needs to be galvanised : base color GS STEEL; instance color GS GALVA ZINCOR

# Welding

## Norm

The norm for welding and allied processes 'EN ISO 2553' has been renewed since 2013, with a small update in 2019.

It's basically a compromise between European and American norms, with some slight differences. European **→** System A American **→** System B

![](Documents/converted/media/image91.png){width="5.072503280839895in" height="1.2381944444444444in"}

**Rule : always use the welding symbols according SYSTEM A.**

In the title block on our drawings, it is mentioned that we use the European viewset / standard (in green) and 'ISO 13920-AE' for general tolerances for welded structures and the geometrical tolerances (in yellow).

![](Documents/converted/media/image92.png){width="6.291666666666667in" height="1.5069444444444444in"}

In case higher tolerances than according ISO 13920-AE are required, mainly about deformation due to welding, add a special remark in the tail of the welding symbol.

It is also possible to refer to WPS (Welding Procedure Specification) if known.

A welding symbol is always composed of :

1 : arrow line

2 : reference line

3 : tail

![Une image contenant croquis, ligne, diagramme, dessin Description générée automatiquement](Documents/converted/media/image93.png){width="2.000266841644794in" height="1.1920199037620298in"}

## Elementary welding symbols and how to use them

The elementary symbols are defined by norm ISO 2553 and can't be adapted or modified. In case any clarification has to be made, then use supplementary symbols and the tail.

- Butt weld : welding bead \<45°

> ![Afbeelding met lijn, schets, diagram, tekst Automatisch gegenereerde beschrijving](Documents/converted/media/image94.png){width="3.1979166666666665in" height="1.0198764216972878in"} ![Afbeelding met lijn, diagram Automatisch gegenereerde beschrijving](Documents/converted/media/image95.png){width="1.5851356080489938in" height="1.0067749343832022in"}

A certain depth is burnt into the connected parts

**→** There is a lot of different butt weld symbols that refer to different joint preparations.

But it's appropriate to not designate the welding preparation and use this symbol that doesn't define the joint preparation, but leaves it up to the production.

![Afbeelding met schets, lijn, diagram, tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image96.png){width="1.53125in" height="1.403646106736658in"}

- Fillet weld : welding bead from 45° to 90°

![Afbeelding met lijn, tekst, diagram, Perceel Automatisch gegenereerde beschrijving](Documents/converted/media/image97.png){width="1.641839457567804in" height="1.625in"} ![Afbeelding met lijn, diagram Automatisch gegenereerde beschrijving](Documents/converted/media/image98.png){width="2.9220220909886265in" height="1.5930555555555554in"}

Adding of a certain amount of material on the connected parts\
**→** Commonly known as corner welds

![Afbeelding met lijn, diagram, schets, Perceel Automatisch gegenereerde beschrijving](Documents/converted/media/image99.png){width="1.952830271216098in" height="1.5600634295713036in"} ![Afbeelding met schets, diagram, lijn, tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image100.png){width="1.9856889763779528in" height="1.547169728783902in"}

- Combination of Butt and Fillet

Where you burn into the connected parts and add a second layer material on to it\
**→** For this kind of more advanced weld, ask to a manager

![Afbeelding met diagram, lijn, schets, Perceel Automatisch gegenereerde beschrijving](Documents/converted/media/image101.png){width="1.8645833333333333in" height="1.5653291776027995in"}

- Edge weld : welding bead \> 90°

![Afbeelding met lijn, diagram, schets, Parallel Automatisch gegenereerde beschrijving](Documents/converted/media/image102.png){width="1.8645833333333333in" height="1.8155161854768154in"}

> Adding of a certain amount of material on the connected parts

![](Documents/converted/media/image103.png){width="1.5213593613298337in" height="3.1977930883639547in"}

- Flare V weld : to connect 2 round surfaces

![Afbeelding met schets, tekening, lijntekening Automatisch gegenereerde beschrijving](Documents/converted/media/image104.png){width="1.78125in" height="1.4092366579177602in"}

- Flare bevel : to connect 1 round surface on a flat one

> ![Afbeelding met schets, tekening, lijn, diagram Automatisch gegenereerde beschrijving](Documents/converted/media/image105.png){width="1.5in" height="1.5in"} ![Afbeelding met cirkel, diagram, lijn, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image106.png){width="1.6787981189851269in" height="1.488888888888889in"}
>
> **→** To be used to weld a net onto a frame, dimensions of the net has to be clearly identified:
>
> ![Une image contenant texte, diagramme, ligne, capture d'écran Description générée automatiquement](Documents/converted/media/image107.png){width="5.0223928258967625in" height="3.248611111111111in"}

- Plug weld : to fill holes and connect groove / tongue connections

> ![Afbeelding met schets, lijn, diagram, tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image108.png){width="1.8020833333333333in" height="1.5887215660542433in"}

- Resistance Spot Weld or Projection Weld\
  **→** To be used for welding nuts

> ![Afbeelding met diagram, cirkel, schets, lijn Automatisch gegenereerde beschrijving](Documents/converted/media/image109.png){width="2.0833333333333335in" height="1.6310312773403324in"}

- Stud weld : for stud bolts

> ![Afbeelding met diagram, cirkel, lijn, tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image110.png){width="2.5520833333333335in" height="1.5769422572178478in"}

## Supplementary welding symbols and how to use them

**These symbols are used to add info on how to perform the weld** but not on the operations to perform afterwards (that are specified in text on the tail of the symbol)

- 

- Field weld : the weld is done on site, during mounting.\
  This can be very useful to avoid misalignment of flanges for example.

![Afbeelding met cirkel, diagram, ontwerp, patroon Automatisch gegenereerde beschrijving](Documents/converted/media/image111.png){width="1.905660542432196in" height="1.627189413823272in"}

- 

- Flush : to specify that the weld has to be flash-finished

![Afbeelding met lijn, diagram, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image112.png){width="2.4320516185476815in" height="1.9339621609798776in"}

- Convex :

![Afbeelding met diagram, lijn, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image113.png){width="2.416438101487314in" height="1.9215463692038495in"}

- Concave :

![Afbeelding met diagram, lijn, Perceel, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image114.png){width="2.3294149168853893in" height="1.8490562117235345in"}

- Weld all-round symbol : to indicate with a single symbol, that the part needs to be welded all the way around, in case the weld type and dimension of the weld remain the same

![Afbeelding met diagram, lijn, Parallel, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image115.png){width="1.9916666666666667in" height="1.5743055555555556in"} ![Afbeelding met diagram, lijn, schets, Rechthoek Automatisch gegenereerde beschrijving](Documents/converted/media/image116.png){width="1.7037237532808398in" height="1.5748031496062993in"} ![Afbeelding met lijn, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image117.png){width="1.068688757655293in" height="1.5748031496062993in"}

**Rule : this symbol is also used for circular welding to insist on the fact that the weld has to be continuous and start & stop points are the same.**

![Une image contenant diagramme, cercle, ligne, conception Description générée automatiquement](Documents/converted/media/image118.png){width="1.9152777777777779in" height="1.5375in"}

- Weld between 2 points : to indicate a continuous weld along several edges, in all directions, having the exact same characteristics from start to end points.

![Une image contenant diagramme, croquis, Dessin technique, ligne Description générée automatiquement](Documents/converted/media/image119.png){width="2.560741469816273in" height="1.6788746719160106in"} ![Une image contenant ligne, diagramme, Tracé, Parallèle Description générée automatiquement](Documents/converted/media/image120.png){width="2.071648075240595in" height="1.6181025809273841in"}

Note : the arrow can be drawn with : ALT + 26

- Chain intermittent welds :

![Afbeelding met tekst, diagram, lijn, schermopname Automatisch gegenereerde beschrijving](Documents/converted/media/image121.png){width="4.697916666666667in" height="2.538490813648294in"}

**Rule : the number of weld has to be specified only if relevant**

**Rule : the lengths of weld and of space don't have to be on a mm but rounded**

- Staggered intermittent weld\
  **→** Less deformation of thin plates

![Une image contenant texte, diagramme, ligne, capture d'écran Description générée automatiquement](Documents/converted/media/image122.png){width="4.520833333333333in" height="2.4896478565179354in"}

**Rule : the number of weld has to be specified only if relevant**

**Rule : the lengths of weld and of space don't have to be on a mm but rounded**

## Arrow placement and information

European standards use following rules:

- According SYSTEM A, the dashed line is always underneath the reference line.

- The arrow always points to a visible line (never to a hidden line)

- The location of the weld (in red) is defined by the position of the arrow and the position of the welding symbol regarding the dashed line:

![Afbeelding met lijn, diagram, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image123.png){width="1.741813210848644in" height="1.488708442694663in"} ![Afbeelding met lijn, diagram, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image124.png){width="2.0059765966754157in" height="1.4790485564304463in"} ![Afbeelding met lijn, diagram, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image125.png){width="1.744514435695538in" height="1.4700207786526684in"}

Fig.1 Fig.2 Fig.3

> **→** One side is welded: the side of the arrow. The symbol is placed on top. (Fig.1).
>
> **→** One side is welded: the opposite side of the arrow. The symbol is placed at the bottom. (Fig.2).
>
> **→** Both sides have the same weld: the dashed line is removed (Fig.3).
>
> **→** Both sides have different welds: the dashed line is kept (Fig.4).
>
> ![](Documents/converted/media/image126.png){width="2.2895833333333333in" height="0.9149606299212598in"}

- 

- When it's not important to specify which part needs to be prepared or when no preparation is needed, multiple (broken) lines can be used to indicate identical welds

![Une image contenant diagramme, ligne, croquis, origami Description générée automatiquement](Documents/converted/media/image127.png){width="1.5849048556430447in" height="1.4909383202099737in"}

- 

- When it's important to specify which part needs to be prepared, use a broken arrow.

![Afbeelding met lijn, diagram, schets, Perceel Automatisch gegenereerde beschrijving](Documents/converted/media/image128.png){width="1.2452832458442695in" height="1.5250207786526684in"}

## Additional information on welding symbols

Additional information and special remarks about the weld can be added to the symbol in the tail. **The tail has to be open for additional information and closed for a reference to any document** (as WPS for example).

![Une image contenant texte, Police, ligne, capture d'écran Description générée automatiquement](Documents/converted/media/image129.png){width="4.783018372703412in" height="0.8462029746281715in"}

Common remarks are:

- Watertight

- Leave flow holes free

- Leave free near mounting holes

- Smooth finish (polish)

- Flat grind finish

- Prepare for watertight sealing

- ...

Combinations of these remarks are also possible

![Afbeelding met diagram, schets, tekening, tekst Automatisch gegenereerde beschrijving](Documents/converted/media/image130.png){width="2.84375in" height="1.69461832895888in"}

![Afbeelding met diagram, lijn, Technische tekening, tekst Automatisch gegenereerde beschrijving](Documents/converted/media/image131.png){width="2.8976181102362206in" height="1.582638888888889in"}![Afbeelding met diagram, schets, lijn, Technische tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image132.png){width="2.877357830271216in" height="1.959786745406824in"}

Crucial welding's should be named and refer to the 'WPS' (Welding Procedure Specification)\
**→** Has to be discussed with a manager

![Afbeelding met diagram, lijn, schets, tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image133.png){width="2.233053368328959in" height="1.358490813648294in"}

## Weld size indication

Defining the size of the weld should be calculated by a welding engineer.\
But for simple applications, you can use following thumb rules:

- Fillet weld

> Following the European standard, the size of the corner weld must be indicated by 'a'
>
> ![Afbeelding met lijn, diagram, Rechthoek, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image134.png){width="1.4145767716535433in" height="1.5188670166229221in"}
>
> **→** American standards use 'z'
>
> ![Afbeelding met Lettertype, diagram, lijn, wit Automatisch gegenereerde beschrijving](Documents/converted/media/image135.png){width="2.4375656167979in" height="0.5600207786526684in"}
>
> 'a' is calculated as follow :

- Double sided weld a ≥ 0,6 x t

- Single sided weld a ≥ 0,8 x t

Where 't' is the thickness of the thinnest plate.

**IMPORTANT NOTE : Always check that there is enough space to weld.**

> If a3 is specified, 3x1,4=4,2 mm minimum of available surface is required.

- Butt weld

  - If there is no weld size mentioned **→** full weld-through

![Afbeelding met lijn, diagram, Perceel, ontwerp Automatisch gegenereerde beschrijving](Documents/converted/media/image136.png){width="1.822422353455818in" height="1.3773578302712162in"}

- 

- If there is a weld size mentioned

> **→** depth of penetration

![Afbeelding met schets, diagram, lijn, tekening Automatisch gegenereerde beschrijving](Documents/converted/media/image137.png){width="1.7830194663167105in" height="1.193847331583552in"}

If the application isn't that simple anymore, better to calculate or discuss with a manager or a welding engineer. To calculate you can use following tools:

- Fillet weld calculation static load <https://werktuigbouw.nl/sub22.htm>

- Butt weld calculation dynamic load <https://werktuigbouw.nl/sub22.htm>

- R:\\Nota\'s Ontwerp en Technische Catalogi\\00_Technisch Praktisch-Theorie\\Lassen-toelaatbare belasting WL.pdf

# Platforms (to be updated)

![Afbeelding met schermopname Automatisch gegenereerde beschrijving](Documents/converted/media/image138.png){width="2.6458333333333335in" height="1.4166666666666667in"}Part number with platforms, stairs, safety fences :\
\
**23845114, Standard_platforms, A.12 **

**\
\
\
\**

Where to find the C160 profiles :\
(in classification : )\
\
![](Documents/converted/media/image139.png){width="4.064926727909011in" height="5.197916666666667in"}\
\
But **not** the accessories and **not** the railing

# Geared motors (Siemens)

## Siemens Mall: Select the correct Mains voltage 

In the configurator geared motors of Siemens specify the voltages as follow :

![](Documents/converted/media/image140.png){width="6.3in" height="2.376388888888889in"}

> Select [(1)]{.mark} standard (P80) tolerance on voltage +/- 10%
>
> Motors up to and including 7.5 kW select [(2)]{.mark} 260/400 V\
> Motors \> 7.5 kW **with** frequency control select [(2)]{.mark} 260/400 V\
> Motors \> 7.5 kW **without** frequency control select [(3)]{.mark} 400/690 V

## Siemens Mall : how to select file type SAT

![](Documents/converted/media/image141.png){width="3.59375in" height="3.9457141294838145in"}

# Classification

## Classification checkbox

These are the criteria where commercial parts are checked on for release approval.

![Afbeelding met diagram Automatisch gegenereerde beschrijving](Documents/converted/media/image142.png){width="6.3in" height="4.725in"}

## Approval planning

Parts open for approval will be checked daily in the morning by the keyusers.\
There is approximately an half hour planned daily for this.\
But this can vary by the amount of requests.

If there are any questions concerning classification, please prepare your question by mail with a detailed explanation of the problem, so they can refer back to you when possible.

# Norms on electrics

![Afbeelding met tekst, ontwerp Door AI gegenereerde inhoud is mogelijk onjuist.](Documents/converted/media/image143.png){width="4.789033245844269in" height="8.661417322834646in"}
