def accuracy_score(y_true, y_predict, percent=None):
    tp = 0
    for i in range(len(y_true)):
        if y_true[i] == y_predict[i]:
            tp += 1
    return tp / len(y_true)


def precision_score(y_true, y_predict, percent=None):
    tp = 0
    fp = 0
    for i in range(len(y_true)):
        if y_true[i] == y_predict[i]:
            tp += 1
        if y_predict[i] == 1 and y_predict[i] != y_true[i]:
            fp += 1
    return tp / (tp + fp)


def recall_score(y_true, y_predict, percent=None):
    tp = 0
    fn = 0
    for i in range(len(y_true)):
        if y_true[i] == y_predict[i]:
            tp += 1
        if y_predict[i] == 0 and y_predict[i] != y_true[i]:
            fn += 1
    return tp / (tp + fn)


def lift_score(y_true, y_predict, percent=None):
    tp = 0
    fn = 0
    for i in range(len(y_true)):
        if y_true[i] == y_predict[i]:
            tp += 1
        if y_predict[i] == 0 and y_predict[i] != y_true[i]:
            fn += 1
    return len(y_true) * precision_score(y_true, y_predict) / (fn + tp)


def f1_score(y_true, y_predict, percent=None):
    return 2 * precision_score(y_true, y_predict) * recall_score(y_true, y_predict) / \
           (precision_score(y_true, y_predict) + recall_score(y_true, y_predict))








