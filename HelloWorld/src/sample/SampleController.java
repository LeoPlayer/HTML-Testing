package sample;

import javafx.event.ActionEvent;
import javafx.scene.control.Label;

import java.util.concurrent.TimeUnit;

public class SampleController {
    public Label helloWorld;
    public Label score;
    private int scoreMark;
    private int score2 = scoreMark + 1;

    public void sayHelloWorld(ActionEvent actionEvent) {
        helloWorld.setText("Hello World!");
        scoreMark = 0;
    }

    public void dontSayHelloWorld(ActionEvent actionEvent) {
        if (scoreMark == 0) {
            helloWorld.setText("");
            scoreMark = 1;
            score.setText(String.valueOf(score2));
            score2 = score2 + 1;
        }
    }

    public void resetScore(ActionEvent actionEvent){
        score.setText(String.valueOf(0));
        scoreMark = 0;
        score2 = 1;
    }
}