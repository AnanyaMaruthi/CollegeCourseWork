package com.labs.lab1;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    int colorCounter = 0;
    int sizeCounter = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


    }

    public void changeFont(View view){
        int[] fontSizes = {20, 30, 40, 50, 60, 70};
        ((TextView)findViewById(R.id.textBox)).setTextSize(TypedValue.COMPLEX_UNIT_PX,fontSizes[sizeCounter]);
        sizeCounter = (sizeCounter + 1) % 5;
    }

    public void changeColor(View view){
        int[] colors = {Color.BLUE, Color.RED, Color.GREEN, Color.CYAN, Color.MAGENTA};
        ((TextView)findViewById(R.id.textBox)).setTextColor(colors[colorCounter]);
        colorCounter = (colorCounter + 1 ) % 5;
    }


}




