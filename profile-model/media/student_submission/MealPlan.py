class MealPlan:

    def countDistinct (self, morningMeal, noonMeal, eveningMeal, nightMeal):

        plate2 = []
        list2 = []

        for i in morningMeal:
            for j in noonMeal:
                for k in eveningMeal:
                    for l in nightMeal:
                        AllPossibleComb = (i,j,k,l)
                        list2.append(sorted(AllPossibleComb))

        for a in plate2:
            if a in plate2:
                continue
            else:
                plate2.append(n)

        return len(plate2)

            
        
           

                
            
