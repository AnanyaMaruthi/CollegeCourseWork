package com.labs.lab2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void submitForm(View view){
        String name = ((EditText)findViewById(R.id.nameField)).getText().toString();
        String phone = ((EditText)findViewById(R.id.phoneField)).getText().toString();
        String email = ((EditText)findViewById(R.id.emailField)).getText().toString();

        Intent intent = new Intent(getApplicationContext(), DisplayActivity.class);
        Bundle bundle = new Bundle();
        bundle.putString("Name", name);
        bundle.putString("Phone", phone);
        bundle.putString("Email", email);

        intent.putExtras(bundle);
        startActivity(intent);
    }
}
