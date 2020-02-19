package com.labs.lab2;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class DisplayActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display);

        Bundle bundle = getIntent().getExtras();

        ((TextView) findViewById(R.id.nameValue)).setText(bundle.getCharSequence("Name"));
        ((TextView) findViewById(R.id.phoneValue)).setText(bundle.getCharSequence("Phone"));
        ((TextView) findViewById(R.id.emailValue)).setText(bundle.getCharSequence("Email"));
    }
}
