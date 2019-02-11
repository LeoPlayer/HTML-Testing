package sample;

import javafx.event.ActionEvent;
import javafx.scene.control.Label;

import java.util.concurrent.TimeUnit;

public class SampleController {
    public Label helloWorld;
    public Label score;
    public Label scoreResetMessage;
    public Label spacer;
    private int scoreMark;
    private int score2 = scoreMark + 1;

    public void sayHelloWorld(ActionEvent actionEvent) {
        helloWorld.setText("Hello World!");
        scoreMark = 0;
        spacer.setText(String.valueOf("The score has been reset")); //so the buttons don't glitch left and right
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
        scoreResetMessage.setText("The score has been reset");
        scoreMark = 0;
        score2 = 1;
        try
        {
            TimeUnit.SECONDS.sleep(1000);
            scoreResetMessage.setText("The score has been reset");
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
            scoreResetMessage.setText("Error - sleep text error");
        }
    }
}