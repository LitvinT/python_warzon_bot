from models import Category, Model, Brand, ProductImage


async def main():
    cat = [
        'Lockwood 300', 'Expedite 12', 'Bryson 800', 'Bryson 890'
    ]
    for i in cat:
        i = Model(name=i, brand_id=9)
        await i.save()



# async def main():
#     cat = [
#         'EBR-14', 'SP-R 208', 'Lockwood MK2', 'LM-S', 'SA-B 50', 'TAQ-M'
#         ]
#     for i in cat:
#         i = Model(name=i, brand_id=20)
#         await i.save()
#




# async def main():
#     cat = Category(category='CS.GO', is_published=True)
#     await cat.save()
# #
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())