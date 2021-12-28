# Reconstructing By Hand (Jeff's rewrite draft)
Unfinished and to be continued...

## Step 1. Assign Numbers
Convert each word to it's corresponding number on the BIP39 Word List and subtract 1 (e.g. "abandon" = 0, "monkey" = 1145, "zoo" = 2047).

Example:

| #  | Word    | BIP39 Index (minus 1) |
|----|---------|-----------------------|
| 1  | thank   | 1790                  |
| 2  | equip   | 609                   |
| 3  | quality | 1401                  |
| 4  | viable  | 1946                  |
| 5  | merit   | 1116                  |
| 6  | garden  | 765                   |
| 7  | phone   | 1308                  |
| 8  | jeans   | 957                   |
| 9  | mansion | 1082                  |
| 10 | pilot   | 1319                  |
| 11 | grant   | 813                   |
| 12 | toddler | 1819                  |
etc..


## Step 2. Calculate The Missing Shard
### Missing Shard 1
XOR each number from Shard 2 and Shard 3 to generate Shard 1. Start from the top of Shard 3 working down and the bottom of Shard 2 working up. 

Example:

| Formula                      | Result       |
|------------------------------|--------------|
| Shard3-Word1 ⊕ Shard2-Word24 | Shard1-Word1 |
| Shard3-Word2 ⊕ Shard2-Word23 | Shard1-Word2 |
| Shard3-Word3 ⊕ Shard2-Word22 | Shard1-Word3 |

### Missing Shard 2
XOR each number from Shard 1 and Shard 2 to generate Shard 2. Start from the top of both shards.
 
Example:
 
| Formula                      | Result       |
|------------------------------|--------------|
| Shard1-Word1 ^ Shard3-Word1  | Shard2-Word1 |
| Shard1-Word2 ^ Shard3-Word2  | Shard2-Word2 |
| Shard1-Word3 ^ Shard3-Word3  | Shard2-Word3 |

### Missing Shard 3
Skip to final step.

## Step 3 (final step):
XOR Shard 1 and Shard 2 to recover the original seed phrase. Start with the first word for both shards (Shard1-Word1 ^ Shard2-Word1, etc.)

|           Formula           |        Result        |
|:---------------------------:|:--------------------:|
| Shard1-Word1 ^ Shard2-Word1 | Seed Phrase - Word 1 |
| Shard1-Word2 ^ Shard2-Word2 | Seed Phrase - Word 2 |
| Shard1-Word3 ^ Shard2-Word3 | Seed Phrase - Word 3 |


# Resources and Links
  - The BIP39 word list is included in this repo, [but here it is, just in case](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt)
  - The original instructions are over in the [seedpart](https://github.com/MJL85/seedpart) repo


# Reconstructing By Hand (Original Instructions)

You can reconstruct the seed by hand with the following procedure:  
1. Convert each shard into a list of numbers, where each number is the line the word appears in the BIP39 list minus 1 (e.g. "abondon" = 0, "monkey" = 1145).
1. If you are missing shard 0:
    1. XOR each number from both shards to generate a third shard. For shard 1, start with the last word and work up. For shard 2, start with the first word and work down.
1. If you are missing shard 1:
    1. XOR each number from both shards to generate a third shard. For both shards start with the first word.
	1. Reverse the list generated from the previous step.
1. If you are missing shard 2:
    1. Skip to next step.
1. XOR shard 0 and shard 1 to recover the original seed phrase.
