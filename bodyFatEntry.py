class bodyFatEntry:
    def __init__(self, date, age, weight, thighSize, chestSize, abSize):
        self.age       = age
        self.weight    = weight
        self.thighSize = float(thighSize)
        self.chestSize = float(chestSize)
        self.abSize    = float(abSize)
        self.date      = date
        self.bfp       = self.bodyFatCalculation()

    def __str__(self):
        formattedString = '{:<12}{:<5}{:<10}{:.2f}     {:.2f}     {:.2f}     {:.2f}%'
        return formattedString.format(
            self.date,
            self.age,
            self.weight,
            self.thighSize,
            self.chestSize,
            self.abSize,
            self.bfp
        )
    
    def __iter__(self):
        return iter(
            [
                self.date,
                self.age,
                self.weight,
                self.thighSize,
                self.chestSize,
                self.abSize,
            ]
        )

    def bodyFatCalculation(self):
        measurement = self.thighSize + self.chestSize + self.abSize
        measurementSquared = measurement * measurement

        bodyDensity = (1.10938 - (0.0008267 * measurement) + 
                       (0.0000016 * measurementSquared) - 
                       (0.0002574 * float(self.age)))
        
        bodyFatPercentage = (495 / bodyDensity) - 450

        return bodyFatPercentage
    