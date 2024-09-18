purchasePrice = float(input("Enter purchase price: "))
sellingPrice = float(input("Enter selling price: "))

markup = sellingPrice - purchasePrice

percentageMarkup = markup / purchasePrice * 100

profitMargin = markup / sellingPrice * 100

print("Markup: ${:.1f}".format(markup))
print("Percentage markup: {:.1f}%".format(percentageMarkup))
print("Profit margin: {:.2f}%".format(profitMargin))
