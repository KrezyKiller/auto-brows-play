def classify(text):
    if text == 'inaap':
        return 'Contains inappropriate words'
    elif text == 'hindi':
        return 'Hindi or other language'
    elif text == 'personal':
        return 'Contains personal details'
    elif text == 'retailers':
        return 'promating outher reatailers'
    elif text == 'offer':
        return 'Discount/offer'
    elif text == 'price':
        return 'price/emi related query'
    elif text == 'return':
        return 'return/replace/exchange'
    elif text == 'delivery':
        return 'shipment/delivary/pin code'
    elif text == 'seller':
        return 'query directly about or to the seller'
    elif text == 'credibility':
        return 'asks about credibility'
    elif text == 'stock':
        return 'stock availablity'
    elif text == 'chart':
        return 'image/size chart related query'
    elif text == 'varient':
        return 'size/color/varient availability'
    elif text == 'after':
        return 'after purchase service/suport releated'
    elif text == 'comparison':
        return 'product comparison'
    elif text == 'warranty':
        return 'warranty realted'
    elif text == 'generic':
        return 'genaric/irrevalent quation'
    elif text == 'bad':
        return 'Bad english'
    elif text == 'valid':
        return 'Valid product related query'
    elif text == 'not':
        return 'Not a question'
