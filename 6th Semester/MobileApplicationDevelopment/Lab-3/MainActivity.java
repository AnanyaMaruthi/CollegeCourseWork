package com.labs.lab3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void performOperation(View view){
        int number1, number2;
        try {
            number1 = Integer.parseInt(((EditText) findViewById(R.id.number1)).getText().toString());
            number2 = Integer.parseInt(((EditText) findViewById(R.id.number2)).getText().toString());
        }
        catch(Exception e){
            ((TextView)findViewById(R.id.outputBox)).setText("Please Enter Valid Numbers");
            return ;
        }
        String answer = " " ;
        switch(view.getId()){
            case R.id.add:
                answer = number1 + " + " + number2 + " = " + (number1 + number2);
                break;
            case R.id.sub:
                answer = number1 + " - " + number2 + " = " + (number1 - number2);
                break;
            case R.id.mul:
                answer = number1 + " * " + number2 + " = " + (number1 * number2);
                break;
            case R.id.div:
                if (number2 == 0){
                    answer = "Divisor cannot be 0";
                }
                else{
                    answer = number1 + " / " + number2 + " = " + (number1 / number2);
                }
                break;
        }
        ((TextView)findViewById(R.id.outputBox)).setText(answer);

    }
}
