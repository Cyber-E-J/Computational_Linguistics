# Russian example from Kenstowicz and Kisseberth
# This version defines moprphological relation Mor
# and phonological relation Phon.  Compose them as
# VMor .o. Phon to map morphology to surface.

# Vowel-final verb stems
# govori SPEAK
# pisa WRITE
# čita READ
# vise HANG
define VstemV [ [SPEAK .x. {govori}] | 
                [WRITE .x. {pisa}] | 
                [READ .x. {čita}] | 
                [HANG .x. {vise}] ];

# Consonant-final verb stems
# bred lounge
# bereg guard
# greb row
# krad steal 
# klad place
# lez crawl
# mog be_able
# met sweep
# nes carry
# obret find
# plet plait
# pek bake
# pas herd
# skreb scrape
# sek thrash

define VstemC [[LOUNGE .x. {bred}] | [GUARD .x. {bereg}] | 
     [ROW .x. {greb}] |
     [STEAL .x. {krad}] | 
     [ PLACE .x. {klad}] |
     [ CRAWL .x. {lez}] | 
     [ BEABLE .x. {mog}] |
     [ SWEEP .x. {met}] |
     [ CARRY .x. {nes}] |
     [ FIND .x. {obret}] |
     [ PLAIT .x. {plet}] |
     [ BAKE .x. {pek}] |
     [ HERD .x. {pas}] |
     [ SCRAPE .x. {skreb}] |
     [ THRASH .x. {sek}]];




# ***** Define Vstem from VstemV and VstemC
define Vstem VstemV | VstemC;


# ***** Define the inflections
# define Infl INF : t' | SG1 : u | MasPst : l | [[FemPst : 0] 0:l 0:a];
define Infl MasPst : l | [[FemPst : 0] 0:l 0:a];

# **** Define underlying phrases (inflected words)
define PHRASE Vstem.u "+" Infl.u;

# ***** Define the morphology MOR, mapping a sequence of morphemes to an 
# ***** underlying phone spelling
define M Vstem | "+":0 | Infl; 
define MOR M+;

# Russian consonants
define C b | č | d | k | g | l | m | n | p | r | s | t | t' | v | z;

# Phonology
# ***** Define LDrop, a rule which deletes l in certain contexts.
define LDrop l -> 0 || C _ .#.;

# ***** Define Devoi, a rule which devoices b,d,g,z in certain contexts.
define Devoi b -> p, d -> t, g -> k, z -> s || _ .#.;

# ***** Define DSD (dental stop deletion), a rule which deletes t,d
# in certain contexts.
define DSD [t | d | t'] -> 0 || _ l;

# ***** Define the relation PHON.
define PHON DSD .o. LDrop .o. Devoi;

# ***** Define a finite state lexicon in terms of Phon, Mor, and Phrase.
define Russian PHRASE .o. MOR .o. PHON;

# ***** Underlying words
define Uword [PHRASE .o. MOR].l;

# ***** Uword to surface
define Russian2 [Uword .o. PHON];


