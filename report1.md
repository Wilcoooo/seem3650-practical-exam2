# SEEM3650 Practical Exam Report

Name: [Your Name]
Student ID: [Your Student ID]

## Step 2: Shakespeare Character-level Model

I prepared the `shakespeare_char` dataset using:

python data/shakespeare_char/prepare.py

I then trained the Shakespeare character-level BabyGPT model using `config/train_shakespeare_char.py` and generated sample outputs from the trained model.

First 5 lines of generated Shakespeare samples:

All before will and is to be maders a way to take
On the call and be this foul him to bardeth.

GLOUCESTER:
When stard God me

## Step 3: Model Architecture Exploration

For my student ID, the last three digits are `106`.

- `106 mod 4 = 2`
- Therefore, according to the assignment:
  - the number of layers is fixed at 7
  - the number of heads varies among 2, 3, 5, and 7

I trained the following settings:

- Layers = 7, Heads = 2
- Layers = 7, Heads = 3
- Layers = 7, Heads = 5
- Layers = 7, Heads = 7

The assignment suggests comparing performance at iteration 5000. Since training to iteration 5000 was slower on my setup, I used iteration 1000 consistently across all runs, as allowed by the assignment instructions.

The plot was saved in:

figures/step3_heads_vs_loss.png

Lowest validation loss achieved:

1.9039

Best settings on my machine:

- Layers: 7
- Heads: 7

## Step 4: Training BabyGPT for Code Generation

For my student ID:

- `106 mod 2 = 0`

Therefore, I used open-source C/C++ code from GitHub to build the dataset in:

data/code_generation/input.txt

I prepared the dataset using:

python data/code_generation/prepare.py

Number of tokens in the dataset:

5002942

This satisfies the assignment requirement of having at least 100000 tokens.

I created a new configuration file for this task in:

config/train_code_generation.py

Then I trained the BabyGPT model for code generation and generated sample outputs.

First 20 lines of generated code samples:

#include "in", GLbyte this abon to so per icenction us of and fon xed rele dave ornd ifintonangesion.
   EXINT[2]                                                                                 1.5 = 2, 0.5
                                                                                                                                   \
                                                                                                                                                       \
               
---------------
#include "fixeled;
    if (cJSON_Prock_becont = NUL)
     if (UNITY_CLEX_CHINTTA_AT(threshold, lengthold, num_num_endexpected, &&unsigned cJSON_MOULLL);
   if (!dectemp(tcJSON_Feltem(0) && STB_C_STIM_SARSSE(lad = NULL) ||(astate->childe))) {
     stbtte___rresh_seize( floation_wrind_to_chart
                                                                                                                                                                                                                       
---------------
#include > 0 || dif STBVOX_STAR_IND
                                                                                                                                       3x8, 0x800006,
#define GL_ATER_FILOTATER_PRATRE                                 0x800336143, 0x8B37F
#define GL_TEXT_ARRB                                0x82077
#define GL_MEXTEFF_ARMINTER_)              0x8B016
#define GL_VERTHALUB                        0x8FFFF
#define GL_TEXTRED_SUQUAL_DINTINT124
typedef void (APIENTRYP PFNGLPEXTRIN

Favorite generated snippet(s):

The following snippet is one of my favorite outputs because it resembles C/C++ header-style code with multiple #define statements and a function pointer typedef:

#include > 0 || dif STBVOX_STAR_IND
                                                                                                                                       3x8, 0x800006,
#define GL_ATER_FILOTATER_PRATRE                                 0x800336143, 0x8B37F
#define GL_TEXT_ARRB                                0x82077
#define GL_MEXTEFF_ARMINTER_)              0x8B016
#define GL_VERTHALUB                        0x8FFFF
#define GL_TEXTRED_SUQUAL_DINTINT124
typedef void (APIENTRYP PFNGLPEXTRIN

Another interesting generated snippet is shown below because it imitates conditional statements and function-like code structure, even though the syntax is not fully correct:

#include "fixeled;
    if (cJSON_Prock_becont = NUL)
     if (UNITY_CLEX_CHINTTA_AT(threshold, lengthold, num_num_endexpected, &&unsigned cJSON_MOULLL);
   if (!dectemp(tcJSON_Feltem(0) && STB_C_STIM_SARSSE(lad = NULL) ||(astate->childe))) {
     stbtte___rresh_seize( floation_wrind_to_chart