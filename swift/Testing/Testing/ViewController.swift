//
//  ViewController.swift
//  Testing
//
//  Created by Leo Player on 5/2/19.
//  Copyright © 2019 Jenasis290. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    @IBOutlet var adminPassword: NSSecureTextField! //password input
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    @IBAction func sceneOne(_ sender: Any) {
        //go to scene 1
    }
    
    @IBAction func adminEnter(_ sender: Any) {
        if adminPassword.isEqual(to: 1234){
            //go to somewhere
        }
    }
    
}

