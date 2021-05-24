import blocksmith

# Generate private key

key_generator = blocksmith.KeyGenerator()
user_input = input('Please mash your keyboard then hit enter (we need entropy):')
key_generator.seed_input(user_input)
key = key_generator.generate_key()

print('''
--------------------------
|       PRIVATE KEY      |
--------------------------
''')

print(key)

print(
'''
--------------------------
|     BITCOIN ADDRESS    |
--------------------------
''')

# Generate wallet

address = blocksmith.BitcoinWallet.generate_address(key)
print(address, '\n')