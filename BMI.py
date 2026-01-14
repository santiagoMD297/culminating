class BMI_Thing:

    def load_rows(self, file_t):
        lines = []
        rows = []
        with open(file_t, 'r') as file:
                for line in file:
                    Line = line.split()
                    lines.append(Line)
        for nums in lines:
             row = {}
             row["BiacromialDiameter"]=float(nums[0])
             row["BiiliacDiameter"]= float(nums[1])
             row["BitrochantericDiameter"]= float(nums[2])
             row["ChestDepth"]= float(nums[3])
             row["ChestDiameter"]= float(nums[4])
             row["ElbowDiameter"]= float(nums[5])
             row["WristDiameter"]= float(nums[6])
             row["KneeDiameter"]= float(nums[7])
             row["AnkleDiameter"]= float(nums[8])
             row["ShoulderGirth"]= float(nums[9])
             row["ChestGirth"]= float(nums[10])
             row["WaistGirth"]= float(nums[11])
             row["NavelGirth"]= float(nums[12])
             row["HipGirth"]= float(nums[13])
             row["ThighGirth"]= float(nums[14])
             row["BicepGirth"]= float(nums[15])
             row["ForearmGirth"]= float(nums[16])
             row["KneeGirth"]= float(nums[17])
             row["CalfGirth"]= float(nums[18])
             row["AnkleMinGirth"]= float(nums[19])
             row["WristMinGirth"]= float(nums[20])
             row["Age"]= float(nums[21])
             row["WeightKg"]= float(nums[22])
             row["HeightCm"]= float(nums[23])
             row["Gender"]= int(nums[24])
             rows.append(row)
        return rows
    def standard_bmi(self, weight_kg, height_cm):
        height_m = height_cm / 100
        return weight_kg / (height_m * height_m)

    def new_bmi(self, chest_d, chest_depth, bitro, wrist_g, ankle_g, height_cm):
        return -110 + 1.34*chest_d + 1.54*chest_depth + 1.20*bitro + 1.11*wrist_g + 1.15*ankle_g + 0.177*height_cm

    def regression_and_corr(self, x_list, y_list):
        
        n = len(x_list)
        sum_x = 0.0
        for num in x_list:
            sum_x += num

        sum_y = 0.0
        for num in y_list:
            sum_y += num

        sum_xy = 0.0
        for num in range(len(x_list)):
            sum_xy += x_list[num] * y_list[num]

        sum_x2 = 0.0
        for num in x_list:
            sum_x2 += num ** 2
        
        sum_y2 = 0.0
        for num in y_list:
            sum_y2 += num ** 2

        slope = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
        intercept = (sum_y - slope*sum_x) / n
        corr = (n*sum_xy - sum_x*sum_y) / (((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))**0.5)

        return slope, intercept, corr

    def run(self, filename):
        rows = self.load_rows(filename)

        
        ages = []
        stdbmis = []
        weights = []
        newbmis = []

        for r in rows:
            ages.append(r["Age"])
            stdbmis.append(self.standard_bmi(r["WeightKg"], r["HeightCm"]))
            newbmis.append(self.new_bmi(r["ChestDiameter"], r["ChestDepth"], r["BitrochantericDiameter"],
                                        r["WristMinGirth"], r["AnkleMinGirth"], r["HeightCm"]))
            weights.append(r["WeightKg"])

        
        print("Regression 1: Age vs Standard BMI", self.regression_and_corr(ages, stdbmis))
        print("Regression 2: Weight vs New BMI", self.regression_and_corr(weights, newbmis))

b = BMI_Thing()
b.run("body.dat")