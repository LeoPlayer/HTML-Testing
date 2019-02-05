//
//  ViewController.swift
//  Hello World
//
//  Created by Leo Player on 5/2/19.
//  Copyright © 2019 Jenasis290. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    
    @IBOutlet weak var helloLabel: NSTextField!
    @IBOutlet weak var nameField: NSTextField!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    @IBAction func sayButtonClicked(_ sender: Any) {
        var name = nameField.stringValue
        if name.isEmpty {
            name = "World"
        }
        let greeting = "Hello \(name)"
        helloLabel.stringValue = greeting
    }


}

