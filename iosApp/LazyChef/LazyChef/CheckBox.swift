//
//  CheckBox.swift
//  LazyChef
//
//  Created by Denson George on 4/8/18.
//  Copyright © 2018 Alice Gamarnik. All rights reserved.
//

import UIKit

class CheckBoxButton: UIButton {
    
    let checkedImage = UIImage(named: "check")! as UIImage
    let uncheckedImage = UIImage(named: "unchecked")! as UIImage
    
    override func awakeFromNib() {
        super.awakeFromNib()
        self.clipsToBounds = true
        //TODO: Code for our button
    }
    
    var isChecked: Bool = false {
        didSet{
            if isChecked == true {
                self.setImage(checkedImage, for: UIControlState.normal)
            } else {
                self.setImage(uncheckedImage, for: UIControlState.normal)
            }
        }
    }
    
    func buttonClicked(sender: UIButton) {
        if sender == self {
            isChecked = !isChecked
        }
    }
    
}
