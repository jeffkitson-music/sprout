import sprout

### WARNING ###
# DO NOT USE THIS ON REAL SEED PHRASES.
# This is for demonstration purposes only.

# Demo Data
original_seed = ['thank', 'equip', 'quality', 'viable', 'merit', 'garden', 'phone', 'jeans', 'mansion', 'pilot', 'grant', 'toddler', 'crisp', 'velvet', 'ability', 'aim', 'dutch', 'camp', 'actor', 'coconut', 'negative', 'thought', 'color', 'involve']
s1 = ['noble', 'outer', 'repair', 'slow', 'health', 'guard', 'tag', 'witness', 'gas', 'awful', 'chapter', 'glory', 'monkey', 'hub', 'reform', 'sport', 'seek', 'chapter', 'combine', 'fan', 'few', 'chimney', 'among', 'potato']
s2 = ['engine', 'sphere', 'boost', 'disorder', 'ticket', 'decline', 'leaf', 'mention', 'trap', 'reform', 'duck', 'liberty', 'route', 'orient', 'refuse', 'subject', 'manual', 'allow', 'consider', 'lawsuit', 'shoe', 'similar', 'clean', 'ten']
s3 = ['ensure', 'require', 'lazy', 'apart', 'beef', 'elite', 'swear', 'knock', 'retire', 'pill', 'road', 'tenant', 'average', 'coil', 'abandon', 'curious', 'elite', 'flee', 'bench', 'recall', 'helmet', 'coyote', 'story', 'tired']

print("=== Recovering the Seed ===")
# Recover from Shard 1 & 2
seed = sprout_public.recover_seed(s1,s2,"1 & 2")
print(seed)

# Recover from Shard 1 & 3
seed2 = sprout_public.recover_seed(s1,s3,"1 & 3")
print(seed2)

# Recover from Shard 2 & 3
seed3 = sprout_public.recover_seed(s2,s3,"2 & 3")
print(seed3)

if seed == original_seed and seed2 == original_seed and seed3 == original_seed:
    print("Outcome: All match! Success!")

print()
print("=== Splitting the Seed ===")
split_seed = sprout_public.split_seed(s1)
print(split_seed)

print(split_seed[0])
print(split_seed[1])
print(split_seed[2])
