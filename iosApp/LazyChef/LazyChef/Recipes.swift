//
//  Recipes.swift
//  LazyChef
//
//  Created by Alice Gamarnik on 4/8/18.
//  Copyright © 2018 Alice Gamarnik. All rights reserved.
//

import Foundation

class Recipes {
    
    var description: String = ""
    var title: String = ""
    var servings: Int = 0
    var hours: Int = 0
    var minutes: Int = 0
    var rankByTime: Bool = false
    enum diet {
        case balanced, highprotein, highfiber, lowfat, lowcarb, lowsodium
    }
    var directions: [String] = []
}

struct Ingredients {
    var ingredients: [String] = []
    enum measurement {
        case grams, milliliters, ounces, pounds, kilograms, gallons
    }
    var quantity: Int = 0
}


