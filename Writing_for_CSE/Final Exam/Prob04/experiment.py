def tp_tn_fp_fn(real, guess, c_real, c_guess):
    TP, TN, FP, FN = 0,0,0,0
    for r in range(len(real)):
        if real[r] >= c_real:
            if guess[r] >= c_guess:
                TP += 1
            else:
                TN += 1
        else:
            if guess[r] >= c_guess:
                FP += 1
            else:
                FN += 1
    return TP, TN, FP, FN
def dataIn():
    real = [39.1, 38.2, 37.5, 38.7, 36.2, 38.6, 38.1, 35.3, 36.3, 39.3, 35.5, 36.5, 36.4]
    guess = [95, 93, 87, 86, 75, 72, 66, 63, 58, 53, 49, 44, 22]

    c_real = 38
    c_guess = 70

    return tp_tn_fp_fn(real, guess, c_real, c_guess)
def various_e():
    TP, TN, FP, FN = dataIn()

    Precision = TP / (TP + FP)
    Recall = TP / (TP + FN)
    True_Negative = TN / (TN + FP)
    Accuracy = (TP + TN) / (TP + TN + FP + FN)
    F1 = 2 / (1 / Recall + 1 / Precision)

    print(Precision, Recall, True_Negative, Accuracy, F1)

various_e()